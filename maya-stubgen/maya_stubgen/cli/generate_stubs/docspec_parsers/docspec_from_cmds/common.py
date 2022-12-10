import re
from enum import Enum

__all__ = [
    "mel_to_python_type",
]

array_regex = re.compile(r"(?P<type>\w+)\[(?P<length>\d+)?\]")
tuple_regex = re.compile(r"\[(?P<types>(\w+(, )?)+)\]")


def mel_to_python_type(type_name: str) -> str:
    """Transform the given MEL type to a python type

    Notes:
        None is converted to bool as an unnamed argument in mel is equivalent to a bool
        on|off is converted to bool
    """
    type_map = {
        # str
        "string": "str",
        "name": "str",
        "script": "Callable",
        # float
        "float": "float",
        "length": "float",
        "angle": "float",
        # int
        "int": "int",
        "int64": "int",
        "unsignedint": "int",
        "time": "int",
        # bool
        "": "bool",
        "boolean": "bool",
        None: "bool",
        "none": "bool",
        "on|off": "bool",
        "any": "Any",
    }

    class SequenceType(Enum):
        NONE = "None"
        LIST = "List"
        TUPLE = "Tuple"

    type_name = type_name.lower()

    match_array = array_regex.match(type_name)
    match_tuple = tuple_regex.match(type_name)

    if match_array:
        match_dict = match_array.groupdict()
        type_name = match_dict.get("type")
        length = int(match_dict.get("length") or 0)

        python_type = type_map.get(type_name, "Incomplete")
        if length:
            sequence_type = SequenceType.TUPLE
            python_type = ", ".join([python_type] * length)
        else:
            sequence_type = SequenceType.LIST
    elif match_tuple:
        match_dict = match_tuple.groupdict()
        types = match_dict["types"].split(", ")
        python_types = [type_map.get(t.lower(), "Incomplete") for t in types]
        python_type = ", ".join(python_types)
        sequence_type = SequenceType.TUPLE
    else:
        sequence_type = SequenceType.NONE
        python_type = type_map.get(type_name, "Incomplete")

    if sequence_type is not SequenceType.NONE:
        python_type = f"{sequence_type.value}[{python_type}]"

    return python_type

