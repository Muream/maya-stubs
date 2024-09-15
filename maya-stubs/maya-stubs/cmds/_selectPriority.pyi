from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def selectPriority(*, query: bool = ..., allComponents: Queryable[int] = ..., allObjects: Queryable[int] = ..., animBreakdown: Queryable[int] = ..., animCurve: Queryable[int] = ..., animInTangent: Queryable[int] = ..., animKeyframe: Queryable[int] = ..., animOutTangent: Queryable[int] = ..., byName: Multiuse[Tuple[str, bool]] = ..., camera: Queryable[int] = ..., cluster: Queryable[int] = ..., collisionModel: Queryable[int] = ..., controlVertex: Queryable[int] = ..., curve: Queryable[int] = ..., curveKnot: Queryable[int] = ..., curveOnSurface: Queryable[int] = ..., curveParameterPoint: Queryable[int] = ..., dimension: Queryable[int] = ..., dynamicConstraint: Queryable[int] = ..., edge: Queryable[int] = ..., editPoint: Queryable[int] = ..., emitter: Queryable[int] = ..., facet: Queryable[int] = ..., field: Queryable[int] = ..., fluid: Queryable[int] = ..., follicle: Queryable[int] = ..., hairSystem: Queryable[int] = ..., handle: Queryable[int] = ..., hull: Queryable[int] = ..., ikEndEffector: Queryable[int] = ..., ikHandle: Queryable[int] = ..., imagePlane: Queryable[int] = ..., implicitGeometry: Queryable[int] = ..., isoparm: Queryable[int] = ..., joint: Queryable[int] = ..., jointPivot: Queryable[int] = ..., lattice: Queryable[int] = ..., latticePoint: Queryable[int] = ..., light: Queryable[int] = ..., localRotationAxis: Queryable[int] = ..., locator: Queryable[int] = ..., locatorUV: Queryable[int] = ..., locatorXYZ: Queryable[int] = ..., meshUVShell: Queryable[int] = ..., motionTrailPoint: Queryable[int] = ..., motionTrailTangent: Queryable[int] = ..., nCloth: Queryable[int] = ..., nParticle: Queryable[int] = ..., nParticleShape: Queryable[int] = ..., nRigid: Queryable[int] = ..., nonlinear: Queryable[int] = ..., nurbsCurve: Queryable[int] = ..., nurbsSurface: Queryable[int] = ..., orientationLocator: Queryable[int] = ..., particle: Queryable[int] = ..., particleShape: Queryable[int] = ..., plane: Queryable[int] = ..., polymesh: Queryable[int] = ..., polymeshEdge: Queryable[int] = ..., polymeshFace: Queryable[int] = ..., polymeshFreeEdge: Queryable[int] = ..., polymeshUV: Queryable[int] = ..., polymeshVertex: Queryable[int] = ..., polymeshVtxFace: Queryable[int] = ..., queryByName: str = ..., rigidBody: Queryable[int] = ..., rigidConstraint: Queryable[int] = ..., rotatePivot: Queryable[int] = ..., scalePivot: Queryable[int] = ..., sculpt: Queryable[int] = ..., selectHandle: Queryable[int] = ..., spring: Queryable[int] = ..., springComponent: Queryable[int] = ..., stroke: Queryable[int] = ..., subdiv: Queryable[int] = ..., subdivMeshEdge: Queryable[int] = ..., subdivMeshFace: Queryable[int] = ..., subdivMeshPoint: Queryable[int] = ..., subdivMeshUV: Queryable[int] = ..., surfaceEdge: Queryable[int] = ..., surfaceFace: Queryable[int] = ..., surfaceKnot: Queryable[int] = ..., surfaceParameterPoint: Queryable[int] = ..., surfaceRange: Queryable[int] = ..., texture: Queryable[int] = ..., vertex: Queryable[int] = ...) -> int:
    """Thecommand is used to change the selection
    priority of particular types of objects that can be selected when using
    the select tool. It accepts no other arguments besides the flags.
    These flags are the same as used by the 'selectType' command.
    Args:
        allComponents (Queryable[int]?): Set all component selection priority  
                Properties: create, query
        allObjects (Queryable[int]?): Set all object selection priority  
                Properties: create, query
        animBreakdown (Queryable[int]?): Set animation breakdown selection priority  
                Properties: create, query
        animCurve (Queryable[int]?): Set animation curve selection priority  
                Properties: create, query
        animInTangent (Queryable[int]?): Set animation in-tangent selection priority  
                Properties: create, query
        animKeyframe (Queryable[int]?): Set animation keyframe selection priority  
                Properties: create, query
        animOutTangent (Queryable[int]?): Set animation out-tangent selection priority  
                Properties: create, query
        byName (Multiuse[Tuple[str, bool]]?): Set selection priority for the specified user-defined selection type  
                Properties: create, multiuse
        camera (Queryable[int]?): Set camera selection priority  
                Properties: create, query
        cluster (Queryable[int]?): Set cluster selection priority  
                Properties: create, query
        collisionModel (Queryable[int]?): Set collision model selection priority  
                Properties: create, query
        controlVertex (Queryable[int]?): Set control vertex selection priority  
                Properties: create, query
        curve (Queryable[int]?): Set curve selection priority  
                Properties: create, query
        curveKnot (Queryable[int]?): Set curve knot selection priority  
                Properties: create, query
        curveOnSurface (Queryable[int]?): Set curve-on-surface selection priority  
                Properties: create, query
        curveParameterPoint (Queryable[int]?): Set curve parameter point selection priority  
                Properties: create, query
        dimension (Queryable[int]?): Set dimension shape selection priority  
                Properties: create, query
        dynamicConstraint (Queryable[int]?): Set dynamicConstraint selection priority  
                Properties: create, query
        edge (Queryable[int]?): Set mesh edge selection priority  
                Properties: create, query
        editPoint (Queryable[int]?): Set edit-point selection priority  
                Properties: create, query
        emitter (Queryable[int]?): Set emitter selection priority  
                Properties: create, query
        facet (Queryable[int]?): Set mesh face selection priority  
                Properties: create, query
        field (Queryable[int]?): Set field selection priority  
                Properties: create, query
        fluid (Queryable[int]?): Set fluid selection priority  
                Properties: create, query
        follicle (Queryable[int]?): Set follicle selection priority  
                Properties: create, query
        hairSystem (Queryable[int]?): Set hairSystem selection priority  
                Properties: create, query
        handle (Queryable[int]?): Set object handle selection priority  
                Properties: create, query
        hull (Queryable[int]?): Set hull selection priority  
                Properties: create, query
        ikEndEffector (Queryable[int]?): Set ik end effector selection priority  
                Properties: create, query
        ikHandle (Queryable[int]?): Set ik handle selection priority  
                Properties: create, query
        imagePlane (Queryable[int]?): Set image plane selection mask priority  
                Properties: create, query
        implicitGeometry (Queryable[int]?): Set implicit geometry selection priority  
                Properties: create, query
        isoparm (Queryable[int]?): Set surface iso-parm selection priority  
                Properties: create, query
        joint (Queryable[int]?): Set ik handle selection priority  
                Properties: create, query
        jointPivot (Queryable[int]?): Set joint pivot selection priority  
                Properties: create, query
        lattice (Queryable[int]?): Set lattice selection priority  
                Properties: create, query
        latticePoint (Queryable[int]?): Set lattice point selection priority  
                Properties: create, query
        light (Queryable[int]?): Set light selection priority  
                Properties: create, query
        localRotationAxis (Queryable[int]?): Set local rotation axis selection priority  
                Properties: create, query
        locator (Queryable[int]?): Set locator (all types) selection priority  
                Properties: create, query
        locatorUV (Queryable[int]?): Set uv locator selection priority  
                Properties: create, query
        locatorXYZ (Queryable[int]?): Set xyz locator selection priority  
                Properties: create, query
        meshUVShell (Queryable[int]?): Set uv shell component mask on/off.  
                Properties: create, query
        motionTrailPoint (Queryable[int]?): Set motion point selection priority  
                Properties: create, query
        motionTrailTangent (Queryable[int]?): Set motion point tangent priority  
                Properties: create, query
        nCloth (Queryable[int]?): Set nCloth selection priority  
                Properties: create, query
        nParticle (Queryable[int]?): Set nParticle point selection priority  
                Properties: create, query
        nParticleShape (Queryable[int]?): Set nParticle shape selection priority  
                Properties: create, query
        nRigid (Queryable[int]?): Set nRigid selection priority  
                Properties: create, query
        nonlinear (Queryable[int]?): Set nonlinear selection priority  
                Properties: create, query
        nurbsCurve (Queryable[int]?): Set nurbs-curve selection priority  
                Properties: create, query
        nurbsSurface (Queryable[int]?): Set nurbs-surface selection priority  
                Properties: create, query
        orientationLocator (Queryable[int]?): Set orientation locator selection priority  
                Properties: create, query
        particle (Queryable[int]?): Set particle point selection priority  
                Properties: create, query
        particleShape (Queryable[int]?): Set particle shape selection priority  
                Properties: create, query
        plane (Queryable[int]?): Set sketch plane selection priority  
                Properties: create, query
        polymesh (Queryable[int]?): Set poly-mesh selection priority  
                Properties: create, query
        polymeshEdge (Queryable[int]?): Set poly-mesh edge selection priority  
                Properties: create, query
        polymeshFace (Queryable[int]?): Set poly-mesh face selection priority  
                Properties: create, query
        polymeshFreeEdge (Queryable[int]?): Set poly-mesh free-edge selection priority  
                Properties: create, query
        polymeshUV (Queryable[int]?): Set poly-mesh UV point selection priority  
                Properties: create, query
        polymeshVertex (Queryable[int]?): Set poly-mesh vertex selection priority  
                Properties: create, query
        polymeshVtxFace (Queryable[int]?): Set poly-mesh vtxFace selection priority  
                Properties: create, query
        queryByName (str?): Query selection priority for the specified user-defined selection type  
                      In query mode, this flag needs a value.  
                Properties: query
        rigidBody (Queryable[int]?): Set rigid body selection priority  
                Properties: create, query
        rigidConstraint (Queryable[int]?): Set rigid constraint selection priority  
                Properties: create, query
        rotatePivot (Queryable[int]?): Set rotate pivot selection priority  
                Properties: create, query
        scalePivot (Queryable[int]?): Set scale pivot selection priority  
                Properties: create, query
        sculpt (Queryable[int]?): Set sculpt selection priority  
                Properties: create, query
        selectHandle (Queryable[int]?): Set select handle selection priority  
                Properties: create, query
        spring (Queryable[int]?): Set spring shape selection priority  
                Properties: create, query
        springComponent (Queryable[int]?): Set individual spring selection priority  
                Properties: create, query
        stroke (Queryable[int]?): Set stroke selection priority  
                Properties: create, query
        subdiv (Queryable[int]?): Set subdivision surface selection priority  
                Properties: create, query
        subdivMeshEdge (Queryable[int]?): Set subdivision surface mesh edge selection priority  
                Properties: create, query
        subdivMeshFace (Queryable[int]?): Set subdivision surface mesh face selection priority  
                Properties: create, query
        subdivMeshPoint (Queryable[int]?): Set subdivision surface mesh point selection priority  
                Properties: create, query
        subdivMeshUV (Queryable[int]?): Set subdivision surface mesh UV map selection priority  
                Properties: create, query
        surfaceEdge (Queryable[int]?): Set surface edge selection priority  
                Properties: create, query
        surfaceFace (Queryable[int]?): Set surface face selection priority  
                Properties: create, query
        surfaceKnot (Queryable[int]?): Set surface knot selection priority  
                Properties: create, query
        surfaceParameterPoint (Queryable[int]?): Set surface parameter point selection priority  
                Properties: create, query
        surfaceRange (Queryable[int]?): Set surface range selection priority  
                Properties: create, query
        texture (Queryable[int]?): Set texture selection priority  
                Properties: create, query
        vertex (Queryable[int]?): Set mesh vertex selection priority  
                Properties: create, query

    Returns:
        int: if a query operation

    Example:
    """

