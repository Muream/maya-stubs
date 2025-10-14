from __future__ import annotations


import docspec

__all__ = ["degraded_function"]


def degraded_function(name: str) -> docspec.Function:
    return docspec.Function(
        name=name,
        docstring=None,
        modifiers=None,
        args=[
            docspec.Argument(
                "args",
                docspec.Argument.Type.POSITIONAL_REMAINDER,
                datatype="Any",
                default_value=None,
            ),
            docspec.Argument(
                "kwargs",
                docspec.Argument.Type.KEYWORD_REMAINDER,
                datatype="Any",
                default_value=None,
            ),
        ],
        return_type="Any",
        decorations=None,
        semantic_hints=[],
    )
