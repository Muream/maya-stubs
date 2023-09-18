import docstring_parser


def process_google_docstring(
    docstring: docstring_parser.Docstring,
) -> docstring_parser.Docstring:
    # docstring_parser doesn't parse the examples properly, let's make our own.
    for example in docstring.examples:
        if not example.description:
            continue

        # First let's remove poorly parsed example from the docstring object
        docstring.meta.remove(example)

        example_sections = example.description.split("\n\n")
        description: list[str] = []
        for example_section in example_sections:
            if example_section.startswith(">>>"):
                docstring.meta.append(
                    docstring_parser.common.DocstringExample(
                        args=["examples"],
                        description="\n\n".join(description),
                        snippet=example_section,
                    )
                )
                description = []
            else:
                # Add the current paragraph to the current description
                # the description will be used then cleared when encountering a snippet.
                description.append(example_section)

    return docstring
