from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dynPaintEditor(*args: Any, edit: bool = ..., query: bool = ..., activeOnly: bool = ..., autoSave: bool = ..., camera: Queryable[str] = ..., canvasMode: bool = ..., canvasUndo: bool = ..., changeCommand: Queryable[Tuple[str, str, str, str]] = ..., clear: Tuple[float, float, float] = ..., control: bool = ..., currentCanvasSize: bool = ..., defineTemplate: str = ..., displayAppearance: Queryable[str] = ..., displayFog: bool = ..., displayImage: Queryable[int] = ..., displayLights: Queryable[str] = ..., displayStyle: Queryable[str] = ..., displayTextures: bool = ..., docTag: Queryable[str] = ..., doubleBuffer: bool = ..., drawAxis: bool = ..., drawContext: bool = ..., exists: bool = ..., fastUpdate: int = ..., fileName: Queryable[str] = ..., filter: Queryable[str] = ..., forceMainConnection: Queryable[str] = ..., highlightConnection: Queryable[str] = ..., iconGrab: bool = ..., loadImage: str = ..., lockMainConnection: bool = ..., mainListConnection: Queryable[str] = ..., menu: str = ..., nbImages: bool = ..., newImage: Queryable[Tuple[int, int, float, float, float]] = ..., paintAll: float = ..., panel: Queryable[str] = ..., parent: Queryable[str] = ..., redrawLast: bool = ..., refresh: bool = ..., refreshMode: Queryable[int] = ..., removeAllImages: bool = ..., removeImage: bool = ..., rollImage: Tuple[float, float] = ..., saveAlpha: bool = ..., saveBumpmap: Queryable[str] = ..., saveImage: bool = ..., scaleBlue: Queryable[float] = ..., scaleGreen: Queryable[float] = ..., scaleRed: Queryable[float] = ..., selectionConnection: Queryable[str] = ..., singleBuffer: bool = ..., snapShot: bool = ..., stateString: bool = ..., swap: int = ..., tileSize: int = ..., unParent: bool = ..., undoCache: bool = ..., unlockMainConnection: bool = ..., updateMainConnection: bool = ..., useTemplate: str = ..., wrap: Queryable[Tuple[bool, bool]] = ..., writeImage: str = ..., zoom: Queryable[float] = ...) -> Union[str, bool, Tuple[str, str, str, str], int, Tuple[int, int, float, float, float], float, Tuple[bool, bool]]:
    """Create a editor window that can be painted into
    Args:
        activeOnly (bool?): For Scene mode, this determines if only the active strokes will  
                be refreshed.  
                Properties: query, edit
        autoSave (bool?): For Canvas mode, this determines if the buffer will be saved  
                to a disk file after every stroke. Good for painting textures and  
                viewing the results in shaded display in the model view.  
                Properties: query, edit
        camera (Queryable[str]?): Sets the name of the camera which the Paint Effects panel  
                looks through.  
                Properties: query, edit
        canvasMode (bool?): Sets the Paint Effects panel into Canvas mode if true.  
                Properties: query, edit
        canvasUndo (bool?): Does a fast undo in Canvas mode. This is a special undo because  
                we are not using any history when we paint in Canvas mode so we  
                provide a single level undo for the Canvas.  
                Properties: edit
        changeCommand (Queryable[Tuple[str, str, str, str]]?): Parameters:  
              
                First string: command  
                Second string: editorName  
                Third string: editorCmd  
                Fourth string: updateFunc  
              
              
                Call the command when something changes in the editor The command  
                should have this prototype :  
              
                command(string $editor, string $editorCmd, string $updateFunc, int $reason)  
              
                The possible reasons could be :  
              
                0. no particular reason  
                1. scale color  
                2. buffer (single/double)  
                3. axis   
                4. image displayed  
                5. image saved in memory  
                Properties: create, query, edit
        clear (Tuple[float, float, float]?): Clears the buffer (if in Canvas mode) to the floating point  
                values (R,G,B).  
                Properties: edit
        control (bool?): Query only. Returns the top level control for this editor.  
                Usually used for getting a parent to attach popup menus.  
                Caution: It is possible for an editor to exist without a  
                control. The query will return "NONE" if no control is present.  
                Properties: query
        currentCanvasSize (bool?): In Query mode, this returns the (X,Y) resolution of the  
                current canvas.  
                Properties: query
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        displayAppearance (Queryable[str]?): Sets the display appearance of the model panel.  Possible  
                values are "wireframe", "points", "boundingBox", "smoothShaded",  
                "flatShaded".  This flag may be used with the -interactive  
                and -default flags.  Note that only "wireframe", "points", and  
                "boundingBox" are valid for the interactive mode.  
                Properties: query, edit
        displayFog (bool?): For Scene mode, this determines if fog will be displayed in  
                the Paint Effects panel when refreshing the scene. If fog is on,  
                but this is off, fog will only be drawn on the strokes, not the  
                rest of the scene.  
                Properties: query, edit
        displayImage (Queryable[int]?): Set a particular image in the Editor Image Stack as the current Editor Image.  
                Images are added to the Editor Image Stack using the "si/saveImage" flag.  
                Properties: query, edit
        displayLights (Queryable[str]?): Sets the lighting for shaded mode.  Possible values are "selected",  
                "active", "all", "default".  
                Properties: query, edit
        displayStyle (Queryable[str]?): Set the mode to display the image. Valid values are:  
              
                "color" to display the basic RGB image  
                "mask" to display the mask channel  
                "lum" to display the luminance of the image  
                Properties: create, query, edit
        displayTextures (bool?): Turns on or off display of textures in shaded mode  
                Properties: query, edit
        docTag (Queryable[str]?): Attaches a tag to the editor.  
                Properties: create, query, edit
        doubleBuffer (bool?): Set the display in double buffer mode  
                Properties: create, query, edit
        drawAxis (bool?): Set or query whether the axis will be drawn.  
                Properties: create, query, edit
        drawContext (bool?): Returns the name of the context.  
                Properties: query
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        fastUpdate (int?): Obsolete - do not use
        fileName (Queryable[str]?): This sets the file to which the canvas will be saved.  
                Properties: query, edit
        filter (Queryable[str]?): Specifies the name of an itemFilter object to be used with this editor.  
                This filters the information coming onto the main list  
                of the editor.  
                Properties: create, query, edit
        forceMainConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will use as its source of content. The editor will only  
                display items contained in the selectionConnection object. This is  
                a variant of the -mainListConnection flag in that it will force a  
                change even when the connection is locked. This flag is used to  
                reduce the overhead when using the -unlockMainConnection  
                , -mainListConnection, -lockMainConnection flags in immediate  
                succession.  
                Properties: create, query, edit
        highlightConnection (Queryable[str]?): Specifies the name of a selectionConnection object that  
                the editor will synchronize with its highlight list. Not all  
                editors have a highlight list. For those that do, it is a secondary  
                selection list.  
                Properties: create, query, edit
        iconGrab (bool?): This puts the Paint Effects panel into Grab Icon mode where the  
                user is expected to drag out a section of the screen to be made into  
                an icon.  
                Properties: edit
        loadImage (str?): load an image from disk and set it as the current Editor Image  
                Properties: edit
        lockMainConnection (bool?): Locks the current list of objects within the mainConnection,  
                so that only those objects are displayed within the editor.  
                Further changes to the original mainConnection are ignored.  
                Properties: create, edit
        mainListConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will use as its source of content. The editor will  
                only display items contained in the selectionConnection object.  
                Properties: create, query, edit
        menu (str?): Sets the name of the script used to build a menu in the editor. The script  
                takes the editor name as an argument.  
                Properties: create
        nbImages (bool?): returns the number of images  
                Properties: query
        newImage (Queryable[Tuple[int, int, float, float, float]]?): Starts a new image in edit mode, setting the resolution to  
                the integer values (X,Y) and clearing the buffer to the floating point  
                values (R,G,B). In Query mode, this returns the (X,Y) resolution of the  
                current Image.  
                Properties: query, edit
        paintAll (float?): Redraws the buffer in current refresh mode.  
                Properties: edit
        panel (Queryable[str]?): Specifies the panel for this editor. By default if  
                an editor is created in the create callback of a scripted panel it  
                will belong to that panel. If an editor does not belong to a panel  
                it will be deleted when the window that it is in is deleted.  
                Properties: create, query
        parent (Queryable[str]?): Specifies the parent layout for this editor. This flag will only  
                have an effect if the editor is currently un-parented.  
                Properties: create, query, edit
        redrawLast (bool?): Redraws the last stroke again. Useful when it's brush has just  
                changed. This feature does a fast undo and redraws the stroke again.  
                Properties: edit
        refresh (bool?): requests a refresh of the current Editor Image.  
                Properties: edit
        refreshMode (Queryable[int]?): Sets the refresh mode to the specified value. 0. Do not draw  
                strokes on refresh, 1. Redraw strokes in wireframe mode, 2. Redraw strokes in final rendered mode.  
                Properties: query, edit
        removeAllImages (bool?): remove all the Editor Images from the Editor Image Stack  
                Properties: edit
        removeImage (bool?): remove the current Editor Image from the Editor Image Stack  
                Properties: edit
        rollImage (Tuple[float, float]?): In Canvas mode, this rolls the image by the floating point  
                values (X,Y). X and Y are between 0 (no roll) and 1 (full roll). A  
                value of .5 rolls the image 50% (ie. the border moves to the center of the screen.  
                Properties: edit
        saveAlpha (bool?): For Canvas mode, this determines if the alpha will be saved when  
                storing the canvas to a disk file.  
                Properties: query, edit
        saveBumpmap (Queryable[str]?): Saves the current buffer as a bump map to the specified file.  
                Properties: query, edit
        saveImage (bool?): save the current Editor Image to memory. Saved Editor Images are  
                stored in an Editor Image Stack. The most recently saved image is stored in  
                position 0, the second most recently saved image in position 1,  
                and so on... To set the current Editor Image to a previously saved  
                image use the "di/displayImage" flag.  
                Properties: edit
        scaleBlue (Queryable[float]?): Define the scaling factor for the blue component  
                in the View. The default value is 1 and can be  
                between -1000 to +1000  
                Properties: create, query, edit
        scaleGreen (Queryable[float]?): Define the scaling factor for the green component  
                in the View. The default value is 1 and can be  
                between -1000 to +1000  
                Properties: create, query, edit
        scaleRed (Queryable[float]?): Define the scaling factor for the red component  
                in the View. The default value is 1 and can be  
                between -1000 to +1000  
                Properties: create, query, edit
        selectionConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will synchronize with its own selection list. As the user  
                selects things in this editor, they will be selected in the  
                selectionConnection object. If the object undergoes changes, the  
                editor updates to show the changes.  
                Properties: create, query, edit
        singleBuffer (bool?): Set the display in single buffer mode  
                Properties: create, query, edit
        snapShot (bool?): Takes a snapshot of the current camera view.  
                Properties: edit
        stateString (bool?): Query only flag. Returns the MEL command that will create an  
                editor to match the current editor state. The returned command string  
                uses the string variable $editorName in place of a specific name.  
                Properties: query
        swap (int?): Obsolete - do not use
        tileSize (int?): Sets the size of the tile for the hardware texture redraw of the display buffer.  
                Properties: edit
        unParent (bool?): Specifies that the editor should be removed from its layout.  
                This cannot be used in query mode.  
                Properties: create, edit
        undoCache (bool?): By default the last image is cached for undo. If this is set false, then  
                undoing will be disabled in canvas mode and undo in scene mode will force a full  
                refresh. Less memory will be used if this is set false before the first clear or  
                refresh of the current scene.  
                Properties: edit
        unlockMainConnection (bool?): Unlocks the mainConnection, effectively restoring the original  
                mainConnection (if it is still available), and dynamic updates.  
                Properties: create, edit
        updateMainConnection (bool?): Causes a locked mainConnection to be updated from the orginal  
                mainConnection, but preserves the lock state.  
                Properties: create, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        wrap (Queryable[Tuple[bool, bool]]?): For Canvas mode, should the buffer wrap in U, and V  
                (respectively) when painting.  
                Properties: query, edit
        writeImage (str?): write the current Editor Image to disk  
                Properties: edit
        zoom (Queryable[float]?): Zooms the Canvas image by the specified value.  
                Properties: query, edit

    Returns:
        str: Editor name

    Example:
    """

