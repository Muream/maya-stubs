from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dynExport(*args: str, allObjects: bool = ..., attribute: Multiuse[str] = ..., format: str = ..., maxFrame: int = ..., minFrame: int = ..., onlyUpdateParticles: bool = ..., overSampling: int = ..., path: str = ...) -> str:
    """Export particle data to disk files.For cache export (-format cache), dynExport also sets three attributes
    of the current dynGlobals node.  It sets the useParticleRenderCache
    attribute to true, and the min/maxFrameOfLastParticleRenderCache
    attributes to correspond to the min and max frames.Exported .pda or .pdb files are assigned a name of form, whereis "pda" or "pdb."The naming convention for .pdc files is similar but does not use frame
    numbers, it uses a more precise representation of the time instead.By default, the pda and pdb formats export all per-particle
    attributes, and all integer or float type attributes except those
    which are hidden or not storable. (Exception: level of detail is not
    exported, by default) The pdc format exports all attributes which the
    particle object needs for its state cache.To specify only selected attributes, use the -atr flag (which is
    multi-use).  In general, it is recommended not to use this flag with
    pdc type, since you need all the attributes in order for the cache to
    be useful.dynExport exports data for the current frame, or for a range of frames
    specified with -mnf and -mxf. If you are not already at the start
    frame, dynExport will run up the scene for you.If you use dynExport in -prompt mode, it does NOT
    automatically force evaluation of your objects.  You must do this
    yourself from your script.  The easiest way is to request each
    particle object's "count" attribute each frame.  You must request the
    count attribute for each object you want to export, because their
    solvers run independently of one another.  In interactive mode,
    objects WILL get evaluated automatically and you don't have to worry
    about any of this.When exporting a particle object whose particles are created from
    collisions involving particles in another particle object(s), you must
    make sure you simultaneously export all the particle objects involved
    in the dependency chain otherwise you will get an empty cache file.For non-per-particle attributes, pda and pdb formats write the
    identical value once for each particle.  The following types of
    non-per-particle attributes can be exported: float, double,
    doubleLinear, doubleAngle, byte, short, long, enum.  The first four
    are exported as "Real" (in PDB parlance), and the last four as
    "Integer."In the pda and pdb formats, "particleId" and "particleId0" are
    exported as Integer, and are exported under the names "id" and "id0"
    respectively.  All other attributes are exported under their long
    names.
    Args:
        allObjects (bool?): Ignore the selection list and export all particle objects.  
                If you also specify an object name, the -all flag will be ignored.  
                Properties: create
        attribute (Multiuse[str]?): Name of attribute to be exported. If any specified object  
                does not have one of the specified attributes, dynExport will issue  
                an error and not do the export.  
                Properties: create, multiuse
        format (str?): Desired format: "binary" ("pdb"), "ascii" ("pda"), or "cache" ("pdc").  
                The pdc format is for use by the Maya particle system to  
                cache particle data.  The pda and pdb format options  
                are intended for pipelines involving other software (for example,  
                sending the data to some program written in-house);  
                Maya cannot read pda or pdb files.  
                There is no formal description of the PDB format, but the  
                ExploreMe/particles/readpdb directory contains the source  
                and Makefile for a small, simple C program called "readpdb"  
                which reads it. Note that you must compile and run readpdb on the  
                platform which you exported the files on.  
                Properties: create
        maxFrame (int?): Ending frame to be exported.  
                Properties: create
        minFrame (int?): Starting frame to be exported. The export operation will play the  
                scene through from min frame to max frame as it exports.  
                Properties: create
        onlyUpdateParticles (bool?): Specify to only update the particles before exporting.  
                Properties: create
        overSampling (int?): OverSampling to be used during export.  
                Properties: create
        path (str?): This option allows you to specify a subdirectory of the workspace  
                "particles" directory where you want the exported files to be stored.  
                By default, files are stored in the workspace particles directory,  
                i.e., -path is relative to that directory.  
                ( Please Read This:  This is a change from previous versions of Maya  
                in which the path was relative to the workspace root directory.)  
                You can set the "particles" directory anywhere you want using the  
                project window or workspace -fr command. (In this way, you can use  
                an absolute path for export).  
                The -path flag cannot handle strings which include "/" or "\\",  
                in other words, it lets you go down only one level in the directory hierarchy.  
                If you specify a path which doesn't exist, the action will create it  
                if possible; if it can't create the path it will warn you and fail.  
                If you are using a project for which a particle data directory is  
                not defined, dynExport will create a default one called "particles"  
                and add it to your workspace.  
                Properties: create

    Returns:
        str: Path to the exported files

    Example:
    """

