import re

from ..... import _logging

logger = _logging.getLogger(__name__)

__all__ = [
    "mel_to_python_type",
]

# | is a union unless it's used for on|off
union_regex = re.compile(r"(?<!on)\|(?!off)")
array_regex = re.compile(r"(?P<type>\w+)\[(?P<length>\d+|\.\.\.)?\]")
tuple_regex = re.compile(r"\[(?P<types>.+)\]")


def mel_to_python_type(type_name: str) -> str:
    """Transform the given MEL type to a python type

    Notes:
        None is converted to bool as an unnamed argument in mel is equivalent to a bool
        on|off is converted to bool
    """
    python_type = _parse_complex_type(type_name)
    if "Unknown" in python_type:
        logger.warning("Could not map MEL type to Python: %s", type_name)
    return python_type


def _parse_complex_type(type_name: str) -> str:
    if (match_union := union_regex.split(type_name)) and len(match_union) > 1:
        parts = [_parse_complex_type(part.strip()) for part in match_union]
        return "Union[{}]".format(", ".join(parts))
    elif match_array := array_regex.match(type_name):
        match_dict = match_array.groupdict()
        array_type = _parse_complex_type(match_dict["type"])
        if (length := match_dict.get("length")) and length != "...":
            return "Tuple[{}]".format(", ".join([array_type] * int(length)))
        else:
            return "List[{}]".format(array_type)
    elif match_tuple := tuple_regex.match(type_name):
        tuple_types = match_tuple["types"]
        return _parse_tuple(tuple_types)
    else:
        return _parse_simple_type(type_name)


# lenient tokenizer - just extract all types and brackets
# and ignore other characters
tuple_token_regex = re.compile(r"[\w|]+(?:\[[\d.]*\])?|[\[\]]")


def _parse_tuple(tuple_string: str) -> str:
    """
    Parses a tuple type, potentially with optional elements.
    The tuple string should be passed with its outer brackets removed.

    >>> _parse_tuple("int, int")
    Tuple[int, int]
    >>> _parse_tuple("int, [, int[], int, ]")
    Union[Tuple[int], Tuple[int, List[int], int]]
    >>> _parse_tuple("string, [, string, ], [, string, ]")
    Union[Tuple[str], Tuple[str, str], Tuple[str, str, str]]
    >>> _parse_tuple("[, int, int, int, ]")
    Union[Tuple[()], Tuple[int, int, int]]
    >>> _parse_tuple("String String[...]")
    Tuple[str, List[str]]
    >>> _parse_tuple("Int Float [ Float Float ]")
    Union[Tuple[int, float], Tuple[int, float, float, float]]
    >>> _parse_tuple("Float [ on|off Float ]")
    Union[Tuple[float], Tuple[float, bool, float]]
    """

    tokens = iter(tuple_token_regex.findall(tuple_string))
    element_groups: list[list[str]] = [[]]
    for token in tokens:
        if token == "[":
            # elements within brackets are optional; add as a new element group
            optional_elements: list[str] = []
            # scan elements until end of group
            for subtoken in tokens:
                if subtoken == "[":
                    # ignore unexpected opening brackets; don't attempt to handle
                    # nested optional elements, as it's unclear what that
                    # would even mean here
                    continue
                elif subtoken == "]":
                    break
                else:
                    optional_elements.append(subtoken)
            element_groups.append(optional_elements)
        elif token == "]":
            # ignore unexpected brackets
            continue
        else:
            # elements not in brackets are interpreted as required
            # and are placed in the first element group
            element_groups[0].append(token)

    union_parts: list[str] = []
    seen_elements: list[str] = []
    for element_group in element_groups:
        seen_elements.extend(_parse_complex_type(element) for element in element_group)
        union_parts.append("Tuple[{}]".format(", ".join(seen_elements) or "()"))

    if len(union_parts) == 1:
        return union_parts[0]
    else:
        return "Union[{}]".format(", ".join(union_parts))


def _parse_simple_type(type_name: str) -> str:
    type_map = {
        # str
        "string": "str",
        "name": "str",
        "selectionitem": "str",
        "script": "Callable[..., Any]",
        # float
        "float": "float",
        "double": "float",
        "length": "float",
        "angle": "float",
        "linear": "float",
        # int
        "int": "int",
        "int64": "int",
        "unsignedint": "int",
        "uint": "int",
        "time": "int",
        "indexrange": "int",
        # bool
        "": "bool",
        "boolean": "bool",
        None: "bool",
        "none": "bool",
        "on|off": "bool",
        "any": "Any",
        # ranges
        "timerange": "NullableRange[float]",
        "floatrange": "Range[float]",
    }
    return type_map.get(type_name.lower(), "Unknown")
