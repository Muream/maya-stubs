from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def artFluidAttrCtx(*args: Any, edit: bool = ..., query: bool = ..., accopacity: bool = ..., activeListChangedProc: Queryable[str] = ..., afterStrokeCmd: Queryable[str] = ..., alphaclamp: Queryable[str] = ..., alphaclamplower: Queryable[float] = ..., alphaclampupper: Queryable[float] = ..., attrSelected: Queryable[str] = ..., autoSave: Queryable[str] = ..., beforeStrokeCmd: Queryable[str] = ..., brushalignment: bool = ..., brushfeedback: bool = ..., clamp: Queryable[str] = ..., clamplower: Queryable[float] = ..., clampupper: Queryable[float] = ..., clear: bool = ..., colorAlphaValue: Queryable[float] = ..., colorRGBAValue: Queryable[Tuple[float, float, float, float]] = ..., colorRGBValue: Queryable[Tuple[float, float, float]] = ..., colorRamp: Queryable[str] = ..., colorfeedback: bool = ..., colorfeedbackOverride: bool = ..., colorrangelower: Queryable[float] = ..., colorrangeupper: Queryable[float] = ..., currentPaintableFluid: Queryable[str] = ..., dataTypeIndex: Queryable[int] = ..., delaySelectionChanged: bool = ..., disablelighting: bool = ..., displayAsRender: bool = ..., displayVelocity: bool = ..., doAutoSave: bool = ..., dragSlider: str = ..., duringStrokeCmd: Queryable[str] = ..., dynclonemode: bool = ..., exists: bool = ..., expandfilename: bool = ..., exportaspectratio: Queryable[float] = ..., exportfilemode: Queryable[str] = ..., exportfilesave: str = ..., exportfilesizex: Queryable[int] = ..., exportfilesizey: Queryable[int] = ..., exportfiletype: Queryable[str] = ..., filterNodes: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., importfileload: str = ..., importfilemode: Queryable[str] = ..., importreassign: bool = ..., interactiveUpdate: bool = ..., lastRecorderCmd: Queryable[str] = ..., lastStampName: Queryable[str] = ..., lowerradius: Queryable[float] = ..., makeStroke: Queryable[Multiuse[int]] = ..., mappressure: Queryable[str] = ..., maxvalue: Queryable[float] = ..., minvalue: Queryable[float] = ..., name: str = ..., numericColorRamp: Queryable[str] = ..., numericDisplayColor: Queryable[Tuple[float, float, float]] = ..., numericDisplayPrecision: Queryable[int] = ..., numericMaxColor: Queryable[Tuple[float, float, float]] = ..., numericMinColor: Queryable[Tuple[float, float, float]] = ..., objattrArray: Queryable[str] = ..., objattrArrayNoMenu: Queryable[str] = ..., opacity: Queryable[float] = ..., outline: bool = ..., outwhilepaint: bool = ..., paintNodeArray: Queryable[str] = ..., paintattrselected: str = ..., paintmode: Queryable[str] = ..., paintoperationtype: Queryable[str] = ..., pickColor: bool = ..., pickValue: bool = ..., playbackCursor: Queryable[Multiuse[Tuple[float, float]]] = ..., playbackPressure: Queryable[Multiuse[float]] = ..., preserveclonesource: bool = ..., profileShapeFile: Queryable[str] = ..., projective: bool = ..., property: Queryable[str] = ..., radius: Queryable[float] = ..., rampMaxColor: Queryable[Tuple[float, float, float]] = ..., rampMinColor: Queryable[Tuple[float, float, float]] = ..., record: bool = ..., reflection: bool = ..., reflectionaboutorigin: bool = ..., reflectionaxis: Queryable[str] = ..., rgbValue: Queryable[Tuple[float, float, float]] = ..., screenRadius: Queryable[float] = ..., selectclonesource: bool = ..., selectedattroper: Queryable[str] = ..., showactive: bool = ..., stampDepth: Queryable[float] = ..., stampProfile: Queryable[str] = ..., stampSpacing: Queryable[float] = ..., strokesmooth: Queryable[str] = ..., surfaceConformedBrushVertices: bool = ..., tablet: bool = ..., tangentOutline: bool = ..., toolOffProc: Queryable[str] = ..., toolOnProc: Queryable[str] = ..., useColorRamp: bool = ..., useMaxMinColor: bool = ..., useNumericColorRamp: bool = ..., useNumericDisplay: bool = ..., useStrokeDirection: bool = ..., usepressure: bool = ..., value: Queryable[float] = ..., velocity: Queryable[Tuple[float, float, float]] = ..., whichTool: Queryable[str] = ..., worldRadius: Queryable[float] = ...) -> Union[bool, str, float, Tuple[float, float, float, float], Tuple[float, float, float], int, Multiuse[int], Multiuse[Tuple[float, float]], Multiuse[float]]:
    """This is a context command to set the flags on the artAttrContext,
    which is the base context for attribute painting operations. All
    commands require the name of the context as the last argument as
    this provides the name of the context to create, edit or query.This command is used to paint properties
    (such as density) of selected fluid volumes.
    Args:
        accopacity (bool?): Sets opacity accumulation on/off.  
                C: Default is false (Except for sculpt tool for which it is true by default).  
                Q: When queried, it returns a boolean.  
                Properties: create, query, edit
        activeListChangedProc (Queryable[str]?): Accepts a string that contains a MEL command that is  
                invoked whenever the active list changes. There may be some  
                situations where the UI, for example, needs to be updated,  
                when objects are selected/deselected in the scene. In query  
                mode, the name of the currently registered MEL command is  
                returned and this will be an empty string if none is defined.  
                Properties: create, query, edit
        afterStrokeCmd (Queryable[str]?): The passed string is executed as a MEL command  
                immediately after the end of a stroke.  
                C: Default is no command. Q: When queried, it returns  
                the current command  
                Properties: create, query, edit
        alphaclamp (Queryable[str]?): Specifies if the weight value should be alpha clamped to  
                the lower and upper bounds. There are four options here:  
                "none" - no clamping is performed, "lower" - clamps only to  
                the lower bound, "upper" - clamps only to the upper bounds,  
                "both" - clamps to the lower and upper bounds.  
                C: Default is "none".  Q: When queried, it returns a string.  
                Properties: create, query, edit
        alphaclamplower (Queryable[float]?): Specifies the lower bound for the alpha values.  
                C: Default is 0.0.  Q: When queried, it returns a float.  
                Properties: create, query, edit
        alphaclampupper (Queryable[float]?): Specifies the upper bound for the alpha values.  
                C: Default is 1.0.  Q: When queried, it returns a float.  
                Properties: create, query, edit
        attrSelected (Queryable[str]?): Returns a name of the currently selected attribute.  
                Q: When queried, it returns a string.  
                Properties: query
        autoSave (Queryable[str]?): A MEL command to save the fluid state.  Called  
                before an event which could overwrite unsaved values of  
                painted fluid properties.  Such events include: changing  
                current time, changing the current paintable property, and  
                exiting the paint tool.  (To turn auto-save off, pass in  
                an empty-valued string argument: e.g., "".)  
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
        clamp (Queryable[str]?): Specifies if the weight value should be clamped to  
                the lower and upper bounds. There are four options here:  
                "none" - no clamping is performed, "lower" - clamps only to  
                the lower bound, "upper" - clamps only to the upper bounds,  
                "both" - clamps to the lower and upper bounds.  
                C: Default is "none".  Q: When queried, it returns a string.  
                Properties: create, query, edit
        clamplower (Queryable[float]?): Specifies the lower bound for the values.  
                C: Default is 0.0.  Q: When queried, it returns a float.  
                Properties: create, query, edit
        clampupper (Queryable[float]?): Specifies the upper bound for the values.  
                C: Default is 1.0.  Q: When queried, it returns a float.  
                Properties: create, query, edit
        clear (bool?): Floods all cvs/vertices to the current value.  
                Properties: create, edit
        colorAlphaValue (Queryable[float]?): The Alpha value of the color.  
                Properties: create, query, edit
        colorRGBAValue (Queryable[Tuple[float, float, float, float]]?): The RGBA value of the color.  
                Properties: create, query, edit
        colorRGBValue (Queryable[Tuple[float, float, float]]?): The RGB value of the color.  
                Properties: create, query, edit
        colorRamp (Queryable[str]?): Allows a user defined color ramp to be used to map values to colors.  
                Properties: create, query, edit
        colorfeedback (bool?): Sets on/off the color feedback display.  
                C: Default is FALSE.  Q: When queried, it returns a boolean.  
                Properties: create, query, edit
        colorfeedbackOverride (bool?): Sets on/off the color feedback override.  
                C: Default is FALSE.  Q: When queried, it returns a boolean.  
                Properties: create, query, edit
        colorrangelower (Queryable[float]?): Specifies the value that maps to black when  
                color feedback mode is on.  
                C: Default is 0.0.  Q: When queried, it returns a float.  
                Properties: create, query, edit
        colorrangeupper (Queryable[float]?): Specifies the value that maps to the maximum  
                color when color feedback mode is on.  
                C: Default is 1.0.  Q: When queried, it returns a float.  
                Properties: create, query, edit
        currentPaintableFluid (Queryable[str]?): Query the name of the fluid on which this context is  
                currently painting.  Returns string.  
                Properties: query
        dataTypeIndex (Queryable[int]?): When the selected paintable attribute is a vectorArray,  
                it specifies which field to paint on.  
                Properties: query, edit
        delaySelectionChanged (bool?): Internal use only.  Under normal conditions,  
                the tool responds to changes to the selection list so it  
                can update its list of paintable geometry.  When  
                -dsl true is used, the tool will not update its paintable  
                list until a corresponding -dsl false is called.  
                Properties: create, query, edit
        disablelighting (bool?): If color feedback is on, this flag determines whether  
                lighting is disabled or not for the surfaces that are  
                affected.  
                C: Default is FALSE.  Q: When queried, it returns a boolean.  
                Properties: create, query, edit
        displayAsRender (bool?): When true, sets the "Shaded Display" attribute  
                of the fluid to "AsRender": all fluid properties displayed  
                as hardware rendered.  When false, displays only the  
                currently selected paintable attribute of the fluid.  
                Properties: create, query, edit
        displayVelocity (bool?): Turns on/off velocity display, independently of the  
                above "dar/displayAsRender" setting.  Use this flag  
                to enable velocity display while only displaying density, for  
                example.  
                Properties: create, query, edit
        doAutoSave (bool?): Execute the -autoSave command if there are  
                unsaved painted fluid properties.  
                Properties: edit
        dragSlider (str?): Sets the current brush drag state for resizing or  
                offsetting the brush (like the 'b' and 'm' default hotkeys).  
                The string argument is one of: "radius", "lowradius",  
                "opacity", "value", "depth", "displacement", "uvvector"  
                or "none".  
                C: Default is "none".  
                Properties: create, edit
        duringStrokeCmd (Queryable[str]?): The passed string is executed as a MEL command  
                during the stroke, each time the mouse is dragged.  
                C: Default is no command. Q: When queried, it returns  
                the current command  
                Properties: create, query, edit
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
        filterNodes (bool?): Sets the node filter.  
                Properties: edit
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
        interactiveUpdate (bool?): Specifies how often to transfer the painted values  
                into the attribute.  
                TRUE: transfer them "continuously" (many times per stroke)  
                FALSE: transfer them only at the end of a stroke (on mouse  
                button release).  
                C: Default is TRUE. Q: When queried, it returns a boolean.  
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
        maxvalue (Queryable[float]?): Specifies the maximum value for each attribute.  
                C: Default is 1.0.  Q: When queried, it returns a float.  
                Properties: create, query, edit
        minvalue (Queryable[float]?): Specifies the minimum value for each attribute.  
                C: Default is 0.0.  Q: When queried, it returns a float.  
                Properties: create, query, edit
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        numericColorRamp (Queryable[str]?): Allows a user defined color ramp to be used to map values to colors for the  
                numeric display.  
                Properties: create, query, edit
        numericDisplayColor (Queryable[Tuple[float, float, float]]?): Defines a color to be used when displaying numeric values.  
                Properties: create, query, edit
        numericDisplayPrecision (Queryable[int]?): Specifies how many decimal points of precision should be used for the  
                numeric display.  
                Properties: create, query, edit
        numericMaxColor (Queryable[Tuple[float, float, float]]?): Defines a special color to be used when the value is greater than or equal to  
                the maximum value.  
                Properties: create, query, edit
        numericMinColor (Queryable[Tuple[float, float, float]]?): Defines a special color to be used when the value is less than or equal to the  
                minimum value.  
                Properties: create, query, edit
        objattrArray (Queryable[str]?): An array of all paintable attributes. Each element of  
                the array is a string with the following information:  
                NodeType.NodeName.AttributeName.MenuType  
                *MenuType: type (level) of the item in the Menu (UI).  
                Q: When queried, it returns a string.  
                Properties: query
        objattrArrayNoMenu (Queryable[str]?): Returns an array of all paintable attributes in their original order.  
                Each element of the array is a string with the following information:  
                NodeType.NodeName.AttributeName  
                Properties: query
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
        paintNodeArray (Queryable[str]?): An array of paintable nodes.  
                Q: When queried, it returns a string.  
                Properties: query
        paintattrselected (str?): An array of selected paintable attributes.  
                Each element of the array is a string with the  
                following information:  
                NodeType.NodeName.AttributeName.  
                Properties: edit
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
        property (Queryable[str]?): Specifies a property to paint on the fluid.  
                Valid values are "color", "density", "densityAndColor,"  
                "densityAndFuel," "temperature," "fuel", "velocity".  
                Properties: create, query, edit
        radius (Queryable[float]?): Sets the size of the brush.  
                C: Default is 1.0 cm. Q: When queried, it returns a float.  
                Properties: create, query, edit
        rampMaxColor (Queryable[Tuple[float, float, float]]?): Defines a special color to be used when the value is greater than or equal to  
                the maximum value.  
                Properties: create, query, edit
        rampMinColor (Queryable[Tuple[float, float, float]]?): Defines a special color to be used when the value is less than or equal to the  
                minimum value.  
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
        rgbValue (Queryable[Tuple[float, float, float]]?): Specifies the values of the red, green, and  
                blue components of the color to  
                use when painting the property "color."  
                Properties: create, query, edit
        screenRadius (Queryable[float]?): Brush radius on the screen  
                Properties: create, query, edit
        selectclonesource (bool?): Toggle on to select the clone source  
                Properties: create, query, edit
        selectedattroper (Queryable[str]?): Sets the edit weight operation. Four edit weights  
                operations are provided : "absolute" - the value of the weight  
                is replaced by the current one, "additive" - the value of the  
                weight is added to the current one, "scale" - the value of the  
                weight is multiplied by the current one, "smooth" - the value  
                of the weight is divided by the current one.  
                C: Default is "absolute".  Q: When queried, it returns a string.  
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
        toolOffProc (Queryable[str]?): Accepts a strings describing the name of a MEL  
                procedure that is invoked whenever the tool is turned off.  
                For example, cloth invokes "clothPaintToolOff" when the cloth  
                paint tool is turned on. Define this callback if your tool  
                requires special functionality when your tool is deactivated.  
                It is typical that if you implement a toolOffProc you will  
                want to implement a toolOnProc as well (see the -toolOnProc  
                flag. In query mode, the name of the currently registered MEL  
                command is returned and this will be an empty string if none  
                is defined.  
                Properties: create, query, edit
        toolOnProc (Queryable[str]?): Accepts a strings describing the name of a MEL  
                procedure that is invoked whenever the tool is turned on.  
                For example, cloth invokes "clothPaintToolOn" when the cloth  
                paint tool is turned on. Define this callback if your tool  
                requires special functionality when your tool is activated.  
                It is typical that if you implement a toolOnProc you will  
                want to implement a toolOffProc as well (see the -toolOffProc  
                flag. In query mode, the name of the currently registered MEL  
                command is returned and this will be an empty string if none  
                is defined.  
                Properties: create, query, edit
        useColorRamp (bool?): Specifies whether the user defined color ramp should be used to map values  
                from to colors.  If this is turned off, the default greyscale feedback  
                will be used.  
                Properties: create, query, edit
        useMaxMinColor (bool?): Specifies whether the out of range colors should be used.  See rampMinColor  
                and rampMaxColor flags for further details.  
                Properties: create, query, edit
        useNumericColorRamp (bool?): Specifies whether the user defined color ramp should be used to map values  
                from to colors on the numeric display. If this is turned off, the set single  
                numeric color will be used.  
                Properties: create, query, edit
        useNumericDisplay (bool?): Specifies whether numerical weight values should be displayed next to  
                their associated control points.  
                Properties: create, query, edit
        useStrokeDirection (bool?): Applicable only during "velocity"  
                painting.  Specifies whether the value of the  
                painted velocity should come from the direction  
                of the brush stroke, overriding the value specified  
                by the -v/-velocity flag.  
                Properties: create, query, edit
        usepressure (bool?): Sets the tablet pressure on/off.  
                C: Default is false. Q: When queried, it returns a boolean.  
                Properties: create, query, edit
        value (Queryable[float]?): Specifies the value for each attribute.  
                C: Default is 0.0.  Q: When queried, it returns a float.  
                Properties: create, query, edit
        velocity (Queryable[Tuple[float, float, float]]?): Specifies the values of the x, y, and z  
                components of the velocity to use when painting the property  
                "velocity".  
                Properties: create, query, edit
        whichTool (Queryable[str]?): The string defines the name of the tool to be  
                used for the Artisan context. An example is "artClothPaint".  
                In query mode, the tool name for the given context is returned.  
                Note: due to the way MEL works, always specify the -query flag  
                last when specifying a flag that takes arguments.  
                Properties: create, query, edit
        worldRadius (Queryable[float]?): Radius in worldspace  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

