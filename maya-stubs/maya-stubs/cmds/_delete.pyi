from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def delete(*args: str, all: bool = ..., attribute: Multiuse[str] = ..., channels: bool = ..., constraints: bool = ..., constructionHistory: bool = ..., controlPoints: bool = ..., expressions: bool = ..., hierarchy: str = ..., inputConnectionsAndNodes: bool = ..., motionPaths: bool = ..., shape: bool = ..., staticChannels: bool = ..., timeAnimationCurves: bool = ..., unitlessAnimationCurves: bool = ...) -> bool:
    """This command is used to delete selected objects, or all objects, or
    objects specified along with the command. Flags are available to
    filter the type of objects that the command acts on.At times, more than just specified items will be deleted.  For
    example, deleting two CVs in the same "row" on a NURBS surface
    will delete the whole row.
    Args:
        all (bool?): Remove all objects of specified kind, in the scene. This flag  
                is to be used in conjunction with the following flags.  
                Properties: create
        attribute (Multiuse[str]?): List of attributes to select  
                      In query mode, this flag needs a value.  
                Properties: create, multiuse
        channels (bool?): Remove animation channels in the scene. Either all channels  
                can be removed, or the scope can be narrowed down by specifying  
                some of the above mentioned options.  
                Properties: create
        constraints (bool?): Remove selected constraints and constraints attached to the  
                selected nodes, or remove all constraints in the scene.  
                Properties: create
        constructionHistory (bool?): Remove the construction history on the objects specified or  
                selected.  
                Properties: create
        controlPoints (bool?): This flag explicitly specifies whether or not to include the  
                control points of a shape (see "-s" flag) in the list of attributes.  
                Default: false.  (Not valid for "pasteKey" cmd.)  
                In query mode, this flag needs a value.  
                Properties: create
        expressions (bool?): Remove expressions in the scene. Either all expressions  
                can be removed, or the scope can be narrowed down by specifying  
                some of the above mentioned options.  
                Properties: create
        hierarchy (str?): Hierarchy expansion options.  Valid values are "above,"  
                "below," "both," and "none." (Not valid for "pasteKey" cmd.)  
                In query mode, this flag needs a value.  
                Properties: create
        inputConnectionsAndNodes (bool?): Break input connection to specified attribute and delete all  
                unconnected nodes that are left behind. The graph will be  
                traversed until a node that cannot be deleted is encountered.  
                Properties: create
        motionPaths (bool?): Remove motion paths in the scene. Either all  
                motion paths can be removed, or the scope can be narrowed down  
                by specifying some of the above mentioned options.  
                Properties: create
        shape (bool?): Consider attributes of shapes below transforms as well,  
                except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.)  
                In query mode, this flag needs a value.  
                Properties: create
        staticChannels (bool?): Remove static animation channels in the scene. Either all  
                static channels can be removed, or the scope can be narrowed down  
                by specifying some of the above mentioned options.  
                Properties: create
        timeAnimationCurves (bool?): Modifies the -c/channels and -sc/staticChannels flags.  
                When true, only channels connected to time-input  
                animation curves (for instance, those created by  
                'setKeyframe' will be deleted.  When false, no  
                time-input animation curves will be deleted.  
                Default: true.  
                Properties: create
        unitlessAnimationCurves (bool?): Modifies the -c/channels and -sc/staticChannels flags.  
                When true, only channels connected to  
                unitless-input animation curves (for instance,  
                those created by 'setDrivenKeyframe' will be  
                deleted.  When false, no unitless-input  
                animation curves will be deleted.  Default:  
                true.  
                Properties: create

    Returns:
        bool:

    Example:
    """

