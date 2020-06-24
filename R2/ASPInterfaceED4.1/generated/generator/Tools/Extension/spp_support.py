"""Grouping of support functionality needed by the generators
"""

from enum import Enum
from functools import reduce
import sys


class Allocation(Enum):
    NONE = 0
    STATIC = 1
    POINTER = 2


class Names:
    """Keeps a set of nested names and formats them to an identifier."""

    def __init__(self, parts=()):
        if isinstance(parts, Names):
            parts = parts.parts
        elif isinstance(parts, (str,)):
            parts = (parts,)
        self.parts = tuple(parts)

    def __str__(self):
        return self.to_string(".")

    def __add__(self, other):
        if isinstance(other, (str,)):
            return Names(self.parts + (other,))
        elif isinstance(other, Names):
            return Names(self.parts + other.parts)
        else:
            raise TypeError("Name parts should be of type str")

    def remove_from_beginning(self, other):
        del_list = []
        if isinstance(other, (str,)):
            del_list = (other,)
        elif isinstance(other, Names):
            del_list = other.parts

        new_parts = None
        for i in range(0, len(del_list)):
            if self.parts[i] != del_list[i]:
                new_parts = self.parts[i:]
                break

        if not new_parts:
            new_parts = self.parts[len(del_list):]

        return Names(new_parts)

    def __eq__(self, other):
        return isinstance(other, Names) and self.parts == other.parts

    def to_string(self, separator: str):
        return separator.join(self.parts)

    def empty(self):
        return len(self.parts) == 0

    @staticmethod
    def from_type_name(type_name: str):
        """Parse Names() from FieldDescriptorProto type_name"""
        if type_name[0] != ".":
            raise NotImplementedError(
                "Lookup of non-absolute type names is not supported"
            )
        return Names(type_name[1:].split("."))

    @staticmethod
    def from_package_name_and_type(package_name: "Names", type_name: str):
        names = package_name
        names += type_name
        return names


class EncodedSize:
    """Class used to represent the encoded size of a field or a message.
       Consists of a combination of symbolic sizes and integer sizes.
    """

    def __init__(self, value=0, symbols=[], reduction=0):
        if isinstance(value, EncodedSize):
            self.value = value.value
            self.symbols = value.symbols
            self.reduction = value.reduction
        elif isinstance(value, (str,) + (Names,)):
            self.symbols = [str(value)]
            self.value = 0
            self.reduction = 0
        else:
            self.value = value
            self.symbols = symbols
            self.reduction = reduction

    def __add__(self, other):
        if isinstance(other, int):
            return EncodedSize(self.value + other, self.symbols, self.reduction)
        elif isinstance(other, (str,) + (Names,)):
            return EncodedSize(self.value, self.symbols + [str(other)], self.reduction)
        elif isinstance(other, EncodedSize):
            return EncodedSize(
                self.value + other.value,
                self.symbols + other.symbols,
                self.reduction + other.reduction,
            )
        else:
            raise TypeError("Cannot add size: " + repr(other))

    def __mul__(self, other):
        if isinstance(other, int):
            return EncodedSize(
                self.value * other,
                [str(other) + "*" + s for s in self.symbols],
                self.reduction * other,
            )
        else:
            raise TypeError("Cannot multiply size: " + repr(other))

    def __str__(self):
        if not self.symbols:
            return str(self.value)
        else:
            return "({}{})".format(
                str(self.value) + " + " if self.value != 0 else "",
                " + ".join(self.symbols),
            )

    def string_with_reduction(self):
        if not self.symbols:
            if self.reduction == 0:
                return str(self.value)
            else:
                return f"{self.value} [{self.value - self.reduction}]"
        else:
            result = "(" + str(self.value) + " + " + " + ".join(self.symbols)
            if self.reduction != 0:
                result += " - " + str(self.reduction)
            result += ")"
            return result

    def add_reduction(self, reduction):
        self.reduction += reduction

    def upperlimit(self):
        if not self.symbols:
            return self.value
        else:
            return 2 ** 32 - 1


class NumericType(Enum):
    """These should not overlap with Fixed32NumericType or Fixed64NumericType.
       This so that these can co exist in the same dict.
    """

    NONE = 0
    I8 = 1
    I16 = 2
    I32 = 3
    I64 = 4
    U8 = 5
    U16 = 6
    U32 = 7
    U64 = 8
    S8 = 9
    S16 = 10
    S32 = 11
    S64 = 12
    ENUM = 15
    BOOL = 16


class Fixed32NumericType(Enum):
    """These should not overlap with NumericType or Fixed64NumericType.
       This so that these can co exist in the same dict.
    """

    FIXED32 = 20
    SFIXED32 = 21
    FLOAT = 22


class Fixed64NumericType(Enum):
    """These should not overlap with NumericType or Fixed32NumericType.
       This so that these can co exist in the same dict.
    """

    FIXED64 = 30
    SFIXED64 = 31
    DOUBLE = 32


"""Use map non standard types to standard "C" types
"""
NUMERIC_MAPPER = {
    NumericType.S8: NumericType.I8,
    NumericType.S16: NumericType.I16,
    NumericType.S32: NumericType.I32,
    NumericType.S64: NumericType.I64,
    Fixed32NumericType.FIXED32: NumericType.U32,
    Fixed32NumericType.SFIXED32: NumericType.I32,
    Fixed64NumericType.FIXED64: NumericType.U64,
    Fixed64NumericType.SFIXED64: NumericType.I64,
}

"""Numeric ranges for all supported datatypes used to evaluate that
   seleced values are in range
"""
NUMERIC_RANGE = {
    NumericType.I8: (-(2 ** 7), 2 ** 7 - 1),
    NumericType.I16: (-(2 ** 15), 2 ** 15 - 1),
    NumericType.I32: (-(2 ** 31), 2 ** 31 - 1),
    NumericType.I64: (-(2 ** 63), 2 ** 63 - 1),
    NumericType.U8: (0, 2 ** 8 - 1),
    NumericType.U16: (0, 2 ** 16 - 1),
    NumericType.U32: (0, 2 ** 32 - 1),
    NumericType.U64: (0, 2 ** 64 - 1),
    NumericType.BOOL: (0, 1),
    Fixed32NumericType.FLOAT: (
        -(2 - (2 ** -23)) * (2 ** 127),
        (2 - (2 ** -23)) * (2 ** 127),
    ),
    Fixed64NumericType.DOUBLE: (
        -(1 + (1 - 2 ** -52)) * (2 ** 1023),
        (1 + (1 - 2 ** -52)) * (2 ** 1023),
    ),
}


def snake_case_to_camel_case(snake_case):
    tokens = snake_case.split("_")
    return tokens[0] + "".join(word.capitalize() for word in tokens[1:])


def snake_case_to_pascal_case(snake_case):
    tokens = snake_case.split("_")
    return "".join(word.capitalize() for word in tokens)


def varint_max_size(max_value):
    """Returns the maximum number of bytes a varint can take when encoded."""
    max_value = int(max_value)
    if max_value < 0:
        max_value = 2 ** 64 - max_value
    for i in range(1, 11):
        if (max_value >> (i * 7)) == 0:
            return i
    raise ValueError("Value too large for varint: " + str(max_value))


def svarint_convert(value):
    if value < 0:
        return ~value << 1
    else:
        return value << 1


def make_c_identifier(headername):
    """Make #ifndef identifier that contains uppercase A-Z and digits 0-9"""
    result = ""
    for c in headername.upper():
        if c.isalnum():
            result += c
        else:
            result += "_"
    return result


def toposort2(data):
    """Topological sort.
    From http://code.activestate.com/recipes/577413-topological-sort/
    This function is under the MIT license.
    """
    for k, v in list(data.items()):
        v.discard(k)  # Ignore self dependencies
    extra_items_in_deps = reduce(set.union, list(data.values()), set()) - set(
        data.keys()
    )
    data.update(dict([(item, set()) for item in extra_items_in_deps]))
    while True:
        ordered = set(item for item, dep in list(data.items()) if not dep)
        if not ordered:
            break
        for item in sorted(ordered):
            yield item
        data = dict(
            [
                (item, (dep - ordered))
                for item, dep in list(data.items())
                if item not in ordered
            ]
        )
    assert not data, "A cyclic dependency exists amongst %r" % data


def sort_dependencies(messages: "Message"):
    """Sort a list of Messages based on dependencies."""
    dependencies = {}
    message_by_name = {}
    for message in messages:
        dependencies[str(message.get_full_name())] = set(message.get_dependencies())
        message_by_name[str(message.get_full_name())] = message
    for msgname in toposort2(dependencies):
        if msgname in message_by_name:
            yield message_by_name[msgname]


def get_int_reverse_scale(scale: float, value: float):
    int_value = int(round(value / scale)) if scale else int(value)
    return int_value


def scale_value(scale: float, value: float):
    return scale * value if scale else value


def get_basic_numeric_type(numeric_type):
    if numeric_type in NUMERIC_RANGE:
        return numeric_type
    else:
        return get_basic_numeric_type(NUMERIC_MAPPER[numeric_type])


def get_numeric_range(numeric_type: NumericType):
    return NUMERIC_RANGE[get_basic_numeric_type(numeric_type)]


def strip_float(float_str: str):
    return float_str.rstrip("0").rstrip(".") if "." in float_str else float_str


def verify_imports():
    try:
        import google.protobuf.descriptor_pb2 as descriptor
        import google.protobuf.compiler.plugin_pb2 as plugin
    except BaseException:
        sys.stderr.write(
            """
             *************************************************************
             *** Could not import the Google protobuf Python libraries ***
             *** Try installing package 'protobuf' or similar.  ***
             *************************************************************
        """
            + "\n"
        )
        raise

    try:
        import Tools.Extension.SystemOptions_pb2 as so
        import Tools.Extension.DataSources_pb2 as ds
        import Tools.Extension.SystemProductsProtocolVersion_pb2 as spp_file_version
    except TypeError:
        sys.stderr.write(
            """
             ****************************************************************************
             *** Got TypeError when importing the protocol definitions for generator. ***
             *** This usually means that the protoc in your path doesn't match the    ***
             *** Python protobuf library version.                                     ***
             ***                                                                      ***
             *** Please check the output of the following commands:                   ***
             *** which protoc                                                         ***
             *** protoc --version                                                     ***
             *** python -c 'import google.protobuf; print(google.protobuf.__file__)'  ***
             *** If you are not able to find the python protobuf version using the    ***
             *** above command, use this command.                                     ***
             *** pip freeze | grep -i protobuf                                        ***
             ****************************************************************************
        """
            + "\n"
        )
        raise
    except BaseException:
        sys.stderr.write(
            """
             ********************************************************************
             *** Failed to import the protocol definitions for generator.     ***
             ********************************************************************
        """
            + "\n"
        )
        raise


def c_include(file: str):
    return f'#include "{file}"\n'


def c_library_include(file: str):
    return f"#include <{file}>\n"
