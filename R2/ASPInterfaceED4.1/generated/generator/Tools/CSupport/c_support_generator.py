"""
Brief: This file contains classes for C code generation of Support files
       based on protobuf definitions extended with SystemOptions.

Copyright (c) 2019 Veoneer Sweden AB

Author: Ludwig Ring

All rights reserved. Property of Veoneer Sweden AB.
Restricted rights to use, duplicate or disclose this code are granted through contract.
"""

from optparse import OptionParser, Values
import sys

import Tools.CSupport.c_support as CSupport

import Tools.Extension.spp_support as Support
from Tools.Extension.spp_support import Names, NumericType

from Tools.Extension.spp_base import (
    ArrayProtoType,
    ProtoType,
    EncodedSize,
    Enum,
    Field,
    Generator,
    GeneratorResult,
    VarintProtoType,
    Message,
    ProtoFile,
)

from Tools.Extension.spp_base import run_generator

Support.verify_imports()

# Availability checked by verify_imports
import google.protobuf.descriptor_pb2 as descriptor

import Tools.Extension.DataSources_pb2 as ds

c_support_version = 1
c_support_version_header = f"C Conversion Support - {c_support_version}"

NUMERIC_TYPES = {
    NumericType.I8: "int8_t",
    NumericType.I16: "int16_t",
    NumericType.I32: "int32_t",
    NumericType.I64: "int64_t",
    NumericType.U8: "uint8_t",
    NumericType.U16: "uint16_t",
    NumericType.U32: "uint32_t",
    NumericType.U64: "uint64_t",
}


class CSupportField(Field):
    def __init__(self, parent, descriptor, field_options):
        super().__init__(parent, descriptor, field_options)

    def get_data_type(self, data_type: ProtoType = None):
        # Get the source datatype, so if it is an array get the subtype
        data_type = data_type if data_type else self.data_type
        if isinstance(data_type, ArrayProtoType):
            return self.get_data_type(data_type.data_type)

        return data_type

    def has_support_code(self):
        data_type = self.get_data_type()
        return hasattr(data_type, "scale") and data_type.scale != None

    def conversion_functions(self, include_code=False):
        """Return conversion functions for field ."""
        result = ""

        if self.has_support_code():
            data_type = self.get_data_type()
            struct_name = self.parent.get_full_name().to_string("_")
            float_define = CSupport.float_define(data_type.scale)
            ctype = NUMERIC_TYPES[
                Support.get_basic_numeric_type(data_type.numeric_type)
            ]
            result += f"float {struct_name}_{self.name[0].lower() + self.name[1:]}ToFloat(const {ctype} value)"
            if include_code:
                result += "\n{\n"
                result += f"   return value * {float_define};\n"
                result += "}\n\n"
            else:
                result += ";\n"

            result += f"{ctype} {struct_name}_floatTo{self.name[0].upper() + self.name[1:]}(const float value)"

            if include_code:
                result += "\n{\n"
                convert_call = CSupport.get_float_to_int_convert_call(
                    ctype, "value", float_define
                )
                result += f"   return {convert_call};\n"
                result += "}\n"
            else:
                result += ";\n"

        return result


class CSupportMessage(Message):
    def __init__(self, name: str, descriptor, parent, message_options, options):
        super().__init__(name, descriptor, parent, message_options, options)

    def create_field(self, field, field_options):
        return CSupportField(self, field, field_options)


class CSupportProtoFile(ProtoFile):
    def create_enum(self, name, enum, parent, enum_options):
        return None

    def create_message(self, name, message, parent, message_options):
        return CSupportMessage(name, message, parent, message_options, self.options)

    def has_support_code(self):
        if self.messages:
            return any(
                any(f.has_support_code() for f in m.fields) for m in self.messages
            )

        return False

    def generate_header(self, options):
        """Generate content for a header file.
        Generates strings, which should be concatenated and stored to file.
        """
        yield "/* Automatically generated Extension Support header */\n"
        yield f"/* SPP version {self.spp_version} */\n"
        yield f"/* Generated by {c_support_version_header} */\n\n"

        include_guard = "SUPPORT_{}_INCLUDED".format(
            Support.make_c_identifier(self.get_target_base())
        )
        yield f"#ifndef {include_guard}\n"
        yield f"#define {include_guard}\n"
        yield "\n"
        yield Support.c_library_include("stdint.h")
        yield "\n"
        yield "#ifdef __cplusplus\n"
        yield 'extern "C" {\n'
        yield "#endif\n\n"

        if self.messages:
            yield "/* Conversion functions */\n"
            for msg in self.messages:
                for field in msg.fields:
                    yield field.conversion_functions()

        yield "\n"
        yield "#ifdef __cplusplus\n"
        yield '} /* extern "C" */\n'
        yield "#endif\n"
        yield "\n"
        yield f"#endif /* {include_guard} */\n"

    def generate_source(self, options):
        """Generate content for a source file."""

        yield "/* Automatically generated Extension Support code */\n"
        yield f"/* SPP version {self.spp_version} */\n"
        yield f"/* Generated by {c_support_version_header} */\n\n"
        yield Support.c_include("Tools/CSupport/ConversionSupport.h")
        yield Support.c_include(self.get_target_base() + ".support.h")

        if self.messages:
            float_defines = {}
            for msg in self.messages:
                for field in msg.fields:
                    if field.has_support_code():
                        data_type = field.get_data_type()
                        scale = float(data_type.scale)
                        if scale not in float_defines:
                            float_define = CSupport.float_define(data_type.scale)
                            float_defines[
                                scale
                            ] = f"#define {float_define:<20} {data_type.scale}f\n"

            yield "\n/* Defines */\n"
            for key, define_str in sorted(float_defines.items()):
                yield define_str

            yield "\n"
            yield "/* Conversion functions */\n"
            for msg in self.messages:
                for field in msg.fields:
                    if field.has_support_code():
                        yield field.conversion_functions(True)


class CSupportGenerator(Generator):
    def create_proto_file(self, fdesc: descriptor.FileDescriptorProto):
        return CSupportProtoFile(fdesc, self.options, self.spp_version)

    def generate_result(self):
        result = []
        if self.proto_file.has_support_code():
            base_name = "{}.support".format(self.proto_file.get_target_base())
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
    generator = CSupportGenerator()
    optparser = OptionParser()

    run_generator(generator, optparser, plugin)
