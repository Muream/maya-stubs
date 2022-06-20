from typing import *
from typing_extensions import Self
from _typeshed import Incomplete

class MDGContextGuard:
    def context(self: Self) -> Any:
        """Return the context that was passed into this object on entry/construction"""
    def original_context(self: Self) -> Any:
        """Return the context that was current when this object was entered/constructed"""
    def restore(self: Self) -> Any:
        """Restore the context on entry/construction to be the current evaluation context"""
