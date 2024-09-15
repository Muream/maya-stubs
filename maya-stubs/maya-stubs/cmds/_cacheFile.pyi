from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def cacheFile(*args: str, edit: bool = ..., query: bool = ..., appendFrame: bool = ..., attachFile: bool = ..., cacheFileNode: Multiuse[str] = ..., cacheFormat: Queryable[str] = ..., cacheInfo: Queryable[Multiuse[str]] = ..., cacheableAttrs: Queryable[str] = ..., cacheableNode: Multiuse[str] = ..., channelIndex: bool = ..., channelName: Queryable[Multiuse[str]] = ..., convertPc2: bool = ..., createCacheNode: bool = ..., creationChannelName: Multiuse[str] = ..., dataSize: bool = ..., deleteCachedFrame: bool = ..., descriptionFileName: bool = ..., directory: Queryable[str] = ..., doubleToFloat: bool = ..., endTime: int = ..., fileName: Queryable[str] = ..., format: str = ..., geometry: bool = ..., inAttr: Multiuse[str] = ..., inTangent: str = ..., interpEndTime: int = ..., interpStartTime: int = ..., noBackup: bool = ..., outAttr: Multiuse[str] = ..., outTangent: str = ..., pc2File: str = ..., pointCount: bool = ..., points: Multiuse[str] = ..., pointsAndNormals: Multiuse[str] = ..., prefix: bool = ..., refresh: bool = ..., replaceCachedFrame: bool = ..., replaceWithoutSimulating: bool = ..., runupFrames: Queryable[int] = ..., sampleMultiplier: Queryable[int] = ..., simulationRate: Queryable[int] = ..., singleCache: bool = ..., startTime: int = ..., staticCache: bool = ..., worldSpace: bool = ...) -> Union[str, Multiuse[str], bool, int]:
    """Creates one or more cache files on disk to store attribute data for a span of
    frames. The caches can be created for points/normals on a geometry (using
    the pts/points or pan/pointsAndNormals flag), for vectorArray output data
    (using the oa/outAttr flag), or for additional node specific data (using the
    cnd/cacheableNode flag for those nodes that support it).When the ia/inAttr flag is used, connects a cacheFile node that
    associates the data file on disk with the attribute.Frames can be replaced/appended to an existing cache with the
    rcf/replaceCachedFrame and apf/appendFrame flag.  Replaced frames are never deleted.
    They are stored in the same directory as the original cache files with the
    name provided by the f/fileName flag. If no file name is provided,
    the cacheFile name is prefixed with "backup" followed by a unique number.Single file caches are backed up in their entirety. To revert to an older
    version, simply attach to this cache. One file per frame caches only backup
    the description file and the frames that were replaced. To recover these
    types of caches, the user must rename these files to the original name.cache, file, disk
    Args:
        appendFrame (bool?): Appends data to the cache for the times specified by the startTime and endTime flags. If no  
                time is provided, appends the current time. Must be used in conjunction  
                with the pts/points or cnd/cacheableNode flag. Any overwritten frames will not be  
                deleted, but renamed as specified by the f/fileName flag.  
                Properties: create
        attachFile (bool?): Used to indicate that rather than creating a cache file, that an  
                existing cache file on disk should be attached to an attribute in the scene.  
                The inAttr flag is used to specify the attribute.  
                Properties: create
        cacheFileNode (Multiuse[str]?): Specifies the name of the cache file node(s) we are appending/replacing to  
                if more than one cache is attached to the specified geometries.  
                			In query mode, this flag needs a value.  
                Properties: create, multiuse
        cacheFormat (Queryable[str]?): Cache file format, default is Maya's .mcx format, but others available via plugin  
                Properties: create, query
        cacheInfo (Queryable[Multiuse[str]]?): In create mode, used to specify a mel script returning a string array. When  
                creating the cache, this mel script will be executed and the returned strings  
                will be written to the .xml description file of the cache.  
                In query mode, returns descriptive info stored in the cacheFile such as  
                the user name, Maya scene name and maya version number.  
                Properties: create, query, multiuse
        cacheableAttrs (Queryable[str]?): Returns the list of cacheable attributes defined on the accompanying cache node.  
                This argument requires the use of the cacheableNode flag.  
                Properties: query
        cacheableNode (Multiuse[str]?): Specifies the name of a cacheable node whose contents will be cached.  
                A cacheable node is a node that is specially designed to work with  
                the caching mechanism.  An example of a cacheable node is a nCloth node.  
                			In query mode, this flag needs a value.  
                Properties: create, multiuse
        channelIndex (bool?): A query-only flag which returns the channel index for the selected geometry  
                for the cacheFile node specified using the cacheFileNode flag.  
                Properties: create, query
        channelName (Queryable[Multiuse[str]]?): When attachFile is used, used to indicate the channel in the file that  
                should be attached to inAttr.  If not specified, the first channel in  
                the file is used. In query mode, allows user to query the channels associated  
                with a description file.  
                Properties: create, query, multiuse
        convertPc2 (bool?): Convert a PC2 file to the Maya cache format (true), or convert Maya cache to pc2 format (false)  
                Properties: create
        createCacheNode (bool?): Used to indicate that rather than creating a cache file, that a cacheFile  
                node should be created related to an existing cache file on disk.  
                Properties: create
        creationChannelName (Multiuse[str]?): When creating a new cache, this multi-use flag specifies the channels to be cached.  
                The names come from the cacheable channel names defined by the object being cached.  
                If this flag is not used when creating a cache, then all cacheable channels are cached.  
                Properties: create, multiuse
        dataSize (bool?): This is a query-only flag that returns the size of the data being cached per frame.  
                This flag is to be used in conjunction with the cacheableNode, points,  
                pointsAndNormals and outAttr flags.  
                Properties: query
        deleteCachedFrame (bool?): Deletes cached data for the times specified by the startTime/endTime flags.  
                If no time is provided, deletes the current frame. Must be used in conjunction  
                with the pts/points or cnd/cacheableNode flag. Deleted frames will not be  
                removed from disk, but renamed as specified by the f/fileName flag.  
                Properties: create
        descriptionFileName (bool?): This is a query-only flag that returns the name of the description file  
                for an existing cacheFile node. Or if no cacheFile node is specified, it  
                returns the description file name that would be created based on the other  
                flags specified.  
                Properties: query
        directory (Queryable[str]?): Specifies the directory where the cache files will be located. If the  
                directory flag is not specified, the cache files will be placed in the  
                project data directory.  
                Properties: create, query
        doubleToFloat (bool?): During cache creation, double data is stored in the file as floats.  This helps cut down  
                file size.  
                Properties: create
        endTime (int?): Specifies the end frame of the cache range.  
                Properties: create
        fileName (Queryable[str]?): Specifies the base file name for the cache files. If more than one object is  
                being cached and the format is OneFilePerFrame, each cache file will be  
                prefixed with this base file name. In query mode, returns the files  
                associated with the specified cacheFile node.  
                When used with rpf/replaceCachedFrame or apf/appendFrame specifies the name of the backup files.  
                If not specified, replaced frames will be stored with a default name.  
                			In query mode, this flag can accept a value.  
                Properties: create, query
        format (str?): Specifies the distribution format of the cache.  Valid values are "OneFile" and "OneFilePerFrame"  
                Properties: create
        geometry (bool?): A query flag which returns the geometry controlled by the specified cache node  
                Properties: query
        inAttr (Multiuse[str]?): Specifies the name of the attribute that the cache file will drive.  
                This file is optional when creating cache files.  
                If this flag is not used during create mode, the cache files will  
                be created on disk, but will not be driving anything in the scene.  
                This flag is required when the attachFile flag is used.  
                Properties: create, multiuse
        inTangent (str?): Specifies the in-tangent type when interpolating frames before the replaced  
                frame(s). Must be used with the ist/interpStartTime and iet/interpEndTime flags.  
                Valid values are "linear", "smooth" and "step".  
                Properties: create
        interpEndTime (int?): Specifies the frame until which there will be linear interpolation, beginning  
                at endTime. Must be used with the rpf/replaceCachedFrame or apf/appendFrame flag.  
                Interpolation is achieved by removing frames between endTime and  
                interpEndTime from the cache. Removed frames will be renamed as specified  
                by the f/fileName flag.  
                Properties: create
        interpStartTime (int?): Specifies the frame from which to begin linear interpolation, ending at  
                startTime. Must be used with the rpf/replaceCachedFrame or apf/appendFrame flags.  
                Interpolation is achieved by removing  frames between interpStartTime and  
                startTime from the cache. These removed frames will will be renamed as  
                specified by the f/fileName flag.  
                Properties: create
        noBackup (bool?): Specifies that backup files should not be created for any files that may be over-written during  
                append, replace or delete cache frames. Can only be used with the apf/appendFrame,  
                rpf/replaceCachedFrame or dcf/deleteCachedFrame flags.  
                Properties: create
        outAttr (Multiuse[str]?): Specifies the name of the attribute that will be cached to disk.  
                			In query mode, this flag needs a value.  
                Properties: create, multiuse
        outTangent (str?): Specifies the out-tangent type when interpolating frames after the replaced  
                frame(s). Must be used with the ist/interpStartTime and iet/interpEndTime flags.  
                Valid values are "linear", "smooth" and "step".  
                Properties: create
        pc2File (str?): Specifies the full path to the pc2 file.  Must be used in conjunction with the pc2 flag.  
                Properties: create
        pointCount (bool?): A query flag which returns the number of points stored in the cache file.  
                The channelName flag should be used to specify the channel to be queried.  
                Properties: query
        points (Multiuse[str]?): Specifies the name of a geometry whose points will be cached.  
                			In query mode, this flag needs a value.  
                Properties: create, multiuse
        pointsAndNormals (Multiuse[str]?): Specifies the name of a geometry whose points and normals will be cached.  
                The normals is per-vertex per-polygon. The normals cache cannot be imported  
                back to geometry.  
                This flag can only be used to export cache file. It cannot be used with  
                the apf/appendFrame, dcf/deleteCachedFrame and rpf/replaceCachedFrame flags.  
                			In query mode, this flag needs a value.  
                Properties: create, multiuse
        prefix (bool?): Indicates that the specified fileName should be used as a prefix for the  
                cacheName.  
                Properties: create
        refresh (bool?): When used during cache creation, forces a screen refresh during caching.  
                This causes the cache creation to be slower but allows you to see how the  
                simulation is progressing during the cache.  
                Properties: create
        replaceCachedFrame (bool?): Replaces cached data for the times specified by the startTime/endTime  
                flags. If no time is provided, replaces cache file for the current time.  
                Must be used in conjunction with the pts/points or cnd/cacheableNode flag.  
                Replaced frames will not be deleted, but renamed as specified by the  
                f/fileName flag.  
                Properties: create
        replaceWithoutSimulating (bool?): When replacing cached frames, this flag specifies whether the replacement should  
                come from the cached node without simulating or from advancing time and letting  
                the simulation run.  This flag is valid only when neither the startTime nor endTime flags  
                are used or when both the startTime and endTime flags specify the same time value.  
                Properties: edit
        runupFrames (Queryable[int]?): Specifies the number of frames of runup to simulate ahead of the starting frame.  
                The value must be greater than or equal to 0.  The default is 2.  
                Properties: create, query, edit
        sampleMultiplier (Queryable[int]?): Specifies the sample rate when caches are being created as a multiple of  
                simulation Rate. If the value is 1, then a sample will be cached everytime  
                the time is advanced.  If the value  
                is 2, then every other sample will be cached, and so on.  The default is 1.  
                Properties: create, query, edit
        simulationRate (Queryable[int]?): Specifies the simulation rate when caches are being created.  During cache  
                creation, the time will be advanced by the simulation rate, until the end  
                time of the cache is reached or surpassed.  The value is given in frames.  
                The default value is 1 frame.  
                Properties: create, query, edit
        singleCache (bool?): When used in conjunction with the points, pointsAndNormal or cacheableNode  
                flag, specifies whether multiple geometries should be put into a single  
                cache or to create one cache per geometry (default).  
                Properties: create
        startTime (int?): Specifies the start frame of the cache range.  
                Properties: create
        staticCache (bool?): If false, during cache creation, do not save a cache for the object if it  
                appears to have no animation or deformation. If true, save a cache even if  
                the object appears to have no animation or deformation. Default is true. In  
                query mode, when supplied a shape, the flag returns true if the shape appears  
                to have no animation or deformation.  
                Properties: create, query
        worldSpace (bool?): If the points flag is used, turning on this flag will result in the world  
                space positions of the points being written. The expected use of this  
                flag is for cache export.  
                Properties: create

    Returns:
        str: name of created cache description file(s)

    Example:
    """

