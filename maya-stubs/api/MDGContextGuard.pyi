from typing import *
from typing_extensions import Self
from _typeshed import Incomplete

__all__: list
__builtins__: dict
__cached__: str
__doc__: str
__file__: str
__loader__: SourceFileLoader
__name__: str
__package__: str
__spec__: ModuleSpec

class MDGContextGuard:
    def _MDGContextGuard__save_state(self, new_current_context: Any) -> Any:
        """Save the state of the current evaluation context"""
    __doc__: str = ...
    def __enter__(self) -> Any:
        """Begin the scope, the work is done in __init__"""
    def __exit__(self, object_type: Any, value: Any, traceback: Any) -> Any:
        """Ensure the state is restored if this object goes out of scope"""
    def __init__(self, context: Any) -> Any:
        """Initialize the object with a specific context"""
    __module__: str = ...
    @property
    def __weakref__(*args: Any, **kwargs: Any) -> Any:
        """list of weak references to the object (if defined)"""
    @__weakref__.setter
    def __weakref__(*args: Any, **kwargs: Any) -> Any:
        """list of weak references to the object (if defined)"""
    def context(self) -> Any:
        """Return the context that was passed into this object on entry/construction"""
    def original_context(self) -> Any:
        """Return the context that was current when this object was entered/constructed"""
    def restore(self) -> Any:
        """Restore the context on entry/construction to be the current evaluation context"""
