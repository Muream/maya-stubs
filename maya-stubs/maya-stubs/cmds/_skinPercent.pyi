from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def skinPercent(arg0: str = ..., /, *args: str, query: bool = ..., ignoreBelow: float = ..., normalize: bool = ..., pruneWeights: float = ..., relative: bool = ..., resetToDefault: bool = ..., transform: Queryable[str] = ..., transformMoveWeights: Multiuse[str] = ..., transformValue: Multiuse[Tuple[str, float]] = ..., value: bool = ..., zeroRemainingInfluences: bool = ...) -> Union[bool, str]:
    """This command edits and queries the weight values on members of a
    skinCluster node, given as the first argument. If no object components
    are explicitly mentioned in the command line, the current selection
    list is used.Note that setting multiple weights in a single invocation of this
    command is far more efficient than calling it once per weighted
    vertex.
    Args:
        ignoreBelow (float?): Limits the output of the -value and -transform queries  
                to the entries whose weight values are over the specified  
                limit.  This flag has to be used before the -query flag.  
                      In query mode, this flag needs a value.  
                Properties: query
        normalize (bool?): If set, the weights not assigned by the -transformValue  
                flag are normalized so that the sum of the all weights  
                for the selected object component add up to 1. The default  
                is on. NOTE: The skinCluster has a normalizeWeights attribute  
                which when set to OFF overrides this attribute! If the  
                skinCluster.normalizeWeights attribute is OFF, you must  
                set it to Interactive in order to normalize weights using the  
                skinPercent command.  
                Properties: create
        pruneWeights (float?): Sets to zero any weight smaller than the given value for  
                all the selected components. To use this command to set  
                all the weights to zero, you must turn the -normalize flag  
                "off" or the skinCluster node will normalize the weights  
                to sum to one after pruning them. Weights for influences with  
                a true value on their "Hold Weights" attribute will not  
                be pruned.  
                Properties: create
        relative (bool?): Used with -transformValue to specify a relative setting of values.  
                If -relative is true, the value passed to -tv is added to the  
                previous value.  Otherwise, it replaces the previous value.  
                Properties: create
        resetToDefault (bool?): Sets the weights of the selected components to their  
                default values, overwriting any custom weights.  
                Properties: create
        transform (Queryable[str]?): In Mel, when used after the -query flag (without an argument)  
                the command returns an array of strings corresponding to  
                the names of the transforms influencing the selected object  
                components.  If used before the -query flag (with a  
                transform name), the command returns the weight of the  
                selected object component corresponding to the given  
                transform. The command will return an average weight if several  
                components have been selected.  
              
                In Python, when used with None instead of the name of the transform,  
                the command returns an array of strings corresponding to  
                the names of the transforms influencing the selected object  
                components. If used with a transform name, the command returns the weight of the  
                selected object. The command will return an average weight if several  
                components have been selected.  
              
                      In query mode, this flag can accept a value.  
                Properties: query
        transformMoveWeights (Multiuse[str]?): This flag is used to transfer weights from a source influence to one or more target influences. It acts on the selected vertices. The flag must be used at least twice to generate a valid command. The first flag usage indicates the source influence from which the weights will be copied. Subsequent flag usages indicate the target influences.  
                Properties: create, multiuse
        transformValue (Multiuse[Tuple[str, float]]?): Accepts a pair consisting of a transform name and a value  
                and assigns that value as the weight of the selected  
                object components corresponding to the given transform.  
                Properties: create, multiuse
        value (bool?): Returns an array of doubles corresponding to the  
                joint weights for the selected object component.  
                Properties: query
        zeroRemainingInfluences (bool?): If set, the weights not assigned by the -transformValue  
                flag are set to 0. The default is off.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

