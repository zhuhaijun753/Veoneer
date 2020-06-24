from __future__ import unicode_literals

"""
Brief: This file contains base classes for System Products Protocol generation
       based on protobuf definitions extended with SystemOptions.
       The design intent is that a generator is created in a separate file and
       inherit from the base classes to create a complete generator.

Copyright (c) 2019 Veoneer Sweden AB

Author: Ludwig Ring

All rights reserved. Property of Veoneer Sweden AB.
Restricted rights to use, duplicate or disclose this code are granted through contract.
"""

spp_version = "System Products Protocol Generator - 1.0"

from optparse import OptionParser, Values
import copy
import sys
import os.path
import io
import shlex
from enum import Enum

from Tools.Extension.spp_prototypes import (
    ArrayProtoType,
    BoolProtoType,
    BytesProtoType,
    ProtoType,
    EnumProtoType,
    FixedProtoType,
    Fixed32ProtoType,
    Fixed64ProtoType,
    MessageProtoType,
    StringProtoType,
    VarintProtoType,
)

import Tools.Extension.spp_support as Support
from Tools.Extension.spp_support import (
    Allocation,
    EncodedSize,
    NumericType,
    Fixed32NumericType,
    Fixed64NumericType,
)

try:
    # Add some dummy imports to keep packaging tools happy.
    import google
except BaseException:
    # Don't care, we will error out later if it is actually
    # important.
    pass

Support.verify_imports()

# Availability checked by verify_imports
import google.protobuf.descriptor_pb2 as descriptor
import google.protobuf.compiler.plugin_pb2 as plugin

import Tools.Extension.SystemOptions_pb2 as so
import Tools.Extension.DataSources_pb2 as ds
import Tools.Extension.SystemProductsProtocolVersion_pb2 as spp_file_version

"""
Supported SPP Format Versions
"""
SUPPORTED_SPP_VERSIONS = {
    # Major: [Minor, ...]
    2: [0]
}

FieldD = descriptor.FieldDescriptorProto


def get_so_suboptions(subdesc):
    """Get copy of options, and merge information from subdesc."""
    new_options = None
    # Handle options defined in .proto
    if isinstance(subdesc.options, descriptor.EnumOptions):
        ext_type = so.system_enum_options
        new_options = so.SystemEnumOptions()
    elif isinstance(subdesc.options, descriptor.FieldOptions):
        ext_type = so.system_field_options
        new_options = so.SystemFieldOptions()
    elif isinstance(subdesc.options, descriptor.FileOptions):
        ext_type = so.system_file_options
        new_options = so.SystemFileOptions()
    elif isinstance(subdesc.options, descriptor.MessageOptions):
        ext_type = so.system_message_options
        new_options = so.SystemMessageOptions()
    else:
        raise TypeError("Unknown options type")
    if subdesc.options.HasExtension(ext_type):
        ext = subdesc.options.Extensions[ext_type]
        new_options.MergeFrom(ext)
    return new_options


class Version:
    def __init__(self, major: int, minor: int, patch: int):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __str__(self):
        return "{}.{}.{}".format(self.major, self.minor, self.patch)


class SppParentGuarantees:
    """Used to make sure EnumDefinition parent input has the two
       functions below available
    """

    def get_package(self):
        raise NotImplementedError("Implement me")

    def get_full_name(self):
        raise NotImplementedError("Implement me")


class EnumValue:
    def __init__(self, parent: "EnumDefinition", number: int, name: str):
        self.parent = parent
        self.number = number
        self.name = name

    def get_full_name(self):
        return self.parent.get_full_name() + self.name


class EnumDefinition:
    def __init__(
        self,
        name: str,
        descriptor: descriptor.EnumDescriptorProto,
        parent: SppParentGuarantees,
        enum_options: descriptor.EnumOptions,
    ):
        self.name = name
        self.parent = parent
        self.description = None
        if enum_options.description != "":
            self.description = enum_options.description

        values_dict = {}
        for x in descriptor.value:
            values_dict[x.number] = self.create_enum_value(x.number, x.name)

        self.values = [values_dict[x] for x in sorted(values_dict)]
        self.encoded_size = EncodedSize(
            max(
                [
                    Support.varint_max_size(enum_value.number)
                    for enum_value in self.values
                ]
            )
        )
        self.min_value = min([enum_value.number for enum_value in self.values])
        self.max_value = max([enum_value.number for enum_value in self.values])

    def create_enum_value(self, number: int, name: str):
        return EnumValue(self, number, self.remove_type_from_name(name))

    def remove_type_from_name(self, value_name):
        value_name = Support.snake_case_to_pascal_case(value_name.lower())
        value_name = value_name.replace(self.name, "")
        return value_name

    def has_negative(self):
        for enum_value in self.values:
            if enum_value.number < 0:
                return True
        return False

    def get_package(self):
        return self.parent.get_package()

    def get_full_name(self):
        return self.parent.get_full_name() + self.name


class Field:
    def __init__(
        self, parent, descriptor: FieldD, field_options: so.SystemFieldOptions
    ):
        """desc is FieldDescriptorProto"""
        self.id = descriptor.number
        self.parent = parent
        self.type_name = None
        if descriptor.type_name != "":
            self.type_name = descriptor.type_name[1:]
        self.raw_name = descriptor.name
        self.name = Support.snake_case_to_pascal_case(descriptor.name)
        self.data_type = None

        self.unit = field_options.unit
        self.description = field_options.description

        try:
            self.data_type = self.create_data_type(descriptor, field_options)
        except Exception as err:
            raise Exception(
                f"Error creating field {self.parent.name}.{self.name}. {err}"
            )

    def create_string(self, field_options: so.SystemFieldOptions):
        return StringProtoType(field_options, self.id)

    def create_enum(self, field_options: so.SystemFieldOptions, type_name: str):
        return EnumProtoType(field_options, self.id, type_name)

    def create_bytes(self, field_options: so.SystemFieldOptions):
        return BytesProtoType(field_options, self.id)

    def create_message(self, field_options: so.SystemFieldOptions, type_name: str):
        return MessageProtoType(field_options, self.id, type_name)

    def create_bool(self, field_options: so.SystemFieldOptions):
        return BoolProtoType(field_options, self.id)

    def create_fixed32(
        self, field_options: so.SystemFieldOptions, fixed32_type: Fixed32NumericType
    ):
        return Fixed32ProtoType(field_options, self.id, fixed32_type)

    def create_fixed64(
        self, field_options: so.SystemFieldOptions, fixed64_type: Fixed64NumericType
    ):
        return Fixed64ProtoType(field_options, self.id, fixed64_type)

    def create_varint(
        self, field_options: so.SystemFieldOptions, numeric_type: NumericType
    ):
        return VarintProtoType(field_options, self.id, numeric_type)

    def create_array(self, field_options: so.SystemFieldOptions, data_type: ProtoType):
        return ArrayProtoType(field_options, self.id, data_type)

    def create_data_type(
        self, field_descriptor: FieldD, field_options: so.SystemFieldOptions
    ):
        data_type = None

        fixed32_mapping = {
            FieldD.TYPE_FIXED32: Fixed32NumericType.FIXED32,
            FieldD.TYPE_SFIXED32: Fixed32NumericType.SFIXED32,
            FieldD.TYPE_FLOAT: Fixed32NumericType.FLOAT,
        }
        fixed64_mapping = {
            FieldD.TYPE_FIXED64: Fixed64NumericType.FIXED64,
            FieldD.TYPE_SFIXED64: Fixed64NumericType.SFIXED64,
            FieldD.TYPE_DOUBLE: Fixed64NumericType.DOUBLE,
        }
        varint_conversion = {
            FieldD.TYPE_INT32: NumericType.I32,
            FieldD.TYPE_INT64: NumericType.I64,
            FieldD.TYPE_SINT32: NumericType.S32,
            FieldD.TYPE_SINT64: NumericType.S64,
            FieldD.TYPE_UINT32: NumericType.U32,
            FieldD.TYPE_UINT64: NumericType.U64,
        }

        if field_descriptor.type == FieldD.TYPE_STRING:
            data_type = self.create_string(field_options)
        elif field_descriptor.type == FieldD.TYPE_ENUM:
            data_type = self.create_enum(field_options, self.type_name)
        elif field_descriptor.type == FieldD.TYPE_BYTES:
            data_type = self.create_bytes(field_options)
        elif field_descriptor.type == FieldD.TYPE_MESSAGE:
            data_type = self.create_message(field_options, self.type_name)
        elif field_descriptor.type == FieldD.TYPE_BOOL:
            data_type = self.create_bool(field_options)
        elif field_descriptor.type in fixed32_mapping:
            data_type = self.create_fixed32(
                field_options, fixed32_mapping[field_descriptor.type]
            )
        elif field_descriptor.type in fixed64_mapping:
            data_type = self.create_fixed64(
                field_options, fixed64_mapping[field_descriptor.type]
            )
        elif field_descriptor.type in varint_conversion:
            data_type = self.create_varint(
                field_options, varint_conversion[field_descriptor.type]
            )

        if data_type and field_descriptor.label == FieldD.LABEL_REPEATED:
            data_type = self.create_array(field_options, data_type)

        if data_type:
            return data_type
        else:
            raise Exception("Unsupported Data Type")

    def __lt__(self, other):
        return self.id < other.id

    def handle_dependencies(self, dependencies):
        self.data_type.handle_dependencies(dependencies)

        if self.data_type.allocation == Allocation.STATIC:
            if not self.data_type.encoded_size:
                raise RuntimeError(
                    "Could not determine encoded size for {}.{}".format(
                        self.parent.get_full_name(), self.name
                    )
                )

    def get_dependencies(self):
        """Get list of type names used by this field."""
        if self.data_type.allocation == Allocation.STATIC:
            return [self.data_type.get_name()]
        else:
            return []

    def get_encoded_size(self):
        return self.data_type.get_encoded_size()

    def get_package(self):
        return self.parent.get_package()

    def get_full_name(self):
        return self.parent.get_full_name() + self.name


class Message(SppParentGuarantees):
    def __init__(self, name: str, descriptor, parent, message_options, options):
        self.name = name
        self.fields = []
        self.source = None
        self.identifier = None
        self.description = None
        self.version = None
        major = None
        minor = 0
        patch = 0
        self.parent = parent
        self.dependencies_handled = False

        if message_options.source != 0:
            self.source = message_options.source

        if message_options.identifier != 0:
            self.identifier = message_options.identifier

        if message_options.description != "":
            self.description = message_options.description

        if message_options.major_version != 0:
            major = message_options.major_version

        if message_options.minor_version != 0:
            minor = message_options.minor_version

        if message_options.patch_version != 0:
            patch = message_options.patch_version

        if major is not None:
            self.version = Version(major, minor, patch)

        self.parse(descriptor, options)

    def create_field(self, field, field_options):
        return Field(self, field, field_options)

    def parse(self, descriptor, options):
        for f in descriptor.field:
            field_options = get_so_suboptions(f)

            field = self.create_field(f, field_options)
            self.fields.append(field)

        self.ordered_fields = self.fields[:]
        self.ordered_fields.sort()

    def handle_dependencies(self, dependencies):
        """Process all dependencies to initialize all fields correctly"""
        if not self.dependencies_handled:
            for field in self.fields:
                field.handle_dependencies(dependencies)
            self.dependencies_handled = True

    def get_dependencies(self):
        """Get list of type names that this structure refers to."""
        deps = []
        for f in self.fields:
            deps += f.get_dependencies()
        return deps

    def get_package(self):
        return self.parent.get_package()

    def get_full_name(self):
        return self.parent.get_full_name() + self.name

    def get_encoded_size(self):
        """Return the maximum size that this message can take when encoded.
        If the size cannot be determined, returns None.
        """
        size = EncodedSize(0)
        for field in self.fields:
            fsize = field.get_encoded_size()
            if fsize is None:
                return None
            size += fsize

        return size

    def get_encoded_size_static_only(self):
        """Return the maximum size that this message can take when encoded.
        Only statically allocated parts are considered.
        """
        size = EncodedSize(0)
        for field in self.fields:
            fsize = field.get_encoded_size()
            if fsize != None:
                size += fsize
            else:
                size += field.data_type.get_tag_size()

        return size


class ProtoFile(SppParentGuarantees):
    def __init__(
        self,
        fdesc: descriptor.FileDescriptorProto,
        options: Values,
        spp_file_version: Version,
    ):
        """Takes a file, file descriptor and options to generate a ProtoFile."""
        if not fdesc:
            data = open(file_with_path, "rb").read()
            fdesc = descriptor.FileDescriptorSet.FromString(data).file[0]

        # Parse the file
        file_options = get_so_suboptions(fdesc)
        self.spp_version = spp_file_version
        self.path, name_ext = os.path.split(fdesc.name)
        self.filename = os.path.splitext(name_ext)[0]
        self.target_base = os.path.splitext(fdesc.name)[0]
        self.fdesc = fdesc
        self.file_options = file_options
        self.options = options
        self.dependencies = {}

        self.parse()

        # Some of types used in this file probably come from the file itself.
        # Thus it has implicit dependency on itself.
        self.add_dependency(self)

    @staticmethod
    def iterate_messages(desc, parent_names):
        """Recursively find all messages. For each, yield name, parent name, DescriptorProto."""
        if hasattr(desc, "message_type"):
            submsgs = desc.message_type
        else:
            submsgs = desc.nested_type

        for submsg in submsgs:
            yield submsg.name, parent_names, submsg

            sub_parent_names = parent_names + submsg.name

            for x in ProtoFile.iterate_messages(submsg, sub_parent_names):
                yield x

    def create_enum(self, name, enum, parent, enum_options):
        return EnumDefinition(name, enum, parent, enum_options)

    def create_message(self, name, message, parent, message_options):
        return Message(name, message, parent, message_options, self.options)

    def parse(self):
        self.enums = []
        self.messages = []

        for enum in self.fdesc.enum_type:
            enum_options = get_so_suboptions(enum)
            spp_enum = self.create_enum(enum.name, enum, self, enum_options)
            if spp_enum:
                self.enums.append(spp_enum)

        message_dict = {}

        for name, parent_name, message in ProtoFile.iterate_messages(
            self.fdesc, Support.Names()
        ):
            message_options = get_so_suboptions(message)

            message = copy.deepcopy(message)
            parent = self
            # Find parent message if this is a child message
            if not parent_name.empty():
                parent_str = str(self.get_package() + parent_name)
                if parent_str in message_dict:
                    parent = message_dict[parent_str]
                else:
                    raise Exception(
                        f"Parent message {parent_name} not found for message {name}"
                    )

            spp_message = self.create_message(name, message, parent, message_options)
            if spp_message:
                self.messages.append(spp_message)
                message_dict[str(spp_message.get_full_name())] = spp_message

            for enum in message.enum_type:
                enum_options = get_so_suboptions(enum)
                spp_enum = self.create_enum(enum.name, enum, spp_message, enum_options)
                if spp_enum:
                    self.enums.append(spp_enum)

    def get_package(self):
        return (
            Support.Names(self.fdesc.package.split("."))
            if self.fdesc.package != ""
            else Support.Names()
        )

    def get_full_name(self):
        return self.get_package()

    def get_target_base(self):
        return self.target_base

    def add_dependency(self, other):
        for enum in other.enums:
            self.dependencies[str(enum.get_full_name())] = enum
            enum.protofile = other

        for msg in other.messages:
            self.dependencies[str(msg.get_full_name())] = msg
            msg.protofile = other

    def handle_dependencies(self):
        for message in self.messages:
            message.handle_dependencies(self.dependencies)


class GeneratorResult:
    def __init__(self, name, data):
        self.name = name
        self.data = data


class Generator:
    """Base for creating a custom generator"""

    def __init__(self):
        self.other_files = {}
        self.proto_file = None
        self.options = Values()

        spp_format_version = so.DESCRIPTOR.GetOptions().Extensions[
            spp_file_version.spp_file_version
        ]
        self.spp_version = Version(
            spp_format_version.major, spp_format_version.minor, spp_format_version.patch
        )

        self.check_spp_version(self.spp_version)

    def check_spp_version(self, version: Version):
        """This function should be overridden by inheriting class if additional
        support checks are needed
        """

        # Check SPP Format Version
        if (
            not version.major in SUPPORTED_SPP_VERSIONS
            or not version.minor in SUPPORTED_SPP_VERSIONS[version.major]
        ):
            raise Exception(f"SPP format {version} not supported by Base generator")

    def create_proto_file(self, fdesc: descriptor.FileDescriptorProto):
        """This function should be overridden by custom generator
           if a custom protofile is needed
        """

        return ProtoFile(descriptor, self.options, self.spp_version)

    def generate_result(self):
        """This function should be overridden by custom generator"""

        raise NotImplementedError("This function needs to be implemented")

    def process_file(self, fdesc):
        """This function should not be overridden by custom generator"""

        self.proto_file = self.create_proto_file(fdesc)
        for dep in self.proto_file.fdesc.dependency:
            if dep in self.other_files:
                self.proto_file.add_dependency(self.other_files[dep])
        self.proto_file.handle_dependencies()

        return self.generate_result()

    def add_other_file(self, fdesc):
        """This function should not be overridden by custom generator"""

        self.other_files[fdesc.name] = self.create_proto_file(fdesc)

    def set_options(self, options: Values):
        """This function can be overridden by custom generator if needed"""

        self.options = options


def add_base_options(optparser: OptionParser):
    """This function should be called by custom generator"""

    optparser.add_option(
        "-D",
        "--output-dir",
        dest="output_dir",
        metavar="OUTPUTDIR",
        default=None,
        help="Output directory of files",
    )
    optparser.add_option(
        "-p",
        "--package-in-name",
        dest="package_in_name",
        default=False,
        help="Determines if package name should be used for generated file. [default: %default]",
    )
    optparser.add_option(
        "-w",
        "--separator",
        dest="separator",
        metavar="EXTENSION",
        default=".",
        help="Separating string used between package names. [default: %default]",
    )


def main_cli(generator: Generator, optparser: OptionParser):
    """Main function when invoked directly from the command line."""

    options, filenames = optparser.parse_args()
    generator.set_options(options)

    if not filenames:
        optparser.print_help()
        sys.exit(1)

    if options.output_dir and not os.path.exists(options.output_dir):
        optparser.print_help()
        sys.stderr.write("\noutput_dir does not exist: {\}n".format(options.output_dir))
        sys.exit(1)

    base_dir = options.output_dir or ""
    for filename in filenames:
        with open(filename, "rb") as input_file:
            data = input_file.read()
            fdesc = descriptor.FileDescriptorSet.FromString(data).file[0]
            for generated_file in generator.process_file(fdesc):
                # TODO: Create dir if needed
                path = os.path.join(base_dir, generated_file.name)
                with open(path, "w") as f:
                    f.write(generated_file.data)


def main_plugin(generator: Generator, optparser: OptionParser):
    """Main function when invoked as a protoc plugin."""

    if sys.platform == "win32":
        import os, msvcrt

        # Set stdin and stdout to binary mode
        msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)
        msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)

    data = io.open(sys.stdin.fileno(), "rb").read()
    request = plugin.CodeGeneratorRequest.FromString(data)

    try:
        # Versions of Python prior to 2.7.3 do not support unicode
        # input to shlex.split(). Try to convert to str if possible.
        params = str(request.parameter)
    except UnicodeEncodeError:
        params = request.parameter

    args = shlex.split(params)

    if len(args) == 1 and "," in args[0]:
        # Protoc plugins separete options by comma.
        lex = shlex.shlex(params)
        lex.whitespace_split = True
        lex.whitespace = ","
        args = list(lex)

    optparser.usage = (
        "Usage: protoc --spp_out='[options],[more_options]':outdir file.proto"
    )
    optparser.epilog = "Output will be written based on selected options."

    # By default optparser prints help to stdout, which doesn't work for
    # protoc plugins.
    if "-h" in args or "--help" in args:
        optparser.print_help(sys.stderr)
        sys.exit(1)

    options, dummy = optparser.parse_args(args)
    generator.set_options(options)

    excluded_files = [
        "google/protobuf/descriptor.proto",
        "SystemOptions.proto",
        "SystemProductsProtocolVersion.proto",
    ]

    for fdesc in request.proto_file:
        if not any(fdesc.name.endswith(f) for f in excluded_files):
            generator.add_other_file(fdesc)

    response = plugin.CodeGeneratorResponse()

    for filename in request.file_to_generate:
        for fdesc in request.proto_file:
            if fdesc.name == filename:
                for generated_file in generator.process_file(fdesc):
                    f = response.file.add()
                    f.name = generated_file.name
                    f.content = generated_file.data

    io.open(sys.stdout.fileno(), "wb").write(response.SerializeToString())


def run_generator(generator: Generator, optparser: OptionParser, plugin: bool):
    """This function should be called by custom generator"""

    add_base_options(optparser)
    # Check if we are running as a plugin under protoc
    if plugin:
        main_plugin(generator, optparser)
    else:
        optparser.usage = "{} [options] file.pb ...".format(
            os.path.split(sys.argv[0])[1]
        )
        optparser.epilog = (
            "Compile file.pb from file.proto by: 'protoc -ofile.pb file.proto'. "
        )
        main_cli(generator, optparser)
