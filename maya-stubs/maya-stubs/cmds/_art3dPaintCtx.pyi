from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def art3dPaintCtx(*args: Any, edit: bool = ..., query: bool = ..., accopacity: bool = ..., afterStrokeCmd: Queryable[str] = ..., alphablendmode: Queryable[str] = ..., assigntxt: bool = ..., attrnames: Queryable[str] = ..., beforeStrokeCmd: Queryable[str] = ..., brushalignment: bool = ..., brushdepth: Queryable[float] = ..., brushfeedback: bool = ..., brushtype: Queryable[str] = ..., clear: bool = ..., commonattr: Queryable[str] = ..., dragSlider: str = ..., dynclonemode: bool = ..., exists: bool = ..., expandfilename: bool = ..., extendFillColor: bool = ..., fileformat: Queryable[str] = ..., filetxtaspectratio: Queryable[float] = ..., filetxtsizex: Queryable[int] = ..., filetxtsizey: Queryable[int] = ..., floodOpacity: Queryable[float] = ..., floodall: bool = ..., floodselect: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., keepaspectratio: bool = ..., lastRecorderCmd: Queryable[str] = ..., lastStampName: Queryable[str] = ..., lowerradius: Queryable[float] = ..., makeStroke: Queryable[Multiuse[int]] = ..., mappressure: Queryable[str] = ..., name: str = ..., opacity: Queryable[float] = ..., outline: bool = ..., outwhilepaint: bool = ..., paintmode: Queryable[str] = ..., paintoperationtype: Queryable[str] = ..., painttxtattr: Queryable[str] = ..., painttxtattrname: Queryable[str] = ..., pfxScale: Queryable[float] = ..., pfxWidth: Queryable[float] = ..., pickColor: bool = ..., pickValue: bool = ..., playbackCursor: Queryable[Multiuse[Tuple[float, float]]] = ..., playbackPressure: Queryable[Multiuse[float]] = ..., preserveclonesource: bool = ..., pressureMapping1: Queryable[int] = ..., pressureMapping2: Queryable[int] = ..., pressureMapping3: Queryable[int] = ..., pressureMax1: Queryable[float] = ..., pressureMax2: Queryable[float] = ..., pressureMax3: Queryable[float] = ..., pressureMin1: Queryable[float] = ..., pressureMin2: Queryable[float] = ..., pressureMin3: Queryable[float] = ..., profileShapeFile: Queryable[str] = ..., projective: bool = ..., radius: Queryable[float] = ..., record: bool = ..., reflection: bool = ..., reflectionaboutorigin: bool = ..., reflectionaxis: Queryable[str] = ..., reloadtexfile: bool = ..., resizeratio: Queryable[float] = ..., resizetxt: bool = ..., rgbcolor: Queryable[Tuple[float, float, float]] = ..., rgbflood: Queryable[Tuple[float, float, float]] = ..., saveTextureOnStroke: bool = ..., saveonstroke: bool = ..., savetexture: bool = ..., screenRadius: Queryable[float] = ..., selectclonesource: bool = ..., shadernames: Queryable[str] = ..., shapeattr: bool = ..., shapenames: Queryable[str] = ..., showactive: bool = ..., soloAsDiffuse: bool = ..., stampDepth: Queryable[float] = ..., stampProfile: Queryable[str] = ..., stampSpacing: Queryable[float] = ..., strokesmooth: Queryable[str] = ..., surfaceConformedBrushVertices: bool = ..., tablet: bool = ..., tangentOutline: bool = ..., textureFilenames: bool = ..., updateEraseTex: bool = ..., usepressure: bool = ..., worldRadius: Queryable[float] = ...) -> Union[bool, str, float, int, Multiuse[int], Multiuse[Tuple[float, float]], Multiuse[float], Tuple[float, float, float]]:
    """This is a tool context command for 3d Paint tool.
    Args:
        accopacity (bool?): Sets opacity accumulation on/off.  
                C: Default is false (Except for sculpt tool for which it is true by default).  
                Q: When queried, it returns a boolean.  
                Properties: create, query, edit
        afterStrokeCmd (Queryable[str]?): The passed string is executed as a MEL command  
                immediately after the end of a stroke.  
                C: Default is no command. Q: When queried, it returns  
                the current command  
                Properties: create, query, edit
        alphablendmode (Queryable[str]?): Specifies the blend mode used while painting  
                RGB channel. Currently, we support the following blend modes:  
                "Default" "Lighten" "Darken" "Difference" "Exclusion"  
                "Hard Light" "Soft Light" "Multiply" "Screen" "Overlay" "Constant"  
                Default is "Default".  
                Properties: create, query, edit
        assigntxt (bool?): Sends a request to the tool to allocate and assign  
                file textures to the specified attibute on the selected  
                shaders.  
                Properties: edit
        attrnames (Queryable[str]?): Name of attributes  
                Properties: create, query, edit
        beforeStrokeCmd (Queryable[str]?): The passed string is executed as a MEL command  
                immediately before the start of a stroke.  
                C: Default is no command. Q: When queried, it returns the  
                current command  
                Properties: create, query, edit
        brushalignment (bool?): Specifies the path brush alignemnt. If true,  
                the brush will align to stroke path, otherwise it will  
                align to up vector.  
                C: Default is true. Q: When queried, it returns a boolean.  
                Properties: create, query, edit
        brushdepth (Queryable[float]?): Depth of the brush  
                Properties: create, query, edit
        brushfeedback (bool?): Specifies if the brush additional feedback should  
                be drawn.  
                C: Default is TRUE. Q: When queried, it returns a boolean.  
                Properties: create, query, edit
        brushtype (Queryable[str]?): Name of the brush type  
                Properties: create, query, edit
        clear (bool?): Floods all cvs/vertices to the current value.  
                Properties: create, edit
        commonattr (Queryable[str]?): Returns a string with the names of all common to  
                all the shaders paintable attributes and supported by the  
                Paint Texture Tool.  
                Properties: query
        dragSlider (str?): Sets the current brush drag state for resizing or  
                offsetting the brush (like the 'b' and 'm' default hotkeys).  
                The string argument is one of: "radius", "lowradius",  
                "opacity", "value", "depth", "displacement", "uvvector"  
                or "none".  
                C: Default is "none".  
                Properties: create, edit
        dynclonemode (bool?): Enable or disable dynamic clone mode.  
                Properties: create, query, edit
        exists (bool?): Returns true or false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
        expandfilename (bool?): If true, it will expand the name of the export file  
                and concatenate it with the surface name. Otherwise it  
                will take the name as it is.  
                C: Default is true.  
                Properties: create, edit
        extendFillColor (bool?): States if the painted textures will be automatically  
                postprocessed on each stroke to fill in the background color.  
                Default is true.  
                Properties: create, query, edit
        fileformat (Queryable[str]?): Name of the file format  
                Properties: create, query, edit
        filetxtaspectratio (Queryable[float]?): Specifies the aspect ration of the texture  
                width and height.  
                Default is 1.  
                Properties: create, query, edit
        filetxtsizex (Queryable[int]?): Specifies the width of the texture.  
                Default is 256.  
                Properties: create, query, edit
        filetxtsizey (Queryable[int]?): Specifies the height of the texture.  
                Default is 256.  
                Properties: create, query, edit
        floodOpacity (Queryable[float]?): Value of the flood opacity  
                Properties: create, query, edit
        floodall (bool?): Turn on to flood everything  
                Properties: create, query, edit
        floodselect (bool?): Should the selected area be flooded?  
                Properties: create, query, edit
        history (bool?): If this is a tool command, turn the construction history on  
                for the tool in question.  
                Properties: create
        image1 (Queryable[str]?): First of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        image2 (Queryable[str]?): Second of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        image3 (Queryable[str]?): Third of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        keepaspectratio (bool?): States if the aspect ratio of the file texture  
                sizes should remain constant.  
                Default is true.  
                boolean.  
                Properties: create, query, edit
        lastRecorderCmd (Queryable[str]?): Value of last recorded command.  
                Properties: create, query, edit
        lastStampName (Queryable[str]?): Value of the last stamp name.  
                Properties: create, query, edit
        lowerradius (Queryable[float]?): Sets the lower size of the brush (only apply on tablet).  
                Properties: create, query, edit
        makeStroke (Queryable[Multiuse[int]]?): Stroke point values.  
                Properties: create, query, edit, multiuse
        mappressure (Queryable[str]?): Sets the tablet pressure mapping when the table  
                is used. There are three options:  
                "Opacity" - the pressure is mapped to the opacity,  
                "Radius" - the is mapped to modify the radius of the brush,  
                "Both" - the pressure modifies both the opacity and the radius.  
                C: Default is "Opacity". Q: When queried, it returns a string.  
                Properties: create, query, edit
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        opacity (Queryable[float]?): Sets the brush opacity.  
                C: Default is 1.0. Q: When queried, it returns a float.  
                Properties: create, query, edit
        outline (bool?): Specifies if the brush should be drawn.  
                C: Default is TRUE. Q: When queried, it returns a boolean.  
                Properties: create, query, edit
        outwhilepaint (bool?): Specifies if the brush outline should be drawn  
                while painting.  
                C: Default is FALSE. Q: When queried, it returns a boolean.  
                Properties: create, query, edit
        paintmode (Queryable[str]?): Specifies the paint mode. There are two  
                possibilities: "screen" and "tangent".  
                C: Default is "screen". Q: When queried, it returns a string.  
                Properties: create, query, edit
        paintoperationtype (Queryable[str]?): Specifies the operation type used by the  
                Paint Tool.  Currently, we support the following  
                paint modes: "Paint", "Smear", "Blur", "Erase"  
                and "Clone".  
                Default is "Paint".  
                Properties: create, query, edit
        painttxtattr (Queryable[str]?): Specifies the attribute on the shader which  
                the user wants to paint. Currently, we support the following  
                attributes: "Color", "Transparency", "Ambient", "Incandescence",  
                "BumpMap", "Diffuse", "Translucence" "Eccentricity"  
                "SpecularColor", "Reflectivity", "ReflectedColor", and  
                user-defined float, float3, double, and double3 attributes.  
                Default is "Color".  
                Properties: create, query, edit
        painttxtattrname (Queryable[str]?): Returns a string with the names of all paintable  
                attributes supported by the Paint Texture Tool.  
                Properties: query, edit
        pfxScale (Queryable[float]?): Specifies the scale for Paint Effect brushes.  
                Properties: query, edit
        pfxWidth (Queryable[float]?): Specifies the width for Paint Effect brushes.  
                Properties: query, edit
        pickColor (bool?): Set pick color mode on or off  
                Properties: create, query, edit
        pickValue (bool?): Toggle for picking  
                Properties: create, query, edit
        playbackCursor (Queryable[Multiuse[Tuple[float, float]]]?): Values for the playback cursor.  
                Properties: create, query, edit, multiuse
        playbackPressure (Queryable[Multiuse[float]]?): Valus for the playback pressure.  
                Properties: create, query, edit, multiuse
        preserveclonesource (bool?): Whether or not to preserve a clone source.  
                Properties: create, query, edit
        pressureMapping1 (Queryable[int]?): First pressure mapping value  
                Properties: create, query, edit
        pressureMapping2 (Queryable[int]?): Second pressure mapping value  
                Properties: create, query, edit
        pressureMapping3 (Queryable[int]?): Third pressure mapping value  
                Properties: create, query, edit
        pressureMax1 (Queryable[float]?): First pressure maximum value  
                Properties: create, query, edit
        pressureMax2 (Queryable[float]?): Second pressure maximum value  
                Properties: create, query, edit
        pressureMax3 (Queryable[float]?): Third pressure maximum value  
                Properties: create, query, edit
        pressureMin1 (Queryable[float]?): First pressure minimum value  
                Properties: create, query, edit
        pressureMin2 (Queryable[float]?): Second pressure minimum value  
                Properties: create, query, edit
        pressureMin3 (Queryable[float]?): Third pressure minimum value  
                Properties: create, query, edit
        profileShapeFile (Queryable[str]?): Passes a name of the image file for the stamp shape  
                profile.  
                Properties: query, edit
        projective (bool?): Specifies the projective paint mode.  
                C: Default is 'false'. Q: When queried, it returns a boolean.  
                Properties: create, query, edit
        radius (Queryable[float]?): Sets the size of the brush.  
                C: Default is 1.0 cm. Q: When queried, it returns a float.  
                Properties: create, query, edit
        record (bool?): Toggle on for recording.  
                Properties: create, query, edit
        reflection (bool?): Specifies the reflection mode.  
                C: Default is 'false'. Q: When queried, it returns a boolean.  
                Properties: create, query, edit
        reflectionaboutorigin (bool?): Toggle on to reflect about the origin  
                Properties: create, query, edit
        reflectionaxis (Queryable[str]?): Specifies the reflection axis. There are three  
                possibilities: "x", "y" and "z".  
                C: Default is "x". Q: When queried, it returns a string.  
                Properties: create, query, edit
        reloadtexfile (bool?): Sends a request to the tool to reload the texture  
                from the disc.  
                Properties: edit
        resizeratio (Queryable[float]?): Specifies the scale by which to resize the  
                current textures.  
                Properties: query, edit
        resizetxt (bool?): Sends a request to the tool to resize all the  
                currently in use textures.  
                Properties: edit
        rgbcolor (Queryable[Tuple[float, float, float]]?): Colour value  
                Properties: create, query, edit
        rgbflood (Queryable[Tuple[float, float, float]]?): Color of the flood  
                Properties: create, query, edit
        saveTextureOnStroke (bool?): States if the original texture will be automatically saved  
                on each stroke.  
                Default is false.  
                Properties: create, query, edit
        saveonstroke (bool?): States if the temporary texture will be automatically saved  
                on each stroke.  
                Default is false.  
                Properties: create, query, edit
        savetexture (bool?): Sends a request to the tool to save the texture  
                to the disc.  
                Properties: edit
        screenRadius (Queryable[float]?): Brush radius on the screen  
                Properties: create, query, edit
        selectclonesource (bool?): Toggle on to select the clone source  
                Properties: create, query, edit
        shadernames (Queryable[str]?): Returns a string with the names of all shaders assigned  
                to selected surfaces.  
                Properties: query
        shapeattr (bool?): States if the attribute to paint is an attribute of the shape and not the shader.  
                Default is false.  
                Properties: query, edit
        shapenames (Queryable[str]?): Returns a string with the names of all surfaces  
                which are being painted on.  
                Properties: query
        showactive (bool?): Sets on/off the display of the surface isoparms.  
                C: Default is TRUE. Q: When queried, it returns a boolean.  
                Properties: create, query, edit
        soloAsDiffuse (bool?): States if the currently paintable texture will be rendered as  
                as diffuse texture in the viewport.  
                Default is false.  
                Properties: query, edit
        stampDepth (Queryable[float]?): Depth of the stamps  
                Properties: create, query, edit
        stampProfile (Queryable[str]?): Sets the brush profile of the current stamp.  
                Currently, the following profiles are supported:  
                "gaussian", "poly", "solid" and "square".  
                C: Default is gaussian. Q: When queried, it returns a string.  
                Properties: create, query, edit
        stampSpacing (Queryable[float]?): Specifies the stamp spacing. Default is 1.0.  
                Properties: create, query, edit
        strokesmooth (Queryable[str]?): Stroke smoothing type name  
                Properties: create, query, edit
        surfaceConformedBrushVertices (bool?): Enables/disables the the display of the effective brush area  
                as affected vertices.  
                Properties: create, query, edit
        tablet (bool?): Returns true if the tablet device is present, false if it is absent  
                Properties: query
        tangentOutline (bool?): Enables/disables the display of the brush circle tangent to  
                the surface.  
                Properties: create, query, edit
        textureFilenames (bool?): Returns a string array with the names of all the painted  
                file textures.  
                Properties: query
        updateEraseTex (bool?): Should the erase texture update?  
                Properties: create, query, edit
        usepressure (bool?): Sets the tablet pressure on/off.  
                C: Default is false. Q: When queried, it returns a boolean.  
                Properties: create, query, edit
        worldRadius (Queryable[float]?): Radius in worldspace  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

