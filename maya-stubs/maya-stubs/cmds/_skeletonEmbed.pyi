from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def skeletonEmbed(*args: str, query: bool = ..., mergedMesh: bool = ..., segmentationMethod: int = ..., segmentationResolution: int = ...) -> bool:
    """This command is used to embed a skeleton inside meshes.geomBind
    Args:
        mergedMesh (bool?): When specified, the query command merges selected meshes together and returns a  
                Python object representing the merged mesh.  
                Properties: query
        segmentationMethod (int?): Specifies which segmentation algorithm to use to determine what is inside the mesh  
                and what is outside the mesh.  By default, boundary-and-fill-and-grow voxelization  
                will be used.  
              
                Available algorithms are:  
              
              
                0  : Perfect mesh (no voxelization).  
                This method works for "perfect meshes", i.e. meshes that are closed, watertight,  
                2. manifold and without self-intersection or interior/hidden geometry.  It segments  
                the interior region of the mesh from the exterior using a pseudo-normal test.  
                It does not use voxelization.  If mesh conditions are not respected, the segmentation  
                is likely to be wrong.  This can make the segmentation process significantly longer  
                and prevent successful skeleton embedding.  
              
              
                1. Watertight mesh (flood fill).  
                This method works for "watertight meshes", i.e. meshes for which faces completely  
                separate the interior region of the mesh from the exterior.  The mesh can have  
                degenerated faces, wrong face orientation, self-intersection, etc.  The method  
                uses surface voxelization to classify as part of the interior region all voxels  
                intersecting with a mesh face.  It then performs flood-filling from the outside,  
                marking all reached voxels as part of the exterior region of the model.  Finally,  
                all unreached voxels are marked as part of the interior region.  This method works  
                so long as the mesh is watertight, i.e. without holes up to the voxelization resolution.  
                Otherwise, flood-filling reaches the interior region and creates inaccurate segmentation.  
              
              
                2. Imperfect mesh (flood fill + growing).  
                This method works for meshes where holes could make the flood-filling step reach the  
                interior region of the mesh, but that have face orientation consistent enough so filling  
                them is possible.  First, it uses surface voxelization to classify as part of the interior  
                region all voxels intersecting with a mesh face.  It then alternates flood-filling and  
                growing steps.  The flood-filling tries to reach all voxels from the outside so that  
                unreached voxels are marked as part of the interior region.  The growing step uses a  
                relatively computation-intensive process to check for interior voxels in all neighbors  
                to those already identified.  Any voxel identified as interior is likely to fill holes,  
                allowing subsequent flood-filling steps to identify more interior voxels.  
              
              
                3. Polygon soup (repair).  
                This method has no manifold or face orientation requirements.  It reconstructs a mesh  
                that wraps the input mesh with a given offset (3 times the voxel size) and uses this  
                perfect 2. manifold mesh to segment the interior region from the exterior region of the model.  
                Because of the offset, it might lose some of the details and merge parts that are proximal.  
                However, this usually is not an issue with common models where body parts are not too close  
                to one another.  
              
              
                99. Direct skeleton (no embedding).  
                This method does not try to perform embedding.  It simply returns the skeleton in its initial  
                pose without any attempt at embedding inside the meshes, other than placing it in the meshes  
                bounding box.  
                Properties: create
        segmentationResolution (int?): Specifies which segmentation resolution to use for the voxel grid.  By default,  
                256x256x256 voxels will be used.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

