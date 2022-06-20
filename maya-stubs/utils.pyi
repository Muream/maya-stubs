from typing import *
from typing_extensions import Self
from _typeshed import Incomplete
from logging import Handler

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

def execfile(filename: Any, myglobals: Any = ..., mylocals: Any = ...) -> Any:
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

def format_over(*args: Any, **kwargs: Any) -> Any:
    """format"""

def frozenset_over(*args: Any, **kwargs: Any) -> Any:
    """frozenset"""

def getPossibleCompletions(input: Any) -> Any:
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

def helpNonVerbose(thing: Any, title: Any = ..., forceload: Any = ...) -> Any:
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

def loadStringResourcesForFile(scriptPath: Any, fullModulePath: Any, resourceFileName: Any) -> Any:
    """Load a string resource.

    The 'scriptPath' argument must be a string containing the full path of to
    a language resource file. The 'resourceFileName' is the _res.py that must be loaded.

    If the _res.py fails to be found or executed successfully, the method returns False.
    Otherwise it returns True.
    """

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

os_environ: _Environ

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

class MayaGuiLogHandler(Handler):
    def emit(self: Self, record: Any) -> Any: ...

class Output:
    def flush(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Flush no-op"""
    softspace: member_descriptor = ...
    def write(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Write the given string"""
    def writelines(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Write the given sequence"""

class StringTable:
    pass

class range:
    def count(self: Self, *args: Any, **kwargs: Any) -> Any:
        """rangeobject.count(value) -> integer -- return number of occurrences of value"""
    def index(self: Self, *args: Any, **kwargs: Any) -> Any:
        """rangeobject.index(value) -> integer -- return index of value.
        Raise ValueError if the value is not present.
        """
    start: member_descriptor = ...
    step: member_descriptor = ...
    stop: member_descriptor = ...
