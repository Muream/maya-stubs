from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def geometryAttrInfo(*args: str, boundingBox: bool = ..., castToEdges: bool = ..., castToFaces: bool = ..., castToVerts: bool = ..., componentTagCategory: bool = ..., componentTagExpression: str = ..., componentTagHash: bool = ..., componentTagHistory: bool = ..., componentTagHistoryHash: bool = ..., componentTagNames: bool = ..., components: bool = ..., deformerChain: bool = ..., elementCount: bool = ..., groupId: int = ..., matrix: bool = ..., nodeChain: bool = ..., originalGeometry: bool = ..., outputPlugChain: bool = ..., plugChain: bool = ..., pointCount: bool = ..., pointIndices: bool = ..., points: bool = ..., subsetState: bool = ...) -> Any:
    """This command provides information about the geometry in an attribute. This
    command therefore only works on attributes that contain geometry.
    A variety of types of information can be requested, like the number of verts,
    the boundingbox, which componentTags exist, etc.The requests can be made on a subset of the geometry, either limited by a
    specific groupId or by a componentTag expression. For example, when a componentTag
    expression is used, the requested indices will be the indices that match the
    subset as defined by that expression.
    Args:
        boundingBox (bool?): Returns the bounding box of the geometry  
                Properties: create
        castToEdges (bool?): Ensures the componentTag expression will be resolved to edge components  
                Properties: create
        castToFaces (bool?): Ensures the componentTag expression will be resolved to face components  
                Properties: create
        castToVerts (bool?): Ensures the componentTag expression will be resolved to vert components  
                Properties: create
        componentTagCategory (bool?): This flag will return the component tag category of the resulting components.  
                Verts are "v", edges are "e", faces are "f". In case the the category can not  
                be determined "unknown" is returned  
                Properties: create
        componentTagExpression (str?): Specifies the componentTagExpression we want to query. When specified all answers to  
                the information requests will be limited to the subset of the geometry as is  
                contained in the combination of these componentTags  
                Properties: create
        componentTagHash (bool?): This flag will return a unique hash value for the state of all the componentTags  
                contained in the geometry. If a hash is different from before it means that  
                something has changed, either tags have been added/removed/renamed and/or their  
                component contents have been altered.  
                Properties: create
        componentTagHistory (bool?): This flag will return a description of the componentTags and the nodes in the chain  
                where they were added to the geometry.  
                Properties: create
        componentTagHistoryHash (bool?): This flag will return a unique hash value for the componentTag history of the  
                geometry in the plug. If a hash is different from before it means that  
                something has changed, either different nodes have created the tags or the  
                contents of the tags have been altered.  
                Properties: create
        componentTagNames (bool?): Returns the names of the componentTags on the geometry  
                Properties: create
        components (bool?): Returns the components of the geometry  
                Properties: create
        deformerChain (bool?): This flag will return the list of deformer nodes through which the geometry passes to the specified plug  
                Properties: create
        elementCount (bool?): Returns the element count of the components  
                Properties: create
        groupId (int?): Specifies the groupId we want to query. When specified all answers to the  
                information requests will be limited to the subset of the geometry as is  
                contained in this groupId  
                Properties: create
        matrix (bool?): Returns the matrix associated with the geometry  
                Properties: create
        nodeChain (bool?): This flag will return the list of nodes through which the geometry passes to the specified plug  
                Properties: create
        originalGeometry (bool?): This flag will return the name of a plug on a node upstream (likely at the front end)  
                that is the best candidate to be used as the originalGeometry. This can return an  
                empty plug when none exists.  
                Properties: create
        outputPlugChain (bool?): This flag will return the chain of plugs upstream of the specified plug (including only output plugs)  
                Properties: create
        plugChain (bool?): This flag will return the chain of plugs upstream of the specified plug (including both input and output plugs)  
                Properties: create
        pointCount (bool?): Returns the point count of the geometry  
                Properties: create
        pointIndices (bool?): Returns the indices of the geometry  
                Properties: create
        points (bool?): Returns a list of points of the geometry  
                Properties: create
        subsetState (bool?): Returns the state of the specified subset  
                -1 means the subset was invalid  
                0 means the subset contains none of the points of the geometry  
                1 means the subset contains some (but not all) of the points of the geometry  
                2 means the subset contains all the points of the geometry  
                Properties: create

    Returns:
        Any: Information about the geometry in the attribute. The number and type
            of values returned depends on the information request.

    Example:
    """

