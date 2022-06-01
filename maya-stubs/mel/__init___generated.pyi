# fmt: off
from typing import *
from typing_extensions import Self
from _typeshed import Incomplete


__builtins__: dict
__cached__: str
__doc__: NoneType
__file__: str
__loader__: SourceFileLoader
__name__: str
__package__: str
__path__: list
__spec__: ModuleSpec
def createMelWrapper(fn: Any, types: Any = ..., retType: Any = ..., ignoreDefaultArgs: Any = ..., returnCmd: Any = ..., outDir: Any = ...) -> Any:
    """@brief Create a wrapper mel proc for a python function
    
        When the mel proc is invoked, it will call the python function, 
        passing any arguments it receives, and then return the function's
        result.

        Example:
            - I need a mel proc with signature: proc string[] fn(int $a, string $b)
            - I've created a python function to do the work in 'mymod.py' which looks like:
            - def fn(a,b): return [b]*a
            python>> import mymod
            python>> maya.mel.createMelWrapper(mymod.fn,types=['int','string'], retType='string[]')
            # Result: /users/username/maya/scripts/fn.mel # 
            mel>> rehash;
            mel>> string $as[] = fn(3,"a");
            // Result: a a a // 

        @param fn the function to wrap, must be a function.
        @param types string list of mel argument types to use, 
        defaults to all 'string'.
        @param retType mel return type of the function, must be convertible to
        what fn actually returns. None means return type is 'void'.
        @param ignoreDefaultArgs  True means arguments with default values will be
        ignored when creating the mel wrapper proc.
        @param returnCmd True means return the generated mel code that defines the 
        wrapper proc, False means write it to a mel file.
        @param outDir The directory to write the generated file to.  None means 
        prompt for the directory.
        @return path to generated mel proc OR generated mel code, depending on
        returnCmd.
    """
    ...
def eval(*args: Any, **kwargs: Any) -> Any:
    """Takes as input a string containing MEL code, evaluates it, and returns the result.

    This function takes a string which contains MEL code and evaluates it using 
    the MEL interpreter. The result is converted into a Python data type and is 
    returned.

    If an error occurs during the execution of the MEL script, a Python exception
    is raised with the appropriate error message.
    """
    ...
class zip(object):
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
    def __iter__(self: Self) -> Any:
        """Implement iter(self)."""
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
    def __next__(self: Self) -> Any:
        """Implement next(self)."""
        ...
    def __reduce__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return state information for pickling."""
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
