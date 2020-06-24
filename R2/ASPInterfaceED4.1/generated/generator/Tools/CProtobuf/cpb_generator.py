"""
Brief: This file contains classes for C code generation with a generic extractor
       based on protobuf definitions extended with SystemOptions.

Copyright (c) 2019 Veoneer Sweden AB

Author: Ludwig Ring

Partly based on nanopb by Petteri Aimonen <jpa@kapsi.fi>

All rights reserved. Property of Veoneer Sweden AB.
Restricted rights to use, duplicate or disclose this code are granted through contract.
"""

import sys
from optparse import OptionParser, Values

from Tools.Extension.spp_base import (
    Allocation,
    EnumProtoType,
    EnumDefinition,
    Field,
    Generator,
    GeneratorResult,
    Message,
    ProtoFile,
    Version,
)

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

from Tools.Extension.spp_base import run_generator

pb_version = 1
pb_version_header = f"Protocol Buffers - {pb_version}"

Support.verify_imports()

# Availability checked by verify_imports
import google.protobuf.descriptor_pb2 as descriptor
import Tools.Extension.SystemOptions_pb2 as so

NUMERIC_TYPES = {
    NumericType.I8: "int8_t",
    NumericType.I16: "int16_t",
    NumericType.I32: "int32_t",
    NumericType.I64: "int64_t",
    NumericType.U8: "uint8_t",
    NumericType.U16: "uint16_t",
    NumericType.U32: "uint32_t",
    NumericType.U64: "uint64_t",
    NumericType.BOOL: "bool",
    Fixed32NumericType.FLOAT: "float",
    Fixed64NumericType.DOUBLE: "double",
}

SHORTHAND_PB_TYPES = {
    NumericType.I8: "INT32",
    NumericType.I16: "INT32",
    NumericType.I32: "INT32",
    NumericType.I64: "INT64",
    NumericType.S8: "SINT32",
    NumericType.S16: "SINT32",
    NumericType.S32: "SINT32",
    NumericType.S64: "SINT64",
    NumericType.U8: "UINT32",
    NumericType.U16: "UINT32",
    NumericType.U32: "UINT32",
    NumericType.U64: "UINT64",
}


def get_prototype_tag(proto_type: ProtoType):
    if isinstance(proto_type, ArrayProtoType):
        return get_prototype_tag(proto_type.data_type)
    else:
        return proto_type.id << 3 | proto_type.pbtype


def generate_enum_typedef(enum: EnumDefinition):
    c_type_name = enum.get_full_name().to_string("_")
    enum_min = enum.values[0].get_full_name().to_string("_")
    enum_max = enum.values[-1].get_full_name().to_string("_")

    enum_rows = ",\n".join(
        [
            "    {0} = {1:d}".format(
                enum_value.get_full_name().to_string("_"), enum_value.number
            )
            for enum_value in enum.values
        ]
    )

    code = (
        f"typedef enum _{c_type_name} {{\n"
        + f"{enum_rows}"
        + "\n}"
        + f" {c_type_name};\n"
        + f"#define {c_type_name}_MIN {enum_min}\n"
        + f"#define {c_type_name}_MAX {enum_max}\n"
        + f"#define {c_type_name}_ARRAYSIZE (({c_type_name})({enum_max}+1))\n"
    )

    yield code


class CpbStringProtoType(StringProtoType):
    def __init__(self, field_options: so.SystemFieldOptions, identifier: int):
        super().__init__(field_options, identifier)
        if self.allocation == Allocation.POINTER:
            sys.stderr.write(
                "#### Please note! ####\n"
                "CProtobuf\n"
                "Only encoding of string pointers is supported.\n"
                "This since decoding only sets the pointer to the position in the "
                "receive buffer which is not null terminated.\n"
                "#### End note ####\n"
            )


class CpbField(Field):
    def __init__(
        self,
        parent,
        field_descriptor: descriptor.FieldDescriptorProto,
        field_options: so.SystemFieldOptions,
    ):
        super().__init__(parent, field_descriptor, field_options)
        self.entry_name = self.name[0].lower() + self.name[1:]

    def create_string(self, field_options: so.SystemFieldOptions):
        return CpbStringProtoType(field_options, self.id)

    def handle_dependencies(self, dependencies):
        super().handle_dependencies(dependencies)

        self.ctype = self.get_ctype(self.data_type)

    def generate_struct_entry(self):
        result = ""
        array_decl = ""
        repeated = False

        data_type = self.data_type

        if isinstance(data_type, ArrayProtoType):
            repeated = True
            array_decl = f"[{data_type.max_count}]"
            data_type = data_type.data_type

        if repeated:
            result += f"    pb_size_t {self.entry_name}_count;\n"

        result += f"    /** {self.name}"
        comments = []
        if self.description:
            comments.append(self.description)

        if self.unit:
            comments.append(f"Unit: {self.unit}")

        if hasattr(data_type, "scale") and data_type.scale is not None:
            comments.append(f"Scale: {data_type.scale}")

        if (
            hasattr(data_type, "min")
            and hasattr(data_type, "max")
            and data_type.min is not None
            and data_type.max is not None
        ):
            comments.append(Support.strip_float(f"Min: {data_type.min:g}"))
            comments.append(Support.strip_float(f"Max: {data_type.max:g}"))

        if len(comments) > 0:
            comments.insert(0, "")
            result += "\n     * ".join(comments) + "\n    "
        result += " */\n"

        if data_type.allocation == Allocation.POINTER and isinstance(
            data_type, StringProtoType
        ):
            result += f"    {self.ctype} *{self.entry_name}{array_decl};"
        else:
            if isinstance(data_type, StringProtoType):
                array_decl += f"[{data_type.max_size}]"
            result += f"    {self.ctype} {self.entry_name}{array_decl};"

        return result

    def generate_typedef(self, data_type: ProtoType = None):
        """Return definitions for any special types this field might need."""
        data_type = data_type if data_type else self.data_type

        if (
            isinstance(data_type, BytesProtoType)
            and data_type.allocation == Allocation.STATIC
        ):
            result = f"typedef PB_BYTES_ARRAY_T({data_type.max_size}) {self.ctype};\n"
        elif isinstance(data_type, ArrayProtoType):
            result = self.generate_typedef(data_type.data_type)
        else:
            result = ""
        return result

    def get_ctype(self, data_type: ProtoType):
        ctype = None

        if isinstance(data_type, EnumProtoType):
            ctype = data_type.get_name().replace(".", "_")
        elif data_type.packable:
            ctype = NUMERIC_TYPES[
                Support.get_basic_numeric_type(data_type.numeric_type)
            ]
        elif isinstance(data_type, StringProtoType):
            ctype = "char"
        elif isinstance(data_type, BytesProtoType):
            if data_type.allocation == Allocation.STATIC:
                ctype = "_".join([self.parent.struct_name, self.entry_name, "t"])
            else:
                ctype = "pb_bytes_pointer_t"
        elif isinstance(data_type, MessageProtoType):
            ctype = data_type.get_name().replace(".", "_")
        elif isinstance(data_type, ArrayProtoType):
            ctype = self.get_ctype(data_type.data_type)
        else:
            raise TypeError(
                "ProtoType {} not supported yet".format(data_type.__class__.__name__)
            )
        return ctype

    def get_type(self, data_type: ProtoType):
        pbtype = None

        if isinstance(data_type, FixedProtoType):
            pbtype = str(data_type.numeric_type).split(".")[1]
        elif isinstance(data_type, EnumProtoType):
            pbtype = str(data_type.numeric_type).split(".")[1]
            if data_type.enum_definition.has_negative():
                pbtype = "S" + pbtype
        elif isinstance(data_type, VarintProtoType):
            numeric_type = data_type.numeric_type
            if numeric_type in SHORTHAND_PB_TYPES:
                pbtype = SHORTHAND_PB_TYPES[numeric_type]
            else:
                pbtype = str(data_type.numeric_type).split(".")[1]
        elif isinstance(data_type, StringProtoType):
            pbtype = "STRING"
        elif isinstance(data_type, BytesProtoType):
            pbtype = "BYTES"
        elif isinstance(data_type, MessageProtoType):
            pbtype = "MESSAGE"
        elif isinstance(data_type, ArrayProtoType):
            pbtype = self.get_type(data_type.data_type)
        else:
            raise TypeError(
                "ProtoType {} not supported yet".format(data_type.__class__.__name__)
            )
        return pbtype

    def tags(self):
        """Return the #define for the id number of this field."""
        identifier = "{struct_name}_{name}_identifier".format(
            struct_name=self.parent.struct_name, name=self.name
        )
        return f"#define {identifier:<80} {self.id}\n"

    def pb_field_t(self, prev_field_name, union_index=None):
        """Return the pb_field_t initializer to use in the constant array.
        prev_field_name is the name of the previous field or None.
        """

        tag = get_prototype_tag(self.data_type)

        result = "    PB_FIELD("
        result += f"{self.id:>3}, "
        result += f"{tag:<5}, "
        result += "{size:<5}, ".format(size=Support.varint_max_size(tag))
        result += "{type:<8}, ".format(type=self.get_type(self.data_type))
        result += "{}, ".format(
            "REPEATED" if isinstance(self.data_type, ArrayProtoType) else "OPTIONAL"
        )
        result += "{:<8}, ".format(
            "STATIC" if self.data_type.allocation == Allocation.STATIC else "POINTER"
        )

        if prev_field_name is None:
            result += "FIRST, "
        else:
            result += "OTHER, "

        result += f"{self.parent.struct_name}, "
        result += f"{self.entry_name}, "
        result += "{}, ".format(prev_field_name or self.entry_name)

        if isinstance(self.data_type, MessageProtoType):
            result += "&{name}_fields)".format(
                name=self.data_type.message.get_full_name().to_string("_")
            )
        else:
            result += "0)"

        return result


class CpbMessage(Message):
    def __init__(self, name: str, descriptor, parent, message_options, options):
        super().__init__(name, descriptor, parent, message_options, options)
        self.struct_name = self.get_full_name().to_string("_")

    def create_field(self, field, field_options):
        return CpbField(self, field, field_options)

    def generate_typedef(self):
        result = "".join([f.generate_typedef() for f in self.fields])
        result += f"typedef struct _{self.struct_name} {{\n"

        if not self.ordered_fields:
            # Empty structs are not allowed in C standard.
            # Therefore add a dummy field if an empty message occurs.
            result += "    char dummy_field;"

        result += "\n".join([f.generate_struct_entry() for f in self.ordered_fields])
        result += "\n}"

        result += f" {self.struct_name};"

        return result

    def fields_declaration(self):
        return f"extern const pb_field_t {self.struct_name}_fields[{len(self.fields) + 1}];"

    def fields_definition(self):
        result = (
            f"const pb_field_t {self.struct_name}_fields[{len(self.fields) + 1}] = {{\n"
        )

        prev = None
        for field in self.ordered_fields:
            result += f"{field.pb_field_t(prev)},\n"
            prev = field.entry_name

        result += "    PB_LAST_FIELD\n};"
        return result

    def generate_encoded_size(self):
        result = ""
        msize = self.get_encoded_size()
        if msize is not None:
            submessage_exist = any(
                isinstance(x.data_type, MessageProtoType) for x in self.fields
            )
            if submessage_exist:
                msize = EncodedSize()
                for field in self.fields:
                    fieldsize = field.get_encoded_size()
                    if isinstance(field.data_type, MessageProtoType):
                        msize += field.data_type.message.struct_name + "_size"
                        msize += Support.varint_max_size(field.id << 3)
                        msize += Support.varint_max_size(fieldsize.upperlimit())
                    else:
                        msize += fieldsize

            identifier = f"{self.struct_name}_size"

            extra = " + PB_VARINT_MAX_ENCODED_SIZE" if submessage_exist else ""
            result += f"#define {identifier:<80} ({msize}{extra})\n"
            # PB_VARINT_MAX_ENCODED_SIZE is added since we shift the result when writing a message to
            # be able to go back and add the size
        else:
            identifier = f"{self.struct_name}_static_size"
            result += f"/* {identifier} depends on runtime parameters */\n"
            result += (
                f"#define {identifier:<80} {self.get_encoded_size_static_only()}\n"
            )
        return result

    def generate_header_misc(self):
        result = ""
        if self.source:
            source = f"{self.struct_name}_source"
            result += f"#define {source:<80} {self.source}U\n"
        if self.identifier:
            identifier = f"{self.struct_name}_identifier"
            result += f"#define {identifier:<80} {self.identifier}U\n"
        if self.version:
            result += "#define {name:<80} {version}U\n".format(
                name=f"{self.struct_name}_majorVersion", version=self.version.major
            )
            result += "#define {name:<80} {version}U\n".format(
                name=f"{self.struct_name}_minorVersion", version=self.version.minor
            )
        return result


class CpbProtoFile(ProtoFile):
    def __init__(
        self,
        fdesc: descriptor.FileDescriptorProto,
        options: Values,
        spp_version: Version,
    ):
        """Takes a file, file descriptor and options to generate a CpbProtoFile."""
        super().__init__(fdesc, options, spp_version)
        self.includes = []

    def create_message(self, name, message, parent, message_options):
        return CpbMessage(name, message, parent, message_options, self.options)

    def add_dependency(self, other):
        super().add_dependency(other)

        if other.get_target_base() != self.get_target_base():
            self.includes.append(other.get_target_base())

    def generate_header(self, options: Values):
        """Generate content for a header file.
        Generates strings, which should be concatenated and stored to file.
        """

        yield "/* Automatically generated pb header */\n"
        yield f"/* Generated by {pb_version_header} */\n\n"

        include_guard = "{}_INCLUDED".format(
            Support.make_c_identifier(self.get_target_base())
        )
        yield f"#ifndef {include_guard}\n"
        yield f"#define {include_guard}\n"
        yield Support.c_include("Tools/CProtobuf/pb.h")
        yield Support.c_include("Tools/CProtobuf/pb_decode.h")
        yield Support.c_include("Tools/CProtobuf/pb_encode.h")
        yield "\n"

        for incfile in self.includes:
            yield Support.c_include(incfile + ".cpb.h")

        yield f"#if PB_PROTO_HEADER_VERSION != {pb_version}\n"
        yield "#error Regenerate this file with the current version of pb generator.\n"
        yield "#endif\n"
        yield "\n"

        yield "#ifdef __cplusplus\n"
        yield 'extern "C" {\n'
        yield "#endif\n\n"

        if self.messages:
            yield "/* Maximum encoded size of messages (where known) */\n"
            for msg in Support.sort_dependencies(self.messages):
                yield msg.generate_encoded_size()
            yield "\n"

            yield '/* Message IDs (where set with "identifier" option) */\n'
            for msg in self.messages:
                yield msg.generate_header_misc()
            yield "\n"

        if self.enums:
            yield "/* Enum definitions */\n"
            for enum in self.enums:
                yield "".join(generate_enum_typedef(enum))
                yield "\n"

        if self.messages:
            yield "/* Struct definitions */\n"
            for msg in Support.sort_dependencies(self.messages):
                yield msg.generate_typedef() + "\n\n"

            yield "/* Struct field encoding specification for pb */\n"
            for msg in self.messages:
                yield msg.fields_declaration()
                yield "\n"

        yield "#ifdef __cplusplus\n"
        yield '} /* extern "C" */\n'
        yield "#endif\n"

        # End of header
        yield f"\n#endif /* {include_guard} */\n"

    def generate_source(self, options: Values):
        """Generate content for a source file."""

        yield "/* Automatically generated pb constant definitions */\n"
        yield f"/* Generated by {pb_version_header} */\n\n"
        yield Support.c_include(self.get_target_base() + ".cpb.h")
        yield "\n"

        yield f"#if PB_PROTO_HEADER_VERSION != {pb_version}\n"
        yield "#error Regenerate this file with the current version of pb generator.\n"
        yield "#endif\n"
        yield "\n"

        for msg in self.messages:
            yield msg.fields_definition() + "\n\n"

        # Add check for sizeof(double)
        has_double = False
        for msg in self.messages:
            for field in msg.fields:
                if (
                    isinstance(field.data_type, Fixed64ProtoType)
                    and field.data_type.numeric_type == Fixed64NumericType.DOUBLE
                ):
                    has_double = True

        if has_double:
            yield "/* On some platforms (such as AVR), double is really float.\n"
            yield " * These are not directly supported by pb.\n"
            yield " * To get rid of this error, remove any double fields from your .proto.\n"
            yield " */\n"
            yield "PB_STATIC_ASSERT(sizeof(double) == 8, DOUBLE_MUST_BE_8_BYTES)\n"


class CpbGenerator(Generator):
    def create_proto_file(self, fdesc: descriptor.FileDescriptorProto):
        return CpbProtoFile(fdesc, self.options, self.spp_version)

    def generate_result(self):
        result = []
        base_name = "{}.cpb".format(self.proto_file.get_target_base())
        header_name = f"{base_name}.h"
        source_name = f"{base_name}.c"
        header = GeneratorResult(
            header_name, "".join(self.proto_file.generate_header(self.options))
        )
        source = GeneratorResult(
            source_name, "".join(self.proto_file.generate_source(self.options))
        )
        result.append(header)
        result.append(source)

        return result


def main(plugin: bool = True):
    generator = CpbGenerator()
    optparser = OptionParser()

    run_generator(generator, optparser, plugin)
