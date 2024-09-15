from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def scriptNode(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., afterScript: Queryable[str] = ..., beforeScript: Queryable[str] = ..., executeAfter: bool = ..., executeBefore: bool = ..., ignoreReferenceEdits: bool = ..., name: str = ..., scriptType: Queryable[int] = ..., sourceType: Queryable[str] = ...) -> Union[bool, str, int]:
    """scriptNodes contain scripts that are executed when a file is loaded or
    when the script node is deleted. If a script modifies a referenced node,
    the changes will be tracked as reference edits unless the scriptNode was
    created with the ignoreReferenceEdits flag. The scriptNode command is used
    to create, edit, query, and test scriptNodes.
    Args:
        afterScript (Queryable[str]?): The script executed when the script node is deleted.   
                C: The default is an empty string.   
                Q: When queried, this flag returns a string.  
                Properties: create, query, edit
        beforeScript (Queryable[str]?): The script executed during file load.   
                C: The default is an empty string.   
                Q: When queried, this flag returns a string.  
                Properties: create, query, edit
        executeAfter (bool?): Execute the script stored in the .after attribute of the  
                scriptNode. This script is normally executed when the script node  
                is deleted.  
                Properties: create
        executeBefore (bool?): Execute the script stored in the .before attribute of the  
                scriptNode. This script is normally executed when the file  
                is loaded.  
                Properties: create
        ignoreReferenceEdits (bool?): Sets whether changes made to referenced nodes during the execution of the  
                script should be recorded as reference edits. This flag must be set when  
                the scriptNode is created. If this flag is not set, changes to referenced  
                nodes will be recorded as edits by default.  
                Properties: create
        name (str?): When creating a new scriptNode, this flag specifies the name  
                of the node. If a non-unique name is used, the name will be  
                modified to ensure uniqueness.  
                Properties: create
        scriptType (Queryable[int]?): Specifies when the script is executed. The following  
                values may be used:  
              
              
                0 Execute on demand.  
              
              
                1 Execute on file load or on node deletion.  
              
              
                2 Execute on file load or on node deletion  
                when not in batch mode.   
              
              
                3 Internal  
              
              
                4 Execute on software render  
              
              
                5 Execute on software frame render  
              
              
                6 Execute on scene configuration  
              
              
                7 Execute on time changed  
              
              
                C: The default value is 0.   
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        sourceType (Queryable[str]?): Sets the language type for both the attached scripts.  
                Valid values are "mel" (enabled by default), and "python".  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

