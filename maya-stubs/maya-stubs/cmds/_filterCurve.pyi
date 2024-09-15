from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def filterCurve(*args: str, cutoffFrequency: float = ..., endTime: int = ..., filter: str = ..., keepKeysOnFrame: bool = ..., kernel: str = ..., keySync: bool = ..., maxTimeStep: float = ..., minTimeStep: float = ..., period: float = ..., precision: float = ..., precisionMode: int = ..., preserveKeyTangent: Multiuse[str] = ..., sampleCount: int = ..., samplingRate: float = ..., selectedKeys: bool = ..., startTime: int = ..., timeTolerance: float = ..., tolerance: float = ..., useQuaternion: bool = ..., width: int = ...) -> int:
    """The filterCurve command takes a list of anim curve and filters
            them using a specified filter. The following filters are supported:filter
    Args:
        cutoffFrequency (float?): Defines the cutoff frequency (in Hz) for the Butterworth filter.  
                Properties: create
        endTime (int?): Specify the end time of the section to filter. If not specified, the last  
                key of the animation curve is used to define the end time.  
                Properties: create
        filter (str?): Specifies the filter type to use. The avalible filters are:  
                butterworth  
                euler (default)  
                gaussian  
                keyReducer  
                peakRemover  
                keySync  
                resample  
                simplify  
                Properties: create
        keepKeysOnFrame (bool?): When specified, a secondary filter pass is applied to position keys on whole  
                frames. This flag is only supported by the Butterworth filter.  
                Properties: create
        kernel (str?): The resample kernel is a decimation resampling filter used to resample  
                dense data. It works on the keyframes and may not produce the desired results  
                when used with sparse data.  
              
                The resample filter converts from either uniform or non-uniform  
                timestep input data samples to the specified uniform timeStep. Various  
                time domain filters are available and are specified with the kernel  
                flag which selects the resampling kernel applied to the keyframes  
                on the animation curves.  
              
              
                Kernel Values  
                closest  
                 Closest sample to output timestamp  
                lirp  
                 Linear interpolation between closest samples  
                box  
                 Box filter: moving average  
                triangle  
                 Triangle filter: (1. |x|)  weighted moving average  
                gaussian2  
                 Gaussian2 Filter: (2^(-2x*x))  weighted moving average  
                gaussian4  
                 Gaussian4 Filter: (2^(-4x*x))  weighted moving average  
              
              
                This filter is only targeted at decimation resampling  
                -- interpolation resampling is basically unsupported.  If your  
                output framerate is much higher than your input frame rate  
                (approximate, as the input timestep is not assumed to be regular)  
                the lirp and triangle will interpolate (usually) and the rest will  
                either average, or use the closest sample (depending on the  
                phase and frequency of the input).  However this mode of operation  
                may not give the expected result.  
                Properties: create
        keySync (bool?): When specified, a secondary filter pass is applied that adds a key to sibling  
                curves (X,Y,Z) for each key that is encountered. This flag is only supported by the  
                Key Reducer filter.  
                Properties: create
        maxTimeStep (float?): Simplify filter.  
                Properties: create
        minTimeStep (float?): Simplify filter.  
                Properties: create
        period (float?): Resample filter  
                Properties: create
        precision (float?): Defines the precision parameter.  
                For the Key Reducer filter, this parameter specifies the error limit between the  
                source and output curves. Greater values reduce precision. Lower values increase  
                precision.  
                Properties: create
        precisionMode (int?): Defines whether the precision value should be treated as:  
                0. An absolute value  
                1. A percentage.  
                Properties: create
        preserveKeyTangent (Multiuse[str]?): When specified, keys whose in or out tangent type match the  
                specified type are preserved.  
                Supported tangent types:  
                fixed  
                linear  
                flat  
                smooth  
                step  
                clamped  
                plateau  
                stepnext  
                auto  
                This flag is only supported by the Key Reducer filter.  
                Properties: create, multiuse
        sampleCount (int?): Defines the Gaussian filter kernel dimension.  
                Properties: create
        samplingRate (float?): Defines the rate at which keys are added to the Butterworth filtered curve in  
                frames per second (FPS).  
                Properties: create
        selectedKeys (bool?): When specified, the filter is only applied to selected keys. This flag  
                supercedes the startTime/endTime specification.  
                Properties: create
        startTime (int?): Specify the start time to filter. If not specified, then the first key in the  
                animation curve is used to get the start time.  
                Properties: create
        timeTolerance (float?): Simplify filter.  
                Properties: create
        tolerance (float?): Simplify filter.  
                Properties: create
        useQuaternion (bool?): Enable to use quaternion instead of euler.  
                Properties: create
        width (int?): Defines the width of the Gaussian filter.  
                Properties: create

    Returns:
        int: The number of filtered curves

    Example:
    """

