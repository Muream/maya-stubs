from __future__ import annotations

from typing import *


Unknown = Any

class MDGContextGuard:
    """Scoping object to manage changes to the current evaluation context"""
    def _MDGContextGuard__save_state(self, new_current_context: Unknown) -> Any:
        """Save the state of the current evaluation context"""

    def __enter__(self) -> Any:
        """Begin the scope, the work is done in __init__"""

    def __exit__(self, object_type: Unknown, value: Unknown, traceback: Unknown) -> Any:
        """Ensure the state is restored if this object goes out of scope"""

    def __init__(self, context: Unknown) -> None:
        """Initialize the object with a specific context"""

    def context(self) -> Any:
        """Return the context that was passed into this object on entry/construction"""

    def original_context(self) -> Any:
        """Return the context that was current when this object was entered/constructed"""

    def restore(self) -> Any:
        """Restore the context on entry/construction to be the current evaluation context"""


