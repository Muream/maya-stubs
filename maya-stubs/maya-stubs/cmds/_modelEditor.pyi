from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def modelEditor(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., activeComponentsXray: bool = ..., activeCustomEnvironment: str = ..., activeCustomGeometry: Queryable[str] = ..., activeCustomLighSet: Queryable[str] = ..., activeCustomOverrideGeometry: Queryable[str] = ..., activeCustomRenderer: Queryable[str] = ..., activeOnly: bool = ..., activeShadingGraph: Queryable[str] = ..., activeView: bool = ..., addObjects: str = ..., addSelected: bool = ..., addSelectedObjects: bool = ..., allObjects: bool = ..., backfaceCulling: bool = ..., bluePencil: bool = ..., bufferMode: Queryable[str] = ..., bumpResolution: Queryable[Tuple[int, int]] = ..., camera: Queryable[str] = ..., cameraName: str = ..., cameraSet: Queryable[str] = ..., cameraSetup: bool = ..., cameras: bool = ..., capture: Queryable[str] = ..., captureSequenceNumber: Queryable[int] = ..., clipGhosts: bool = ..., cmEnabled: bool = ..., colorMap: bool = ..., colorResolution: Queryable[Tuple[int, int]] = ..., control: bool = ..., controlVertices: bool = ..., cullingOverride: Queryable[str] = ..., default: bool = ..., defineTemplate: str = ..., deformers: bool = ..., dimensions: bool = ..., displayAppearance: Queryable[str] = ..., displayLights: Queryable[str] = ..., displayTextures: bool = ..., docTag: Queryable[str] = ..., dynamicConstraints: bool = ..., dynamics: bool = ..., editorChanged: Queryable[Callable[..., Any]] = ..., excludeObjectMask: Queryable[int] = ..., excludeObjectPreset: Queryable[str] = ..., excludePluginList: Queryable[Multiuse[str]] = ..., exists: bool = ..., exposure: Queryable[float] = ..., filter: Queryable[str] = ..., filteredObjectList: bool = ..., fluids: bool = ..., fogColor: Queryable[Tuple[float, float, float, float]] = ..., fogDensity: Queryable[float] = ..., fogEnd: Queryable[float] = ..., fogMode: Queryable[str] = ..., fogSource: Queryable[str] = ..., fogStart: Queryable[float] = ..., fogging: bool = ..., follicles: bool = ..., forceMainConnection: Queryable[str] = ..., gamma: Queryable[float] = ..., greasePencils: bool = ..., grid: bool = ..., hairSystems: bool = ..., handles: bool = ..., headsUpDisplay: bool = ..., height: bool = ..., highlightConnection: Queryable[str] = ..., hulls: bool = ..., ignorePanZoom: bool = ..., ikHandles: bool = ..., imagePlane: bool = ..., interactive: bool = ..., interactiveBackFaceCull: bool = ..., interactiveDisableShadows: bool = ..., isFiltered: bool = ..., jointXray: bool = ..., joints: bool = ..., lights: bool = ..., lineWidth: Queryable[float] = ..., locators: bool = ..., lockMainConnection: bool = ..., lowQualityLighting: bool = ..., mainListConnection: Queryable[str] = ..., manipulators: bool = ..., maxConstantTransparency: Queryable[float] = ..., maximumNumHardwareLights: bool = ..., modelPanel: str = ..., motionTrails: bool = ..., nCloths: bool = ..., nParticles: bool = ..., nRigids: bool = ..., noUndo: bool = ..., nurbsCurves: bool = ..., nurbsSurfaces: bool = ..., objectFilter: Queryable[Callable[..., Any]] = ..., objectFilterList: Queryable[Callable[..., Any]] = ..., objectFilterListUI: Queryable[Callable[..., Any]] = ..., objectFilterShowInHUD: bool = ..., objectFilterUI: Queryable[Callable[..., Any]] = ..., occlusionCulling: bool = ..., panel: Queryable[str] = ..., parent: Queryable[str] = ..., particleInstancers: bool = ..., pivots: bool = ..., planes: bool = ..., pluginObjects: Multiuse[Tuple[str, bool]] = ..., pluginShapes: bool = ..., polymeshes: bool = ..., queryPluginObjects: Queryable[str] = ..., removeSelected: bool = ..., rendererDeviceName: bool = ..., rendererList: bool = ..., rendererListUI: bool = ..., rendererName: Queryable[str] = ..., rendererOverrideList: bool = ..., rendererOverrideListUI: bool = ..., rendererOverrideName: Queryable[str] = ..., resetCustomCamera: bool = ..., sceneRenderFilter: Queryable[str] = ..., selectionConnection: Queryable[str] = ..., selectionHiliteDisplay: bool = ..., setSelected: bool = ..., shadingModel: Queryable[int] = ..., shadows: bool = ..., smallObjectCulling: bool = ..., smallObjectThreshold: Queryable[float] = ..., smoothWireframe: bool = ..., sortTransparent: bool = ..., stateString: bool = ..., stereoDrawMode: bool = ..., strokes: bool = ..., subdivSurfaces: bool = ..., textureAnisotropic: bool = ..., textureCompression: bool = ..., textureDisplay: Queryable[str] = ..., textureEnvironmentMap: bool = ..., textureHilight: bool = ..., textureMaxSize: Queryable[int] = ..., textureMemoryUsed: bool = ..., textureSampling: Queryable[int] = ..., textures: bool = ..., toggleExposure: bool = ..., toggleGamma: bool = ..., transpInShadows: bool = ..., transparencyAlgorithm: Queryable[str] = ..., twoSidedLighting: bool = ..., unParent: bool = ..., unlockMainConnection: bool = ..., updateColorMode: bool = ..., updateMainConnection: bool = ..., useBaseRenderer: bool = ..., useColorIndex: bool = ..., useDefaultMaterial: bool = ..., useInteractiveMode: bool = ..., useRGBImagePlane: bool = ..., useReducedRenderer: bool = ..., useTemplate: str = ..., userNode: Queryable[str] = ..., viewObjects: bool = ..., viewSelected: bool = ..., viewTransformName: Queryable[str] = ..., viewType: bool = ..., width: bool = ..., wireframeBackingStore: bool = ..., wireframeOnShaded: bool = ..., xray: bool = ...) -> Union[str, bool, Tuple[int, int], int, Callable[..., Any], Multiuse[str], float, Tuple[float, float, float, float]]:
    """Create, edit or query a model editor.Note that some of the flags of this command may have different settings
    for normal mode and for interactive/playback mode.  For example, a
    modelEditor can be set to use shaded mode normally, but to use wireframe
    during playback for greater speed.  Some flags also support having
    defaults set so that new model editors will be created with those settings.
    Args:
        activeComponentsXray (bool?): Turns on or off Xray mode for active components.  
                Properties: query, edit
        activeCustomEnvironment (str?): Specifies a path to an image file to be used as environment map.  
                It is only enabled when a valid scene render filter is specified.  
                Properties: edit
        activeCustomGeometry (Queryable[str]?): Specifies an identifier for custom geometry to override the geometry  
                to display. It is only enabled when a valid scene render filter is specified.  
                Properties: query, edit
        activeCustomLighSet (Queryable[str]?): Specifies an identifier for the light set to use  
                with a scene render filter. It is only enabled when a valid scene render filter is specified.  
                Properties: query, edit
        activeCustomOverrideGeometry (Queryable[str]?): Specifies an identifier for an override on the custom geometry for a scene  
                render filter.  
                Properties: query, edit
        activeCustomRenderer (Queryable[str]?): Specifies an identifier for custom renderer to use when  
                a valid scene render filter is also specified.  
                Properties: query, edit
        activeOnly (bool?): Sets whether only active objects should appear shaded in  
                shaded display.  
                Properties: query, edit
        activeShadingGraph (Queryable[str]?): Specifies the shading graph to use to override material display.  
                Only enabled when a valid scene render filter is specified.  
                Properties: query, edit
        activeView (bool?): Sets this model editor to be the active view.  Returns true  
                if successful.  On query this flag will return whether the view is  
                the active view.  
                Properties: query, edit
        addObjects (str?): This flag causes the objects contained within the selection  
                connection to be added to the list of objects visible in the view  
                (if viewSelected is true).  
                Properties: edit
        addSelected (bool?): This flag causes the currently active objects to be added  
                to the list of objects visible in the view (if viewSelected is true).  
                Properties: edit
        addSelectedObjects (bool?): If set then add the selected objects to the editor  
                Properties: create
        allObjects (bool?): Turn on/off the display of all objects for the view of  
                the model editor. This excludes NURBS, CVs, hulls, grids and  
                manipulators.  
                Properties: query, edit
        backfaceCulling (bool?): Turns on or off backface culling for the whole view.  This  
                setting overrides the culling settings of individual objects.  All  
                objects draw in the view will be backface culled.  When backface  
                culling is turned on, surfaces becomes invisible in areas where the  
                normal is pointing away from the camera.  
                Properties: query, edit
        bluePencil (bool?): Define whether the blue pencil should be added or not  
                Properties: create, query, edit
        bufferMode (Queryable[str]?): Deprecated: this is not supported in Viewport 2.0.  Sets the  
                graphic buffer mode.  Possible values are "single" or "double".  
                Properties: query, edit
        bumpResolution (Queryable[Tuple[int, int]]?): Set the resolution for "baked" bump map textures when using the  
                hardware renderer. The default value is 512, 512 respectively.  
                Properties: query, edit
        camera (Queryable[str]?): Change or query the name of the camera in model editor.  
                Properties: query, edit
        cameraName (str?): Set the name of the panel's camera transform and shape. The  
                shape name is computed by appending the string "Shape" to the  
                transform name. This flag may not be queried.  
                Properties: create, edit
        cameraSet (Queryable[str]?): Name of the camera set  
                Properties: create, query, edit
        cameraSetup (bool?): Based on the model editor name passed in will  
                returns a string list containing camera setups.  
                A camera setup can contain one or more cameras  
                which are associated with each other.  
                Camera setups are defined as pairs of consecutive  
                strings in the list. Each pair is comprised of:  
                a string which identifies an active camera,  
                and a string which defines a script  
                to set up a given active camera. As many pairs of strings  
                can be returned as the number of active cameras. If nothing  
                is returned then it is assumed that no set up is  
                required to activate a given camera.  
                Properties: query
        cameras (bool?): Turn on/off the display of cameras for the view of the  
                model editor.  
                Properties: query, edit
        capture (Queryable[str]?): Perform an one-time capture of the viewport to the named image file on disk.  
                Properties: query, edit
        captureSequenceNumber (Queryable[int]?): When a number greater or equal to 0 is specified each subsequent refresh will  
                save an image file to disk if the capture flag has been enabled.  
              
                The naming of the file is:  
              
                {root name}.#.{extension}  
              
                if the name {root name}.{extension} is used for the capture flag argument.  
              
                The value of # starts at the number specified to for this argument and  
                increments for each subsequent refresh.  
              
                Sequence capture can be disabled by specifying a number less than 0 or an  
                empty file name for the capture flag.  
                Properties: query, edit
        clipGhosts (bool?): Define whether the clip ghosts should be added or not  
                Properties: create, query, edit
        cmEnabled (bool?): Turn on or off applying color management in the editor.  If set, the color  
                management configuration set in the current editor is used.  
                Properties: query, edit
        colorMap (bool?): Queries the color map style for the model panel. Possible  
                values are "colorIndex" and "rgb".  
                Properties: query
        colorResolution (Queryable[Tuple[int, int]]?): Set the resolution for "baked" color textures when using the  
                hardware renderer. The default value is 256, 256 respectively.  
                Properties: query, edit
        control (bool?): Query only. Returns the top level control for this editor.  
                Usually used for getting a parent to attach popup menus.  
                Caution: It is possible for an editor to exist without a  
                control. The query will return "NONE" if no control is present.  
                Properties: query
        controlVertices (bool?): Turn on/off the display of NURBS CVs for the view of the  
                model editor.  
                Properties: query, edit
        cullingOverride (Queryable[str]?): Set whether to override the culling attributes on objects when using  
                the hardware renderer. The options are:  
              
                "none" : Use the culling object attributes per object.  
                "doubleSided" : Force all objects to be double sided.  
                "singleSided": Force all objects to be single sided.  
              
                The default value is "none".  
                Properties: query, edit
        default (bool?): Causes this command to modify the default value of this setting.  
                Newly created model editors will inherit the values.  This flag may  
                be used with the -interactive to set default interactive settings.  
                Properties: query, edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        deformers (bool?): Turn on/off the display of deformer objects for the view  
                of the model editor.  
                Properties: query, edit
        dimensions (bool?): Turn on/off the display of dimension objects for the view  
                of the model editor.  
                Properties: query, edit
        displayAppearance (Queryable[str]?): Sets the display appearance of the model panel.  Possible  
                values are "wireframe", "points", "boundingBox", "smoothShaded",  
                "flatShaded".  This flag may be used with the -interactive  
                and -default flags.  Note that only "wireframe", "points", and  
                "boundingBox" are valid for the interactive mode.  
                Properties: query, edit
        displayLights (Queryable[str]?): Sets the lighting for shaded mode.  Possible values are  
                "selected", "active", "all", "default", "none".  
                Properties: query, edit
        displayTextures (bool?): Turns on or off display of textures in shaded mode  
                Properties: query, edit
        docTag (Queryable[str]?): Attaches a tag to the editor.  
                Properties: create, query, edit
        dynamicConstraints (bool?): Turn on/off the display of dynamicConstraints for the view  
                of the model editor.  
                Properties: query, edit
        dynamics (bool?): Turn on/off the display of dynamics objects for the view  
                of the model editor.  
                Properties: query, edit
        editorChanged (Queryable[Callable[..., Any]]?): An optional script callback which is called when the editors  
                options have changed.  This is useful in a situation where a scripted  
                panel contains a modelEditor and wants to be notified when the contained  
                editor changes its options.  
                Properties: create, query, edit
        excludeObjectMask (Queryable[int]?): Set exclude object display settings for all individual objects at once using  
                a integer mask.  
                Properties: create, query, edit
        excludeObjectPreset (Queryable[str]?): Set exclude object display settings for all individual objects at once using  
                a named preset.  
                Properties: create, query, edit
        excludePluginList (Queryable[Multiuse[str]]?): Set exclude object display settings for a plugin object.  
                Properties: create, query, edit, multiuse
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        exposure (Queryable[float]?): The exposure value used by the color management of the current editor.  
                Properties: query, edit
        filter (Queryable[str]?): Specifies the name of an itemFilter object to be used with this editor.  
                This filters the information coming onto the main list  
                of the editor.  
                Properties: create, query, edit
        filteredObjectList (bool?): For model editors with filtering on (either using an object filter, or isolate  
                select), this flag returns a string list of the objects which are displayed in  
                this editor. Note that this list does not take into account visibility (based on  
                camera frustum or flags), it purely captures the objects which are considered  
                when rendering the view.  
                Properties: query
        fluids (bool?): Turn on/off the display of fluids for the view  
                of the model editor.  
                Properties: query, edit
        fogColor (Queryable[Tuple[float, float, float, float]]?): The color used for hardware fogging.  
                Properties: query, edit
        fogDensity (Queryable[float]?): Determines the density of hardware fogging.  
                Properties: query, edit
        fogEnd (Queryable[float]?): The end location of hardware fogging.  
                Properties: query, edit
        fogMode (Queryable[str]?): This determines the drop-off mode for fog. The possibilities are:  
              
                "linear" : linear drop-off  
                "exponent" : exponential drop-off  
                "exponent2" : squared exponential drop-off  
                Properties: query, edit
        fogSource (Queryable[str]?): Set the type of fog algorithm to use. If the argument  
                is "fragment" (default) then fog is computed per pixel. If  
                the argument is "coordinate" then if the geometry has  
                specified vertex fog coordinates, and the OpenGL extension  
                for vertex fog is supported by the graphics system, then  
                fog is computed per vertex.  
                Properties: query, edit
        fogStart (Queryable[float]?): The start location of hardware fogging.  
                Properties: query, edit
        fogging (bool?): Set whether hardware fogging is enabled or not.  
                Properties: query, edit
        follicles (bool?): Turn on/off the display of follicles for the view  
                of the model editor.  
                Properties: query, edit
        forceMainConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will use as its source of content. The editor will only  
                display items contained in the selectionConnection object. This is  
                a variant of the -mainListConnection flag in that it will force a  
                change even when the connection is locked. This flag is used to  
                reduce the overhead when using the -unlockMainConnection  
                , -mainListConnection, -lockMainConnection flags in immediate  
                succession.  
                Properties: create, query, edit
        gamma (Queryable[float]?): The gamma value used by the color management of the current editor.  
                Properties: query, edit
        greasePencils (bool?): Define whether the grease pencil marks should be added or not  
                Properties: create, query, edit
        grid (bool?): Turn on/off the display of the grid for the view of the  
                model editor.  
                Properties: query, edit
        hairSystems (bool?): Turn on/off the display of hairSystems for the view  
                of the model editor.  
                Properties: query, edit
        handles (bool?): Turn on/off the display of select handles for the view  
                of the model editor.  
                Properties: query, edit
        headsUpDisplay (bool?): Sets whether the model panel will draw any enabled heads up  
                display	elements in this window (if true).  Currently this requires  
                the HUD elements to be globally enabled.  
                Properties: query, edit
        height (bool?): Return the height of the associated viewport in pixels  
                Properties: query
        highlightConnection (Queryable[str]?): Specifies the name of a selectionConnection object that  
                the editor will synchronize with its highlight list. Not all  
                editors have a highlight list. For those that do, it is a secondary  
                selection list.  
                Properties: create, query, edit
        hulls (bool?): Turn on/off the display of NURBS hulls for the view of the  
                model editor.  
                Properties: query, edit
        ignorePanZoom (bool?): Sets whether the model panel will ignore the 2D pan/zoom value to  
                give an overview of the scene.  
                Properties: query, edit
        ikHandles (bool?): Turn on/off the display of ik handles and end effectors  
                for the view of the model editor.  
                Properties: query, edit
        imagePlane (bool?): Turn on/off the display of image plane for the view  
                Properties: query, edit
        interactive (bool?): Causes this command to modify the interactive refresh settings of  
                the view.  In this way it is possible to change the behavior of the  
                model editor during playback for improved performance.  
                Properties: query, edit
        interactiveBackFaceCull (bool?): Define whether interactive backface culling should be on or not  
                Properties: create, query, edit
        interactiveDisableShadows (bool?): Define whether interactive shadows should be disabled or not  
                Properties: create, query, edit
        isFiltered (bool?): Returns true for model editors with filtering applied to their view of the  
                scene. This could either be an explicit object filter, or a display option such  
                as isolate select which filters the objects that are displayed.  
                Properties: query
        jointXray (bool?): Turns on or off Xray mode for joints.  
                Properties: query, edit
        joints (bool?): Turn on/off the display of joints for the view of the  
                model editor.  
                Properties: query, edit
        lights (bool?): Turn on/off the display of lights for the view of the  
                model editor.  
                Properties: query, edit
        lineWidth (Queryable[float]?): Set width of lines for display  
                Properties: query, edit
        locators (bool?): Turn on/off the display of locator objects for the view  
                of the model editor.  
                Properties: query, edit
        lockMainConnection (bool?): Locks the current list of objects within the mainConnection,  
                so that only those objects are displayed within the editor.  
                Further changes to the original mainConnection are ignored.  
                Properties: create, edit
        lowQualityLighting (bool?): Set whether to use "low quality lighting" when using the  
                hardware renderer. The default value is false.  
                Properties: query, edit
        mainListConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will use as its source of content. The editor will  
                only display items contained in the selectionConnection object.  
                Properties: create, query, edit
        manipulators (bool?): Turn on/off the display of manipulator objects for the view  
                of the model editor.  
                Properties: query, edit
        maxConstantTransparency (Queryable[float]?): Sets the maximum constant transparency.  Setting this value remaps  
                constant transparency values from the range [0.0, 1.0] to the range  
                [0.0, maxConstantTransparency]. All transparency values are shifted  
                linearly to the new range, so a fully transparency object  
                (transparency 1.0) would  
                appear with a transparency of maxConstantTransparency in the viewport,  
                allowing highly transparent objects to be made visible.  This flag only  
                affects constant (non-textured) transparent objects.  
                Properties: query, edit
        maximumNumHardwareLights (bool?): Define whether the hardware light maximum should be respected or not  
                Properties: create, query, edit
        modelPanel (str?): Allows the created model editor to be embedded in the named model panel.  
                Intended for use with custom model editors created via the API (i.e. the  
                flag would be used on the derived MPxModelEditorCommand), though the flag  
                may also be used on the base modelEditor command to restore a default Maya  
                model editor to the panel.  
                Note that the model editor previously owned by the panel is deleted.  
                Properties: create
        motionTrails (bool?): Turn on/off the Motion Trail display in the Viewport.  
                Properties: query, edit
        nCloths (bool?): Turn on/off the display of nCloths for the view  
                of the model editor.  
                Properties: query, edit
        nParticles (bool?): Turn on/off the display of nParticles for the view  
                of the model editor.  
                Properties: query, edit
        nRigids (bool?): Turn on/off the display of nRigids for the view  
                of the model editor.  
                Properties: query, edit
        noUndo (bool?): This flag prevents some viewport operations (such as isolate  
                select) from being added to the undo queue.  
                Properties: edit
        nurbsCurves (bool?): Turn on/off the display of nurbs curves for the view  
                of the model editor.  
                Properties: query, edit
        nurbsSurfaces (bool?): Turn on/off the display of nurbs surfaces for the view  
                of the model editor.  
                Properties: query, edit
        objectFilter (Queryable[Callable[..., Any]]?): Set or query the current object filter name. An object filter  
                is required to have already been registered.  
                Properties: query, edit
        objectFilterList (Queryable[Callable[..., Any]]?): Return a list of names of registered filters.  
                Properties: query
        objectFilterListUI (Queryable[Callable[..., Any]]?): Return a list of UI names of registered filters.  
                Properties: query
        objectFilterShowInHUD (bool?): Sets whether or not to display the object filter UI name in the heads  
                up display when an object filter is active. This string is concatenated  
                with the camera name.  
                Properties: query, edit
        objectFilterUI (Queryable[Callable[..., Any]]?): Query the current object filter UI name. The object filter  
                is required to have already been registered.  
                Properties: query
        occlusionCulling (bool?): Set whether to enable occlusion culling testing when using  
                the hardware renderer. The default value is false.  
                Properties: query, edit
        panel (Queryable[str]?): Specifies the panel for this editor. By default if  
                an editor is created in the create callback of a scripted panel it  
                will belong to that panel. If an editor does not belong to a panel  
                it will be deleted when the window that it is in is deleted.  
                Properties: create, query
        parent (Queryable[str]?): Specifies the parent layout for this editor. This flag will only  
                have an effect if the editor is currently un-parented.  
                Properties: create, query, edit
        particleInstancers (bool?): Define whether the particle instances should be shown or not  
                Properties: create, query, edit
        pivots (bool?): Turn on/off the display of transform pivots for the view  
                of the model editor.  
                Properties: query, edit
        planes (bool?): Turn on/off the display of sketch planes for the view  
                of the model editor.  
                Properties: query, edit
        pluginObjects (Multiuse[Tuple[str, bool]]?): Turn on/off the display of plug-in objects for the view.  
                It depends on the plug-in implementation whether to respect this flag.  
                Properties: edit, multiuse
        pluginShapes (bool?): Turn on/off the display of plug-in shapes for the view.  
                It depends on the plug-in implementation whether to respect this flag.  
                Properties: edit
        polymeshes (bool?): Turn on/off the display of polygon meshes for the view  
                of the model editor.  
                Properties: query, edit
        queryPluginObjects (Queryable[str]?): Query the on/off state of plug-in objects display for the view.  
                To set the on/off state, use -pluginObjects instead.  
                Properties: query
        removeSelected (bool?): This flag causes the currently active objects to be removed  
                from the list of objects visible in the view (if viewSelected is true).  
                Properties: edit
        rendererDeviceName (bool?): Query for the name of the draw API used by the Viewport 2.0 renderer for a 3d modeling viewport.  
                The possible return values are "VirtualDeviceGL" if Maya is set to use "OpenGL - Legacy" for Viewport 2.0,  
                "VirtualDeviceGLCore" if Maya is set to use "OpenGL - Core Profile" (either Compatibility or Strict) for  
                Viewport 2.0, or "VirtualDeviceDx11" if Maya is set to use DirectX for Viewport 2.0.  
                If the renderer for the 3d modeling viewport is not Viewport 2.0, an empty string will be returned.  
                Properties: query
        rendererList (bool?): Query for a list of the internal names for renderers available for use with the  
                3d modeling viewport. The default list contains at least "vp2Renderer", if supported. See  
                rendererName for more details on these renderers. Any plug-in viewport renderers will also appear  
                in this list.  
                Properties: query
        rendererListUI (bool?): Query for a list of the UI names for renderers available for use with the  
                3d modeling viewport. The default list consists of the UI name for "vp2Renderer", if it is supported.  
                Any plug-in viewport renderer's UI names will also appear in this list. This list  
                and the list returned from rendererList have a 1. 1 correspondance.  
                Properties: query
        rendererName (Queryable[str]?): Set or get the renderer used for a 3d modeling viewport. The name provided  
                should be an internal name of a renderer. The 'rendererList' flag  
                can be used to query for a list of available names.  
                The default renderer is "vp2Renderer": Viewport 2.0.  
                Properties: query, edit
        rendererOverrideList (bool?): Query for a list of the internal names for renderer overrides for a 3d viewport renderer.  
                Currently only the "Viewport 2" renderer supports renderer overrides.  
                Properties: query
        rendererOverrideListUI (bool?): Query for a list of the UI names for renderer overrides for a 3d viewport renderer.  
                Currently only the "Viewport 2" renderer supports renderer overrides.  
                Properties: query
        rendererOverrideName (Queryable[str]?): Set or get the override used for a 3d viewport renderer. The name provided  
                should be the internal name for an override.  The 'rendererOverrideList' flag  
                can be used to query for a list of available names.  
                Currently only the "Viewport 2" renderer  supports renderer overrides.  
                Setting an empty string will unset any currently active override.  
                Properties: query, edit
        resetCustomCamera (bool?): When specified will reset the camera transform for the active custom camera  
                used for a scene render filter. It is only enabled when a valid scene render filter is specified.  
                Properties: edit
        sceneRenderFilter (Queryable[str]?): Specifies the name of a scene render filter  
                Properties: query, edit
        selectionConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will synchronize with its own selection list. As the user  
                selects things in this editor, they will be selected in the  
                selectionConnection object. If the object undergoes changes, the  
                editor updates to show the changes.  
                Properties: create, query, edit
        selectionHiliteDisplay (bool?): Sets whether the model panel will draw any selection hiliting  
                on the objects in this window.  
                Properties: query, edit
        setSelected (bool?): This flag causes the currently active objects to be the  
                only objects visible in the view (if viewSelected is true).  
                Properties: edit
        shadingModel (Queryable[int]?): Shading model to use  
                Properties: create, query, edit
        shadows (bool?): Turn on/off the display of hardware shadows in shaded mode.  
                Properties: query, edit
        smallObjectCulling (bool?): Define whether small object culling should be enabled or not  
                Properties: create, query, edit
        smallObjectThreshold (Queryable[float]?): Threshold used for small object culling  
                Properties: create, query, edit
        smoothWireframe (bool?): Turns on or off smoothing of wireframe lines and points  
                Properties: query, edit
        sortTransparent (bool?): This flag turns on/off sorting of transparent objects during  
                shaded mode refresh. Normally, objects are sorted according to their  
                origin in camera space but when this flag is turned off they will be  
                drawn according to their (depth-first traversal) order in the scene  
                graph. This is a global flag that affects all model editors.  
                Properties: query, edit
        stateString (bool?): Query only flag. Returns the MEL command that will create an  
                editor to match the current editor state. The returned command string  
                uses the string variable $editorName in place of a specific name.  
                Properties: query
        stereoDrawMode (bool?): If this flag is used then set stereo draw mode  
                Properties: create, query, edit
        strokes (bool?): Turn on/off the display of Paint Effects strokes for the view  
                Properties: query, edit
        subdivSurfaces (bool?): Turn on/off the display of subdivision surfaces for the view  
                of the model editor.  
                Properties: query, edit
        textureAnisotropic (bool?): Set whether to perform anisotropic texture filtering.  
                Will work only if the anisotropic texture filtering extension  
                is supported in OpenGL on the graphics system.  
                Properties: query, edit
        textureCompression (bool?): Defines whether texture compression should be used or not  
                Properties: create, query, edit
        textureDisplay (Queryable[str]?): Set the type of blending to use for textures.  
                The blend is performed between the destination fragment  
                and the texture fragment. The source is usually the  
                material color. Argument options are:  
                "modulate" : multiply the destination and texture fragment  
                "decal" : overwrite the destination with the texture fragment  
                Properties: query, edit
        textureEnvironmentMap (bool?): If true then use a texture environment map  
                Properties: create, query, edit
        textureHilight (bool?): Set whether to show specular hilighting  
                when the display is in shaded textured mode.  
                Properties: query, edit
        textureMaxSize (Queryable[int]?): Set maximum texture size for hardware texturing.  The integer  
                value must be a power of 2.  Recommended values are 128 or 256.  If  
                the value specified is larger than the OpenGL maximim textures size  
                for the graphics hardware it will be clamped to the OpenGL size.  If  
                many large textures are used in a scene reducing this value improves  
                performance.  On Impact texture memory is pinned in RAM so using  
                large textures can cause reliability and performance problems. Again  
                reducing this value will help. Software rendering does not use this  
                value.  
                This flag is obsolete as of Maya 6.5. The maxTextureResolution/mtr  
                argument on the displayPref command should be used instead.  
                Properties: query, edit
        textureMemoryUsed (bool?): Returns the total number of bytes used by all texture maps.  This  
                is typicly width*height*channels for all texture objects in the scene  
                If the texture is mip mapped all mip map levels are included in the  
                total though not never more than two level will be in use at one time  
                Properties: query
        textureSampling (Queryable[int]?): Set the type of sampling to be used for texture  
                display. The argument can be either:  
              
                1. means to perform point sample  
                2. means to perform bilinear interpolation (default)  
                Properties: query, edit
        textures (bool?): Turn on/off the display of texture objects for the view  
                Properties: query, edit
        toggleExposure (bool?): Toggles between the current and the default exposure value of the editor.  
                Properties: edit
        toggleGamma (bool?): Toggles between the current and the default gamma value of the editor.  
                Properties: edit
        transpInShadows (bool?): Set whether to enable display of transparency in shadows when  
                using the hardware renderer. The default value is false.  
                Properties: query, edit
        transparencyAlgorithm (Queryable[str]?): Set the transparency algorithm.  
                The options are:  
              
                1) "frontAndBackCull" : Two pass front and back culling technique.  
                2) "perPolygonSort" : Draw transparent polygons in back-to-front order technique.  
              
                transparency pptions 1) and 2) are supported by the hardware renderer. Options 1) is  
                supported by the interactive modeling viewports.  
                The default value is "frontAndBackCull".  
                Properties: query, edit
        twoSidedLighting (bool?): Turns on or off two sided lighting.  This may be used with  
                the -default flag.  
                Properties: query, edit
        unParent (bool?): Specifies that the editor should be removed from its layout.  
                This cannot be used in query mode.  
                Properties: create, edit
        unlockMainConnection (bool?): Unlocks the mainConnection, effectively restoring the original  
                mainConnection (if it is still available), and dynamic updates.  
                Properties: create, edit
        updateColorMode (bool?): Using this flag tells the model panel to check which color  
                mode it should be in, and to switch accordingly.  This flag may  
                be used to update a model panel after a camera image plane has  
                been added or removed.  
                Properties: edit
        updateMainConnection (bool?): Causes a locked mainConnection to be updated from the orginal  
                mainConnection, but preserves the lock state.  
                Properties: create, edit
        useBaseRenderer (bool?): Set whether to use the "base" renderer when using  
                the hardware renderer and in "interactive display mode" (-useInteractiveMode)  
                The default value is false.  
                Properties: query, edit
        useColorIndex (bool?): Sets whether the model panel will attempt to use color index  
                mode when possible.  Color index mode can provide a performance  
                increase for point, bounding box, and wireframe display modes.  
                This may be used with the -default flag.  
                Properties: query, edit
        useDefaultMaterial (bool?): Sets whether the model panel will draw all the shaded surfaces  
                using the default material as opposed to using the material(s) currently  
                assigned to the surfaces.  
                Properties: query, edit
        useInteractiveMode (bool?): Turns on or off the use of the special interaction settings  
                during playback.  This flag may be used with the -default flag.  
                Properties: query, edit
        useRGBImagePlane (bool?): Sets whether the model panel will be forced into RGB mode  
                when there is an image plane attached to the panel's camera.  
                Properties: query, edit
        useReducedRenderer (bool?): Set true if using the reduced renderer  
                Properties: create, query, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        userNode (Queryable[str]?): Allows the user to associate a node name with the modelEditor.  
                The value is automatically updated in the event the node is deleted  
                or renamed.  
                Properties: query, edit
        viewObjects (bool?): Returns the name (if any) of the objectSet which contains the  
                list of objects visible in the view if viewSelected is true and the  
                list of objects being displayed does not come from the  
                active list.  
                Properties: query
        viewSelected (bool?): This flag turns on/off viewing of selected objects. When the  
                flag is set to true, the currently active objects are captured and  
                used as the list of objects to view.  
                Properties: query, edit
        viewTransformName (Queryable[str]?): Sets the view pipeline to be applied if color management is enabled in the  
                current editor.  
                Properties: query, edit
        viewType (bool?): Returns a string indicating the type of the model editor. For the  
                default model editor, returns the empty string. For custom model  
                editor types created via the API, returns the same string as is  
                returned via the method MPx3dModelView::viewType().  
                Properties: query
        width (bool?): Return the width of the associated viewport in pixels.  
                Properties: query
        wireframeBackingStore (bool?): Sets whether a backing store is used to optimization the drawing  
                of active objects. This mode can provide a performance increase in  
                wireframe mode for certain scenes.  
                Properties: query, edit
        wireframeOnShaded (bool?): Sets whether the model panel will draw the wireframe on  
                all shaded objects (if true) or only for active objects (if false).  
                Properties: query, edit
        xray (bool?): Turns on or off Xray mode.  This may be used with the -default  
                flag.  
                Properties: query, edit

    Returns:
        str: the name of the editor.

    Example:
    """

