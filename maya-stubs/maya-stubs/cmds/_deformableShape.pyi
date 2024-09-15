from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def deformableShape(*args: str, chain: bool = ..., createOriginalGeometry: bool = ..., createTweakNode: bool = ..., createUpstreamTagInjectionNode: bool = ..., deformShapeInAttr: bool = ..., deformShapeOutAttr: bool = ..., frontOfChain: bool = ..., localShapeInAttr: bool = ..., localShapeOutAttr: bool = ..., nodeChain: bool = ..., originalGeometry: bool = ..., outputPlugChain: bool = ..., plugChain: bool = ..., supportsComponentTags: bool = ..., tagInjectionList: bool = ..., tagInjectionNode: bool = ..., tweakNode: bool = ..., upstreamTagInjectionNode: bool = ..., worldShapeOutAttr: bool = ...) -> bool:
    """This command finds information about deforming shape(s).If no shapes are specified on the command then the curently selected
    shapes are used.
    Args:
        chain (bool?): This flag will return the list of deformers that deformer the specified shapes  
                Properties: create
        createOriginalGeometry (bool?): This creates an original geometry for the shape if it does not exist yet.  
                Properties: create
        createTweakNode (bool?): This creates a traditional tweak node if one did not exist yet.  
                Properties: create
        createUpstreamTagInjectionNode (bool?): This creates an upstream component tag injection node if an editable one does not exist yet.  
                Properties: create
        deformShapeInAttr (bool?): Returns the name of deform shape in attribute  
                Properties: create
        deformShapeOutAttr (bool?): Returns the name of deform shape out attribute  
                Properties: create
        frontOfChain (bool?): This flag will return the name of the plug on a shape node at the front end of  
                the deformation chain. This can return an empty plug when none exists.  
                Properties: create
        localShapeInAttr (bool?): Returns the name of local shape in attribute  
                Properties: create
        localShapeOutAttr (bool?): Returns the name of local shape out attribute  
                Properties: create
        nodeChain (bool?): This flag will return the list of nodes through which the geometry passes to get to this shape  
                Properties: create
        originalGeometry (bool?): This flag will return the name of a plug on a node in the deformation chain  
                (likely at the front end) that is the best candidate to be used as the  
                originalGeometry. This can return an empty plug when none exists.  
                Properties: create
        outputPlugChain (bool?): This flag will return the list of output plugs leading to the shape  
                Properties: create
        plugChain (bool?): This flag will return the list of plugs leading to the shape (both input and output plugs)  
                Properties: create
        supportsComponentTags (bool?): Returns whether the shape supports component tags  
                Properties: create
        tagInjectionList (bool?): This flag will return the list of nodes which are non-procedural componentTag injection nodes  
                Properties: create
        tagInjectionNode (bool?): This flag will return the name of the non-referenced component tag injection node as high  
                up in the deformation chain as possible. This can be the same as the input shape or an  
                empty string when none exists.  
                Properties: create
        tweakNode (bool?): This flag will return the name of the tweak node in the deformation chain.  
                This can return an empty string when none exists.  
                Properties: create
        upstreamTagInjectionNode (bool?): This flag will return the name of the non-referenced component tag injection node most  
                upstream from (but not including) the input shape.  
                This can be an empty string when none exists. If so, one can be created using the  
                cti/createUpstreamTagInjectionNode flag.  
                Properties: create
        worldShapeOutAttr (bool?): Returns the name of world shape out attribute  
                Properties: create

    Returns:
        bool:

    Example:
    """

