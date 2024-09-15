from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def renderWindowEditor(*args: Any, edit: bool = ..., query: bool = ..., autoResize: bool = ..., blendMode: Queryable[int] = ..., caption: Queryable[str] = ..., changeCommand: Queryable[Tuple[str, str, str, str]] = ..., clear: Queryable[Tuple[int, int, float, float, float]] = ..., cmEnabled: bool = ..., colorManage: bool = ..., compDisplay: Queryable[int] = ..., compImageFile: Queryable[str] = ..., control: bool = ..., currentCamera: Queryable[str] = ..., currentCameraRig: Queryable[str] = ..., defineTemplate: str = ..., displayImage: Queryable[int] = ..., displayImageViewCount: Queryable[int] = ..., displayStyle: Queryable[str] = ..., docTag: Queryable[str] = ..., doubleBuffer: bool = ..., drawAxis: bool = ..., editorName: bool = ..., exists: bool = ..., exposure: Queryable[float] = ..., filter: Queryable[str] = ..., forceMainConnection: Queryable[str] = ..., frameImage: bool = ..., frameRegion: bool = ..., gamma: Queryable[float] = ..., highlightConnection: Queryable[str] = ..., loadImage: str = ..., lockMainConnection: bool = ..., mainListConnection: Queryable[str] = ..., marquee: Queryable[Tuple[float, float, float, float]] = ..., nbImages: bool = ..., nextViewImage: bool = ..., outputColorManage: bool = ..., panel: Queryable[str] = ..., parent: Queryable[str] = ..., pcaption: Queryable[str] = ..., realSize: bool = ..., refresh: bool = ..., removeAllImages: bool = ..., removeImage: bool = ..., resetRegion: bool = ..., resetViewImage: bool = ..., saveImage: bool = ..., scaleBlue: Queryable[float] = ..., scaleGreen: Queryable[float] = ..., scaleRed: Queryable[float] = ..., selectionConnection: Queryable[str] = ..., showRegion: Queryable[Tuple[int, int]] = ..., singleBuffer: bool = ..., snapshot: Queryable[Tuple[str, int, int]] = ..., snapshotMode: bool = ..., stateString: bool = ..., stereo: Queryable[int] = ..., stereoImageOrientation: Queryable[Tuple[str, str]] = ..., stereoMode: Queryable[str] = ..., toggle: bool = ..., unParent: bool = ..., unlockMainConnection: bool = ..., updateMainConnection: bool = ..., useTemplate: str = ..., viewImageCount: Queryable[int] = ..., viewTransformName: Queryable[str] = ..., writeImage: str = ...) -> Union[str, bool, int, Tuple[str, str, str, str], Tuple[int, int, float, float, float], float, Tuple[float, float, float, float], Tuple[int, int], Tuple[str, int, int], Tuple[str, str]]:
    """Create a editor window that can receive the result of the
    rendering process
    Args:
        autoResize (bool?): Lets the render view editor automatically resize the viewport or not.  
                Properties: create, query, edit
        blendMode (Queryable[int]?): Sets the blend mode for the render view.  
                New image sent to the render view will be blended  
                with the previous image in the render view,  
                and the composited image will appear.  
                Properties: create, query, edit
        caption (Queryable[str]?): Sets the caption which appears at the bottom of the render view.  
                Properties: create, query, edit
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
        clear (Queryable[Tuple[int, int, float, float, float]]?): Clear the image with the given color at the given resolution.  
                Arguments are respectively: width height red green blue.  
                Properties: create, query, edit
        cmEnabled (bool?): Turn on or off applying color management in the View.  If set, the color  
                management configuration set in the current view is used.  
                Properties: query, edit
        colorManage (bool?): When used with the writeImage flag, causes the written image to  
                be color-managed using the settings from the view color manager  
                attached to the view.  
                Properties: edit
        compDisplay (Queryable[int]?): 0. disable compositing.  
                1. displays the composited image immediately.  
                For example, when foreground layer tile is sent to the render  
                view window,  
                the composited tile is displayed in the render view window,  
                and the original foreground layer tile is not displayed.  
                2. display the un-composited image, and keep the  
                composited image for the future command.  
                For example, when foreground layer tile is sent to the  
                render view window,  
                the original foreground layer tile is not displayed,  
                and the composited tile is stored in a buffer.  
                3. show the current composited image.  
                If there is a composited image in the buffer, display it.  
                Properties: create, query, edit
        compImageFile (Queryable[str]?): Open the given image file  
                and blend with the buffer  
                as if the image was just rendered.  
                Properties: create, query, edit
        control (bool?): Query only. Returns the top level control for this editor.  
                Usually used for getting a parent to attach popup menus.  
                Caution: It is possible for an editor to exist without a  
                control. The query will return "NONE" if no control is present.  
                Properties: query
        currentCamera (Queryable[str]?): Get or set the current camera. (used when redoing last render)  
                Properties: create, query, edit
        currentCameraRig (Queryable[str]?): Get or set the current camera rig name. If a camera rig is  
                specified, it will be used when redoing the last render as  
                opposed to the currentCamera value, as the currentCamera  
                value will hold the child camera last used for rendering  
                the camera rig.  
                Properties: create, query, edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        displayImage (Queryable[int]?): Set a particular image in the Editor Image Stack as the current Editor Image.  
                Images are added to the Editor Image Stack using the "si/saveImage" flag.  
                Properties: query, edit
        displayImageViewCount (Queryable[int]?): Query the number of views stored for a given image in the Editor Image Stack. This is not the same  
                as querying using "viewImageCount" which returns the number of views for the current rendered image.  
                Properties: query
        displayStyle (Queryable[str]?): Set the mode to display the image. Valid values are:  
              
                "color" to display the basic RGB image  
                "mask" to display the mask channel  
                "lum" to display the luminance of the image  
                Properties: create, query, edit
        docTag (Queryable[str]?): Attaches a tag to the editor.  
                Properties: create, query, edit
        doubleBuffer (bool?): Set the display in double buffer mode  
                Properties: create, query, edit
        drawAxis (bool?): Set or query whether the axis will be drawn.  
                Properties: create, query, edit
        editorName (bool?): Returns the name of the editor, or an empty string if the editor has not been created yet.  
                Properties: query
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        exposure (Queryable[float]?): The exposure value used by the color management of the current view.  
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
        frameImage (bool?): Frames the image inside the window.  
                Properties: create, query, edit
        frameRegion (bool?): Frames the region inside the window.  
                Properties: create, query, edit
        gamma (Queryable[float]?): The gamma value used by the color management of the current view.  
                Properties: query, edit
        highlightConnection (Queryable[str]?): Specifies the name of a selectionConnection object that  
                the editor will synchronize with its highlight list. Not all  
                editors have a highlight list. For those that do, it is a secondary  
                selection list.  
                Properties: create, query, edit
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
        marquee (Queryable[Tuple[float, float, float, float]]?): The arguments define the four corners of a rectangle: top left bottom right.  
                The rectangle defines a marquee for the render computation.  
                Properties: create, query, edit
        nbImages (bool?): returns the number of images  
                Properties: query
        nextViewImage (bool?): The render editor has the capability to render multiple cameras within a  
                single view. This is different from image binning where an image is saved. Multiple image views  
                are useful for comparing two different camera renders side-by-side. The nextViewImage flag tells  
                the editor that it should prepare its internal image storage mechanism to store to the next  
                view location.  
                Properties: create, edit
        outputColorManage (bool?): When used with the writeImage flag, causes the written image to  
                be color-managed using the outpute color space in the color preferences  
                attached to the view.  
                Properties: edit
        panel (Queryable[str]?): Specifies the panel for this editor. By default if  
                an editor is created in the create callback of a scripted panel it  
                will belong to that panel. If an editor does not belong to a panel  
                it will be deleted when the window that it is in is deleted.  
                Properties: create, query
        parent (Queryable[str]?): Specifies the parent layout for this editor. This flag will only  
                have an effect if the editor is currently un-parented.  
                Properties: create, query, edit
        pcaption (Queryable[str]?): Get or set the permanent caption which appears under  
                the image that is currently showing in the render editor.  
                Properties: create, query, edit
        realSize (bool?): Display the image with a one to one pixel match.  
                Properties: create, query, edit
        refresh (bool?): requests a refresh of the current Editor Image.  
                Properties: edit
        removeAllImages (bool?): remove all the Editor Images from the Editor Image Stack  
                Properties: edit
        removeImage (bool?): remove the current Editor Image from the Editor Image Stack  
                Properties: edit
        resetRegion (bool?): Forces a reset of any marquee/region.  
                Properties: create, query, edit
        resetViewImage (bool?): The render editor has the capability to render multiple cameras within a  
                single view. This is different from image binning where an image is saved. Multiple image views  
                are useful for comparing two different camera renders side-by-side. The resetViewImage flag tells  
                the editor that it should reset its internal image storage mechanism to the first image.  
                This would happen at the very start of a render view render.  
                Properties: create, edit
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
        showRegion (Queryable[Tuple[int, int]]?): Shows the current region at the given resolution. The two parameters  
                define the width and height.  
                Properties: create, query, edit
        singleBuffer (bool?): Set the display in single buffer mode  
                Properties: create, query, edit
        snapshot (Queryable[Tuple[str, int, int]]?): Makes a copy of the camera of the model editor at the  
                given size.  
                First argument is the editor name, second is the width, third is the height.  
                Properties: create, query, edit
        snapshotMode (bool?): Get or set the window's snapshot mode.  
                Properties: create, query, edit
        stateString (bool?): Query only flag. Returns the MEL command that will create an  
                editor to match the current editor state. The returned command string  
                uses the string variable $editorName in place of a specific name.  
                Properties: query
        stereo (Queryable[int]?): Puts the editor into stereo image mode.  The effective resolution of the  
                output image is twice the size of the horizontal size. The orientation of the  
                images can be set using the stereoOrientation flag.  
                Properties: create, query, edit
        stereoImageOrientation (Queryable[Tuple[str, str]]?): Specifies the orientation of stereo camera renders.  The first argument specifies the orientation  
                value for the firstleft image and the second argument specifies the orientation value for the right  
                image. The orientation values are 'normal', the image appears as seen throught he camera, or  
                'mirrored', the image is mirrored horizontally.  
                Properties: create, query, edit
        stereoMode (Queryable[str]?): Specifies how the image is displayed in the view.  By default the stereo is rendered with a  
                side by side image.  The rendered image is a single image that is twice the size of a normal image,  
                'both'. Users can also choose to display as 'redcyan', 'redcyanlum', 'leftonly', 'rightonly', or 'stereo'.  
              
                both - displays both the left and right  
                redcyan - displays the images as a red/cyan pair.  
                redcyanlum - displays the luminance of the images as a red/cyan pair.  
                leftonly - displays the left side only  
                rightonly - displays the right side only  
                stereo - mode that supports Crystal Eyes(tm) or Zscreen (tm) renders  
                Properties: create, query, edit
        toggle (bool?): Turns the ground plane display on/off.  
                Properties: create, query, edit
        unParent (bool?): Specifies that the editor should be removed from its layout.  
                This cannot be used in query mode.  
                Properties: create, edit
        unlockMainConnection (bool?): Unlocks the mainConnection, effectively restoring the original  
                mainConnection (if it is still available), and dynamic updates.  
                Properties: create, edit
        updateMainConnection (bool?): Causes a locked mainConnection to be updated from the orginal  
                mainConnection, but preserves the lock state.  
                Properties: create, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        viewImageCount (Queryable[int]?): The render editor has the capability to render multiple cameras within a  
                single view. This is different from image binning where an image is saved. Multiple image views  
                are useful for comparing two different camera renders side-by-side. The viewImageCount flag tells  
                the editor that it should prepare its internal image storage mechanism for a given number of views.  
                Properties: create, query, edit
        viewTransformName (Queryable[str]?): Sets/gets the view transform to be applied if color management is enabled in the  
                current view.  
                Properties: query, edit
        writeImage (str?): write the current Editor Image to disk  
                Properties: edit

    Returns:
        str: The name of the editor

    Example:
    """

