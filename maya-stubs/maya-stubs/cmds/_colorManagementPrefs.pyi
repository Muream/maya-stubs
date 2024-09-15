from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def colorManagementPrefs(*, edit: bool = ..., query: bool = ..., cmConfigFileEnabled: bool = ..., cmEnabled: bool = ..., colorManageAllNodes: bool = ..., colorManagePots: bool = ..., colorManagedNodes: bool = ..., colorManagementSDKVersion: Queryable[str] = ..., configFilePath: Queryable[str] = ..., configFileVersion: Queryable[str] = ..., defaultInputSpaceName: Queryable[str] = ..., displayName: Queryable[str] = ..., displayNames: bool = ..., equalsToPolicyFile: str = ..., exportPolicy: str = ..., inhibitEvents: bool = ..., inputSpaceDescription: str = ..., inputSpaceFamilies: str = ..., inputSpaceNames: bool = ..., loadPolicy: str = ..., loadedDefaultInputSpaceName: Queryable[str] = ..., loadedDisplayName: Queryable[str] = ..., loadedOutputTransformName: Queryable[str] = ..., loadedRenderingSpaceName: Queryable[str] = ..., loadedViewName: Queryable[str] = ..., loadedViewTransformName: Queryable[str] = ..., missingColorSpaceNodes: bool = ..., ocioRulesEnabled: bool = ..., ociov2Enabled: bool = ..., outputTarget: str = ..., outputTransformEnabled: bool = ..., outputTransformName: Queryable[str] = ..., outputTransformNames: bool = ..., outputTransformUseColorConversion: bool = ..., outputUseViewTransform: bool = ..., policyFileName: Queryable[str] = ..., popupOnError: bool = ..., refresh: bool = ..., renderingSpaceName: Queryable[str] = ..., renderingSpaceNames: bool = ..., restoreDefaults: bool = ..., viewDisplayNames: str = ..., viewName: Queryable[str] = ..., viewNames: bool = ..., viewTransformName: Queryable[str] = ..., viewTransformNames: bool = ...) -> Union[bool, str]:
    """This command allows querying and editing the color management global data in a
    scene.  It also allows for setting the view transform and rendering space which
    automatically configures the color processing in the enabled views.color, management
    Args:
        cmConfigFileEnabled (bool?): Turn on or off applying an OCIO configuration file.  If set, the color  
                management configuration set in the preferences is used.  
                Properties: query, edit
        cmEnabled (bool?): Turn on or off color management in general.  If set, the color  
                management configuration set in the preferences is used.  
                Properties: query, edit
        colorManageAllNodes (bool?): Adds color management to all input nodes such as file texture nodes  
                Properties: create
        colorManagePots (bool?): Turn on or off color management of color pots in the UI.  If set, colors  
                in color pots are taken to be in rendering space, and are displayed after being  
                transformed by the view transform set in the preferences.  
                Properties: query, edit
        colorManagedNodes (bool?): Gets the names of all nodes that apply color management to bring pixels from an input color space  
                to the rendering space. Examples include file texture node.  
                Properties: query
        colorManagementSDKVersion (Queryable[str]?): Obtain the version of the color management SDK used by Maya.  
                Properties: query
        configFilePath (Queryable[str]?): The configuration file to be used, if color management is enabled.  
                Properties: query, edit
        configFileVersion (Queryable[str]?): Obtain the version of the config version.  
                Properties: query
        defaultInputSpaceName (Queryable[str]?): This flag is obsolete.  See the colorManagementFileRules command for more  
                information.  
                Properties: query, edit
        displayName (Queryable[str]?): The display from the (display, view) pair, to be applied by color managed viewers and color  
                managed UI controls.  
                Properties: query, edit
        displayNames (bool?): Returns the list of available displays.  Used to populate the color  
                management preference UI popup.  
                Properties: query
        equalsToPolicyFile (str?): Query if the current loaded policy settings is the same with the settings described  
                in the policy file which is the argument of the command.  
                			In query mode, this flag needs a value.  
                Properties: query
        exportPolicy (str?): Export the color management parameters to policy file  
                Properties: create
        inhibitEvents (bool?): Inhibit client-server notifications and event triggers which occur when changing  
                the color management settings.  
                Properties: create
        inputSpaceDescription (str?): Returns the description for a specific input color space.  
                			In query mode, this flag needs a value.  
                Properties: query
        inputSpaceFamilies (str?): Returns the list of families for a specific input color space. Used to add submenus  
                when populating the input color spaces UI popup.  
                			In query mode, this flag needs a value.  
                Properties: query
        inputSpaceNames (bool?): Returns the list of available input color spaces. Used to populate the input color  
                spaces UI popup.  
                Properties: query
        loadPolicy (str?): Load the color management policy file. This file overides the color management settings.  
                Properties: create
        loadedDefaultInputSpaceName (Queryable[str]?): This flag is obsolete.  
                Properties: query
        loadedDisplayName (Queryable[str]?): Gets the loaded display from the (display, view) pair.  Used by file open, import, and reference  
                to check for missing color spaces or transforms.  
                Properties: query
        loadedOutputTransformName (Queryable[str]?): Gets the loaded output transform.  Used by file open, import, and reference  
                to check for missing color spaces or transforms.  
                Properties: query
        loadedRenderingSpaceName (Queryable[str]?): Gets the loaded rendering space.  Used by file open, import, and reference  
                to check for missing color spaces or transforms.  
                Properties: query
        loadedViewName (Queryable[str]?): Gets the loaded view from the (display, view) pair.  Used by file open, import, and reference  
                to check for missing color spaces or transforms.  
                Properties: query
        loadedViewTransformName (Queryable[str]?): Gets the loaded view transform.  Used by file open, import, and reference  
                to check for missing color spaces or transforms.  
                Properties: query
        missingColorSpaceNodes (bool?): Gets the names of the nodes that have color spaces not defined in the selected transform collection  
                or in the selected config file. Note that an inactive color space is not a missing color space.  
                Properties: query
        ocioRulesEnabled (bool?): Turn on or off the use of colorspace assignment rules from the OCIO library.  
                Properties: query, edit
        ociov2Enabled (bool?): Is OCIOv2 the colour management system by default.  
                Properties: query
        outputTarget (str?): Indicates to which output the outputTransformEnabled or the outputTransformName  
                flags are to be applied. Valid values are "renderer" or "playblast".  
                			In query mode, this flag needs a value.  
                Properties: query, edit
        outputTransformEnabled (bool?): Turn on or off applying the output transform for out of viewport renders.  
                If set, the output transform set in the preferences is used.  
                Properties: query, edit
        outputTransformName (Queryable[str]?): The output transform to be applied for out of viewport renders.  Disables  
                output use view transform mode.  
                Properties: query, edit
        outputTransformNames (bool?): Returns the list of available output transforms.  
                Properties: query
        outputTransformUseColorConversion (bool?): Turn on or off selecting the color space conversion for the output color space  
                of viewport renders.  If set, a conversion color space is used; otherwise,  
                a view transform is used.  
                Properties: query, edit
        outputUseViewTransform (bool?): Turns use view transform mode on.  In this mode, the output transform is set  
                to match the view transform.  To turn the mode off, set an output transform  
                using the outputTransformName flag.  
                Properties: query, edit
        policyFileName (Queryable[str]?): Set the policy file name  
                Properties: query, edit
        popupOnError (bool?): Turn on or off displaying a modal popup on error (as well as the normal  
                script editor reporting of the error), for this invocation of the  
                command.  Default is off.  
                Properties: edit
        refresh (bool?): Refresh the color management.  
                Properties: create
        renderingSpaceName (Queryable[str]?): The color space to be used during rendering.  This is the  
                source color space to the viewing transform, for color managed viewers and  
                color managed UI controls, and the destination color space for color managed  
                input pixels.  
                Properties: query, edit
        renderingSpaceNames (bool?): Returns the list of available rendering spaces.  Used to populate the color  
                management preference UI popup.  
                Properties: query
        restoreDefaults (bool?): Restore the color management settings to their default value.  
                Properties: create
        viewDisplayNames (str?): Returns the list of available views for a specific display. Used to populate the view name  
                list UI for file and image plane nodes.  
                			In query mode, this flag needs a value.  
                Properties: query
        viewName (Queryable[str]?): The view from the (display, view) pair, to be applied by color managed viewers and color  
                managed UI controls.  
                Properties: query, edit
        viewNames (bool?): Returns the list of available views from the selected display.  Used to populate the color  
                management preference UI popup.  
                Properties: query
        viewTransformName (Queryable[str]?): The view transform to be applied by color managed viewers and color  
                managed UI controls.  
                Properties: query, edit
        viewTransformNames (bool?): Returns the list of available view transforms.  Used to populate the color  
                management preference UI popup.  
                Properties: query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

