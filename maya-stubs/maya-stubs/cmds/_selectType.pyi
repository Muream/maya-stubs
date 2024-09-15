from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def selectType(*, query: bool = ..., allComponents: bool = ..., allObjects: bool = ..., animBreakdown: bool = ..., animCurve: bool = ..., animInTangent: bool = ..., animKeyframe: bool = ..., animOutTangent: bool = ..., byName: Multiuse[Tuple[str, bool]] = ..., camera: bool = ..., cluster: bool = ..., collisionModel: bool = ..., controlVertex: bool = ..., curve: bool = ..., curveKnot: bool = ..., curveOnSurface: bool = ..., curveParameterPoint: bool = ..., dimension: bool = ..., dynamicConstraint: bool = ..., edge: bool = ..., editPoint: bool = ..., emitter: bool = ..., facet: bool = ..., field: bool = ..., fluid: bool = ..., follicle: bool = ..., hairSystem: bool = ..., handle: bool = ..., hull: bool = ..., ikEndEffector: bool = ..., ikHandle: bool = ..., imagePlane: bool = ..., implicitGeometry: bool = ..., isoparm: bool = ..., joint: bool = ..., jointPivot: bool = ..., lattice: bool = ..., latticePoint: bool = ..., light: bool = ..., localRotationAxis: bool = ..., locator: bool = ..., locatorUV: bool = ..., locatorXYZ: bool = ..., meshUVShell: bool = ..., motionTrailPoint: bool = ..., motionTrailTangent: bool = ..., nCloth: bool = ..., nParticle: bool = ..., nParticleShape: bool = ..., nRigid: bool = ..., nonlinear: bool = ..., nurbsCurve: bool = ..., nurbsSurface: bool = ..., objectComponent: bool = ..., orientationLocator: bool = ..., particle: bool = ..., particleShape: bool = ..., plane: bool = ..., polymesh: bool = ..., polymeshEdge: bool = ..., polymeshFace: bool = ..., polymeshFreeEdge: bool = ..., polymeshUV: bool = ..., polymeshVertex: bool = ..., polymeshVtxFace: bool = ..., queryByName: str = ..., rigidBody: bool = ..., rigidConstraint: bool = ..., rotatePivot: bool = ..., scalePivot: bool = ..., sculpt: bool = ..., selectHandle: bool = ..., spring: bool = ..., springComponent: bool = ..., stroke: bool = ..., subdiv: bool = ..., subdivMeshEdge: bool = ..., subdivMeshFace: bool = ..., subdivMeshPoint: bool = ..., subdivMeshUV: bool = ..., surfaceEdge: bool = ..., surfaceFace: bool = ..., surfaceKnot: bool = ..., surfaceParameterPoint: bool = ..., surfaceRange: bool = ..., surfaceUV: bool = ..., texture: bool = ..., vertex: bool = ...) -> bool:
    """Thecommand is used to change the set of
    allowable types of objects that can be selected when using
    the select tool. It accepts no other arguments besides the flags.There are basically two different types of items that are selectable
    when interactively selecting objects in the 3D views.  They are
    classified as objects (entire objects) or components (parts of
    objects).  Theandcommand flags
    control which class of objects are selectable.It is possible to select components while in the object selection mode.
    To set the components which are selectable in object
    selection mode you must use the -ocm flag when specifying the component
    flags.
    Args:
        allComponents (bool?): Set all component selection masks on/off  
                Properties: create, query
        allObjects (bool?): Set all object selection masks on/off  
                Properties: create, query
        animBreakdown (bool?): Set animation breakdown selection mask on/off.  
                Properties: create, query
        animCurve (bool?): Set animation curve selection mask on/off.  
                Properties: create, query
        animInTangent (bool?): Set animation in-tangent selection mask on/off.  
                Properties: create, query
        animKeyframe (bool?): Set animation keyframe selection mask on/off.  
                Properties: create, query
        animOutTangent (bool?): Set animation out-tangent selection mask on/off.  
                Properties: create, query
        byName (Multiuse[Tuple[str, bool]]?): Set the specified user-defined selection mask on/off. (object flag)  
                Properties: create, multiuse
        camera (bool?): Set camera selection mask on/off. (object flag)  
                Properties: create, query
        cluster (bool?): Set cluster selection mask on/off. (object flag)  
                Properties: create, query
        collisionModel (bool?): Set collision model selection mask on/off. (object flag)  
                Properties: create, query
        controlVertex (bool?): Set control vertex selection mask on/off. (component flag)  
                Properties: create, query
        curve (bool?): Set curve selection mask on/off. (object flag)  
                Properties: create, query
        curveKnot (bool?): Set curve knot selection mask on/off. (component flag)  
                Properties: create, query
        curveOnSurface (bool?): Set curve-on-surface selection mask on/off. (object flag)  
                Properties: create, query
        curveParameterPoint (bool?): Set curve parameter point selection mask on/off. (component flag)  
                Properties: create, query
        dimension (bool?): Set dimension shape selection mask on/off. (object flag)  
                Properties: create, query
        dynamicConstraint (bool?): Set dynamicConstraint selection mask on/off. (object flag)  
                Properties: create, query
        edge (bool?): Set mesh edge selection mask on/off. (component flag)  
                Properties: create, query
        editPoint (bool?): Set edit-point selection mask on/off. (component flag)  
                Properties: create, query
        emitter (bool?): Set emitter selection mask on/off. (object flag)  
                Properties: create, query
        facet (bool?): Set mesh face selection mask on/off. (component flag)  
                Properties: create, query
        field (bool?): Set field selection mask on/off. (object flag)  
                Properties: create, query
        fluid (bool?): Set fluid selection mask on/off. (object flag)  
                Properties: create, query
        follicle (bool?): Set follicle selection mask on/off. (object flag)  
                Properties: create, query
        hairSystem (bool?): Set hairSystem selection mask on/off. (object flag)  
                Properties: create, query
        handle (bool?): Set object handle selection mask on/off. (object flag)  
                Properties: create, query
        hull (bool?): Set hull selection mask on/off. (component flag)  
                Properties: create, query
        ikEndEffector (bool?): Set ik end effector selection mask on/off. (object flag)  
                Properties: create, query
        ikHandle (bool?): Set ik handle selection mask on/off. (object flag)  
                Properties: create, query
        imagePlane (bool?): Set image plane selection mask on/off. (component flag)  
                Properties: create, query
        implicitGeometry (bool?): Set implicit geometry selection mask on/off. (object flag)  
                Properties: create, query
        isoparm (bool?): Set surface iso-parm selection mask on/off. (component flag)  
                Properties: create, query
        joint (bool?): Set ik handle selection mask on/off. (object flag)  
                Properties: create, query
        jointPivot (bool?): Set joint pivot selection mask on/off. (component flag)  
                Properties: create, query
        lattice (bool?): Set lattice selection mask on/off. (object flag)  
                Properties: create, query
        latticePoint (bool?): Set lattice point selection mask on/off. (component flag)  
                Properties: create, query
        light (bool?): Set light selection mask on/off. (object flag)  
                Properties: create, query
        localRotationAxis (bool?): Set local rotation axis selection mask on/off. (component flag)  
                Properties: create, query
        locator (bool?): Set locator (all types) selection mask on/off. (object flag)  
                Properties: create, query
        locatorUV (bool?): Set uv locator selection mask on/off. (object flag)  
                Properties: create, query
        locatorXYZ (bool?): Set xyz locator selection mask on/off. (object flag)  
                Properties: create, query
        meshUVShell (bool?): Set uv shell component mask on/off.  
                Properties: create, query
        motionTrailPoint (bool?): Set motion point selection mask on/off.  
                Properties: create, query
        motionTrailTangent (bool?): Set motion point tangent mask on/off.  
                Properties: create, query
        nCloth (bool?): Set nCloth selection mask on/off. (object flag)  
                Properties: create, query
        nParticle (bool?): Set nParticle point selection mask on/off. (component flag)  
                Properties: create, query
        nParticleShape (bool?): Set nParticle shape selection mask on/off. (object flag)  
                Properties: create, query
        nRigid (bool?): Set nRigid selection mask on/off. (object flag)  
                Properties: create, query
        nonlinear (bool?): Set nonlinear selection mask on/off. (object flag)  
                Properties: create, query
        nurbsCurve (bool?): Set nurbs-curve selection mask on/off. (object flag)  
                Properties: create, query
        nurbsSurface (bool?): Set nurbs-surface selection mask on/off. (object flag)  
                Properties: create, query
        objectComponent (bool?): Component flags apply to object mode.  
                Properties: create, query
        orientationLocator (bool?): Set orientation locator selection mask on/off. (object flag)  
                Properties: create, query
        particle (bool?): Set particle point selection mask on/off. (component flag)  
                Properties: create, query
        particleShape (bool?): Set particle shape selection mask on/off. (object flag)  
                Properties: create, query
        plane (bool?): Set sketch plane selection mask on/off. (object flag)  
                Properties: create, query
        polymesh (bool?): Set poly-mesh selection mask on/off. (object flag)  
                Properties: create, query
        polymeshEdge (bool?): Set poly-mesh edge selection mask on/off. (component flag)  
                Properties: create, query
        polymeshFace (bool?): Set poly-mesh face selection mask on/off. (component flag)  
                Properties: create, query
        polymeshFreeEdge (bool?): Set poly-mesh free-edge selection mask on/off. (component flag)  
                Properties: create, query
        polymeshUV (bool?): Set poly-mesh UV point selection mask on/off. (component flag)  
                Properties: create, query
        polymeshVertex (bool?): Set poly-mesh vertex selection mask on/off. (component flag)  
                Properties: create, query
        polymeshVtxFace (bool?): Set poly-mesh vertexFace selection mask on/off. (component flag)  
                Properties: create, query
        queryByName (str?): Query the specified user-defined selection mask. (object flag)  
                      In query mode, this flag needs a value.  
                Properties: query
        rigidBody (bool?): Set rigid body selection mask on/off. (object flag)  
                Properties: create, query
        rigidConstraint (bool?): Set rigid constraint selection mask on/off. (object flag)  
                Properties: create, query
        rotatePivot (bool?): Set rotate pivot selection mask on/off. (component flag)  
                Properties: create, query
        scalePivot (bool?): Set scale pivot selection mask on/off. (component flag)  
                Properties: create, query
        sculpt (bool?): Set sculpt selection mask on/off. (object flag)  
                Properties: create, query
        selectHandle (bool?): Set select handle selection mask on/off. (component flag)  
                Properties: create, query
        spring (bool?): Set spring shape selection mask on/off. (object flag)  
                Properties: create, query
        springComponent (bool?): Set individual spring selection mask on/off. (component flag)  
                Properties: create, query
        stroke (bool?): Set the Paint Effects stroke selection mask on/off. (object flag)  
                Properties: create, query
        subdiv (bool?): Set subdivision surfaces selection mask on/off. (object flag)  
                Properties: create, query
        subdivMeshEdge (bool?): Set subdivision surfaces mesh edge selection mask on/off. (component flag)  
                Properties: create, query
        subdivMeshFace (bool?): Set subdivision surfaces mesh face selection mask on/off. (component flag)  
                Properties: create, query
        subdivMeshPoint (bool?): Set subdivision surfaces mesh point selection mask on/off. (component flag)  
                Properties: create, query
        subdivMeshUV (bool?): Set subdivision surfaces mesh UV map selection mask on/off. (component flag)  
                Properties: create, query
        surfaceEdge (bool?): Set surface edge selection mask on/off. (component flag)  
                Properties: create, query
        surfaceFace (bool?): Set surface face selection mask on/off. (component flag)  
                Properties: create, query
        surfaceKnot (bool?): Set surface knot selection mask on/off. (component flag)  
                Properties: create, query
        surfaceParameterPoint (bool?): Set surface parameter point selection mask on/off. (component flag)  
                Properties: create, query
        surfaceRange (bool?): Set surface range selection mask on/off. (component flag)  
                Properties: create, query
        surfaceUV (bool?): Set surface uv selection mask on/off. (component flag)  
                Properties: create, query
        texture (bool?): Set texture selection mask on/off. (object flag)  
                Properties: create, query
        vertex (bool?): Set mesh vertex selection mask on/off. (component flag)  
                Properties: create, query

    Returns:
        bool: if a query operation

    Example:
    """

