from __future__ import annotations

from typing import *

import logging

Unknown = Any

class MayaGuiLogHandler(logging.Handler):
    """A python logging handler that displays error and warning
    records with the appropriate color labels within the Maya GUI
    """
    def __init__(self) -> None:
        """Initializes the instance - basically setting the formatter to None
        and the filter list to empty.
        """

    def emit(self, record: Unknown) -> Any:
        """Do whatever it takes to actually log the specified logging record.

        This version is intended to be implemented by subclasses and so
        raises a NotImplementedError.
        """

class StringTable:
    """The StringTable object allows access to the application's string catalog which is used, which is used to support application lookup for localized string resources.  The strings in this table may be over written by localized versions, which will then be picked up by scripts that access these values.

    This class behaves in the same way as a Dictionary object in Python with respect to getting and setting values.
    Note that StringTable objects just provide access to the single application-wide string table.  So, creating a new StringTable object does not create a new string table inside the application, it is just another interface to the existing global table.
    """
    def __delitem__(self, key: Unknown, /) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key: Unknown, /) -> Any:
        """Return self[key]."""

    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self, /) -> Any:
        """Return len(self)."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __setitem__(self, key: Unknown, value: Unknown, /) -> Any:
        """Set self[key] to value."""

def abs_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """abs"""

def all_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """all"""

def any_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """any"""

def ascii_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """ascii"""

def bin_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """bin"""

def bool_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """bool"""

def breakpoint_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """breakpoint"""

def bytearray_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """bytearray"""

def bytes_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """bytes"""

def callable_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """callable"""

def chr_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """chr"""

def classmethod_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """classmethod"""

def compile_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """compile"""

def complex_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """complex"""

def delattr_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """delattr"""

def dict_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """dict"""

def dir_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """dir"""

def divmod_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """divmod"""

def enumerate_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """enumerate"""

def eval_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """eval"""

def exec_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """exec"""

def executeDeferred(*args: Unknown, **kwargs: Unknown) -> Any:
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

def executeInMainThreadWithResult(*args: Unknown, **kwargs: Unknown) -> Any:
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

def filter_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """filter"""

def float_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """float"""

def formatGuiException(
    exceptionType: Unknown,
    exceptionObject: Unknown,
    traceBack: Unknown,
    detail: int = 2,
) -> Any:
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

def formatGuiResult(obj: Unknown) -> Any:
    """Gets a string representation of a result object.

    To perform an action when a result is about to returned to the script editor
    without modifying Maya's default printing of results, do the following:

        import maya.utils
        def myResultCallback(obj):
            # do something here...
            return maya.utils._formatGuiResult(obj)
        maya.utils.formatGuiResult = myResultCallback
    """

def format_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """format"""

def frozenset_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """frozenset"""

def getPossibleCompletions(input: Unknown) -> Any:
    """Utility method to handle command completion
    Returns in a list all of the possible completions that apply
    to the input string
    """

def getattr_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """getattr"""

def globals_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """globals"""

def guiLogHandler() -> Any:
    """Adds an additional handler to the root logger to print to
    the script editor.  Sets the shell/outputWindow handler to
    only print 'Critical' records, so that the logger's primary
    output is the script editor.
    Returns the handler.
    """

def hasattr_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """hasattr"""

def hash_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """hash"""

def helpNonVerbose(
    thing: Unknown, title: str = "Python Library Documentation: %s", forceload: int = 0
) -> Any:
    """Utility method to return python help in the form of a string

    thing - str or unicode name to get help on
    title - format string for help result
    forceload - argument to pydoc.resolve, force object's module to be reloaded from file

    returns formated help string
    """

def help_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """help"""

def hex_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """hex"""

def id_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """id"""

def input_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """input"""

def int_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """int"""

def isinstance_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """isinstance"""

def issubclass_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """issubclass"""

def iter_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """iter"""

def len_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """len"""

def list_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """list"""

def loadStringResourcesForFile(
    scriptPath: Unknown, fullModulePath: Unknown, resourceFileName: Unknown
) -> Any:
    """Load a string resource.

    The 'scriptPath' argument must be a string containing the full path of to
    a language resource file. The 'resourceFileName' is the _res.py that must be loaded.

    If the _res.py fails to be found or executed successfully, the method returns False.
    Otherwise it returns True.
    """

def loadStringResourcesForModule(moduleName: Unknown) -> Any:
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

def locals_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """locals"""

def map_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """map"""

def max_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """max"""

def memoryview_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """memoryview"""

def min_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """min"""

def next_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """next"""

def object_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """object"""

def oct_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """oct"""

def open_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """open"""

def ord_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """ord"""

def pow_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """pow"""

def print_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """print"""

def processIdleEvents(*args: Unknown, **kwargs: Unknown) -> Any:
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

def property_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """property"""

def range_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """range"""

def repr_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """repr"""

def reversed_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """reversed"""

def round_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """round"""

def set_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """set"""

def setattr_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """setattr"""

def shellLogHandler() -> Any:
    """Adds an additional handler to the root logger to print to sys.stdout
    Returns the handler.
    """

def slice_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """slice"""

def sorted_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """sorted"""

def staticmethod_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """staticmethod"""

def str_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """str"""

def sum_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """sum"""

def super_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """super"""

def tuple_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """tuple"""

def type_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """type"""

def vars_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """vars"""

def zip_over(*args: Unknown, **kwargs: Unknown) -> Any:
    """zip"""
