from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def playblast(*, activeEditor: bool = ..., cameraSetup: Multiuse[Tuple[str, str]] = ..., clearCache: bool = ..., codecOptions: bool = ..., combineSound: bool = ..., completeFilename: str = ..., compression: str = ..., editorPanelName: str = ..., endTime: int = ..., filename: str = ..., forceOverwrite: bool = ..., format: str = ..., frame: Multiuse[int] = ..., framePadding: int = ..., height: int = ..., indexFromZero: bool = ..., offScreen: bool = ..., offScreenViewportUpdate: bool = ..., options: bool = ..., percent: int = ..., quality: int = ..., rawFrameNumbers: bool = ..., replaceAudioOnly: bool = ..., replaceEndTime: int = ..., replaceFilename: str = ..., replaceStartTime: int = ..., sequenceTime: bool = ..., showOrnaments: bool = ..., sound: str = ..., startTime: int = ..., throwOnError: bool = ..., useTraxSounds: bool = ..., viewer: bool = ..., width: int = ..., widthHeight: Tuple[int, int] = ...) -> str:
    """This command playblasts the current playback range.
    Sound is optional.Note that the playblast command registers a condition called "playblasting"
    so that users can monitor whether playblasting is occurring. You may monitor the
    condition using the API (MConditionMessage) or a script (scriptJob and condition
    commands).
    Args:
        activeEditor (bool?): This flag will return the current model editor that would be used  
                for playblast. It does not invoke playblast itself.  
                Properties: create
        cameraSetup (Multiuse[Tuple[str, str]]?): Information about camera setup. The first string defines a camera setup MEL procedure.  
                The camera setup procedure will be invoked before executing a playblast.  
                The second string argument which is used as a camera identifier and is  
                appended to the root file name to specify the final output file name(s).  
                The command will fail there is not a pair of strings supplied to the argument.  
                Properties: create, multiuse
        clearCache (bool?): When true, all previous temporary playblast files will be deleted  
                before the new playblast files are created and the remaining temporary  
                playblast files will be deleted when the application quits.  
                Any playblast files that were explicitly given a name by the user will not be deleted.  
                Properties: create
        codecOptions (bool?): Brings up the OS specific dialog for setting playblast codec options, and  
                does not run the playblast.  
                Properties: create
        combineSound (bool?): Combine the trax sounds into a single track. This might force a  
                resampling of the sound if the sound paramters don't match up.  
                Properties: create
        completeFilename (str?): When set, this string specifies the exact name of the output image.  
                In contrast with the -f/filename flag, -cf/completeFilename does not  
                append any frame number or extension string at the end of the filename.  
                Additionally, playblast will not delete the image from disk after it is  
                displayed. This flag should not be used in conjunction with -f/filename.  
                Properties: create
        compression (str?): Specify the compression to use for the movie file.  To determine which settings are available on your system, use the  
                `playblast -options` command. This will display a system-specific dialog with supported compression formats.  
                When the 'format' flag is 'image', this flag is used to pass in the  
                desired image format. If the format is 'image' and the compression flag is ommitted,  
                the output format specified via the Render Globals preference (see -format) will be used.  
                If compression is set to 'none', the iff image format will be used.  
                Properties: create
        editorPanelName (str?): This optional flag specifies the name of the model editor or panel, which is to  
                be used for playblast. The current model editor or panel won't be used for  
                playblast unless its name is specified. Flag usage is specific to invoking  
                playblast.  
                Properties: create
        endTime (int?): Specify the end time of the playblast.  Default  
                is the end time of the playback range displayed in  
                the Time Slider. Overridden by -frame.  
                Properties: create
        filename (str?): The filename to use for the output of this playblast.  
                If the file already exists, a confirmation box will be  
                displayed if playblast is performed interactively.  If  
                playblast is executed from the command line and the file  
                already exists, it will abort.  
                Properties: create
        forceOverwrite (bool?): Overwrite existing playblast files which may have the  
                the same name as the one specified with the "-f" flag  
                Properties: create
        format (str?): The format for the playblast output.  
              
              
              
                ValueDescription  
              
              
                "movie"  
                This option selects a platform-specific default movie format.  
                On Linux and Mac OSX the default movie format is Quicktime.  
                On Windows the default movie format is Audio Video Interleave.  
              
              
              
                "avi"  
                Set the format to Audio Video Interleave (Windows only)  
              
              
                "qt"  
                Set the format to QuickTime (all platforms).  
              
              
                "avfoundation"  
                Write movie by AVFoundation (Mac only).  
              
              
                "image"  
                Outputs a sequence of image files.  
                The image format will be the Output Format specified using Window > RenderEditors > RenderSettings > CommonTab.  
                The resulting files use the value of the "-f" flag as a prefix, with an  
                appended frame number, as in "myFile.0007.iff"  
              
              
                "iff"  
                Same as "image"  
              
              
              
                The default value of the -fmt/format flag is "movie".  
                Depending on the selected format, a platform-specific default application will be used to view results.  
                For image sequences, the default application is "fcheck".  
                For movies, the default application is Windows Media Player (on Windows),  
                Quicktime Player (on Mac OSX), and Lqtplay (on Linux).  
                Users can specify different applications via Maya's application preferences.  
                Properties: create
        frame (Multiuse[int]?): List of frames to blast. One frame specified per flag.  
                The frames can be specified in any order but will be output  
                in an ordered sequence. When specified this flag will override any  
                start/end range  
                Properties: create, multiuse
        framePadding (int?): Number of zeros used to pad file name. Typically set to 4 to support fcheck.  
                Properties: create
        height (int?): Height of the final image. This value will be clamped if larger  
                than the width of the active window.  
                Windows: If not using fcheck, the width and height must each be divisible  
                by 4.  
                Properties: create
        indexFromZero (bool?): Output frames starting with file.0000.ext and incrementing by one. Typically  
                frames use the Maya time as their frame number. This option can only be used  
                for frame based output formats.  
                Properties: create
        offScreen (bool?): When set, this toggle allow playblast to use an offscreen buffer  
                to render the view. This allows playblast to work when the application  
                is iconified, or obscured.  
                Properties: create
        offScreenViewportUpdate (bool?): When set, this toggle allows playblast to update the viewport  
                while rendering with the offscreen buffer.  
                Properties: create
        options (bool?): Brings up a dialog for setting playblast options, and  
                does not run the playblast.  
                Properties: create
        percent (int?): Percentage of current view size  to use during blasting.  
                Accepted values are integers between 10 and 100.  All other  
                values are clamped to be within this range.  A value of 25  
                means 1/4 of the  current view size; a  value of 50  means  
                half the current view size; a value of 100 means full  
                size.  (Default is 50.)  
                Properties: create
        quality (int?): Specify the compression quality factor to use for the movie file.  
                Value should be in the 0. 100 range  
                Properties: create
        rawFrameNumbers (bool?): Playblast typically numbers its frames sequentially, starting at zero.  
                This flag will override the default action and frames will be numbered using the  
                actual frames specified by the -frame or -startFrame/-endFrame flags.  
                Properties: create
        replaceAudioOnly (bool?): When set, this string dictates that only the audio will be replaced when  
                the scene is re-playblasted.  
                Properties: create
        replaceEndTime (int?): Specify the end time of a replayblast of an existing  
                playblast.  Default is the start time of the playback  
                range displayed in the Time Slider. Overridden by -frame.  
                Properties: create
        replaceFilename (str?): When set, this string specifies the name of an input playblast file which  
                will have frames replaced according to the replace start and end times.  
                Properties: create
        replaceStartTime (int?): Specify the start time of a replayblast of an existing  
                playblast.  Default is the start time of the playback  
                range displayed in the Time Slider. Overridden by -frame.  
                Properties: create
        sequenceTime (bool?): Use sequence time  
                Properties: create
        showOrnaments (bool?): Sets whether or not model view ornaments (e.g. the axis icon)  
                should be displayed  
                Properties: create
        sound (str?): Specify the sound node to be used during playblast  
                Properties: create
        startTime (int?): Specify the start time of the playblast.  Default  
                is the start time of the playback range displayed in  
                the Time Slider. Overridden by -frame.  
                Properties: create
        throwOnError (bool?): Playblast is tolerant of failures in most situations. When set,  
                this toggle allows playblast to throw an error on these failures.  
                Properties: create
        useTraxSounds (bool?): Use sounds from TRAX.  
                Properties: create
        viewer (bool?): Specify whether a viewer should be launched for the  
                playblast.  Default is "true".  Runs "fcheck" when -fmt is "image".  
                The player for movie files depends on the OS: Windows uses Microsoft Media  
                Player, Irix uses movieplayer, OSX uses QuickTime.  
                Properties: create
        width (int?): Width of the final image. This value will be clamped if larger than  
                the width of the active window.  
                Windows: If not using fcheck, the width and height must each be divisible  
                by 4.  
                Properties: create
        widthHeight (Tuple[int, int]?): Final image's width and height.  
                Values larger than the dimensions of the active window are clamped.  
                A width and height of 0 means to use the window's current  
                size.  
                Windows: If not using fcheck, the width and height must each be divisible  
                by 4.  
                Properties: create

    Returns:
        str: Name of moviefile created.

    Example:
    """

