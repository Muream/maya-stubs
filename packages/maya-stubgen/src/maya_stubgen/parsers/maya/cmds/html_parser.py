"""A Docspec parser for maya.cmds"""

from __future__ import annotations

import logging
import re
import textwrap
from typing import Optional, Union

import bs4
import docspec
import docstring_parser
import httpx

from ....utils import cache_dir, maya_version
from ...common import NULL_LOCATION
from ... import Parser
from .common import mel_to_python_type

logger = logging.getLogger(__name__)

__all__ = [
    "DocumentationNotFound",
    "CmdsDocsParser",
]


# The base URL for all maya commands doc pages
_BASE_COMMAND_URL = (
    "https://help.autodesk.com/cloudhelp/{maya_version}/"
    "ENU/Maya-Tech-Docs/CommandsPython/{command}.html"
)


def cmds_documentation_url(command: str) -> str:
    return _BASE_COMMAND_URL.format(maya_version=maya_version(), command=command)


# #: Reusable request session to improve performance when
# #: getting pages from the same domain
# requests_session = requests.Session()


flag_name_re = re.compile(r"(?P<long_name>\w+)\((?P<short_name>\w*)\)")

properties_re = re.compile(
    r"is (?P<not_undoable>NOT )?undoable, "
    r"(?P<not_queryable>NOT )?queryable, and "
    r"(?P<not_editable>NOT )?editable"
)

# if this is present in the argument description,
# the argument does not become bool in query mode
query_mandatory_value_str = "In query mode, this flag needs a value"


class DocumentationNotFound(Exception):
    """Raised when the HTML Documentation is not found for the maya command."""


class CmdsDocsParser(Parser):
    def parse_package(self, name: str) -> list[docspec.Module]:
        raise NotImplementedError

    def parse_module(self, name: str) -> docspec.Module:
        raise NotImplementedError

    def parse_function(
        self,
        module_name: str,
        name: str,
        synopsis_function: Optional[docspec.Function] = None,
    ) -> docspec.Function:
        """Returns a `Function` object from the command's HTML documentation

        Args:
            name: the name of the function to parse

        Raises:
            DocumentationNotFound: when the documentation page isn't available.

        Returns:
            the Function with all the relevant data parsed from the docs.
        """
        logger.debug("Scraping docs for: %s", name)

        try:
            documentation = get_documentation(name)
        except DocumentationNotFound as exc:
            # Explicitly re-raise the error
            raise exc from exc

        soup = bs4.BeautifulSoup(documentation, "html.parser")

        docspec_args: list[docspec.Argument] = []
        docstring_parser_params: list[docstring_parser.DocstringParam] = []
        queryable_types: list[str] = []
        docspec_return = None
        docstring_parser_return: list[docstring_parser.DocstringReturns] = []
        docstring_parser_example = None

        # We iterate over the H2 titles as they act as nice section delimitations.
        if isinstance(flag_title := soup.find("h2", string="Flags"), bs4.Tag):
            synopsis_title = soup.select_one("#synopsis")
            docspec_args, docstring_parser_params, queryable_types = get_arguments(
                flag_title, synopsis_title, synopsis_function
            )
        if isinstance(return_title := soup.find("h2", string="Return value"), bs4.Tag):
            docspec_return, docstring_parser_return = get_return_type(
                return_title, queryable_types
            )
        if isinstance(
            examples_title := soup.find("h2", string="Python examples"), bs4.Tag
        ):
            docstring_parser_example = get_examples(examples_title)

        # The docstring is the only piece of text in the body that has no tag.
        body_text = []
        if body := soup.body:
            body_text = [
                t.text.strip() for t in body.find_all(string=True, recursive=False)
            ]

        # filter the "," and "", that we get with the previous line.
        body_text = [t for t in body_text if len(t) > 1]
        description = "".join(body_text)

        docstring_parser_docstring = docstring_parser.Docstring()
        docstring_parser_docstring.long_description = description

        docstring_parser_docstring.meta.extend(docstring_parser_return)
        docstring_parser_docstring.meta.extend(docstring_parser_params)

        if docstring_parser_example:
            docstring_parser_docstring.meta.append(docstring_parser_example)

        docstring = docstring_parser.compose(
            docstring_parser_docstring, docstring_parser.DocstringStyle.GOOGLE
        )

        docspec_docstring = docspec.Docstring(NULL_LOCATION, content=docstring)

        return docspec.Function(
            location=NULL_LOCATION,
            name=name,
            docstring=docspec_docstring,
            modifiers=[],
            args=docspec_args,
            return_type=docspec_return,
            decorations=None,
            semantic_hints=[],
        )

    def parse_variable(self, module_name: str, name: str) -> docspec.Variable:
        raise NotImplementedError

    def parse_class(self, module_name: str, name: str) -> docspec.Class:
        raise NotImplementedError


def get_return_type(
    title: bs4.Tag,
    queryable_types: list[str],
) -> tuple[str, list[docstring_parser.DocstringReturns]]:
    return_types: list[Union[str, None]] = []
    return_descriptions: list[str] = []
    next_tag = title.find_next_sibling()
    if isinstance(next_tag, bs4.Tag) and next_tag.name == "table":
        for return_type_row in next_tag.find_all("tr"):
            if not isinstance(return_type_row, bs4.Tag):
                continue

            columns = [t.text.strip() for t in return_type_row.find_all("td")]
            try:
                return_type, return_description = columns
            except ValueError:
                # the first row of the return value table sometimes only has one column
                # in the 2024 documentation; seems to indicate no return value?
                # see e.g. instanceable
                return_type = None
                (return_description,) = columns
            return_types.append(return_type)
            return_descriptions.append(return_description)
    elif next_tag and next_tag.name == "p":
        return_types.append(next_tag.text)
        return_descriptions.append(
            "\n".join([p.text for p in next_tag.find_next_siblings("p")])
        )
    else:
        raise ValueError(
            f"Unspported Tag Type for return types {next_tag.name if next_tag else 'Not Found'}"
        )

    python_types = [
        mel_to_python_type(return_type) if return_type is not None else "None"
        for return_type in return_types
    ]
    # add the types of the flags that can be queried in query mode
    python_types.extend(queryable_types)

    docstring_returns = [
        docstring_parser.DocstringReturns(
            ["returns"],
            description=return_description,
            type_name=return_type,
            is_generator=False,
            return_name=None,
        )
        for return_type, return_description in zip(python_types, return_descriptions)
    ]

    # using dict.fromkeys to dedup types instead of set to ensure order is preserved,
    # so order can't change between executions
    unique_types = list(dict.fromkeys(python_types))
    union_type = (
        unique_types[0]
        if len(unique_types) == 1
        else "Union[{}]".format(", ".join(unique_types))
    )

    return union_type, docstring_returns


def copy_or_create_arg(
    source_func: Optional[docspec.Function], name: str, datatype: str
) -> docspec.Argument:
    if source_func is not None and source_func.args:
        for arg in source_func.args:
            if arg.name == name:
                return arg

    return docspec.Argument(
        location=NULL_LOCATION,
        name=name,
        type=docspec.Argument.Type.KEYWORD_ONLY,
        datatype=datatype,
        default_value="...",
    )


def get_arguments(
    title: bs4.Tag,
    synopsis: Optional[bs4.Tag],
    synopsis_function: Optional[docspec.Function] = None,
) -> tuple[list[docspec.Argument], list[docstring_parser.DocstringParam], list[str]]:
    """Get the docspec arguments.

    Returns:
        The docspec arguments along with their descriptions.
    """

    #: The docspec arguments we'll return, along with their descriptions.
    arguments: list[docspec.Argument] = []
    argument_docs: list[docstring_parser.DocstringParam] = []
    queryable_types: list[str] = []

    if synopsis is not None and (props := synopsis.find_next_sibling("p")):
        if m := properties_re.search(props.text):
            if not m["not_editable"]:
                arguments.append(
                    copy_or_create_arg(
                        synopsis_function,
                        name="edit",
                        datatype="bool",
                    )
                )

            if not m["not_queryable"]:
                arguments.append(
                    copy_or_create_arg(
                        synopsis_function,
                        name="query",
                        datatype="bool",
                    )
                )

    flag_links: list[Union[bs4.Tag, bs4.NavigableString]] = []
    #: The <table> containing all the information for the flags.
    if isinstance(table := title.find_next("table"), bs4.Tag):
        # each link in the table corresponds to a flag name
        # this is the easiest way to get all the rows that define each argument
        flag_links = table.find_all("a")

    for link in flag_links:
        # We can now easily get the parent row of the link to get access
        flag_data_row = link.find_parent("tr")
        if not flag_data_row:
            continue

        long_name = None
        flag_type = "Unknown"
        properties = []
        for i, child in enumerate(flag_data_row.find_all("td", recursive=False)):
            if i == 0:
                # First column is the flag name
                name = child.text.strip()
                match = flag_name_re.match(name)
                if match:
                    long_name = match["long_name"]
            elif i == 1:
                # Second column is the flag Type
                flag_type = mel_to_python_type(child.text.strip())
            elif i == 2:
                properties = [img["alt"] for img in child.find_all("img")]

        if not long_name:
            logger.warning(
                "Could not extract flag name from table row: %s", flag_data_row
            )
            continue

        flag_description = ""
        if flag_description_row := flag_data_row.find_next_sibling("tr"):
            flag_description = flag_description_row.text.strip()

        flag_description = flag_description.replace("\\n\\0", "")

        # Standardize numbered lists
        # `1 - `, `1: `, etc. are converted to `1. `
        flag_description = re.sub(r"(\d+)\s?[:-]\s?", r"\1. ", flag_description)

        if properties:
            flag_description += f"\nProperties: {', '.join(properties)}"

        # make sure everything following the first line is indented properly.
        # Wrapped in a try except because some descriptions only have one line
        # and can't be split between a short and long description.
        try:
            short_desc, long_desc = flag_description.split("\n", 1)
            long_desc = textwrap.indent(long_desc, "    ")
            flag_description = "\n".join([short_desc, long_desc])
        except:
            pass

        # Support markdown's hard line breaks
        flag_description = flag_description.replace("\n", "  \n")

        if "multiuse" in properties:
            flag_type = "Multiuse[{}]".format(flag_type)

        if "query" in properties and query_mandatory_value_str not in flag_description:
            queryable_types.append(flag_type)
            if flag_type != "bool":
                flag_type = "Queryable[{}]".format(flag_type)

        argument_docs.append(
            docstring_parser.DocstringParam(
                args=["param"],
                description=flag_description,
                arg_name=long_name,
                type_name=flag_type,
                is_optional=True,
                default=None,
            )
        )

        arguments.append(
            docspec.Argument(
                location=NULL_LOCATION,
                name=long_name,
                type=docspec.Argument.Type.KEYWORD_ONLY,
                decorations=None,
                datatype=flag_type,
                default_value="...",
            )
        )

    return arguments, argument_docs, list(dict.fromkeys(queryable_types))


def get_examples(title: bs4.Tag) -> docstring_parser.common.DocstringExample:
    snippet = ""
    if pre := title.find_next("pre"):
        snippet = pre.text
    snippet = snippet.replace("import maya.cmds as cmds", "from maya import cmds")

    return docstring_parser.common.DocstringExample(
        args=["example"],
        snippet=snippet,
        description=None,
    )


def get_documentation(command_name: str) -> str:
    """Get the HTML Documentation for the given command

    Args:
        command_name: The command to get the documentation for.

    Raises:
        DocumentationNotFound: when the documentation page isn't available.

    Returns:
        The content of the HTML documentation page.
    """

    cache_page = cache_dir() / "docs" / "maya" / "cmds" / f"{command_name}.html"
    if not cache_page.exists():
        command_url = cmds_documentation_url(command_name)
        logger.debug("Downloading documentation: %s", command_url)

        response = httpx.get(command_url)

        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            # Explicitly raise a more specific error that is meant to be caught upstream.
            raise DocumentationNotFound(
                f"Documentation not found for {command_name}"
            ) from exc

        logger.debug("Writing documentation cache: %s", cache_page)
        cache_page.parent.mkdir(parents=True, exist_ok=True)
        with cache_page.open("w", encoding="utf8") as f:
            f.write(response.text)
    else:
        logger.debug("Found existing documentation cache: %s", cache_page)

    return cache_page.read_text()
