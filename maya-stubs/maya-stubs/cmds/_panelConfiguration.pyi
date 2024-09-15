from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def panelConfiguration(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., addPanel: Multiuse[Tuple[bool, str, str, str, str]] = ..., configString: Queryable[str] = ..., createStrings: bool = ..., defaultImage: Queryable[str] = ..., defineTemplate: str = ..., editStrings: bool = ..., exists: bool = ..., image: Queryable[str] = ..., isFixedState: bool = ..., label: Queryable[str] = ..., labelStrings: bool = ..., numberOfPanels: bool = ..., removeAllPanels: bool = ..., removeLastPanel: bool = ..., replaceCreateString: Tuple[int, str] = ..., replaceEditString: Tuple[int, str] = ..., replaceFixedState: Tuple[int, bool] = ..., replaceLabel: Tuple[int, str] = ..., replacePanel: Tuple[int, bool, str, str, str, str] = ..., replaceTypeString: Tuple[int, str] = ..., sceneConfig: bool = ..., typeStrings: bool = ..., useTemplate: str = ..., userCreated: bool = ...) -> Union[str, bool]:
    """This command creates a panel configuration object. Typically you would
    not call this method command directly. Instead use the Panel Editor.Once a panel configuration is created you can make it appear in the
    main Maya window by selecting it from any panel's "Panels->Saved Layouts"
    menu.
    Args:
        addPanel (Multiuse[Tuple[bool, str, str, str, str]]?): Adds the specified panel to the configuration.  Arguments are:  
                isFixed, label string, type string, create string, edit string.  
                Properties: create, edit, multiuse
        configString (Queryable[str]?): Specifies the string that arranges the panels.  
                Properties: create, query, edit
        createStrings (bool?): Returns an string array of the panel creation strings.  
                Properties: query
        defaultImage (Queryable[str]?): The default image for this configuration. Once the default image  
                is set it may not be changed. If an image is set with the -i/image  
                flag then it's value will take precedence.  
                Properties: create, query
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        editStrings (bool?): Returns an string array of the panel edit strings.  
                Properties: query
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        image (Queryable[str]?): The user specified image for this configuration. Use this flag  
                to override the default image.  
                Properties: create, query, edit
        isFixedState (bool?): Returns an integer array of whether the panels have fixed states or not.  
                Properties: query
        label (Queryable[str]?): Configuration label.  
                Properties: create, query, edit
        labelStrings (bool?): Returns an string array of the panel labels.  
                Properties: query
        numberOfPanels (bool?): Returns the number of panels in the configuration.  
                Properties: query
        removeAllPanels (bool?): Removes the last panel in the config.  
                Properties: edit
        removeLastPanel (bool?): Removes the last panel in the config.  
                Properties: edit
        replaceCreateString (Tuple[int, str]?): Replaces the specified create string.  The index is 1 based.  
                Properties: edit
        replaceEditString (Tuple[int, str]?): Replaces the specified edit string.  The index is 1 based.  
                Properties: edit
        replaceFixedState (Tuple[int, bool]?): Replaces the specified fixed state value (true|false).  The index is 1 based.  
                Properties: edit
        replaceLabel (Tuple[int, str]?): Replaces the specified label.  The index is 1 based.  
                Properties: edit
        replacePanel (Tuple[int, bool, str, str, str, str]?): Replaces the specified panel in the configuration.  Arguments are:  
                index, isFixed, label string, type string, create string, edit string.  
                The index is 1 based.  
                Properties: create, edit
        replaceTypeString (Tuple[int, str]?): Replaces the specified type string.  The index is 1 based.  
                Properties: edit
        sceneConfig (bool?): Specifies whether the configuration is associated with the scene.  
                Scene configurations are created when the scene is opened and deleted when  
                the scene is closed.  
                Properties: create, query, edit
        typeStrings (bool?): Returns an string array of the panel types.  
                Properties: query
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        userCreated (bool?): Returns true if the configuration was created by the user. If it is user created, the configuration will show up in the RMB menu in the toolbox's saved layouts.  
                Properties: create, query, edit

    Returns:
        str: The name of the panelConfiguration created.

    Example:
    """

