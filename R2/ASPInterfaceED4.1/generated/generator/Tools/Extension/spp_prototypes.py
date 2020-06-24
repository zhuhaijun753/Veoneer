"""This file contains the Proto types
"""
import Tools.Extension.spp_support as Support
from Tools.Extension.spp_support import (
    Allocation,
    EncodedSize,
    NumericType,
    Fixed32NumericType,
    Fixed64NumericType,
)

Support.verify_imports()

# Availability checked by verify_imports
import Tools.Extension.SystemOptions_pb2 as so


def get_scale(field_options: so.SystemFieldOptions):
    scale_str = None
    if field_options.scale != "":
        scale_str = field_options.scale
        if "." not in scale_str:
            scale_str += ".0"
        # Check that string represents a float
        # This will raise an error if string is not float
        float(scale_str)

    return scale_str


class ProtoType:
    """Base properties for all proto types"""

    def __init__(
        self,
        field_options: so.SystemFieldOptions,
        identifier: int,
        allow_pointer: bool,
        pbtype: int,
    ):
        self.allow_pointer = allow_pointer
        self.max_size = None
        self.max_count = None
        self.encoded_size = None
        self.packable = False
        self.pbtype = pbtype
        self.id = identifier
        self.tag = self.id << 3 | self.pbtype
        self.is_64bit = False

        if field_options.type == so.FT_STATIC:
            self.allocation = Allocation.STATIC
        elif field_options.type == so.FT_POINTER:
            if not allow_pointer:
                raise ValueError("Pointer type not allowed")

            self.allocation = Allocation.POINTER
        else:
            raise NotImplementedError(field_options.type)

    def handle_dependencies(self, dependencies):
        return

    def get_name(self):
        raise NotImplementedError(
            f"Type specification missing for ProtoType {self.__class__.__name__}"
        )

    def get_tag_size(self):
        return Support.varint_max_size(self.id << 3)

    def get_encoded_size(self):
        # Add Id + wire type for completeness
        return self.encoded_size + self.get_tag_size() if self.encoded_size else None


class VarintProtoType(ProtoType):
    int_sizer = {
        NumericType.I32: {
            so.IS_8: NumericType.I8,
            so.IS_16: NumericType.I16,
            so.IS_32: NumericType.I32,
        },
        NumericType.I64: {
            so.IS_8: NumericType.I8,
            so.IS_16: NumericType.I16,
            so.IS_32: NumericType.I32,
            so.IS_64: NumericType.I64,
        },
        NumericType.S32: {
            so.IS_8: NumericType.S8,
            so.IS_16: NumericType.S16,
            so.IS_32: NumericType.S32,
        },
        NumericType.S64: {
            so.IS_8: NumericType.S8,
            so.IS_16: NumericType.S16,
            so.IS_32: NumericType.S32,
            so.IS_64: NumericType.S64,
        },
        NumericType.U32: {
            so.IS_8: NumericType.U8,
            so.IS_16: NumericType.U16,
            so.IS_32: NumericType.U32,
        },
        NumericType.U64: {
            so.IS_8: NumericType.U8,
            so.IS_16: NumericType.U16,
            so.IS_32: NumericType.U32,
            so.IS_64: NumericType.U64,
        },
    }

    def __init__(
        self,
        field_options: so.SystemFieldOptions,
        identifier: int,
        numeric_type: NumericType,
    ):
        super().__init__(field_options, identifier, False, 0)
        self.packable = True
        self.numeric_type = numeric_type
        self.min = None
        self.max = None
        self.scale = None
        self.is_64bit = numeric_type.name.endswith("64")

        int_size = field_options.int_size
        if int_size != so.IS_DEFAULT:
            try:
                self.numeric_type = self.int_sizer[numeric_type][int_size]
            except KeyError:
                pass
            except Exception:
                raise Exception("Int size specified but something unknown went wrong")

        if numeric_type != NumericType.ENUM and numeric_type != NumericType.BOOL:
            self._check_int_support(field_options)

    def _read_min(self, field_options, raw_min):
        scale = float(self.scale) if self.scale is not None else None
        self.min = Support.scale_value(scale, raw_min)

        if field_options.min != 0 or field_options.force_min_max_usage:
            proposed_min = Support.get_int_reverse_scale(scale, field_options.min)
            if raw_min <= proposed_min:
                self.min = field_options.min
            else:
                allowed_str = (
                    (f"{self.min}")
                    if self.min == raw_min
                    else f"{self.min} [{raw_min}]"
                )
                raise Exception(
                    f"Min value not supported by numeric type. "
                    f"Allowed: {allowed_str}, proposed value: {field_options.min}"
                )

        self.int_min = Support.get_int_reverse_scale(scale, self.min)

    def _read_max(self, field_options, raw_max):
        scale = float(self.scale) if self.scale is not None else None
        self.max = Support.scale_value(scale, raw_max)

        if field_options.max != 0 or field_options.force_min_max_usage:
            proposed_max = Support.get_int_reverse_scale(scale, field_options.max)
            if raw_max >= proposed_max:
                self.max = field_options.max
            else:
                allowed_str = (
                    f"{self.max}" if self.max == raw_max else f"{self.max} [{raw_max}]"
                )
                raise Exception(
                    f"Max value not supported by numeric type. "
                    f"Allowed: {allowed_str}, proposed value: {field_options.max}"
                )

        self.int_max = Support.get_int_reverse_scale(scale, self.max)

    def _calculate_encoded_size(self, raw_min, raw_max):
        min_encoded = Support.varint_max_size(raw_min)
        max_encoded = Support.varint_max_size(raw_max)

        self.encoded_size = EncodedSize(max(min_encoded, max_encoded))

        int_min = self.int_min
        int_max = self.int_max
        if self.numeric_type.name.startswith("S"):
            int_min = Support.svarint_convert(int_min)
            int_max = Support.svarint_convert(int_max)

        min_size = Support.varint_max_size(int_min)
        max_size = Support.varint_max_size(int_max)

        self.encoded_size.add_reduction(
            self.encoded_size.value - max(min_size, max_size)
        )

    def _check_int_support(self, field_options):
        self.scale = get_scale(field_options)
        raw_min, raw_max = Support.get_numeric_range(self.numeric_type)

        self._read_min(field_options, raw_min)
        self._read_max(field_options, raw_max)

        if self.numeric_type.name.startswith("S"):
            raw_min = Support.svarint_convert(raw_min)
            raw_min = Support.svarint_convert(raw_max)

        self._calculate_encoded_size(raw_min, raw_max)

    def get_name(self):
        return self.numeric_type.name


class EnumProtoType(VarintProtoType):
    def __init__(
        self, field_options: so.SystemFieldOptions, identifier: int, type_name: str
    ):
        super().__init__(field_options, identifier, NumericType.ENUM)
        self.type_name = type_name
        self.enum_definition = None

    def handle_dependencies(self, dependencies):
        if self.type_name in dependencies:
            self.enum_definition = dependencies[self.type_name]
            self.encoded_size = self.enum_definition.encoded_size
        else:
            # Conservative assumption
            self.encoded_size = EncodedSize(10)

    def get_name(self):
        return self.type_name


class BoolProtoType(VarintProtoType):
    def __init__(self, field_options: so.SystemFieldOptions, identifier: int):
        super().__init__(field_options, identifier, NumericType.BOOL)
        self.encoded_size = EncodedSize(1)

    def get_name(self):
        return "boolean"


class FixedProtoType(ProtoType):
    def __init__(
        self,
        field_options: so.SystemFieldOptions,
        identifier: int,
        numeric_type,
        pbtype: int,
    ):
        super().__init__(field_options, identifier, False, pbtype)
        self.packable = True
        self.numeric_type = numeric_type
        self.bits = None
        self.scale = None
        self.min = None
        self.max = None
        if (
            self.numeric_type != Fixed32NumericType.FLOAT
            and self.numeric_type != Fixed64NumericType.DOUBLE
        ):
            self.scale = get_scale(field_options)
        scale = float(self.scale) if self.scale is not None else None
        raw_min, raw_max = Support.get_numeric_range(self.numeric_type)
        self.min = Support.scale_value(scale, raw_min)
        self.max = Support.scale_value(scale, raw_max)

    def get_name(self):
        return self.numeric_type.name.lower()


class Fixed32ProtoType(FixedProtoType):
    def __init__(
        self,
        field_options: so.SystemFieldOptions,
        identifier: int,
        numeric_type: Fixed32NumericType,
    ):
        super().__init__(field_options, identifier, numeric_type, 5)
        self.encoded_size = EncodedSize(4)
        self.bits = 32


class Fixed64ProtoType(FixedProtoType):
    def __init__(
        self,
        field_options: so.SystemFieldOptions,
        identifier: int,
        numeric_type: Fixed64NumericType,
    ):
        super().__init__(field_options, identifier, numeric_type, 1)
        self.encoded_size = EncodedSize(8)
        self.bits = 64
        self.is_64bit = True


class LengthDelimitedType(ProtoType):
    def __init__(
        self,
        field_options: so.SystemFieldOptions,
        identifier: int,
        allow_pointer: bool,
        require_max_size: bool,
    ):
        super().__init__(field_options, identifier, allow_pointer, 2)
        self.name = None
        self.max_size = None
        if field_options.max_size != 0:
            self.max_size = field_options.max_size
            self.encoded_size = EncodedSize(
                Support.varint_max_size(self.max_size) + self.max_size
            )
        elif require_max_size and self.allocation == Allocation.STATIC:
            raise Exception(f"Missing max_size {self.id} {self.allocation}")

    def get_name(self):
        if self.allocation == Allocation.STATIC:
            return f"{self.name}[{self.max_size}]"
        else:
            return f"*{self.name}"


class StringProtoType(LengthDelimitedType):
    def __init__(self, field_options: so.SystemFieldOptions, identifier: int):
        super().__init__(field_options, identifier, True, True)
        self.name = "String"


class BytesProtoType(LengthDelimitedType):
    def __init__(self, field_options: so.SystemFieldOptions, identifier: int):
        super().__init__(field_options, identifier, True, True)
        self.name = "Bytes"


class MessageProtoType(LengthDelimitedType):
    def __init__(
        self, field_options: so.SystemFieldOptions, identifier: int, message_type: str
    ):
        super().__init__(field_options, identifier, False, False)
        self.message_type = message_type
        self.message = None
        self.dependencies_handled = False

    def handle_dependencies(self, dependencies):
        if not self.dependencies_handled:
            if self.message_type in dependencies:
                self.message = dependencies[self.message_type]
                self.message.handle_dependencies(dependencies)
                self.encoded_size = self.message.get_encoded_size()

                if self.encoded_size is not None:
                    # Include submessage length prefix
                    self.encoded_size += Support.varint_max_size(
                        self.encoded_size.upperlimit()
                    )
                else:
                    # Submessage or its size cannot be found.
                    # This can occur if submessage is defined in different
                    # file, and it or its .options could not be found.
                    # Instead of direct numeric value, reference the size that
                    # has been #defined in the other file.
                    self.encoded_size = EncodedSize(self.message.type_name + "size")
                    # We will have to make a conservative assumption on the length
                    # prefix size, though.
                    self.encoded_size += 5
            self.dependencies_handled = True

    def get_name(self):
        return self.message_type


class ArrayProtoType(LengthDelimitedType):
    def __init__(
        self,
        field_options: so.SystemFieldOptions,
        identifier: int,
        data_type: ProtoType,
    ):
        super().__init__(field_options, identifier, data_type.allow_pointer, False)
        self.data_type = data_type
        self.is_64bit = self.data_type.is_64bit
        self.max_count = None
        self.dependencies_handled = False

        if field_options.max_count != 0:
            self.max_count = field_options.max_count
        else:
            raise Exception("Repeated field requires max_count to be set")

    def handle_dependencies(self, dependencies):
        if not self.dependencies_handled:
            self.data_type.handle_dependencies(dependencies)
            if self.allocation == Allocation.STATIC:
                self.encoded_size = self.data_type.get_encoded_size()
                # Decoders must always able to handle unpacked arrays.
                # Therefore we have to reserve space for it, even though
                # we emit packed arrays ourselves. For length of 1, packed
                # arrays are larger however so we need to add allowance
                # for the length byte.
                self.encoded_size *= self.max_count

                if self.max_count == 1:
                    self.encoded_size += 1

            self.dependencies_handled = True

    def get_name(self):
        return f"{self.data_type.get_name()}"

    def get_tag_size(self):
        return Support.varint_max_size(self.id << 3) * self.max_count

    def get_encoded_size(self):
        # No need to add ID since this is already considered by each element
        return self.encoded_size
