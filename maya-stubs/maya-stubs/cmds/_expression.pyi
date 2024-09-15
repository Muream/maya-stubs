from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def expression(*args: str, edit: bool = ..., query: bool = ..., alwaysEvaluate: Queryable[int] = ..., animated: Queryable[int] = ..., attribute: Queryable[str] = ..., name: Queryable[str] = ..., object: Queryable[str] = ..., safe: bool = ..., shortNames: bool = ..., string: Queryable[str] = ..., timeDependent: bool = ..., unitConversion: Queryable[str] = ...) -> Union[str, int, bool]:
    """This command describes an expression that belongs to the current scene.
    The expression is a block of code of unlimited length with a C-like syntax that can perform
    conversions, mathematical operations, and logical decision making on
    any numeric attribute(s) in the scene.  One expression can read and
    alter any number of numeric attributes.  Theoretically, every expression
    in a scene can be combined into one long expression, but it is
    recommended that they are separated for ease of use and editing, as well
    as efficiency.If this command is being sent by the command line or in a script, then
    the user should be sure to embed escaped newlines (\\n), tabs (\\t) for
    clarity when reading them in the expression editor.  Also, quotes in an
    expression must be escaped (\\") so that they are not confused by the system
    as the end of your string.  When using the expression editor, these
    characters are escaped for you unless they are already within quotes.Note, expressions that alter or use per-particle attributes of a particle
    shape should use the '' command.
    Args:
        alwaysEvaluate (Queryable[int]?): If this is TRUE (the default), then the expression will be evaluated  
                whenever time changes regardless of whether the other inputs have  
                changed, and an output is requested.  If it is FALSE, then the expression  
                will only be evaluated if one or more of the inputs changes and an output is requested.  Note, if  
                'time' or 'frame' are inputs, then the expression will act as if this  
                was set to TRUE.  
                Properties: create, query, edit
        animated (Queryable[int]?): Sets the animation mode on the expression node:  
                0 = Not Animated,  
                1 = Animated,  
                2 = Animated with No Callback.  
                Properties: create, query, edit
        attribute (Queryable[str]?): Sets the name of the attribute to use for the expression  
                Properties: create, query, edit
        name (Queryable[str]?): Sets the name of the dependency graph node to use for the expression  
                Properties: create, query, edit
        object (Queryable[str]?): Sets the "default" object for the expression.  This allows the  
                expression writer to not type the object name for frequently-used  
                objects.  See the examples below.  
                Properties: create, query, edit
        safe (bool?): Returns true if no potential side effect can occurs running that expression.  
                Safe expression will be optimized to evaluate only when needed even if flagged alwaysEvaluate.  
                Properties: query
        shortNames (bool?): When used with the -q/query flag, tells the command to return the expression with attribute names as short as possible.  
                The default is to return the FULL attribute name, regardless of how the user entered  
                it into the expression, including the object names.  With this flag set, attribute names  
                are returned as their short versions, and any attribute that belongs to the default object,  
                if there is one specified, will not display the object's name.  
                Properties: create, query, edit
        string (Queryable[str]?): Set the expression string  
                Properties: create, query, edit
        timeDependent (bool?): Returns true if expression is evaluated when time change.  
                An expression can be time-dependent for the following reasons:  
                - The expression refers to 'time' or 'frame' keywords.  
                - The expression have side effects (unsafe).  
                - The expression node's "time" attribute is connected manually.  
                If the expression is safe and not time dependend, then they will always evaluate on depend, even if alwaysEvaluate is on.  
                Properties: query
        unitConversion (Queryable[str]?): Insert specified unit conversion nodes at creation: "all", "none,"  
                or "angularOnly." Default is "all."  For angularOnly, will insert unit  
                conversion nodes only for angular attributes (allowing degrees-to-radians  
                conversion).  This is for performance tuning.  
                If queried, returns the option used when the expression was created  
                or last edited.  
                Properties: query, edit

    Returns:
        str: The name of the expression

    Example:
    """

