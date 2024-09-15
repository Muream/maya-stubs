from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def attributeMenu(*args: Any, beginMenu: bool = ..., editor: str = ..., finishMenu: bool = ..., inputs: bool = ..., plug: str = ..., regPulldownMenuCommand: str = ..., unregPulldownMenuCommand: int = ...) -> str:
    """Action to generate popup connection menus for Hypershade. This command is
    used internally by the Hypershade panel.render, hypergraph, shader, hypershade
    Args:
        beginMenu (bool?): If true the menu will be used to start a connection edit so it will list all  
                available attributes for either inputs or outputs.  If false the menu will  
                be used to complete a connection so it will list only the attributes  
                compatible with the attribute at the other end of the connection.  A  
                plug must be supplied in this case.  
                Properties: create
        editor (str?): Name of the Hypergraph, Hypershade or Visor editor for which this menu  
                is being built.  This argument is no longer mandatory. If it is omitted,  
                the inputs flag and the node must be used to specify the search targets.  
                This allows attributeMenu to be used in the absence of a hypershade editor.  
                Properties: create
        finishMenu (bool?): finishes the menu  
                Properties: create
        inputs (bool?): If true only attributes which can be used as inputs will be listed.  If  
                false only attributes which can be used as outputs will be listed  
                Properties: create
        plug (str?): If inputs is false then we are completing a connection and the name  
                of the plug at the other end of the connection must be supplied.  
                Properties: create
        regPulldownMenuCommand (str?): This flag will register a callback that allows the user to define their own popup menu  
                for a specific node type for use in the Hypershade and Hypergraph editor.  
                The command signature should look like this:  
              
                global proc int proc_name>(string $editorName, string $nodeName, string $plug, string $mode, string $menuType)  
              
                The method should return 0 if it does not recognize the node type  
                and the default attributeMenu popup menu will be displayed.  
                If the callback returns one then the menu is considered built and no other menuItems will be  
                added to the popup. The return value from this flag will be the ID to use for the -unregPulldownMenuCommand flag.  
                Properties: create
        unregPulldownMenuCommand (int?): This flag will unregister a callback procedure that was registered with the -regPulldownMenuCommand flag.  
                The argument should be the integer identifier returned from the -regPulldownMenuCommand flag.  
                Properties: create

    Returns:
        str: Command result

    Example:
    """

