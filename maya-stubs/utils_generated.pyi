# fmt: off
from typing import *
from typing_extensions import Self
from _typeshed import Incomplete


class MayaGuiLogHandler(Handler):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    __dict__: mappingproxy = ...
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
    def __init__(self: Self) -> Any: ...
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
    def __repr__(self: Self) -> Any: ...
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
    def _at_fork_reinit(self: Self) -> Any: ...
    def acquire(self: Self) -> Any:
        """Acquire the I/O thread lock."""
        ...
    def addFilter(self: Self, filter: Any) -> Any:
        """Add the specified filter to this handler."""
        ...
    def close(self: Self) -> Any:
        """Tidy up any resources used by the handler.

                This version removes the handler from an internal map of handlers,
                _handlers, which is used for handler lookup by name. Subclasses
                should ensure that this gets called from overridden close()
                methods.
        """
        ...
    def createLock(self: Self) -> Any:
        """Acquire a thread lock for serializing access to the underlying I/O."""
        ...
    def emit(self: Self, record: Any) -> Any: ...
    def filter(self: Self, record: Any) -> Any:
        """Determine if a record is loggable by consulting all the filters.

                The default is to allow the record to be logged; any filter can veto
                this and the record is then dropped. Returns a zero value if a record
                is to be dropped, else non-zero.

                .. versionchanged:: 3.2

                   Allow filters to be just callables.
        """
        ...
    def flush(self: Self) -> Any:
        """Ensure all logging output has been flushed.

                This version does nothing and is intended to be implemented by
                subclasses.
        """
        ...
    def format(self: Self, record: Any) -> Any:
        """Format the specified record.

                If a formatter is set, use it. Otherwise, use the default formatter
                for the module.
        """
        ...
    def get_name(self: Self) -> Any: ...
    def handle(self: Self, record: Any) -> Any:
        """Conditionally emit the specified logging record.

                Emission depends on filters which may have been added to the handler.
                Wrap the actual emission of the record with acquisition/release of
                the I/O thread lock. Returns whether the filter passed the record for
                emission.
        """
        ...
    def handleError(self: Self, record: Any) -> Any:
        """Handle errors which occur during an emit() call.

                This method should be called from handlers when an exception is
                encountered during an emit() call. If raiseExceptions is false,
                exceptions get silently ignored. This is what is mostly wanted
                for a logging system - most users will not care about errors in
                the logging system, they are more interested in application errors.
                You could, however, replace this with a custom handler if you wish.
                The record which was being processed is passed in to this method.
        """
        ...
    name: property = ...
    def release(self: Self) -> Any:
        """Release the I/O thread lock."""
        ...
    def removeFilter(self: Self, filter: Any) -> Any:
        """Remove the specified filter from this handler."""
        ...
    def setFormatter(self: Self, fmt: Any) -> Any:
        """Set the formatter for this handler."""
        ...
    def setLevel(self: Self, level: Any) -> Any:
        """Set the logging level of this handler.  level must be an int or a str."""
        ...
    def set_name(self: Self, name: Any) -> Any: ...

class Output(object):
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
    def flush(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Flush no-op"""
        ...
    softspace: member_descriptor = ...
    def write(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Write the given string"""
        ...
    def writelines(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Write the given sequence"""
        ...

class StringTable(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __delitem__(self: Self, key: Any) -> Any:
        """Delete self[key]."""
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
    def __getitem__(self: Self, key: Any) -> Any:
        """Return self[key]."""
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
    def __len__(self: Self) -> Any:
        """Return len(self)."""
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
    def __setitem__(self: Self, key: Any, value: Any) -> Any:
        """Set self[key] to value."""
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

__cached__: str
__doc__: str
__file__: str
__loader__: SourceFileLoader
__name__: str
__package__: str
__spec__: ModuleSpec
def _decodeStack(tbStack: Any) -> Any: ...
def _dumpCurrentFrames() -> Any: ...
def _fixConsoleLineNumbers(tbStack: Any) -> Any: ...
def formatGuiException(exceptionType: Any, exceptionObject: Any, traceBack: Any, detail: Any = ...) -> Any:
    """Format a trace stack into a string.

            exceptionType   : Type of exception
            exceptionObject : Detailed exception information
            traceBack       : Exception traceback stack information
            detail          : 0 = no trace info, 1 = line/file only, 2 = full trace
                          
        To perform an action when an exception occurs without modifying Maya's 
        default printing of exceptions, do the following::
    
            import maya.utils
            def myExceptCB(etype, value, tb, detail=2):
                # do something here...
                return maya.utils._formatGuiException(etype, value, tb, detail)
            maya.utils.formatGuiException = myExceptCB
    """
    ...
def formatGuiResult(obj: Any) -> Any:
    """Gets a string representation of a result object.

        To perform an action when a result is about to returned to the script editor
        without modifying Maya's default printing of results, do the following:
    
            import maya.utils
            def myResultCallback(obj):
                # do something here...
                return maya.utils._formatGuiResult(obj)
            maya.utils.formatGuiResult = myResultCallback
    """
    ...
def _guiExceptHook(exceptionType: Any, exceptionObject: Any, traceBack: Any, detail: Any = ...) -> Any:
    """Whenever Maya receives an error from the command engine it comes into here
        to format the message for display. 
        Formatting is performed by formatGuiException.
            exceptionType   : Type of exception
            exceptionObject : Detailed exception information
            traceBack       : Exception traceback stack information
            detail          : 0 = no trace info, 1 = line/file only, 2 = full trace
    """
    ...
_guiLogHandler: NoneType
def _guiResultHook(obj: Any) -> Any:
    """In GUI mode, called by the command engine to stringify a result for display."""
    ...
def _mayadisplayhook(*args: Any, **kwargs: Any) -> Any:
    """Display hook function used to capture interpreter results"""
    ...
def _overriden_import(*args: Any, **kwargs: Any) -> Any:
    """Import hook function used to capture import statement"""
    ...
def _prefixTraceStack(tbStack: Any, prefix: Any = ...) -> Any:
    """prefix with '#', being sure to get internal newlines. do not prefix first line
        as that will be added automatically.
    """
    ...
_shellLogHandler: StreamHandler
_shellStdoutLogHandler: NoneType
def abs_over(*args: Any, **kwargs: Any) -> Any:
    """abs"""
    ...
def all_over(*args: Any, **kwargs: Any) -> Any:
    """all"""
    ...
def any_over(*args: Any, **kwargs: Any) -> Any:
    """any"""
    ...
def ascii_over(*args: Any, **kwargs: Any) -> Any:
    """ascii"""
    ...
def bin_over(*args: Any, **kwargs: Any) -> Any:
    """bin"""
    ...
def bool_over(*args: Any, **kwargs: Any) -> Any:
    """bool"""
    ...
def breakpoint_over(*args: Any, **kwargs: Any) -> Any:
    """breakpoint"""
    ...
def bytearray_over(*args: Any, **kwargs: Any) -> Any:
    """bytearray"""
    ...
def bytes_over(*args: Any, **kwargs: Any) -> Any:
    """bytes"""
    ...
def callable_over(*args: Any, **kwargs: Any) -> Any:
    """callable"""
    ...
def chr_over(*args: Any, **kwargs: Any) -> Any:
    """chr"""
    ...
def classmethod_over(*args: Any, **kwargs: Any) -> Any:
    """classmethod"""
    ...
def compile_over(*args: Any, **kwargs: Any) -> Any:
    """compile"""
    ...
def complex_over(*args: Any, **kwargs: Any) -> Any:
    """complex"""
    ...
def delattr_over(*args: Any, **kwargs: Any) -> Any:
    """delattr"""
    ...
def dict_over(*args: Any, **kwargs: Any) -> Any:
    """dict"""
    ...
def dir_over(*args: Any, **kwargs: Any) -> Any:
    """dir"""
    ...
def divmod_over(*args: Any, **kwargs: Any) -> Any:
    """divmod"""
    ...
def enumerate_over(*args: Any, **kwargs: Any) -> Any:
    """enumerate"""
    ...
def eval_over(*args: Any, **kwargs: Any) -> Any:
    """eval"""
    ...
def exec_over(*args: Any, **kwargs: Any) -> Any:
    """exec"""
    ...
def execfile(filename: Any, myglobals: Any = ..., mylocals: Any = ...) -> Any:
    """Read and execute a Python script from a file in the given namespaces.
            The globals and locals are dictionaries, defaulting to the current
            globals and locals. If only globals is given, locals defaults to it.
    """
    ...
def executeDeferred(*args: Any, **kwargs: Any) -> Any:
    """Delays the execution of the given script or function until Maya is idle.

    This function runs code using the idle event loop.  This means that the
    main thread must become idle before this python code will be executed.

    There are two different ways to call this function.  The first is to
    supply a single string argument which contains the Python code to execute.
    In that case the code is interpreted.

    The second way to call this routine is to pass it a "callable" object.
    When that is the case, then the remaining regular arguments and keyword
    arguments will be passed to the callable object
    """
    ...
def executeInMainThreadWithResult(*args: Any, **kwargs: Any) -> Any:
    """Runs Python code in the main thread and waits for the return code.

    There are two different ways to call this function.  The first is to
    supply a single string argument which contains the Python code to execute.
    In that case the code is interpreted.

    The second way to call this routine is to pass it a "callable" object.
    When that is the case, then the remaining regular arguments and keyword
    arguments will be passed to the callable object

    Note that if this routine is called from the main thread, then it will
    simply execute the given Python on the spot and return the result
    """
    ...
def filter_over(*args: Any, **kwargs: Any) -> Any:
    """filter"""
    ...
def float_over(*args: Any, **kwargs: Any) -> Any:
    """float"""
    ...
def formatGuiException(exceptionType: Any, exceptionObject: Any, traceBack: Any, detail: Any = ...) -> Any:
    """Format a trace stack into a string.

            exceptionType   : Type of exception
            exceptionObject : Detailed exception information
            traceBack       : Exception traceback stack information
            detail          : 0 = no trace info, 1 = line/file only, 2 = full trace
                          
        To perform an action when an exception occurs without modifying Maya's 
        default printing of exceptions, do the following::
    
            import maya.utils
            def myExceptCB(etype, value, tb, detail=2):
                # do something here...
                return maya.utils._formatGuiException(etype, value, tb, detail)
            maya.utils.formatGuiException = myExceptCB
    """
    ...
def formatGuiResult(obj: Any) -> Any:
    """Gets a string representation of a result object.

        To perform an action when a result is about to returned to the script editor
        without modifying Maya's default printing of results, do the following:
    
            import maya.utils
            def myResultCallback(obj):
                # do something here...
                return maya.utils._formatGuiResult(obj)
            maya.utils.formatGuiResult = myResultCallback
    """
    ...
def format_over(*args: Any, **kwargs: Any) -> Any:
    """format"""
    ...
def frozenset_over(*args: Any, **kwargs: Any) -> Any:
    """frozenset"""
    ...
class futureStr(object):
    def __add__(self: Self, value: Any) -> Any:
        """Return self+value."""
        ...
    def __contains__(self: Self, key: Any) -> Any:
        """Return key in self."""
        ...
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
        """Return a formatted version of the string as described by format_spec."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __getitem__(self: Self, key: Any) -> Any:
        """Return self[key]."""
        ...
    def __getnewargs__(self: Self, *args: Any, **kwargs: Any) -> Any: ...
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
    def __len__(self: Self) -> Any:
        """Return len(self)."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __mod__(self: Self, value: Any) -> Any:
        """Return self%value."""
        ...
    def __mul__(self: Self, value: Any) -> Any:
        """Return self*value."""
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
    def __rmod__(self: Self, value: Any) -> Any:
        """Return value%self."""
        ...
    def __rmul__(self: Self, value: Any) -> Any:
        """Return value*self."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Return the size of the string in memory, in bytes."""
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
    def capitalize(self: Self) -> Any:
        """Return a capitalized version of the string.

        More specifically, make the first character have upper case and the rest lower
        case.
        """
        ...
    def casefold(self: Self) -> Any:
        """Return a version of the string suitable for caseless comparisons."""
        ...
    def center(self: Self, width: Any, fillchar: Any = ...) -> Any:
        """Return a centered string of length width.

        Padding is done using the specified fill character (default is a space).
        """
        ...
    def count(self: Self, *args: Any, **kwargs: Any) -> Any:
        """S.count(sub[, start[, end]]) -> int

        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are
        interpreted as in slice notation.
        """
        ...
    def encode(self: Self, encoding: Any = ..., errors: Any = ...) -> Any:
        """Encode the string using the codec registered for encoding.

          encoding
            The encoding in which to encode the string.
          errors
            The error handling scheme to use for encoding errors.
            The default is 'strict' meaning that encoding errors raise a
            UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
            'xmlcharrefreplace' as well as any other name registered with
            codecs.register_error that can handle UnicodeEncodeErrors.
        """
        ...
    def endswith(self: Self, *args: Any, **kwargs: Any) -> Any:
        """S.endswith(suffix[, start[, end]]) -> bool

        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """
        ...
    def expandtabs(self: Self, tabsize: Any = ...) -> Any:
        """Return a copy where all tab characters are expanded using spaces.

        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        ...
    def find(self: Self, *args: Any, **kwargs: Any) -> Any:
        """S.find(sub[, start[, end]]) -> int

        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.

        Return -1 on failure.
        """
        ...
    def format(self: Self, *args: Any, **kwargs: Any) -> Any:
        """S.format(*args, **kwargs) -> str

        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        ...
    def format_map(self: Self, *args: Any, **kwargs: Any) -> Any:
        """S.format_map(mapping) -> str

        Return a formatted version of S, using substitutions from mapping.
        The substitutions are identified by braces ('{' and '}').
        """
        ...
    def index(self: Self, *args: Any, **kwargs: Any) -> Any:
        """S.index(sub[, start[, end]]) -> int

        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.

        Raises ValueError when the substring is not found.
        """
        ...
    def isalnum(self: Self) -> Any:
        """Return True if the string is an alpha-numeric string, False otherwise.

        A string is alpha-numeric if all characters in the string are alpha-numeric and
        there is at least one character in the string.
        """
        ...
    def isalpha(self: Self) -> Any:
        """Return True if the string is an alphabetic string, False otherwise.

        A string is alphabetic if all characters in the string are alphabetic and there
        is at least one character in the string.
        """
        ...
    def isascii(self: Self) -> Any:
        """Return True if all characters in the string are ASCII, False otherwise.

        ASCII characters have code points in the range U+0000-U+007F.
        Empty string is ASCII too.
        """
        ...
    def isdecimal(self: Self) -> Any:
        """Return True if the string is a decimal string, False otherwise.

        A string is a decimal string if all characters in the string are decimal and
        there is at least one character in the string.
        """
        ...
    def isdigit(self: Self) -> Any:
        """Return True if the string is a digit string, False otherwise.

        A string is a digit string if all characters in the string are digits and there
        is at least one character in the string.
        """
        ...
    def isidentifier(self: Self) -> Any:
        """Return True if the string is a valid Python identifier, False otherwise.

        Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
        such as "def" or "class".
        """
        ...
    def islower(self: Self) -> Any:
        """Return True if the string is a lowercase string, False otherwise.

        A string is lowercase if all cased characters in the string are lowercase and
        there is at least one cased character in the string.
        """
        ...
    def isnumeric(self: Self) -> Any:
        """Return True if the string is a numeric string, False otherwise.

        A string is numeric if all characters in the string are numeric and there is at
        least one character in the string.
        """
        ...
    def isprintable(self: Self) -> Any:
        """Return True if the string is printable, False otherwise.

        A string is printable if all of its characters are considered printable in
        repr() or if it is empty.
        """
        ...
    def isspace(self: Self) -> Any:
        """Return True if the string is a whitespace string, False otherwise.

        A string is whitespace if all characters in the string are whitespace and there
        is at least one character in the string.
        """
        ...
    def istitle(self: Self) -> Any:
        """Return True if the string is a title-cased string, False otherwise.

        In a title-cased string, upper- and title-case characters may only
        follow uncased characters and lowercase characters only cased ones.
        """
        ...
    def isupper(self: Self) -> Any:
        """Return True if the string is an uppercase string, False otherwise.

        A string is uppercase if all cased characters in the string are uppercase and
        there is at least one cased character in the string.
        """
        ...
    def join(self: Self, iterable: Any) -> Any:
        """Concatenate any number of strings.

        The string whose method is called is inserted in between each given string.
        The result is returned as a new string.

        Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
        """
        ...
    def ljust(self: Self, width: Any, fillchar: Any = ...) -> Any:
        """Return a left-justified string of length width.

        Padding is done using the specified fill character (default is a space).
        """
        ...
    def lower(self: Self) -> Any:
        """Return a copy of the string converted to lowercase."""
        ...
    def lstrip(self: Self, chars: Any = ...) -> Any:
        """Return a copy of the string with leading whitespace removed.

        If chars is given and not None, remove characters in chars instead.
        """
        ...
    def maketrans(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return a translation table usable for str.translate().

        If there is only one argument, it must be a dictionary mapping Unicode
        ordinals (integers) or characters to Unicode ordinals, strings or None.
        Character keys will be then converted to ordinals.
        If there are two arguments, they must be strings of equal length, and
        in the resulting dictionary, each character in x will be mapped to the
        character at the same position in y. If there is a third argument, it
        must be a string, whose characters will be mapped to None in the result.
        """
        ...
    def partition(self: Self, sep: Any) -> Any:
        """Partition the string into three parts using the given separator.

        This will search for the separator in the string.  If the separator is found,
        returns a 3-tuple containing the part before the separator, the separator
        itself, and the part after it.

        If the separator is not found, returns a 3-tuple containing the original string
        and two empty strings.
        """
        ...
    def removeprefix(self: Self, prefix: Any) -> Any:
        """Return a str with the given prefix string removed if present.

        If the string starts with the prefix string, return string[len(prefix):].
        Otherwise, return a copy of the original string.
        """
        ...
    def removesuffix(self: Self, suffix: Any) -> Any:
        """Return a str with the given suffix string removed if present.

        If the string ends with the suffix string and that suffix is not empty,
        return string[:-len(suffix)]. Otherwise, return a copy of the original
        string.
        """
        ...
    def replace(self: Self, old: Any, new: Any, count: Any = ...) -> Any:
        """Return a copy with all occurrences of substring old replaced by new.

          count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.

        If the optional argument count is given, only the first count occurrences are
        replaced.
        """
        ...
    def rfind(self: Self, *args: Any, **kwargs: Any) -> Any:
        """S.rfind(sub[, start[, end]]) -> int

        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.

        Return -1 on failure.
        """
        ...
    def rindex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """S.rindex(sub[, start[, end]]) -> int

        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.

        Raises ValueError when the substring is not found.
        """
        ...
    def rjust(self: Self, width: Any, fillchar: Any = ...) -> Any:
        """Return a right-justified string of length width.

        Padding is done using the specified fill character (default is a space).
        """
        ...
    def rpartition(self: Self, sep: Any) -> Any:
        """Partition the string into three parts using the given separator.

        This will search for the separator in the string, starting at the end. If
        the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it.

        If the separator is not found, returns a 3-tuple containing two empty strings
        and the original string.
        """
        ...
    def rsplit(self: Self, sep: Any = ..., maxsplit: Any = ...) -> Any:
        """Return a list of the words in the string, using sep as the delimiter string.

          sep
            The delimiter according which to split the string.
            None (the default value) means split according to any whitespace,
            and discard empty strings from the result.
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.

        Splits are done starting at the end of the string and working to the front.
        """
        ...
    def rstrip(self: Self, chars: Any = ...) -> Any:
        """Return a copy of the string with trailing whitespace removed.

        If chars is given and not None, remove characters in chars instead.
        """
        ...
    def split(self: Self, sep: Any = ..., maxsplit: Any = ...) -> Any:
        """Return a list of the words in the string, using sep as the delimiter string.

          sep
            The delimiter according which to split the string.
            None (the default value) means split according to any whitespace,
            and discard empty strings from the result.
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        """
        ...
    def splitlines(self: Self, keepends: Any = ...) -> Any:
        """Return a list of the lines in the string, breaking at line boundaries.

        Line breaks are not included in the resulting list unless keepends is given and
        true.
        """
        ...
    def startswith(self: Self, *args: Any, **kwargs: Any) -> Any:
        """S.startswith(prefix[, start[, end]]) -> bool

        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        """
        ...
    def strip(self: Self, chars: Any = ...) -> Any:
        """Return a copy of the string with leading and trailing whitespace removed.

        If chars is given and not None, remove characters in chars instead.
        """
        ...
    def swapcase(self: Self) -> Any:
        """Convert uppercase characters to lowercase and lowercase characters to uppercase."""
        ...
    def title(self: Self) -> Any:
        """Return a version of the string where each word is titlecased.

        More specifically, words start with uppercased characters and all remaining
        cased characters have lower case.
        """
        ...
    def translate(self: Self, table: Any) -> Any:
        """Replace each character in the string using the given translation table.

          table
            Translation table, which must be a mapping of Unicode ordinals to
            Unicode ordinals, strings, or None.

        The table must implement lookup/indexing via __getitem__, for instance a
        dictionary or list.  If this operation raises LookupError, the character is
        left untouched.  Characters mapped to None are deleted.
        """
        ...
    def upper(self: Self) -> Any:
        """Return a copy of the string converted to uppercase."""
        ...
    def zfill(self: Self, width: Any) -> Any:
        """Pad a numeric string with zeros on the left, to fill a field of the given width.

        The string is never truncated.
        """
        ...

def getPossibleCompletions(input: Any) -> Any:
    """Utility method to handle command completion
        Returns in a list all of the possible completions that apply
        to the input string
    """
    ...
def getattr_over(*args: Any, **kwargs: Any) -> Any:
    """getattr"""
    ...
def globals_over(*args: Any, **kwargs: Any) -> Any:
    """globals"""
    ...
def guiLogHandler() -> Any:
    """Adds an additional handler to the root logger to print to
        the script editor.  Sets the shell/outputWindow handler to
        only print 'Critical' records, so that the logger's primary
        output is the script editor.
        Returns the handler.
    """
    ...
def hasattr_over(*args: Any, **kwargs: Any) -> Any:
    """hasattr"""
    ...
def hash_over(*args: Any, **kwargs: Any) -> Any:
    """hash"""
    ...
def helpNonVerbose(thing: Any, title: Any = ..., forceload: Any = ...) -> Any:
    """Utility method to return python help in the form of a string
    
        thing - str or unicode name to get help on
        title - format string for help result
        forceload - argument to pydoc.resolve, force object's module to be reloaded from file
    
        returns formated help string
    """
    ...
def help_over(*args: Any, **kwargs: Any) -> Any:
    """help"""
    ...
def hex_over(*args: Any, **kwargs: Any) -> Any:
    """hex"""
    ...
def id_over(*args: Any, **kwargs: Any) -> Any:
    """id"""
    ...
def input_over(*args: Any, **kwargs: Any) -> Any:
    """input"""
    ...
def int_over(*args: Any, **kwargs: Any) -> Any:
    """int"""
    ...
def isinstance_over(*args: Any, **kwargs: Any) -> Any:
    """isinstance"""
    ...
def issubclass_over(*args: Any, **kwargs: Any) -> Any:
    """issubclass"""
    ...
def iter_over(*args: Any, **kwargs: Any) -> Any:
    """iter"""
    ...
def len_over(*args: Any, **kwargs: Any) -> Any:
    """len"""
    ...
def list_over(*args: Any, **kwargs: Any) -> Any:
    """list"""
    ...
def loadStringResourcesForFile(scriptPath: Any, fullModulePath: Any, resourceFileName: Any) -> Any:
    """Load a string resource.
    
        The 'scriptPath' argument must be a string containing the full path of to 
        a language resource file. The 'resourceFileName' is the _res.py that must be loaded.
    
        If the _res.py fails to be found or executed successfully, the method returns False.
        Otherwise it returns True.
    """
    ...
def loadStringResourcesForModule(moduleName: Any) -> Any:
    """Load the string resources associated with the given module
    
        Note that the argument must be a string containing the full name of the 
        module (eg "maya.app.utils").  The module of that name must have been 
        previously imported.
    
        The base resource file is assumed to be in the same location as the file
        defining the module and will have the same name as the module except with
        _res.py appended to it.  So, for the module foo, the resource file should
        be foo_res.py.  
    
        If Maya is running in localized mode, then the standard location for 
        localized scripts will also be searched (the location given by the 
        command cmds.about( localizedResourceLocation=True ))
    
        Failure to find the base resources for the given module will trigger an 
        exception. Failure to find localized resources is not an error.
    """
    ...
def locals_over(*args: Any, **kwargs: Any) -> Any:
    """locals"""
    ...
def map_over(*args: Any, **kwargs: Any) -> Any:
    """map"""
    ...
def max_over(*args: Any, **kwargs: Any) -> Any:
    """max"""
    ...
def memoryview_over(*args: Any, **kwargs: Any) -> Any:
    """memoryview"""
    ...
def min_over(*args: Any, **kwargs: Any) -> Any:
    """min"""
    ...
def next_over(*args: Any, **kwargs: Any) -> Any:
    """next"""
    ...
def object_over(*args: Any, **kwargs: Any) -> Any:
    """object"""
    ...
def oct_over(*args: Any, **kwargs: Any) -> Any:
    """oct"""
    ...
def open_over(*args: Any, **kwargs: Any) -> Any:
    """open"""
    ...
def ord_over(*args: Any, **kwargs: Any) -> Any:
    """ord"""
    ...
os_environ: _Environ
def pow_over(*args: Any, **kwargs: Any) -> Any:
    """pow"""
    ...
def print_over(*args: Any, **kwargs: Any) -> Any:
    """print"""
    ...
def processIdleEvents(*args: Any, **kwargs: Any) -> Any:
    """Run commands from the idle queue.

    In general there should be no need to call this method.  It is included here
    as it allows for testing of code that uses the idle events for processing.
    Use this method with caution as will change the behaviour of Maya by 
    possibly forcing refreshes or causing other code run before it normally would.
    This may make Maya unrepsonsive.

    This function will return True if all items on the idle queue have been 
    processed.  It will return False if only some of the items have been processed.
    There are several cases in which not all items on the idle queue will execute,
    such as when there is an item with exclusive priority.

    This function does not take any arguments.
    """
    ...
def property_over(*args: Any, **kwargs: Any) -> Any:
    """property"""
    ...
class range(object):
    def __bool__(self: Self) -> Any:
        """self != 0"""
        ...
    def __contains__(self: Self, key: Any) -> Any:
        """Return key in self."""
        ...
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
    def __getitem__(self: Self, key: Any) -> Any:
        """Return self[key]."""
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
    def __len__(self: Self) -> Any:
        """Return len(self)."""
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
    def __reduce__(self: Self, *args: Any, **kwargs: Any) -> Any: ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __reversed__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return a reverse iterator."""
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
    def count(self: Self, *args: Any, **kwargs: Any) -> Any:
        """rangeobject.count(value) -> integer -- return number of occurrences of value"""
        ...
    def index(self: Self, *args: Any, **kwargs: Any) -> Any:
        """rangeobject.index(value) -> integer -- return index of value.
        Raise ValueError if the value is not present.
        """
        ...
    start: member_descriptor = ...
    step: member_descriptor = ...
    stop: member_descriptor = ...

def range_over(*args: Any, **kwargs: Any) -> Any:
    """range"""
    ...
def repr_over(*args: Any, **kwargs: Any) -> Any:
    """repr"""
    ...
def reversed_over(*args: Any, **kwargs: Any) -> Any:
    """reversed"""
    ...
def round_over(*args: Any, **kwargs: Any) -> Any:
    """round"""
    ...
def set_over(*args: Any, **kwargs: Any) -> Any:
    """set"""
    ...
def setattr_over(*args: Any, **kwargs: Any) -> Any:
    """setattr"""
    ...
def shellLogHandler() -> Any:
    """Adds an additional handler to the root logger to print to sys.stdout
        Returns the handler.
    """
    ...
def slice_over(*args: Any, **kwargs: Any) -> Any:
    """slice"""
    ...
def sorted_over(*args: Any, **kwargs: Any) -> Any:
    """sorted"""
    ...
def staticmethod_over(*args: Any, **kwargs: Any) -> Any:
    """staticmethod"""
    ...
def str_over(*args: Any, **kwargs: Any) -> Any:
    """str"""
    ...
def sum_over(*args: Any, **kwargs: Any) -> Any:
    """sum"""
    ...
def super_over(*args: Any, **kwargs: Any) -> Any:
    """super"""
    ...
def tuple_over(*args: Any, **kwargs: Any) -> Any:
    """tuple"""
    ...
def type_over(*args: Any, **kwargs: Any) -> Any:
    """type"""
    ...
def vars_over(*args: Any, **kwargs: Any) -> Any:
    """vars"""
    ...
def zip_over(*args: Any, **kwargs: Any) -> Any:
    """zip"""
    ...