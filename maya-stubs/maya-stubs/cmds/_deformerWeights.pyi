from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def deformerWeights(*args: str, edit: bool = ..., query: bool = ..., attribute: Queryable[Multiuse[str]] = ..., defaultValue: Queryable[float] = ..., deformer: Queryable[Multiuse[str]] = ..., export: bool = ..., format: Queryable[str] = ..., ignoreName: bool = ..., im: bool = ..., method: Queryable[str] = ..., path: Queryable[str] = ..., positionTolerance: Queryable[float] = ..., remap: Queryable[Multiuse[str]] = ..., shape: Queryable[Multiuse[str]] = ..., skip: Queryable[Multiuse[str]] = ..., vertexConnections: bool = ..., weightPrecision: Queryable[int] = ..., weightTolerance: Queryable[float] = ..., worldSpace: bool = ...) -> Union[str, Multiuse[str], float, bool, int]:
    """Command to import and export deformer weights to and from a simple XML
     file. The weight data is stored in a per-vertex fashion along with a
     "point cloud" corresponding to the vertices from the geometry input to
     the deformer.
     For example a cluster deformer would have the following information:On import the weights are then mapped back to a specified deformer
     based on the specified mapping method. Note that the geometry used to
     perform the mapping association is not the visible shape but rather
     the incoming geometry to the deformer. For example, in the case of a
     skin cluster this would be the bind pose geometry.deformer, export
    Args:
        attribute (Queryable[Multiuse[str]]?): Specify the long name of deformer attribute that should be imported/exported along with the deformerWeights. i.e. -at "envelope" -at "skinningMethod" etc.. No warning or error is given if a specified attribute does not exist on a particular deformer, making it possible to use this command with multiple deformers without aborting or slowing down the import/export process.  Currently supports numeric attributes and matrix attributes  
                Properties: create, query, edit, multiuse
        defaultValue (Queryable[float]?): Manually set the default value. Default values are values that are not written to file. For example, for blendShapes the default value is automatically set to 1.0 and these values are not written to disk. For skinClusters the value is 0.0. If all weights should be forced to be written to disk, set a defaultValue = -1.0.  
                Properties: create, query, edit
        deformer (Queryable[Multiuse[str]]?): Specify the deformer whose weights should be exported or imported. If a pattern is supplied for the deformer  
                name (i.e: cluster*), only the first deformer that matches the pattern will be imported/exported unless used  
                in conjunction with the -skip option  
                Properties: create, query, edit, multiuse
        export (bool?): Export the given deformer  
                Properties: create, query, edit
        format (Queryable[str]?): Specify either "XML" or "JSON" as the file extension to save as.  
                Properties: create, query, edit
        ignoreName (bool?): Ignore the names of the layers on import, just use the order of the layers instead. This can be used when  
                joint names have been changed. Leaving it on only name that match on import will be write to the deformer.  
                Properties: create, query, edit
        im (bool?): Import weights to the specified deformer. See the method flag for details  
                on how the weights will be mapped to the destination deformer.  
                Properties: create, query, edit
        method (Queryable[str]?): Specify the method used to map the weight during import. Valid values are:  
                "index", "nearest", "barycentric", "bilinear" and "over". The "index" method  
                uses the vertex index to map the weights onto the object. This is most useful  
                when the destination object shares the same topology as the exported data.  
                The "nearest" method finds the nearest vertex in the imported data set and  
                sets the weight value to that value. This is best used when mapping a higher  
                resolution mesh to a lower resolution. The "barycentric" and "bilinear" methods  
                are only supported with polygon mesh exported with -vc/vertexConnections flag.  
                The "barycentric" method finds the nearest triangle of the input geometry and  
                rescales the weights at the triangle vertices according to the barycentric  
                weights to each vertex of the nearest triangle. The "bilinear" method finds the  
                nearest convex quad of the input geometry and rescales the weights at the quad  
                vertices according to the bilinear weights to each vertex of the nearest convex  
                quad. For non-quad polygon, the "bilinear" method will fall back to "barycentric"  
                method. The "over" method is similar to the "index" method but the weights on the  
                destination mesh are not cleared prior to mapping, so that unmatched indices  
                keep their weights intact.  
                Properties: create, query, edit
        path (Queryable[str]?): The path to the given file. Default to the current project.  
                Properties: create, query, edit
        positionTolerance (Queryable[float]?): The position tolerance is used to determine the radius of search for the nearest method. This flag is only  
                used with import.  
                Defaults to a huge number.  
                Properties: create, query, edit
        remap (Queryable[Multiuse[str]]?): Remap maps source regular expression to destination format. It maps any name that matches the regular expression (before the semi-colon) to the expression format (after the semi-colon).  
                For example, -remap "test:(.*);$1" will rename all items in the test namespace to the global namespace. Accepts $1, $2, .., $9 as pattern holders in the expression format.  
                Remap flag must be used together with import or export. When working with import, the name of the object from the xml file matching the regular expression is remapped to object in scene. When working with export, the name of the object from the scene matching the regular expression is remapped to object in xml file.  
                Properties: create, query, edit, multiuse
        shape (Queryable[Multiuse[str]]?): Specify the source shape. Export will write out all the deformers on the shape node into one file.  
                If a pattern is supplied for the shape name (i.e: pCylinder*), only the first shape that matches the pattern will  
                be imported/exported unless used in conjunction with the -skip option.  
                Properties: create, query, edit, multiuse
        skip (Queryable[Multiuse[str]]?): Skip any deformer, shape, or layer that whose name matches the given regular expression string  
                Properties: create, query, edit, multiuse
        vertexConnections (bool?): Export vertex connection information, which is required for -m/-method "barycentric" and "bilinear". The flag is only used with -ex/-export flag. The vertex connection information is automatically loaded during import if available in xml file.  
                Properties: create, query, edit
        weightPrecision (Queryable[int]?): Sets the output decimal precision for exported weights. The default value is 3.  
                Properties: create, query, edit
        weightTolerance (Queryable[float]?): The weight tolerance is used to decide if a given weight value is close enough to the default value that it does not need to be included. This flag is only used with export. The default value is .001.  
                Properties: create, query, edit
        worldSpace (bool?): For spatially based association methods (nearest), the position should be based on the world space position  
                rather then the local object space.  
                Properties: create, query, edit

    Returns:
        str: path to the file imported/exported, if successful

    Example:
    """

