from __future__ import annotations

from typing import *

Unknown = Any

class MayaGuiLogHandler(Handler):
    """A python logging handler that displays error and warning
    records with the appropriate color labels within the Maya GUI
    """
    def __init__(self) -> Any:
        """Initializes the instance - basically setting the formatter to None
        and the filter list to empty.
        """

    def emit(self, record) -> Any:
        """Do whatever it takes to actually log the specified logging record.

        This version is intended to be implemented by subclasses and so
        raises a NotImplementedError.
        """


class Output(object):
    """MayaOutput objects"""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def flush(self, *args: Any, **kwargs: Any) -> Any:
        """Flush no-op"""

    softspace: member_descriptor = <member 'softspace' of 'maya.Output' objects>
    def write(self, *args: Any, **kwargs: Any) -> Any:
        """Write the given string"""

    def writelines(self, *args: Any, **kwargs: Any) -> Any:
        """Write the given sequence"""


class StringTable(object):
    """The StringTable object allows access to the application's string catalog which is used, which is used to support application lookup for localized string resources.  The strings in this table may be over written by localized versions, which will then be picked up by scripts that access these values.

    This class behaves in the same way as a Dictionary object in Python with respect to getting and setting values.
    Note that StringTable objects just provide access to the single application-wide string table.  So, creating a new StringTable object does not create a new string table inside the application, it is just another interface to the existing global table.
    """
    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __setitem__(self, key, value) -> Any:
        """Set self[key] to value."""


def abs_over(*args: Any, **kwargs: Any) -> Any:
    """abs"""

def all_over(*args: Any, **kwargs: Any) -> Any:
    """all"""

def any_over(*args: Any, **kwargs: Any) -> Any:
    """any"""

def ascii_over(*args: Any, **kwargs: Any) -> Any:
    """ascii"""

def bin_over(*args: Any, **kwargs: Any) -> Any:
    """bin"""

def bool_over(*args: Any, **kwargs: Any) -> Any:
    """bool"""

def breakpoint_over(*args: Any, **kwargs: Any) -> Any:
    """breakpoint"""

def bytearray_over(*args: Any, **kwargs: Any) -> Any:
    """bytearray"""

def bytes_over(*args: Any, **kwargs: Any) -> Any:
    """bytes"""

def callable_over(*args: Any, **kwargs: Any) -> Any:
    """callable"""

def chr_over(*args: Any, **kwargs: Any) -> Any:
    """chr"""

def classmethod_over(*args: Any, **kwargs: Any) -> Any:
    """classmethod"""

def compile_over(*args: Any, **kwargs: Any) -> Any:
    """compile"""

def complex_over(*args: Any, **kwargs: Any) -> Any:
    """complex"""

def delattr_over(*args: Any, **kwargs: Any) -> Any:
    """delattr"""

def dict_over(*args: Any, **kwargs: Any) -> Any:
    """dict"""

def dir_over(*args: Any, **kwargs: Any) -> Any:
    """dir"""

def divmod_over(*args: Any, **kwargs: Any) -> Any:
    """divmod"""

def enumerate_over(*args: Any, **kwargs: Any) -> Any:
    """enumerate"""

def eval_over(*args: Any, **kwargs: Any) -> Any:
    """eval"""

def exec_over(*args: Any, **kwargs: Any) -> Any:
    """exec"""

def execfile(filename, myglobals=None = None, mylocals=None = None) -> Any:
    """Read and execute a Python script from a file in the given namespaces.
    The globals and locals are dictionaries, defaulting to the current
    globals and locals. If only globals is given, locals defaults to it.
    """

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

def filter_over(*args: Any, **kwargs: Any) -> Any:
    """filter"""

def float_over(*args: Any, **kwargs: Any) -> Any:
    """float"""

def formatGuiException(exceptionType, exceptionObject, traceBack, detail=2 = 2) -> Any:
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

def formatGuiResult(obj) -> Any:
    """Gets a string representation of a result object.

    To perform an action when a result is about to returned to the script editor
    without modifying Maya's default printing of results, do the following:

        import maya.utils
        def myResultCallback(obj):
            # do something here...
            return maya.utils._formatGuiResult(obj)
        maya.utils.formatGuiResult = myResultCallback
    """

def format_over(*args: Any, **kwargs: Any) -> Any:
    """format"""

def frozenset_over(*args: Any, **kwargs: Any) -> Any:
    """frozenset"""

class futureStr(object):
    """str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.
    """
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __contains__(self, key) -> Any:
        """Return key in self."""

    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __format__(self, format_spec) -> Any:
        """Return a formatted version of the string as described by format_spec."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __getattribute__(self, name) -> Any:
        """Return getattr(self, name)."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __getnewargs__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __iter__(self) -> Any:
        """Implement iter(self)."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __mod__(self, value) -> Any:
        """Return self%value."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmod__(self, value) -> Any:
        """Return value%self."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __sizeof__(self) -> Any:
        """Return the size of the string in memory, in bytes."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def capitalize(self) -> Any:
        """Return a capitalized version of the string.

        More specifically, make the first character have upper case and the rest lower
        case.
        """

    def casefold(self) -> Any:
        """Return a version of the string suitable for caseless comparisons."""

    def center(self, width, fillchar=' ' =  ) -> Any:
        """Return a centered string of length width.

        Padding is done using the specified fill character (default is a space).
        """

    def count(self, *args: Any, **kwargs: Any) -> Any:
        """S.count(sub[, start[, end]]) -> int

        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are
        interpreted as in slice notation.
        """

    def encode(self, encoding='utf-8' = utf-8, errors='strict' = strict) -> Any:
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

    def endswith(self, *args: Any, **kwargs: Any) -> Any:
        """S.endswith(suffix[, start[, end]]) -> bool

        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """

    def expandtabs(self, tabsize=8 = 8) -> Any:
        """Return a copy where all tab characters are expanded using spaces.

        If tabsize is not given, a tab size of 8 characters is assumed.
        """

    def find(self, *args: Any, **kwargs: Any) -> Any:
        """S.find(sub[, start[, end]]) -> int

        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.

        Return -1 on failure.
        """

    def format(self, *args: Any, **kwargs: Any) -> Any:
        """S.format(*args, **kwargs) -> str

        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """

    def format_map(self, *args: Any, **kwargs: Any) -> Any:
        """S.format_map(mapping) -> str

        Return a formatted version of S, using substitutions from mapping.
        The substitutions are identified by braces ('{' and '}').
        """

    def index(self, *args: Any, **kwargs: Any) -> Any:
        """S.index(sub[, start[, end]]) -> int

        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.

        Raises ValueError when the substring is not found.
        """

    def isalnum(self) -> Any:
        """Return True if the string is an alpha-numeric string, False otherwise.

        A string is alpha-numeric if all characters in the string are alpha-numeric and
        there is at least one character in the string.
        """

    def isalpha(self) -> Any:
        """Return True if the string is an alphabetic string, False otherwise.

        A string is alphabetic if all characters in the string are alphabetic and there
        is at least one character in the string.
        """

    def isascii(self) -> Any:
        """Return True if all characters in the string are ASCII, False otherwise.

        ASCII characters have code points in the range U+0000-U+007F.
        Empty string is ASCII too.
        """

    def isdecimal(self) -> Any:
        """Return True if the string is a decimal string, False otherwise.

        A string is a decimal string if all characters in the string are decimal and
        there is at least one character in the string.
        """

    def isdigit(self) -> Any:
        """Return True if the string is a digit string, False otherwise.

        A string is a digit string if all characters in the string are digits and there
        is at least one character in the string.
        """

    def isidentifier(self) -> Any:
        """Return True if the string is a valid Python identifier, False otherwise.

        Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
        such as "def" or "class".
        """

    def islower(self) -> Any:
        """Return True if the string is a lowercase string, False otherwise.

        A string is lowercase if all cased characters in the string are lowercase and
        there is at least one cased character in the string.
        """

    def isnumeric(self) -> Any:
        """Return True if the string is a numeric string, False otherwise.

        A string is numeric if all characters in the string are numeric and there is at
        least one character in the string.
        """

    def isprintable(self) -> Any:
        """Return True if the string is printable, False otherwise.

        A string is printable if all of its characters are considered printable in
        repr() or if it is empty.
        """

    def isspace(self) -> Any:
        """Return True if the string is a whitespace string, False otherwise.

        A string is whitespace if all characters in the string are whitespace and there
        is at least one character in the string.
        """

    def istitle(self) -> Any:
        """Return True if the string is a title-cased string, False otherwise.

        In a title-cased string, upper- and title-case characters may only
        follow uncased characters and lowercase characters only cased ones.
        """

    def isupper(self) -> Any:
        """Return True if the string is an uppercase string, False otherwise.

        A string is uppercase if all cased characters in the string are uppercase and
        there is at least one cased character in the string.
        """

    def join(self, iterable) -> Any:
        """Concatenate any number of strings.

        The string whose method is called is inserted in between each given string.
        The result is returned as a new string.

        Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
        """

    def ljust(self, width, fillchar=' ' =  ) -> Any:
        """Return a left-justified string of length width.

        Padding is done using the specified fill character (default is a space).
        """

    def lower(self) -> Any:
        """Return a copy of the string converted to lowercase."""

    def lstrip(self, chars=None = None) -> Any:
        """Return a copy of the string with leading whitespace removed.

        If chars is given and not None, remove characters in chars instead.
        """

    def maketrans(self, *args: Any, **kwargs: Any) -> Any:
        """Return a translation table usable for str.translate().

        If there is only one argument, it must be a dictionary mapping Unicode
        ordinals (integers) or characters to Unicode ordinals, strings or None.
        Character keys will be then converted to ordinals.
        If there are two arguments, they must be strings of equal length, and
        in the resulting dictionary, each character in x will be mapped to the
        character at the same position in y. If there is a third argument, it
        must be a string, whose characters will be mapped to None in the result.
        """

    def partition(self, sep) -> Any:
        """Partition the string into three parts using the given separator.

        This will search for the separator in the string.  If the separator is found,
        returns a 3-tuple containing the part before the separator, the separator
        itself, and the part after it.

        If the separator is not found, returns a 3-tuple containing the original string
        and two empty strings.
        """

    def removeprefix(self, prefix) -> Any:
        """Return a str with the given prefix string removed if present.

        If the string starts with the prefix string, return string[len(prefix):].
        Otherwise, return a copy of the original string.
        """

    def removesuffix(self, suffix) -> Any:
        """Return a str with the given suffix string removed if present.

        If the string ends with the suffix string and that suffix is not empty,
        return string[:-len(suffix)]. Otherwise, return a copy of the original
        string.
        """

    def replace(self, old, new, count=-1 = -1) -> Any:
        """Return a copy with all occurrences of substring old replaced by new.

          count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.

        If the optional argument count is given, only the first count occurrences are
        replaced.
        """

    def rfind(self, *args: Any, **kwargs: Any) -> Any:
        """S.rfind(sub[, start[, end]]) -> int

        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.

        Return -1 on failure.
        """

    def rindex(self, *args: Any, **kwargs: Any) -> Any:
        """S.rindex(sub[, start[, end]]) -> int

        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.

        Raises ValueError when the substring is not found.
        """

    def rjust(self, width, fillchar=' ' =  ) -> Any:
        """Return a right-justified string of length width.

        Padding is done using the specified fill character (default is a space).
        """

    def rpartition(self, sep) -> Any:
        """Partition the string into three parts using the given separator.

        This will search for the separator in the string, starting at the end. If
        the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it.

        If the separator is not found, returns a 3-tuple containing two empty strings
        and the original string.
        """

    def rsplit(self, sep=None = None, maxsplit=-1 = -1) -> Any:
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

    def rstrip(self, chars=None = None) -> Any:
        """Return a copy of the string with trailing whitespace removed.

        If chars is given and not None, remove characters in chars instead.
        """

    def split(self, sep=None = None, maxsplit=-1 = -1) -> Any:
        """Return a list of the words in the string, using sep as the delimiter string.

        sep
          The delimiter according which to split the string.
          None (the default value) means split according to any whitespace,
          and discard empty strings from the result.
        maxsplit
          Maximum number of splits to do.
          -1 (the default value) means no limit.
        """

    def splitlines(self, keepends=False = False) -> Any:
        """Return a list of the lines in the string, breaking at line boundaries.

        Line breaks are not included in the resulting list unless keepends is given and
        true.
        """

    def startswith(self, *args: Any, **kwargs: Any) -> Any:
        """S.startswith(prefix[, start[, end]]) -> bool

        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        """

    def strip(self, chars=None = None) -> Any:
        """Return a copy of the string with leading and trailing whitespace removed.

        If chars is given and not None, remove characters in chars instead.
        """

    def swapcase(self) -> Any:
        """Convert uppercase characters to lowercase and lowercase characters to uppercase."""

    def title(self) -> Any:
        """Return a version of the string where each word is titlecased.

        More specifically, words start with uppercased characters and all remaining
        cased characters have lower case.
        """

    def translate(self, table) -> Any:
        """Replace each character in the string using the given translation table.

          table
            Translation table, which must be a mapping of Unicode ordinals to
            Unicode ordinals, strings, or None.

        The table must implement lookup/indexing via __getitem__, for instance a
        dictionary or list.  If this operation raises LookupError, the character is
        left untouched.  Characters mapped to None are deleted.
        """

    def upper(self) -> Any:
        """Return a copy of the string converted to uppercase."""

    def zfill(self, width) -> Any:
        """Pad a numeric string with zeros on the left, to fill a field of the given width.

        The string is never truncated.
        """


def getPossibleCompletions(input) -> Any:
    """Utility method to handle command completion
    Returns in a list all of the possible completions that apply
    to the input string
    """

def getattr_over(*args: Any, **kwargs: Any) -> Any:
    """getattr"""

def globals_over(*args: Any, **kwargs: Any) -> Any:
    """globals"""

def guiLogHandler() -> Any:
    """Adds an additional handler to the root logger to print to
    the script editor.  Sets the shell/outputWindow handler to
    only print 'Critical' records, so that the logger's primary
    output is the script editor.
    Returns the handler.
    """

def hasattr_over(*args: Any, **kwargs: Any) -> Any:
    """hasattr"""

def hash_over(*args: Any, **kwargs: Any) -> Any:
    """hash"""

def helpNonVerbose(thing, title='Python Library Documentation: %s' = Python Library Documentation: %s, forceload=0 = 0) -> Any:
    """Utility method to return python help in the form of a string

    thing - str or unicode name to get help on
    title - format string for help result
    forceload - argument to pydoc.resolve, force object's module to be reloaded from file

    returns formated help string 
    """

def help_over(*args: Any, **kwargs: Any) -> Any:
    """help"""

def hex_over(*args: Any, **kwargs: Any) -> Any:
    """hex"""

def id_over(*args: Any, **kwargs: Any) -> Any:
    """id"""

def input_over(*args: Any, **kwargs: Any) -> Any:
    """input"""

def int_over(*args: Any, **kwargs: Any) -> Any:
    """int"""

def isinstance_over(*args: Any, **kwargs: Any) -> Any:
    """isinstance"""

def issubclass_over(*args: Any, **kwargs: Any) -> Any:
    """issubclass"""

def iter_over(*args: Any, **kwargs: Any) -> Any:
    """iter"""

def len_over(*args: Any, **kwargs: Any) -> Any:
    """len"""

def list_over(*args: Any, **kwargs: Any) -> Any:
    """list"""

def loadStringResourcesForFile(scriptPath, fullModulePath, resourceFileName) -> Any:
    """Load a string resource.

    The 'scriptPath' argument must be a string containing the full path of to 
    a language resource file. The 'resourceFileName' is the _res.py that must be loaded.

    If the _res.py fails to be found or executed successfully, the method returns False.
    Otherwise it returns True.
    """

def loadStringResourcesForModule(moduleName) -> Any:
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

def locals_over(*args: Any, **kwargs: Any) -> Any:
    """locals"""

def map_over(*args: Any, **kwargs: Any) -> Any:
    """map"""

def max_over(*args: Any, **kwargs: Any) -> Any:
    """max"""

def memoryview_over(*args: Any, **kwargs: Any) -> Any:
    """memoryview"""

def min_over(*args: Any, **kwargs: Any) -> Any:
    """min"""

def next_over(*args: Any, **kwargs: Any) -> Any:
    """next"""

def object_over(*args: Any, **kwargs: Any) -> Any:
    """object"""

def oct_over(*args: Any, **kwargs: Any) -> Any:
    """oct"""

def open_over(*args: Any, **kwargs: Any) -> Any:
    """open"""

def ord_over(*args: Any, **kwargs: Any) -> Any:
    """ord"""

def pow_over(*args: Any, **kwargs: Any) -> Any:
    """pow"""

def print_over(*args: Any, **kwargs: Any) -> Any:
    """print"""

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

def property_over(*args: Any, **kwargs: Any) -> Any:
    """property"""

class range(object):
    """range(stop) -> range object
    range(start, stop[, step]) -> range object

    Return an object that produces a sequence of integers from start (inclusive)
    to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
    start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
    These are exactly the valid indices for a list of 4 elements.
    When step is given, it specifies the increment (or decrement).
    """
    def __bool__(self) -> Any:
        """self != 0"""

    def __contains__(self, key) -> Any:
        """Return key in self."""

    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __getattribute__(self, name) -> Any:
        """Return getattr(self, name)."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __iter__(self) -> Any:
        """Implement iter(self)."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __reduce__(self, *args: Any, **kwargs: Any) -> Any:
        """Helper for pickle."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __reversed__(self, *args: Any, **kwargs: Any) -> Any:
        """Return a reverse iterator."""

    def count(self, *args: Any, **kwargs: Any) -> Any:
        """rangeobject.count(value) -> integer -- return number of occurrences of value"""

    def index(self, *args: Any, **kwargs: Any) -> Any:
        """rangeobject.index(value) -> integer -- return index of value.
        Raise ValueError if the value is not present.
        """

    start: member_descriptor = <member 'start' of 'range' objects>
    step: member_descriptor = <member 'step' of 'range' objects>
    stop: member_descriptor = <member 'stop' of 'range' objects>

def range_over(*args: Any, **kwargs: Any) -> Any:
    """range"""

def repr_over(*args: Any, **kwargs: Any) -> Any:
    """repr"""

def reversed_over(*args: Any, **kwargs: Any) -> Any:
    """reversed"""

def round_over(*args: Any, **kwargs: Any) -> Any:
    """round"""

def set_over(*args: Any, **kwargs: Any) -> Any:
    """set"""

def setattr_over(*args: Any, **kwargs: Any) -> Any:
    """setattr"""

def shellLogHandler() -> Any:
    """Adds an additional handler to the root logger to print to sys.stdout
    Returns the handler.
    """

def slice_over(*args: Any, **kwargs: Any) -> Any:
    """slice"""

def sorted_over(*args: Any, **kwargs: Any) -> Any:
    """sorted"""

def staticmethod_over(*args: Any, **kwargs: Any) -> Any:
    """staticmethod"""

def str_over(*args: Any, **kwargs: Any) -> Any:
    """str"""

def sum_over(*args: Any, **kwargs: Any) -> Any:
    """sum"""

def super_over(*args: Any, **kwargs: Any) -> Any:
    """super"""

def tuple_over(*args: Any, **kwargs: Any) -> Any:
    """tuple"""

def type_over(*args: Any, **kwargs: Any) -> Any:
    """type"""

def vars_over(*args: Any, **kwargs: Any) -> Any:
    """vars"""

def zip_over(*args: Any, **kwargs: Any) -> Any:
    """zip"""

