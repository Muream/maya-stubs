from __future__ import annotations

from typing import *

import maya.api.OpenMaya
import maya.api.OpenMayaRender

Unknown = Any

class M3dView:
    """M3dView provides methods for working with 3D model views."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    @staticmethod
    def active3dView(*args: Unknown, **kwargs: Unknown) -> Any:
        """active3dView() -> M3dView

        Returns the active view in the form of a class (M3dView) that can operate on it.
        """

    @staticmethod
    def activeAffectedColor(*args: Unknown, **kwargs: Unknown) -> Any:
        """activeAffectedColor() -> MColor

        Returns the color for active affected objects.
        """

    @staticmethod
    def activeTemplateColor(*args: Unknown, **kwargs: Unknown) -> Any:
        """activeTemplateColor() -> MColor

        Returns the color for active template objects.
        """

    @staticmethod
    def applicationShell(*args: Unknown, **kwargs: Unknown) -> Any:
        """applicationShell() -> long

        Returns a long containing a C++ 'void' pointer which points to the native handle for Maya's main window.
        """

    @staticmethod
    def backgroundColor(*args: Unknown, **kwargs: Unknown) -> Any:
        """backgroundColor() -> MColor

        Returns the value of the background color.
        """

    @staticmethod
    def backgroundColorBottom(*args: Unknown, **kwargs: Unknown) -> Any:
        """backgroundColorBottom() -> MColor

        Returns the value of the background gradient bottom color.
        """

    @staticmethod
    def backgroundColorTop(*args: Unknown, **kwargs: Unknown) -> Any:
        """backgroundColorTop() -> MColor

        Returns the value of the background gradient top color.
        """

    def beginGL(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """(Deprecated: Please use Viewport 2.0 APIs instead.) beginGL() -> self

        Setup port for native OpenGL drawing calls.
        """

    def beginProjMatrixOverride(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """(Deprecated: Please use MHWRender::MRenderOverride instead.) beginProjMatrixOverride(projectionMatrix) -> self

        Begin overriding the projection matrix used in openGL drawing.
        This override is enabled until endProjMatrixOverride() is called.

        * projectionMatrix (MMatrix) - Projection matrix used in openGL drawing
        """

    def beginSelect(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """beginSelect(buffer=None, size=0) -> self

        Start selecting. The buffer passed is used to record selection hits.

        * buffer (bytearray) - OpenGl pick buffer
        * size (int) - Buffer size
        """

    def beginXorDrawing(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """beginXorDrawing(drawOrthographic=True, disableDepthTesting=True, lineWidth=1.0, stipplePattern=kStippleNone, lineColor=MColor(1, 1, 1)) -> self

        Setup the context for exclusive-or (XOR) drawing.

        In XOR drawing the color values of the pixels being drawn is exclusive-ored with the color values already present in the view. The advantage of this is that exclusive-oring the same pixels with the same color values a second time will restore the pixels to their original colors, making it possible to temporarily display and erase lines without having to redraw the entire view. This makes XOR drawing particularly useful for drawing guidelines for tools.

        One disadvantage of XOR drawing is that the final color after the exclusive-or will not match your drawing color, except when the original color of the pixel was black. For example, XORing a white line across a red background will result in a cyan line and XORing it across a changing background will result in a line of changing colors. However in most situations where you would use XOR drawing the color of the lines is irrelevant just so long as they are visible.

        It is an error to call beginXorDrawing() again before calling endXorDrawing() first.

        * drawOrthographic (bool) - Draw using orthographic projection. Default is True.
        * disableDepthTesting (bool) - Disable depth testing during draw. Default is True.
        * lineWidth (float) - Set up line width. Default is 1.
        * stipplePattern (int) - Line stipple pattern. Default is kStippleNone.
        * lineColor (MColor) - Line color. Default is white (1,1,1).

        Valid stipple patterns:
          kStippleNone      No stipple. Solid line
          kStippleDashed    Dashed line stipple
        """

    def colorAtIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """colorAtIndex(index, table=kActiveColors) -> MColor

        Returns the value of the color at the given index in the application's color table.


        * index (int) - Index of the color to retrieve
        * table (int) - Table to index into

        Valid color tables:
          kActiveColors        Colors for active objects
          kDormantColors       Colors for dormant objects
          kTemplateColor       Colors for templated objects
          kBackgroundColor     Colors for background color
        """

    def colorMask(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """(Deprecated: Please use MHWRender::MUIDrawManager instead.) colorMask() -> [bool, bool, bool, bool]

        Get the current color mask
        """

    def disallowPolygonOffset(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """disallowPolygonOffset() -> bool

        Returns the current state of the disallow polygon offset bit.  See setDisallowPolygonOffset for more information.
        """

    def display(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """display() -> long

        Returns a long containing a C++ 'void' pointer which points to the X display for this view.
        The X display is neccessary for using openGL.
        """

    @staticmethod
    def displayStatus(*args: Unknown, **kwargs: Unknown) -> Any:
        """displayStatus(path) -> int

        Returns the display status of the given DAG path.

        * path (MDagPath) - the DAG path to get.

        Valid display status:
          kActive               Object is active (selected).
          kLive                 Object is live (construction surface).
          kDormant              Object is dormant.
          kInvisible            Object is invisible (not drawn).
          kHilite               Object is hilited (has selectable components).
          kTemplate             Object is templated (Not renderable).
          kActiveTemplate       Object is active and templated.
          kActiveComponent      Object has active components.
          kLead                 Last selected object.
          kIntermediateObject   Construction object (not drawn).
          kActiveAffected       Affected by active object(s).
          kNoStatus             Object does not have a valid display status.
        """

    def displayStyle(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """displayStyle() -> int

        Return the display style for this 3d view.  kBoundingBox     Bounding box display.
          kFlatShaded      Flat shaded display.
          kGouraudShaded   Gouraud shaded display.
          kWireFrame       Wire frame display.
          kPoints          Points only display.
        """

    def drawText(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """(Deprecated: Please use MHWRender::MUIDrawManager in a MHWRender::MHUDRender operation instead.) drawText(text, position, textPosition=kLeft) -> self

        Draws the given text at the given spot in the default font.  This method is provided as a convienient way to draw OpenGL text.

        * text (string) - Text to draw
        * position (MPoint) - Position in space to draw at
        * textPosition (int) - Text position relative to the point

        Valid textPosition values:
          kLeft      Draw text to the left of the point
          kCenter    Draw text centered around the point
          kRight     Draw text to the right of the point
        """

    def endGL(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """(Deprecated: Please use Viewport 2.0 APIs instead.) endGL() -> self

        End OpenGL drawing.
        """

    def endProjMatrixOverride(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """(Deprecated: Please use MHWRender::MRenderOverride instead.) endProjMatrixOverride() -> self

        End projection matrix override enabled by beginProjMatrixOverride().
        """

    def endSelect(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """endSelect() -> int

        Finish a selection sequence. Result is stored in the buffer passed  in the beginSelect call.
        """

    def endXorDrawing(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """endXorDrawing() -> self

        Reset the context to non-exclusive-or (non-XOR) screen drawing.

        If endXorDrawing() is called without first calling beginXorDrawing() an error will result.
        """

    def filteredObjectList(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """filteredObjectList() -> MSelectionList

        Returns a selection list containing all of the objects that remain after filtering is applied to the view.
        """

    @staticmethod
    def get3dView(*args: Unknown, **kwargs: Unknown) -> Any:
        """get3dView(index) -> M3dView

        Returns the 3D view at the given index.

        * index (int) - index of the view to get
        """

    def getCamera(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getCamera() -> MDagPath

        Get the camera for this view.
        """

    def getColorIndexAndTable(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getColorIndexAndTable(glindex) -> [int, int]

        Returns the index and color table representing the given OpenGL color-index value. This method is useful when converting color indices obtained from glReadPixels(GL_COLOR_INDEX) to Maya color-index values suitable for use with the colorAtIndex and setDrawColor methods.

        * glindex (int) - Value of the OpenGL color-index to retrieve
        """

    def getLightCount(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getLightCount(visible=True) -> int

        Get the number of lights for the view.

        * visible (bool) - Specify whether to count visible lights only. By Default this is set True.
        """

    def getLightIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getLightIndex(lightNumber) -> int

        Get the internal light index for a given light number

        * lightNumber (int) - Number of the light interested in
        """

    def getLightPath(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getLightPath(lightNumber) -> MDagPath

        Get the path to a certain light.

        * lightNumber (int) - Number of the light interested in
        """

    def getLightingMode(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getLightingMode() -> int

        Get the current lighting mode for the view:
          kLightAll         All lights
          kLightSelected    Selected lights
          kLightActive      Active lights
          kLightDefault     Default light
          kUnused1          Not currently used in Maya
          kLightNone        No lights / lighting disabled
        """

    @staticmethod
    def getM3dViewFromModelEditor(*args: Unknown, **kwargs: Unknown) -> Any:
        """getM3dViewFromModelEditor(name) -> M3dView

        Given the name of a model editor, get the M3dView used by that editor. If this fails, then a editor with the given name could not be located.

        * name (string) - The name of the model editor.
        """

    @staticmethod
    def getM3dViewFromModelPanel(*args: Unknown, **kwargs: Unknown) -> Any:
        """getM3dViewFromModelPanel(name) -> M3dView

        Given the name of a model panel, get the M3dView used by that panel. If this fails, then a panel with the given name could not be located.

        * name (string) - The name of the model panel.
        """

    def getRendererName(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getRendererName() -> int

        Get the name of the current renderer being used for drawing to this view:
          kDefaultQualityRenderer   Equivalent to when the renderer name is "base_OpenGL_Renderer" when queried from the "modelEditor" command
          kHighQualityRenderer      Equivalent to when the renderer name is "hwRender_OpenGL_Renderer" when queried from the "modelEditor" command
          kViewport2Renderer        Equivalent to the viewport 2.0 renderer
          kExternalRenderer         An externally defined renderer name has been set.
        """

    def getScreenPosition(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getScreenPosition() -> [int, int]

        Returns the current position of this view window in screen coordinates.

        This is useful for finding out the exact location of the window as it appears on the screen. These values are in UI coordinate space so the y value increases from bottom to top.
        """

    def glxContext(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """glxContext() -> long

        Returns a long containing a C++ 'void' pointer which points to the OpenGL context for this view.
        This context is neccessary for using the offscreen rendering API to share textures and display lists with Maya.
        """

    @staticmethod
    def hiliteColor(*args: Unknown, **kwargs: Unknown) -> Any:
        """hiliteColor() -> MColor

        Returns the color for hilited objects.
        """

    def initNames(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """initNames() -> self

        Reset the name stack. Valid only when beginSelect() has been called.
        """

    @staticmethod
    def isBackgroundGradient(*args: Unknown, **kwargs: Unknown) -> Any:
        """isBackgroundGradient() -> bool

        Returns whether a gradient is being used as the background color.
        """

    def isLightVisible(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """isLightVisible(lightNumber) -> bool

        Find out if a light is visible in the view

        * lightNumber (int) - Number of the light interested in
        """

    def isShadeActiveOnly(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """isShadeActiveOnly() -> bool

        Returns True if this view's display style is shaded for objects that are active and wireframe otherwise.
        """

    def isVisible(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """isVisible() -> bool

        Returns True if this viewport is visible.
        """

    kActive: int = 0
    kActiveAffected: int = 10
    kActiveColors: int = 0
    kActiveComponent: int = 7
    kActiveTemplate: int = 6
    kBackgroundColor: int = 6
    kBoundingBox: int = 0
    kCenter: int = 1
    kDefaultQualityRenderer: int = 0
    kDepth_8: int = 0
    kDepth_Float: int = 1
    kDisplayCVs: int = 131072
    kDisplayCameras: int = 32
    kDisplayDeformers: int = 256
    kDisplayDimensions: int = 4096
    kDisplayDynamicConstraints: int = 134217728
    kDisplayDynamics: int = 512
    kDisplayEverything: int = -1
    kDisplayFluids: int = 2097152
    kDisplayFollicles: int = 4194304
    kDisplayGrid: int = 65536
    kDisplayHairSystems: int = 8388608
    kDisplayHulls: int = 262144
    kDisplayIkHandles: int = 128
    kDisplayImagePlane: int = 16777216
    kDisplayJoints: int = 64
    kDisplayLights: int = 16
    kDisplayLocators: int = 2048
    kDisplayManipulators: int = 268435456
    kDisplayMeshes: int = 4
    kDisplayNCloths: int = 33554432
    kDisplayNParticles: int = 536870912
    kDisplayNRigids: int = 67108864
    kDisplayNurbsCurves: int = 1
    kDisplayNurbsSurfaces: int = 2
    kDisplayParticleInstancers: int = 1024
    kDisplayPivots: int = 16384
    kDisplayPlanes: int = 8
    kDisplaySelectHandles: int = 8192
    kDisplayStrokes: int = 524288
    kDisplaySubdivSurfaces: int = 1048576
    kDisplayTextures: int = 32768
    kDormant: int = 2
    kDormantColors: int = 2
    kExcludeMotionTrails: int = 1073741824
    kExcludePluginShapes: int = -2147483648
    kExternalRenderer: int = 3
    kFlatShaded: int = 1
    kGouraudShaded: int = 2
    kHighQualityRenderer: int = 1
    kHilite: int = 4
    kIntermediateObject: int = 9
    kInvisible: int = 3
    kLead: int = 8
    kLeft: int = 0
    kLightActive: int = 2
    kLightAll: int = 0
    kLightDefault: int = 3
    kLightNone: int = 5
    kLightSelected: int = 1
    kLive: int = 1
    kNoStatus: int = 11
    kPoints: int = 4
    kRight: int = 2
    kStippleDashed: int = 1
    kStippleNone: int = 0
    kTemplate: int = 5
    kTemplateColor: int = 5
    kUnused1: int = 4
    kViewport2Renderer: int = 2
    kWireFrame: int = 3
    @staticmethod
    def leadColor(*args: Unknown, **kwargs: Unknown) -> Any:
        """leadColor() -> MColor

        Returns the color for lead objects.
        """

    @staticmethod
    def liveColor(*args: Unknown, **kwargs: Unknown) -> Any:
        """liveColor() -> MColor

        Returns the color for live objects.
        """

    def loadName(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """loadName(int) -> self

        Replace the top of the name stack with the given name. Valid only when beginSelect() has been called.

        * name (int) - Name to be loaded onto the top of the stack.
        """

    def modelViewMatrix(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """modelViewMatrix() -> MMatrix

        Returns the modelview matrix currently being used by OpenGL in the current view
        """

    def multipleDrawEnabled(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """multipleDrawEnabled() -> bool

        This method returns the multiple draw enable state for this view.
        """

    def multipleDrawPassCount(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """(Deprecated: Please use MHWRender::MRenderOverride instead.) multipleDrawPassCount() -> int

        This method returns the number of multiple draw passes that are going to be made. By default a 1 is returned.
        """

    def numActiveColors(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """numActiveColors() -> int

        Returns the number of active object colors in the internal application color table.
        """

    def numDormantColors(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """numDormantColors() -> int

        Returns the number of dormant object colors in the internal application color table.
        """

    def numUserDefinedColors(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """numUserDefinedColors() -> int

        Returns the number of user defined colors in the internal application color table.  These colors may be changed by the user and assigned to specific objects.  See the methods of MFnDagNode for information on assigning user defined colors to individual objects.

        The user defined colors are not a color table of their own.  They exist in the active and dormant color tables.
        """

    @staticmethod
    def numberOf3dViews(*args: Unknown, **kwargs: Unknown) -> Any:
        """numberOf3dViews() -> int

        Returns the number of 3D views currently in existance.
        """

    def objectDisplay(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """objectDisplay() -> int

        Returns a display object mask that indicates which object types are drawn in the current view:
          kDisplayEverything            Show everything
          kDisplayNurbsCurves           Show nurbs curves
          kDisplayNurbsSurfaces         Show nurbs surfaces
          kDisplayMeshes                Show meshes
          kDisplayPlanes                Show planes
          kDisplayLights                Show lights
          kDisplayCameras               Show camera
          kDisplayJoints                Show joints
          kDisplayIkHandles             Show IK handles
          kDisplayDeformers             Show deformers
          kDisplayDynamics              Show dynamics
          kDisplayLocators              Show locators
          kDisplayDimensions            Show dimensions
          kDisplaySelectHandles         Show selection handles
          kDisplayPivots                Show pivots
          kDisplayTextures              Show textures
          kDisplayGrid                  Show the grid
          kDisplayCVs                   Show NURBS CVs
          kDisplayHulls                 Show NURBS hulls
          kDisplayStrokes               Show strokes
          kDisplaySubdivSurfaces        Show subdivision surfaces
          kDisplayFluids                Show fluids
          kDisplayFollicles             Show follcles
          kDisplayHairSystems           Show hair systems
          kDisplayImagePlane            Show image plane
          kDisplayNCloths               Show nCloths
          kDisplayNRigids               Show nRigids
          kDisplayDynamicConstraints    Show nDynamicConstraints
          kDisplayManipulators          Show Manipulators
          kDisplayNParticles            Show nParticles
          kExcludeMotionTrails          Show motion trails
          kExcludePluginShapes          Show plugin shapes
        """

    def objectListFilterName(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """objectListFilterName() -> string

        Get the current object list filter name. If none then an emptystring will be returned.
        """

    def playblastPortHeight(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """playblastPortHeight() -> int

        Returns the port height of current playblast.
        Valid only when playblast command has been called.
        Otherwise, an invalid value 0 is returned.
        """

    def playblastPortWidth(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """playblastPortWidth() -> int

        Returns the port width of current playblast.
        Valid only when playblast command has been called.
        Otherwise, an invalid value 0 is returned.
        """

    def pluginObjectDisplay(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """pluginObjectDisplay(pluginDisplayFilter) -> bool

        Returns True if the plugin display filter specified by the pluginDisplayFilter is enabled in the current view.

        * pluginDisplayFilter (string) - The name of the plugin display filter.
        """

    def popName(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """popName() -> self

        Removes the top of the name stack. Valid only when beginSelect() has been called.
        """

    def popViewport(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """popViewport() -> self

        Pops the current viewport off of the viewport stack.
        """

    def portHeight(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """portHeight() -> int

        Returns the height of the current viewport.
        """

    def portWidth(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """portWidth() -> int

        Returns the width of the current viewport.
        """

    def projectionMatrix(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """projectionMatrix() -> MMatrix

        Returns the projection matrix currently being used by OpenGL in the current view
        """

    def pushName(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """pushName(int) -> self

        Pushes a new name on the name stack. Valid only when beginSelect() has been called.

        * name (int) - Name to be loaded onto the top of the stack.
        """

    def pushViewport(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """pushViewport(x, y, width, height) -> self

        Set the current viewport dimensions. Will keep track of the last viewport dimensions on a stack.
        When finished with this viewport, the current dimensions should be removed from the top of stack using M3dView.popViewport().

        * x (int) - Lower left corner of viewport (x coordinate).
        * y (int) - Lower left corner of viewport (y coordinate).
        * width (int) - Width of the viewport.
        * height (int) - Height of the viewport.
        """

    def readBufferTo2dTexture(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """(Deprecated: Please use MHWRender::MRenderTargetManager instead.) readBufferTo2dTexture(x, y, width, height) -> self

        Read the depth values from the frame buffer for a given view into a predefined OpenGL 2d texture. It is assumed that such a texture has been created and bound before making this call.

        * x (int) - Start position x to read.
        * y  (int) - Start position y to read.
        * width (int) - Number of pixels in x to read.
        * height (int) - Number of pixels in y to read.
        """

    def readColorBuffer(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """(Deprecated: Please use MHWRender::MRenderTargetManager::acquireRenderTarget() instead.)readColorBuffer(image, readRGBA=False) -> self

        Read the RGB values from the frame buffer for a given view.
        The buffer is read in a pixel format which is BGRA by default, such that each channel is one byte in size.

        * image (MImage) - The image contains the frame buffer pixels.
        * readRGBA (bool) - Read the image back in RGBA format. By default the format is BGRA.
        """

    def readDepthMap(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """(Deprecated: Please use MHWRender::MRenderTargetManager::acquireRenderTarget() instead.) readDepthMap(x, y, width, heigth, bufferPtr, depthMapPrecision) -> self

        Read the depth values from the frame buffer for a given view.
        The buffer is read into a block of data as defined as an argument. The data block size must be large enough to accomodate ( view width * view height * depth map precision ) bytes of data.

        * x (int) - Start position x to read.
        * y (int) - Start position y to read.
        * width (int) - Number of pixels in x to read.
        * height (int) - Number of pixels in y to read.
        * bufferPtr (byterray) - Pointer to depth data allocated by the caller.
        * depthMapPrecision (int) - Enumerated depth precision:
            kDepth_8          8 bits.
            kDepth_Float      Floating point.
        """

    @staticmethod
    def referenceLayerColor(*args: Unknown, **kwargs: Unknown) -> Any:
        """referenceLayerColor() -> MColor

        Returns the color for objects which belong to a display layer whose display type is Reference. This color is also used for objects whose display override is set to Reference.
        """

    def refresh(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """refresh(all=False, force=False, offscreen=False) -> self


        Refresh the this view.

        * all (bool) - If True then refresh all views, otherwise refresh this view.
        * force (bool) - If True then force views to refresh even if they do not require it.
        * offscreen (bool) - Should the buffer be redrawn if it's offscreen?
        """

    def renderOverrideName(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """renderOverrideName() -> string

        Get the current render override name. If none then an empty string will be returned.
        """

    def rendererString(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """rendererString() -> string

        Get the string name of the current renderer being used for drawing to this view
        """

    def scheduleRefresh(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """scheduleRefresh() -> self

        Schedule a forced refresh for this 3d-view. This method may be called safely at any time from any thread. The refresh will occur on the main thread when Maya next becomes idle. If a refresh has already been scheduled for this view but has not yet occurred then this method will do nothing.
        """

    @staticmethod
    def scheduleRefreshAllViews(*args: Unknown, **kwargs: Unknown) -> Any:
        """scheduleRefreshAllViews() -> None

        Schedule a forced refresh for all 3d-views. This method may be called safely at any time from any thread. The refresh will occur on the main thread when Maya next becomes idle. If a refresh has already been scheduled but has not yet occurred then this method will do nothing.
        """

    def selectMode(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """selectMode() -> bool

        Tells if this M3dView is in selection mode.
        """

    def setCamera(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setCamera(camera) -> self

        Set the camera for this view.

        * camera (MDagPath) - Dag path of the camera for this view
        """

    def setColorMask(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """(Deprecated: Please use MHWRender::MUIDrawManager instead.) setColorMask(r, g, b, a) -> self

        Set the current color mask.

        * r (bool) - Red color mask flag.
        * g (bool) - Green color mask flag.
        * b (bool) - Blue color mask flag.
        * a (bool) - Alpha color mask flag.
        """

    def setDisallowPolygonOffset(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setDisallowPolygonOffset(v) -> self

        Certain Maya actions will use glPolygonOffset to offset polygons drawing into the depth buffer.  This method controls this behavior. When True, it prevents Maya from altering the polygon offset parameters.

        * v (bool) - enable/disable the polygon offset
        """

    def setDisplayStyle(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setDisplayStyle(style, activeOnly=False) -> self

        Sets the display style for this view.

        * style (int) - The display style to be set for this view
        See displayStyle() description for a list a valid display style
        """

    def setDrawColor(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """(Deprecated: Please use MUIDrawManager::setColorIndex instead.) setDrawColor(index, table=kActiveColors) -> self
        setDrawColor(color) -> self

        Set the color to draw in.  The index argument is an index into the application's color tables.  Valid values range between zero and the size of the table minus one.  The size of the active and dormant color tables can be found using methods of this class.  The background and template color tables are both of size one.

        These indices do not directly correspond to those of the underlying OpenGL color index mode.  Using the glIndex call directly is not recommended and may cause unpredictable results.  This method should be used instead.

        Note that this method will work in either RGBA mode or color index mode.

        * index (int) - index of the color to draw in
        * table (int) - color table to index into
        See colorAtIndex() description of a list a valid color table

        Or
        Set the color to draw in.
        It is a convenient replacement for glColor3.

        * color (MColor) - color to draw in
        """

    def setDrawColorAndAlpha(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """(Deprecated: Please use MUIDrawManager::setColor instead.) setDrawColorAndAlpha(color) -> self

        Set the color to draw in.
        It is a convenient replacement for glColor4.

        * color (MColor) - color to draw in
        """

    def setMultipleDrawEnable(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """(Deprecated: Please use MHWRender::MRenderOverride instead.)setMultipleDrawEnable(enable) -> self

        This method enables/disables multiple camera drawing for this view. If multiple draw is disabled, then this view will behave like a normal Maya view.

        * enable (bool) - If True, then multiple draw is enabled.
        """

    def setMultipleDrawPassCount(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """(Deprecated: Please use MHWRender::MRenderOverride instead.) setMultipleDrawPassCount(count) -> self

        This method sets the number of multiple draw passes when multiple draw is enabled.

        * count (int) - The number of multiple draw passes.
        """

    def setObjectDisplay(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setObjectDisplay(displayMask) -> self

        Sets a display object mask that indicates which object types are drawn in current view. By default every thing is displayed.

        * displayMask (int) - A combination of display object mask
        See objectDisplay() description for a list of valid display mask
        """

    def setObjectListFilterName(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setObjectListFilterName(name) -> self

        Set the name of the object list filter (MObjectListFilter) to use.

        The filter must be registered before it can be used.

        If the name is an empty string then any existing filter will be removed.

        Any previously set filter will be replaced with the new one.

        * name (string) - Name of the filter.
        """

    def setPluginObjectDisplay(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setPluginObjectDisplay(pluginDisplayFilter, on) -> self

        Enables or disables a user-defined display filter (i.e. one which was registered using MFnPlugin.registerDisplayFilter() or the 'pluginDisplayFilter' command).

        In Default Viewport, the plug-in will have to check the state of the user-defined display filter in the node's draw code.
        In Viewport 2.0, nodes will be filtered automatically based on the classification associated with the filter.
        During selection/snapping, the plugin will have to check the state of the filter in the node's select/snap code.

        * pluginDisplayFilter (string) - The name of the plugin display filter.
        * on (bool) - Enable or disable the plugin display filter.
        """

    def setRenderOverrideName(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setRenderOverrideName(name) -> self

        Set the name of a render override (MRenderOverride) to use.

        The override must be registered before it can be used.

        The override cannot be set unless the view is set to be using the Viewport 2.0 renderer.

        If the override name is an empty string then the any existing override will be removed.

        * name (string) - name Name of the override.
        """

    def setShowObjectFilterNameInHUD(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setShowObjectFilterNameInHUD(show) -> self

        Sets whether or not to display the object filter UI name in the heads up display when an object filter is active. This string is concatenated with the camera name.

        * show (bool) - If True, show the filter UI name in the HUD
        """

    def setShowViewSelectedChildren(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setShowViewSelectedChildren(show) -> self

        This method changes the way that view selected works. By default, view selected with show all of the children of the objects in the view selected set. If False is passed to this method, then only the obejcts in the view selected set and their shapes will be drawn.

        * show (bool) - True if all of the children of view selected objects should be displayed. True is the default behavior for view selected.
        """

    def setUserDefinedColor(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setUserDefinedColor(index, color) -> self

        Sets the user defined color at the given index.  Valid indices range between zero and the number of user defined colors.
        Returns an index into the application's color table

        * index (int) - index into the user defined color
        * color (MColor) - color to set to
        """

    def setViewSelectedPrefix(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setViewSelectedPrefix(prefix) -> self

        Sets the prefix for the camera name as displayed in the heads up display when view selected is enabled. The prefix is concatenated with the camera name.
        The default value is "isolate: "

        * prefix (string) - The prefix to use.
        """

    def showObjectFilterNameInHUD(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """showObjectFilterNameInHUD() -> bool

        Returns whether the object filter UI name is shown in the heads up display when an object filter is active.
        """

    def showViewSelectedChildren(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """showViewSelectedChildren() -> bool

        Returns turn if view selected shows all of the children of the obejcts that are flagged for view selected.
        """

    @staticmethod
    def templateColor(*args: Unknown, **kwargs: Unknown) -> Any:
        """templateColor() -> MColor

        Returns the value of the template color.
        """

    def textureMode(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """textureMode() -> bool

        Tells if this M3dView is in texture mode.
        """

    def twoSidedLighting(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """twoSidedLighting() -> bool

        Return True if the Two-sided lighting mode is enabled.
        """

    def updateViewingParameters(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """updateViewingParameters() -> self

        This method tells the camera to set the view's transformation matrix.
        """

    def userDefinedColorIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """userDefinedColorIndex(index) -> int

        Returns the index for the given user-defined color.  Valid values for the index argument range between zero and the number of user-defined colors minus one.

        The index returned gives the location of the specified color inside the active and dormant color tables (the index is the same in both tables).

        * index (int) - Index into user-defined colors
        """

    def usingDefaultMaterial(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """usingDefaultMaterial() -> bool

        Returns True if the view is currently displaying objects using the default material.
        """

    def usingMipmappedTextures(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """usingMipmappedTextures() -> bool

        Returns if the view is using mipmapped texture display.
        """

    def viewIsFiltered(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """viewIsFiltered() -> bool

        Returns True if the view is filtered.
        """

    def viewSelectedPrefix(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """viewSelectedPrefix() -> string

        Returns the prefix used when displaying the camera name in the heads up display when view selected in on
        """

    def viewToObjectSpace(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """viewToObjectSpace(x_pos, y_pos, localMatrixInverse, oPt, oVector) -> self

        Takes a point in port coordinates and returns a corresponding ray in object coordinates.

        * x_pos (int) - the x position of the point in port coordinates
        * y_pos (int) - the y position of the point in port coordinates
        * localMatrixInverse (MMatrix) - the inclusive matrix inverse of the object in question
        * oPt [OUT] (MPoint) - the source of the ray in object space
        * oVector [OUT] (MVector) - the direction of the ray in object space
        """

    def viewToWorld(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """viewToWorld(x_pos, y_pos, worldPt, worldVector) -> self
        viewToWorld(x_pos, y_pos, nearClipPt, farClipPt) -> self

        Takes a point in port coordinates and returns a corresponding ray in world coordinates.

        * x_pos (int) - the x position of the point in port coordinates
        * y_pos (int) - the y position of the point in port coordinates
        * worldPt [OUT] (MPoint) - the source of the ray
        * worldVector [OUT] (MVector) - the direction of the ray

        Or
        Takes a point in port coordinates and returns a point on the near and far clipping planes.

        * x_pos (int) - the x position of the point in port coordinates
        * y_pos (int) - the y position of the point in port coordinates
        * nearClipPt [OUT] (MPoint) - point on near clipping plane
        * farClipPt [OUT] (MPoint) - point on far clipping plane
        """

    def viewport(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """viewport() -> [int, int, int, int]

        Get the current viewport dimensions.
        """

    def widget(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """widget() -> long

        Returns a long containing a C++ 'void' pointer which points to the view's Qt widget.
        """

    def window(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """window() -> long

        Returns a long containing a C++ 'void' pointer which points to the native window for this view.
        """

    def wireframeOnShaded(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """wireframeOnShaded() -> bool

        Return whether we draw wireframe in shaded mode.
        """

    def wireframeOnlyInShadedMode(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """wireframeOnlyInShadedMode() -> bool

        Return whether we are in shaded mode, but that only non shaded drawing should occur (wireframe).

        In general it will return True only when the current renderer is "hwRender_OpenGL_Renderer". See the M3dView.rendererString() method for more details.
        """

    def worldToView(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """worldToView(worldPt) -> [int, int, bool]

        Converts a point in world space to port space.
        Returns the x and y coordinates of the world point in port space and if the point is not clipped.

        * worldPt (MPoint) - the point to world space
        """

    def writeColorBuffer(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """(Deprecated: Please use MHWRender::MQuadRender operation inside MHWRender::MRenderOverride instead.) writeColorBuffer(image, x=0, y=0) -> self

        Overwrite the RGB values for the frame buffer for a given view.
        Expected input is a block of RGBA, such that each channel is one byte in size.

        * image (MImage) - The image containing the block of pixels to write
        * x (int) - The location in screen space of the lower left corner (X) of the image to write. The default value is 0.
        * y (int) - The location in screen space of the lower left corner (Y) of the image to write. The default value is 0.
        """

    def xray(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """xray() -> bool

        Return True if the X-Ray mode is enabled.
        """

    def xrayJoints(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """xrayJoints() -> bool

        Return True if the X-Ray Joints mode is enabled.
        """


class MCursor:
    """Manipulate Cursors."""
    def __eq__(self, value: Unknown, /) -> Any:
        """Return self==value."""

    def __ge__(self, value: Unknown, /) -> Any:
        """Return self>=value."""

    def __gt__(self, value: Unknown, /) -> Any:
        """Return self>value."""

    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __le__(self, value: Unknown, /) -> Any:
        """Return self<=value."""

    def __lt__(self, value: Unknown, /) -> Any:
        """Return self<value."""

    def __ne__(self, value: Unknown, /) -> Any:
        """Return self!=value."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    kCrossHairCursor: MCursor
    kDefaultCursor: MCursor
    kDoubleCrossHairCursor: MCursor
    kEditCursor: MCursor
    kHandCursor: MCursor
    kPencilCursor: MCursor

class MDrawData:
    """The MDrawData class holds geometry specific information for user defined shapes which maya does not intrinsicly know about."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def geometry(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """geometry() -> long

        Returns a long containing a C++ 'void' pointer which points to the geometry associated with this draw data object.
        The geometry is set using the getDrawData method of MPxSurfaceShapeUI.
        """


class MDrawInfo:
    """This class is used by the getDrawRequests method of MPxSurfaceShapeUI to specify the current object drawing state for a user defined shape."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def canDrawComponent(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """canDrawComponent(isDisplayOn, compMask) -> bool

        Convenience method to test if components specified by the given mask can be drawn.

        * isDisplayOn (bool) - component display is on
        * mask (MSelectionMask) - component mask to test
        """

    def completelyInside(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """completelyInside() -> bool

        Returns True if the object being drawn is inside the viewing frustum.
        """

    def displayStatus(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """displayStatus() -> int

        Returns the status of the object to draw.
        See M3dView.displayStatus() for a list of status.
        """

    def displayStyle(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """displayStyle() -> int

        Returns the display appearance.
        See M3dView.displayStyle() for a list of styles.
        """

    def getPrototype(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getPrototype(drawHandler) -> MDrawRequest

        This method creates a draw request based on the current draw state.

        The draw request is placed onto maya's drawing queue (MDrawRequestQueue) where it can be processed in turn. The drawHandler argument is the shape that will be doing the drawing which is the object calling this function.

        * drawHandler (MPxSurfaceShapeUI) - the ui object that is doing the drawing
        """

    def inSelect(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """inSelect() -> bool

        Returns True during any interactive refresh, as when user is interacting with the scene in any way including camera changes, object or component TRS changes, etc. Use userChangingViewContext for determining whether user is changing the view using view context tools such as tumble, dolly or track.
        """

    def inUserInteraction(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """inUserInteraction() -> bool

        Returns True during any interactive refresh, as when user is changing the view using view context tools such as tumble, dolly or track.  Useful for changing drawing mode to something simpler to speed up interaction re-draw.  Use inUserInteraction for determining whether user is interacting with the scene in any way.
        """

    def inclusiveMatrix(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """inclusiveMatrix() -> MMatrix

        Returns the world space inclusive matrix.
        """

    def multiPath(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """multiPath() -> MDagPath

        Returns the path to the object to be drawn.
        """

    def objectDisplayStatus(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """objectDisplayStatus(displayObj) -> bool

        Determines whether the specified objects are allowed to be displayed.

        * displayObj (int) - display object mask. See M3dView.objectDisplay() for a list of valid masks.
        """

    def pluginObjectDisplayStatus(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """pluginObjectDisplayStatus(pluginDisplayFilter) -> bool

        Determines whether the specified plugin object is allowed to be displayed.

        * pluginDisplayFilter (string) - The name of the plugin display filter which is registered by pluginDisplayFilter command.
        """

    def projectionMatrix(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """projectionMatrix() -> MMatrix

        Returns the camera*projection matrix.
        """

    def setMultiPath(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setMultiPath(path) -> self

        Sets the path of the object to be drawn.

        * path (MDagPath) - the path of the object to be drawn
        """

    def userChangingViewContext(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """userChangingViewContext() -> bool

        Returns True during any interactive refresh, as when user is interacting with the scene in any way including camera changes, object or component TRS changes, etc. Use userChangingViewContext for determining whether user is changing the view using view context tools such as tumble, dolly or track.
        """

    def view(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """view() -> M3dView

        Returns the view that the drawing will take place.
        """


class MDrawProperties:
    """Draw properties"""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    color: maya.api.OpenMaya.MColor
    lineStyle: int
    lineWidth: float
    pointSize: float

class MDrawRequest:
    """This class encapsulates all the information needed to fulfill a request to draw an object or part of an object.
    This class is used by the draw methods of MPxSurfaceShapeUI derived objects.
    """
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    color: maya.api.OpenMaya.MColor
    component: maya.api.OpenMaya.MObject
    displayCullOpposite: bool
    displayCulling: bool
    displayStatus: int
    displayStyle: int
    drawData: MDrawData
    drawLast: bool
    isTransparent: bool
    material: MMaterial
    matrix: maya.api.OpenMaya.MMatrix
    multiPath: maya.api.OpenMaya.MDagPath
    def planeColor(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """planeColor(table) -> int

        Get which color is used for the specified color table.

        * table (int) - color table

        See M3dView.colorAtIndex() for a list of color tables.
        """

    def setPlaneColor(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setPlaneColor(value, table) -> self

        Set which color to use for the specified color table.

        * value (int) - index into the color table
        * table (int) - color table

        See M3dView.colorAtIndex() for a list of color tables.
        """

    token: int
    view: M3dView

class MEvent:
    """Query interactive system events."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    controlKey: int = 4
    def getWindowPosition(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getWindowPosition() -> (x, y)

        This routine is used by responders to query the position of the
        pointer when the event occurred.  It is given in screen co-ordinates.


        Returns a tuple containing the x and y position of the event.
        """

    def isModifierControl(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """isModifierControl() -> bool

        Return the state of the control key.


        Returns True if the control key was pressed at the time the event was triggered, False otherwise.
        """

    def isModifierKeyRelease(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """isModifierKeyRelease() -> bool

        Was a modifier key released.


        Returns True if a modifier key was released, False otherwise.
        """

    def isModifierLeftMouseButton(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """isModifierLeftMouseButton() -> bool

        Return the state of the left mouse button.


        This method is only valid when called in the hold event for
        another mouse press.


        Returns True if the left mouse button was pressed at the time the event was triggered, False otherwise.
        """

    def isModifierMiddleMouseButton(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """isModifierMiddleMouseButton() -> bool

        Return the state of the middle mouse button.


        This method is only valid when called in the hold event for
        another mouse press.


        Returns True if the left mouse button was pressed at the time the event was triggered, False otherwise.
        """

    def isModifierNone(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """isModifierNone() -> bool

        Determines if there are any modifiers for this event.


        Returns True if there are modifiers for this event, False otherwise.
        """

    def isModifierShift(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """isModifierShift() -> bool

        Return the state of the shift key.


        Returns True if the shift key was pressed at the time the event was triggered, False otherwise.
        """

    kLeftMouse: int = 64
    kMiddleMouse: int = 128
    modifiers: Any
    def mouseButton(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """mouseButton() -> mouseButtonType

        Get the mouse button of the last event.


        Returns the mouse button from last event.
        """

    position: Any
    shiftKey: int = 1

class MFnCircleSweepManip(MFnManip3D):
    """The CircleSweepManip allows the user to manipulate a point constrained to move around a circle, in order to specify a sweep angle. This manipulator generates a single floating point value corresponding to the sweep angle."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def angleIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """angleIndex() -> int

        Returns the index for the angle of CircleSweepManip. The data type corresponding to this index is a double.
        """

    def axisIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """axisIndex() -> int

        Returns the index for the axis of CircleSweepManip. The data type corresponding to this index is MFnNumericData.k3Double.
        """

    def centerIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """centerIndex() -> int

        Returns the index for the center of the CircleSweepManip. The data type corresponding to this index is MFnNumericData.k3Double.
        """

    def connectToAnglePlug(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectToAnglePlug(anglePlug) -> self

        Connect to the angle plug. The data type corresponding to the anglePlug is a double. (Note that MFnUnitAttribute.kAngle is used to specify an angle attribute.)

        * anglePlug (MPlug) - the angle plug
        """

    def create(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """create(manipName=None, angleName=None) -> MObject

        Creates a new CircleSweepManip.
        This function set's object is set to be the new manipulator.

        This method should only be used to create a non-composite CircleSweepManip.

        The name that appears in the feedback line is specified by the angleName argument.

        * manipName (string) - Name of the manip for UI purposes.
        * angleName (string) - Label for the angle value which appears in the feedback line.
        """

    def endCircleIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """endCircleIndex() -> int

        Returns the index for the end of the circle of CircleSweepManip. The data type corresponding to this index is a double.
        """

    endPoint: Any
    def setAngle(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setAngle(angle) -> self

        Sets the angle of the CircleSweepManip.

        * angle (MAngle) - the angle of the CircleSweepManip
        """

    def setCenterPoint(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setCenterPoint(centerPoint) -> self

        Sets the center point of the CircleSweepManip.

        * centerPoint (MPoint) - the center point of the CircleSweepManip
        """

    def setDrawAsArc(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setDrawAsArc(state) -> self

        Sets whether or not to draw as arc.

        * state (bool) - whether or not to draw as arc
        """

    def setNormal(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setNormal(normal) -> self

        Sets the normal of the CircleSweepManip.

        * normal (MVector) - the normal of the CircleSweepManip
        """

    def setRadius(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setRadius(radius) -> self

        Sets the radius of the CircleSweepManip.

        * radius (float) - the radius of the CircleSweepManip
        """

    def startCircleIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """startCircleIndex() -> int

        Returns the index for the start of the circle of CircleSweepManip. The data type corresponding to this index is a double.
        """

    startPoint: Any

class MFnCurveSegmentManip(MFnManip3D):
    """The CurveSegmentManip allows the user to manipulate two points on a curve, in order to specify a curve segment. This manipulator generates two floating point values, which correspond to the parameters of the start and end of the curve segment."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def connectToCurvePlug(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectToCurvePlug(curvePlug) -> self

        Connect to the curve plug. The data type corresponding to the curvePlug is MFnData.kNurbsCurve.

        * curvePlug (MPlug) - the curve plug
        """

    def connectToEndParamPlug(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectToEndParamPlug(endParamPlug) -> self

        Connect to the endParam plug. The data type corresponding to the endParamPlug is a double.

        * endParamPlug (MPlug) - the endParam plug
        """

    def connectToStartParamPlug(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectToStartParamPlug(startParamPlug) -> self

        Connect to the startParam plug. The data type corresponding to the startParamPlug is a double.

        * startParamPlug (MPlug) - the startParam plug
        """

    def create(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """create(manipName=None, startParamName=None, endParamName=None) -> MObject

        Creates a new CurveSegmentManip.
        This function set's object is set to be the new manipulator.

        This method should only be used to create a non-composite CurveSegmentManip.

        The names that appears in the feedback line are specified by the startParamName and endParamName arguments.

        * manipName (string) - Name of the manip for UI purposes.
        * startParamName (string) - Label for the startParam value which appears in the feedback line.
        * endParamName (string) - Label for the endParam value which appears in the feedback line.
        """

    def curveIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """curveIndex() -> int

        Returns the index of the curve. The data type corresponding to this index is MFnData.kNurbsCurve.
        """

    def endParamIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """endParamIndex() -> int

        Returns the index of the end parameter of the CurveSegmentManip. The data type corresponding this index is a double.
        """

    endParameter: Any
    def startParamIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """startParamIndex() -> int

        Returns the index of the start parameter of the CurveSegmentManip. The data type corresponding to this index is a double.
        """

    startParameter: Any

class MFnDirectionManip(MFnManip3D):
    """The DirectionManip allows the user to specify a direction, as defined by the vector from the start point to the manipulator position."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def connectToDirectionPlug(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectToDirectionPlug(directionPlug) -> self

        Connect to the direction plug. The data type corresponding to the directionPlug is MFnNumericData.k3Double.

        * directionPlug (MPlug) - the direction plug
        """

    def create(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """create(manipName=None, directionName=None) -> MObject

        Creates a new DirectionManip.
        This function set's object is set to be the new manipulator.

        This method should only be used to create a non-composite DirectionManip.

        The name that appears in the feedback line is specified by the directionName argument.

        * manipName (string) - Name of the manip for UI purposes.
        * directionName (string) - Label for the direction value which appears in the feedback line.
        """

    def directionIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """directionIndex() -> int

        Returns the index of the direction. The data type corresponding to this index is MFnNumericData.k3Double.
        """

    def endPointIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """endPointIndex() -> int

        Returns the index of the end point of the DirectionManip. The data type corresponding to this index is MFnNumericData.k3Double.
        """

    def setDirection(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setDirection(direction) -> self

        Sets the direction of the DirectionManip.

        * direction (MVector) - the direction of the DirectionManip
        """

    def setDrawStart(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setDrawStart(bool) -> self

        Sets whether or not to draw the start of the DirectionManip.
        The start of the DirectionManip is indicated by a grey dot.
        By default the start is not drawn.
        """

    def setNormalizeDirection(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setNormalizeDirection(bool) -> self

        Sets whether or not to the direction should be normalized.
        By default the direction is normalized.
        """

    def setStartPoint(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setStartPoint(startPoint) -> self

        Sets the start point of the DirectionManip.

        * startPoint (MPoint) - the start point of the DirectionManip
        """

    def startPointIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """startPointIndex() -> int

        Returns the index of the start point of the DirectionManip. The data type corresponding to this index is MFnNumericData.k3Double.
        """


class MFnDiscManip(MFnManip3D):
    """The DiscManip allows the user to rotate a disc in order to specify a rotation about an axis. This manipulator generates a single floating point value corresponding to the rotation."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def angleIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """angleIndex() -> int

        Returns the index of the angle. The data type corresponding to this index is a double.
        """

    def axisIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """axisIndex() -> int

        Returns the index of the axis of the DiscManip. The data type corresponding to this index is MFnNumericData.k3Double.
        """

    def centerIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """centerIndex() -> int

        Returns the index of the center of the DiscManip. The data type corresponding to this index is MFnNumericData.k3Double.
        """

    def connectToAnglePlug(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectToAnglePlug(directionPlug) -> self

        Connect to the angle plug. The data type corresponding to the anglePlug is a double. (Note that MFnUnitAttribute.kAngle is used to specify an angle attribute.)

        * anglePlug (MPlug) - the angle plug
        """

    def create(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """create(manipName=None, angleName=None) -> MObject

        Creates a new DiscManip.
        This function set's object is set to be the new manipulator.

        This method should only be used to create a non-composite DiscManip.

        The name that appears in the feedback line is specified by the angleName argument.

        * manipName (string) - Name of the manip for UI purposes.
        * angleName (string) - Label for the angle value which appears in the feedback line.
        """

    def setAngle(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setAngle(angle) -> self

        Sets the angle of the DiscManip.

        * angle (MAngle) - the angle of the DiscManip
        """

    def setCenterPoint(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setCenterPoint(centerPoint) -> self

        Sets the center point of the DiscManip.

        * centerPoint (MPoint) - the center point of the DiscManip
        """

    def setNormal(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setNormal(normal) -> self

        Sets the normal of the DiscManip.

        * normal (MVector) - the normal of the DiscManip
        """

    def setRadius(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setRadius(radius) -> self

        Sets the radius of the DiscManip.

        * radius (float) - the radius of the DiscManip
        """


class MFnDistanceManip(MFnManip3D):
    """The DistanceManip allows the user to manipulate a point that is constrained to move along a line. This manipulator generates a single floating point value. Scaling factors can be used to determine how the manipulator appears when it is drawn."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def connectToDistancePlug(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectToDistancePlug(directionPlug) -> self

        Connect to the distance plug. The data type corresponding to the distancePlug is a double. (Note that MFnUnitAttribute.kDistance is used to specify a distance attribute.)

        * distancePlug (MPlug) - the distance plug
        """

    def create(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """create(manipName=None, distanceName=None) -> MObject

        Creates a new DistanceManip.
        This function set's object is set to be the new manipulator.

        This method should only be used to create a non-composite DistanceManip.

        The name that appears in the feedback line is specified by the distanceName argument.

        * manipName (string) - Name of the manip for UI purposes.
        * distanceName (string) - Label for the distance value which appears in the feedback line.
        """

    def currentPointIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """currentPointIndex() -> int

        Returns the index of the current point of the DistanceManip. The data type corresponding to this index is MFnNumericData.k3Double.
        """

    def directionIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """directionIndex() -> int

        Returns the index of the direction. The data type corresponding to this index is MFnNumericData.k3Double.
        """

    def distanceIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """distanceIndex() -> int

        Returns the index of the distance. The data type corresponding to this index is a double.
        """

    isDrawLineOn: Any
    isDrawStartOn: Any
    scalingFactor: Any
    def setDirection(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setDirection(direction) -> self

        Sets the direction of the DistanceManip.

        * direction (MVector) - the direction of the DistanceManip
        """

    def setStartPoint(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setStartPoint(startPoint) -> self

        Sets the start point of the DistanceManip.

        * startPoint (MPoint) - the start point of the DistanceManip
        """

    def startPointIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """startPointIndex() -> int

        Returns the index of the start point of the DistanceManip. The data type corresponding to this index is MFnNumericData.k3Double.
        """


class MFnFreePointTriadManip(MFnManip3D):
    """The FreePointTriadManip provides a moveable point, which can be moved anywhere, and has axes for constrained x, y, and z movement and obeys grid snapping, point snapping, and curve snapping. The FreePointTriadManip generates the 3D position of the moveable point. It is useful for specifying the position of an object in space.

    Note that only the MFnNumericData::k3Double data type is supportedwhen connecting to a pointPlug via connectToPointPlug.
    """
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def connectToPointPlug(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectToPointPlug(pointPlug) -> self

        Connect to the point plug. The data type corresponding to the pointPlug is MFnNumericData.k3Double.

        * pointPlug (MPlug) - the point plug
        """

    def create(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """create(manipName=None, pointName=None) -> MObject

        Creates a new FreePointTriadManip.
        This function set's object is set to be the new manipulator.

        This method should only be used to create a non-composite FreePointTriadManip.

        The name that appears in the feedback line is specified by the pointName argument.

        * manipName (string) - Name of the manip for UI purposes.
        * pointName (string) - Label for the position value which appears in the feedback line.
        """

    isDrawAxesOn: Any
    isKeyframeAllOn: Any
    isSnapModeOn: Any
    def pointIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """pointIndex() -> int

        Returns the index of the point of the FreePointTriadManip. The data type corresponding to this index is MFnNumericData.k3Double.
        """

    def setDirection(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setDirection(direction) -> self

        Sets the orientation of the FreePointTriadManip.

        * direction (MVector) - the new direction for freePointTriadManip.
        """

    def setDrawArrowHead(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setDrawArrowHead(state) -> self

        Sets whether or not drawArrowHead is on.

        * state (bool) - whether or not drawArrowHead is on
        """

    def setGlobalTriadPlane(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setGlobalTriadPlane(whichPlane) -> self

        Sets which plane to use as the global triad plane. The global triad plane does not change until the context switches.

        * whichPlane (int) - which plane to use as the global triad plane

        Valid plane values:
          kYZPlane       Y-Z Plane
          kXZPlane       X-Z Plane
          kXYPlane       X-Y Plane
          kViewPlane     View Plane
        """

    def setPoint(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setPoint(pointValue) -> self

        Set the point manipulator value to the given vector.  This method can be called in the MPxManipContainer.connectToDependNode() method to set the initial position for the manipulator.

        * pointValue (MPoint) - The new value of the point manipValue
        """


class MFnManip3D(maya.api.OpenMaya.MFnTransform):
    """MFnManip3D allows the creation and manipulation of 3D manipulators."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    @staticmethod
    def deleteManipulator(*args: Unknown, **kwargs: Unknown) -> Any:
        """deleteManipulator(manip) -> None

        Delete a manipulator.  This method should be used to delete manipulators that have been created using base manipulator create() methods.

        * manip (MObject) - the manipulator to be deleted
        """

    @staticmethod
    def drawPlaneHandles(*args: Unknown, **kwargs: Unknown) -> Any:
        """drawPlaneHandles() -> bool

        This method returns the global option that says if the planar manipulator handles should be drawn or not.Setting this will affect the drawing of all manipulators that support the planar handles.
        """

    @staticmethod
    def globalSize(*args: Unknown, **kwargs: Unknown) -> Any:
        """globalSize() -> float

        Returns the global manipulator size.
        """

    @staticmethod
    def handleSize(*args: Unknown, **kwargs: Unknown) -> Any:
        """handleSize() -> float

        Returns the manipulator handle size.
        """

    isOptimizePlaybackOn: Any
    isVisible: Any
    @staticmethod
    def lineSize(*args: Unknown, **kwargs: Unknown) -> Any:
        """lineSize() -> float

        Returns the manipulator line size.
        """

    manipScale: Any
    def rotateXYZValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """rotateXYZValue(valIndex) -> MEulerRotation

        Gets the rotation for the active manipulator.

        * valIndex (int) - rotation index of the manipulator
        """

    @staticmethod
    def setDrawPlaneHandles(*args: Unknown, **kwargs: Unknown) -> Any:
        """setDrawPlaneHandles(bool) -> None

        Sets the global option to display planar handles or not on supported manipulators.
        """

    @staticmethod
    def setGlobalSize(*args: Unknown, **kwargs: Unknown) -> Any:
        """setGlobalSize(float) -> None

        Sets the global manipulator size.
        """

    @staticmethod
    def setHandleSize(*args: Unknown, **kwargs: Unknown) -> Any:
        """setHandleSize(float) -> None

        Sets the manipulator handle size.
        """

    @staticmethod
    def setLineSize(*args: Unknown, **kwargs: Unknown) -> Any:
        """setLineSize(float) -> None

        Sets the manipulator line size.
        """


class MFnPointOnCurveManip(MFnManip3D):
    """The PointOnCurveManip allows the user to manipulate a point constrained to move along a curve, in order to specify the "u" curve parameter value. This manipulator generates a single floating point value corresponding to the curve parameter.the sweep angle."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def connectToCurvePlug(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectToCurvePlug(curvePlug) -> self

        Connect to the curve plug. The data type corresponding to the curvePlug is MFnData::kNurbsCurve.

        * curvePlug (MPlug) - the curve plug
        """

    def connectToParamPlug(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectToParamPlug(paramPlug) -> self

        Connect to the param plug. The data type corresponding to the paramPlug is a double.

        * paramPlug (MPlug) - the param plug
        """

    def create(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """create(manipName=None, paramName=None) -> MObject

        Creates a new PointOnCurveManip.
        This function set's object is set to be the new manipulator.

        This method should only be used to create a non-composite PointOnCurveManip.

        The name that appears in the feedback line is specified by the paramName argument.

        * manipName (string) - Name of the manip for UI purposes.
        * paramName (string) - Label for the parameter value that appears in the feedback line.
        """

    def curveIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """curveIndex() -> int

        Returns the index of the curve. The data type corresponding to this index is MFnData::kNurbsCurve.
        """

    def curvePoint(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """curvePoint() -> MPoint

        Returns the curve point.
        """

    isDrawCurveOn: Any
    def paramIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """paramIndex() -> int

        Returns the index of the parameter of the PointOnCurveManip. The data type corresponding to this index is a double.
        """

    parameter: Any

class MFnPointOnSurfaceManip(MFnManip3D):
    """The PointOnSurfaceManip allows the user to manipulate a point constrained to move along a surface, in order to specify the (u, v) surface parameter values. This manipulator generates two floating point values corresponding to the surface (u, v) parameters."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def connectToParamPlug(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectToParamPlug(paramPlug) -> self

        Connect to the param plug. The data type corresponding to the paramPlug is MFnNumericData.k2Double.

        * paramPlug (MPlug) - the param plug
        """

    def connectToSurfacePlug(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectToSurfacePlug(surfacePlug) -> self

        Connect to the surface plug. The data type corresponding to the surfacePlug is MFnData.kNurbsSurface.

        * surfacePlug (MPlug) - the surface plug
        """

    def create(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """create(manipName=None, paramName=None) -> MObject

        Creates a new PointOnSurfaceManip.
        This function set's object is set to be the new manipulator.

        This method should only be used to create a non-composite PointOnSurfaceManip.

        The name that appears in the feedback line is specified by the paramName argument.

        * manipName (string) - Name of the manip for UI purposes.
        * paramName (string) - Label for the parameter value which appears in the feedback line
        """

    isDrawSurfaceOn: Any
    def paramIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """paramIndex() -> int

        Returns the index of the parameter of the PointOnSurfaceManip. The data type corresponding to this index is MFnNumericData.k2Double.
        """

    def setDrawArrows(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setDrawArrows(state) -> self

        Sets whether or not the arrows should be drawn.

        * state (bool) - whether or not the arrows should be drawn
        """

    def surfaceIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """surfaceIndex() -> int

        Returns the index of the surface. The data type corresponding to this index is MFnData.kNurbsSurface.
        """

    uParam: Any
    vParam: Any

class MFnRotateManip(MFnManip3D):
    """This class provides access to the built-in Maya rotate manipulator."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def connectToRotationCenterPlug(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectToRotationCenterPlug(rotationCenterPlug) -> self

        Create a 1-1 association of the rotation center on the manipulator and the rotationCenterPlug parameter.  When both the rotation center is attached to a plug and the displayWithNode() method has been called, the manipulator will display with the node regardless of the connection made to the rotation center.

        The plug must have a data type of MFnNumericData.k3Double.

        * rotationCenterPlug (MPlug) - The plug to connect the rotation center to
        """

    def connectToRotationPlug(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectToRotationPlug(rotationPlug) -> self

        Create a 1-1 connection from the rotation manipVal to the rotationPlug parameter.  Any changes to the rotation manipVal will be immediately reflected in the connected plug.  Connecting to the "rotation" plug on a transform node will produce similar behavior to the built-in rotation manipulator.

        The plug must have a data type of MFnNumericData.k3Double.

        * rotationPlug (MPlug) - The plug to connect the rotation value to
        """

    def create(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """create(manipName=None, rotationName=None) -> MObject

        Creates a new RotateManip, and attaches this function set to the new manipulator.

        This method should only be used to create a non-composite manipulator, meaning that the manipulator is standalone and not part of a container.

        When the manipulator is being used, the feedback line will display a string including rotationName, indicating that this manipulator is in use.

        * manipName (string) - Name of the manip for UI purposes.
        * rotationName (string) - Label for the rotation value displayed in the feedback line.
        """

    def displayWithNode(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """displayWithNode(node) -> self

        Configures the manipulator to display with the node, causing the position of the manipulator to follow the position of the node whenever the node is moved.  The node must be a DAG object.

        * node (MObject) - The node the manipulator should display with
        """

    isSnapModeOn: bool
    rotateMode: int
    def rotationCenterIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """rotationCenterIndex() -> int

        Returns the index of the rotation center for this manipulator.

        Note that the rotation center is only used for positioning the display of the manipulator, and has no effect on the rotation values generated by the manipulator.
        """

    def rotationIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """rotationIndex() -> int

        Returns the index of the rotation manipVal for the manipulator.  When plugToManip conversion functions are used to produce the rotation manipVal, the manipulator data must be of the type MFnNumericData.k3Double, with X,Y, and Z rotations given in radians.  This is easily accomplished by using the MEulerRotation class to manage the rotations.
        """

    def setInitialRotation(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setInitialRotation(rotation) -> self

        Sets the initial rotation for the rotate manipulator.  Setting the initial rotation will prevent the manipulator from jumping back to the default rotation when there is already an existing rotation on the target plug.

        * rotation (MEulerRotation) - The initial rotation
        """

    def setRotationCenter(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setRotationCenter(rotationCenter) -> self

        Sets the position of the rotation center for the manipulator.

        The value set by this method is ignored if a plug has been connected to the rotationCenterPlug. This value is only relevant when there is no plug connection to rotationCenterPlug nor node associated with the manip (see connectToRotationCenterPlug and displayWithNode, respectively).

        Note that the rotation center is only used for positioning the display of the manipulator, and has no effect on the rotation values generated by the manipulator.

        * rotationCenter (MPoint) - The world space position of the rotation center.
        """

    snapIncrement: float

class MFnScaleManip(MFnManip3D):
    """This class provides access to the built-in Maya scale manipulator."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def connectToScaleCenterPlug(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectToScaleCenterPlug(scaleCenterPlug) -> self

        Create a 1-1 association of the scale center on the manipulator and the scaleCenterPlug parameter.  When both the scale center is attached to a plug and the displayWithNode() method has been called, the manipulator will display with the node regardless of the connection made to the scale center.

        The plug must have a data type of MFnNumericData.k3Double.

        * scaleCenterPlug (MPlug) - The plug to connect the scale center to
        """

    def connectToScalePlug(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectToScalePlug(scalePlug) -> self

        Create a 1-1 connection from the scale manipVal to the scalePlug parameter.  Any changes to the scale manipVal will be immediately reflected in the connected plug.  Connecting to the "scale" plug on a transform node will produce similar behavior to the built-in scale manipulator.

        The plug must have a data type of MFnNumericData.k3Double.

        * scalePlug (MPlug) - The plug to connect the scale value to
        """

    def create(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """create(manipName=None, scaleName=None) -> MObject

        Creates a new ScaleManip, and attaches this function set to the new manipulator.

        This method should only be used to create a non-composite manipulator, meaning that the manipulator is standalone and not part of a container.

        When the manipulator is being used, the feedback line will display a string including scaleName, indicating that this manipulator is in use.

        * manipName (string) - Name of the manip for UI purposes.
        * scaleName (string) - Label for the scale value displayed in the feedback line.
        """

    def displayWithNode(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """displayWithNode(node) -> self

        Configures the manipulator to display with the node, causing the position of the manipulator to follow the position of the node whenever the node is moved.  The node must be a DAG object.

        * node (MObject) - The node the manipulator should display with
        """

    isSnapModeOn: bool
    orientation: Any
    orientationMode: Any
    def scaleCenterIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """scaleCenterIndex() -> int

        Returns the index of the scale center manipVal for this manipulator.

        Note that the scale center is only used for display of the manipulator and has no effect on scale values produced by the manipulator.
        """

    def scaleIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """scaleIndex() -> int

        Returns the index of the scale manipVal for this manipulator.
        """

    def setInitialScale(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setInitialScale(scale) -> self

        Sets the initial scale for the scale manipulator.  Setting the initial scale will prevent the manipulator from jumping back to the default scale when there is already an existing scale on the target plug.

        * scale (MVector) - The initial scale
        """

    snapIncrement: float

class MFnStateManip(MFnManip3D):
    """The StateManip allows the user to switch between multiple states. It is drawn as a circle with a notch. Each click on the circle increments the value of the state (modulo the maximum number of states). This manipulator generates an integer value corresponding to the state of the manip."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def connectToStatePlug(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectToStatePlug(statePlug) -> self

        Connect to the state plug. The data type corresponding to the statePlug is a int integer.

        * statePlug (MPlug) - the state plug
        """

    def create(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """create(manipName=None, stateName=None) -> MObject

        Creates a new StateManip.
        This function set's object is set to be the new manipulator.

        This method should only be used to create a non-composite StateManip.

        The name that appears in the feedback line is specified by the stateName argument.

        * manipName (string) - Name of the manip for UI purposes.
        * stateName (string) - Label for the state value which appears in the feedback line.
        """

    maxStates: Any
    def positionIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """positionIndex() -> int

        Returns the index of the position of the StateManip. The data type corresponding to this index is MFnNumericData.k3Double.
        """

    def setInitialState(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setInitialState(initialState) -> self

        Sets the initial state of the StateManip.

        * initialState (int) - initial state of the StateManip
        """

    def state(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """state() -> int

        Returns the current state.
        """

    def stateIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """stateIndex() -> int

        Returns the index of the state. The data type corresponding to this index is a int integer.
        """


class MFnToggleManip(MFnManip3D):
    """The ToggleManip allows the user to switch between two modes or some on/off state. It is drawn as a circle with or without a dot. When the mode is on, the dot is drawn in the circle; when the mode is off, the circle is drawn without the dot. This manipulator generates a boolean value corresponding to whether or not the mode is on or off."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def connectToTogglePlug(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectToTogglePlug(togglePlug) -> self

        Connect to the toggle plug. The data type corresponding to the togglePlug is a boolean value.

        * togglePlug (MPlug) - the toggle plug
        """

    def create(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """create(manipName=None, toggleName=None) -> MObject

        Creates a new ToggleManip.
        This function set's object is set to be the new manipulator.

        This method should only be used to create a non-composite ToggleManip.

        The name that appears in the feedback line is specified by the toggleName argument.

        * manipName (string) - Name of the manip for UI purposes.
        * toggleName (string) - Label for the toggle value which appears in the feedback line.
        """

    direction: Any
    def directionIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """directionIndex() -> int

        Returns the index of the direction. The data type corresponding to this index is MFnNumericData.k3Double.
        """

    length: Any
    def lengthIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """lengthIndex() -> int

        Returns the index of the length of the ToggleManip. The data type corresponding to this index is a double.
        """

    startPoint: Any
    def startPointIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """startPointIndex() -> int

        Returns the index of the start point of the ToggleManip. The data type corresponding to this index is MFnNumericData.k3Double.
        """

    toggle: Any
    def toggleIndex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """toggleIndex() -> int

        Returns the index of the toggle of the ToggleManip. The data type corresponding to this index is a boolean.
        """


class MHWShaderSwatchGenerator(maya.api.OpenMayaRender.MSwatchRenderBase):
    """Hardware shader swatch generator utility class."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    @staticmethod
    def createObj(*args: Unknown, **kwargs: Unknown) -> Any:
        """createObj(obj, renderObj, res) -> MSwatchRenderBase

        Class constructor.
        Saves the Node object and image resolution as data members for future use.

        * obj (MObject) - The node object for which the swatch needs to be generated.
        * renderObj (MObject) - The node used to actually compute the swatch. In most situations, this can be the same as <b>obj</b>. This parameter can be used to request the computation of the swatch on another node, and display the swatch on the obj node.* resolution (int) - The expected resolution of the swatch image.
        """

    def doIteration(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doIteration() -> bool

        Method called from the MSwatchRenderRegister for generation of swatch image. The doIteration function is called repeatedly (during idle events) until it returns true. Using this swatch image can be generated in stages.

        This method should be overridden in derived classes which can compute the swatches in several steps.

        Returns False as long as the swatch computation is not completed.
        """

    @staticmethod
    def getSwatchBackgroundColor(*args: Unknown, **kwargs: Unknown) -> Any:
        """getSwatchBackgroundColor() -> MColor

        Returns the default background color for the hardware rendered swatch.
        """

    @staticmethod
    def initialize(*args: Unknown, **kwargs: Unknown) -> Any:
        """initialize() -> string

        This method sets a swatch name, and registers a new swatch generator creation function for the swatch name.
        The string returned from this method can be used for node classification purpose.
        """


class MManipData:
    """Class that encapsulates manipulator data."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def asBool(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """asBool() -> bool

        Returns the manipulator data as a bool
        """

    def asDouble(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """asDouble() -> float

        Returns the manipulator data as a double
        """

    def asFloat(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """asFloat() -> float

        Returns the manipulator data as a float
        """

    def asLong(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """asLong() -> int

        Returns the manipulator data as a long
        """

    def asMObject(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """asMObject() -> int

        Returns the manipulator data as an MObject.
        The MObjects returned from this method are created and used
        by MFnData or classes derived from MFnData.
        """

    def asShort(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """asShort() -> int

        Returns the manipulator data as a short
        """

    def asUnsigned(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """asUnsigned() -> int

        Returns the manipulator data as a unsigned
        """

    def isSimple(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """isSimple() -> bool

        Returns whether or not the manipulator data is simple or complex.
        Simple data is used to represent bool, int, and float types.
        Complex data is used to represent MObjects created by MFnData,
        or classes derived from MFnData.
        """


class MMaterial:
    """This class is used in the draw functions of user defined shapes (see MPxSurfaceShapeUI) for setting up and querying materials in shaded mode drawing."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def applyTexture(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """applyTexture(view, data) -> self

        For materials that have texture, this method must be used before the OpenGL drawing to apply the texture to the current view.
        This method should be called from within your MPxSurfaceShapeUI.draw() method.

        * view (M3dView) - the view in which the textured drawing is to take place
        * data (MDrawData) - the draw data from the draw request
        """

    @staticmethod
    def defaultMaterial(*args: Unknown, **kwargs: Unknown) -> Any:
        """defaultMaterial() -> MMaterial

        Get the default material. There will always be a default material in the scene and therefore the result of this function should always succeed.  The default material will correspond to the initialShadingGroup node that is in the scene.
        """

    def evaluateDiffuse(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """evaluateDiffuse() -> self

        Perform necessary evaluation to be able to get diffuse back.
        """

    def evaluateEmission(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """evaluateEmission() -> self

        Perform necessary evaluation to be able to get emission back.
        """

    def evaluateMaterial(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """evaluateMaterial(view, path) -> self

        Evaluate a material. Must be called before evaluating or getting any material properties.

        * view (M3dView) - the view
        * path (MDagPath) - path to the object
        """

    def evaluateShininess(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """evaluateShininess() -> self

        Perform necessary evaluation to be able to get shininess back.
        """

    def evaluateSpecular(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """evaluateSpecular() -> self

        Perform necessary evaluation to be able to get specular back.
        """

    def evaluateTexture(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """evaluateTexture(data) -> self

        Evaluate texturing related information. Must be called before getting any texture properties such as getHasTransparency(), getTextureTransformation() and applyTexture().

        This method should be called from MPxSurfaceShapeUI.getDrawRequests().
        The draw data argument is the MDrawData for the request that will carry the texture information to the MPxSurfaceShapeUI.draw() method.

        * data (MDrawData) - draw request data to carry the texture information
        """

    def getDiffuse(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getDiffuse() -> MColor

        Get the GL diffuse color.
        """

    def getEmission(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getEmission() -> MColor

        Get the GL emission color.
        """

    def getHasTransparency(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getHasTransparency() -> bool

        Returns True if material or texture has transparency, False otherwise.
        """

    def getHwShaderNode(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getHwShaderNode() -> MPxHwShaderNode

        Get the hardware shader node.
        """

    def getShininess(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getShininess() -> float

        Get the GL shininess.
        """

    def getSpecular(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getSpecular() -> MColor

        Get the GL specular color.
        """

    def getTextureTransformation(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getTextureTransformation(data, texXform) -> self
        getTextureTransformation(data) -> [float, float, float, float, float, float]

        Get the current textures transformation.

        * data (MDrawData) - the draw data from the draw request
        * texXform [OUT] (MMatrix) - storage for the texture transformation

        Or
        * data (MDrawData) - the draw data from the draw request
        Returns the transformations values:
           rotateUV (float) - storage for rotatation value of the UV coordinates
           scaleU (float) - storage for u scale value
           scaleV (float) - storage for v scale value
           translateU (float) - storage for u translation value
           translateV (float) - storage for v translation value
           rotateFrame (float) - storage for rotatation value of the frame coordinates
        """

    kAmbientColor: int = 2
    kBumpMap: int = 4
    kColor: int = 0
    kCosinePower: int = 10
    kDiffuse: int = 5
    kEccentricity: int = 11
    kHighlightSize: int = 8
    kIncandescence: int = 3
    kReflectedColor: int = 15
    kReflectivity: int = 14
    kRoughness: int = 7
    kSpecularColor: int = 13
    kSpecularRollOff: int = 12
    kTransluscence: int = 6
    kTransparency: int = 1
    kWhiteness: int = 9
    def materialIsTextured(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """materialIsTextured() -> bool

        Returns True if the material is textured, False otherwise.
        """

    def setMaterial(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setMaterial(path, hasTransparency) -> self

        Set the current GL material.

        * path (MDagPath) - path to the object
        * hasTransparency (bool) - whether the material has transparency
        """

    def shadingEngine(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """shadingEngine() -> MObject

        Get the shading engined associated with this material.
        """

    def textureImage(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """textureImage(image, color, chan, dagPath, xRes=-1, yRes=-1) -> self

        For materials that have texture, this method will attempt to retrieve the pixel map for a given mapped channel of that material.
        Will fails If the channel is not mapped.

        The material types that can be queried include:
          - Lambert
          - Phong
          - PhongE
          - Anisotropic
          - Blinn

        Currently only channels mapped to single file textures is supported.

        * image [OUT] (MImage) - The image retrieved. If no image could be retrieve, the value will not change.
        * color [OUT] (MColor) - Either the mapped or unmapped color. If the channel is mapped then an RGBA value of (1,1,1,1) will be returned, otherwise the unmapped channel's current color value will be returned.
        * chan (int) - Texture channel to check.
        * dagPath (MDagPath) - Optional dag path to object. An object path is required to produce texture maps from non-2D procedural textures.
        * xRes (int) - Optional width of image to create. The minimal allowed value is 2. This parameter only applies to procedural textures. The dimension in X will be 128 by default, if a value less than 2 is specified.
        * yRes (int) - Optional height of image to create. The minimal allowed value is 2. This parameter only applies to procedural textures. The dimension in Y will be 128 by default, if a value less than 2 is specified.

        Valid Texture channel:
          kColor
          kTransparency
          kAmbientColor
          kIncandescence
          kBumpMap
          kDiffuse
          kTransluscence
          kRoughness           PhongE only
          kHighlightSize       PhongE only
          kWhiteness           PhongE only
          kCosinePower         Phong only
          kEccentricity        Blinn only
          kSpecularRollOff     Blinn only
          kSpecularColor       Blinn and Phong(E) only
          kReflectivity        Blinn and Phong(E) only
          kReflectedColor      Blinn and Phong(E) only
        """


class MMaterialArray:
    """An array of MMaterial."""
    def __getitem__(self, key: Unknown, /) -> Any:
        """Return self[key]."""

    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self, /) -> Any:
        """Return len(self)."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def append(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """append(element) -> self

        Adds a new element to the end of the array.

        * element (MMaterial) - the value for the new last element.
        """

    def clear(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """clear() -> self

        Clear the contents of the array. After this operation the length will be 0.  This does not change the amount of memory allocated to the array, only the number of valid elements in it.
        """

    def copy(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """copy(source) -> self

        Copy the contents of the source array to this array.

        * source (MMaterialArray) - array to copy from.
        """

    def insert(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """insert(element, index) -> self

        Inserts a new value into the array at the given index. The initial element at that index, and all following elements, are shifted towards the last.

        * element (MMaterial) - the new value to insert into the array.
        * index (int) - the index of the element to set.
        """

    def remove(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """remove(index) -> self

        Removes the element in the array at the given index.

        * index (int) - the index of the element to remove.
        """

    def set(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """set(element, index) -> self

        Sets the value of the specified element to the given attribute spec.

        * element (MMaterial) - the new value for the specified element.
        * index (int) - the index of the element to be set.
        """

    def setLength(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setLength(length) -> self

        Set the length of the array. This will grow and shrink the array as desired. Elements that are grown have uninitialized values, while those which are shrunk will lose the data contained in the deleted elements

        * length (int) - the new size of the array.
        """

    sizeIncrement: int

class MPaintMessage(maya.api.OpenMaya.MMessage):
    """Class used to register callbacks for paint related messages."""
    @staticmethod
    def addVertexColorCallback(*args: Unknown, **kwargs: Unknown) -> Any:
        """addVertexColorCallback(function, clientData=None) -> id

        Adds a new callback on vertex color paint.

        Note: the 'colors' parameter supplied to the callback function contains a color per vertex, even if the type of the component being painted is faces. To interpret the colors when faces are being painted, it will be necessary to query the vertex count of each face and step over that many vertices while iterating the array.

        The callback function will be passed any client data that was
        provided when the callback was registered.

         * function - callable which will be passed:
           The DAG path of the object being painted (MDagPath)
           The components (e.g. vertices, faces) being painted (MObject)
           The plug being painted (MPlug)
           The colors that were applied to the components (MColorArray)
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """


class MPanelCanvas:
    """Provides API extension to panel canvas.

    __init__()
    Initializes a new MPanelCanvas.
    """
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addPrimitive(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addPrimitive( int, int )

        Add the primitive referred to by the given id to the list of
        primitives to be drawn at the given layer.
        Return: None
        """

    def createFloatVertexBuffer(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """createFloatVertexBuffer( tVals, yVals, colors ) -> int

        Create a vertex buffer with float values as the x-coordinate.
        An id referring to the created buffer is returned. The values
        are passed as arrays of float values
        Return: int
        """

    def createPrimitive(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """createPrimitive( primType, bufferId, startIndex, numVertices, props ) -> int

        Create a primitive of the given type using the vertex buffer
        specified by the given id, the range of vertices used from
        the buffer, and a drawing style. An id referring to the
        created primitive is returned.
        Return: int
        """

    def createTimeVertexBuffer(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """createTimeVertexBuffer( tVals, yVals, colors ) -> int

        Create a vertex buffer with time values as the x-coordinate.
        An id referring to the created buffer is returned. The values
        are passed as arrays of OpenMaya.MTime values
        Return: int
        """

    def destroyPrimitive(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """destroyPrimitive( primitiveId )

        Destroy the primitive referred to by the given id.
        Return: None
        """

    def destroyVertexBuffer(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """destroyVertexBuffer( bufferId )

        Destroy the vertex buffer referred to by the given id.  If the.
        buffer is being used by a primitive, an error will be generated.
        Return: None
        """

    def isAutoRefresh(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """isAutoRefresh() -> bool

        Returns whether the associated editor will automatically refresh.


        Return: bool
        """

    def isLayerVisible(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """isLayerVisible( int) -> bool

        Return whether the given layer is visible.
        Return: bool
        """

    def isValid(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """isValid() -> bool

        Returns True if MPanelCanvas has a valid pointer to a Graph
        Editor object, False otherwise.
        Return: bool
        """

    kGraphEditorAxisLabels: int = 1000
    kGraphEditorBackground: int = 0
    kGraphEditorCurveNames: int = 3000
    kGraphEditorCurves: int = 2000
    kGraphEditorFirstDefaultDraw: int = 100
    kGraphEditorGrid: int = 100
    kGraphEditorLastDefaultDraw: int = 10000
    kGraphEditorOverlayTexture: int = 10000
    kGraphEditorRetimeToolText: int = 5000
    kGraphEditorTimeMarker: int = 4000
    kGraphEditorUndefined: int = -1
    def refresh(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """refresh()

        Force the associated Graph Editor to refresh
        Return: None
        """

    def registerDrawUICallback(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """registerDrawUICallback( layer, cb, clientData ) -> callbackId

        Register a callback to be called when the given panel is drawing
        the given layer. An id to the callback is returned. The function
        takes two parameters, an instance of an OpenMayaRender.MUIDrawManager
        and whatever client data was passed to this method.
        Return: int
        """

    def removePrimitive(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """removePrimitive( int, int )

        Remove the primitive referred to by the given id from the list of
        primitives to be drawn at the given layer. The primitive will not
        be destroyed.
        Return: None
        """

    def setAutoRefresh(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setAutoRefresh()

        Set whether the associated editor will be automatically refreshed.
        Initially, automatic refresh is enabled.
        Return: None
        """

    def setLayerVisible(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setLayerVisible( int, bool )

        Set whether the given layer will be drawn. All layers are
        initially set to be visible. Only user defined layers may have
        their visibility set.
        Return: None
        """

    def supportsUIDrawing(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """supportsUIDrawing() -> bool

        Returns whether the attached panel control supports drawing
        primitives in screen space. If such drawing is not supported,
        the registerDrawUICallback () method will throw an exception.

        Note that the Graph Editor will return false if it exists, but the
        panel for drawing has not yet been created (e.g., for the default
        Graph Editor when it has not yet been opened, but exists by default).
        Return: bool
        """

    def unregisterDrawUICallback(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """unregisterDrawUICallback( callbackId )

         Unregister the callback specified by the given id.
        Return: None
        """


class MPanelCanvasInfo:
    """Provides API extension to get/set panel canvas information.

    __init__()
    Initializes a new MPanelCanvasInfo.
    """
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def getViewportBounds(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getViewportBounds()

        Returns an array of four values representing the corners of the
        viewing region: [left, right, bottom, top].
        Return: float[]
        """

    def getViewportSize(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getViewportSize()

        Returns an array of two values representing the size of the
        viewing region: [width, height].
        Return: int[]
        """

    def name(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """name() -> MString

        Return the name of the currently attached panel.
        Return: MString
        """

    def setViewportBounds(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setViewportBounds( bounds )

        Set the bounds of the editor's viewing region. The passed.
        bounds are specified as an array of four values: [left, right,
        bottom, top].
        Return: None
        """

    def supportsUIDrawing(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """supportsUIDrawing() -> bool

        Returns whether the attached panel control supports drawing
        primitives in screen space. If such drawing is not supported,
        the registerDrawUICallback () method will throw an exception.

        Note that the Graph Editor will return false if it exists, but the
        panel for drawing has not yet been created (e.g., for the default
        Graph Editor when it has not yet been opened, but exists by default).
        Return: bool
        """


class MPxContext:
    """This is the base class for user defined drag and drop behaviors."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def abortAction(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """abortAction() -> None

        This method is called when the abort key is pressed.
        The default abort key in Maya is the <b>escape</b> key.
        Users can override this method if they wish to perform
        certain operations when the abort key is pressed.
        """

    def addManipulator(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addManipulator(manipulator) -> None

        This method adds a manipulator to the context.

        * manipulator (MObject) - the manipulator to be added to the context.
        """

    def argTypeNumericalInput(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """argTypeNumericalInput(index) -> MSyntax.MArgType

        This method is used by the feedback line to determine what units to display.
        Users should override this method to return the appropriate
        argument type for the given index of the numeric input field.
        Specifically, this method should be overridden to return one of the following:

            <b>MSyntax.kNoArg</b> for no argument
            <b>MSyntax.kDistance</b> for linear units
            <b>MSyntax.kAngle</b> for angular units

        * index (int) - the index of the numerical input whose argument type is requested.
        """

    def beginMarquee(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """beginMarquee(event) -> self

        Start drawing a dragged out marquee box.
        A marquee box is a rectangular area of the screen specified by
        two points representing opposite corners of the rectangle.
        Marquee's are commonly used in the selection of multiple items from
        a region of the screen. The marquee rectangle acts as a guideline
        for the region of the screen that will be effected.

        * event (MEvent) - current event information.
        """

    def completeAction(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """completeAction() -> None

        This method is called when the complete key is pressed.
        The default complete key in Maya is the <b>enter</b> key.
        Users can override this method if a tool has several steps.
        For example, a tool may have several steps where the user must
        select objects and then press the completion key before proceeding.
        """

    def deleteAction(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """deleteAction() -> None

        This method is called when the delete or backspace key is pressed.
        The default behaviour for this method is to delete the items on the
        current selection list.
        Users can override this method if they wish to do anything else
        when this event occurs.
        """

    def deleteManipulators(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """deleteManipulators() -> None

        This method deletes all the manipulators that belong
        to the context.
        """

    def doDrag(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doDrag(event, drawMgr, context) -> None

        This method is called when a mouse drag event occurs.
        The base method does nothing and should be overridden if
        the user needs to do anything during a mouse drag.

        This method is called only when in Viewport 2.0. MUIDrawManager
        must be used for any viewport drawing done in this method. Direct
        calls to OpenGL or DirectX are unsupported and may result in instability
        or unpredictable behavior.

        MUIDrawManager allows for drawing primitives in the 3D modeling space.
        Those primitives will then be projected onto a 2D overlay plane before being
        displayed.

        The <b>event</b> can be used to get more explicit information
        about the drag such as the cursor location. See MEvent for
        more information.

        * event (MEvent) - The button press event information.
        * drawMgr (MHWRender::MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry including text.
        * context (MHWRender::MFrameContextFrame) - level context information.
        """

    def doDragLegacy(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doDragLegacy(event) -> None

        This method is called when a mouse drag event occurs.
        The base method does nothing and should be overridden if
        the user needs to do anything during a mouse drag.

        This method is called only when it is in either default viewport renderer
        or hardware viewport renderer, not viewport 2.0.

        The <b>event</b> can be used to get more explicit information
        about the drag such as the cursor location. See MEvent for
        more information.

        * event (MEvent) - The button drag event information.
        """

    def doEnterRegion(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doEnterRegion(event) -> None

        This method is called when a mouse enters the viewport.
        The base method does nothing and should be overridden if
        the user needs to do anything during an enter event.

        The <b>event</b> can be used to get more explicit information
        about the event such as the cursor location. See MEvent for
        more information.

        * event (MEvent) - The event information.
        """

    def doExitRegion(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doExitRegion(event) -> None

        This method is called when a mouse exits the viewport.
        The base method does nothing and should be overridden if
        the user needs to do anything during an exit event.

        The <b>event</b> can be used to get more explicit information
        about the event such as the cursor location. See MEvent for
        more information.

        * event (MEvent) - The event information.
        """

    def doHold(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doHold(event, drawMgr, context) -> None

        This method is called when a mouse button is pressed but
        before the mouse is dragged.
        The base method does nothing and should be overridden if the user needs
        to do anything on a button hold.

        This method is called only when in Viewport 2.0. MUIDrawManager
        must be used for any viewport drawing done in this method. Direct
        calls to OpenGL or DirectX are unsupported and may result in instability
        or unpredictable behavior.

        MUIDrawManager allows for drawing primitives in the 3D modeling space.
        Those primitives will then be projected onto a 2D overlay plane before being
        displayed.

        The <b>event</b> can be used to get more explicit information
        about the hold such as the button number. See MEvent for
        more information.

        * event (MEvent) - The button press event information.
        * drawMgr (MHWRender::MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry including text.
        * context (MHWRender::MFrameContextFrame) - level context information.
        """

    def doHoldLegacy(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doHoldLegacy(event) -> None

        This method is called when a mouse button is pressed but
        before the mouse is dragged.
        The base method does nothing and should be overridden if the user needs
        to do anything on a button hold.

        This method is called only when it is in either default viewport renderer
        or hardware viewport renderer, not viewport 2.0.

        The <b>event</b> can be used to get more explicit information
        about the hold such as the button number. See MEvent for
        more information.

        * event (MEvent) - The button hold event information.
        """

    def doPress(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doPress(event, drawMgr, context) -> None

        This method is called when any mouse button is pressed.
        The base method does nothing and should be overridden if
        the user needs to do anything on a button press.

        This method is called only when in Viewport 2.0. MUIDrawManager
        must be used for any viewport drawing done in this method. Direct
        calls to OpenGL or DirectX are unsupported and may result in instability
        or unpredictable behavior.

        MUIDrawManager allows for drawing primitives in the 3D modeling space.
        Those primitives will then be projected onto a 2D overlay plane before being
        displayed.

        The event can be used to get more explicit information
        about the press such as the button number. See MEvent for
        more information.

        * event (MEvent) - The button press event information.
        * drawMgr (MHWRender::MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry including text.
        * context (MHWRender::MFrameContextFrame) - level context information.
        """

    def doPressLegacy(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doPressLegacy(event) -> None

        This method is called when any mouse button is pressed.
        The base method does nothing and should be overridden if
        the user needs to do anything on a button press.

        This method is called only when it is in either default viewport renderer
        or hardware viewport renderer, not viewport 2.0.

        The <b>event</b> can be used to get more explicit information
        about the press such as the button number. See MEvent for
        more information.

        * event (MEvent) - The button press event information.
        """

    def doPtrMoved(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doPtrMoved(event, drawMgr, context ) -> None

        This method is called when a mouse move event occurs.
        The base method does nothing and should be overridden if
        the user needs to do anything during a mouse drag.

        This method is called only when in Viewport 2.0. MUIDrawManager
        must be used for any viewport drawing done in this method. Direct
        calls to OpenGL or DirectX are unsupported and may result in instability
        or unpredictable behavior.

        MUIDrawManager allows for drawing primitives in the 3D modeling space.
        Those primitives will then be projected onto a 2D overlay plane before being
        displayed.

        The <b>event</b> can be used to get more explicit information
        about the drag such as the cursor location. See MEvent for
        more information.

        * event (MEvent) - The button press event information.
        * drawMgr (MHWRender::MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry including text.
        * context (MHWRender::MFrameContextFrame) - level context information.
        """

    def doPtrMovedLegacy(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doPtrMovedLegacy(event) -> None

        This method is called when a mouse drag event occurs.
        The base method does nothing and should be overridden if
        the user needs to do anything during a mouse drag.

        This method is called only when it is in either default viewport renderer
        or hardware viewport renderer, not viewport 2.0.

        The <b>event</b> can be used to get more explicit information
        about the drag such as the cursor location. See MEvent for
        more information.

        * event (MEvent) - The button press event information.
        """

    def doRelease(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doRelease(event, drawMgr, context) -> None

        This method is called when any mouse button is released.
        The base method does nothing and should be overridden if
        the user needs to do anything on a button release.

        This method is called only when in Viewport 2.0. MUIDrawManager
        must be used for any viewport drawing done in this method. Direct
        calls to OpenGL or DirectX are unsupported and may result in instability
        or unpredictable behavior.

        MUIDrawManager allows for drawing primitives in the 3D modeling space.
        Those primitives will then be projected onto a 2D overlay plane before being
        displayed.

        The <b>event</b> can be used to get more explicit information
        about the release such as the button number. See MEvent for
        more information.

        * event (MEvent) - The button press event information.
        * drawMgr (MHWRender::MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry including text.
        * context (MHWRender::MFrameContextFrame) - level context information.
        """

    def doReleaseLegacy(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doReleaseLegacy(event) -> None

        This method is called when any mouse button is released.
        The base method does nothing and should be overridden if
        the user needs to do anything on a button release.

        This method is called only when it is in either default viewport renderer
        or hardware viewport renderer, not viewport 2.0.

        The <b>event</b> can be used to get more explicit information
        about the release such as the button number. See MEvent for
        more information.

        * event (MEvent) - The button release event information.
        """

    def dragMarquee(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """dragMarquee(event) -> self

        Draws a rectangle representing the dragged out area initiated with
        the beginMarquee method.

        * event (MEvent) - current event information.
        """

    def drawFeedback(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """drawFeedback(event, drawMgr, context ) -> None

        This method is called to draw primitives when your context is activated

        This method is called only when using Viewport 2.0. MUIDrawManager
        must be used for any viewport drawing done in this method. Direct
        calls to OpenGL or DirectX are unsupported and may result in instability
        or unpredictable behavior.

        MUIDrawManager allows for drawing primitives in the 3D modeling space.
        Those primitives will then be projected onto a 2D overlay plane before being
        displayed.

        * drawMgr (MHWRender::MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry including text.
        * context (MHWRender::MFrameContextFrame) - level context information.
        """

    def feedbackNumericalInput(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """feedbackNumericalInput() -> bool

        This method is called to update the numerical feedback.
        The format and values for the feedback line can be set through the
        methods in MFeedbackLine, specifically setFormat and setValue.
        The return value should indicate whether or not the numerical feedback
        has been provided.  The default return value is false.
        """

    def helpStateHasChanged(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """helpStateHasChanged(event) -> None

        This method is called whenever the help state may need to be
        updated.
        The base method does nothing and should be overriden if
        the user needs to change the help information based on events.

        The <b>event</b> can be used to get more explicit information
        about the event. See MEvent for more information.

        * event (MEvent) - The event information.
        """

    def image(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """image(index) -> string

        This method is used to retrieve an XPM icon image that has
        previously been set for this tool context. This icon image will be
        used to represent this tool context in various places including
        the tool bar and can be queried from mel using the contextInfo
        command.

        * index (ImageIndex) - the index of the image being retrieved; three image
        representations are permitted: kImage1, kImage2, kImage3.
        """

    def inAlternateContext(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """inAlternateContext() -> bool

        This method is called to determine if an alternate context is active.
        For example, this method returns true if the user moves the camera
        while the current context is active.
        """

    kImage1: int = 0
    kImage2: int = 1
    kImage3: int = 2
    def newToolCommand(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """newToolCommand() -> MPxToolCommand

        Create a new instance of the tool command associated with this context.
        The tool command (derived from MPxToolCommand) is the command that was
        registered along with the context command in.

        Returns a new instance of the MPxToolCommand.
        """

    def processNumericalInput(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """processNumericalInput(values, flags, isAbsolute) -> bool

        This method processes the input from the numerical input field.
        Users can override this method if they wish to process numerical input.
        For a given entry in the numeric input field, if the user types a dot '.',
        this indicates that the entry should not be modified.
        The overridden version of this method should take this into account
        using the ignoreEntry method with the flags that are passed in.
        The overridden version of this method should also process the numeric
        input as an absolute input or relative input depending on whether
        the isAbsolute flag is true or not.
        The return value should indicate whether or not the numerical input has
        been processed.

        * values (MDoubleArray) - the values from the numerical input field.
        * flags (MIntArray) - used in conjunction with the ignoreEntry method,
        determines whether or not a given entry should be ignored.
        * isAbsolute (bool) - whether or not the input should be interpreted as absolute.
        """

    def releaseMarquee(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """releaseMarquee(event) -> (top, left, bottom, right)

        End the marquee drawing cycle and return the coordinates corresponding to
        the dragged out area.
        The rectangular guideline representing the dragged area is cleared.

        Returns a tuple consisting of the top, left, bottom, and right corners of the marquee area.
        * event (MEvent) - current event information.
        """

    def setCursor(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setCursor(newCursor) -> self

        Set the cursor used by the context to the MCursor that is passed in.

        * newCursor (MCursor) - The new cursor.
        """

    def setHelpString(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setHelpString(str) -> self

        Set the help string to the given MString.
        This string will appear in the help line in Maya.

        * str (string) - The new help string.
        """

    def setImage(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setImage(image, index) -> self

        This method is used to set an XPM icon image that is to be
        used to represent this tool context in various places
        including the tool bar and can be queried from mel using the
        contextInfo command.

        * image (string) - the name of an XPM file to be used as the icon.
        * index (ImageIndex) - the index of the image being set; three image
        representations are permitted: kImage1, kImage2, kImage3.
        """

    def setTitleString(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setTitleString(str) -> self

        Set the title of the context to the MString that is passed in.
        This string will appear in the help line when this context is
        activated.

        * str (string) - The new title string.
        """

    def stringClassName(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """stringClassName() -> string

        This method is called to determine the name that uniquely identifies
        the context.  Either this method, or the getClassName method, should
        be overridden such that the name is set to the appropriate string.
        For example:

        def stringClassName(self)
            return 'exampleTool'

        This name is used by Maya to call the appropriate
        tool property sheet MEL scripts, specifically:
            <b>name</b>Properties.mel
            <b>name</b>Values.mel
        If this method is not overriden, by default it will set
        the string to 'defaultTool'.  The method returns a string
        that uniquely identifies the context.
        """

    def toolOffCleanup(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """toolOffCleanup() -> None

        This method is called when the context is deactivated, i.e when
        another context is activated.
        Users can override this method and use it to reset any user
        defined data to a specific state.
        """

    def toolOnSetup(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """toolOnSetup(event) -> None

        This method is called when the context is activated, i.e when
        the toolButton for the context is pressed.
        Users can override this method and use it to set up any user
        defined data that needs to be initialized on each activation.


        * event (MEvent) - The button press event information.
        """


class MPxContextCommand:
    """Base class for custom context commands."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def appendSyntax(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """appendSyntax() -> None

        This method should be overridden to append syntax
        to the context command.  The syntax object can be
        obtained by calling the syntax method.
        The following flags cannot be used as user-defined
        flags as they are reserved for edit and query:
        '-e', '-edit', '-q', '-query'.
        """

    def doEditFlags(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doEditFlags() -> None

        This method is called when the command is called in edit mode.
        This method should be overridden by context commands
        to determine which edit flags are set in conjunction with
        the argument parser for this command.  The argument parser
        for this command can be obtained by calling the
        parser method.
        If the command is called with both the edit flag and
        the query flag, then the query flag will be ignored.
        """

    def doQueryFlags(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doQueryFlags() -> None

        This method is called when the command is called in query mode.
        This method should be overridden by context commands
        to determine which query flags are set in conjunction with
        the argument parser for this command.  The argument parser
        for this command can be obtained by calling the
        parser method.
        If the command is called with both the edit flag and
        the query flag, then the query flag will be ignored.
        """

    def makeObj(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """makeObj() -> MPxContext

        This function is used to instantiate a proxy context.
        In your derived class, declare this function:

        def makeObj(self)
            return userContextClass()

        where userContextClass is derived from MPxContext.
        """

    def parser(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Returns the context command's MArgParser object, if it has one."""

    def setResult(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setResult() -> None

        Set the value of the result to be returned by the command.  The value can be
        either a boolean, integer, floating point value, or string.
        """

    def syntax(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Returns the context command's MSyntax object, if it has one."""


class MPxDragAndDropBehavior:
    """This is the base class for user defined drag and drop behaviors."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def connectAttrToAttr(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectAttrToAttr(sourcePlug, destinationPlug, force) -> None

        This method is called by the defaultNavigation command to connect a source attribute to a destination attribute.

        If this method is overidden it should attempt to determine what the user probably wants this connection to be, and set up the connection appropriately. If the force argument is true it is intended to notify the user to break any existing connections to the plug, similar to what the mel command 'connectAttr' -f flag is used for.

        * sourcePlug (MPlug) - Source plug in the connection.
        * destinationPlug (MPlug) - Destination plug in the connection.
        * force (bool) - Tells whether or not to break any existing connections to the destination attribute.
        """

    def connectAttrToNode(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectAttrToNode(sourcePlug, destinationNode, force) -> None

        This method is called by the defaultNavigation command to connect a source attribute to a destination node.

        You should override this method if you can determine from the type of source node and attribute and the type of destination node what the user is trying to do and you know the appropriate connections that must be made for the end result to be what the user expects.

        * sourcePlug (MPlug) - Source plug in the connection.
        * destinationNode (MObject) - Destination node for the connection.
        * force (bool) - Tells whether or not to break any existing connections to the destination node.
        """

    def connectNodeToAttr(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectNodeToAttr(sourceNode, destinationPlug, force) -> None

        This method is called by the defaultNavigation command to connect a source node to a destination attribute.

        You should override this method if you can determine from the type of source node and the type of destination node and attribute what the user is trying to do and you know the appropriate connections that must be made for the end result to be what the user expects.

        * sourceNode (MObject) - Source node in the connection.
        * destinationPlug (MPlug) - Destination plug for the connection.
        * force (bool) - Tells whether or not to break any existing connections to the destination attribute.
        """

    def connectNodeToNode(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectNodeToNode(sourceNode, destinationNode, force) -> None

        This method is called by the defaultNavigation command to connect a source node to a destination node.

        You should override this method if you can determine from the type of source node and the type of destination node what the user is trying to do and you know the appropriate connections that must be made for the end result to be what the user expects.

        * sourceNode (MObject) - Source node in the connection.
        * destinationNode (MObject) - Destination node for the connection.
        * force (bool) - Tells whether or not to break any existing connections to the destination node.
        """

    def shouldBeUsedFor(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """shouldBeUsedFor(sourceNode, destinationNode, sourcePlug, destinationPlug) -> bool

        This method must be overridden in order to use a drag and drop behavior.

        The overridden method will be called by the defaultNavigation command to determine wether or not to use this drag and drop behavior to finish a connection. If the user would like to handle the connection between sourceNode/Plug and destinationNode/Plug then this routine must pass back true, otherwise the routine must pass back false in order for the default connection mechanism to work between these two nodes. sourcePlug and destinationPlug may be null depending on if there were any attributes given in the drag and drop. Use the isNull() method on MPlug to assure the plugs are valid.

        * sourceNode (MObject) - The source node of the drag and drop or the node being dragged.
        * destinationNode (MObject) - the destination node of the drag and drop or the node being dropped upon.
        * sourcePlug (MPlug) - The source plug of the drag and drop or the plug being dragged (this may be null).
        * destinationPlug (MPlug) - The destination plug of the drag and drop or the plug being dropped upon (this may be null).
        """


class MPxHardwareShader(maya.api.OpenMaya.MPxNode):
    """Base class for user defined hardware shaders."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    @staticmethod
    def findResource(*args: Unknown, **kwargs: Unknown) -> Any:
        """findResource(name, shaderPath) -> string

        This is a static utility to find the full path to a shader resource (typically a texture). This method will search the list of paths in the MAYA_HW_SHADER_RESOURCE_PATH environment variable, resolving relative paths based on the directory containing the shader.

        * name (string) - The name of the resource to look for (e.g. 'normals.dds')
        * shaderPath (string) - The full path to the current shader (e.g. 'C:/shaders/myshader.fx')


        Return the full path of the resource (e.g. 'C:/shaders/textures/normals.dds').
        """

    def getAvailableImages(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getAvailableImages(context, uvSetName) -> list of string/None

        Maya will call this method to get your shader's list of images which are available for use in the UV texture editor for the UV set specified. Typically, this list will include one entry for each texture using the specified UV set, however, your shader is free to return as many images as you wish (for example, blending between two textures, texture alpha masks, artificially shaded views of bump/normal maps, etc). Your shader's renderImage() method will be used to render the images themselves.

        * context (ShaderContext) - Context of the draw request (e.g. the surface being shaded, shading engine making the request)
        * uvSetName (string) - Name of a UV set the channel list should be filtered against.

        Returns the names of the images this shader defines which are valid for the uvSetName specified.
        Returns None if method is not implemented : Use the default behaviour.
        """

    @staticmethod
    def getHardwareShader(*args: Unknown, **kwargs: Unknown) -> Any:
        """getHardwareShader(object) -> TODO

        This is a static convenience method to be able to get an MPxHardwareShader from an MObject provided by a swatch generator class (Class derived from MSwatchRenderRegister).

        * object (MObject) - The object to examine.

        Return a MPxHardwareShader. If the method failed for any reason then None will be returned.
        """

    outColor: maya.api.OpenMaya.MObject
    outColorB: maya.api.OpenMaya.MObject
    outColorG: maya.api.OpenMaya.MObject
    outColorR: maya.api.OpenMaya.MObject
    def profile(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """profile() -> MRenderProfile

        Override this method to specify the renderers your shader supports. If this method is not overridden, Maya will assume your shader supports only Maya's iternal OpenGL based renderer.

        Note that this method is called inside the rendering loop and as such, you should make this method as fast as possible - typically just returning a static/precalculated value.

        Return a reference to the render profile for this Shader. Your shader class should create this once (usually for the whole class) and return the same object each time this method is called.
        """

    def renderImage(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """renderImage(context, imageName, region, parameters) -> [int, int]/None
        renderImage(context, uiDrawManager, imageName, region, parameters) -> [int, int]/None

        This method allows you to to render the background image used for this shader in the UV texture editor. The image requested will be one of the image names returned by your shader's getAvailableImages() method.

        The implementation must return the dimensions of the image in the 'imageWidth' and 'imageHeight' parameters so that Maya can perform pixel snapping and other resolution-dependent operations.

        The implementation can assume OpenGL context, model view projection matrix, and texture transformations have already been set. A default color of white will be set, however you are free to change this. The magnification filter will be set to either point or bilinear based on user configuration and should not be modified. The values of GL_TEXTURE_WRAP_S and GL_TEXTURE_WRAP_T are undefined on entry, and your implementation is responsible for setting them to appropriate values (e.g. GL_REPEAT).

        The arguments contain the name of the image to render, and the vertex and texture coordinate values to use at each corner of the rectangular image being rendered. Your implementation is responsible for restoring the original the value of any OpenGL state that is modified.

        * context (ShaderContext) - Context of the draw request (e.g. the surface being shaded, shading engine making the request)
        * imageName (string) - Name of the image to render. This corresponds to one of the image names returned by your shader's getAvailableImages() method.
        * region (float[2][2]) - Rectangular region to be rendered. The values of this parameter should be used to populate the vertex and texture coordinates of the rectangle being rendered.
        * parameters (RenderParamters) - Additional parameters on how to render the image. The values reflect the image settings of the UV editor.

        A second version with the uiDrawManager parameter allows you to to render the background image used for this shader in the UV texture editor in viewport 2.0.

        * uiDrawManager (MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry

        Returns None if method is not implemented : No rendering will occur.
        """

    def renderSwatchImage(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """renderSwatchImage(image) -> self

        If the shader specifies to override swatch rendering, then this method must be overridden in order to draw anything into a swatch.

        The shader will only draw a swatch if it has been registered to do so, by providing a valid classification during MFnPlugin::registerNode(). The shader should provide a classification that defines a swatch rendering node such as : "shader/surface/utility/:drawdb/shader/surface/myCustomShader:swatch/myCustomShaderSwatchGenerator" and have "myCustomShaderSwatchGenerator" registered has a swatch renderer : MSwatchRenderRegister.registerSwatchRender("myCustomShaderSwatchGenerator", MHWShaderSwatchGenerator.createObj );

        The default implementation is to draw nothing. The basic logic to draw a swatch is as follows:

          Determine the size of the swatch required. This is the dimensions of the MImage passed in as an argument. The pixels for the MImage will have been pre-allocated. The format of the pixels is 32-bit R,G,B,A, with 8-bits per channel.
          Either use an offscreen "swatch context" provided to you or use your own offscreen context. The provided context is available via the MHardwareRenderer class method makeSwatchContextCurrent(). Note that the swatch context may be smaller than the desired image size. In this case the rendering dimensions will be clamped.
          Either use swatch geometry provided to you, or use your own swatch geometry. The provided geometry is available via the method MHardwareRenderer::referenceDefaultGeometry(). The possible "default" geometries are either a sphere, cube or plane.
          Either use the provided "default" light and "default" camera or set up your own. Use the methods (getSwatchOrthoCameraSetting(), getSwatchLightDirection()) on MHardwareRenderer to get these defaults.
          Read back the swatch context into the provided MImage. The convenience method MHardwareRenderer::readSwatchContextPixels() can be used. By default the format of the MImage and the swatch context are the same, so the user does not need to worry about this. The context will read into the pre-allocated MImage pixels.
          Unreference any swatch geometry used for rendering using MHardwareRenderer::dereferenceGeometry().

        * image [IN/OUT] (MImage) - Image object to which this method must write the rendered swatch. On input the image's dimensions are already set and pixel storage already allocated.

        Returns None if method is not implemented : No rendering will occur.
        """

    def setUniformParameters(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setUniformParameters(parameters, remapCurrentValues=True, dagModifier=None) -> self

        Call this method to set the list of uniform parameters this shader uses. Once set, you can use these parameters to access the cached values of shader parameters, including testing when the value has been updated (to minimise the shader state changes). When using this method to manage uniform parameters, Maya will handle the underlyintg attributes, serialization and user interface for you.It is important to call this method whenever the shader parameters are modified (including at load time).This is an optional method - shader implementations are still free to manage uniform (i.e. shader-level) parameters independently if they wish.* parameters (MUniformParameterList) - the list of uniform parameters for this shader
        * remapCurrentValues (bool) - if True (the default), Maya will attempt to initialise the value of new parameters based on any equivalently named parameters that currently exist on the node. Otherwise, the parameters will be setup using default values. Unless you wish to forcibly reset parameter values, the default value of True should be used.
        * dagModifier (MDagModifier) - an optional DG modifier to use when managing the attributes used to represent the geometry parameters on this shader.
        """

    def setVaryingParameters(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setVaryingParameters(parameters, remapCurrentValues=True, dagModifier=None) -> self

        Call this method to set the list of varying parameters this shader uses. Once set, you can use these parameters directly to access geometry data for surfaces being shaded. When using this method to manage shader varying parameters, there is no need to override populateRequirements or handle the node interface as Maya will handle parameter setup, presentation and configuration for you.

        It is important to call this method whenever the shader parameters are modified (including at load time).

        This is an optional method - shader implementations are still free to manage geometry parameters independently if they wish.

        * parameters (MUniformParameterList) - the list of varying parameters for this shader
        * remapCurrentValues (bool) - if True (the default), Maya will attempt to initialise the value of new parameters based on any equivalently named parameters that currently exist on the node. Otherwise, the parameters will be setup using default values. Unless you wish to forcibly reset parameter values, the default value of True should be used.
        * dagModifier (MDagModifier) - an optional DG modifier to use when managing the attributes used to represent the geometry parameters on this shader.
        """

    def transparencyOptions(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """transparencyOptions() -> int

        This method returns transparency options for usage as hints for Maya's internal draw during a given rendering pass. Parameters are returned via an integer containing masked out bits. By default the mask is set to 0, meaning that the drawing should be treated as regular opaque object drawing. This will generally mean one call per draw pass.

        Options to control transparency are specified by returning one or more masks specified by the following values :
          - kIsTransparent : Draw as a transparent object. If no transparency overrides are specified, then control of how to draw during a given pass is determined internally by Maya's refresh algorithm, and options the user can set per modelling viewport.
          - kNoTransparencyFrontBackCull : When kisTransparent is set and this flag is set, do not perform transparency drawing using the internal 2-pass front-face + back-face culling algorithm.
          - kNoTransparencyPolygonSort : When kisTransparent is set and this flag is set, do not perform transparency drawing using the internal 2-pass drawing of back-to-front sorted triangles.
        """


class MPxHwShaderNode(maya.api.OpenMaya.MPxNode):
    """Base class for user defined hardware shaders."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def bind(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """bind(request, view) -> self

        This method is invoked for hardware rendering to Maya's 3D view.

        This is the preferred method of interactive feedback and performance. the "gl" version should be used for batch hardware rendering.

        This method is called to set up the OpenGL state.  It would typically ensure that textures were bound and that any specific OpenGL extensions are enabled.  A status code of MS::kSuccess should be returned unless there was a problem during the display, such as insufficient memory or required input data is missing or invalid.

        * request (MDrawRequest) - the draw request.
        * view (M3dView) - the view in which to draw.
        """

    def colorsPerVertex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """colorsPerVertex() -> int

        This method returns the number of color values per vertex that the hw shader node would like to receive from Maya.  Maya will attempt to provide all the color data that the shader would like but it will never provide more data that is actually available in the shape.  The color sets returned by getColorSetNames() will override the number of color sets specified by colorsPerVertex(). If you do not override this method or getColorSetNames(), Maya will provide no colors per vertex.

        Returns the number of color values desired
        """

    def currentPath(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """currentPath() -> MDagPath

        This method returns a reference to the current path that the shader is invoked for.

        The path is only valid before a call to any of the attribute specifying routines:

           normalsPerVertex()
           colorsPerVertex()
           getColorSetNames()
           texCoordsPerVertex()
           getTexCoordSetNames()
           hasTransparency()
           provideVertexIDs()

        The path is not guaranteed to be valid at any other time.

        This method allows the plugin to return attribute queries which are relative to a specific path or object.

        For example, the plugin can retrieve the MObject from the path, then use the MFnMesh class on the MObject, assuming the object is a polygonal surface. Through MFnMesh the code can query the actual number of texture coordinate sets on the surface and return appropriate values for the getTexCoordSetNames() routine.

        The [gl]bind(), [gl]unbind() and [gl]geometry() routines already have access to a dag path which is the same path as the one which can be retrieved via this method.

        For performance reasons, it is recommended that for those methods the MDagPath passed in as an argument should be used.

        Returns an MDagPath. Note that this path can be invalid
        Use MDagPath.isValid() to confirm the validity of the path.
        """

    def currentShadingEngine(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """currentShadingEngine() -> MObject

        This method returns an MObject to the shading engine that is currently being rendered. This method will only return a valid MObject during the following calls:

          normalsPerVertex()
          colorsPerVertex()
          getColorSetNames()
          texCoordsPerVertex()
          getTexCoordSetNames()
          hasTransparency()
          provideVertexIDs()
          getAvailableImages()
          bind(), glBind()
          geometry(), glGeometry()
          unbind(), glUnbind()
        """

    def dirtyMask(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """dirtyMask() -> int

        This method returns a "dirty" mask that indicates which geometry items have changed from the last invocation of the plugin to draw. The mask is valid at the time that geometry() or glGeometry() is called and at no other time.

        Note that this mask is relative to the geometry for the current object (path) being drawn by the shader. The current path is the MDagPath argument passed in via the geometry routines.

        In general the mask will mark the geometry as not being dirty.

        Scenarios where the geometry will be marked dirty include:

          Whenever a geometry attribute changes. For example positions or normals are modified.
          Whenever the attributes being requested changes from the previous invocation of the shader. For example, if in the previous invocation the plugin asks for position only, and in the current invocation asks for position and normals, then the geometry attributes returned will have changed and thus be marked "dirty".

        Returns the dirty mask which can be bit 'AND'ed against the values:
          kDirtyNone
          kDirtyVertexArray
          kDirtyNormalArray
          kDirtyColorArrays
          kDirtyTexCoordArrays
          kDirtyAll
        """

    def geometry(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """geometry(request, view, prim, writable, indexCount, indexArray, vertexCount, vertexIDs, vertexArray, normalCount, normalArrays, colorCount, colorArrays, texCoordCount, texCoordArrays) -> self

        This method is invoked for hardware rendering to Maya's 3D view.

        This is the preferred method of interactive feedback and performance. the "gl" version should be used for batch hardware rendering.

        This method does all the actual OpenGL drawing.  The arguments contain all the data to successfully call glDrawElements or glDrawRangeElements.  It is possible that there will be multiple calls to this method surrounded by a single call to bind() and unbind().

        Note 1.
        The array of vertex IDs returned corresponds to each triangle's vertex. This allows access to associated blind data per vertex. The vertexIDs array allows querying of information such as color per vertex etc.

        Note 2.
        The arrays passed to this method can contain sparse information.  Check array positions against None to ensure that the array information item is valid.

        It is necessary to use the indexArray to access information contained in the data arrays.

        * request (MDrawRequest) - the draw request.
        * view (M3dView) - the view in which to draw.
        * prim (int) - the type of primitive to draw.  This is one of the values accepted by glBegin().  Typically it will be GL_TRIANGLES but it could be any of the others.
        * writable (int) this is a mask which indicates which of the various array arguments can be modified in place.  If a bit in writable is set then you can modify corresponding data array (after casting it to a non-const type).  If the bit is not set in writable then you must not> modify the data since it points to internal Maya storage.  You can test the bits in writeable against the values
        :  kWriteNone
          kWriteVertexArray
          kWriteNormalArray
          kWriteColorArrays
          kWriteTexCoordArrays
          kWriteAll
        * indexCount (int) - specifies both the number of indices to draw and the size of the indexArray argument.
        * indexArray (buffer of int values) - the array of index values.  This array is in a format suitable for passing as the indices argument to glDrawElements() or glDrawRangeElements().  See the OpenGL documentation for details on calling these routines.
        * vertexCount (int) - the number of elements in the vertexArray, the normalArray, each of the colorArrays, and each of the texCoordArrays.
        * vertexIDs (buffer - int values) - the component IDs of the vertices in vertexArray. This array is only provided if it was requested by overriding the provideVertexIDs() method to return True.
        * vertexArray (buffer - float values) - the array of vertex data.  Currently, this is always 3 element floating point values.  This data is in a format suitable for passing to glVertexPointer().  See the OpenGL documentation for details.
        * normalCount (int) - the number of individual "normal" arrays that are being provided in normalArrays.  See the description of normalsPerVertex method below for details.
        * normalArrays (array of buffer - float values) - the normal (and tangent) data suitable. There may be 0, 1, 2, or 3 "normal" arrays.  See the description of the normalsPerVertex method below for details.
        * colorCount (int) - the number of individual color arrays.
        * colorArrays (array of buffer - float values) - the arrays of color data.  The first set of color data is pointed to by colorArrays[0].  Each color array contains vertexCount color values, each of which is 4 floating point values long and represents the red, green, blue, and alph values on a 0 to 1 scale.  Each individual array is suitable for passing to glColorPointer().
        * texCoordCount (int) - the number of texture coordinate arrays. Each array contains one set of UV texture coordinates.
        * texCoordArrays (array of buffer - float values) - the arrays of texture coordinate data. The first set of texture coordinate data is pointed to by texCoordArrays[0].  Each array contains vertexCount coordinate values, each of which is 2 floating point values long.  Each individual array is suitable for passing to glTexCoordPointer().
        """

    def getAvailableImages(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getAvailableImages(uvSetName) -> list of strings/None

        Maya will call this method to get your shader's list of images which are available for use in the UV texture editor for the UV set specified. Typically, this list will include one entry for each texture using the specified UV set, however, your shader is free to return as many images as you wish (for example, blending between two textures, texture alpha masks, artificially shaded views of bump/normal maps, etc). Your shader's renderImage() method will be used to render the images themselves.

        * uvSetName (string) - Name of a UV set the channel list should be filtered against.

        Returns the names of the images this shader defines which are valid for the uvSetName specified.
        Returns None if method is not implemented : Use the default behaviour.
        """

    def getColorSetNames(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getColorSetNames(names) -> int

        This method returns an array of color per vertex set names. Maya will attempt to provide color per vertex data from these maps in the corresponding array element in the colorArrays argument to the geometry method.  For example, if the names[2] is "cpv56" then colorArrays[2] will be the array of values from cpv56, or None if the shape being rendered does not have a color set of that name. Ifthis method is not overridden an empty list of names will be returned,and Maya will use colorsPerVertex() to determine how many color setsto provide.

        * names [IN/OUT] (list of string) - a string array holding the names of the color per vertex sets from which color data should be extracted.

        Returns the number of elements in the names array.
        """

    @staticmethod
    def getHwShaderNode(*args: Unknown, **kwargs: Unknown) -> Any:
        """getHwShaderNode(object) -> MPxHwShaderNode

        This is a static convenience method to be able to get an MPxHwShaderNode from an MObject provided by a swatch generator class (Class derived from MSwatchRenderRegister).

        * object (MObject) - The object to examine.
        """

    def getTexCoordSetNames(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getTexCoordSetNames(names) -> int

        This method returns an array of texture coordinate set names. Maya will attempt to provide texture coordinates from these maps in the corresponding array element in the texCoordArrays argument to the geometry method.  For example, if the names[2] is "uvSet3" then texCoordArrays[2] will be the array of values from uvSet3. If this method is not overridden an empty list of names will be returned, and Maya will use texCoordsPerVertex() to determine how many uv sets to provide.

        * names [IN/OUT] (list of string) - a string array holding the names of the uvSets from which texture coordinate data should be extracted.

        Returns the number of elements in the names array.
        """

    def glBind(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """glBind(shapePath) -> self

        This method should only be overridden for hardware rendering.

        The implementation can assume the graphics context and model view projection matrix have already been set.

        This method will be invoked once per frame and should be overridden to allocate any resources needed for the draw. For example, binding vertex programs, fragment programs, or allocating textures. A status code of MS::kSuccess should be returned unless there was a problem such as insufficient memory or required input data is missing or        invalid.

        * shapePath (MDagPath) - Path to the surface being drawn.
        """

    def glGeometry(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """glGeometry(shapePath, prim, writable, indexCount, indexArray, vertexCount, vertexIDs, vertexArray, normalCount, normalArrays, colorCount, colorArrays, texCoordCount, texCoordArrays) -> self

        This method should only be overridden for hardware rendering.

        The implementation can assume graphics context and model view projection matrix have already been set.

        This method does all the actual OpenGL drawing.  The arguments contain all the data to successfully call glDrawElements or glDrawRangeElements.  It is possible that there will be multiple calls to this method surrounded by a single call to bind() and unbind().

        Note 1.
        The array of vertex IDs returned corresponds to each triangle's vertex. This allows access to associated blind data per vertex. The vertexIDs array allows querying of information such as color per vertex etc.

        Note 2.
        The arrays passed to this method can contain sparse information.  Check array positions against None to ensure that the array information item is valid.

        It is necessary to use the indexArray to access information contained in the data arrays.

        * shapePath (MDagPath) - Path to the surface being drawn.
        See geometry() description for detail on the other parameters.
        """

    def glUnbind(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """glUnbind(shapePath) -> self

        This method should only be overridden for hardware rendering.

        The implementation can assume the graphics context and model view projection matrix have already been set.

        This method will be invoked once per frame and should be overridden to deallocate any resources used to draw. It's important that all resources be released when a batch hardware render has occured because the graphics context will be deleted. It may be desireable to override the other version of bind/unbind to keep track of whether the draw is for the 3D view or the batch hardware renderer. This information could then be used to better track the reuse of resources and optimize performance.

        A status code of MS::kSuccess should be returned unless there was a problem.

        * shapePath (MDagPath) - Path to the surface being drawn.
        """

    def hasTransparency(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """hasTransparency() -> bool

        This method returns a boolean value that indicates whether the object will be drawn transparently or not.  Transparent objects must be drawn after all the opaque objects in the scene or they will not display correctly.  Maya uses the return value to determine when it can draw this shape.

        Note : The functionality in this method has been subsumed by the transparencyOptions() method. It is recommended that shader node writers use this newer method as it provides greater control over how transparency is interpreted by Maya's refresh mechanism.

        For backward compatibility, if this method is specified and returns True, it will override the transparencyOptions() method.

        Returns True if the object will be transparent or False if it will not.
        """

    def invertTexCoords(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """invertTexCoords() -> bool

        Specifies whether this shader requires inverted texture coordinates. (i.e. where the top-left hand corner of UV space is (0,0) instead of the bottom-left corner).

        By default, this method will return False to ensure compatibility with existing shader code.
        """

    def normalsPerVertex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """normalsPerVertex() -> int

        Specifies how many normals per vertex the HW shader would like Maya to provide.  This can range from 0 to 3.  The first normal is the surface normal.  The second "normal" is the primary tangent (generally the "u" direction).  The third "normal" is the secondary tangent or the binormal (generally the "v" direction). Together, the normal, tangent and binormal form an orthogonal basis frequently named "tangent space basis".

        The tangent and binormal vectors are guaranteed to be normalized and orthogonal to the surface normal. Please note that extracting the tangent and/or binormal requires expensive calculations, that will slow down refresh time substantially. In a future version, Maya may cache the resulting tangent space basis; in the meantime, only ask for more than one normal per vertex if they are absolutely required.

        Also note that the tangent and binormal calculation requires a uv map. Currently, they are always computed from the first available uv map; if there is no uv mapping on the surface, Maya will only provide surface normals in the geometry call, regardless of the value returned by normalsPerVertex().

        If you do not override this method, Maya will provide 1 normal per vertex.

        Maya will automatically and silently clamp the result of this function to the [0,3] range.

        COMPATIBILITY NOTE: Automatic tangent space basis calculation is only supported starting with Maya 4.0.1. Maya 4.0 supported a different scheme that was much more complicated and no longer supported.

        Returns the number of normal values desired. (0 = none, 1 = surface normal only, 2 = surface normal + tangent, 3 = surface normal + tangent + binormal)
        """

    outColor: maya.api.OpenMaya.MObject
    outColorB: maya.api.OpenMaya.MObject
    outColorG: maya.api.OpenMaya.MObject
    outColorR: maya.api.OpenMaya.MObject
    outGlowColor: maya.api.OpenMaya.MObject
    outGlowColorB: maya.api.OpenMaya.MObject
    outGlowColorG: maya.api.OpenMaya.MObject
    outGlowColorR: maya.api.OpenMaya.MObject
    outMatteOpacity: maya.api.OpenMaya.MObject
    outMatteOpacityB: maya.api.OpenMaya.MObject
    outMatteOpacityG: maya.api.OpenMaya.MObject
    outMatteOpacityR: maya.api.OpenMaya.MObject
    outTransparency: maya.api.OpenMaya.MObject
    outTransparencyB: maya.api.OpenMaya.MObject
    outTransparencyG: maya.api.OpenMaya.MObject
    outTransparencyR: maya.api.OpenMaya.MObject
    def provideVertexIDs(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """provideVertexIDs() -> bool

        This method returns a boolean value that indicates whether a map of the vertex IDs will be provided to the geometry method.

        Returns True if vertex IDs should be provided to the geometry method.
        """

    def renderImage(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """renderImage(imageName, region, parameters) -> [int, int]/None
        renderImage(uiDrawManager, imageName, region, parameters) -> [int, int]/None

        This method allows you to to render the background image used for this shader in the UV texture editor. The image requested will be one of the image names returned by your shader's getAvailableImages() method.

        The implementation must return the dimensions of the image in the 'imageWidth' and 'imageHeight' parameters so that Maya can perform pixel snapping and other resolution-dependent operations.

        The implementation can assume OpenGL context, model view projection matrix, and texture transformations have already been set. A default color of white will be set, however you are free to change this. The magnification filter will be set to either point or bilinear based on user configuration and should not be modified. The values of GL_TEXTURE_WRAP_S and GL_TEXTURE_WRAP_T are undefined on entry, and your implementation is responsible for setting them to appropriate values (e.g. GL_REPEAT).

        The arguments contain the name of the image to render, and the vertex and texture coordinate values to use at each corner of the rectangular image being rendered. Your implementation is responsible for restoring the original the value of any OpenGL state that is modified.

        * imageName (string) - Name of the image to render. This corresponds to one of the image names returned by your shader's getAvailableImages() method.
        * region (float[2][2]) - Rectangular region to be rendered. The values of this parameter should be used to populate the vertex and texture coordinates of the rectangle being rendered.
        * parameters (RenderParamters) - Additional parameters on how to render the image. The values reflect the image settings of the UV editor.

        A second version with the uiDrawManager parameter allows you to to render the background image used for this shader in the UV texture editor in viewport 2.0.

        * uiDrawManager (MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry

        Returns None if method is not implemented : No rendering will occur.
        """

    def renderSwatchImage(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """renderSwatchImage(image) -> self/None

        If the shader specifies to override swatch rendering, then this method must be overridden in order to draw anything into a swatch.

        The shader will only draw a swatch if it has been registered to do so, by providing a valid classification during MFnPlugin::registerNode(). The shader should provide a classification that defines a swatch rendering node such as : "shader/surface/utility/:drawdb/shader/surface/myCustomShader:swatch/myCustomShaderSwatchGenerator" and have "myCustomShaderSwatchGenerator" registered has a swatch renderer : MSwatchRenderRegister.registerSwatchRender("myCustomShaderSwatchGenerator", MHWShaderSwatchGenerator.createObj );

        The default implementation is to draw nothing. The basic logic to draw a swatch is as follows:

          Determine the size of the swatch required. This is the dimensions of the MImage passed in as an argument. The pixels for the MImage will have been pre-allocated. The format of the pixels is 32-bit R,G,B,A, with 8-bits per channel.
          Either use an offscreen "swatch context" provided to you or use your own offscreen context. The provided context is available via the MHardwareRenderer class method makeSwatchContextCurrent(). Note that the swatch context may be smaller than the desired image size. In this case the rendering dimensions will be clamped.
          Either use swatch geometry provided to you, or use your own swatch geometry. The provided geometry is available via the method MHardwareRenderer::referenceDefaultGeometry(). The possible "default" geometries are either a sphere, cube or plane.
          Either use the provided "default" light and "default" camera or set up your own. Use the methods (getSwatchOrthoCameraSetting(), getSwatchLightDirection()) on MHardwareRenderer to get these defaults.
          Read back the swatch context into the provided MImage. The convenience method MHardwareRenderer::readSwatchContextPixels() can be used. By default the format of the MImage and the swatch context are the same, so the user does not need to worry about this. The context will read into the pre-allocated MImage pixels.
          Unreference any swatch geometry used for rendering using MHardwareRenderer::dereferenceGeometry().

        * image [IN/OUT] (MImage) - Image object to which this method must write the rendered swatch. On input the image's dimensions are already set and pixel storage already allocated.

        Returns None if method is not implemented : No rendering will occur.
        """

    def supportsBatching(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """supportsBatching() -> bool

        Specifies whether or not this shader supports batched rendering of shapes.

        In normal rendering, a shader is invoked using bind/geometry/unbind (or glBind/glGeometry/glUnbind) once for each shape being rendered. When a shader is used in batched rendering mode however, bind is called once, a series of geometry calls are made for each shape being rendered, followed by a single call to unbind (and similarly for glBind, glGeometry and glUnbind). As shader binding/unbinding can be expensive, batched rendering can significantly improve rendering performance. The more (particularly expensive) operations that can be moved out of the geometry/glGeometry methods the greater the performance improvement is. Ideally, only shape specific operations (such as binding geometry arrays and shape matrices) should be left in the geometry methods.

        It is important to note that your shader can only use batched rendering mode if there is no shape (i.e. dag path) specific code in bind, glBind, unbind, or glUnbind. If any of these methods perform shape specific processing, this code must either be moved into geometry/glGeometry, or you must return False in this method to indicate batching should be disabled for this shader.

        By default, this method will return False to ensure compatibility with existing shader code.
        """

    def texCoordsPerVertex(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """texCoordsPerVertex() -> int

        This method returns the number of texture coordinate values per vertex that the hw shader node would like to receive from Maya. Maya will attempt to provide all the texture coordinate data that the shader would like but it will never provide more data than is actually available in the shape.  The uv sets returned by getTexCoordSetNames() will override the number of uv sets specified by texCoordsPerVertex(). If you do not override this method or getTexCoordSetNames(), Maya will provide no texture coordinates per vertex.

        Note: Currently, Maya only retains 2 dimensional texture coordinate data but this may change in a future release.

        Returns the number of texture coordinate values desired
        """

    def transparencyOptions(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """transparencyOptions() -> int

        This method returns transparency options for usage as hints for Maya's internal draw during a given rendering pass. Parameters are returned via an integer containing masked out bits. By default the mask is set to 0, meaning that the drawing should be treated as regular opaque object drawing. This will generally mean one call per draw pass.

        Options to control transparency are specified by returning one or more masks specified by the values
        :

          kIsTransparent : Draw as a transparent object. If no transparency overrides are specified, then control of how to draw during a given pass is determined internally by Maya's refresh algorithm, and options the user can set per modelling viewport.
          kNoTransparencyFrontBackCull : When kisTransparent is set and this flag is set, do not perform transparency drawing using the internal 2-pass front-face + back-face culling algorithm.
          kNoTransparencyPolygonSort : When kisTransparent is set and this flag is set, do not perform transparency drawing using the internal 2-pass drawing of back-to-front sorted triangles.

        Note : Setting the "hasTransparency()" method to True will override this method. This is for backward compatibility with behaviour on existing hardware shader nodes. It is recommended that shaders use the "transparencyOptions()" override, and not longer use the older "hasTransparency()" override from their shader classes.

        Retuns an integer containing the appropriate options set via masks.
        """

    def unbind(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """unbind(request, view) -> self

        This method is invoked for hardware rendering to Maya's 3D view.

        This is the preferred method of interactive feedback and performance. the "gl" version should be used for batch hardware rendering.

        This method is called to restore the OpenGL state.  Specifically, it must disable any OpenGL extensions that the matching bind() method may have enabled.  This is necessary to ensure that the rest of Maya's drawing code continues to work correctly.  A status code of MS::kSuccess should be returned unless there was a problem such as insufficient memory or required input data is missing or invalid.

        The arguments passed to this method are the same ones that were passed to the bind() method.

        * request (MDrawRequest) - the draw request.
        * view (M3dView) - the view in which to draw.
        """


class MPxLocatorNode(maya.api.OpenMaya.MPxNode):
    """Base class for user defined locators."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def boundingBox(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """boundingBox() -> MBoundingBox

        This method should be overridden to return a bounding box for the locator.
        If this method is overridden, then MPxLocatorNode.isBounded should also be overridden to return True.
        """

    boundingBoxCenterX: maya.api.OpenMaya.MObject
    boundingBoxCenterY: maya.api.OpenMaya.MObject
    boundingBoxCenterZ: maya.api.OpenMaya.MObject
    center: maya.api.OpenMaya.MObject
    def closestPoint(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """closestPoint(rayPoint, rayDir) -> MPoint

        Returns the point on the locator, in the locator's local space, which is closest along the specified ray.

        By default, the locator's origin (0, 0, 0) is returned.

        This is currently only used by Maya during single selection. See useClosestPointForSelection() for further details on that.

        * rayPoint (MPoint) - The base point defining the ray in space
        * rayDir (MVector) - The ray direction in space
        """

    def color(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """color(status) -> int

        This method returns the index of the color that is the default draw color for the given display status.  The index should be used with the methods of M3dView.  The value is not an index into the OpenGL color table. 

        The index that is returned will be into the active, dormant, or template color tables depending on the display status passed in.

        * displayStatus (int) - display status. See M3dView.displayStatus() for a list of valid status.
        """

    def colorRGB(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """colorRGB(status) -> MColor

        This method returns the RGB values of the default draw color for the given display status.

        * displayStatus (int) - display status. See M3dView.displayStatus() for a list of valid status.
        """

    def draw(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """draw(view, path, style, status) -> self

        Overriding this method allows the drawing of custom geometry using standard OpenGL calls.  The OpenGL state should be left in the same state that it was in previously.  The OpenGL routine glPushAttrib may be used to make this easier.

        When this routine is called, the following conditions may be assumed:
         - the correct transform matrix will be loaded for the locator, so the geometry should be drawn in local space
         - the correct default color will be set for wire frame drawing given the object's state (eg active, dormant, etc.)
         - the object is not invisible or hidden
         - if the object has a bounding box, then the bounding box is at least partially in the frustum


        As a convenience, this draw method will also be used by OpenGL's selection mechanism to determine whether this object gets selected by a particular mouse event.  The user does not need to write a separate selection routine.

        * view (M3dView) - 3D view that is being drawn into.
        * path (MDagPath) - to the parent (transform node) of this locator in the DAG.
        If there is a shape node parented directly beneath the transform node, you can access it 
        by calling MDagPath.extendToShape(). 
        * style (int) - style to draw object in. See M3dView.displayStyle() for a list of valid styles.
        * status (int) - selection status of object. See M3dView.displayStatus() for a list of valid status.

                        DEPRECATED in 2024, draw is no longer supported.
        """

    def drawLast(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """drawLast() -> bool

        Indicates that this locator should be the last item draw in a given refresh cycle.  Objects drawn out-of-order will not preserve the proper transparency sorting.  Conflicts among multiple objects with the drawLast indicator set to TRUE will be resolved by their order in the Outliner, where they will be drawn top-to-bottom.

        The default return value is True.
        """

    def excludeAsLocator(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """excludeAsLocator() -> bool

        When the modelPanel is set to not draw locators, returing True will also not draw the custom locator. If False is returned, the custom locator will also be drawn.

        The default return value is True.
        """

    def getShapeSelectionMask(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getShapeSelectionMask() -> MSelectionMask

        This routine can be overridden to provide information aboutthe selection mask of the locator. By default the selection maskfor locators is returned.
        """

    instObjGroups: maya.api.OpenMaya.MObject
    intermediateObject: maya.api.OpenMaya.MObject
    inverseMatrix: maya.api.OpenMaya.MObject
    def isBounded(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """isBounded() -> bool

        This method should be overridden to return True if the user supplies a bounding box routine.  Supplying a bounding box routine makes refresh and selection more efficient.
        """

    isTemplated: maya.api.OpenMaya.MObject
    def isTransparent(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """isTransparent() -> bool

        Indicates that this locator uses transparency during ::draw method calls. Objects with transparency must be drawn in a special queue, i.e. after all opaque objects are drawn.

        The default return value is False.
        """

    localPosition: maya.api.OpenMaya.MObject
    localPositionX: maya.api.OpenMaya.MObject
    localPositionY: maya.api.OpenMaya.MObject
    localPositionZ: maya.api.OpenMaya.MObject
    localScale: maya.api.OpenMaya.MObject
    localScaleX: maya.api.OpenMaya.MObject
    localScaleY: maya.api.OpenMaya.MObject
    localScaleZ: maya.api.OpenMaya.MObject
    matrix: maya.api.OpenMaya.MObject
    nodeBoundingBox: maya.api.OpenMaya.MObject
    nodeBoundingBoxMax: maya.api.OpenMaya.MObject
    nodeBoundingBoxMaxX: maya.api.OpenMaya.MObject
    nodeBoundingBoxMaxY: maya.api.OpenMaya.MObject
    nodeBoundingBoxMaxZ: maya.api.OpenMaya.MObject
    nodeBoundingBoxMin: maya.api.OpenMaya.MObject
    nodeBoundingBoxMinX: maya.api.OpenMaya.MObject
    nodeBoundingBoxMinY: maya.api.OpenMaya.MObject
    nodeBoundingBoxMinZ: maya.api.OpenMaya.MObject
    nodeBoundingBoxSize: maya.api.OpenMaya.MObject
    nodeBoundingBoxSizeX: maya.api.OpenMaya.MObject
    nodeBoundingBoxSizeY: maya.api.OpenMaya.MObject
    nodeBoundingBoxSizeZ: maya.api.OpenMaya.MObject
    objectColor: maya.api.OpenMaya.MObject
    objectGroupColor: maya.api.OpenMaya.MObject
    objectGroupId: maya.api.OpenMaya.MObject
    objectGroups: maya.api.OpenMaya.MObject
    objectGrpCompList: maya.api.OpenMaya.MObject
    parentInverseMatrix: maya.api.OpenMaya.MObject
    parentMatrix: maya.api.OpenMaya.MObject
    underWorldObject: maya.api.OpenMaya.MObject
    def useClosestPointForSelection(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """useClosestPointForSelection() -> bool

        Determines whether Maya should call closestPoint() when doing single selection.

        When doing single selection Maya generally chooses the object closest to the selection ray. For locators it first does a hit test by calling the locator's draw method to determine if any part of it lies within the selection box. If the hit test succeeds Maya will add the locator to the list of objects being considered for selection and will use the center of the locator (i.e. its local origin) in determining its distance from the selection ray. This works well for locators which mark a single point in space, with no offset, but may not work as well for more complex locators.

        If this method is overridden to return True, then rather than using the locator's center to determine its distance from the selection ray, Maya will pass the ray to the closestPoint() method and use the point it returns. Note that you will have override closestPoint() as well to provide an appropriate point.
        """

    useObjectColor: maya.api.OpenMaya.MObject
    visibility: maya.api.OpenMaya.MObject
    worldInverseMatrix: maya.api.OpenMaya.MObject
    worldMatrix: maya.api.OpenMaya.MObject
    worldPosition: maya.api.OpenMaya.MObject
    worldPositionX: maya.api.OpenMaya.MObject
    worldPositionY: maya.api.OpenMaya.MObject
    worldPositionZ: maya.api.OpenMaya.MObject

class MPxManipContainer(maya.api.OpenMaya.MPxNode):
    """Parent class of all user defined manipulators."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addCircleSweepManip(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addCircleSweepManip(manipName, angleName) -> MDagPath

        This method creates a CircleSweepManip and adds it to
        the MPxManipContainer container.

        * manipName (string) manipulator name
        * angleName (string) angle name

        Returns the new CircleSweepManip
        """

    def addCurveSegmentManip(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addCurveSegmentManip(manipName, startParamName, endParamName ) -> MDagPath

        This method creates a CurveSegmentManip and adds it to
        the MPxManipContainer container.

        * manipName (string) manipulator name
        * startParamName (string) start param name
        * endParamName (string) end param name

        Returns the new CurveSegmentManip
        """

    def addDirectionManip(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addDirectionManip(manipName, directionName) -> MDagPath

        This method creates a DirectionManip and adds it to
        the MPxManipContainer container.

        * manipName (string) manipulator name
        * directionName (string) direction name

        Returns the new DirectionManip
        """

    def addDiscManip(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addDiscManip(manipName, angleName) -> MDagPath

        This method creates a DiscManip and adds it to
        the MPxManipContainer container.

        * manipName (string) manipulator name
        * angleName (string) angle name

        Returns the new DiscManip
        """

    def addDistanceManip(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addDistanceManip(manipName, distanceName) -> MDagPath

        This method creates a DistanceManip and adds it to
        the MPxManipContainer container.

        * manipName (string) manipulator name
        * distanceName (string) distance name

        Returns the new DistanceManip
        """

    def addFreePointTriadManip(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addFreePointTriadManip(manipName, pointName) -> MDagPath

        This method creates a FreePointTriadManip and adds it to
        the MPxManipContainer container.

        * manipName (string) manipulator name
        * pointName (string) point name

        Returns the new FreePointTriadManip
        """

    def addMPxManipulatorNode(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addMPxManipulatorNode(manipTypeName, manipName, proxyManip) -> None

        This method creates a custom MPxManipulatorNode and adds it to the
        MPxManipContainer container.

        * manipTypeName (string) manipulator name
        * manipName (string) name of the manip
        Returns a pointer to the new manipulator
        """

    def addManipToPlugConversion(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addManipToPlugConversion(plug) -> unsigned int

        This method adds a manipulator to plug converter for the specified
        plug. The converter must be implemented in the manipToPlugConversion()
        virtual method of this class.

        NOTE: The conversion methods and callback methods of this class should
        not be mixed.  The conversion methods are: addManipToPlugConversion(),
        addManipToPlugConversion() The callback methods are:
        addPlugToManipConversionCallback() addManipToPlugConversionCallback()

        * plug (MPlug) - The plug for which the converter is being requested.

        Returns the index used to identify the plug inside the
        manipToPlugConversion() method.
        """

    def addPlugToInViewEditor(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addPlugToInViewEditor(plug)

        Adds a plug to the In-View Editor.

        The first such call will cause the In-View Editor to
        be displayed automatically with the custom manip.

        Should be called from connectToDependNode().

        * plug (MPlug) - The plug that the slider should control
        """

    def addPlugToManipConversion(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addPlugToManipConversion(manipIndex)

        This method adds a plug to manipulator converter for the specified
        manipulator value (e.g. the start point of a distance manip). The
        converter must be implemented in the plugToManipConversion() virtual
        method of this class.

        NOTE: The conversion methods and callback methods of this class should
        not be mixed.  The conversion methods are: addManipToPlugConversion(),
        addManipToPlugConversion() The callback methods are:
        addPlugToManipConversionCallback() addManipToPlugConversionCallback()

        * manipIndex (int) - The index of the manipulator value for which the
        converter is being requested. The index is determined by calling the
        appropriate method of the manipulator's functionset (e.g.
        MFnDistanceManip::startPointIndex).
        """

    def addPointOnCurveManip(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addPointOnCurveManip(manipName, paramName) -> MDagPath

        This method creates a PointOnCurveManip and adds it to
        the MPxManipContainer container.

        * manipName (string) manipulator name
        * paramName (string) param name

        Returns the new PointOnCurveManip
        """

    def addPointOnSurfaceManip(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addPointOnSurfaceManip(manipName, paramName) -> MDagPath

        This method creates a PointOnSurfaceManip and adds it to
        the MPxManipContainer container.

        * manipName (string) manipulator name
        * paramName (string) param name

        Returns the new PointOnSurfaceManip
        """

    def addRotateManip(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addRotateManip(manipName, rotationName) -> MDagPath

        This method creates a RotateManip and adds it to
        the MPxManipContainer container.

        * manipName (string) manipulator name
        * rotationName (string) name of the rotation vector

        Returns the dag path to the new rotate manipulator
        """

    def addScaleManip(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addScaleManip(manipName, scaleName) -> MDagPath

        This method creates a ScaleManip and adds it to
        the MPxManipContainer container.

        * manipName (string) manipulator name
        * scaleName (string) name of the scale vector

        Returns the dag path to the new scale manipulator
        """

    def addStateManip(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addStateManip(manipName, stateName) -> MDagPath

        This method creates a StateManip and adds it to
        the MPxManipContainer container.

        * manipName (string) manipulator name
        * stateName (string) state name

        Returns the new StateManip
        """

    @staticmethod
    def addToManipConnectTable(*args: Unknown, **kwargs: Unknown) -> Any:
        """addToManipConnectTable( typeId )

        This method adds the user defined node as an entry in the
        manipConnectTable so that when this node is selected the user can
        use the show manip tool to get the user defined manipulator
        associated with this node. Note that the name of the manipulator
        node has to be the name of the plug-in node appended with 'Manip'.

        * mid (MTypeId) - Id of the user defined node
        """

    def addToggleManip(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addToggleManip(manipName, toggleName) -> MDagPath

        This method creates a ToggleManip and adds it to
        the MPxManipContainer container.

        * manipName (string) manipulator name
        * toggleName (string) toggle name

        Returns the new ToggleManip
        """

    def connectToDependNode(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectToDependNode(node) -> None

        This method connects the manipulator to the dependency node. This
        is a virtual method and needs to be overridden from the plug-in.

        * node (MObject) - the node to which the manipulator should be connected
        """

    def createChildren(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """createChildren() -> None

        This method should be overridden in user defined manipulators.
        This method is called after the user node derived from
        MPxManipContainer is set up.
        """

    def doDrag(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doDrag() -> None

        This method gets called when the manipulator receives a mouse drag event.

        Returns None if successful.  Otherwise, returns MStatus.kUnknownParameter
        to allow Maya to further process the event.
        """

    def doPress(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doPress() -> None

        This method gets called when the manipulator receives a mouse down event.

        Returns None if successful.  Otherwise, returns MStatus.kUnknownParameter
        to allow Maya to further process the event.
        """

    def doRelease(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doRelease() -> None

        This method gets called when the manipulator receives a mouse release
        event.

        Returns None if successful.  Otherwise, returns MStatus.kUnknownParameter
        to allow Maya to further process the event.
        """

    def draw(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """draw(view, path, style, status) -> None

        This method can be overloaded to customize the drawing of the
        child manipulators. If the default draw is also required, this
        method should be called from the derived method.

        * view (M3dView) - the view in which to draw
        * path (MDagPath) - the current path
        * style (M3dView.DisplayStyle) - the display appearance
        * status (M3dView.DisplayStatus) - the display status
        """

    def drawUI(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """drawUI(drawManager, frameContext) -> None

        This is the primary method for doing custom drawing for the
        manipulator in Viewport 2.0. All drawing should occur using the
        MUIDrawManager and any data cached in preDrawUI(). Raw OpenGL calls
        are not supported and if used behaviour will be undefined. Selection
        must still be handled in the draw() method, this method is only for
        display.

        This method is only called when the manipulator needs to be drawn in
        Viewport 2.0.

        We only need to override this function when we have some custom
        elements to draw other than the child manipulators in Viewport 2.0.

        This function is empty in this base class.

        * drawManager (MUIDrawManager) - The draw manager interface for
                                         drawing some simple UI
        * frameContext (MFrameContext) - Frame level context information
        """

    def finishAddingManips(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """finishAddingManips()

        This method should be called from the user-defined manipulator
        plug-in near the end of the connectToDependNode method so that the
        converter in the manipulator can be initialized. The converter
        cannot be initialized until all the connections from the manip
        values to the plug values have been specified.
        """

    def getConverterManipDoubleValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getConverterManipDoubleValue() -> double

        This method retrieves the value of a converterManipValue of type
        double at a given index from the converter.

        * manipIndex (unsigned int) - The index of the value
        """

    def getConverterManipMEulerRotationValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getConverterManipMEulerRotationValue() -> MEulereRotation

        This method retrieves the value of a converterManipValue of type
        MEulerRotation at a given index from the converter.

        * manipIndex (unsigned int) - The index of the value
        """

    def getConverterManipMMatrixValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getConverterManipMMatrixValue() -> MMatrix

        This method retrieves the value of a converterManipValue of type
        MMatrix at a given index from the converter.

        * manipIndex (unsigned int) - The index of the value
        """

    def getConverterManipMPointValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getConverterManipMPointValue() -> MPoint

        This method retrieves the value of a converterManipValue of type
        MPoint at a given index from the converter.

        * manipIndex (unsigned int) - The index of the value
        """

    def getConverterManipMTransformationMatrixValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getConverterManipMTransformationMatrixValue() -> MTransformationMatrix

        This method retrieves the value of a converterManipValue of type
        MTransformationMatrix at a given index from the converter.

        * manipIndex (unsigned int) - The index of the value
        """

    def getConverterManipMVectorValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getConverterManipMVectorValue() -> MVector

        This method retrieves the value of a converterManipValue of type
        MVector at a given index from the converter.

        * manipIndex (unsigned int) - The index of the value
        """

    def getConverterManipUIntValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getConverterManipUIntValue() -> unsigned int

        This method retrieves the value of a converterManipValue of type
        unsigned int at a given index from the converter.

        * manipIndex (unsigned int) - The index of the value
        """

    def getConverterManipValues(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getConverterManipValues() -> [double,double]

        This method retrieves the value of a converterManipValue of type
        [double, double] at a given index from the converter.

        * manipIndex (unsigned int) - The index of the value
        """

    def getConverterPlugDoubleValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getConverterPlugDoubleValue() -> double

        This method retrieves the value of a converterPlugValue of type
        double at a given index from the converter.

        * plugIndex (unsigned int) - The index of the value
        """

    def getConverterPlugMEulerRotationValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getConverterPlugMEulerRotationValue() -> MEulerRotation

        This method retrieves the value of a converterPlugValue of type
        MEulerRotation at a given index from the converter.

        * plugIndex (unsigned int) - The index of the value
        """

    def getConverterPlugMMatrixValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getConverterPlugMMatrixValue() -> MMatrix

        This method retrieves the value of a converterPlugValue of type
        MMatrix at a given index from the converter.

        * plugIndex (unsigned int) - The index of the value
        """

    def getConverterPlugMPointValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getConverterPlugMPointValue() -> MPoint

        This method retrieves the value of a converterPlugValue of type
        MPoint at a given index from the converter.

        * plugIndex (unsigned int) - The index of the value
        """

    def getConverterPlugMVectorValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getConverterPlugMVectorValue() -> MVector

        This method retrieves the value of a converterPlugValue of type
        MVector at a given index from the converter.

        * plugIndex (unsigned int) - The index of the value
        """

    def getConverterPlugValues(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getConverterPlugValues() -> [double, double]

        This method retrieves the value of a converterPlugValue of type
        [double, double] at a given index from the converter.

        * plugIndex (unsigned int) - The index of the value
        """

    @staticmethod
    def initialize(*args: Unknown, **kwargs: Unknown) -> Any:
        """initialize() -> None

        This method initializes the manipulator,
        and should be overriden in user-defined manipulators.

        Return: Status of the operation.
        The base class always returns MS::kSuccess.
        """

    def isManipActive(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """isManipActive(manipName, stateName) -> MDagPath

        This method returns if custom manip is active & gets the
        current manip object.

        * manipType (MFn Type constant) - The type of the custom manip
        * manipObject (MObject) - Manipulator object
        """

    def manipToPlugConversion(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """manipToPlugConversion(manipIndex) -> MManipData

        This virtual method calculates and returns the requested manipulator
        value, based upon the values of plugs on the nodes being manipulated.

        To use, call addPlugToManipConversion() for each manipulator value
        (e.g. the start point of a distance manip) you want this method to
        calculate, then implement this method to calculate those
        manipulator values. Each manipulator value is identified by the
        unique index returned by the corresponding method of its functionset 
        (e.g. MFnDistanceManip::startPointIndex).

        * manipIndex (int) - The index of the manipulator value to be
        calculated

        return
        New manipulator value.
        """

    @staticmethod
    def newManipulator(*args: Unknown, **kwargs: Unknown) -> Any:
        """newManipulator(manipName) -> (MPxManipContainer, MObject)

        This static function is used to create a user-defined manipulator.
        The manipObject argument is set to the new manipulator node.
        Note that the manipName argument must be the name of a
        manipulator derived from MPxManipContainer.
        Also note that this method creates the newManipulator,
        but doesn't add it to the DAG.
        The primary use of this method is in conjunction with
        MPxSelectionContext::addManipulator, to add
        user-defined manipulators to a context.

        Returns a tuple consisting of new MPxManipContainer instance, 
        and the manipulator node.

        * manipName (string) - manipulator name
        """

    def plugToManipConversion(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """plugToManipConversion(manipIndex) -> MManipData

        This virtual method calculates and returns the requested
        plug value, based upon the container's manipulator values.

        To use, call addManipToPlugConversion() for each plug whose value you
        want this method to calculate then implement this method to calculate
        those plug values. Each plug is identified by the unique index
        returned by the addManipToPlugConversion() call.

        plugIndex (int) - The index of the plug value to be calculated

        return
        New plug value.
        """

    def preDrawUI(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """preDrawUI(view) -> None

        This function is used to setup some drawing data for drawing the
        manipulator in Viewport 2.0 . The data updated and cached in this
        function will be used later during 'drawUI()'.

        This method is only called when the manipulator needs to be drawn
        in Viewport 2.0.

        This method needs only be overridden if custom data is needed for
        drawing in drawUI(). If no such data is needed, this method may be
        left unimplemented.

        This function is empty in this base class.

        * view (M3dView) * The view in which to draw
        """

    @staticmethod
    def removeFromManipConnectTable(*args: Unknown, **kwargs: Unknown) -> Any:
        """removeFromManipConnectTable( typeId )

        This method adds the user defined node as an entry in the
        manipConnectTable so that when this node is selected the user can
        use the show manip tool to get the user defined manipulator
        associated with this node. Note that the name of the manipulator
        node has to be the name of the plug-in node appended with 'Manip'.

        * mid (MTypeId) - Id of the user defined node
        """


class MPxManipulatorNode(maya.api.OpenMaya.MPxNode):
    """Parent class of all user defined manipulators."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addDependentPlug(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addDependentPlug(plug) -> None

        This method adds the plug to the list of those to be keyframed.
        The call to addDependentPlug() should happen prior to the manipulator
        identifying the plugs to be set. For example, if your manipulator
        sets plugs based on the selection list or modifier keys you could
        call addDependentPlug() from your doPress() method. Note that the
        dependentPlugsReset() method is provided to clear out the list and
        should be called prior to addDependentPlugs().

        * plug (MPlug) - the plug to keyframe when using this manipulator
        """

    def addDoubleValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addDoubleValue(valueName, defaultValue) -> int

        Manipulators which call connectPlugToValue() must first create
        the value on the node. Use this method to create a value of
        double type.
        Returns the index assigned to this value by Maya.

        * valueName (string) - Name of the value.
        * defaultValue (float) - Default value.
        """

    def addPointValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addPointValue(valueName, defaultValue) -> int

        Manipulators which call connectPlugToValue() must first create
        the value on the node. Use this method to create a value of
        MPoint type.
        Returns the index assigned to this value by Maya.

        * valueName (string) - Name of the value.
        * defaultValue (MPoint) - Default value.
        """

    def addVectorValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addVectorValue(valueName, defaultValue) -> int

        Manipulators which call connectPlugToValue() must first create
        the value on the node. Use this method to create a value of
        MVector type.
        Returns the index assigned to this value by Maya.

        * valueName (string) - Name of the value.
        * defaultValue (MVector) - Default value.
        """

    def colorAndName(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """colorAndName(view, glName, glNameIsPickable, colorIndex) -> None

        This method is used to set the color of the GL component that is
        being drawn next. It is also used to set GL name of the component
        so that picking can be supported.

        * view (M3dView) - the view in which to draw
        * glName (MGLuint) - GL 'name' (an unsigned int) of the component. Must be unique.
        * glNameIsPickable (bool) - If true, the component will be pickable
        * colorIndex (half) - Color to use, as provided by one of the *Color()
                              methods in this class.
        """

    def connectPlugToValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectPlugToValue(plug, valueIndex) -> int

        This method is called in the connectToDependNode() virtual if
        it is implemented for the custom manipulator. It will
        connect a plug to an already added manipulator value of
        the same type.

        Returns a new index for the plug that is being connected.

        * plug (MPlug) - the plug to connect the value to
        * valueIndex (int) - the index of the value. index is set by add*Value() method
        """

    def connectToDependNode(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """connectToDependNode(node) -> None

        This method connects the manipulator to the dependency node. This
        is a virtual method and needs to be overridden from the plug-in.

        * node (MObject) - the node to which the manipulator should be connected
        """

    def dependentPlugsReset(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """dependentPlugsReset() -> None

        This method resets the list of dependent plugs for this manipulator.
        Call this method prior to adding plugs via addDependentPlug() such as
        from your doPress() method.
        """

    def deregisterForMouseMove(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """deregisterForMouseMove() -> None

        This method deregisters this manipulator from receiving
        mouse move events.
        """

    def dimmedColor(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """dimmedColor() -> half

        This method returns the color index for a dimmed or unselectable component.
        """

    def doDrag(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doDrag(view) -> None

        This method gets called when the manipulator receives a mouse drag event.

        Returns None if successful.  Otherwise, returns MStatus.kUnknownParameter
        to allow Maya to further process the event.

        * view (M3dView) - the view in which to draw
        """

    def doMove(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doMove(view, refresh) -> None

        This method gets called when the manipulator receives a mouse move event,
        if the manipulator registered for mouse move events. To register for mouse
        move events, invoke registerForMouseMove() in the postConstructor of your
        manipulator.

        Returns MStatus.kSuccess if successful.  Otherwise, returns MStatus.kUnknownParameter
        to allow Maya to further process the event.

        * view (M3dView) - the view in which to draw
        * refresh (bool) - if true, refresh the view on this event. Default is false.
        """

    def doPress(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doPress(view) -> None

        This method gets called when the manipulator receives a mouse down event.

        Returns None if successful.  Otherwise, returns MStatus.kUnknownParameter
        to allow Maya to further process the event.

        * view (M3dView) - the view in which to draw
        """

    def doRelease(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doRelease(view) -> None

        This method gets called when the manipulator receives a mouse release event.

        Returns None if successful.  Otherwise, returns MStatus.kUnknownParameter
        to allow Maya to further process the event.

        * view (M3dView) - the view in which to draw
        """

    def draw(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """draw(view, path, style, status) -> None

        This method is overloaded to draw the manipulators. Selection
        is also setup with this method using the colorAndName()
        method call.

        * view (M3dView) - the view in which to draw
        * path (MDagPath) - the current path
        * style (M3dView.DisplayStyle) - the display appearance
        * status (M3dView.DisplayStatus) - the display status
        """

    def drawUI(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """drawUI(drawManager, frameContext) -> None

        This is the primary method for drawing the manipulator in Viewport 2.0.
        All drawing should occur using the MUIDrawManager and any data cached
        in preDrawUI(). Raw OpenGL calls are not supported and if used behaviour
        will be undefined. Selection must still be handled in the draw() method,
        this method is only for display.

        This method is only called when the manipulator needs to be drawn in Viewport 2.0.

        This function is empty in this base class.

        * drawManager (MUIDrawManager) - The MUIDrawManager used to draw some simple UI
        * frameContext (MFrameContext) - Frame level context information
        """

    def finishAddingManips(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """finishAddingManips() -> None

        This method should be called from the user-defined manipulator
        plug-in near the end of the connectToDependNode method so that the
        converter in the manipulator can be initialized. The converter
        cannot be initialized until all the connections from the manip
        values to the plug values have been specified.
        """

    def getDoubleValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getDoubleValue(valueIndex, previousValue) -> float

        This method is used for getting a floating point value associated with the manipulator.

        Returns the floating point value

        * valueIndex (int) - the index of the value to be retrieved
        * previousValue (bool) - if true, get the previous value. if false, get the current value
        """

    def getPointValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getPointValue(valueIndex, previousValue) -> MPoint

        This method is used for getting an MPoint value associated with the manipulator.

        Returns the MPoint value

        * valueIndex (int) - the index of the value to be retrieved
        * previousValue (bool) - if true, get the previous value. if false, get the current value
        """

    def getVectorValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getVectorValue(valueIndex, previousValue) -> float

        This method is used for getting an MVector value associated with the manipulator.

        Returns the MVector value

        * valueIndex (int) - the index of the value to be retrieved
        * previousValue (bool) - if true, get the previous value. if false, get the current value
        """

    def glActiveName(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """glActiveName() -> MGLuint

        This method returns the unsigned int value which
        specifies the current active handle.

        Returns the active handle name.
        """

    def glFirstHandle(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """glFirstHandle() -> MGLuint

        This method is used to find the unsigned int value that should
        be used for the first GL handle name.

        Returns the first handle name.
        """

    def labelBackgroundColor(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """labelBackgroundColor() -> half

        This method returns the color index of a label background.
        """

    def labelColor(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """labelColor() -> half

        This method returns the color index of a label.
        """

    def lineColor(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """lineColor() -> half

        This method returns the color index of a line
        """

    def mainColor(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """mainColor() -> half

        This method returns the main color index.
        """

    def mouseDown(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """mouseDown() -> (half, half)

        This method returns the mouse down position within
        a view. The position is in port coordinates.

        Returns a tuple consisting of the x and y port coodinates.
        """

    def mousePosition(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """mousePosition() -> (half, half)

        This method returns the current mouse position within
        a view. The position is in port coordinates.

        Returns a tuple consisting of the x and y port coodinates.
        """

    def mouseRay(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """mouseRay() -> (MPoint, MVector)

        This method returns the location of the mouse within
        a view. The location is defined by a point and a direction
        through the point. Both point and direction are in local
        space.

        Returns a tuple consisting the local space point and direction.
        """

    def mouseRayWorld(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """mouseRayWorld() -> (MPoint, MVector)

        This method returns the location of the mouse within
        a view. The location is defined by a point and a direction
        through the point. Both point and direction are in world
        space.

        Returns a tuple consisting the world space point and direction.
        """

    def mouseUp(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """mouseUp() -> (half, half)

        This method returns the mouse up position within
        a view. The position is in port coordinates.

        Returns a tuple consisting of the x and y port coodinates.
        """

    @staticmethod
    def newManipulator(*args: Unknown, **kwargs: Unknown) -> Any:
        """newManipulator(manipName) -> (MPxManipulatorNode, MObject)

        This static function is used to create a user-defined manipulator node.
        The manipObject argument is set to the new manipulator node.
        Note that the manipName argument must be the name of a
        manipulator derived from MPxManipulatorNode.
        Also note that this method creates the newManipulator
        but doesn't add it to the DAG.
        The primary use of this method is in conjunction with
        MPxSelectionContext.addManipulator, to add
        user-defined manipulators to a context.

        Returns a tuple consisting of new MPxManipulatorNode instance, 
        and the manipulator node.

        * manipName (string) - manipulator name
        """

    def preDrawUI(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """preDrawUI(view) -> None

        This method is used to setup some drawing data for drawing the manipulator
        in Viewport 2.0 . The data updated and cached in this function will be used later
        during 'drawUI()'.

        This method is only called when the manipulator needs to be drawn in Viewport 2.0.

        This method need only be overridden if custom data is needed for drawing in drawUI().
        If no such data is needed, this method may be left unimplemented.

        This function is empty in this base class.

        * view (M3dView) - The view in which to draw
        """

    def prevColor(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """prevColor() -> half

        This method returns the previously color used by the colorAndName() method.
        """

    def registerForMouseMove(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """registerForMouseMove() -> None

        This method registers this manipulator to receive mouse
        move events. When registered, the doMove() function will
        be invoked on mouse move events.
        """

    def selectedColor(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """selectedColor() -> half

        This method returns the color index of a selected component.
        """

    def setDoubleValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setDoubleValue(valueIndex, value) -> None

        This method is used for setting a floating point value associated with the
        manipulator.

        * valueIndex (int) - the index of the value to be set
        * value (float) - the value to set it to
        """

    def setHandleColor(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setHandleColor(drawManager, handleName, colorIndex) -> None

        This method is used to set the color of component that is being drawn next.
        The color will be correctly selected based on the component's state(highlighted, selected, etc.)

        * drawManager (MUIDrawManager) - The MUIDrawManager used to draw some simple UI
        * handleName (MGLuint) - The unique name (an unsigned int) of the component.
        * colorIndex (half) - The default color to use, as provided by one of the *Color()
                              methods in this class.  If the component is neither highlighted nor selected,
                              this colorIndex will be used.
        """

    def setPointValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setPointValue(valueIndex, value) -> None

        This method is used for setting an MPoint value associated with the
        manipulator.

        * valueIndex (int) - the index of the value to be set
        * value (MPoint) - the value to set it to
        """

    def setVectorValue(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setVectorValue(valueIndex, value) -> None

        This method is used for setting an MVector value associated with the
        manipulator.

        * valueIndex (int) - the index of the value to be set
        * value (MVector) - the value to set it to
        """

    def shouldDrawHandleAsSelected(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """shouldDrawHandleAsSelected(name) -> bool
        This function is obsolete, please use 'setHandleColor' instead

        This method can be used to find out if the handle should be drawn
        using the selected color instead of the regular one.

        * name (unsigned int) unique name of the component.

        Returns true if the handle is active or highlighted.
        """

    def xColor(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """xColor() -> half

        This method returns the color index of the x axis.
        """

    def yColor(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """yColor() -> half

        This method returns the color index of the y axis.
        """

    def zColor(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """zColor() -> half

        This method returns the color index of the z axis.
        """


class MPxSelectionContext(MPxContext):
    """Base class for interative selection tools."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def abortAction(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """abortAction() -> None

        This method is called when the abort key is pressed.
        The default abort key in Maya is the <b>escape</b> key.
        Users can override this method if they wish to perform
        certain operations when the abort key is pressed.
        """

    def addManipulator(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addManipulator(manipulator) -> None

        This method adds a manipulator to the context.

        * manipulator (MObject) - the manipulator to be added to the context.
        """

    def argTypeNumericalInput(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """argTypeNumericalInput(index) -> MSyntax.MArgType

        This method is used by the feedback line to determine what units to display.
        Users should override this method to return the appropriate
        argument type for the given index of the numeric input field.
        Specifically, this method should be overridden to return one of the following:

            <b>MSyntax.kNoArg</b> for no argument
            <b>MSyntax.kDistance</b> for linear units
            <b>MSyntax.kAngle</b> for angular units

        * index (int) - the index of the numerical input whose argument type is requested.
        """

    def deleteManipulators(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """deleteManipulators() -> None

        This method deletes all the manipulators that belong
        to the context.
        """

    def doDrag(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doDrag(event, drawManager, frameContext) -> None

        This method is called when a mouse drag event occurs.
        The base method does nothing and should be overridden if
        the user needs to do anything during a mouse drag.

        This method is called only when it is in either default viewport renderer
        or hardware viewport renderer, not viewport 2.0.

        The <b>event</b> can be used to get more explicit information
        about the drag such as the cursor location. See MEvent for
        more information.

        * event (MEvent) - The button drag event information.
        * drawManager (MUIDrawManager) - Draw manager to use to draw custom shape
        * frameContext (MFrameContext) - Context of the frame being rendered.
        """

    def doDragLegacy(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doDragLegacy(event) -> None

        This method is called when a mouse drag event occurs.
        The base method does nothing and should be overridden if
        the user needs to do anything during a mouse drag.

        This method is called only when it is in either default viewport renderer
        or hardware viewport renderer, not viewport 2.0.

        The <b>event</b> can be used to get more explicit information
        about the drag such as the cursor location. See MEvent for
        more information.

        * event (MEvent) - The button drag event information.

            DEPRECATED in 2023, please use doDrag.
        """

    def doHold(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doHold(event, drawManager, frameContext) -> None

        This method is called when a mouse button is pressed but
        before the mouse is dragged.
        The base method does nothing and should be overridden if the user needs
        to do anything on a button hold.

        This method is called only when it is in either default viewport renderer
        or hardware viewport renderer, not viewport 2.0.

        The <b>event</b> can be used to get more explicit information
        about the hold such as the button number. See MEvent for
        more information.

        * event (MEvent) - The button hold event information.
        * drawManager (MUIDrawManager) - Draw manager to use to draw custom shape
        * frameContext (MFrameContext) - Context of the frame being rendered.
        """

    def doHoldLegacy(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doHoldLegacy(event) -> None

        This method is called when a mouse button is pressed but
        before the mouse is dragged.
        The base method does nothing and should be overridden if the user needs
        to do anything on a button hold.

        This method is called only when it is in either default viewport renderer
        or hardware viewport renderer, not viewport 2.0.

        The <b>event</b> can be used to get more explicit information
        about the hold such as the button number. See MEvent for
        more information.

        * event (MEvent) - The button hold event information.

            DEPRECATED in 2023, please use doHold.
        """

    def doPress(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doPress(event, drawManager, frameContext) -> None

        This method is called when any mouse button is pressed.
        The base method does nothing and should be overridden if
        the user needs to do anything on a button press.

        This method is called only when it is in either default viewport renderer
        or hardware viewport renderer, not viewport 2.0.

        The <b>event</b> can be used to get more explicit information
        about the press such as the button number. See MEvent for
        more information.

        * event (MEvent) - The button press event information.
        * drawManager (MUIDrawManager) - Draw manager to use to draw custom shape
        * frameContext (MFrameContext) - Context of the frame being rendered.
        """

    def doPressLegacy(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doPressLegacy(event) -> None

        This method is called when any mouse button is pressed.
        The base method does nothing and should be overridden if
        the user needs to do anything on a button press.

        This method is called only when it is in either default viewport renderer
        or hardware viewport renderer, not viewport 2.0.

        The <b>event</b> can be used to get more explicit information
        about the press such as the button number. See MEvent for
        more information.

        * event (MEvent) - The button press event information.

            DEPRECATED in 2023, please use doPress.
        """

    def doRelease(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doRelease(event, drawManager, frameContext) -> None

        This method is called when any mouse button is released.
        The base method does nothing and should be overridden if
        the user needs to do anything on a button release.

        This method is called only when it is in either default viewport renderer
        or hardware viewport renderer, not viewport 2.0.

        The <b>event</b> can be used to get more explicit information
        about the release such as the button number. See MEvent for
        more information.

        * event (MEvent) - The button release event information.
        * drawManager (MUIDrawManager) - Draw manager to use to draw custom shape
        * frameContext (MFrameContext) - Context of the frame being rendered.
        """

    def doReleaseLegacy(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doReleaseLegacy(event) -> None

        This method is called when any mouse button is released.
        The base method does nothing and should be overridden if
        the user needs to do anything on a button release.

        This method is called only when it is in either default viewport renderer
        or hardware viewport renderer, not viewport 2.0.

        The <b>event</b> can be used to get more explicit information
        about the release such as the button number. See MEvent for
        more information.

        * event (MEvent) - The button release event information.

            DEPRECATED in 2023, please use doRelease.
        """

    def feedbackNumericalInput(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """feedbackNumericalInput() -> bool

        This method is called to update the numerical feedback.
        The format and values for the feedback line can be set through the
        methods in MFeedbackLine, specifically setFormat and setValue.
        The return value should indicate whether or not the numerical feedback
        has been provided.  The default return value is false.
        """

    def helpStateHasChanged(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """helpStateHasChanged(event) -> None

        This method is called whenever the help state may need to be
        updated.
        The base method does nothing and should be overriden if
        the user needs to change the help information based on events.

        The <b>event</b> can be used to get more explicit information
        about the event. See MEvent for more information.

        * event (MEvent) - The event information.
        """

    def image(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """image(index) -> string

        This method is used to retrieve an XPM icon image that has
        previously been set for this tool context. This icon image will be
        used to represent this tool context in various places including
        the tool bar and can be queried from mel using the contextInfo
        command.

        * index (ImageIndex) - the index of the image being retrieved; three image
        representations are permitted: kImage1, kImage2, kImage3.
        """

    def isSelecting(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """isSelecting() -> bool

        Determines whether an object is selected.
        returns True if an object(s) is selected, False otherwise.
        """

    def lastDragPoint(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """lastDragPoint() -> MPoint

        Returns the position of the last drag point.
        """

    def newToolCommand(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """newToolCommand() -> MPxToolCommand

        Create a new instance of the tool command associated with this context.
        The tool command (derived from MPxToolCommand) is the command that was
        registered along with the context command in.

        Returns a new instance of the MPxToolCommand.
        """

    def processNumericalInput(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """processNumericalInput(values, flags, isAbsolute) -> bool

        This method processes the input from the numerical input field.
        Users can override this method if they wish to process numerical input.
        For a given entry in the numeric input field, if the user types a dot '.',
        this indicates that the entry should not be modified.
        The overridden version of this method should take this into account
        using the ignoreEntry method with the flags that are passed in.
        The overridden version of this method should also process the numeric
        input as an absolute input or relative input depending on whether
        the isAbsolute flag is true or not.
        The return value should indicate whether or not the numerical input has
        been processed.

        * values (MDoubleArray) - the values from the numerical input field.
        * flags (MIntArray) - used in conjunction with the ignoreEntry method,
        determines whether or not a given entry should be ignored.
        * isAbsolute (bool) - whether or not the input should be interpreted as absolute.
        """

    def setAllowDoubleClickAction(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setAllowDoubleClickAction() -> None

        This method enables the support of double click smart selection for this context.
        """

    def setAllowPaintSelect(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setAllowPaintSelect() -> None

        This method enables drag selection mode for this context.
        """

    def setAllowPreSelectHilight(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setAllowPreSelectHilight() -> None

        This method enables the support of pre-selection highlight for this context.
        It needs to be called by the user-overriden MPxContext::toolOnSetup method.
        """

    def setAllowSoftSelect(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setAllowSoftSelect() -> None

        This method enables the support of soft selection for this context.
        """

    def setAllowSymmetry(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setAllowSymmetry() -> None

        This method enables the support of symmetrical selection for this context.
        """

    def setImage(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setImage(image, index) -> self

        This method is used to set an XPM icon image that is to be
        used to represent this tool context in various places
        including the tool bar and can be queried from mel using the
        contextInfo command.

        * image (string) - the name of an XPM file to be used as the icon.
        * index (ImageIndex) - the index of the image being set; three image
        representations are permitted: kImage1, kImage2, kImage3.
        """

    def startPoint(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """startPoint() -> MPoint

        Returns the position of the button press.
        """


class MPxSurfaceShapeUI:
    """(Deprecated: Please use MHWRender::MPxGeometryOverride, MHWRender::MPxSubSceneOverride, or MHWRender::MPxDrawOverride instead.)
    Base class for the UI portion of all user defined shapes.
    """
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def canDrawUV(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """canDrawUV() -> bool

        Called by Maya to determine if this surface shape supports UV drawing.
        """

    def drawUV(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """drawUV(view, info) -> self

        This method is called when the surface shape is selected and the texture view is open.  Users should override this method if their custom shape supports UVs.

        * view (M3dView) - Texture view in which to draw UVs.
        * info (MTextureEditorDrawInfo) - Drawing parameters.
        """

    kSelectMeshEdges: int = 3
    kSelectMeshFaces: int = 2
    kSelectMeshUVs: int = 0
    kSelectMeshVerts: int = 1
    def material(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """material(path) -> MMaterial

        COMMENT
        """

    def materials(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """materials(path, componentFilter, materials, componentSet=None) -> self

        Returns the material associated with this shape.
        The user must supply a DAG path as a shape can have several materials if instanced.

        * path (MDagPath) - the path for which to get the material
        """

    def select(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """select(selectInfo, selectionList, worldSpaceSelectPts) -> bool

        This routine must be overriden if the shape is to support interactive object and/or component selection. The implementation of this method should call selectInfo.addSelection with information about the selected item and its selection mask. For single click selection, detected using the selectInfo.singleSection() method, the hit point should also be passed as an argument to selectInfo.addSelection().

        Returns True if something was selected.

        * selectInfo (MSelectInfo) - the Selection state information.
        * selectionList [OUT] (MSelectionList) - List of items selected by this method. Do not update directly: use MSelectInfo.addSelection instead.
        * worldSpaceSelectPts [OUT] (MPointArray) - List of points used to sort corresponding selections in single-select mode. (Closest to camera wins.) Do not update directly: use MSelectInfo.addSelection instead.
        """

    def selectUV(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """selectUV(view, selType, xmin, ymin, xmax, ymax, singleSelect, selList) -> bool

        This method is called when the user performs a selection within the texture view.  The method is called only when the surface shape is member of the active selection list.

        Maya provides the current viewport instance, the type of the selection, the extents of the selection rectangle (in viewport coordinates), and if the selection mode is single selection. The API user is expected to fill the selection list and return a result of True if 'something was selected'.

        To properly use this method, you must make sure that you have a valid component type that Maya can recognize. Selection tests can be done using a pick buffer or by spatially determining the selected objects.

        Currently Maya does not know how to manipulate custom UV components. This method only provides the facilities to visualize what has been selected in the viewport.  The API user is responsible for implementing commands that can manipulate the currently selected UVs.

        Returns True if something was selected.

        * view (M3dView) - the texture drawing view
        * selType (int) - the selection type
        * xmin (int) - minimum x coordinate value of the selection rectangle.
        * ymin (int) - minimum y coordinate value of the selection rectangle.
        * xmax (int) - maximum x coordinate value of the selection rectangle.
        * ymax (int) - maximum y coordinate value of the selection rectangle.
        * singleSelect (bool) - indicates if the user is in single selection mode.
        * selList [OUT] (MSelectionList) - the selection list to be populated.

        Valid selection types:
          kSelectMeshUVs      The UV selection type is UVs.
          kSelectMeshVerts    The UV selection type is vertices.
          kSelectMeshFaces    The UV selection type is faces.
          kSelectMeshEdges    The UV selection type is edges.
        """

    def snap(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """snap(snapInfo) -> bool

        Maya calls this method when snapping to the shape's vertices.
        If you wish your custom shape to support point snapping then you must override this method and have it call snapInfo's MSelectInfo.setSnapPoint() method to set the point to be snapped to.
        If setSnapPoint() is called multiple times then the point closest to the cursor will be used.

        Returns True if a vertex was found to be snapped to was selected.

        * snapInfo (MSelectInfo) - the Selection state information.
        """

    def surfaceShape(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """surfaceShape() -> MPxSurfaceShape

        Returns the non-ui shape associated with current instance.
        """

    @staticmethod
    def surfaceShapeUI(*args: Unknown, **kwargs: Unknown) -> Any:
        """surfaceShapeUI(path) -> MPxSurfaceShapeUI

        This is a static method that can be used to find the corresponding MPxSurfaceShapeUI for the specified path.  If an MPxSurfaceShapeUI does not exist then one is created.

        This function can only be used for custom surface shapes and the function will return NULL if the provided path is not a custom surface shape.

        * path (MDagPath) - The full path to a surface shape, including the shape.
        """


class MPxToolCommand(maya.api.OpenMaya.MPxCommand):
    """Base class for custom tool commands."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def cancel(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """cancel() -> None

        This method cancels the command.
        The user should override this method when the original program state
        needs to be restored.
        """

    def doFinalize(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """doFinalize() -> None

        Call this method with an MArgList representing your command.
        This method will register the command with the undo manager
        for journalling.

        * command (MArgList) Reference representing an equivalent
        """

    def doIt(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Called by Maya to execute the command."""

    def finalize(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """finalize() -> None

        This method is used to create a string representing the command
        and its arguments.
        Users should override this method and contruct an MArgList and
        then pass it to <b>doFinalize</b> for journalling.
        """


class MSelectInfo(MDrawInfo):
    """(Deprecated: Please use MHWRender::MPxGeometryOverride, MHWRender::MPxSubSceneOverride, or MHWRender::MPxDrawOverride instead.)
    Selection state information used in MPxSurfaceShapeUI.select.
    """
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addSelection(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """addSelection(item, point, list, points, mask, isComponent) -> self

        Adds components or objects to the active selection list.

        * item (MSelectionList) - The component or object to add to the list
        * point (MPoint) - The world space point representing the selected object. This is used during single-click selection when the click overlaps multiple objects in order to determine which point is closest to the camera.
        * list [OUT] (MSelectionList) - The selection list to add the item(s) to
        * points [OUT] (MPointArray) - A copy of the points of all currently selected components in the list (if components are selected)
        * mask (MSelectionMask) - Mask used to determine selection priority
        * isComponent (bool) - Indicates whether item to be added is an object or a component
        """

    def getAlignmentMatrix(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getAlignmentMatrix() -> MMatrix

        Returns the alignment matrix.
        This method is used to find ray object intersection.
        """

    def getLocalRay(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """getLocalRay() -> [MPoint, MVector]

        Returns the selection ray defined by its starting point (MPoint) and its direction (MVector).
        This method is used to find ray object intersection.
        """

    highestPriority: Any
    def isRay(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """isRay() -> bool

        Returns True if there is a selection ray.
        This method isused to find ray object intersection.
        """

    def selectClosest(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """selectClosest() -> bool

        Returns True if we want to select the closest object.
        """

    def selectForHilite(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """selectForHilite(mask) -> bool

        Given the selection mask, can this object be selected for the hilite list.

        * mask (MSelectionMask) - the mask to test
        """

    def selectOnHilitedOnly(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """selectOnHilitedOnly() -> bool

        Returns True if you can only select components if the object is hilited.
        """

    def selectPath(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """selectPath() -> MDagPath

        Returns a path to the item that is being selected.
        """

    def selectRect(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """selectRect() -> [int, int, int, int]

        Get the current selection rectangle dimensions, defined by:
          its lower left corner - x coordinate,
          its lower left corner - y coordinate,
          its width,
          its height.
        """

    def selectable(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """selectable(mask) -> bool

        Given the selection mask, this method determines if the object is selectable.

        * mask (MSelectionMask) - the mask to test
        """

    def selectableComponent(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """selectableComponent(displayed, mask) -> bool

        Given the selection mask, this method determines if the component is selectable.

        * displayed (bool) - is the component displayed
        * mask (MSelectionMask) - selection mask
        """

    def setSnapPoint(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """setSnapPoint(point) -> bool

        When a snapping operation is being performed the shape's overridden MPxSurfaceShapeUI.snap() method can call this method to set the point to be snapped to. If setSnapPoint() is called multiple times then the point passed in which is nearest to the current cursor location will be used. So the shape can either compute the snap point itself and call setSnapPoint() once or it can make a series of calls and let setSnapPoint() determine the closest of those for itself.

        * point (MPoint) - The point to be snapped to, must be given in world space coordinates.
        """

    def singleSelection(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """singleSelection() -> bool

        This method determines if we want to select a single object.
        """

    def view(self, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """view() -> M3dView

        Returns the view that the current selection is taking place in.
        """


class MTextureEditorDrawInfo:
    """Drawing state for drawing to the UV texture window with custom shapes."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    drawingFunction: int
    kDrawEdgeForSelect: int = 4
    kDrawEverything: int = 2
    kDrawFacetForSelect: int = 5
    kDrawFunctionFirst: int = 1
    kDrawFunctionLast: int = 6
    kDrawUVForSelect: int = 6
    kDrawVertexForSelect: int = 3
    kDrawWireframe: int = 1

class MTimeSliderCustomDrawManager:
    """Manager to add drawing primitive to the time slider."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def clearDrawPrimitives(self, /, *args: Unknown, **kwargs: Unknown) -> Any: ...
    def deregisterCustomDraw(self, /, *args: Unknown, **kwargs: Unknown) -> Any: ...
    kAbove: int = 0
    kBelow: int = 1
    kOn: int = 2
    def registerCustomDrawOn(self, /, *args: Unknown, **kwargs: Unknown) -> Any: ...
    def registerCustomDrawOutside(self, /, *args: Unknown, **kwargs: Unknown) -> Any: ...
    def requestTimeSliderRedraw(self, /, *args: Unknown, **kwargs: Unknown) -> Any: ...
    def setBackgroundColor(self, /, *args: Unknown, **kwargs: Unknown) -> Any: ...
    def setDrawHeight(self, /, *args: Unknown, **kwargs: Unknown) -> Any: ...
    def setDrawLayer(self, /, *args: Unknown, **kwargs: Unknown) -> Any: ...
    def setDrawLocation(self, /, *args: Unknown, **kwargs: Unknown) -> Any: ...
    def setDrawPrimitives(self, /, *args: Unknown, **kwargs: Unknown) -> Any: ...
    def setDrawPriority(self, /, *args: Unknown, **kwargs: Unknown) -> Any: ...
    def setDrawVisible(self, /, *args: Unknown, **kwargs: Unknown) -> Any: ...
    def setEditPrimitiveFunction(self, /, *args: Unknown, **kwargs: Unknown) -> Any: ...
    def setStartPrimitiveEditFunction(self, /, *args: Unknown, **kwargs: Unknown) -> Any: ...
    def setStopPrimitiveEditFunction(self, /, *args: Unknown, **kwargs: Unknown) -> Any: ...
    def setTooltip(self, /, *args: Unknown, **kwargs: Unknown) -> Any: ...

class MTimeSliderDrawPrimitive:
    """Primitive to be drawn set in a context with MTimeSiderCustomDrawManager."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    bottom: Any
    color: Any
    drawType: Any
    endTime: Any
    height: Any
    kBracket: int = 4
    kFilledRect: int = 0
    kFrameFlag: int = 5
    kFullOutline: int = 2
    kMoveEndTime: int = 3
    kMovePrimitive: int = 1
    kMoveStartTime: int = 2
    kNone: int = 0
    kUpperOutline: int = 1
    kVerticalLine: int = 3
    label: Any
    priority: Any
    startTime: Any
    tooltip: Any

class MUiMessage(maya.api.OpenMaya.MMessage):
    """Class used to register callbacks for UI related messages."""
    @staticmethod
    def add3dViewDestroyMsgCallback(*args: Unknown, **kwargs: Unknown) -> Any:
        """add3dViewDestroyMsgCallback(panelName, function, clientData=None) -> id

                This method registers a callback for when a particular 3d view gets
        destroyed. The callback is called before the destruction of the view.

        The callback function will be passed any client data that was
        provided when the callback was registered

         * panelName (string) - Name of panel to which to attach the callback
         * function - callable which will be passed a string indicating the name
           of the panel that contain the 3d view and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    @staticmethod
    def add3dViewPostRenderMsgCallback(*args: Unknown, **kwargs: Unknown) -> Any:
        """add3dViewPostRenderMsgCallback(panelName, function, clientData=None) -> id

        This method registers a callback for when the 3d view is
        about to display it's rendered contents to the viewport.
        It is called for every refresh of the view, after the scene is drawn,
        but before any 2d adornments are drawn.

        The callback function will be passed any client data that was
        provided when the callback was registered.

         * panelName (string) - Name of panel to which to attach the callback
         * function - callable which will be passed a string indicating the name
           of the panel that contain the 3d view and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    @staticmethod
    def add3dViewPreRenderMsgCallback(*args: Unknown, **kwargs: Unknown) -> Any:
        """add3dViewPreRenderMsgCallback(panelName, function, clientData=None) -> id

        This method registers a callback for when a particular 3d view is
        about to render it's contents. It is called before the scene is drawn,
        but after the background has been drawn.

        The callback function will be passed any client data that was
        provided when the callback was registered.

         * panelName (string) - Name of panel to which to attach the callback
         * function - callable which will be passed a string indicating the name
           of the panel that contain the 3d view and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    @staticmethod
    def add3dViewRenderOverrideChangedCallback(*args: Unknown, **kwargs: Unknown) -> Any:
        """add3dViewRenderOverrideChangedCallback(panelName, function, clientData=None) -> id

        This method registers a callback for when the render override for a
        particular 3d view changes.

        The callback function will be passed any client data that was
        provided when the callback was registered.

         * panelName (string) - Name of panel to which to attach the callback
         * function - callable which will be passed 3 strings indicating: the name of
           the panel that contain the 3d view, the name of the old override used to draw
           in the 3d view, the name of the new override used to draw in the 3d view
           , and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    @staticmethod
    def add3dViewRendererChangedCallback(*args: Unknown, **kwargs: Unknown) -> Any:
        """add3dViewRendererChangedCallback(panelName, function, clientData=None) -> id

        This method registers a callback for when the renderer for a particular 3d
        view changes.

        The callback function will be passed any client data that was
        provided when the callback was registered.

         * panelName (string) - Name of panel to which to attach the callback
         * function - callable which will be passed 3 strings indicating: the name
           of the panel that contain the 3d view, the name of the old renderer used
           to draw the 3d view, the name of the new renderer used to draw the 3d view
           , and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    @staticmethod
    def addCameraChangedCallback(*args: Unknown, **kwargs: Unknown) -> Any:
        """addCameraChangedCallback(panelName, function, clientData=None) -> id

        This method registers a callback for cameras being changed in
        3d views.  The callback is called when the camera changes for the
        given panel, not when attributes on the panel's camera change.

        The callback function will be passed any client data that was
        provided when the callback was registered.

         * panelName (string) - the name of panel to which to attach the
           callback.
         * function - callable which will be passed a string indicating the
           name of the panel that had the camera change, a MObject containing
           the current camera used by the panel and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    @staticmethod
    def addUiDeletedCallback(*args: Unknown, **kwargs: Unknown) -> Any:
        """addUiDeletedCallback(uiName, function, clientData=None) -> id

        This method registers a callback for UI deleted messages.
        The callback function will be passed any client data that was
        provided when the callback was registered.

         * uiName (string) - the name of the UI object to register the
           callback for
         * function - callable which will be passed the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """


class RenderParameters:
    """Provides information on how to render the image."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    baseColor: maya.api.OpenMaya.MColor
    showAlphaMask: bool
    unfiltered: bool

class ShaderContext:
    """Provides contextual information about the current invocation of the shader."""
    def __init__(self, /, *args: Unknown, **kwargs: Unknown) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(cls, /, *args: Unknown, **kwargs: Unknown) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    path: maya.api.OpenMaya.MDagPath
    shadingEngine: maya.api.OpenMaya.MObject

key: str = '__file__'
ourdict: Dict[str, Any]
py2dict: Dict[str, Any]
val: str = '/usr/autodesk/maya2024/lib/python3.10/site-packages/maya/api/_OpenMayaUI_py2.so'
