from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def fileDialog2(*, buttonBoxOrientation: int = ..., cancelCaption: str = ..., caption: str = ..., dialogStyle: int = ..., fileFilter: str = ..., fileMode: int = ..., fileTypeChanged: Callable[..., Any] = ..., hideNameEdit: bool = ..., okCaption: str = ..., optionsUICancel: Callable[..., Any] = ..., optionsUICommit: Callable[..., Any] = ..., optionsUICommit2: Callable[..., Any] = ..., optionsUICreate: Callable[..., Any] = ..., optionsUIInit: Callable[..., Any] = ..., optionsUITitle: str = ..., returnFilter: bool = ..., selectFileFilter: str = ..., selectionChanged: Callable[..., Any] = ..., setProjectBtnEnabled: bool = ..., startingDirectory: str = ...) -> str:
    """This command provides a dialog that allows users to select files or directories.
    Args:
        buttonBoxOrientation (int?): 1 Vertical button box layout. Cancel button is below the accept button.   
                2 Horizontal button box layout. Cancel button is to the right of the accept button.  
                Properties: create
        cancelCaption (str?): If the dialogStyle flag is set to 2 then this provides a caption for the  
                Cancel button within the dialog.  
                Properties: create
        caption (str?): Provide a title for the dialog.  
                Properties: create
        dialogStyle (int?): 1 On Windows or Mac OS X will use a native style file dialog.  
                2 Use a custom file dialog with a style that is consistent across platforms.  
                Properties: create
        fileFilter (str?): Provide a list of file type filters to the dialog.  Multiple filters should be  
                separated by double semi-colons.  See the examples section.  
                Properties: create
        fileMode (int?): Indicate what the dialog is to return.  
              
                0 Any file, whether it exists or not.  
                1 A single existing file.  
                2 The name of a directory.  Both directories and files are displayed in the dialog.  
                3 The name of a directory.  Only directories are displayed in the dialog.  
                4 The names of one or more existing files.  
                Properties: create
        fileTypeChanged (Callable[..., Any]?): MEL only.  The string is interpreted as a MEL callback, to be called  
                when the user-selected file type changes.  The callback is of the form:  
              
                global proc MyCustomFileTypeChanged(string $parent, string $newType)  
              
                The parent argument is the parent layout into which controls have been  
                added using the optionsUICreate flag.  The newType argument is the new  
                file type.  
                Properties: create
        hideNameEdit (bool?): Hide name editing input field.  
                Properties: create
        okCaption (str?): If the dialogStyle flag is set to 2 then this provides a caption for the  
                OK, or Accept, button within the dialog.  
                Properties: create
        optionsUICancel (Callable[..., Any]?): MEL only.  The string is interpreted as a MEL callback, to be called  
                when the dialog is cancelled (with Cancel button or close button to close window).  
                The callback is of the form:  
              
                global proc MyCustomOptionsUICancel()  
                Properties: create
        optionsUICommit (Callable[..., Any]?): MEL only.  The string is interpreted as a MEL callback, to be called  
                when the dialog is successfully dismissed.  It will not be called if  
                the user cancels the dialog, or closes the window using window title  
                bar controls or other window system means.  The callback is of the form:  
              
                global proc MyCustomOptionsUICommit(string $parent)  
              
                The parent argument is the parent layout into which controls have been  
                added using the optionsUICreate flag.  
                Properties: create
        optionsUICommit2 (Callable[..., Any]?): MEL only.  As optionsUICommit, the given string is interpreted as a MEL  
                callback, to be called when the dialog is successfully dismissed. The  
                difference is that this callback takes one additional argument which is  
                the file name selected by the user before the dialog validation.  
                It will not be called if the user cancels the dialog, or closes the window using  
                window title bar controls or other window system means.  The callback is of the form:  
              
                global proc MyCustomOptionsUICommit(string $parent, string $selectedFile)  
              
                The parent argument is the parent layout into which controls have been  
                added using the optionsUICreate flag.  
                Properties: create
        optionsUICreate (Callable[..., Any]?): MEL only.  The string is interpreted as a MEL callback, to be called  
                on creation of the file dialog.  The callback is of the form:  
              
                global proc MyCustomOptionsUISetup(string $parent)  
              
                The parent argument is the parent layout into which controls can be  
                added.  This parent is the right-hand pane of the file dialog.  
                Properties: create
        optionsUIInit (Callable[..., Any]?): MEL only.  The string is interpreted as a MEL callback, to be called  
                just after file dialog creation, to initialize controls.  The callback is of  
                the form:  
              
                global proc MyCustomOptionsUIInitValues(string $parent, string $filterType)  
              
                The parent argument is the parent layout into which controls have been  
                added using the optionsUICreate flag.  The filterType argument is the  
                initial file filter.  
                Properties: create
        optionsUITitle (str?): MEL only. If optionsUICreate is set, user can set a custom title  
                to their option window using this flag. If no title is desired, an  
                empty string i.e. "" can be used.  
                Properties: create
        returnFilter (bool?): If true, the selected filter will be returned as the last item in the string array along  
                with the selected files.  
                Properties: create
        selectFileFilter (str?): Specify the initial file filter to select.  Specify just the begining text and not the full wildcard spec.  
                Properties: create
        selectionChanged (Callable[..., Any]?): MEL only.  The string is interpreted as a MEL callback, to be called  
                when the user changes the file selection in the file dialog.  The  
                callback is of the form:  
              
                global proc MyCustomSelectionChanged(string $parent, string $selection)  
              
                The parent argument is the parent layout into which controls have been  
                added using the optionsUICreate flag.  The selection argument is the  
                full path to the newly-selected file.  
                Properties: create
        setProjectBtnEnabled (bool?): Define whether the project button should be enabled  
                Properties: create
        startingDirectory (str?): Provide the starting directory for the dialog.  
                Properties: create

    Returns:
        str: array

    Example:
    """

