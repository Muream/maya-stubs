from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def hudButton(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., allowOverlap: bool = ..., block: Queryable[int] = ..., blockAlignment: Queryable[str] = ..., blockSize: Queryable[str] = ..., buttonShape: Queryable[str] = ..., buttonWidth: Queryable[int] = ..., label: Queryable[str] = ..., labelFontSize: Queryable[str] = ..., padding: Queryable[int] = ..., pressCommand: Queryable[Callable[..., Any]] = ..., releaseCommand: Queryable[Callable[..., Any]] = ..., section: Queryable[int] = ..., visible: bool = ...) -> Union[int, Union[str, int, Tuple[int, int]], bool, str, Callable[..., Any]]:
    """This command creates a Heads-up Display (HUD) button control which is placed in
    a 2D inactive overlay plane on the 3D viewport. It is to be used to provide hands-on
    interaction designated by a user script. The HUD button is derived from
    a generic HUD object and thus inherits a similar workflow.Although this command provides much of the same functionality as the headsUpDisplay
    command, it does not provide headsUpDisplay layout controls such as layoutVisibility,
    nextFreeBlock, lastOccupiedBlock, exists, remove, etc. To access that functionality,
    please use the headsUpDisplay command. This command is focused solely around the creation
    and management of HUD button controls. Similarly, all operations performed by
    this command are limited to HUDs that are button controls.The only mandatory flags, on creation are the section and block flags.Like the headsUpDisplay command, upon creation of a HUD button, an ID number
    will be assigned to it. This can be used to remove the HUD via the headsUpDisplay
    command (-rid/removeID [int IDNumber]), if desired. Alternatively, the headsUpDisplay
    command can remove HUD objects via their position (section and block),
    or their unique name.hud, headsupdisplay, button, hudbutton
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
              
                For HUD buttons, the format differs from that of the standard HUD.  
                The layout using parameters defined by the formatting flags listed  
                below (eg. justify, padding, buttonWidth) is shown below:  
              
                 __________________________________  
                |     |     |          |     |     |  
                |  P  |  J  |  Button  |  J  |  P  |  
                |_____|_____|__________|_____|_____|  
                P = Sub-block of width, padding  
                J = Justification of the entire block  
                Button = Sub-block of width, buttonWidth  
              
              
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
        buttonShape (Queryable[str]?): Specifies the shape of the button. Available button shapes are:  
                "rectangle" and "roundRectangle". The first will draw a rectangular  
                button, while the latter is a rectangle with rounded edges.  
                Properties: create, query, edit
        buttonWidth (Queryable[int]?): Specifies the width of the button.  
                Properties: create, query, edit
        label (Queryable[str]?): Text label of the HUD button.  
                Properties: create, query, edit
        labelFontSize (Queryable[str]?): Sets the font size of the label. Available sizes are: small and large.  
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
        visible (bool?): Sets the visibility of the Heads-Up Display on and off.  
                Properties: create, query, edit

    Returns:
        int: ID number of the Heads-Up Display (HUD).
        Union[str, int, Tuple[int, int]]: HUD name, HUD ID or Section and block value, for respective remove commands.

    Example:
    """

