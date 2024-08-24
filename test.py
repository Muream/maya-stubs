from maya import cmds

# from __future__ import annotations

# import time
# import asyncio
# import cProfile
# import logging
# import pstats
# import re
# import textwrap
# from pathlib import Path
# from typing import Any, Coroutine, Iterator, Optional, TypeVar

# import aiofiles
# import bs4
# import docspec
# import docspec_to_jinja
# import docstring_parser
# import httpx

# logger = logging.getLogger(__name__)

# base_url = "https://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython"

# flag_name_re = re.compile(r"(?P<long_name>\w+)\((?P<short_name>\w*)\)")

# properties_re = re.compile(
#     r"is (?P<not_undoable>NOT )?undoable, "
#     r"(?P<not_queryable>NOT )?queryable, and "
#     r"(?P<not_editable>NOT )?editable"
# )


# query_mandatory_value_str = "In query mode, this flag needs a value"

# union_regex = re.compile(r"(?<!on)\|(?!off)")
# array_regex = re.compile(r"(?P<type>\w+)\[(?P<length>\d+|\.\.\.)?\]")
# tuple_regex = re.compile(r"\[(?P<types>.+)\]")


# T = TypeVar("T")


# NULL_LOCATION = docspec.Location("", 0)


# def chunks(lst: list[T], n: int) -> Iterator[list[T]]:
#     """Yield successive n-sized chunks from lst."""
#     for i in range(0, len(lst), n):
#         yield lst[i : i + n]


# async def fetch(url: str, client: httpx.AsyncClient) -> str:
#     print(f"Fetching URL {url}")
#     cache_dir = Path() / ".cache/docs/maya/cmds"
#     local_file = cache_dir / url.rpartition("/")[-1]

#     if local_file.exists():
#         print("Found Local Cache")
#         async with aiofiles.open(local_file, "r") as f:
#             return await f.read()
#         # return await aiofiles.open(local_file.read_text()

#     resp = await client.get(url)
#     local_file.write_text(resp.text, encoding="utf8")

#     return resp.text


# async def crawl(client: httpx.AsyncClient) -> list[str]:
#     pages: list[str] = []

#     index_url = base_url + "/index_all.html"
#     content = await fetch(index_url, client)

#     soup = bs4.BeautifulSoup(content, "html.parser")
#     for link in soup.select("a"):
#         href = link["href"]
#         assert isinstance(href, str)
#         pages.append(f"{base_url}/{href}")

#     return pages


# async def scrape(url: str, client: httpx.AsyncClient) -> docspec.Function:
#     """Returns a `Function` object from the command's HTML documentation

#     Args:
#         name: the name of the function to parse

#     Raises:
#         DocumentationNotFound: when the documentation page isn't available.

#     Returns:
#         the Function with all the relevant data parsed from the docs.
#     """
#     synopsis_function = None

#     name = url.split("/")[-1].split(".")[0]
#     # logger.debug("Scraping docs for: %s", name)
#     print(f"Scraping docs for: {name}")

#     documentation = await fetch(url, client)

#     soup = bs4.BeautifulSoup(documentation, "lxml")

#     docspec_args: list[docspec.Argument] = []
#     docstring_parser_params: list[docstring_parser.DocstringParam] = []
#     queryable_types: list[str] = []
#     docspec_return = None
#     docstring_parser_return: list[docstring_parser.DocstringReturns] = []

#     # We iterate over the H2 titles as they act as nice section delimitations.
#     if isinstance(flag_title := soup.find("h2", string="Flags"), bs4.Tag):
#         synopsis_title = soup.select_one("#synopsis")
#         docspec_args, docstring_parser_params, queryable_types = get_arguments(
#             flag_title, synopsis_title, synopsis_function
#         )
#     if isinstance(return_title := soup.find("h2", string="Return value"), bs4.Tag):
#         docspec_return, docstring_parser_return = get_return_type(
#             return_title, queryable_types
#         )
#     # if isinstance(
#     #     examples_title := soup.find("h2", string="Python examples"), bs4.Tag
#     # ):
#     #     docstring_parser_example = get_examples(examples_title)

#     # The docstring is the only piece of text in the body that has no tag.
#     body_text = []
#     if body := soup.body:
#         body_text = [
#             t.text.strip() for t in body.find_all(string=True, recursive=False)
#         ]

#     # filter the "," and "", that we get with the previous line.
#     body_text = [t for t in body_text if len(t) > 1]
#     description = "".join(body_text)

#     docstring_parser_docstring = docstring_parser.Docstring()
#     docstring_parser_docstring.long_description = description

#     docstring_parser_docstring.meta.extend(docstring_parser_return)
#     docstring_parser_docstring.meta.extend(docstring_parser_params)

#     # if docstring_parser_example:
#     #     docstring_parser_docstring.meta.append(docstring_parser_example)

#     docstring = docstring_parser.compose(
#         docstring_parser_docstring, docstring_parser.DocstringStyle.GOOGLE
#     )

#     docspec_docstring = docspec.Docstring(NULL_LOCATION, content=docstring)

#     return docspec.Function(
#         location=NULL_LOCATION,
#         name=name,
#         docstring=docspec_docstring,
#         modifiers=[],
#         args=docspec_args,
#         return_type=docspec_return,
#         decorations=None,
#         semantic_hints=[],
#     )


# def get_return_type(
#     title: bs4.Tag,
#     queryable_types: list[str],
# ) -> tuple[str, list[docstring_parser.DocstringReturns]]:
#     return_types: list[str | None] = []
#     return_descriptions: list[str] = []
#     next_tag = title.find_next_sibling()
#     if isinstance(next_tag, bs4.Tag) and next_tag.name == "table":
#         for return_type_row in next_tag.find_all("tr"):
#             if not isinstance(return_type_row, bs4.Tag):
#                 continue

#             columns = [t.text.strip() for t in return_type_row.find_all("td")]
#             try:
#                 return_type, return_description = columns
#             except ValueError:
#                 # the first row of the return value table sometimes only has one column
#                 # in the 2024 documentation; seems to indicate no return value?
#                 # see e.g. instanceable
#                 return_type = None
#                 (return_description,) = columns
#             return_types.append(return_type)
#             return_descriptions.append(return_description)
#     elif next_tag and next_tag.name == "p":
#         return_types.append(next_tag.text)
#         return_descriptions.append(
#             "\n".join([p.text for p in next_tag.find_next_siblings("p")])
#         )
#     else:
#         raise ValueError(
#             f"Unspported Tag Type for return types {next_tag.name if next_tag else 'Not Found'}"
#         )

#     python_types = [
#         mel_to_python_type(return_type) if return_type is not None else "None"
#         for return_type in return_types
#     ]
#     # add the types of the flags that can be queried in query mode
#     python_types.extend(queryable_types)

#     docstring_returns = [
#         docstring_parser.DocstringReturns(
#             ["returns"],
#             description=return_description,
#             type_name=return_type,
#             is_generator=False,
#             return_name=None,
#         )
#         for return_type, return_description in zip(python_types, return_descriptions)
#     ]

#     # using dict.fromkeys to dedup types instead of set to ensure order is preserved,
#     # so order can't change between executions
#     unique_types = list(dict.fromkeys(python_types))
#     union_type = (
#         unique_types[0]
#         if len(unique_types) == 1
#         else "Union[{}]".format(", ".join(unique_types))
#     )

#     return union_type, docstring_returns


# def copy_or_create_arg(
#     source_func: Optional[docspec.Function], name: str, datatype: str
# ) -> docspec.Argument:
#     if source_func is not None and source_func.args:
#         for arg in source_func.args:
#             if arg.name == name:
#                 return arg

#     return docspec.Argument(
#         location=NULL_LOCATION,
#         name=name,
#         type=docspec.Argument.Type.KEYWORD_ONLY,
#         datatype=datatype,
#         default_value="...",
#     )


# def get_arguments(
#     title: bs4.Tag,
#     synopsis: Optional[bs4.Tag],
#     synopsis_function: Optional[docspec.Function] = None,
# ) -> tuple[list[docspec.Argument], list[docstring_parser.DocstringParam], list[str]]:
#     """Get the docspec arguments.

#     Returns:
#         The docspec arguments along with their descriptions.
#     """

#     #: The docspec arguments we'll return, along with their descriptions.
#     arguments: list[docspec.Argument] = []
#     argument_docs: list[docstring_parser.DocstringParam] = []
#     queryable_types: list[str] = []

#     if synopsis is not None and (props := synopsis.find_next_sibling("p")):
#         if m := properties_re.search(props.text):
#             if not m["not_editable"]:
#                 arguments.append(
#                     copy_or_create_arg(
#                         synopsis_function,
#                         name="edit",
#                         datatype="bool",
#                     )
#                 )

#             if not m["not_queryable"]:
#                 arguments.append(
#                     copy_or_create_arg(
#                         synopsis_function,
#                         name="query",
#                         datatype="bool",
#                     )
#                 )

#     flag_links: list[bs4.Tag | bs4.NavigableString] = []
#     #: The <table> containing all the information for the flags.
#     if isinstance(table := title.find_next("table"), bs4.Tag):
#         # each link in the table corresponds to a flag name
#         # this is the easiest way to get all the rows that define each argument
#         flag_links = table.find_all("a")

#     for link in flag_links:
#         # We can now easily get the parent row of the link to get access
#         flag_data_row = link.find_parent("tr")
#         if not flag_data_row:
#             continue

#         long_name = None
#         flag_type = "Unknown"
#         properties = []
#         for i, child in enumerate(flag_data_row.find_all("td", recursive=False)):
#             if i == 0:
#                 # First column is the flag name
#                 name = child.text.strip()
#                 match = flag_name_re.match(name)
#                 if match:
#                     long_name = match["long_name"]
#             elif i == 1:
#                 # Second column is the flag Type
#                 flag_type = mel_to_python_type(child.text.strip())
#             elif i == 2:
#                 properties = [img["alt"] for img in child.find_all("img")]

#         if not long_name:
#             logger.warning(
#                 "Could not extract flag name from table row: %s", flag_data_row
#             )
#             continue

#         flag_description = ""
#         if flag_description_row := flag_data_row.find_next_sibling("tr"):
#             flag_description = flag_description_row.text.strip()

#         flag_description = flag_description.replace("\\n\\0", "")

#         # Standardize numbered lists
#         # `1 - `, `1: `, etc. are converted to `1. `
#         flag_description = re.sub(r"(\d+)\s?[:-]\s?", r"\1. ", flag_description)

#         if properties:
#             flag_description += f"\nProperties: {', '.join(properties)}"

#         # make sure everything following the first line is indented properly.
#         # Wrapped in a try except because some descriptions only have one line
#         # and can't be split between a short and long description.
#         try:
#             short_desc, long_desc = flag_description.split("\n", 1)
#             long_desc = textwrap.indent(long_desc, "    ")
#             flag_description = "\n".join([short_desc, long_desc])
#         except:
#             pass

#         # Support markdown's hard line breaks
#         flag_description = flag_description.replace("\n", "  \n")

#         if "multiuse" in properties:
#             flag_type = "Multiuse[{}]".format(flag_type)

#         if "query" in properties and query_mandatory_value_str not in flag_description:
#             queryable_types.append(flag_type)
#             if flag_type != "bool":
#                 flag_type = "Queryable[{}]".format(flag_type)

#         argument_docs.append(
#             docstring_parser.DocstringParam(
#                 args=["param"],
#                 description=flag_description,
#                 arg_name=long_name,
#                 type_name=flag_type,
#                 is_optional=True,
#                 default=None,
#             )
#         )

#         arguments.append(
#             docspec.Argument(
#                 location=NULL_LOCATION,
#                 name=long_name,
#                 type=docspec.Argument.Type.KEYWORD_ONLY,
#                 decorations=None,
#                 datatype=flag_type,
#                 default_value="...",
#             )
#         )

#     return arguments, argument_docs, list(dict.fromkeys(queryable_types))


# def mel_to_python_type(type_name: str) -> str:
#     """Transform the given MEL type to a python type

#     Notes:
#         None is converted to bool as an unnamed argument in mel is equivalent to a bool
#         on|off is converted to bool
#     """
#     python_type = _parse_complex_type(type_name)
#     if "Unknown" in python_type:
#         logger.warning("Could not map MEL type to Python: %s", type_name)
#     return python_type


# def _parse_complex_type(type_name: str) -> str:
#     if (match_union := union_regex.split(type_name)) and len(match_union) > 1:
#         parts = [_parse_complex_type(part.strip()) for part in match_union]
#         return "Union[{}]".format(", ".join(parts))
#     elif match_array := array_regex.match(type_name):
#         match_dict = match_array.groupdict()
#         array_type = _parse_complex_type(match_dict["type"])
#         if (length := match_dict.get("length")) and length != "...":
#             return "Tuple[{}]".format(", ".join([array_type] * int(length)))
#         else:
#             return "List[{}]".format(array_type)
#     elif match_tuple := tuple_regex.match(type_name):
#         tuple_types = match_tuple["types"]
#         return _parse_tuple(tuple_types)
#     else:
#         return _parse_simple_type(type_name)


# # lenient tokenizer - just extract all types and brackets
# # and ignore other characters
# tuple_token_regex = re.compile(r"[\w|]+(?:\[[\d.]*\])?|[\[\]]")


# def _parse_tuple(tuple_string: str) -> str:
#     """
#     Parses a tuple type, potentially with optional elements.
#     The tuple string should be passed with its outer brackets removed.

#     >>> _parse_tuple("int, int")
#     Tuple[int, int]
#     >>> _parse_tuple("int, [, int[], int, ]")
#     Union[Tuple[int], Tuple[int, List[int], int]]
#     >>> _parse_tuple("string, [, string, ], [, string, ]")
#     Union[Tuple[str], Tuple[str, str], Tuple[str, str, str]]
#     >>> _parse_tuple("[, int, int, int, ]")
#     Union[Tuple[()], Tuple[int, int, int]]
#     >>> _parse_tuple("String String[...]")
#     Tuple[str, List[str]]
#     >>> _parse_tuple("Int Float [ Float Float ]")
#     Union[Tuple[int, float], Tuple[int, float, float, float]]
#     >>> _parse_tuple("Float [ on|off Float ]")
#     Union[Tuple[float], Tuple[float, bool, float]]
#     """

#     tokens = iter(tuple_token_regex.findall(tuple_string))
#     element_groups: list[list[str]] = [[]]
#     for token in tokens:
#         if token == "[":
#             # elements within brackets are optional; add as a new element group
#             optional_elements: list[str] = []
#             # scan elements until end of group
#             for subtoken in tokens:
#                 if subtoken == "[":
#                     # ignore unexpected opening brackets; don't attempt to handle
#                     # nested optional elements, as it's unclear what that
#                     # would even mean here
#                     continue
#                 elif subtoken == "]":
#                     break
#                 else:
#                     optional_elements.append(subtoken)
#             element_groups.append(optional_elements)
#         elif token == "]":
#             # ignore unexpected brackets
#             continue
#         else:
#             # elements not in brackets are interpreted as required
#             # and are placed in the first element group
#             element_groups[0].append(token)

#     union_parts: list[str] = []
#     seen_elements: list[str] = []
#     for element_group in element_groups:
#         seen_elements.extend(_parse_complex_type(element) for element in element_group)
#         union_parts.append("Tuple[{}]".format(", ".join(seen_elements) or "()"))

#     if len(union_parts) == 1:
#         return union_parts[0]
#     else:
#         return "Union[{}]".format(", ".join(union_parts))


# def _parse_simple_type(type_name: str) -> str:
#     type_map = {
#         # str
#         "string": "str",
#         "name": "str",
#         "selectionitem": "str",
#         "script": "Callable[..., Any]",
#         # float
#         "float": "float",
#         "double": "float",
#         "length": "float",
#         "angle": "float",
#         "linear": "float",
#         # int
#         "int": "int",
#         "int64": "int",
#         "unsignedint": "int",
#         "uint": "int",
#         "time": "int",
#         "indexrange": "int",
#         # bool
#         "": "bool",
#         "boolean": "bool",
#         None: "bool",
#         "none": "bool",
#         "on|off": "bool",
#         "any": "Any",
#         # ranges
#         "timerange": "NullableRange[float]",
#         "floatrange": "Range[float]",
#     }
#     return type_map.get(type_name.lower(), "Unknown")


# async def asdf():
#     async with httpx.AsyncClient() as client:
#         print("Crawling")
#         links = await crawl(client)
#         print("Found Links")
#         tasks: list[Coroutine[Any, Any, docspec.Function]] = []
#         for link in links:
#             tasks.append(scrape(link, client))

#         module = docspec.Module(
#             location=NULL_LOCATION,
#             name="maya.cmds",
#             docstring=None,
#             members=await asyncio.gather(*tasks),
#         )
#         # print(functions)

#         stub = docspec_to_jinja.render_module(module, "pyi")
#         path = Path() / "cmds.pyi"
#         path.write_text(stub)


# async def main():
#     # profiler = cProfile.Profile()
#     # profiler.enable()

#     t0 = time.time()
#     await asdf()
#     t1 = time.time()
#     print(t1 - t0)
#     # profiler.disable()

#     # stats = pstats.Stats(profiler)
#     # prof_file = (Path() / "temp" / "async_parser.prof").resolve()
#     # prof_file.parent.mkdir(exist_ok=True)
#     # stats.dump_stats(str(prof_file))


# if __name__ == "__main__":
#     asyncio.run(main())
