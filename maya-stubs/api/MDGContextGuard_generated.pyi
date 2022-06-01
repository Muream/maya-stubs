# fmt: off
from typing import *
from typing_extensions import Self
from _typeshed import Incomplete


class MDGContextGuard(object):
    def _MDGContextGuard__save_state(self: Self, new_current_context: Any) -> Any:
        """Save the state of the current evaluation context"""
        ...
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    __dict__: mappingproxy = ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __enter__(self: Self) -> Any:
        """Begin the scope, the work is done in __init__"""
        ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __exit__(self: Self, object_type: Any, value: Any, traceback: Any) -> Any:
        """Ensure the state is restored if this object goes out of scope"""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, context: Any) -> Any:
        """Initialize the object with a specific context"""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    __module__: str = ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    @property
    def __weakref__(*args: Any, **kwargs: Any) -> Any:
        """list of weak references to the object (if defined)"""
        ...
    @__weakref__.setter
    def __weakref__(*args: Any, **kwargs: Any) -> Any:
        """list of weak references to the object (if defined)"""
        ...
    def context(self: Self) -> Any:
        """Return the context that was passed into this object on entry/construction"""
        ...
    def original_context(self: Self) -> Any:
        """Return the context that was current when this object was entered/constructed"""
        ...
    def restore(self: Self) -> Any:
        """Restore the context on entry/construction to be the current evaluation context"""
        ...

__all__: list
__builtins__: dict
__cached__: str
__doc__: str
__file__: str
__loader__: SourceFileLoader
__name__: str
__package__: str
__spec__: ModuleSpec
class object:
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
