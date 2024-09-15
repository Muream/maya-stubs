from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def roundConstantRadius(arg0: str = ..., /, *args: str, edit: bool = ..., query: bool = ..., append: bool = ..., constructionHistory: bool = ..., name: str = ..., object: bool = ..., radiuss: Multiuse[float] = ..., side: Multiuse[Tuple[str, int]] = ..., sidea: Multiuse[int] = ..., sideb: Multiuse[int] = ...) -> List[str]:
    """This command generates constant radius NURBS fillets and NURBS
    corner surfaces for matching edge pairs on NURBS surfaces.  An
    edge pair is a matching pair of surface isoparms or trim edges.
    This command
    can handle more than one edge pair at a time.
    This command can also handleedges, which is where an edge
    pair is composed of more than two surfaces.  Use the "-sa" and "-sb"
    flags in this case.The results from this command are three surface var groups plus the
    name of the new roundConstantRadius dependency node, if history was on.
    The 1st var group contains trimmed copies of the original surfaces.  The 2nd
    var group contains the new NURBS fillet surfaces.  The 3rd var group
    contains the new NURBS corners (if any).A simple example of an edge pair is an edge of a NURBS cube,
    where two faces of the cube meet.  This command generates a NURBS
    fillet at the edge and trims back the faces.Another example is a NURBS cylinder with a planar trim surface cap.
    This command will create a NURBS fillet where the cap meets the
    the cylinder and will trim back the cap and the cylinder.Another example involves all 12 edges of a NURBS cube.  NURBS fillets
    are created where any face meets another face.  NURBS corners are
    created whenever 3 edges meet at a corner.
    Args:
        append (bool?): If true, then an edge pair is being added to an existing  
                round dependency node.  Default is false.  
                When this flag is true, an existing round dependency node  
                must be specified. See example below.  
                Properties: create
        constructionHistory (bool?): Turn the construction history on or off.  
                Properties: create
        name (str?): Sets the name of the newly-created node. If it contains  
                namespace path, the new node will be created under the  
                specified namespace; if the namespace does not exist, it  
                will be created.  
                Properties: create
        object (bool?): Create the result, or just the dependency node.  
                Properties: create
        radiuss (Multiuse[float]?): Use this flag to specify radius.  This overrides the  
                "r/radius" flag.  If only one "rad" flag is used,  
                then it is applied to all edge pairs.  If more than one "rad" flag is used,  
                then the number of "-rad" flags must equal the number  
                of edge pairs.  For example, for four edge pairs,  
                zero, one or four "rad" flags must be specified.  
                Properties: create, multiuse
        side (Multiuse[Tuple[str, int]]?): Use this flag for compound edges.  It replaces the sidea/sideb flags and is  
                compatible with Python.  
              
                The first argument must be either "a" or "b".  
              
                The same number of "a" values as "b" values must be specified.  
                If no sides are specified with the "side" flag (or sidea/sideb flags), then  
                the edges are assumed to be in pairs.  
                See also examples below.  
                For example, two faces of a cube meet at an edge pair.  
                Suppose one of the faces is then split in two pieces  
                at the middle of the edge, so that there is one  
                face on side "A", and two pieces on side "B".  In this case  
                the flag combination: -side "a" 1. side "b" 2 would be used.  
                The edges must be specified in the corresponding order:  
                // MEL  
                roundConstantRadius -side "a" 1. side "b" 2 isoA isoB1 isoB2;  
                # Python  
                maya.cmds.roundConstantRadius( 'isoA', 'isoB1', 'isoB2', side=[("a",1), ("b",2)] )  
                Properties: create, multiuse
        sidea (Multiuse[int]?): Use this flag for compound edges in conjunction with the  
                following "-sb" flag.  
              
                This flag is not intended for use from Python.  Please see "side" flag instead.  
              
                The same number of "-sa" flags as "-sb" flags must be specified.  
                If no "-sa" nor "-sb" flags are specified, then the edges  
                are assumed to be in pairs.  
                See also examples below.  
                For example, two faces of a cube meet at an edge pair.  
                Suppose one of the faces is then split in two pieces  
                at the middle of the edge, so that there is one  
                face on side "A", and two pieces on side "B".  In this case,  
                the flag combination: -sidea 1. sideb 2 would be used.  
                The edges must be specified in the corresponding order:  
                roundConstantRadius -sidea 1. sideb 2 isoA isoB1 isoB2;  
                Properties: create, multiuse
        sideb (Multiuse[int]?): Use this flag for compound edges in conjunction with the  
                "-sa" flag.  See description for the "-sa" flag.  
              
                This flag is not intended for use from Python.  Please see "side" flag instead.  
                Properties: create, multiuse

    Returns:
        List[str]: (resulting NURBS surfaces' names and node name)

    Example:
    """

