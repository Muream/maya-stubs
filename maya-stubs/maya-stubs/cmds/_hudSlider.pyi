from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def hudSlider(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., allowOverlap: bool = ..., block: Queryable[int] = ..., blockAlignment: Queryable[str] = ..., blockSize: Queryable[str] = ..., decimalPrecision: Queryable[int] = ..., dragCommand: Queryable[Callable[..., Any]] = ..., internalPadding: Queryable[int] = ..., label: Queryable[str] = ..., labelFontSize: Queryable[str] = ..., labelWidth: Queryable[int] = ..., maxValue: Queryable[float] = ..., minValue: Queryable[float] = ..., padding: Queryable[int] = ..., pressCommand: Queryable[Callable[..., Any]] = ..., releaseCommand: Queryable[Callable[..., Any]] = ..., section: Queryable[int] = ..., sliderIncrement: Queryable[float] = ..., sliderLength: Queryable[int] = ..., type: Queryable[str] = ..., value: Queryable[float] = ..., valueAlignment: Queryable[str] = ..., valueFontSize: Queryable[str] = ..., valueWidth: Queryable[int] = ..., visible: bool = ...) -> Union[int, Union[str, int, Tuple[int, int]], bool, str, Callable[..., Any], float]:
    """This command creates a Heads-up Display (HUD) slider control which is placed in a 2D
    inactive overlay plane on the 3D viewport. It is to be used to provide hands-on
    interaction designated by a user script. The HUD slider is derived from
    a generic HUD object and thus inherits a similar workflow.Although this command provides much of the same functionality as the headsUpDisplay
    command, it does not provide headsUpDisplay layout controls such as layoutVisibility,
    nextFreeBlock, lastOccupiedBlock, exists, remove, etc. To access that functionality,
    please use the headsUpDisplay command. This command is focused solely around the creation
    and management of HUD sliders. Similarly, all operations performed by this command
    are limited to HUDs that are sliders.The only mandatory flags, on creation are the section and block flags.Like the headsUpDisplay command, upon creation of a HUD slider, an ID number will be
    assigned to it. This can be used to remove the HUD slider via the headsUpDisplay
    command (-rid/removeID [int IDNumber]), if desired. Alternatively, the headsUpDisplay
    command can remove HUD objects via their position (section and block),
    or their unique name.hud, headsupdisplay, slider, hudslider
    Args:
        allowOverlap (bool?): Sets the Heads-Up Display to be visible regardless of overlapping section  
                widths/limitations (see -s/section flag description for more details).  
                Properties: create, query, edit
        block (Queryable[int]?): Denotes the individual block that the HUD will reside in, within a  
                section. Each section is composed of a single column of blocks.  
                The total number of blocks contained within each section is variable.  
              
                The number of blocks that will be visible within each section is  
                dependent on the size of blocks contained in each section and the  
                current size of the window. Blocks begin enumerating from 0 and  
                flexibly increase based on need.  
              
                For HUD sliders, the format differs from that of the standard HUD.  
                The layout using parameters defined by the formatting flags listed  
                below (eg. justify, padding, labelWidth, valueWidth) is shown below:  
              
                 __________________________________________________________________  
                |     |     |        |            |      |             |     |     |  
                |  P  |  J  |   LW   |   Slider   |  IP  | SliderValue |  J  |  P  |  
                |_____|_____|________|____________|______|_____________|_____|_____|  
                P = Sub-block of width, padding  
                J = Justification of the entire block  
                LW = Sub-block of width, labelWidth  
                Slider = Length of the slider  
                SliderValue = Sub-block of width, valueWidth  
                IP = Internal padding  
              
              
                Block Positioning  
              
                Blocks on the top section begin from the top edge of the main  
                viewport, while the bottom section begins from the bottom edge.  
                Blocks are dynamically removed from visibility from the midpoint  
                of the viewport. So, a relatively large block number will not  
                draw to the viewport.  
              
                Lastly, there can be at most one HUD occupying a block at any time.  
                Trying to position a HUD in an occupied block will result in an error.  
                Keep this in mind when positioning the HUD.  
                Properties: create, query, edit
        blockAlignment (Queryable[str]?): Specifies the alignment of the block within its respective column. Available  
                alignments are: "center", "left" and "right". The default alignment is "left".  
                Properties: create, query, edit
        blockSize (Queryable[str]?): Sets the height of each block. Available heights are: small, medium and large.  
                In pixel measurements, each corresponds to a 20, 35 or 50 pixel height, respectively.  
                Properties: create, query, edit
        decimalPrecision (Queryable[int]?): Sets the decimal precision of any floating point value returned by the command. The valid  
                range of precision values are 1 to 8.  
                Properties: create, query, edit
        dragCommand (Queryable[Callable[..., Any]]?): Specifies the procedure or script to run during a mouse drag event.  
                Properties: create, query, edit
        internalPadding (Queryable[int]?): Specifies the amount of padding between the internal elements of the HUD. For the  
                hudSlider, this represents the padding between the slider bar and the slider  
                value. The default padding is 10.  
                Properties: create, query, edit
        label (Queryable[str]?): Text label of the HUD.  
                Properties: create, query, edit
        labelFontSize (Queryable[str]?): Sets the font size of the label. Available sizes are: small and large.  
                Properties: create, query, edit
        labelWidth (Queryable[int]?): Specifies the pixel width of the virtual "textbox" which will hold the label. The  
                contents of this "textbox" will be left justified. If the width of the actual label  
                exceeds the width of the "textbox," the label will be truncated to fit within the  
                dimensions of the "textbox." (To see a layout of a block, see the description  
                of the -block flag.)  
                Properties: create, query, edit
        maxValue (Queryable[float]?): Specify the maximum value of the slider.  
                Note: Although this flag takes in a FLOAT as an argument, if the  
                HUD type is "int", the value will be automatically converted  
                internally to an integer.  
                Properties: create, query, edit
        minValue (Queryable[float]?): Specify the minimum value of the slider.  
                Note: Although this flag takes in a FLOAT as an argument, if the  
                HUD type is "int", the value will be automatically converted  
                internally to an integer.  
                Properties: create, query, edit
        padding (Queryable[int]?): Specifies the width of both the left and right margins of a block. Default  
                value is 15 pixels.  
                Properties: create, query, edit
        pressCommand (Queryable[Callable[..., Any]]?): Specifies the procedure or script to run during a mouse click event.  
                Properties: create, query, edit
        releaseCommand (Queryable[Callable[..., Any]]?): Specifies the procedure or script to run during a mouse release event.  
                Properties: create, query, edit
        section (Queryable[int]?): Defines the section the HUD will appear in. There are 10 sections  
                divided across the screen. Five columns and two rows make up the  
                ten element matrix which divide the main viewport. Here is a visual  
                layout of the sections.  
              
                 ________________________  
                |    |    |    |    |    |  
                |    |    |    |    |    |  
                | 0  | 1  | 2  | 3  | 4  |  
                |    |    |    |    |    |  
                |____|____|____|____|____|  
                |    |    |    |    |    |  
                |    |    |    |    |    |  
                | 5  | 6  | 7  | 8  | 9  |  
                |    |    |    |    |    |  
                |____|____|____|____|____|  
                Each section is denoted by a number from 0 to 9 as illustrated above.  
                For example, if the second column of the top row was desired, the  
                section would be defined as: -sec 1  
              
                To prevent HUD objects from displaying over each other and causing a  
                clutter of letters, each row has a defined visibility precedence,  
                where each section would have a visibility priority level. Depending  
                on each priority level, when the screen space begins to shrink to  
                a point where the section widths of a given row begin to collide, the  
                HUD automatically compensates for this by removing the sections of  
                least priority. These sections are made invisible and a warning is  
                issued to inform the user of the removal. This continues until only  
                the section of highest priority remains.  
              
                For each row, the priorities are defined as follows. Using the top  
                row as an example: Section 0, has the highest priority, followed  
                by Section 4, making the outermost sections of highest priority.  
                Next in the list is Section 2, and lastly Sections 1 and 3 are of  
                the equal and least priority. This priority structure can be applied  
                to the bottom row as well. The two outermost sections have the highest  
                priority, followed by the middle section, and finally the remaining  
                two sections are of lowest priority.  
              
                This means that as the viewport gradually decreases in width  
                to the point where sections in the top row begin to overlap, sections  
                1 and 3 will be removed from view first, followed by section 2, and  
                finally section 4. A similar note is provided below for the block layout.  
                Properties: create, query, edit
        sliderIncrement (Queryable[float]?): Specify the number of increments along the slider. If not specified or set to 0 or less,  
                the slider will be linearly even and continuous from minValue to maxValue.  
                Note: Although this flag takes in a FLOAT as an argument, if the  
                HUD type is "int", the value will be automatically converted  
                internally to an integer.  
                Properties: create, query, edit
        sliderLength (Queryable[int]?): Specifies the length of the slider in pixels.  
                Properties: create, query, edit
        type (Queryable[str]?): Specify the numeric type of the HUD. Available types are:  
                "float" and "int".  
                Properties: create, query, edit
        value (Queryable[float]?): Set/Return the slider value if the HUD is a valid HUD slider.  
                Note: Although this flag takes in a FLOAT as an argument, if the  
                HUD type is "int", the value will be automatically converted  
                internally to an integer.  
                Properties: create, query, edit
        valueAlignment (Queryable[str]?): Specifies the alignment of the data blocks and the data text, within a HUD block.  
                Available alignments are: "left" and "right". The default alignment is "left".  
                Properties: create, query, edit
        valueFontSize (Queryable[str]?): Sets the font size of the slider value. Available sizes are: small and large.  
                Properties: create, query, edit
        valueWidth (Queryable[int]?): Specifies the pixel width of the virtual "textbox" which will hold the slider value.  
                (To see a layout of a block, see the description of the -block flag.)  
                Properties: create, query, edit
        visible (bool?): Sets the visibility of the Heads-Up Display on and off.  
                Properties: create, query, edit

    Returns:
        int: ID number of the Heads-Up Display (HUD).
        Union[str, int, Tuple[int, int]]: HUD name, HUD ID or Section and block value, for respective remove commands.

    Example:
    """

