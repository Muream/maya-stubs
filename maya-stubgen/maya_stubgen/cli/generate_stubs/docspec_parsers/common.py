import docspec 

__all__ = [
    "NULL_LOCATION",
]


NULL_LOCATION = docspec.Location("", 0)

def degraded_function(name: str) -> docspec.Function:

    return docspec.Function(
        location=NULL_LOCATION,
        name=name,
        docstring=None,
        modifiers=None,
        args=[
            docspec.Argument(
                NULL_LOCATION,
                "*args",
                docspec.Argument.Type.POSITIONAL_REMAINDER,
                decorations=None,
                datatype="Any",
                default_value=None,
            ),
            docspec.Argument(
                NULL_LOCATION,
                "**kwargs",
                docspec.Argument.Type.KEYWORD_REMAINDER,
                decorations=None,
                datatype="Any",
                default_value=None,
            ),
        ],
        return_type="Any",
        decorations=None,
        semantic_hints=[],
    )

