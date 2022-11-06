"""A Docspec parser for maya.cmds"""

import logging
import re
import textwrap
from pathlib import Path
from typing import List, Tuple

import bs4
import docspec
import docstring_parser
import requests

from ..common import NULL_LOCATION
from .common import mel_to_python_type

logger = logging.getLogger(__name__)

__all__ = [
    "DocumentationNotFound",
    "function_from_documentation",
]

#: The base URL for all maya commands doc pages
cmds_documentation_url = (
    "https://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/{}.html"
)

#: Reusable request session to improve performance when
#: getting pages from the same domain
requests_session = requests.Session()


flag_name_re = re.compile(r"(?P<long_name>\w+)\((?P<short_name>\w*)\)")


class DocumentationNotFound(Exception):
    """Raised when the HTML Documentation is not found for the maya command."""


def function_from_documentation(command_name: str) -> docspec.Function:
    """Returns a `Function` object from the command's HTML documentation

    Args:
        command: the name of the command

    Raises:
        DocumentationNotFound: when the documentation page isn't available.

    Returns:
        the Function with all the relevant data parsed from the doc.
    """
    logger.debug("Scraping docs for: %s", command_name)

    try:
        documentation = get_documentation(command_name)
    except DocumentationNotFound as exc:
        # Explicitly re-raise the error
        raise exc from exc

    soup = bs4.BeautifulSoup(documentation, "html.parser")

    docspec_args: List[docspec.Argument] = []
    docstring_parser_params = []
    docspec_return = None
    docstring_parser_return = None
    docstring_parser_example = None

    # We iterate over the H2 titles as they act as nice section delimitations.
    for title in soup.find_all("h2"):
        title: bs4.Tag
        if title.text == "Return value":
            docspec_return, docstring_parser_return = get_return_type(title)
        if title.text == "Flags":
            arguments = get_arguments(title)
            docspec_args = [arg[0] for arg in arguments]
            docstring_parser_params = [arg[1] for arg in arguments]
        if title.text == "Python examples":
            docstring_parser_example = get_examples(title)

    # The docstring is the only piece of text in the body that has no tag.
    body_text = [t.strip() for t in soup.body.findAll(text=True, recursive=False)]

    # filter the "," and "", that we get with the previous line.
    body_text = [t for t in body_text if len(t) > 1]
    description = "".join(body_text)

    docstring_parser_docstring = docstring_parser.Docstring()
    docstring_parser_docstring.long_description = description

    if docstring_parser_return is not None:
        docstring_parser_docstring.meta.append(docstring_parser_return)
    docstring_parser_docstring.meta.extend(docstring_parser_params)

    if docstring_parser_example:
        docstring_parser_docstring.meta.append(docstring_parser_example)

    docstring = docstring_parser.compose(
        docstring_parser_docstring, docstring_parser.DocstringStyle.GOOGLE
    )

    docspec_docstring = docspec.Docstring(NULL_LOCATION, content=docstring)

    return docspec.Function(
        location=NULL_LOCATION,
        name=command_name,
        docstring=docspec_docstring,
        modifiers=[],
        args=docspec_args,
        return_type=docspec_return,
        decorations=None,
        semantic_hints=[],
    )


def get_return_type(title: bs4.Tag) -> Tuple[str, docstring_parser.DocstringReturns]:
    next_tag: bs4.Tag = title.find_next_sibling()
    if next_tag.name == "table":
        first_return_type_row = next_tag.find("tr")
        return_type, return_description = [
            t.text.strip() for t in first_return_type_row.find_all("td")
        ]
    elif next_tag.name == "p":
        return_type = next_tag.text
        return_description = "\n".join(
            [p.text for p in next_tag.find_next_siblings("p")]
        )
    else:
        raise ValueError(f"Unspported Tag Type for return types {next_tag.name}")

    return_type = mel_to_python_type(return_type)

    return (
        return_type,
        docstring_parser.DocstringReturns(
            ["returns"],
            description=return_description,
            type_name=return_type,
            is_generator=False,
            return_name=None,
        ),
    )


def get_arguments(
    title: bs4.Tag,
) -> List[Tuple[docspec.Argument, docstring_parser.DocstringParam]]:
    """Get the docspec arguments.

    Args:

    Returns:
        The docspec arguments along with their descriptions.
    """

    #: The docspec arguments we'll return, along with their descriptions.
    arguments: List[Tuple[docspec.Argument, docstring_parser.DocstringParam]] = []

    #: The <table> containing all the information for the flags.
    table = title.find_next("table")

    # each link in the table corresponds to a flag name
    # this is the easiest way to get all the rows that define each argument
    flag_links = table.find_all("a")

    for link in flag_links:
        # We can now easily get the parent row of the link to get access
        flag_data_row: bs4.Tag = link.find_parent("tr")
        long_name = None
        flag_type = None
        properties = []
        for i, child in enumerate(flag_data_row.findChildren("td")):
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

        flag_description_row = flag_data_row.find_next_sibling("tr")
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

        docstring_param = docstring_parser.DocstringParam(
            args=["param"],
            description=flag_description,
            arg_name=long_name,
            type_name=flag_type,
            is_optional=True,
            default=None,
        )

        docspec_arg = docspec.Argument(
            location=NULL_LOCATION,
            name=long_name,
            type=docspec.Argument.Type.KEYWORD_ONLY,
            decorations=None,
            datatype=flag_type,
            default_value="...",
        )
        arguments.append((docspec_arg, docstring_param))

    return arguments


def get_examples(title: bs4.Tag) -> docstring_parser.common.DocstringExample:
    snippet = title.find_next("pre").text
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

    cache_page = Path() / ".cache" / "docs" / "maya" / "cmds" / f"{command_name}.html"
    cache_page = cache_page.resolve()
    if not cache_page.exists():
        command_url = cmds_documentation_url.format(command_name)

        response = requests_session.get(command_url)

        try:
            response.raise_for_status()
        except requests.HTTPError as exc:
            # Explicitly raise a more specific error that is meant to be caught upstream.
            raise DocumentationNotFound(
                f"Documentation not found for {command_name}"
            ) from exc

        cache_page.parent.mkdir(parents=True, exist_ok=True)
        with cache_page.open("w", encoding="utf8") as f:
            f.write(response.text)

    logger.debug("Documentation cache: %s", str(cache_page))

    return cache_page.read_text()
