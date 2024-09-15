from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def spring(*args: str, edit: bool = ..., query: bool = ..., addSprings: bool = ..., allPoints: bool = ..., count: bool = ..., damping: Queryable[float] = ..., dampingPS: Queryable[float] = ..., endForceWeight: Queryable[float] = ..., exclusive: bool = ..., length: Queryable[float] = ..., maxDistance: float = ..., minDistance: float = ..., minMax: bool = ..., name: Queryable[str] = ..., noDuplicate: bool = ..., restLength: Queryable[float] = ..., restLengthPS: Queryable[float] = ..., startForceWeight: Queryable[float] = ..., stiffness: Queryable[float] = ..., stiffnessPS: Queryable[float] = ..., useDampingPS: bool = ..., useRestLengthPS: bool = ..., useStiffnessPS: bool = ..., walkLength: int = ..., wireframe: bool = ...) -> Union[str, bool, float]:
    """The spring command can do any of the following:* create a new spring object (shape plus transform).  The shape
    contains springs between the points (particles, cvs, etc.)
    of the objects selected or listed on the command line.* create new springs and add them to an existing spring object* edit or query certain attributes of an existing spring objectOne "spring object" may have hundreds or even thousands of individual springs.
    Certain attributes of the spring object specify exactly where the springs
    are attached to which other objects.Springs may be attached to the following: particles, vertices of soft
    bodies, CVs or edit points of curves or surfaces, vertices of polygonal
    objects, and points of lattices. In the case where one endpoint of a
    spring is non-dynamic (a CV, edit point, etc.), the spring does not affect
    its motion, but the motion of the point affects the spring. A spring will
    be created only if at least one of the endpoints is dynamic: for example,
    a spring will never be created between two CVs. A single spring object can
    hold springs which are incident to any number of other objects.The spring has creation-only flags and editable flags.  Creation-only flags
    (minDistance, maxDistance, add, exclusive, all, wireframe, walklength,
    checkExisting) can be used only when creating new springs (including adding
    springs to existing spring object).  Editable flags modify attributes of an
    existing spring object.If a spring object is created, this command returns the names of
    the shape and transform.  If a spring object is queried, the command returns
    the results of the query.
    Args:
        addSprings (bool?): If specified, springs will be added to the existing selected set of springs.  
                (Default is to create a new spring object.)  
                Properties: create
        allPoints (bool?): If True, sets the mode of spring application to All.  This will add  
                springs between all points selected.  
                (Default is False.)  
                Properties: create, edit
        count (bool?): Return the number of springs in the shape.  Query-only.  
                We maintain this flag only for compatibility with earlier versions  
                of Maya.  To get the count of springs, it is much faster and simpler  
                to use the spring shape's count attribute: getAttr <shapeName>.count.  
                Properties: query
        damping (Queryable[float]?): Damping factor for the springs created in the spring object.  
                (Default = 0.2 )  
                Properties: create, query, edit
        dampingPS (Queryable[float]?): Damping factor for the springs created in the spring object. This will  
                initialize all the entries in dampingPS to the specified value.  
                In both the flag and the attribute name, "PS" stands for "per-spring."  
                (Default = 0.2 )  
                Properties: create, query, edit
        endForceWeight (Queryable[float]?): Amount of the force of the spring that gets applied to the point to which  
                the spring ends. Valid range is from 0.0 to 1.0. (Default = 1.0 )  
                Properties: create, query, edit
        exclusive (bool?): If true, tells the command to create springs only between pairs of  
                points which are not in the same object.  
                (Default is False.)  
                Properties: create
        length (Queryable[float]?): Vestigial form of "restLength." Please use "restLength" instead.  
                Properties: create, query, edit
        maxDistance (float?): Maximum distance between two points that a spring would be  
                considered.  
                Properties: create, edit
        minDistance (float?): Minimum distance between two points that a spring would be considered.  
                (Default = 0.0. See Defaults for more information on this flag's default.)  
                Properties: create
        minMax (bool?): If True, sets the mode of the spring application to Min/Max.  
                This will add springs between all points from the specified point groups  
                that are between the minimum and maximum distance values set with min and max.  
                (Default is False.)  
                Note: This gets automatically set if either the min or max flags are used.  
                Properties: create
        name (Queryable[str]?): Name of spring object.  
                Properties: create, query
        noDuplicate (bool?): Check for existing springs and don't add a new spring between  
                two points already connected by a spring in the same object.  
                Only the object the command is working on is checked.  This flag  
                is relevant only when using -add. (Default = false)  
                Properties: create
        restLength (Queryable[float]?): Per-object rest length for the new springs. Springs can use either  
                their per-object or per-spring rest length.  See the -lPS and -ulp flags.  
                Properties: create, query, edit
        restLengthPS (Queryable[float]?): Per-spring rest length for the new springs. This will  
                initialize all the entries in restLengthPS to the specified value.  
                If this flag is not thrown, each rest length will be initialized to  
                the distance between the two  points at the time the spring is created  
                (i.e., the initial length of the spring).   When playing back, springs  
                can use either their per-spring or per-object rest length.  See the  
                -rl and -urp flags.  
                In both the flag and the attribute name, "PS" stands for "per-spring."  
                Properties: create, query, edit
        startForceWeight (Queryable[float]?): Amount of the force of the spring that gets applied to the point from  
                which the spring starts. Valid range is from 0.0 to 1.0. (Default = 1.0 )  
                Properties: create, query, edit
        stiffness (Queryable[float]?): Stiffness of the springs created in the spring object. (Default = 1.0 )  
                -damp float  
                Vestigial form of "damping."  Please use "damping" instead.  
                Properties: create, query, edit
        stiffnessPS (Queryable[float]?): Stiffness of the springs created in the spring object. This will  
                initialize all the entries in stiffnessPS to the specified value.  
                In both the flag and the attribute name, "PS" stands for "per-spring."  
                (Default = 1.0 )  
                Properties: create, query, edit
        useDampingPS (bool?): Specifies whether to use dampingPS (per spring damping).  
                If set to false, the per object damping attribute value will be used.  
                This flag simply sets the useDampingPS attribute of the spring shape.  
                In both the flag and the attribute name, "PS" stands for "per-spring."  
                (Default = false )  
                Properties: create, query, edit
        useRestLengthPS (bool?): Specifies whether to use restLengthPS (per spring restLength).  
                If set to false, the per object restLength attribute value will be used.  
                This flag simply sets the useRestLengthPS attribute of the spring shape.  
                In both the flag and the attribute name, "PS" stands for "per-spring."  
                (Default = false )  
                Properties: create, query, edit
        useStiffnessPS (bool?): Specifies whether to use stiffnessPS (per spring stiffness).  
                If set to false, the per object stiffness attribute value will be used.  
                This flag simply sets the useStiffnessPS attribute of the spring shape.  
                In both the flag and the attribute name, "PS" stands for "per-spring."  
                (Default = false )  
                Properties: create, query, edit
        walkLength (int?): This flag is valid only when doing wireframe creation.  
                It will create springs between pairs of points connected by the specified  
                number of edges.  For example, if walk length is 2, each pair of points  
                separated by no more than 2 edges will get a spring.  Walk length measures  
                the distance between pairs of vertices just like the number of blocks measures  
                the distance between two intersections in a city.  
                Properties: create
        wireframe (bool?): If True, sets the mode of the spring application to Wireframe.  
                This is valid only for springs created on a soft body.  
                It will add springs along all edges connecting the adjacent points  
                (vertices or CV's) of curves and surfaces.  
                (Default is False.)  
                Properties: create

    Returns:
        str: Command result

    Example:
    """

