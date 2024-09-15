from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def requires(arg0: str = ..., arg1: str = ..., /, *, dataType: Multiuse[str] = ..., nodeType: Multiuse[str] = ...) -> bool:
    """This command is used during file I/O to specify the requirements
    needed to load the given file.  It defines what file format
    version was used to write the file, or what plug-ins are required to
    load the scene.The first string names a product (either "maya", or a plug-in name)The second string gives the version. This command is only useful during
    file I/O, so users should not have any need to use this command themselves.The flags "-nodeType" and "-dataType" specify the node types
    and data types defined by the plug-in. When Maya open a scene file, it
    runs "requires" command in the file and load required plug-ins. But some
    plug-ins may be not loaded because they are missing. The flags "-nodeType"
    and "-dataType" are used by the missing plug-ins. If one plug-in is missing,
    nodes and data created by this plug-in are created as unknown nodes and
    unknown data. Maya records their original types for these unknown nodes
    and data. When these nodes and data are saved back to file, it will be
    possible to determine the associated missing plug-ins. And when export
    selected nodes, Maya can write out the exact required plug-ins.
    The flags "-nodeType" and "-dataType" is optional. In this command, if these
    flags are not given for one plug-in and the plug-in is missing, the "requires"
    command of this plug-in will always be saved back.
    Args:
        dataType (Multiuse[str]?): Specify a data type defined by this plug-in.  
                The data type is specified by MFnPlugin::registerData() when register  
                the plug-in.  
                Properties: create, multiuse
        nodeType (Multiuse[str]?): Specify a node type defined by this plug-in.  
                The node type is specified by MFnPlugin::registerNode() when register  
                the plug-in.  
                Properties: create, multiuse

    Returns:
        bool:

    Example:
    """

