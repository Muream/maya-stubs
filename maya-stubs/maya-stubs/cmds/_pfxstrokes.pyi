from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def pfxstrokes(*, filename: str = ..., postCallback: bool = ..., selected: bool = ...) -> bool:
    """This command will loop through all the Paint Effects strokes, including pfxHair nodes, and write
    the current state of all the tubes to a file. For normal stroke nodes tubes must be ON in the brush or
    there will be no output. For pfxHair nodes there will always be output, but the format is different than
    for stroke nodes(however one can assign a brush with tubes = ON to a pfxHair node, in which case it
    will output the same format as strokes). The general file format is ASCII, using commas to separate numerical
    values and newlines between blocks of data. The format used for pfxHair nodes presents the hair curves points
    in order from root to tip of the hair. The hairs follow sequentially in the following fashion:
    NumCvs
    pointX,pointY,pointZ, normalX,normalY,normalZ, width, colorR,colorG,colorB, paramU
    pointX,pointY,pointZ, normalX,normalY,normalZ, width, colorR,colorG,colorB, paramU
    etc...
    NumCvs
    pointX,pointY,pointZ, normalX,normalY,normalZ, width, colorR,colorG,colorB, paramU
    etc..
    The format used to output files for brushes with tubes=ON is more complex. The tubes can branch and the order
    the segments are written is the same order they are drawn in. Slowly drawing a tall grass brush in the paint
    effects panel can help to illustrate the order the segments will appear in the file. New tubes can start "growing"
    before others are finished. There is no line for "NumCvs". Instead all data for each segment appears on each line.
    The data on each line is the same as passed into the paint effects runtime function. See the argument list of
    paintRuntimeFunc.mel for the order and a description of these parameters. The parameters match up exactly in
    the order they appear on a line of the output file with the order of arguments to this function. If one wishes to
    parse the output file and connect the segments together into curves the branchId, parentId and siblingCnt
    parameters can help when sorting which segment connects to which line.
    Using the -postCallback option will write out the tubes data after it has been proessed by the runTime callback.paint, effects, strokes, callback
    Args:
        filename (str?): The output file.  
                Properties: create
        postCallback (bool?): Output information to the file after the Runtime Callback MEL function has been invoked. The default  
                is to output the information prior to the callback.  
                Properties: create
        selected (bool?): Only loop through the selected strokes.  
                Properties: create

    Returns:
        bool:

    Example:
    """

