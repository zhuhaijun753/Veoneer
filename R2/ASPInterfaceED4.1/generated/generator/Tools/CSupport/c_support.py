"""Grouping of support functionality for c support code
"""


def get_float_to_int_convert_call(ctype: str, data: str, scale: str):
    unsigned = "u" if ctype.startswith("u") else ""
    bits = "64" if "64" in ctype else "32"
    conversion_int_type = f"{unsigned}int{bits}"
    int_type = ctype[:-2].upper()
    int_type_min = (f"{int_type}_MIN") if not int_type.startswith("U") else "0"
    int_type_max = f"{int_type}_MAX"
    return f"({ctype})convertTo{conversion_int_type.capitalize()}({data}, {scale}, {int_type_min}, {int_type_max})"


def float_define(float_str: str):
    return f"F_{float_str}".replace(".", "_").replace("-", "_MINUS_")
