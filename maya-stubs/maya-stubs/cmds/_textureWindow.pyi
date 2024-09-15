from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def textureWindow(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., activeSelectionOnTop: bool = ..., axesColor: Queryable[Tuple[float, float, float]] = ..., backFacingColor: Queryable[Tuple[float, float, float, float]] = ..., capture: str = ..., captureSequenceNumber: int = ..., changeCommand: Queryable[Tuple[str, str, str, str]] = ..., checkerColor1: Queryable[Tuple[float, float, float]] = ..., checkerColor2: Queryable[Tuple[float, float, float]] = ..., checkerColorMode: Queryable[int] = ..., checkerDensity: Queryable[int] = ..., checkerDrawTileLabels: bool = ..., checkerGradient1: Queryable[Tuple[float, float, float]] = ..., checkerGradient2: Queryable[Tuple[float, float, float]] = ..., checkerGradientOverlay: bool = ..., checkerTileLabelColor: Queryable[Tuple[float, float, float]] = ..., clearImage: bool = ..., cmEnabled: bool = ..., control: bool = ..., defineTemplate: str = ..., displayAxes: bool = ..., displayCheckered: bool = ..., displayDistortion: bool = ..., displayDivisionLines: bool = ..., displayGridLines: bool = ..., displayImage: Queryable[int] = ..., displayIsolateSelectHUD: bool = ..., displayLabels: bool = ..., displayOverlappingUVCountHUD: bool = ..., displayPreselection: bool = ..., displayReversedUVCountHUD: bool = ..., displaySolidMap: bool = ..., displayStyle: Queryable[str] = ..., displayTextureBorder: bool = ..., displayUVPositionHUD: bool = ..., displayUVShellCountHUD: bool = ..., displayUVStatisticsHUD: bool = ..., displayUsedPercentageHUD: bool = ..., distortionAlpha: Queryable[float] = ..., distortionPerObject: bool = ..., divisions: Queryable[int] = ..., docTag: Queryable[str] = ..., doubleBuffer: bool = ..., drawAxis: bool = ..., drawSubregions: bool = ..., exists: bool = ..., exposure: Queryable[float] = ..., filter: Queryable[str] = ..., forceMainConnection: Queryable[str] = ..., forceRebake: bool = ..., frameAll: bool = ..., frameSelected: bool = ..., frontFacingColor: Queryable[Tuple[float, float, float, float]] = ..., gamma: Queryable[float] = ..., gridLinesColor: Queryable[Tuple[float, float, float]] = ..., gridNumbersColor: Queryable[Tuple[float, float, float]] = ..., highlightConnection: Queryable[str] = ..., imageBaseColor: Queryable[Tuple[float, float, float]] = ..., imageDim: bool = ..., imageDisplay: bool = ..., imageNames: bool = ..., imageNumber: Queryable[int] = ..., imagePixelSnap: bool = ..., imageRatio: bool = ..., imageRatioValue: Queryable[float] = ..., imageSize: bool = ..., imageTileRange: Queryable[Tuple[float, float, float, float]] = ..., imageUnfiltered: bool = ..., internalFaces: bool = ..., labelPosition: Queryable[str] = ..., loadImage: str = ..., lockMainConnection: bool = ..., mainListConnection: Queryable[str] = ..., maxResolution: Queryable[int] = ..., multiColorAlpha: Queryable[float] = ..., nbImages: bool = ..., nextView: bool = ..., numUvSets: bool = ..., numberOfImages: Queryable[int] = ..., numberOfTextures: Queryable[int] = ..., panel: Queryable[str] = ..., parent: Queryable[str] = ..., previousView: bool = ..., realSize: bool = ..., refresh: bool = ..., relatedFaces: bool = ..., removeAllImages: bool = ..., removeImage: bool = ..., rendererString: Queryable[str] = ..., reset: bool = ..., saveImage: bool = ..., scaleBlue: Queryable[float] = ..., scaleGreen: Queryable[float] = ..., scaleRed: Queryable[float] = ..., selectInternalFaces: bool = ..., selectRelatedFaces: bool = ..., selectionConnection: Queryable[str] = ..., setUvSet: int = ..., singleBuffer: bool = ..., size: Queryable[float] = ..., solidMap3dView: bool = ..., solidMapColorSeed: Queryable[int] = ..., solidMapPerShell: bool = ..., spacing: float = ..., stateString: bool = ..., style: Queryable[int] = ..., subdivisionLinesColor: Queryable[Tuple[float, float, float]] = ..., textureBorder3dView: bool = ..., textureBorderColor: Queryable[Tuple[float, float, float]] = ..., textureBorderWidth: Queryable[int] = ..., textureNames: bool = ..., textureNumber: Queryable[int] = ..., tileLabels: bool = ..., tileLinesColor: Queryable[Tuple[float, float, float]] = ..., toggle: bool = ..., toggleExposure: bool = ..., toggleGamma: bool = ..., unParent: bool = ..., unlockMainConnection: bool = ..., updateMainConnection: bool = ..., useFaceGroup: bool = ..., useTemplate: str = ..., usedPercentageHUDRange: Queryable[Tuple[float, float, float, float]] = ..., uvSets: bool = ..., viewPortImage: bool = ..., viewTransformName: Queryable[str] = ..., wireframeComponentColor: Queryable[Tuple[float, float, float, float]] = ..., wireframeObjectColor: Queryable[Tuple[float, float, float, float]] = ..., writeImage: str = ...) -> Union[str, bool, Tuple[float, float, float], Tuple[float, float, float, float], Tuple[str, str, str, str], int, float]:
    """This command is used to create a UV Editor and to query or edit
    the texture editor settings.The UV Editor displays texture mapped polygon objects in 2D
    texture space. Only active objects are visible in this window.The UV Editor has the ability to display two types of images. The
    Texture Image is a visualisation of the current texture and associated
    placement parameters. The Editor Image is a user specified image loaded
    from disk.A UV Editor can be invoked by selecting the "Window -> UV
    Texture Editor..." menu item from the main maya menu listing that
    appears at the top of the maya window. It can also be invoked by
    selecting the "Panel -> UV Editor" item under the "Panels"
    menu item that appears at the top right hand corner of the view.As a UV Editor typically exists at start-up time, and as only
    one of these can exist at any given time, this command is normally
    used to query and edit the editor settings.
    Args:
        activeSelectionOnTop (bool?): Display the solid map / distortion of active selection on top of others.  
                Properties: create, query, edit
        axesColor (Queryable[Tuple[float, float, float]]?): The color of axes, default is 0.0 0.0 1.0  
                Properties: create, query, edit
        backFacingColor (Queryable[Tuple[float, float, float, float]]?): Sets or queries the RGBA back facing color.  
                Properties: create, query, edit
        capture (str?): Perform an one-time capture of the viewport to the named image file on disk.  
                Properties: edit
        captureSequenceNumber (int?): When a number greater or equal to 0 is specified each  
                subsequent refresh will save an image file to disk if the  
                capture flag has been enabled.  
              
                The naming of the file is:  
              
                {root name}.#.{extension}  
              
                if the name {root name}.{extension} is used for the capture flag argument.  
                The value of # starts at the number specified to for this argument and  
                increments for each subsequent refresh.  
              
                Sequence capture can be disabled by specifying a number less  
                than 0 or an empty file name for the capture flag.  
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
        checkerColor1 (Queryable[Tuple[float, float, float]]?): Sets the first color of the checker and identification pattern, when color mode is 2. colors.  
                Properties: create, query, edit
        checkerColor2 (Queryable[Tuple[float, float, float]]?): Sets the second color of the checker and identification pattern, when color mode is 2. colors.  
                Properties: create, query, edit
        checkerColorMode (Queryable[int]?): Sets the color mode of the checker and identification pattern.  
                0. multi-colors;  
                1. 2. colors;  
                Properties: create, query, edit
        checkerDensity (Queryable[int]?): Sets the density of the checker and identification pattern.  
                Properties: create, query, edit
        checkerDrawTileLabels (bool?): Toggles the checker tile label display.  
                Properties: create, query, edit
        checkerGradient1 (Queryable[Tuple[float, float, float]]?): Sets the first gradient of the checker and identification pattern, when color mode is 2. colors.  
                Properties: create, query, edit
        checkerGradient2 (Queryable[Tuple[float, float, float]]?): Sets the second gradient of the checker and identification pattern, when color mode is 2. colors.  
                Properties: create, query, edit
        checkerGradientOverlay (bool?): Toggle application of the gradient.  
                Properties: create, query, edit
        checkerTileLabelColor (Queryable[Tuple[float, float, float]]?): Sets the checker tile label color.  
                Properties: create, query, edit
        clearImage (bool?): Clears the current Editor Image.  
                Properties: edit
        cmEnabled (bool?): Turn on or off applying color management in the editor.  If set, the color  
                management configuration set in the current editor is used.  
                Properties: query, edit
        control (bool?): Query only. Returns the top level control for this editor.  
                Usually used for getting a parent to attach popup menus.  
                Caution: It is possible for an editor to exist without a  
                control. The query will return "NONE" if no control is present.  
                Properties: query
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        displayAxes (bool?): Specify true to display the grid axes.  
                Properties: query, edit
        displayCheckered (bool?): Display a unique checker and identification pattern for each UV tiles.  
                Properties: create, query, edit
        displayDistortion (bool?): Display the layout in shaded colors to indentify areas with stretched/squashed UVs  
                Properties: create, query, edit
        displayDivisionLines (bool?): Specify true to display the subdivision lines between  
                grid lines.  
                Properties: query, edit
        displayGridLines (bool?): Specify true to display the grid lines.  
                Properties: query, edit
        displayImage (Queryable[int]?): Set a particular image in the Editor Image Stack as the current Editor Image.  
                Images are added to the Editor Image Stack using the "si/saveImage" flag.  
                Properties: query, edit
        displayIsolateSelectHUD (bool?): Show heads-up display of isolate selection  
                Properties: create, query, edit
        displayLabels (bool?): Specify true to display the grid line numeric labels.  
                Properties: query, edit
        displayOverlappingUVCountHUD (bool?): Show heads-up display of overlapping UV count, as a part UV Statistics HUD  
                Properties: create, query, edit
        displayPreselection (bool?): Toggles the pre-selection display.  
                Properties: create, query, edit
        displayReversedUVCountHUD (bool?): Show heads-up display of UV Shells, as a part UV Statistics HUD  
                Properties: create, query, edit
        displaySolidMap (bool?): Display a solid overlay for the active texture map.  
                Properties: create, query, edit
        displayStyle (Queryable[str]?): Set the mode to display the image. Valid values are:  
              
                "color" to display the basic RGB image  
                "mask" to display the mask channel  
                "lum" to display the luminance of the image  
                Properties: create, query, edit
        displayTextureBorder (bool?): Toggles the texture borders display.  
                Properties: create, query, edit
        displayUVPositionHUD (bool?): Show heads-up display of UV positions  
                Properties: create, query, edit
        displayUVShellCountHUD (bool?): Show heads-up display of UV Shell count, as a part UV Statistics HUD  
                Properties: create, query, edit
        displayUVStatisticsHUD (bool?): Show heads-up display of UV Statistics  
                Properties: create, query, edit
        displayUsedPercentageHUD (bool?): Show heads-up display of used UV space percentage, as a part UV Statistics HUD  
                Properties: create, query, edit
        distortionAlpha (Queryable[float]?): Set or query the distortion display alpha.  
                Properties: create, query, edit
        distortionPerObject (bool?): Toggles the per-object distortion display.  
                Properties: create, query, edit
        divisions (Queryable[int]?): Sets the number of subdivisions between main grid lines.  
                Properties: create, query, edit
        docTag (Queryable[str]?): Attaches a tag to the editor.  
                Properties: create, query, edit
        doubleBuffer (bool?): Set the display in double buffer mode  
                Properties: create, query, edit
        drawAxis (bool?): Set or query whether the axis will be drawn.  
                Properties: create, query, edit
        drawSubregions (bool?): Toggles the subregion display.  
                Properties: create, query, edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        exposure (Queryable[float]?): The exposure value used by the color management of the current editor.  
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
        forceRebake (bool?): Forces the current cache texture to refresh.  
                Properties: create, edit
        frameAll (bool?): This will zoom on the whole scene.  
                Properties: create
        frameSelected (bool?): This will zoom on the currently selected objects.  
                Properties: create
        frontFacingColor (Queryable[Tuple[float, float, float, float]]?): Sets or queries the RGBA front facing color.  
                Properties: create, query, edit
        gamma (Queryable[float]?): The gamma value used by the color management of the current editor.  
                Properties: query, edit
        gridLinesColor (Queryable[Tuple[float, float, float]]?): The color of grid lines, default is 0.325 0.325 0.325  
                Properties: create, query, edit
        gridNumbersColor (Queryable[Tuple[float, float, float]]?): The color of grid numbers, default is 0.2 0.2 0.2  
                Properties: create, query, edit
        highlightConnection (Queryable[str]?): Specifies the name of a selectionConnection object that  
                the editor will synchronize with its highlight list. Not all  
                editors have a highlight list. For those that do, it is a secondary  
                selection list.  
                Properties: create, query, edit
        imageBaseColor (Queryable[Tuple[float, float, float]]?): The base color of the image, default is white 1.0 1.0 1.0  
                Properties: create, query, edit
        imageDim (bool?): Toggles the image dimming.  
                Properties: create, query, edit
        imageDisplay (bool?): Toggles the Texture Image display.  
                Properties: query, edit
        imageNames (bool?): List image names for all Texture Images available for display,  
                if any.  
                Properties: query
        imageNumber (Queryable[int]?): Sets the number of Texture Images to display.  
                This depends on the number of textures corresponding to  
                the current selection. If there are N textures, then the  
                possible Texture Image numbers are 0 to N-1.  
                Properties: query, edit
        imagePixelSnap (bool?): Sets a mode so that UV transformations in  
                the UV Texture Editor will cause UV values to snap  
                to image pixel corners. Which pixels are used depends on whether  
                a Texture Image or an Editor Image is being displayed. If both  
                are displayed, the Texture Image pixels will be used.  
                Properties: query, edit
        imageRatio (bool?): Sets the window to draw using the Texture Image's height versus  
                width ratio. If the width is greater than the height,  
                then the width is set to be 1 "unit" in the window,  
                and the height is adjusted by width divided by height. This  
                only affects the display of a Texture Image, not an Editor Image.  
                Properties: query, edit
        imageRatioValue (Queryable[float]?): Query current image ratio value in UV Editor.  
                Properties: query
        imageSize (bool?): Returns the size of the Texture Image currently being displayed.  
                The values returned are width followed by height.  
                Image size can only be queried.  
                Properties: query
        imageTileRange (Queryable[Tuple[float, float, float, float]]?): Sets the UV range of the display. The 4 values specify the  
                minimum U, V and maximum U, V in that order. When viewing a texture  
                image, these values affect how many times the image is tiled based on  
                appropriate parameters (e.g. Repeat UV, Mirror, Wrap, etc...)  
                When viewing an Editor Image these values determine the visible size  
                of the image. For example, setting the range to ( 0, 0, 2, 1 ) will  
                cause the Editor Image to be loaded into a 2x1 rectangle, distorting  
                it as necessary to fill the available space.  
                Properties: query, edit
        imageUnfiltered (bool?): Sets the Texture Image to draw unfiltered. The image will  
                appear "pixelated" when the display resolution is higher than the  
                resolution of the image.  
                Properties: query, edit
        internalFaces (bool?): Display contained faces by the selected components.  
                Properties: create, query, edit
        labelPosition (Queryable[str]?): The position of the grid's numeric labels. Valid values are  
                "axis" and "edge".  
                Properties: query, edit
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
        maxResolution (Queryable[int]?): This flag will set the current cached texture's maximum resolution.  
                Properties: create, query, edit
        multiColorAlpha (Queryable[float]?): Sets the multi-color alpha of shaded UVs.  
                Properties: create, query, edit
        nbImages (bool?): returns the number of images  
                Properties: query
        nextView (bool?): Switches to the next view.  
                Properties: edit
        numUvSets (bool?): This flag will return the number of UV sets for selected  
                objects in the texture window.  
                Properties: create, query, edit
        numberOfImages (Queryable[int]?): The number of Texture Images currently available.  
                for display.  
                Properties: query
        numberOfTextures (Queryable[int]?): The number of textures currently available.  
                for display.  
                Properties: query
        panel (Queryable[str]?): Specifies the panel for this editor. By default if  
                an editor is created in the create callback of a scripted panel it  
                will belong to that panel. If an editor does not belong to a panel  
                it will be deleted when the window that it is in is deleted.  
                Properties: create, query
        parent (Queryable[str]?): Specifies the parent layout for this editor. This flag will only  
                have an effect if the editor is currently un-parented.  
                Properties: create, query, edit
        previousView (bool?): Switches to the previous view.  
                Properties: edit
        realSize (bool?): This will display the image with the size of the  
                internal buffer. Note: This argument no long has  
                any affect on image display.  
                Properties: create
        refresh (bool?): requests a refresh of the current Editor Image.  
                Properties: edit
        relatedFaces (bool?): Display connected faces by the selected components.  
                Properties: create, query, edit
        removeAllImages (bool?): remove all the Editor Images from the Editor Image Stack  
                Properties: edit
        removeImage (bool?): remove the current Editor Image from the Editor Image Stack  
                Properties: edit
        rendererString (Queryable[str]?): Set or query the string describing the current renderer.  
                Properties: create, query, edit
        reset (bool?): Resets the ground plane to its default values.  
                Properties: create
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
        selectInternalFaces (bool?): Add to selectionList the faces which are contained by  
                (internal to) selected components.  
                Properties: create, query, edit
        selectRelatedFaces (bool?): Add to selectionList the faces which are connected to  
                (non-internally related to) selected components.  
                Properties: create
        selectionConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will synchronize with its own selection list. As the user  
                selects things in this editor, they will be selected in the  
                selectionConnection object. If the object undergoes changes, the  
                editor updates to show the changes.  
                Properties: create, query, edit
        setUvSet (int?): This flag will set the current UV set on one given  
                selected object within the texture window.  
                Properties: create, edit
        singleBuffer (bool?): Set the display in single buffer mode  
                Properties: create, query, edit
        size (Queryable[float]?): Sets the size of the grid.  
                Properties: create, query, edit
        solidMap3dView (bool?): Display a solid overlay for the active texture map in 3D viewport.  
                Properties: create, query, edit
        solidMapColorSeed (Queryable[int]?): Sets the multi-color seed of shaded UVs.  
                Properties: create, query, edit
        solidMapPerShell (bool?): Display a solid overlay with a random color per shell.  
                Properties: create, query, edit
        spacing (float?): Sets the spacing between main grid lines.  
                Properties: create
        stateString (bool?): Query only flag. Returns the MEL command that will create an  
                editor to match the current editor state. The returned command string  
                uses the string variable $editorName in place of a specific name.  
                Properties: query
        style (Queryable[int]?): This flag is obsolete and should not be used.  
                Properties: query, edit
        subdivisionLinesColor (Queryable[Tuple[float, float, float]]?): The color of subdivision lines, default is 0.25 0.25 0.25  
                Properties: create, query, edit
        textureBorder3dView (bool?): Toggles the texture borders display in 3d viewport.  
                Properties: create, query, edit
        textureBorderColor (Queryable[Tuple[float, float, float]]?): Sets the display color of texture border.  
                Properties: create, query, edit
        textureBorderWidth (Queryable[int]?): Set the display edge width of texture border.  
                Properties: create, query, edit
        textureNames (bool?): Texture names for all Texture Images available for display,  
                if any.  
                Properties: query
        textureNumber (Queryable[int]?): Sets the number of textures to display  
                This depends on the number of textures corresponding to  
                the current selection. If there are N textures, then the  
                possible Texture Image numbers are 0 to N-1.  
                Properties: query, edit
        tileLabels (bool?): Toggles the texture tile label display.  
                Properties: create, query, edit
        tileLinesColor (Queryable[Tuple[float, float, float]]?): The color of tile lines, default is 0.0 0.0 0.0  
                Properties: create, query, edit
        toggle (bool?): Toggles the ground plane display.  
                Properties: create, query, edit
        toggleExposure (bool?): Toggles between the current and the default exposure value of the editor.  
                Properties: edit
        toggleGamma (bool?): Toggles between the current and the default gamma value of the editor.  
                Properties: edit
        unParent (bool?): Specifies that the editor should be removed from its layout.  
                This cannot be used in query mode.  
                Properties: create, edit
        unlockMainConnection (bool?): Unlocks the mainConnection, effectively restoring the original  
                mainConnection (if it is still available), and dynamic updates.  
                Properties: create, edit
        updateMainConnection (bool?): Causes a locked mainConnection to be updated from the orginal  
                mainConnection, but preserves the lock state.  
                Properties: create, edit
        useFaceGroup (bool?): Display faces that are associated with the groupId  
                that is set on the mesh node that is drawn.  
                (The attribute "displayFacesWithGroupId")  
                Properties: create, query, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        usedPercentageHUDRange (Queryable[Tuple[float, float, float, float]]?): Sets the range when calculating used UV space percentage. The 4 values specify the minimum U, V and maximum U, V in that order., default is 0 0 1 1.  
                Properties: create, query, edit
        uvSets (bool?): This flag will return strings containing  
                UV set and object name pairs for selected  
                objects in the texture window. The syntax of  
                each pair is "objectName | uvSetName", where |  
                is a literal character.  
                Properties: create, query, edit
        viewPortImage (bool?): Toggles the view port/ caching Texture Images.  
                Properties: create, edit
        viewTransformName (Queryable[str]?): Sets the view pipeline to be applied if color management is enabled in the  
                current editor.  
                Properties: query, edit
        wireframeComponentColor (Queryable[Tuple[float, float, float, float]]?): Sets or queries the RGBA component wireframe color.  
                Properties: create, query, edit
        wireframeObjectColor (Queryable[Tuple[float, float, float, float]]?): Sets or queries the RGBA object wireframe color.  
                Properties: create, query, edit
        writeImage (str?): write the current Editor Image to disk  
                Properties: edit

    Returns:
        str: The name of the texture window

    Example:
    """

