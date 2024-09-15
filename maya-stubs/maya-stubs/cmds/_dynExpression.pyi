from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dynExpression(*args: str, edit: bool = ..., query: bool = ..., creation: bool = ..., runtime: bool = ..., runtimeAfterDynamics: bool = ..., runtimeBeforeDynamics: bool = ..., string: str = ...) -> Union[str, bool]:
    """This command describes an expression that belongs to the specified
    particle shape.  The expression is a block of code of unlimited length
    with a C-like syntax that can perform conversions, mathematical
    operations, and logical decision making on any numeric attribute(s) or
    per-particle attribute(s) in the scene.  One expression can read and
    alter any number of these attributes.  Every particle shape in your
    scene has three expressions, one for the runtimeBeforeDynamics, one
    for the runtimeAfterDynamics and one for creation time.  The create
    expression gets executed for every particle in the object whose age is
    0.0.  The runtime expression gets executed for each particle with an
    age greater then 0.0.  Unlike expressions created with thecommand, particle expressions always exist and are a
    part of the owning particle object's shape.  They default to empty
    strings, but they are always there.  Because of this, there is no need
    to use the '-e' flag.  Every call to the dynExpression command is
    considered an edit by default.  Per-particle attributes are those
    attributes of a particle shape that have a potentially different value
    for each particle in the object.  Examples of these includeandIf this command is being sent by the command line or in a script, then
    the user should be sure to embed escaped newlines (\\n), tabs (\\t) for
    clarity when reading them in the expression editor.  Also, quotes in
    an expression must be escaped (\\") so that they are not confused by
    the system as the end of your string.  When using the expression
    editor, these characters are escaped for you unless they are already
    within quotes.This type of expression is executed during the evaluation of the
    dynamics.  If an output of the expression is requested before that,
    then the dynamics will be force to compute at that time.  If dynamics
    is disabled, then these expressions will have no effect.
    Args:
        creation (bool?): Tells the command that the string passed will be a  
                creation expression for the particle shape.  This means that  
                this expression will be executed when a particle is emitted  
                or at the beginning of the scene for existing particles.  
                Properties: create, query, edit
        runtime (bool?): Tells the command that the string passed will be a  
                runtime expression for the particle shape.  This expression  
                will be executed at the beginning of runtime.  
                Properties: create, query, edit
        runtimeAfterDynamics (bool?): Tells the command that the string passed will be a  
                runtime expression for the particle shape.  This expression  
                will be executed after dynamics whenever a particle's age  
                is greater then zero (0).  
                Properties: create, query, edit
        runtimeBeforeDynamics (bool?): Tells the command that the string passed will be a  
                runtime expression for the particle shape.  This expression  
                will be executed before dynamics whenever a particle's age  
                is greater then zero (0).  
                Properties: create, query, edit
        string (str?): Set the expression string. This is queriable with the -q/query flag and the -rbd/runtimeBeforeDynamics,  
                the -rab/runtimeAfterDynamics or the -c/creation flag.  
                Properties: create, edit

    Returns:
        str: The particle shape which this expression belongs to

    Example:
    """

