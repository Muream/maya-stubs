from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def artSetPaintCtx(*args: Any, edit: bool = ..., query: bool = ..., accopacity: bool = ..., afterStrokeCmd: Queryable[str] = ..., beforeStrokeCmd: Queryable[str] = ..., brushalignment: bool = ..., brushfeedback: bool = ..., clear: bool = ..., dragSlider: str = ..., dynclonemode: bool = ..., exists: bool = ..., expandfilename: bool = ..., exportaspectratio: Queryable[float] = ..., exportfilemode: Queryable[str] = ..., exportfilesave: str = ..., exportfilesizex: Queryable[int] = ..., exportfilesizey: Queryable[int] = ..., exportfiletype: Queryable[str] = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., importfileload: str = ..., importfilemode: Queryable[str] = ..., importreassign: bool = ..., lastRecorderCmd: Queryable[str] = ..., lastStampName: Queryable[str] = ..., lowerradius: Queryable[float] = ..., makeStroke: Queryable[Multiuse[int]] = ..., mappressure: Queryable[str] = ..., name: str = ..., objectsetnames: Queryable[str] = ..., opacity: Queryable[float] = ..., outline: bool = ..., outwhilepaint: bool = ..., paintmode: Queryable[str] = ..., paintoperationtype: Queryable[str] = ..., pickColor: bool = ..., pickValue: bool = ..., playbackCursor: Queryable[Multiuse[Tuple[float, float]]] = ..., playbackPressure: Queryable[Multiuse[float]] = ..., preserveclonesource: bool = ..., profileShapeFile: Queryable[str] = ..., projective: bool = ..., radius: Queryable[float] = ..., record: bool = ..., reflection: bool = ..., reflectionaboutorigin: bool = ..., reflectionaxis: Queryable[str] = ..., screenRadius: Queryable[float] = ..., selectclonesource: bool = ..., setcolorfeedback: bool = ..., setdisplaycvs: bool = ..., setopertype: Queryable[str] = ..., settomodify: Queryable[str] = ..., showactive: bool = ..., stampDepth: Queryable[float] = ..., stampProfile: Queryable[str] = ..., stampSpacing: Queryable[float] = ..., strokesmooth: Queryable[str] = ..., surfaceConformedBrushVertices: bool = ..., tablet: bool = ..., tangentOutline: bool = ..., usepressure: bool = ..., worldRadius: Queryable[float] = ...) -> Union[bool, str, float, int, Multiuse[int], Multiuse[Tuple[float, float]], Multiuse[float]]:
    """This tool allows the user to modify the set membership
    (add, transfer, remove cvs) on nurbs surfaces using Maya
    Artisan's interface.
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
        brushfeedback (bool?): Specifies if the brush additional feedback should  
                be drawn.  
                C: Default is TRUE. Q: When queried, it returns a boolean.  
                Properties: create, query, edit
        clear (bool?): Floods all cvs/vertices to the current value.  
                Properties: create, edit
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
        exportaspectratio (Queryable[float]?): Value of aspect ratio for export  
                Properties: create, query, edit
        exportfilemode (Queryable[str]?): Specifies the export channel.The valid  
                entries here are: "alpha", "luminance", "rgb", "rgba".  
                C: Default is "luminance/rgb".  
                Q: When queried, it returns a string.  
                Properties: create, query, edit
        exportfilesave (str?): Exports the attribute map and saves to a specified file.  
                Properties: edit
        exportfilesizex (Queryable[int]?): Specifies the width of the attribute map to export.  
                C: Default width is 256. Q: When queried, it returns an integer.  
                Properties: create, query, edit
        exportfilesizey (Queryable[int]?): Specifies the width of the attribute map to export.  
                C: Default width is 256. Q: When queried, it returns an integer.  
                Properties: create, query, edit
        exportfiletype (Queryable[str]?): Specifies the image file format. It can be one of  
                the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit"  
                "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP".  
                C: default is tiff. Q: When queried, it returns a string.  
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
        importfileload (str?): Load the attribute map a specified file.  
                Properties: edit
        importfilemode (Queryable[str]?): Specifies the channel to import. The valid  
                entries here are: "alpha", "luminance", "red", "green",  
                "blue", and "rgb"  
                C: Default is "alpha". Q: When queried, it returns a string.  
                Properties: create, query, edit
        importreassign (bool?): Specifies if the multiply atrribute maps are to be  
                reassigned while importing. Only maps previously exported from  
                within Artisan can be reassigned.  
                C: Default is FALSE. Q: When queried, it returns a  boolean.  
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
        objectsetnames (Queryable[str]?): Default name of object sets  
                Properties: create, query, edit
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
        screenRadius (Queryable[float]?): Brush radius on the screen  
                Properties: create, query, edit
        selectclonesource (bool?): Toggle on to select the clone source  
                Properties: create, query, edit
        setcolorfeedback (bool?): Specifies if the color feedback is on or off.  
                C: Default is ON.  Q: When queried, it returns a boolean.  
                Properties: create, query, edit
        setdisplaycvs (bool?): Specifies if the active cvs are displayed.  
                C: Default is ON. Q: When queried, it returns a boolean.  
                Properties: create, query, edit
        setopertype (Queryable[str]?): Specifies the setEdit operation  
                ("add", "transfer", "remove").  
                C: Default is "add". Q: When queried, it returns a string.  
                Properties: create, query, edit
        settomodify (Queryable[str]?): Specifies the name of the set to modify.  
                Q: When queried, it returns a string.  
                Properties: create, query, edit
        showactive (bool?): Sets on/off the display of the surface isoparms.  
                C: Default is TRUE. Q: When queried, it returns a boolean.  
                Properties: create, query, edit
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
        usepressure (bool?): Sets the tablet pressure on/off.  
                C: Default is false. Q: When queried, it returns a boolean.  
                Properties: create, query, edit
        worldRadius (Queryable[float]?): Radius in worldspace  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

