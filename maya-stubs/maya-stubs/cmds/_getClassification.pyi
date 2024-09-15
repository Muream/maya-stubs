from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def getClassification(arg0: str = ..., /, *, satisfies: str = ...) -> List[str]:
    """Returns the classification string for a given node type.Classification strings look like file pathnames ("shader/reflective" or "texture/2D", for
    example).  Multiple classifications can be combined into a single compound
    classification string by joining the individual classifications with ':'.
    For example, the classification string "shader/reflective:texture/2D" means
    that the node is both a reflective shader and a 2D texture.The classification string is used to determine how rendering nodes
    are categorized in various UI, such as the Create Render Node and HyperShade
    windows:The classification string is also used to determine how Viewport 2.0
    will interpret the node.
    Args:
        satisfies (str?): Returns true if the given node type's classification satisfies the classification  
                string which is passed with the flag.  
              
                A non-compound classification string A is said to satisfy a non-compound  
                classification string B if A is a subclassification of B (for example,  
                "shaders/reflective" satisfies "shaders").  
              
                A compound classification string A satisfies a compound classification  
                string B iff:  
              
              
                every component of A satisfies at least one component of B and   
                every component of B is satisfied by at least one component of A  
              
              
                Hence, "shader/reflective/phong:texture" satisfies "shader:texture", but  
                "shader/reflective/phong" does not satisfy "shader:texture".  
                Properties: create

    Returns:
        List[str]: Returns the classification strings for the given node type, or
            an empty array if the node type is not classified.

    Example:
    """

