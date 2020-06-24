"""
Brief: This file contains classes for C code generation of Quick Protocol Buffers
       based on protobuf definitions extended with SystemOptions.

Copyright (c) 2020 Veoneer Sweden AB

Author: Ludwig Ring

All rights reserved. Property of Veoneer Sweden AB.
Restricted rights to use, duplicate or disclose this code are granted through contract.
"""

import sys
from optparse import OptionParser, Values

import Tools.CSupport.c_support as CSupport

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

Support.verify_imports()

# Availability checked by verify_imports
import google.protobuf.descriptor_pb2 as descriptor

import Tools.Extension.SystemOptions_pb2 as so

qpb_version = 2
qpb_version_header = f"Quick Protocol Buffers - {qpb_version}"

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


def write_tag(indentation: str, identifier: int, tag: int):
    if identifier < 16:
        yield indentation + f"*stream->buffer = {tag};\n"
        yield indentation + "++stream->buffer;\n"
    else:
        yield indentation + f"qpb_encode_varint(stream, {tag});\n"


def create_array_index(struct_name: str, name: str):
    return f"[(({struct_name}*)data)->{name}_count++]"


def create_function_name(field: "QpbField", raw: bool, function_type: str):
    return f"{function_type}_{field.parent.get_struct_name(raw)}_{field.entry_name}"


def create_varint_function(numeric_type: NumericType, decode: bool = False):
    function = "varint"
    if numeric_type.name.startswith("S"):
        function = "s" + function
    elif numeric_type.name.startswith("U"):
        function = "u" + function

    return function


def create_packable_start(array: bool):
    return "result =" if array else "return"


def write_zero_check(indentation: str, name: str, identifier: int, tag: int):
    yield f"{indentation}if (*data != 0)\n"
    yield f"{indentation}{{\n"
    yield "".join(write_tag(indentation + "   ", identifier, tag))


def generate_tag_and_shift(indentation: str, identifier: int, tag: int):
    yield "".join(write_tag(indentation, identifier, tag))
    yield indentation + "sizePtr = stream->buffer;\n"
    yield indentation + "stream->buffer += QPB_VARINT_MAX_ENCODED_SIZE;\n"
    yield indentation + "dataPtr = stream->buffer;\n"


def generate_size_and_shift(indentation: str):
    yield indentation + "/* Check size of encoded message and write size at the appropriate offset */\n"
    yield indentation + "size = (stream->buffer - dataPtr);\n"
    yield indentation + "stream->buffer = sizePtr;\n"
    yield indentation + "qpb_encode_varint(stream, (qpb_uint64_t)size);\n"
    yield indentation + "dataToClear = QPB_VARINT_MAX_ENCODED_SIZE - (stream->buffer - sizePtr);\n"
    yield indentation + "/* Shift buffer back to end of varint */\n"
    yield indentation + "memmove(stream->buffer, dataPtr, size);\n"
    yield indentation + "stream->buffer += size;\n"
    yield indentation + "memset(stream->buffer, 0, dataToClear);\n"


def generate_encode_declaration(
    field: "QpbField", proto_type: ProtoType, raw: bool, is_array: bool
):
    if is_array:
        result = (
            f'{create_function_name(field, raw, "encode")}(qpb_ostream_t *const stream, '
            f"const {proto_type.get_ctype(raw)} arrayData[], const qpb_size_t arraySize)"
        )
    else:
        result = (
            f'{create_function_name(field, raw, "encode")}'
            "(qpb_ostream_t *const stream, "
            f"const {proto_type.get_ctype(raw)} *const data)"
        )

    return f"static inline void {result}"


def generate_encode_definition(
    field: "QpbField", proto_type: ProtoType, raw: bool, is_array: bool
):
    yield proto_type.generate_encode_declaration(field, raw, is_array) + "\n"
    yield "{\n"
    yield "".join(proto_type.generate_encode("   ", field, raw))
    yield "}\n"


def generate_decode_declaration(field: "QpbField", raw: bool):
    return (
        f'static bool {create_function_name(field, raw, "decode")}'
        "(qpb_istream_t *const stream, void *const data, "
        "const qpb_wire_type_t wiretype)"
    )


def generate_decode_definition(field: "QpbField", proto_type: ProtoType, raw: bool):
    yield proto_type.generate_decode_declaration(field, raw) + "\n"
    yield "{\n"
    yield "".join(proto_type.generate_decode("   ", field, raw))
    yield "}\n"


def generate_fixed_encode(
    proto_type, indentation: str, name: str, is_array: bool = False
):
    full_indentation = indentation
    data = "data"
    if is_array:
        data = "&arrayData[i]"
    else:
        full_indentation += "   "
        yield "".join(
            write_zero_check(indentation, name, proto_type.id, proto_type.tag)
        )

    yield f"{full_indentation}qpb_encode_fixed{proto_type.bits}(stream, {data});\n"

    if not is_array:
        yield f"{indentation}}}\n"


def generate_varint_encode(
    proto_type, indentation: str, name: str, is_array: bool = False
):
    function = create_varint_function(proto_type.numeric_type)
    full_indentation = indentation
    data = "*data"
    if is_array:
        data = "arrayData[i]"
    else:
        full_indentation += "   "
        yield "".join(
            write_zero_check(indentation, name, proto_type.id, proto_type.tag)
        )

    yield f"{full_indentation}qpb_encode_{function}(stream, {data});\n"

    if not is_array:
        yield f"{indentation}}}\n"


def generate_varint_decode(
    proto_type: ProtoType,
    indentation: str,
    name: str,
    struct_name: str,
    is_array: bool = False,
):
    start = create_packable_start(is_array)
    array_index = create_array_index(struct_name, name) if is_array else ""

    if not is_array:
        yield f"{indentation}QPB_UNUSED(wiretype);\n"

    function = create_varint_function(proto_type.numeric_type, True)
    numeric_type = NUMERIC_TYPES[
        Support.get_basic_numeric_type(proto_type.numeric_type)
    ]
    yield (
        f"{indentation}{start} qpb_decode_{function}"
        f"(stream, (void*)&(({struct_name}*)data)->{name}{array_index}, sizeof({numeric_type}));\n"
    )


def generate_processed_varint_decode(
    proto_type: ProtoType,
    indentation: str,
    name: str,
    struct_name: str,
    is_array: bool = False,
):
    start = "bool " if not is_array else ""
    array_index = create_array_index(struct_name, name) if is_array else ""

    if not is_array:
        yield f"{indentation}QPB_UNUSED(wiretype);\n"

    function = create_varint_function(proto_type.numeric_type, True)
    numeric_type = NUMERIC_TYPES[
        Support.get_basic_numeric_type(proto_type.numeric_type)
    ]
    yield f"{indentation}{numeric_type} value;\n"
    yield f"{indentation}{start}result = qpb_decode_{function}(stream, (void*)&value, sizeof({numeric_type}));\n"
    yield (
        f"{indentation}(({struct_name}*)data)->{name}{array_index} = "
        f"value * {CSupport.float_define(proto_type.scale)};\n"
    )
    if not is_array:
        yield f"{indentation}return result;\n"


def generate_enum_decode(
    proto_type: ProtoType,
    indentation: str,
    name: str,
    struct_name: str,
    is_array: bool = False,
):
    start = create_packable_start(is_array)
    array_index = create_array_index(struct_name, name) if is_array else ""

    if not is_array:
        yield f"{indentation}QPB_UNUSED(wiretype);\n"

    array_str = "[0]" if is_array else ""
    yield (
        f"{indentation}{start} qpb_decode_varint"
        f"(stream, (void*)&(({struct_name}*)data)->{name}{array_index}, "
        f"qpb_membersize({struct_name}, {name}{array_str}));\n"
    )


def generate_uenum_decode(
    proto_type: ProtoType,
    indentation: str,
    name: str,
    struct_name: str,
    is_array: bool = False,
):
    array_index = create_array_index(struct_name, name) if is_array else ""

    yield f"{indentation}qpb_int64_t value;\n"
    if not is_array:
        yield f"{indentation}bool result;\n"

    if not is_array:
        yield f"{indentation}QPB_UNUSED(wiretype);\n"

    c_type_name = proto_type.enum_definition.get_full_name().to_string("_")

    yield f"{indentation}result = qpb_decode_varint(stream, &value, sizeof(qpb_int64_t));\n"
    yield f"{indentation}if (result)\n"
    yield f"{indentation}{{\n"
    yield f"#ifndef QPB_WITHOUT_64BIT\n"
    yield f"{indentation}   /* Protobuf only supports int32 values for enums */\n"
    yield f"{indentation}   result = INT32_MIN <= value && value <= INT32_MAX;\n"
    yield f"{indentation}   if (result)\n"
    yield f"{indentation}   {{\n"
    yield f"{indentation}      (({struct_name}*)data)->{name}{array_index} = ({c_type_name})value;\n"
    yield f"{indentation}   }}\n"
    yield "#else\n"
    yield f"{indentation}   (({struct_name}*)data)->{name}{array_index} = ({c_type_name})value;\n"
    yield "#endif\n"
    yield f"{indentation}}}\n"
    if not is_array:
        yield f"{indentation}return result;\n"


def generate_fixed_decode(
    proto_type: ProtoType,
    indentation: str,
    name: str,
    struct_name: str,
    is_array: bool = False,
):
    start = create_packable_start(is_array)
    array_index = create_array_index(struct_name, name) if is_array else ""
    if not is_array:
        yield f"{indentation}QPB_UNUSED(wiretype);\n"
    yield (
        f"{indentation}{start} qpb_decode_fixed{proto_type.bits}"
        f"(stream, (void*)&(({struct_name}*)data)->{name}{array_index});\n"
    )


def generate_simple_array_encode(
    proto_type, indentation: str, field: "QpbField", raw: bool
):
    yield f"{indentation}if (arraySize > 0)\n"
    yield f"{indentation}{{\n"
    yield f"{indentation}   qpb_byte_t* sizePtr;\n"
    yield f"{indentation}   qpb_byte_t* dataPtr;\n"
    yield f"{indentation}   qpb_size_t size;\n"
    yield f"{indentation}   qpb_byte_t dataToClear;\n"

    if proto_type.packable:
        yield "".join(
            generate_tag_and_shift(
                indentation + "   ", proto_type.id, proto_type.id << 3 | 2
            )
        )

    yield f"{indentation}   for (qpb_size_t i = 0; i < arraySize; ++i)\n"
    yield f"{indentation}   {{\n"
    if proto_type.packable:
        yield "".join(
            proto_type.generate_encode(indentation + "      ", field, raw, True)
        )
        yield f"{indentation}   }}\n"
        yield "".join(generate_size_and_shift(indentation + "   "))
    else:
        yield "".join(
            generate_tag_and_shift(
                indentation + "      ", proto_type.id, proto_type.tag
            )
        )
        yield "".join(
            proto_type.generate_encode(indentation + "      ", field, raw, True)
        )
        yield "".join(generate_size_and_shift(indentation + "      "))
        yield f"{indentation}   }}\n"

    yield f"{indentation}}}\n"


def generate_complex_array_encode(
    proto_type, indentation: str, field: "QpbField", raw: bool, source_data: str
):
    yield f"{indentation}for (qpb_size_t i = 0; i < arraySize; ++i)\n"
    yield f"{indentation}{{\n"
    yield "".join(write_tag(indentation + "   ", proto_type.id, proto_type.tag))
    yield f"{indentation}   const {proto_type.get_ctype(raw)} *const data = {source_data};\n"
    yield "".join(proto_type.generate_encode(indentation + "   ", field, raw, True))
    yield f"{indentation}}}\n"


def generate_struct_comment(proto_type: ProtoType, comments: "list(str)"):
    result = "    /** "
    result += "\n     * ".join(comments)
    result += "\n    " if len(comments) > 1 else ""
    result += " */\n"

    return result


def generate_numeric_entry(
    proto_type: ProtoType,
    entry_name: str,
    comments: "list(str)",
    raw: bool,
    array_decl: str,
):
    if proto_type.scale is not None:
        name = "Scale" if raw else "Resolution"
        comments.append(f"{name}: {proto_type.scale}")

    if proto_type.min is not None and proto_type.max is not None:
        comments.append(Support.strip_float(f"Min: {proto_type.min:g}"))
        comments.append(Support.strip_float(f"Max: {proto_type.max:g}"))

    result = generate_struct_comment(proto_type, comments)
    result += f"    {proto_type.get_ctype(raw)} {entry_name}{array_decl};"
    return result


class QpbVarintProtoType(VarintProtoType):
    def __init__(
        self,
        field_options: so.SystemFieldOptions,
        identifier: int,
        numeric_type: NumericType,
    ):
        super().__init__(field_options, identifier, numeric_type)
        self.decode_supported = True

    def is_processed(self):
        return self.scale is not None

    def generate_encode_call(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        raw_call = raw or self.scale is None

        arguments = None
        if is_array:
            arguments = f"data->{field.entry_name}, data->{field.entry_name}_count"
        else:
            arguments = f"&data->{field.entry_name}"

        return (
            f'{create_function_name(field, raw_call, "encode")}(stream, {arguments});\n'
        )

    def generate_encode_declaration(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        return generate_encode_declaration(field, self, raw, is_array)

    def generate_encode_definition(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        return generate_encode_definition(field, self, raw, is_array)

    def generate_encode(
        self, indentation: str, field: "QpbField", raw: bool, is_array: bool = False
    ):
        result = ""
        if not raw and self.scale is not None:
            ctype = self.get_ctype(True)
            data = "arrayData[i]" if is_array else "*data"
            convert_call = CSupport.get_float_to_int_convert_call(
                ctype, data, CSupport.float_define(self.scale)
            )
            result += f"{indentation}{ctype} value = {convert_call};\n"
            result += f"{indentation}encode_{field.parent.get_struct_name(True)}_{field.entry_name}(stream, &value);\n"
        else:
            result = generate_varint_encode(
                self, indentation, field.entry_name, is_array
            )

        return result

    def generate_array_encode(self, indentation: str, field: "QpbField", raw: bool):
        return generate_simple_array_encode(self, indentation, field, raw)

    def generate_processed_array_encode(
        self, indentation: str, field: "QpbField", raw: bool, max_count: int
    ):
        convert_call = CSupport.get_float_to_int_convert_call(
            self.get_ctype(True), "arrayData[i]", CSupport.float_define(self.scale)
        )
        yield f"{indentation}{self.get_ctype(True)} values[{max_count}];\n"
        yield f"{indentation}for (qpb_size_t i = 0; i < arraySize; ++i)\n"
        yield f"{indentation}{{\n"
        yield f"{indentation}   values[i] = {convert_call};\n"
        yield f"{indentation}}}\n"
        yield (
            f"{indentation}encode_{field.parent.get_struct_name(True)}_{field.entry_name}"
            f"(stream, values, arraySize);\n"
        )

    def generate_decode_declaration(self, field: "QpbField", raw: bool):
        return generate_decode_declaration(field, raw)

    def generate_decode_definition(self, field: "QpbField", raw: bool):
        return generate_decode_definition(field, self, raw)

    def generate_decode(
        self, indentation: str, field: "QpbField", raw: bool, is_array: bool = False,
    ):
        if not raw and self.is_processed():
            return generate_processed_varint_decode(
                self,
                indentation,
                field.entry_name,
                field.parent.get_struct_name(raw),
                is_array,
            )
        else:
            return generate_varint_decode(
                self,
                indentation,
                field.entry_name,
                field.parent.get_struct_name(raw),
                is_array,
            )

    def get_ctype(self, raw: bool):
        if not raw and self.scale is not None:
            return "float"
        else:
            return NUMERIC_TYPES[Support.get_basic_numeric_type(self.numeric_type)]

    def generate_struct_entry(
        self, entry_name: str, comments: "list(str)", raw: bool, array_decl: str = ""
    ):
        return generate_numeric_entry(self, entry_name, comments, raw, array_decl)


class QpbEnumProtoType(EnumProtoType):
    def __init__(
        self, field_options: so.SystemFieldOptions, identifier: int, type_name: str
    ):
        super().__init__(field_options, identifier, type_name)
        self.decode_supported = True

    def is_processed(self):
        return False

    def generate_encode_call(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        raw_call = True
        arguments = None
        if is_array:
            arguments = f"data->{field.entry_name}, data->{field.entry_name}_count"
        else:
            arguments = f"&data->{field.entry_name}"

        return (
            f'{create_function_name(field, raw_call, "encode")}(stream, {arguments});\n'
        )

    def generate_encode_declaration(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        return generate_encode_declaration(field, self, raw, is_array)

    def generate_encode_definition(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        return generate_encode_definition(field, self, raw, is_array)

    def generate_encode(
        self, indentation: str, field: "QpbField", raw: bool, is_array: bool = False
    ):
        return generate_varint_encode(self, indentation, field.name, is_array)

    def generate_array_encode(self, indentation: str, field: "QpbField", raw: bool):
        return generate_simple_array_encode(self, indentation, field, raw)

    def generate_decode_declaration(self, field: "QpbField", raw: bool):
        return generate_decode_declaration(field, raw)

    def generate_decode_definition(self, field: "QpbField", raw: bool):
        return generate_decode_definition(field, self, raw)

    def generate_decode(
        self, indentation: str, field: "QpbField", raw: bool, is_array: bool = False,
    ):
        if self.enum_definition.has_negative():
            return generate_uenum_decode(
                self,
                indentation,
                field.entry_name,
                field.parent.get_struct_name(raw),
                is_array,
            )
        else:
            return generate_enum_decode(
                self,
                indentation,
                field.entry_name,
                field.parent.get_struct_name(raw),
                is_array,
            )

    def get_ctype(self, raw: bool):
        return self.get_name().replace(".", "_")

    def generate_struct_entry(
        self, entry_name: str, comments: "list(str)", raw: bool, array_decl: str = ""
    ):
        return generate_numeric_entry(self, entry_name, comments, raw, array_decl)


class QpbBoolProtoType(BoolProtoType):
    def __init__(self, field_options: so.SystemFieldOptions, identifier: int):
        super().__init__(field_options, identifier)
        self.decode_supported = True

    def is_processed(self):
        return False

    def generate_encode_call(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        raw_call = True
        arguments = None
        if is_array:
            arguments = f"data->{field.entry_name}, data->{field.entry_name}_count"
        else:
            arguments = f"&data->{field.entry_name}"

        return (
            f'{create_function_name(field, raw_call, "encode")}(stream, {arguments});\n'
        )

    def generate_encode_declaration(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        return generate_encode_declaration(field, self, raw, is_array)

    def generate_encode_definition(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        return generate_encode_definition(field, self, raw, is_array)

    def generate_encode(
        self, indentation: str, field: "QpbField", raw: bool, is_array: bool = False
    ):
        return generate_varint_encode(self, indentation, field.entry_name, is_array)

    def generate_array_encode(self, indentation: str, field: "QpbField", raw: bool):
        return generate_simple_array_encode(self, indentation, field, raw)

    def generate_decode_declaration(self, field: "QpbField", raw: bool):
        return generate_decode_declaration(field, raw)

    def generate_decode_definition(self, field: "QpbField", raw: bool):
        return generate_decode_definition(field, self, raw)

    def generate_decode(
        self, indentation: str, field: "QpbField", raw: bool, is_array: bool = False,
    ):
        return generate_varint_decode(
            self,
            indentation,
            field.entry_name,
            field.parent.get_struct_name(raw),
            is_array,
        )

    def get_ctype(self, raw: bool):
        return NUMERIC_TYPES[Support.get_basic_numeric_type(self.numeric_type)]

    def generate_struct_entry(
        self, entry_name: str, comments: "list(str)", raw: bool, array_decl: str = ""
    ):
        result = generate_struct_comment(self, comments)
        result += f"    {self.get_ctype(raw)} {entry_name}{array_decl};"
        return result


class QpbFixed32ProtoType(Fixed32ProtoType):
    def __init__(
        self,
        field_options: so.SystemFieldOptions,
        identifier: int,
        numeric_type: Fixed32NumericType,
    ):
        super().__init__(field_options, identifier, numeric_type)
        self.decode_supported = True

    def is_processed(self):
        return False

    def generate_encode_call(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        raw_call = True
        arguments = None
        if is_array:
            arguments = f"data->{field.entry_name}, data->{field.entry_name}_count"
        else:
            arguments = f"&data->{field.entry_name}"

        return (
            f'{create_function_name(field, raw_call, "encode")}(stream, {arguments});\n'
        )

    def generate_encode_declaration(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        return generate_encode_declaration(field, self, raw, is_array)

    def generate_encode_definition(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        return generate_encode_definition(field, self, raw, is_array)

    def generate_encode(
        self, indentation: str, field: "QpbField", raw: bool, is_array: bool = False
    ):
        return generate_fixed_encode(self, indentation, field.entry_name, is_array)

    def generate_array_encode(self, indentation: str, field: "QpbField", raw: bool):
        return generate_simple_array_encode(self, indentation, field, raw)

    def generate_decode_declaration(self, field: "QpbField", raw: bool):
        return generate_decode_declaration(field, raw)

    def generate_decode_definition(self, field: "QpbField", raw: bool):
        return generate_decode_definition(field, self, raw)

    def generate_decode(
        self, indentation: str, field: "QpbField", raw: bool, is_array: bool = False,
    ):
        return generate_fixed_decode(
            self,
            indentation,
            field.entry_name,
            field.parent.get_struct_name(raw),
            is_array,
        )

    def get_ctype(self, raw: bool):
        return NUMERIC_TYPES[Support.get_basic_numeric_type(self.numeric_type)]

    def generate_struct_entry(
        self, entry_name: str, comments: "list(str)", raw: bool, array_decl: str = ""
    ):
        return generate_numeric_entry(self, entry_name, comments, raw, array_decl)


class QpbFixed64ProtoType(Fixed64ProtoType):
    def __init__(
        self,
        field_options: so.SystemFieldOptions,
        identifier: int,
        numeric_type: Fixed64NumericType,
    ):
        super().__init__(field_options, identifier, numeric_type)
        self.decode_supported = True

    def is_processed(self):
        return False

    def generate_encode_call(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        raw_call = True
        arguments = None
        if is_array:
            arguments = f"data->{field.entry_name}, data->{field.entry_name}_count"
        else:
            arguments = f"&data->{field.entry_name}"

        return (
            f'{create_function_name(field, raw_call, "encode")}(stream, {arguments});\n'
        )

    def generate_encode_declaration(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        return generate_encode_declaration(field, self, raw, is_array)

    def generate_encode_definition(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        return generate_encode_definition(field, self, raw, is_array)

    def generate_encode(
        self, indentation: str, field: "QpbField", raw: bool, is_array: bool = False
    ):
        return generate_fixed_encode(self, indentation, field.entry_name, is_array)

    def generate_array_encode(self, indentation: str, field: "QpbField", raw: bool):
        return generate_simple_array_encode(self, indentation, field, raw)

    def generate_decode_declaration(self, field: "QpbField", raw: bool):
        return generate_decode_declaration(field, raw)

    def generate_decode_definition(self, field: "QpbField", raw: bool):
        return generate_decode_definition(field, self, raw)

    def generate_decode(
        self, indentation: str, field: "QpbField", raw: bool, is_array: bool = False,
    ):
        return generate_fixed_decode(
            self,
            indentation,
            field.entry_name,
            field.parent.get_struct_name(raw),
            is_array,
        )

    def get_ctype(self, raw: bool):
        return NUMERIC_TYPES[Support.get_basic_numeric_type(self.numeric_type)]

    def generate_struct_entry(
        self, entry_name: str, comments: "list(str)", raw: bool, array_decl: str = ""
    ):
        return generate_numeric_entry(self, entry_name, comments, raw, array_decl)


class QpbStringProtoType(StringProtoType):
    def __init__(self, field_options: so.SystemFieldOptions, identifier: int):
        super().__init__(field_options, identifier)
        self.decode_supported = self.allocation == Allocation.STATIC
        self.array_size = None
        if not self.decode_supported:
            sys.stderr.write(
                "#### Please note! ####\n"
                "QuickProtobuf\n"
                "Only encoding of string pointers is supported.\n"
                "This since decoding only sets the pointer to the position in the "
                "receive buffer which is not null terminated.\n"
                "#### End note ####\n"
            )

    def is_processed(self):
        return False

    def generate_encode_call(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        raw_call = True
        arguments = None
        if is_array:
            arguments = f"data->{field.entry_name}, data->{field.entry_name}_count"
        else:
            arguments = f"data->{field.entry_name}"

        return (
            f'{create_function_name(field, raw_call, "encode")}(stream, {arguments});\n'
        )

    def _generate_function_declaration(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        result = ""
        if is_array:
            if self.allocation == Allocation.POINTER:
                data_type = f"{self.get_ctype(raw)} *const arrayData[]"
            else:
                data_type = f"{self.get_ctype(raw)} arrayData[{self.array_size}][{self.max_size}]"

            result = (
                f'{create_function_name(field, raw, "encode")}'
                f"(qpb_ostream_t *const stream, const {data_type},"
                "const qpb_size_t arraySize)"
            )
        else:
            result = (
                f'{create_function_name(field, raw, "encode")}'
                f"(qpb_ostream_t *const stream, "
                f"const {self.get_ctype(raw)} *const data)"
            )

        return f"static inline void {result}"

    def generate_encode_declaration(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        return self._generate_function_declaration(field, raw, is_array)

    def generate_encode_definition(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        yield self._generate_function_declaration(field, raw, is_array) + "\n"
        yield "{\n"
        yield "".join(self.generate_encode("   ", field, raw))
        yield "}\n"

    def generate_encode(
        self, indentation: str, field: "QpbField", raw: bool, is_array: bool = False
    ):
        size_string = "strlen(data)"
        if self.allocation == Allocation.POINTER:
            size_string = f"(data != 0 ? strlen(data) : 0)"

        if not is_array:
            yield f"{indentation}qpb_size_t strSize = {size_string};\n"
            yield f"{indentation}if (strSize != 0)\n"
            yield f"{indentation}{{\n"
            yield "".join(write_tag(indentation + "   ", self.id, self.tag))
            yield f"{indentation}   qpb_encode_bytes(stream, (qpb_byte_t*)data, strSize);\n"
            yield f"{indentation}}}\n"
        else:
            yield f"{indentation}qpb_encode_bytes(stream, (qpb_byte_t*)data, {size_string});\n"

    def generate_array_encode(self, indentation: str, field: "QpbField", raw: bool):
        source_data = (
            "arrayData[i]"
            if self.allocation == Allocation.POINTER
            else "&arrayData[i][0]"
        )
        return generate_complex_array_encode(self, indentation, field, raw, source_data)

    def generate_decode_declaration(self, field: "QpbField", raw: bool):
        return generate_decode_declaration(field, raw)

    def generate_decode_definition(self, field: "QpbField", raw: bool):
        return generate_decode_definition(field, self, raw)

    def generate_decode(
        self, indentation: str, field: "QpbField", raw: bool, is_array: bool = False,
    ):
        struct_name = field.parent.get_struct_name(raw)
        name = field.entry_name
        array_index = create_array_index(struct_name, name) if is_array else ""
        if not is_array:
            yield indentation + "QPB_UNUSED(wiretype);\n"
        if self.allocation == Allocation.STATIC:
            yield (
                f"{indentation}return qpb_decode_string_static"
                f"(stream, (({struct_name}*)data)->{name}{array_index}, {self.max_size - 1});\n"
            )

    def get_ctype(self, raw: bool):
        return "char"

    def generate_struct_entry(
        self, entry_name: str, comments: "list(str)", raw: bool, array_decl: str = ""
    ):
        result = generate_struct_comment(self, comments)
        if self.allocation == Allocation.POINTER:
            result += f"    {self.get_ctype(raw)} *{entry_name}{array_decl};"
        else:
            char_decl = f"[{self.max_size}]"
            result += f"    {self.get_ctype(raw)} {entry_name}{array_decl}{char_decl};"

        return result


class QpbBytesProtoType(BytesProtoType):
    def __init__(
        self, field_options: so.SystemFieldOptions, identifier: int, field: "QpbField"
    ):
        super().__init__(field_options, identifier)
        self.decode_supported = True
        self.field = field

    def is_processed(self):
        return False

    def generate_encode_call(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        raw_call = True
        arguments = None
        if is_array:
            arguments = f"data->{field.entry_name}, data->{field.entry_name}_count"
        else:
            arguments = f"&data->{field.entry_name}"

        return (
            f'{create_function_name(field, raw_call, "encode")}(stream, {arguments});\n'
        )

    def generate_encode_declaration(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        return generate_encode_declaration(field, self, raw, is_array)

    def generate_encode_definition(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        yield generate_encode_declaration(field, self, raw, is_array) + "\n"
        yield "{\n"
        yield "".join(self.generate_encode("   ", field, raw))
        yield "}\n"

    def generate_encode(
        self, indentation: str, field: "QpbField", raw: bool, is_array: bool = False
    ):
        full_indentation = indentation
        if not is_array:
            yield f"{indentation}if (data->size != 0)\n"
            yield f"{indentation}{{\n"
            yield "".join(write_tag(indentation + "   ", self.id, self.tag))
            full_indentation += "   "

        yield f"{full_indentation}qpb_encode_bytes(stream, data->bytes, data->size);\n"
        if not is_array:
            yield f"{indentation}}}\n"

    def generate_array_encode(self, indentation: str, field: "QpbField", raw: bool):
        return generate_complex_array_encode(
            self, indentation, field, raw, "&arrayData[i]"
        )

    def generate_decode_declaration(self, field: "QpbField", raw: bool):
        return generate_decode_declaration(field, raw)

    def generate_decode_definition(self, field: "QpbField", raw: bool):
        return generate_decode_definition(field, self, raw)

    def generate_decode(
        self, indentation: str, field: "QpbField", raw: bool, is_array: bool = False,
    ):
        struct_name = field.parent.get_struct_name(raw)
        name = field.entry_name
        array_index = create_array_index(struct_name, name) if is_array else ""
        if not is_array:
            yield indentation + "QPB_UNUSED(wiretype);\n"
        if self.allocation == Allocation.STATIC:
            yield (
                f"{indentation}return qpb_decode_bytes_static"
                f"(stream, (qpb_bytes_array_t*)&(({struct_name}*)data)->{name}{array_index}, {self.max_size});\n"
            )
        else:
            yield (
                f"{indentation}return qpb_decode_bytes_pointer"
                f"(stream, &(({struct_name}*)data)->{name}{array_index});\n"
            )

    def get_ctype(self, raw: bool):
        if self.allocation == Allocation.STATIC:
            return "_".join(
                [self.field.parent.get_struct_name(raw), self.field.entry_name, "t"]
            )
        else:
            return "qpb_bytes_pointer_t"

    def generate_needed_typedef(self, raw: bool):
        result = ""
        if self.allocation == Allocation.STATIC:
            result = (
                f"typedef QPB_BYTES_ARRAY_T({self.max_size}) {self.get_ctype(raw)};\n"
            )
            if not raw:  # Since bytes is the same let's just link the definitions
                result = f"#define {self.get_ctype(False)} {self.get_ctype(True)}\n"

        return result

    def generate_struct_entry(
        self, entry_name: str, comments: "list(str)", raw: bool, array_decl: str = ""
    ):
        result = generate_struct_comment(self, comments)
        result += f"    {self.get_ctype(raw)} {entry_name}{array_decl};"
        return result


class QpbArrayProtoType(ArrayProtoType):
    def __init__(
        self,
        field_options: so.SystemFieldOptions,
        identifier: int,
        data_type: ProtoType,
    ):
        super().__init__(field_options, identifier, data_type)
        self.decode_supported = False  # Assume it is not supported until proven
        if hasattr(data_type, "array_size"):
            data_type.array_size = self.max_size

    def is_processed(self):
        return self.data_type.is_processed()

    def handle_dependencies(self, dependencies):
        super().handle_dependencies(dependencies)

        if self.data_type:
            self.decode_supported = self.data_type.decode_supported

    def generate_encode_call(self, field: "QpbField", raw: bool):
        return self.data_type.generate_encode_call(field, raw, True)

    def generate_encode_declaration(self, field: "QpbField", raw: bool):
        return self.data_type.generate_encode_declaration(field, raw, True)

    def generate_encode_definition(self, field: "QpbField", raw: bool):
        yield self.data_type.generate_encode_declaration(field, raw, True) + "\n"
        code = "".join(self.generate_encode("   ", field, raw))
        if code != "":
            yield "{\n"
            yield code
            yield "}\n"

    def generate_encode(self, indentation: str, field: "QpbField", raw: bool):
        if not raw and self.data_type.is_processed():
            yield "".join(
                self.data_type.generate_processed_array_encode(
                    indentation, field, raw, self.max_count
                )
            )
        else:
            yield "".join(self.data_type.generate_array_encode(indentation, field, raw))

    def generate_decode_declaration(self, field: "QpbField", raw: bool):
        return generate_decode_declaration(field, raw)

    def generate_decode_definition(self, field: "QpbField", raw: bool):
        return generate_decode_definition(field, self, raw)

    def generate_decode(self, indentation: str, field: "QpbField", raw: bool):
        struct_name = field.parent.get_struct_name(raw)
        name = field.entry_name
        if self.data_type.packable:
            yield f"{indentation}bool result = false;\n"
            yield f"{indentation}/* Reading packed */\n"
            yield f"{indentation}if (wiretype == QPB_WT_STRING)\n"
            yield f"{indentation}{{\n"
            yield f"{indentation}   qpb_size_t size;\n"
            yield f"{indentation}   qpb_byte_t* endPtr;\n"
            yield f"{indentation}   result = qpb_decode_uvarint(stream, &size, sizeof(qpb_size_t));\n"
            yield f"{indentation}   if (!result)\n"
            yield f"{indentation}   {{\n"
            yield f"{indentation}      return false;\n"
            yield f"{indentation}   }}\n"
            yield f"{indentation}   endPtr = stream->buffer + size;\n"
            yield f"{indentation}   while (stream->buffer < endPtr && result)\n"
            yield f"{indentation}   {{\n"
            yield f"{indentation}      if ((({struct_name}*)data)->{name}_count + 1 > {self.max_count})\n"
            yield f"{indentation}      {{\n"
            yield f'{indentation}         QPB_RETURN_ERROR(stream, "array overflow");\n'
            yield f"{indentation}      }}\n"
            yield "".join(
                self.data_type.generate_decode(indentation + "      ", field, raw, True)
            )
            yield f"{indentation}   }}\n"
            yield f"{indentation}}}\n"
            yield f"{indentation}/* Reading non-packed */\n"
            yield f"{indentation}else\n"
            yield f"{indentation}{{\n"
            yield f"{indentation}   if (((({struct_name}*)data)->{name}_count + 1) > {self.max_count})\n"
            yield f"{indentation}   {{\n"
            yield f'{indentation}      QPB_RETURN_ERROR(stream, "array overflow");\n'
            yield f"{indentation}   }}\n"
            yield "".join(
                self.data_type.generate_decode(indentation + "   ", field, raw, True)
            )
            yield f"{indentation}}}\n"
            yield f"{indentation}return result;\n"
        else:
            yield f"{indentation}QPB_UNUSED(wiretype);\n"
            yield f"{indentation}if (((({struct_name}*)data)->{name}_count + 1) > {self.max_count})\n"
            yield f"{indentation}{{\n"
            yield f'{indentation}   QPB_RETURN_ERROR(stream, "array overflow");\n'
            yield f"{indentation}}}\n"
            yield "".join(self.data_type.generate_decode(indentation, field, raw, True))

    def get_ctype(self, raw: bool):
        return self.data_type.get_ctype(raw)

    def generate_needed_typedef(self, raw: bool):
        if hasattr(self.data_type, "generate_needed_typedef"):
            return self.data_type.generate_needed_typedef(raw)
        else:
            return ""

    def get_array_declaration(self):
        array_decl = f"[{self.max_count}]"
        return array_decl, self.data_type

    def generate_struct_entry(self, entry_name: str, comments: "list(str)", raw: bool):
        array_decl = f"[{self.max_count}]"
        result = f"    qpb_size_t {entry_name}_count;\n"
        result += self.data_type.generate_struct_entry(
            entry_name, comments, raw, array_decl
        )
        return result


class QpbMessageProtoType(MessageProtoType):
    def __init__(
        self, field_options: so.SystemFieldOptions, identifier: int, message_type: str
    ):
        super().__init__(field_options, identifier, message_type)
        self.decode_supported = True

    def is_processed(self):
        return self.message.is_processed()

    def generate_processed_array_encode(
        self, indentation: str, field: "QpbField", raw: bool, max_count: int
    ):
        return generate_simple_array_encode(self, indentation, field, raw)

    def generate_encode_call(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        arguments = None
        if is_array:
            arguments = f"data->{field.entry_name}, data->{field.entry_name}_count"
        else:
            arguments = f"&data->{field.entry_name}"

        return f'{create_function_name(field, raw, "encode")}(stream, {arguments});\n'

    def generate_encode_declaration(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        return generate_encode_declaration(field, self, raw, is_array)

    def generate_encode_definition(
        self, field: "QpbField", raw: bool, is_array: bool = False
    ):
        yield generate_encode_declaration(field, self, raw, is_array) + "\n"
        yield "{\n"
        yield "".join(self.generate_encode("   ", field, raw))
        yield "}\n"

    def generate_encode(
        self, indentation: str, field: "QpbField", raw: bool, is_array: bool = False
    ):
        full_name = self.message.get_full_name().to_string("_") + (
            "_Raw" if raw else ""
        )
        if is_array:
            yield f"{indentation}encode_{full_name}(stream, &arrayData[i]);\n"
        else:
            yield f"{indentation}qpb_byte_t* start;\n"
            yield f"{indentation}qpb_byte_t* dataPtr;\n"
            yield f"{indentation}qpb_size_t size;\n"
            yield f"{indentation}qpb_byte_t dataToClear;\n"
            yield "".join(write_tag(indentation, self.id, self.tag))
            yield f"{indentation}start = stream->buffer;\n"
            yield f"{indentation}stream->buffer += QPB_VARINT_MAX_ENCODED_SIZE;\n"
            yield f"{indentation}dataPtr = stream->buffer;\n"
            yield f"{indentation}encode_{full_name}(stream, data);\n"
            yield f"{indentation}if (stream->buffer > dataPtr)\n"
            yield f"{indentation}{{\n"
            yield f"{indentation}   /* Check size of encoded message and write size at the appropriate offset */\n"
            yield f"{indentation}   size = (stream->buffer - dataPtr);\n"
            yield f"{indentation}   stream->buffer = start;\n"
            yield f"{indentation}   qpb_encode_varint(stream, (qpb_uint64_t)size);\n"
            yield f"{indentation}   dataToClear = QPB_VARINT_MAX_ENCODED_SIZE - (stream->buffer - start);\n"
            yield f"{indentation}   /* Shift buffer back to end of varint */\n"
            yield f"{indentation}   memmove(stream->buffer, dataPtr, size);\n"
            yield f"{indentation}   stream->buffer += size;\n"
            yield f"{indentation}   memset(stream->buffer, 0, dataToClear);\n"
            yield f"{indentation}}}\n"
            yield f"{indentation}else /* No data written shift buffer back */\n"
            yield f"{indentation}{{\n"
            tag_size = Support.varint_max_size(self.tag)
            yield f"{indentation}   stream->buffer = start - {tag_size};\n"
            yield f"{indentation}   memset(stream->buffer, 0, {tag_size});\n"
            yield f"{indentation}}}\n"

    def generate_array_encode(self, indentation: str, field: "QpbField", raw: bool):
        return generate_simple_array_encode(self, indentation, field, raw)

    def generate_decode_declaration(self, field: "QpbField", raw: bool):
        return generate_decode_declaration(field, raw)

    def generate_decode_definition(self, field: "QpbField", raw: bool):
        return generate_decode_definition(field, self, raw)

    def generate_decode(
        self, indentation: str, field: "QpbField", raw: bool, is_array: bool = False,
    ):
        struct_name = field.parent.get_struct_name(raw)
        name = field.entry_name
        array_index = create_array_index(struct_name, name) if is_array else ""
        full_indentation = indentation
        if is_array:
            yield indentation + "{\n"
            full_indentation += "   "
        else:
            yield indentation + "QPB_UNUSED(wiretype);\n"

        yield f"{full_indentation}qpb_size_t size;\n"
        yield f"{full_indentation}qpb_istream_t substream;\n"
        yield f"{full_indentation}bool result = qpb_decode_uvarint(stream, &size, sizeof(qpb_size_t));\n"
        yield f"{full_indentation}if (!result)\n"
        yield f"{full_indentation}{{\n"
        yield f"{full_indentation}   return false;\n"
        yield f"{full_indentation}}}\n"
        yield f"{full_indentation}substream = qpb_istream_from_buffer(stream->buffer, size);\n"
        full_name = self.message.get_struct_name(raw)
        yield (
            f"{full_indentation}result = decode_{full_name}"
            f"(&substream, &(({struct_name}*)data)->{name}{array_index});\n"
        )
        yield f"{full_indentation}if (!result)\n"
        yield f"{full_indentation}{{\n"
        yield f"{full_indentation}   QPB_RETURN_ERROR(stream, QPB_GET_ERROR(&substream));\n"
        yield f"{full_indentation}}}\n"
        yield f"{full_indentation}stream->buffer += size;\n"
        if is_array:
            yield f"{indentation}}}\n"
            yield f"{indentation}return true;\n"
        else:
            yield f"{indentation}return result;\n"

    def get_ctype(self, raw: bool):
        return self.message.get_struct_name(raw)

    def generate_struct_entry(
        self, entry_name: str, comments: "list(str)", raw: bool, array_decl: str = ""
    ):
        result = generate_struct_comment(self, comments)
        result += f"    {self.get_ctype(raw)} {entry_name}{array_decl};"
        return result


class QpbField(Field):
    def __init__(
        self,
        parent,
        field_descriptor: descriptor.FieldDescriptorProto,
        field_options: so.SystemFieldOptions,
    ):
        super().__init__(parent, field_descriptor, field_options)
        self.entry_name = self.name[0].lower() + self.name[1:]

    def create_string(self, field_options: so.SystemFieldOptions):
        return QpbStringProtoType(field_options, self.id)

    def create_enum(self, field_options: so.SystemFieldOptions, type_name: str):
        return QpbEnumProtoType(field_options, self.id, type_name)

    def create_bytes(self, field_options: so.SystemFieldOptions):
        return QpbBytesProtoType(field_options, self.id, self)

    def create_message(self, field_options: so.SystemFieldOptions, type_name: str):
        return QpbMessageProtoType(field_options, self.id, type_name)

    def create_bool(self, field_options: so.SystemFieldOptions):
        return QpbBoolProtoType(field_options, self.id)

    def create_fixed32(
        self, field_options: so.SystemFieldOptions, fixed32_type: Fixed32NumericType
    ):
        return QpbFixed32ProtoType(field_options, self.id, fixed32_type)

    def create_fixed64(
        self, field_options: so.SystemFieldOptions, fixed64_type: Fixed64NumericType
    ):
        return QpbFixed64ProtoType(field_options, self.id, fixed64_type)

    def create_varint(
        self, field_options: so.SystemFieldOptions, numeric_type: NumericType
    ):
        return QpbVarintProtoType(field_options, self.id, numeric_type)

    def create_array(self, field_options: so.SystemFieldOptions, data_type: ProtoType):
        return QpbArrayProtoType(field_options, self.id, data_type)

    def generate_struct_entry(self, raw: bool):
        comments = []
        comments.append(self.name)
        if self.description:
            comments.append(self.description)

        if self.unit:
            comments.append(f"Unit: {self.unit}")

        return self.data_type.generate_struct_entry(self.entry_name, comments, raw)

    def decode_function(self, raw: bool, definition: bool = False):
        result = ""
        if self.data_type.decode_supported and (raw or self.parent.is_processed()):
            if definition:
                result = (
                    "".join(self.data_type.generate_decode_definition(self, raw)) + "\n"
                )
            else:
                result = self.data_type.generate_decode_declaration(self, raw) + ";\n"

        return result

    def encode_function(self, raw: bool, definition: bool = False):
        result = ""
        if raw or self.parent.is_processed():
            if definition:
                result = (
                    "".join(self.data_type.generate_encode_definition(self, raw)) + "\n"
                )
            else:
                result = self.data_type.generate_encode_declaration(self, raw) + ";\n"

        return result

    def encode_call(self, raw: bool):
        return f"   {self.data_type.generate_encode_call(self, raw)}"

    def decode_array_entry(self, raw: bool):
        if (
            self.data_type.decode_supported
        ):  # TODO: Comment to log about decoding not being supported
            return create_function_name(self, raw, "decode")
        else:
            return "qpb_skip_field"

    def generate_needed_typedef(self, raw: bool):
        """Return definitions for any special types this field might need."""

        if hasattr(self.data_type, "generate_needed_typedef"):
            return self.data_type.generate_needed_typedef(raw)
        else:
            return ""

    def get_data_type(self, data_type: ProtoType = None):
        # Get the source datatype, so if it is an array get the subtype
        data_type = data_type if data_type else self.data_type
        if isinstance(data_type, ArrayProtoType):
            return self.get_data_type(data_type.data_type)

        return data_type

    def is_processed(self):
        return self.get_data_type().is_processed()


class QpbMessage(Message):
    def __init__(self, name: str, descriptor, parent, message_options, options):
        super().__init__(name, descriptor, parent, message_options, options)
        self.struct_name = self.get_full_name().to_string("_")

    def create_field(self, field, field_options):
        return QpbField(self, field, field_options)

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

            extra = " + QPB_VARINT_MAX_ENCODED_SIZE" if submessage_exist else ""
            result += f"#define {identifier:<80} ({msize}{extra})\n"
            # QPB_VARINT_MAX_ENCODED_SIZE is added since we shift the result when writing a message to
            # be able to go back and add the size
        else:
            identifier = f"{self.struct_name}_static_size"
            result += f"/* {identifier} depends on runtime parameters */\n"
            result += (
                f"#define {identifier:<80} {self.get_encoded_size_static_only()}\n"
            )
        return result

    def get_pointer_size(self, data_type: ProtoType, data: str):
        if isinstance(data_type, StringProtoType):
            return (
                f"({data} != 0 ? strlen({data}) + qpb_varint_max(strlen({data})) : 0)"
            )
        else:
            return f"({data}.size + qpb_varint_max({data}.size))"

    def _handle_pointer_field(self, pointer_data_size, field):
        if field.data_type.allocation == Allocation.POINTER:
            if isinstance(field.data_type, ArrayProtoType):
                for i in range(0, field.data_type.max_count):
                    pointer_size = self.get_pointer_size(
                        field.data_type.data_type, f"data->{field.entry_name}[{i}]",
                    )
                    pointer_data_size.append(pointer_size)
            else:
                pointer_size = self.get_pointer_size(
                    field.data_type, f"data->{field.entry_name}"
                )
                pointer_data_size.append(pointer_size)

    def generate_encode(self, raw: bool, definition: bool = False):
        if not (raw or self.is_processed()):
            if not definition:
                yield f"#define encode_{self.get_struct_name(False)} encode_{self.get_struct_name(True)}\n"
        else:
            yield "bool encode_{struct_name}(qpb_ostream_t *const stream, const {struct_name} *const data){end}".format(
                struct_name=self.get_struct_name(raw), end="\n" if definition else ";",
            )

            if definition:
                pointer_data_size = []
                for field in self.fields:
                    self._handle_pointer_field(pointer_data_size, field)

                yield "{\n"
                yield "   /* Optimize by checking that size is enough on top level? */\n"
                size_str = f"{self.struct_name}_size"
                if len(pointer_data_size) > 0:
                    size_str = (
                        f"({self.struct_name}_static_size + "
                        + " + ".join(str(x) for x in pointer_data_size)
                        + ")"
                    )
                yield f"   if ((qpb_size_t)(stream->end - stream->buffer) < {size_str})\n"
                yield "   {\n"
                yield '      QPB_RETURN_ERROR(stream, "Buffer to small");\n'
                yield "   }\n"
                for field in self.ordered_fields:
                    yield "".join(field.encode_call(raw))

                yield "   return true;\n"
                yield "}\n"

            yield "\n"

    def is_processed(self):
        return any(f.is_processed() for f in self.fields)

    def generate_typedef_needs(self, raw: bool):
        return "".join([f.generate_needed_typedef(raw) for f in self.fields])

    def get_struct_name(self, raw: bool):
        return f'{self.struct_name}{"_Raw" if raw else ""}'

    def generate_typedef(self, raw: bool):
        struct_name = self.get_struct_name(raw)
        result = ""

        if raw or self.is_processed():
            result = f"typedef struct _{struct_name} {{\n"
            result += "\n".join(
                [f.generate_struct_entry(raw) for f in self.ordered_fields]
            )
            if not self.ordered_fields:
                # Empty structs are not allowed in C standard.
                # Therefore add a dummy field if an empty message occurs.
                result += "    char dummy_field;"
            result += f"\n}} {struct_name};"
        else:
            result = (
                f"#define {self.get_struct_name(False)} {self.get_struct_name(True)}"
            )

        return result

    def generate_decoder_array(self, raw: bool):
        result = ""
        if raw or self.is_processed():
            id_count = self.ordered_fields[-1].id + 1
            struct_name = self.get_struct_name(raw)
            result = f"#define {struct_name}_DECODERS_COUNT {id_count}\n"
            result += f"const qpb_decoder_entry_t {struct_name}_decoders[{struct_name}_DECODERS_COUNT] = {{\n"

            last_id = 0
            result += "   { &qpb_skip_field } /* Id 0 is not valid and this is skipped one level up */"
            for field in self.ordered_fields:
                while last_id + 1 < field.id:
                    result += ",\n   { &qpb_skip_field }"
                    last_id += 1
                result += f",\n   {{ &{field.decode_array_entry(raw)} }}"
                last_id = field.id

            result += "\n};\n\n"
        return result

    def generate_fields_functions(self, raw: bool, definition: bool = False):
        result = ""

        for field in self.ordered_fields:
            result += field.encode_function(raw, definition)
            result += field.decode_function(raw, definition)
        return result

    def generate_decode(self, raw: bool, definition: bool = False):
        if not (raw or self.is_processed()):
            if not definition:
                yield f"#define decode_{self.get_struct_name(False)} decode_{self.get_struct_name(True)}\n"
        else:
            yield "bool decode_{struct_name}(qpb_istream_t *const stream, {struct_name} *const data){end}".format(
                struct_name=self.get_struct_name(raw), end="\n" if definition else ";"
            )

            if definition:
                yield "{\n"
                yield "   qpb_uint64_t tag;\n"
                yield "   qpb_uint64_t id;\n"
                yield "   qpb_wire_type_t wireType;\n"
                yield "   bool result = true;\n"
                yield "   while (stream->end != stream->buffer)\n"
                yield "   {\n"
                yield "      result = qpb_decode_uvarint(stream, &tag, sizeof(qpb_uint64_t));\n"
                yield "      if (!result)\n"
                yield "      {\n"
                yield "         return false;\n"
                yield "      }\n"
                yield "      /* Extended support for NULL termination */\n"
                yield "      if (tag == 0)\n"
                yield "      {\n"
                yield "         return true;\n"
                yield "      }\n"
                yield "      id = qpb_id(tag);\n"
                yield "      wireType = (qpb_wire_type_t)qpb_wireType(tag);\n"
                yield f"      if (id < {self.get_struct_name(raw)}_DECODERS_COUNT)\n"
                yield "      {\n"
                yield f"         qpb_decoder_t decoder = {self.get_struct_name(raw)}_decoders[id].func;\n"
                yield "         result = decoder(stream, data, wireType);\n"
                yield "      }\n"
                yield "      else\n"
                yield "      {\n"
                yield "         result = qpb_skip_field(stream, NULL, wireType);\n"
                yield "      }\n"
                yield "      if (!result)\n"
                yield "      {\n"
                yield "         return false;\n"
                yield "      }\n"
                yield "   }\n"
                yield "   return result;\n"
                yield "}\n"

            yield "\n"

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


class QpbProtoFile(ProtoFile):
    def __init__(
        self,
        fdesc: descriptor.FileDescriptorProto,
        options: Values,
        spp_version: Version,
    ):
        """Takes a file, file descriptor and options to generate a QpbProtoFile."""
        super().__init__(fdesc, options, spp_version)

        self.includes = []

    def create_message(self, name, message, parent, message_options):
        return QpbMessage(name, message, parent, message_options, self.options)

    def add_dependency(self, other):
        super().add_dependency(other)

        if other.get_target_base() != self.get_target_base():
            self.includes.append(other.get_target_base())

    def generate_type_header(self, options: Values):
        """Generate content for a header file.
        Generates strings, which should be concatenated and stored to file.
        """

        yield "/* Automatically generated qpb types header */\n"
        yield f"/* SPP version {self.spp_version} */\n"
        yield f"/* Generated by {qpb_version_header} */\n\n"

        include_guard = "{identifier}_TYPES_INCLUDED".format(
            identifier=Support.make_c_identifier(self.get_target_base())
        )
        yield f"#ifndef {include_guard}\n"
        yield f"#define {include_guard}\n"
        yield "\n"
        yield Support.c_include("Tools/QuickProtobuf/qpb_types.h")
        yield "\n"

        for incfile in self.includes:
            yield Support.c_include(incfile + "_types.qpb.h")
        yield "\n"

        # Add check for 64 bit support
        for msg in self.messages:
            if any(f.data_type.is_64bit for f in msg.fields):
                yield "#ifdef QPB_WITHOUT_64BIT\n"
                yield "#error 64bit types requires 64bit support.\n"
                yield "#endif\n"
                yield "\n"
                break

        yield "#ifdef __cplusplus\n"
        yield 'extern "C" {\n'
        yield "#endif\n\n"

        if self.enums:
            yield "/* Enum definitions */\n"
            for enum in self.enums:
                yield "".join(QpbProtoFile.generate_enum_typedef(enum))
                yield "\n"

        if self.messages:
            yield "/* Struct definitions */\n"
            for msg in Support.sort_dependencies(self.messages):
                yield msg.generate_typedef_needs(True)
                yield msg.generate_typedef(True)
                yield "\n\n"
                yield msg.generate_typedef_needs(False)
                yield msg.generate_typedef(False)
                yield "\n\n"

        yield "#ifdef __cplusplus\n"
        yield '} /* extern "C" */\n'
        yield "#endif\n"

        # End of header
        yield f"\n#endif /* {include_guard} */\n"

    def generate_header(self, options: Values):
        """Generate content for a header file.
        Generates strings, which should be concatenated and stored to file.
        """

        yield "/* Automatically generated qpb header */\n"
        yield f"/* SPP version {self.spp_version} */\n"
        yield f"/* Generated by {qpb_version_header} */\n\n"

        include_guard = "{identifier}_INCLUDED".format(
            identifier=Support.make_c_identifier(self.get_target_base())
        )
        yield f"#ifndef {include_guard}\n"
        yield f"#define {include_guard}\n"
        yield "\n"
        yield Support.c_include(self.get_target_base() + "_types.qpb.h")
        yield "\n"
        for incfile in self.includes:
            yield Support.c_include(incfile + ".qpb.h")
        yield "\n"
        yield Support.c_include("Tools/QuickProtobuf/qpb.h")
        yield "\n"

        yield f"#if QPB_PROTO_HEADER_VERSION != {qpb_version}\n"
        yield "#error Regenerate this file with the current version of qpb generator.\n"
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

            yield "/* Encoding / decoding functions\n"
            yield " * Returns true on success, false on any failure.\n"
            yield " * Notes on Decode:\n"
            yield " * User is expected to provide a struct with wanted/default values (all zeroes).\n"
            yield " * A case where default values are not wanted is if you want to merge two messages\n"
            yield " * i.e. update only the fields that exist in the new message.\n"
            yield " * Note: These functions supports NULL termination of messages which most other\n"
            yield " *       protobuf implementations do not just so you know\n"
            yield " */\n"
            for msg in Support.sort_dependencies(self.messages):
                yield "".join(msg.generate_encode(True, False))
                yield "".join(msg.generate_decode(True, False))
                yield "".join(msg.generate_encode(False, False))
                yield "".join(msg.generate_decode(False, False))
                yield "\n"

        yield "#ifdef __cplusplus\n"
        yield '} /* extern "C" */\n'
        yield "#endif\n"

        # End of header
        yield f"\n#endif /* {include_guard} */\n"

    def generate_source(self, options: Values):
        """Generate content for a source file."""

        has_processed_types = False
        float_defines = {}
        if self.messages:
            for msg in self.messages:
                for field in msg.fields:
                    if field.is_processed():
                        has_processed_types = True
                        data_type = field.get_data_type()
                        if (
                            hasattr(data_type, "scale")
                            and float(data_type.scale) not in float_defines
                        ):
                            float_define = CSupport.float_define(data_type.scale)
                            float_defines[
                                float(data_type.scale)
                            ] = f"#define {float_define:<20} {data_type.scale}f\n"

        yield "/* Automatically generated qpb constant definitions */\n"
        yield f"/* Generated by {qpb_version_header} */\n\n"
        yield Support.c_include(self.get_target_base() + ".qpb.h")
        yield Support.c_include("Tools/QuickProtobuf/qpb_decode.h")
        yield Support.c_include("Tools/QuickProtobuf/qpb_encode.h")
        if has_processed_types:
            yield Support.c_include("Tools/CSupport/ConversionSupport.h")
        yield "\n"

        yield f"#if QPB_PROTO_HEADER_VERSION != {qpb_version}\n"
        yield "#error Regenerate this file with the current version of qpb generator.\n"
        yield "#endif\n"
        yield "\n"

        if len(float_defines) > 0:
            for key, define_str in sorted(float_defines.items()):
                yield define_str
            yield "\n"

        for msg in Support.sort_dependencies(self.messages):
            yield msg.generate_fields_functions(True, False)
            yield msg.generate_fields_functions(False, False)

        yield "\n"
        for msg in Support.sort_dependencies(self.messages):
            yield msg.generate_decoder_array(True)
            yield msg.generate_decoder_array(False)

        for msg in Support.sort_dependencies(self.messages):
            yield msg.generate_fields_functions(True, True)
            yield msg.generate_fields_functions(False, True)

        yield "/* Encoding / decoding functions */\n"
        for msg in Support.sort_dependencies(self.messages):
            yield "".join(msg.generate_encode(True, True))
            yield "".join(msg.generate_decode(True, True))
            yield "".join(msg.generate_encode(False, True))
            yield "".join(msg.generate_decode(False, True))

        # Add check for sizeof(double)
        has_double = False
        for msg in self.messages:
            for field in msg.fields:
                if (
                    field.data_type.get_ctype(True) == "double"
                    or field.data_type.get_ctype(False) == "double"
                ):
                    has_double = True
                    break
            if has_double:
                break

        if has_double:
            yield "/* On some platforms (such as AVR), double is really float.\n"
            yield " * These are not directly supported by qpb.\n"
            yield " * To get rid of this error, remove any double fields from your .proto.\n"
            yield " */\n"
            yield "QPB_STATIC_ASSERT(sizeof(double) == 8, DOUBLE_MUST_BE_8_BYTES)\n"

    @staticmethod
    def generate_enum_typedef(enum: EnumDefinition):
        c_type_name = enum.get_full_name().to_string("_")
        enum_min = enum.values[0].get_full_name().to_string("_")
        enum_max = enum.values[-1].get_full_name().to_string("_")
        yield f"typedef enum _{c_type_name} {{\n"
        yield ",\n".join(
            [
                "    {name} = {number}".format(
                    name=enum_value.get_full_name().to_string("_"),
                    number=enum_value.number,
                )
                for enum_value in enum.values
            ]
        )
        yield "\n}"
        yield f" {c_type_name};\n"
        yield f"#define {c_type_name}_MIN {enum_min}\n"
        yield f"#define {c_type_name}_MAX {enum_max}\n"
        yield f"#define {c_type_name}_ARRAYSIZE (({c_type_name})({enum_max}+1))\n"


class QpbGenerator(Generator):
    def create_proto_file(self, fdesc: descriptor.FileDescriptorProto):
        return QpbProtoFile(fdesc, self.options, self.spp_version)

    def generate_result(self):
        result = []
        filename = self.proto_file.get_target_base()
        base_name = f"{filename}.qpb"
        type_header_name = f"{filename}_types.qpb.h"
        header_name = f"{base_name}.h"
        source_name = f"{base_name}.c"

        type_header = GeneratorResult(
            type_header_name,
            "".join(self.proto_file.generate_type_header(self.options)),
        )
        header = GeneratorResult(
            header_name, "".join(self.proto_file.generate_header(self.options))
        )
        source = GeneratorResult(
            source_name, "".join(self.proto_file.generate_source(self.options))
        )
        result.append(type_header)
        result.append(header)
        result.append(source)

        return result


def main(plugin: bool = True):
    generator = QpbGenerator()
    optparser = OptionParser()

    run_generator(generator, optparser, plugin)
