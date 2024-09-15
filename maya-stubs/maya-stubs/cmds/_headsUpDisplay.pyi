from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def headsUpDisplay(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., allDescendants: bool = ..., allowOverlap: bool = ..., attachToRefresh: bool = ..., attributeChange: str = ..., block: Queryable[int] = ..., blockAlignment: Queryable[str] = ..., blockSize: Queryable[str] = ..., command: Queryable[Callable[..., Any]] = ..., conditionChange: str = ..., conditionFalse: str = ..., conditionTrue: str = ..., connectionChange: str = ..., dataAlignment: Queryable[str] = ..., dataFontSize: Queryable[str] = ..., dataWidth: Queryable[int] = ..., decimalPrecision: Queryable[int] = ..., disregardIndex: bool = ..., event: str = ..., exists: bool = ..., getOption: str = ..., gridColor: Queryable[int] = ..., label: Queryable[str] = ..., labelFontSize: Queryable[str] = ..., labelWidth: Queryable[int] = ..., lastOccupiedBlock: int = ..., layoutVisibility: bool = ..., listConditions: bool = ..., listEvents: bool = ..., listHeadsUpDisplays: bool = ..., listNodeChanges: bool = ..., listPresets: bool = ..., name: str = ..., nextFreeBlock: int = ..., nodeChanges: Queryable[Multiuse[str]] = ..., padding: Queryable[int] = ..., preset: Queryable[str] = ..., refresh: bool = ..., remove: bool = ..., removeID: int = ..., removePosition: Tuple[int, int] = ..., resetNodeChanges: Multiuse[str] = ..., scriptResult: bool = ..., section: Queryable[int] = ..., setOption: Tuple[str, str] = ..., showGrid: bool = ..., visible: bool = ...) -> Union[int, Union[str, int, Tuple[int, int]], bool, str, Callable[..., Any], Multiuse[str]]:
    """This command creates a Heads-up Display (HUD) object which is placed in a 2D
    inactive overlay plane on the 3D viewport. It is to be used to provide hands-on
    information designated by a user script. The text string displayed on the viewport
    is formatted using the various flags of this command.The only mandatory flags, on creation are the section and block flags. Note if the preset
    OR command/trigger flags are not present, only a label will be drawn on the viewport.Upon creation of a HUD object, an ID number will be assigned to it. This can be used to
    remove the HUD object (-rid/removeID [int IDNumber]), if desired. Alternatively, HUD
    objects may be removed via their position (section and block), or their unique name.hud, headsupdisplay
    Args:
        allDescendants (bool?): This flag can only be used in conjunction with the -ac/attributeChange  
                flag. If it is specified, and the HUD is attached to a compound or multi  
                attribute, then the HUD command will run due to changes to the specified  
                attribute as well as changes to its descendants.  
                Properties: create, edit
        allowOverlap (bool?): Sets the Heads-Up Display to be visible regardless of overlapping section  
                widths/limitations (see -s/section flag description for more details).  
                Properties: create, query, edit
        attachToRefresh (bool?): Attaches the command to the refresh process. The script is then run each time  
                an idle refresh is run and updates directly following it.  
                Properties: create, query, edit
        attributeChange (str?): Runs the command when the named attribute changes value. The string must  
                identify both the dependency node and the particular attribute. If the  
                dependency node is deleted, this HUD is removed (even if the deletion is  
                undoable).  
                Properties: create, edit
        block (Queryable[int]?): Denotes the individual block that the HUD will reside in, within a  
                section. Each section is composed of a single column of blocks.  
                The total number of blocks contained within each section is variable.  
              
                The number of blocks that will be visible within each section is  
                dependent on the size of blocks contained in each section and the  
                current size of the window. Blocks begin enumerating from 0 and  
                flexibly increase based on need.  
              
                The resultant output string of each HUD is formatted within each block,  
                using parameters defined by the formatting flags listed below (eg. justify,  
                padding, labelWidth and dataWidth). The layout is shown in the following  
                diagram:  
              
                 __________________________________________  
                |     |     |        |         |     |     |  
                |  P  |  J  |   LW   |   DWX   |  J  |  P  |  
                |_____|_____|________|_________|_____|_____|  
                P = Sub-block of width, padding  
                J = Justification of the entire block  
                LW = Sub-block of width, labelWidth  
                DWX = X number of sub-blocks of width, dataWidth, for X data elements.  
              
              
                Block Layout  
              
                The above diagram shows the layout of each block. The widths: padding,  
                labelWidth and dataWidth are defined by their respective flags. To  
                elaborate on the layout of the blocks, First the padding of the block is  
                calculated. Then the two main sub-blocks (LW and DWX) in the above diagram,  
                are justified and positioned together between the left and right margins  
                of the block. The widths of the main sub-blocks are not variable based on  
                it's contents. The only sub-block in the above diagram which is unique is the  
                DWX sub-block which actually represents X number of sub-blocks, where X  
                is the number of data elements returned by the command.  
              
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
        command (Queryable[Callable[..., Any]]?): Specifies the procedure or script to run, in order to obtain the  
                desired information. This must return a value or an array of values.  
                A warning will be displayed if the command does not return a value.  
                This flag MUST always be accompanied by a trigger flag (eg. a condition flag,  
                an event flag, an attachToRefresh flag, etc.).  
                Properties: create, query, edit
        conditionChange (str?): A trigger which runs the command (to sample the data), when the  
                named condition changes. The named condition must be pre-defined or a  
                user defined boolean. To get a list of what conditions exist, use  
                the -lc/listConditions flag.  
                Properties: create, edit
        conditionFalse (str?): A trigger which runs the command (to sample the data), when the  
                named condition becomes false. The named condition must be pre-defined or  
                a user defined boolean. To get a list of what conditions exist, use  
                the -lc/listConditions flag.  
                Properties: create, edit
        conditionTrue (str?): A trigger which runs the command (to sample the data), when the  
                named condition becomes true. The named condition must be pre-defined or a  
                user defined boolean. To get a list of what conditions exist, use  
                the -lc/listConditions flag.  
                Properties: create, edit
        connectionChange (str?): Runs the command when the named attribute changes its connectivity. The  
                string must identify both the dependency node and the particular attribute.  
                If the dependency node is deleted, this HUD is removed (even if the deletion  
                is undoable).  
                Properties: create, edit
        dataAlignment (Queryable[str]?): Specifies the alignment of the data blocks and the data text, within a HUD block.  
                Available alignments are: "left" and "right". The default alignment is "left".  
                Properties: create, query, edit
        dataFontSize (Queryable[str]?): Sets the font size of the returned data. Available sizes are: small and large.  
                Properties: create, query, edit
        dataWidth (Queryable[int]?): Specifies the pixel width of the virtual "textbox" which will hold a data value.  
                For commands which return more than one value (ie. arrays), one of these "textboxes"  
                will be created for each data element, each with this specified width. If the width  
                of the data value exceeds the width of the "textbox", the data value will be  
                truncated to fit within the dimensions of the "textbox." (To see a layout of a  
                block, see the description of the -block flag.)  
                Properties: create, query, edit
        decimalPrecision (Queryable[int]?): Sets the decimal precision of any floating point value returned by the command. The valid  
                range of precision values are 1 to 8.  
                Properties: create, query, edit
        disregardIndex (bool?): This flag can only be used in conjunction with the -ac/attributeChange  
                flag. If it is specified, and the HUD is attached to a multi (indexed)  
                attribute, then the HUD command will run no matter which attribute in  
                the multi changes.  
                Properties: create, edit
        event (str?): Runs the command when the named event occurs. The named event, must be a  
                pre-defined Maya event. To get a list of what events exist, use the  
                -le/listEvents flag.  
                Properties: create, edit
        exists (bool?): This flag returns whether the given object exists in the Heads-Up Display layout.  
                An object name must be supplied with this command. This flag cannot be combined  
                with any other flag.  
                Properties: create, query
        getOption (str?): This flag will return the value of the option specified by the string.  
                See setOption for a list of options  
                			In query mode, this flag needs a value.  
                Properties: query
        gridColor (Queryable[int]?): This flag specifies a color for the grid lines using the inactive color palette. Specifying  
                an index number between 1 to 23 will select the corresponding color in the palette.  
                Properties: create, query, edit
        label (Queryable[str]?): Text string that appears to the left of the desired information.  
                Properties: create, query, edit
        labelFontSize (Queryable[str]?): Sets the font size of the label. Available sizes are: small and large.  
                Properties: create, query, edit
        labelWidth (Queryable[int]?): Specifies the pixel width of the virtual "textbox" which will hold the label. The  
                contents of this "textbox" will be left justified. If the width of the actual label  
                exceeds the width of the "textbox," the label will be truncated to fit within the  
                dimensions of the "textbox." (To see a layout of a block, see the description  
                of the -block flag.)  
                Properties: create, query, edit
        lastOccupiedBlock (int?): Returns the block number of the last occupied block in a given section.  
                Properties: create
        layoutVisibility (bool?): Sets the visibility of Heads-Up Display layout on and off. This does not  
                modify individual visibilities of heads-up displays, but turns off the layout  
                so that no heads-up displays will draw to screen. Personalized settings for  
                the visibilities of HUDs are kept safe. This flag can only be used by itself,  
                excepting edit and query.  
                Properties: create, query, edit
        listConditions (bool?): This flag will return a string array containing all names of the available  
                conditions.  
                Properties: create, query
        listEvents (bool?): This flag will return a string array containing all names of the available  
                events.  
                Properties: create, query
        listHeadsUpDisplays (bool?): This flag will return a string array containing all names of existing HUDs.  
                Properties: create, query
        listNodeChanges (bool?): This flag will return a string array containing all names of the available  
                node changes.  
                Properties: create, query
        listPresets (bool?): This flag will return a string array containing all names of the available  
                preset HUDs.  
                Properties: create, query
        name (str?): This flag only permits the EDITING of the name of the Heads-Up Display.  
                Properties: edit
        nextFreeBlock (int?): Returns the block number of the next free block in a given section.  
                Properties: create
        nodeChanges (Queryable[Multiuse[str]]?): Works only with selection based triggers (ie. "SelectionChanged" or "SomethingSelected"),  
                otherwise this flag is ignored. This flag attaches the HUD script to execute on specific  
                node changes of any selected node. This flag is used to set a nodeChange. In order to  
                reset a nodeChange, use the -rnc/resetNodeChanges flag. To view a list of all available  
                node changes, use the -lnc/listNodeChanges flag. The following is a list of available node  
                changes and their function:  
              
                attributeChange:  The script will be sensitive to any attribute changes in the currently  
                                  selected nodes.  
              
                connectionChange: The script will be sensitive to any connection changes in the currently  
                                  selected nodes.  
              
                instanceChange:   The script will be sensitive to any changes to an instance in the  
                                  currently selected nodes.  
              
              
                On query mode, this flag will return the values of all nodeChanges in pairs of values  
                (the name of the nodeChange followed by its value).  
              
                WARNING: (Performance Warning)  
                         Attaching a nodeChange trigger to a selection based trigger can cause a large  
                         performance drop, if the node change that is being watched is caused by the  
                         HUD script itself.  
              
                         With this said, an attempt should be made to keep the HUD command/script  
                                 simple and limited to retrieving data. Changing an attribute, creating or  
                                 modifying a connection or instance will all result in a performance drop.  
                Properties: create, query, edit, multiuse
        padding (Queryable[int]?): Specifies the width of both the left and right margins of a block. Default  
                value is 15 pixels.  
                Properties: create, query, edit
        preset (Queryable[str]?): This setting is used to select certain pre-defined HUDs, some of which retrieve  
                specific data, that is unobtainable through normal MEL commands or scripts. This flag  
                is mutually exclusive from the command and trigger flag combination. However, presets  
                can work with all other headsUpDisplay attribute flags (ie. block alignment, label,  
                dataFontSize, etc.), unless otherwise specified below. To obtain a list  
                of available presets, use the -lp/listPresets flag on this command.  
              
                The following is a list of available presets and a description of each:  
              
                cameraNames  
                This will return the camera name that the view is looking through, in  
                the data block, for each view that the HUD is drawing to.  
                polyVerts  
                This will return three values in the data block, regarding the number of  
                vertices that are visible by the camera.  
              
                1st Value: Represents the number of camera visible vertices, both  
                active and inactive.  
                2nd Value: Represents the number of camera visible vertices, on  
                active objects only.  
                3rd Value: Represents the number of camera visible vertices, that  
                are active.  
              
                polyEdges  
                This will return three values in the data block, regarding the number of  
                edges that are visible by the camera. The order of these three values are  
                similar to the polyVerts preset.  
                polyFaces  
                This will return three values in the data block, regarding the number of  
                faces that are visible by the camera. The order of these three values are  
                similar to the polyVerts preset.  
                polyUVs  
                This will return three values in the data block, regarding the number of  
                UVs that are visible by the camera. The order of these three values are  
                similar to the polyVerts preset.  
                polyTriangles  
                This will return three values in the data block, regarding the number of  
                triangles that are visible by the camera. The order of these three values are  
                similar to the polyVerts preset.  
                materialLoadingCount  
                This will return the material loading count.  
                It updates on each refresh.  
                textureLoadingCount  
                This will return the texture loading count.  
                It updates on each refresh.  
                frameRate  
                This will return a single string carrying both the frame rate and the "fps"  
                string in the data block. It updates on each refresh.  
                viewAxis  
                This will draw the orientation of the grid axes within the HUD. It updates  
                on each refresh. While this preset can take in all attribute flags, the  
                only one which will have an effect are block attribute related flags  
                (ie. block alignment and block size). The block dimensions of this preset  
                are: blockSize - "large" and blockWidth - "50", which results in a 50x50  
                pixel region.  
                distanceFromCamera  
                This will return in the data block the distance from the view's camera  
                to the centre of the bounding box containing the selected objects in the view.  
                Properties: create, query, edit
        refresh (bool?): This flag forces the given Heads-Up Display element to refresh, updating  
                the value displayed.  This flag cannot be combined with any other flag.  
                Properties: create
        remove (bool?): This command will remove a given HUD object, given a specified HUD name. This flag will  
                override all other flags and is mutually exclusive from the other remove flags.  
                Properties: create, edit
        removeID (int?): This command will remove a given HUD object, given a specified HUD ID number assigned  
                to it at creation time. This flag will override all other flags and is mutually exclusive  
                from the other remove flags.  
                Properties: create, edit
        removePosition (Tuple[int, int]?): This command will remove the contents of a specific block location in the HUD layout.  
                This flag will override all other flags and is mutually exclusive from the other remove  
                flags. Syntax for this flag is: -removePosition/rp [section] [block].  
                Properties: create, edit
        resetNodeChanges (Multiuse[str]?): This flag will reset a specificied nodeChange back to false. This flag only operates under  
                the edit flag. See the description for the -nc/nodeChanges flag for further details.  
                Properties: edit, multiuse
        scriptResult (bool?): This flag is only used in conjunction with the query flag. Calling a query on this flag  
                returns the most recent result of the HUD.  
                Properties: query
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
        setOption (Tuple[str, str]?): This flag will edit the option specified by the first string. Current options are:  
                smpPolyCount - "cage" or "smp" - in smooth mesh preview, determines the poly count display  
                Properties: edit
        showGrid (bool?): This flag will toggle the display of the grid lines of the HUD layout.  
                Properties: create, query, edit
        visible (bool?): Sets the visibility of the Heads-Up Display on and off.  
                Properties: create, query, edit

    Returns:
        int: ID number of the Heads-Up Display (HUD), for regular command execution.
        Union[str, int, Tuple[int, int]]: HUD name, HUD ID or Section and block value, for respective remove commands.

    Example:
    """

