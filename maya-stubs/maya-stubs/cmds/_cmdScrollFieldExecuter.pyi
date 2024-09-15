from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def cmdScrollFieldExecuter(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., annotation: Queryable[str] = ..., appendText: str = ..., autoCloseBraces: bool = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., clear: bool = ..., commandCompletion: bool = ..., copySelection: bool = ..., currentLine: Queryable[int] = ..., cutSelection: bool = ..., defineTemplate: str = ..., docTag: Queryable[str] = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., execute: bool = ..., executeAll: bool = ..., exists: bool = ..., fileChangedCommand: Callable[..., Any] = ..., filename: bool = ..., filterKeyPress: Queryable[Callable[..., Any]] = ..., fullPathName: bool = ..., hasFocus: bool = ..., hasSelection: bool = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., insertText: str = ..., isObscured: bool = ..., load: bool = ..., loadContents: str = ..., loadFile: str = ..., manage: bool = ..., modificationChangedCommand: Callable[..., Any] = ..., modified: bool = ..., noBackground: bool = ..., numberOfLines: Queryable[int] = ..., numberOfPopupMenus: bool = ..., objectPathCompletion: bool = ..., parent: Queryable[str] = ..., pasteSelection: bool = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., redo: bool = ..., removeStoredContents: str = ..., replaceAll: Tuple[str, str] = ..., saveFile: str = ..., saveSelection: str = ..., saveSelectionToShelf: bool = ..., searchAndSelect: bool = ..., searchDown: bool = ..., searchMatchCase: bool = ..., searchString: Queryable[str] = ..., searchWraps: bool = ..., select: Tuple[int, int] = ..., selectAll: bool = ..., selectedText: bool = ..., showLineNumbers: bool = ..., showTabsAndSpaces: bool = ..., showTooltipHelp: bool = ..., source: bool = ..., sourceType: Queryable[str] = ..., spacesPerTab: Queryable[int] = ..., statusBarMessage: str = ..., storeContents: str = ..., tabsForIndent: bool = ..., text: Queryable[str] = ..., textLength: bool = ..., undo: bool = ..., useTemplate: str = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., width: Queryable[int] = ...) -> Union[str, bool, Tuple[float, float, float], int, Callable[..., Any]]:
    """A script editor executer control used to issue script commands to
    Maya.
    Args:
        annotation (Queryable[str]?): Annotate the control with an extra string value.  
                Properties: create, query, edit
        appendText (str?): Appends text to the end of this field.  
                Properties: create, edit
        autoCloseBraces (bool?): Specifies whether a closing brace should automatically be added when  
                hitting enter after an opening brace. (default on)  
                Properties: create, query, edit
        backgroundColor (Queryable[Tuple[float, float, float]]?): The background color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                When setting backgroundColor, the background is automatically  
                enabled, unless enableBackground is also specified with a false  
                value.  
                Properties: create, query, edit
        clear (bool?): Clears the field.  
                Properties: create, edit
        commandCompletion (bool?): Enable/disable command completion  
                Properties: create, query, edit
        copySelection (bool?): Copies the current selection from this field.  
                Properties: create, edit
        currentLine (Queryable[int]?): Sets/returns the current line which the cursor is on.  
                Properties: create, query, edit
        cutSelection (bool?): Cuts the current selection from this field.  
                Properties: create, edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        docTag (Queryable[str]?): Add a documentation flag to the control.  The documentation flag  
                has a directory structure.  
                (e.g., -dt render/multiLister/createNode/material)  
                Properties: create, query, edit
        dragCallback (Callable[..., Any]?): Adds a callback that is called when the middle mouse button  
                is pressed.  The MEL version of the callback is of the form:  
              
                global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  
              
                The proc returns a string array that is transferred to the drop site.  
                By convention the first string in the array describes the user settable  
                message type.  Controls that are application defined drag sources may  
                ignore the callback. $mods allows testing for the key modifiers CTRL and  
                SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL,  
                3 == CTRL + SHIFT.  
              
                In Python, it is similar, but there are two ways to specify the callback.  The  
                recommended way is to pass a Python function object as the argument.  In that  
                case, the Python callback should have the form:  
              
                def callbackName( dragControl, x, y, modifiers ):  
              
                The values of these arguments are the same as those for the MEL version above.  
              
                The other way to specify the callback in Python is to specify a string to be  
                executed.  In that case, the string will have the values substituted into it  
                via the standard Python format operator.  The format values are passed in a  
                dictionary with the keys "dragControl", "x", "y", "modifiers".  The  
                "dragControl" value is a string and the other values are integers (eg the  
                callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")  
                Properties: create, edit
        dropCallback (Callable[..., Any]?): Adds a callback that is called when a drag and drop  
                operation is released above the drop site.  The MEL version of the callback is  
                of the form:  
              
                global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  
              
                The proc receives a string array that is transferred from the drag source.  
                The first string in the msgs array describes the user defined message type.  
                Controls that are application defined drop sites may ignore the  
                callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  
              
                In Python, it is similar, but there are two ways to specify the callback.  The  
                recommended way is to pass a Python function object as the argument.  In that  
                case, the Python callback should have the form:  
              
                def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  
              
                The values of these arguments are the same as those for the MEL version above.  
              
                The other way to specify the callback in Python is to specify a string to be  
                executed.  In that case, the string will have the values substituted into it  
                via the standard Python format operator.  The format values are passed in a  
                dictionary with the keys "dragControl", "dropControl", "messages", "x", "y",  
                "type".  The "dragControl" value is a string and the other values are integers  
                (eg the callback string could be  
                "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")  
                Properties: create, edit
        enable (bool?): The enable state of the control.  By default, this flag is  
                set to true and the control is enabled.  Specify false and the control  
                will appear dimmed or greyed-out indicating it is disabled.  
                Properties: create, query, edit
        enableBackground (bool?): Enables the background color of the control.  
                Properties: create, query, edit
        enableKeyboardFocus (bool?): If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.  
                This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.  
                If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).  
                Properties: create, query, edit
        execute (bool?): Executes the current selection.  If there is no selection, all text is executed.  
                Properties: create, edit
        executeAll (bool?): Executes all text.  
                Properties: create, edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        fileChangedCommand (Callable[..., Any]?): Only valid when this field contains a file.  
                Sets a script which will be called whenever the file is externally modified,  
                renamed or removed from disk.  
                In MEL, the function should have the following signature:  
              
                proc fileChanged(string $file)  
                Properties: create, edit
        filename (bool?): Returns the full path + filename of the script which was either loaded or saved.  
                If there isn't one returns an empty string.  
                Properties: query
        filterKeyPress (Queryable[Callable[..., Any]]?): Sets a script which will be called to handle key-press events.  
                The function should have the following signature:  
              
                proc int filterKeyPress(int $modifiers, string $key)  
              
                modifiers: a bit mask where Shift is bit 1, Ctrl is bit 3,  
                Alt is bit 4, and bit 5 is the 'Windows' key on Windows keyboards  
                and the Command key on Mac keyboards.  
              
                key: Specifies what key was pressed. The key is either a single  
                ascii character or one of the keyword strings for the special  
                keyboard characters. For example:  
                Up, Down, Right, Left,  
                Home, End, Page_Up, Page_Down, Insert  
                Return, Space  
                F1 to F12  
              
                The function should return 1 to indicate that they key event has been  
                handled, and 0 to indicate that it has not been handled.  
                Properties: create, query, edit
        fullPathName (bool?): Return the full path name of the widget, which includes all the parents.  
                Properties: query
        hasFocus (bool?): Whether this control is currently in focus.  
                Properties: query
        hasSelection (bool?): Whether this control currently has a selection or not.  
                Properties: query
        height (Queryable[int]?): The height of the control.  The control will attempt to  
                be this size if it is not overruled by parent layout conditions.  
                Properties: create, query, edit
        highlightColor (Queryable[Tuple[float, float, float]]?): The highlight color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                Properties: create, query, edit
        insertText (str?): Inserts the specified text into the position under the cursor,  
                replacing any currently selected text. The selection and cursor  
                position can be set using the select flag. Appends text to the  
                end of this field.  
                Properties: create, edit
        isObscured (bool?): Return whether the control can actually be seen by the user.  
                The control will be obscured if its state is invisible, if it is  
                blocked (entirely or partially) by some other control, if it or a  
                parent layout is unmanaged, or if the control's window is  
                invisible or iconified.  
                Properties: query
        load (bool?): Prompts the user for a script to load into this field.  The loaded filename becomes  
                associated with this executer field and saving will save directly to the file.  
                Properties: create, edit
        loadContents (str?): Loads the contents of the specified filename into this field.  The path and extension for this filename  
                is provided internally.  This command is only intended for loading the contents of this executer field from a previous  
                instance of this executer field.  
                Properties: create, edit
        loadFile (str?): If the provided string is a fully specified file path, then attempts to load the  
                file contents into this field.  If the string is empty or not valid then prompts  
                the user for a script to load into this field.  In both cases the filename becomes  
                associated with this executer field and saving will save directly to the file.  
                Properties: create, edit
        manage (bool?): Manage state of the control.  An unmanaged control is  
                not visible, nor does it take up any screen real estate.  All  
                controls are created managed by default.  
                Properties: create, query, edit
        modificationChangedCommand (Callable[..., Any]?): Sets a script which will be called whenever the content of this field changes in  
                a way that affects the modification state.  
                In MEL, the function should have the following signature:  
              
                proc modificationChanged(int $m)  
              
                If $m is true, the field has been modified; otherwise it is false.  
                Properties: create, edit
        modified (bool?): Sets or returns whether the field has been modified.  
                Properties: query, edit
        noBackground (bool?): Clear/reset the control's background.  
                Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.  
                Properties: create, edit
        numberOfLines (Queryable[int]?): Returns the total number of lines in the document.  
                Properties: query
        numberOfPopupMenus (bool?): Return the number of popup menus attached to this control.  
                Properties: query
        objectPathCompletion (bool?): Enable/disable path completion  
                Properties: create, query, edit
        parent (Queryable[str]?): The parent layout for this control.  
                Properties: create, query
        pasteSelection (bool?): Pastes text into this field at the current caret position.  
                Properties: create, edit
        popupMenuArray (bool?): Return the names of all the popup menus attached to this  
                control.  
                Properties: query
        preventOverride (bool?): If true, this flag prevents overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create, query, edit
        redo (bool?): Redo the last operation.  
                Properties: create, edit
        removeStoredContents (str?): Removes the stored contents of this field with the specified filename.  The path and extension for the file is  
                provided internally.  This command is only intended for removing previously stored contents of this executer field.  
                Properties: create, edit
        replaceAll (Tuple[str, str]?): Replaces all instances of the first string in the field text with the  
                second string.  The case sensitivity of this operation is set with the  
                -searchMatchCase flag.  
                Properties: create, edit
        saveFile (str?): Saves the entire script contents of this field directly to the specified file path.  
                Properties: create, edit
        saveSelection (str?): Prompts to save the current selection to a file.  The default filename prompt will be prepended with the given string.  
                Properties: create, edit
        saveSelectionToShelf (bool?): Prompts to save the current selection to an item in the shelf.  
                Properties: create, edit
        searchAndSelect (bool?): Searches for (and selects) the specified search string using the  
                specified search options.  
                Properties: query
        searchDown (bool?): Specifies whether to search from the cursor down, or up.  
                Properties: create, query, edit
        searchMatchCase (bool?): Specifies whether the search is to be case sensitive or not.  
                Properties: create, query, edit
        searchString (Queryable[str]?): Specifies the string to search for.  
                Properties: create, query, edit
        searchWraps (bool?): Specifies whether the search should wrap around.  
                Properties: create, query, edit
        select (Tuple[int, int]?): Selects text within a specified range.  
                Properties: create, edit
        selectAll (bool?): Selects all text.  
                Properties: create, edit
        selectedText (bool?): The text in the current selection range.  
                Properties: query
        showLineNumbers (bool?): Shows/hides the line numbes column.  
                Properties: create, query, edit
        showTabsAndSpaces (bool?): Visually show tab and space indicators. (default off)  
                Properties: create, query, edit
        showTooltipHelp (bool?): Enable/disable tooltips in the command execution window  
                Properties: create, query, edit
        source (bool?): Prompts the user for a script to source (execute without loading).  
                Properties: create, edit
        sourceType (Queryable[str]?): Sets the source type for this command executer field.  
                Valid values are "mel" (enabled by default)  
                and "python".  
                Properties: create, query
        spacesPerTab (Queryable[int]?): Specifies the number of spaces equivalent to one tab stop. (default 4)  
                Properties: create, query, edit
        statusBarMessage (str?): Extra string to display in the status bar when the mouse is over the control.  
                Properties: create, edit
        storeContents (str?): If the provided string is a fully specified file path, then attempts to store the contents of this field  
                to that path. Otherwise, uses the provided string as a filename only and uses an internally generated  
                path and extension for the file, as used by the -loadContents and -removeStoredContents flags.  
                In both cases, a new unique filename will be generated if the specified name exists.  
                Returns the filename of the file saved upon completion, and an empty string otherwise.  
                Properties: create, edit
        tabsForIndent (bool?): Specifies whether tab characters should be inserted when indenting. (default on)  
                Properties: create, query, edit
        text (Queryable[str]?): Replaces the field text with the given string.  
                Properties: create, query, edit
        textLength (bool?): The number of characters in this text field.  
                Properties: query
        undo (bool?): Undo the last operation.  
                Properties: create, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        visible (bool?): The visible state of the control.  A control is created  
                visible by default.  Note that a control's actual appearance is  
                also dependent on the visible state of its parent layout(s).  
                Properties: create, query, edit
        visibleChangeCommand (Queryable[Callable[..., Any]]?): Command that gets executed when visible state of the control changes.  
                Properties: create, query, edit
        width (Queryable[int]?): The width of the control.  The control will attempt to  
                be this size if it is not overruled by parent layout conditions.  
                Properties: create, query, edit

    Returns:
        str: The name of the executer control

    Example:
    """

