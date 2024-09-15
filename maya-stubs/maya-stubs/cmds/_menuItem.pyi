from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def menuItem(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., allowOptionBoxes: bool = ..., annotation: Queryable[str] = ..., boldFont: bool = ..., checkBox: bool = ..., collection: Queryable[str] = ..., command: Queryable[Callable[..., Any]] = ..., data: Queryable[int] = ..., defineTemplate: str = ..., divider: bool = ..., dividerLabel: Queryable[str] = ..., docTag: Queryable[str] = ..., dragDoubleClickCommand: Queryable[Callable[..., Any]] = ..., dragMenuCommand: Queryable[Callable[..., Any]] = ..., echoCommand: bool = ..., enable: bool = ..., enableCommandRepeat: bool = ..., exists: bool = ..., familyImage: Queryable[str] = ..., image: Queryable[str] = ..., imageOverlayLabel: Queryable[str] = ..., insertAfter: str = ..., isCheckBox: bool = ..., isOptionBox: bool = ..., isRadioButton: bool = ..., italicized: bool = ..., label: Queryable[str] = ..., longDivider: bool = ..., optionBox: bool = ..., optionBoxIcon: Queryable[str] = ..., parent: str = ..., postMenuCommand: Queryable[Callable[..., Any]] = ..., postMenuCommandOnce: bool = ..., radialPosition: Queryable[str] = ..., radioButton: bool = ..., runTimeCommand: str = ..., sourceType: Queryable[str] = ..., subMenu: bool = ..., tearOff: bool = ..., useTemplate: str = ..., version: Queryable[str] = ..., visible: bool = ...) -> Union[str, bool, Callable[..., Any], int]:
    """This command creates/edits/queries menu items.
    Args:
        allowOptionBoxes (bool?): Deprecated. All menus and menu items always allow option boxes.  
                In the case of submenu items this flag specifies whether the  
                submenu will be able to support option box menu items.  
                Always returns true.  
                Properties: create, query
        annotation (Queryable[str]?): Annotate the menu item with an extra string value.  
                Properties: create, query, edit
        boldFont (bool?): Specify if text should be bold. Only supported in menus  
                which use the marking menu implementation.  Default is false  
                for Windows, and true for all other platforms.  
                Properties: create, query
        checkBox (bool?): Creates a check box menu item.  Argument specifies the  
                check box value.  
                Properties: create, query, edit
        collection (Queryable[str]?): To explicitly add a radio menu item to a radioMenuItemCollection.  
                Properties: create, query
        command (Queryable[Callable[..., Any]]?): Attaches a command/script that will be executed when the  
                item is selected. Note this command is not executed when the  
                menu item is in an optionMenu control.  
                Properties: create, query, edit
        data (Queryable[int]?): Attaches a piece of user-defined data to the menu item.  
                Properties: create, query, edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        divider (bool?): Creates a divider menu item.  
                Properties: create, query
        dividerLabel (Queryable[str]?): Adds a label to a divider menu item.  
                Properties: create, query, edit
        docTag (Queryable[str]?): Attaches a tag to the menu item.  
                Properties: create, query, edit
        dragDoubleClickCommand (Queryable[Callable[..., Any]]?): If the menu item is put on the shelf then this command  
                will be invoked when the corresponding shelf object is double  
                clicked.  
                Properties: create, query, edit
        dragMenuCommand (Queryable[Callable[..., Any]]?): If the menu item is put on the shelf then this command  
                will be invoked when the corresponding shelf object is clicked.  
                Properties: create, query, edit
        echoCommand (bool?): Specify whether the action attached with  
                the c/command flag should echo to the command output  
                areas when invoked. This flag is false by default and must be  
                specified with the c/command flag.  
                Properties: create, query, edit
        enable (bool?): Enable state for the menu item.  A disabled menu item is  
                dimmed and unresponsive.  An enabled menu item is selectable and  
                has normal appearance.  
                Properties: create, query, edit
        enableCommandRepeat (bool?): This flag only affects menu items to which a command can be  
                attached.  Specify true and the command may be repeated by  
                executing the command repeatLast.  This flag is true by  
                default for all items except for option box items.  
                Properties: create, query, edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        familyImage (Queryable[str]?): Get the filename of the family icon associated with the menu.  
                The family icon will be used for the shelf unless an icon is specified with  
                the image flag.  
                Properties: query
        image (Queryable[str]?): The filename of the icon associated with the menu item.  If  
                the menu containing the menu item is being edited with a  
                menuEditor widget, then the menuEditor will use this icon to  
                represent the menu item. This icon will be displayed on the  
                shelf when the menu item is placed there.  
                Properties: create, query, edit
        imageOverlayLabel (Queryable[str]?): Specify a short (5 character) text string to be overlayed  
                on top of the icon associated with the menu item. This is primarily  
                a mechanism for differentiating menu items that are using a Family  
                icon due to the fact that an icon image had not been explicitly  
                defined. The image overlay label will not be used if an icon  
                image is defined for the menu item.  
                Properties: create, query, edit
        insertAfter (str?): Specify After which item the new one will be placed. If  
                this flag is not specified, item is added at the end of the  
                menu. Use the empty string "" to insert before the first  
                item of the menu.  
                Properties: create
        isCheckBox (bool?): Returns true if the item is a check box item.  
                Properties: query
        isOptionBox (bool?): Returns true if the item is an option box item.  
                Properties: query
        isRadioButton (bool?): Returns true if the item is a radio button item.  
                Properties: query
        italicized (bool?): Specify if text should be italicized. Only supported in menus  
                which use the marking menu implementation.  Default is false.  
                Properties: create, query
        label (Queryable[str]?): The text that appears in the item.  
                Properties: create, query, edit
        longDivider (bool?): Indicate whether the divider is long or short. Has no effect  
                if divider label is set. Default is true.  
                Properties: create, query, edit
        optionBox (bool?): Indicates that the menu item will be an option box item.  This  
                item will appear to the right of the preceeding menu item.  
                Properties: create, query
        optionBoxIcon (Queryable[str]?): The filename of an icon to be used instead of the usual option box icon.  
                The icon is searched for in the folder specified by the XBMLANGPATH  
                environment variable.  
                The icon can be any size, but will be resized to the standard 16x16 pixels  
                when drawn.  
                Properties: create, query, edit
        parent (str?): Specify the menu that the item will appear in.  
                Properties: create
        postMenuCommand (Queryable[Callable[..., Any]]?): Specify a script to be executed when the submenu is about  
                to be shown.  
                Properties: create, query, edit
        postMenuCommandOnce (bool?): Indicate the pmc/postMenuCommand should only be  
                invoked once.  Default value is false, ie.  
                the pmc/postMenuCommand is invoked everytime the sub menu  
                is shown.  
                Properties: create, query, edit
        radialPosition (Queryable[str]?): The radial position of the menu item if it is in a Marking  
                Menu.  Radial positions are given in the form of a cardinal  
                direction, and may be "N", "NW", "W", "SW", "S", "SE", "E" or "NE".  
                Properties: create, query, edit
        radioButton (bool?): Creates a radio button menu item.  Argument specifies the  
                radio button value.  
                Properties: create, query, edit
        runTimeCommand (str?): A shortcut flag to link the menu item with a runTimeCommand.  
                The value is the name of the runTimeCommand (unique).  
                It copies the following fields from the runTimeCommand if those  
                fields have not been provided to this command:  
                label, annotation, image, command.  
                Note: command will be set to the runTimeCommand itself.  
                Properties: create, edit
        sourceType (Queryable[str]?): Set the language type for a command script. Can only be used in  
                conjunction with a command flag.  Without this flag, commands are  
                assumed to be the same language of the executing script.  In query  
                mode, will return the language of the specified command.  
                Valid values are "mel" and "python".  
                Properties: create, query, edit
        subMenu (bool?): Indicates that the item will have a submenu.  
                Subsequent menuItems will be added to the submenu  
                until setParent -menu is called.  Note that a submenu item  
                creates a menu object and consequently the menu command may  
                be used on the submenu item.  
                Properties: create, query
        tearOff (bool?): For the case where the menu item is a sub menu this flag will  
                make the sub menu tear-off-able. Note that this flag has no  
                effect on the other menu item types.  
                Properties: create, query
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        version (Queryable[str]?): Specify the version that this menu item feature was introduced.  
                The argument should be given as a string of the version number  
                (e.g. "2013", "2014"). Currently only accepts major version  
                numbers (e.g. 2013 Ext 1, or 2013.5 should be given as "2014").  
                Properties: create, query, edit
        visible (bool?): The visible state of the menu item.  A menu item is created  
                visible by default.  Note that a menu item's actual appearance is  
                also dependent on the visible state of its parent layout(s).  
                Properties: create, query, edit

    Returns:
        str: Full path name to the menu item.

    Example:
    """

