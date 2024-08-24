from __future__ import annotations


import docspec

__all__ = [
    "NULL_LOCATION",
    "degraded_function",
    "DocspecModuleMembers",
    "DocspecClassMembers",
]


NULL_LOCATION = docspec.Location("", 0)

# DocspecModuleMembers = (
#     docspec.Variable
#     | docspec.Function
#     | docspec.Class
#     | docspec.Module
#     | docspec.Indirection
# )
DocspecModuleMembers = docspec._ModuleMemberType

DocspecClassMembers = (
    docspec.Variable | docspec.Function | docspec.Class | docspec.Indirection
)


def degraded_function(name: str) -> docspec.Function:
    return docspec.Function(
        location=NULL_LOCATION,
        name=name,
        docstring=None,
        modifiers=None,
        args=[
            docspec.Argument(
                NULL_LOCATION,
                "args",
                docspec.Argument.Type.POSITIONAL_REMAINDER,
                decorations=None,
                datatype="Any",
                default_value=None,
            ),
            docspec.Argument(
                NULL_LOCATION,
                "kwargs",
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
