from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def hotBox(*, query: bool = ..., PaneOnlyMenus: bool = ..., PaneToggleMenus: bool = ..., animationOnlyMenus: bool = ..., animationToggleMenus: bool = ..., clothOnlyMenus: bool = ..., clothToggleMenus: bool = ..., commonOnlyMenus: bool = ..., commonToggleMenus: bool = ..., customMenuSetsToggleMenus: bool = ..., displayCenterOnly: bool = ..., displayHotbox: bool = ..., displayStyle: bool = ..., displayZonesOnly: bool = ..., dynamicsOnlyMenus: bool = ..., dynamicsToggleMenus: bool = ..., liveOnlyMenus: bool = ..., liveToggleMenus: bool = ..., menuSetOnly: str = ..., menuSetToggle: Tuple[str, bool] = ..., modelingOnlyMenus: bool = ..., modelingToggleMenus: bool = ..., noClickCommand: Callable[..., Any] = ..., noClickDelay: float = ..., noClickPosition: bool = ..., noKeyPress: bool = ..., polygonsOnlyMenus: bool = ..., polygonsToggleMenus: bool = ..., position: Tuple[int, int] = ..., release: bool = ..., renderingOnlyMenus: bool = ..., renderingToggleMenus: bool = ..., riggingOnlyMenus: bool = ..., riggingToggleMenus: bool = ..., rmbPopups: bool = ..., showAllToggleMenus: bool = ..., surfacesOnlyMenus: bool = ..., surfacesToggleMenus: bool = ..., transparenyLevel: Queryable[int] = ..., updateMenus: bool = ...) -> Union[bool, int]:
    """This command controls parameters related to the hotBox menubar palette.
    When the command is invoked with no flags, the hotBox is popped up.
    Args:
        PaneOnlyMenus (bool?): Sets a row of menus to be the only visible row.  
                Properties: create
        PaneToggleMenus (bool?): Sets the visibilty of a row of menus to on or off.  
                Properties: create, query
        animationOnlyMenus (bool?):   
                Properties: create, query
        animationToggleMenus (bool?):   
                Properties: create, query
        clothOnlyMenus (bool?):   
                Properties: create, query
        clothToggleMenus (bool?):   
                Properties: create, query
        commonOnlyMenus (bool?):   
                Properties: create, query
        commonToggleMenus (bool?):   
                Properties: create, query
        customMenuSetsToggleMenus (bool?):   
                Properties: create, query
        displayCenterOnly (bool?): Three different display styles are defined for the hotBox. It can  
                be fully displayed (dh), display only the marking menu zones  
                (dzo) or no display (dco) which means that the entire  
                screen can be used to access the marking menus defined in the center zone.  
                Properties: create
        displayHotbox (bool?):   
                Properties: create, query
        displayStyle (bool?): Returns a string that identifies the flag used to set the current  
                display style. The results can be dh, dzo, or  
                dco, depending on  which style the hotBox is using at the moment.  
                Properties: query
        displayZonesOnly (bool?):   
                Properties: create, query
        dynamicsOnlyMenus (bool?):   
                Properties: create, query
        dynamicsToggleMenus (bool?):   
                Properties: create, query
        liveOnlyMenus (bool?):   
                Properties: create, query
        liveToggleMenus (bool?):   
                Properties: create, query
        menuSetOnly (str?): Show only the named menu set  
                Properties: create
        menuSetToggle (Tuple[str, bool]?): Update the given menu sets with the paired toggle value  
                Properties: create
        modelingOnlyMenus (bool?):   
                Properties: create, query
        modelingToggleMenus (bool?):   
                Properties: create, query
        noClickCommand (Callable[..., Any]?): The command to be executed if the hotBox is engaged  
                and then disengaged within noClickDelay time units.  
                Properties: create
        noClickDelay (float?): If the hotBox is engaged and then disengaged within  
                this time interval, then the noClickCommand is executed.  
                The time interval is in seconds.  The default value is 0.1.  
                Properties: create
        noClickPosition (bool?): If a -noClickCommand has been specified then this flag will cause the X and Y  
                screen coordinates of the mouse pointer to be appended as arguments to that command.  
                The coordinates used are those of the pointer at the time when the hotbox command was  
                initiated.  
                Properties: create
        noKeyPress (bool?): Normally the hotbox is popped by a pressing a keyboard key. Use the  
                nkp flag to pop the hotbox from a device other than the keyboard  
                (still use the rl flag to unpop the hotbox).  
                Properties: create, query
        polygonsOnlyMenus (bool?):   
                Properties: create, query
        polygonsToggleMenus (bool?):   
                Properties: create, query
        position (Tuple[int, int]?): Specify the screen position the hotbox should be centered at next time  
                it is displayed.  The default is the cursor position.  
                Properties: create
        release (bool?): Action to be called on the release of the key which invoked the hotbox  
                Properties: create, query
        renderingOnlyMenus (bool?):   
                Properties: create, query
        renderingToggleMenus (bool?):   
                Properties: create, query
        riggingOnlyMenus (bool?):   
                Properties: create, query
        riggingToggleMenus (bool?):   
                Properties: create, query
        rmbPopups (bool?): Enables/Disables a popup menu of the current function set.  
                This popup menu appear when the right mouse button is pressed  
                in the center zone of the hotbox.  
                Properties: create, query
        showAllToggleMenus (bool?): Sets the visibility of all menus to on or off.  
                When queried, will only return true if all menu rows are visible.  
                Properties: create, query
        surfacesOnlyMenus (bool?):   
                Properties: create, query
        surfacesToggleMenus (bool?):   
                Properties: create, query
        transparenyLevel (Queryable[int]?): The percentage of transparency, from 0 to 100.  
                Currently, only the values 0, 25, 50, 75 and 100 are  
                supported.  Any other values will be rounded off  
                to the nearest supported value.  
                Properties: create, query
        updateMenus (bool?): Reloads the hotBox menus from the main menubar.  
                This flag is used when the menus in the main menubar are modified,  
                and the hotBox menus need to be refreshed.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

