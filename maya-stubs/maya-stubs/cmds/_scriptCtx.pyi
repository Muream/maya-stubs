from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def scriptCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., allComponents: Queryable[Multiuse[bool]] = ..., allObjects: Queryable[Multiuse[bool]] = ..., animBreakdown: Queryable[Multiuse[bool]] = ..., animCurve: Queryable[Multiuse[bool]] = ..., animInTangent: Queryable[Multiuse[bool]] = ..., animKeyframe: Queryable[Multiuse[bool]] = ..., animOutTangent: Queryable[Multiuse[bool]] = ..., baseClassName: Queryable[str] = ..., camera: Queryable[Multiuse[bool]] = ..., cluster: Queryable[Multiuse[bool]] = ..., collisionModel: Queryable[Multiuse[bool]] = ..., controlVertex: Queryable[Multiuse[bool]] = ..., cumulativeLists: bool = ..., curve: Queryable[Multiuse[bool]] = ..., curveKnot: Queryable[Multiuse[bool]] = ..., curveOnSurface: Queryable[Multiuse[bool]] = ..., curveParameterPoint: Queryable[Multiuse[bool]] = ..., dimension: Queryable[Multiuse[bool]] = ..., dynamicConstraint: Queryable[Multiuse[bool]] = ..., edge: Queryable[Multiuse[bool]] = ..., editPoint: Queryable[Multiuse[bool]] = ..., emitter: Queryable[Multiuse[bool]] = ..., enableRootSelection: bool = ..., escToQuit: bool = ..., exists: bool = ..., exitUponCompletion: bool = ..., expandSelectionList: bool = ..., facet: Queryable[Multiuse[bool]] = ..., field: Queryable[Multiuse[bool]] = ..., finalCommandScript: Queryable[Callable[..., Any]] = ..., fluid: Queryable[Multiuse[bool]] = ..., follicle: Queryable[Multiuse[bool]] = ..., forceAddSelect: bool = ..., hairSystem: Queryable[Multiuse[bool]] = ..., handle: Queryable[Multiuse[bool]] = ..., history: bool = ..., hull: Queryable[Multiuse[bool]] = ..., ignoreInvalidItems: bool = ..., ikEndEffector: Queryable[Multiuse[bool]] = ..., ikHandle: Queryable[Multiuse[bool]] = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., imagePlane: Queryable[Multiuse[bool]] = ..., implicitGeometry: Queryable[Multiuse[bool]] = ..., isoparm: Queryable[Multiuse[bool]] = ..., joint: Queryable[Multiuse[bool]] = ..., jointPivot: Queryable[Multiuse[bool]] = ..., lastAutoComplete: bool = ..., lattice: Queryable[Multiuse[bool]] = ..., latticePoint: Queryable[Multiuse[bool]] = ..., light: Queryable[Multiuse[bool]] = ..., localRotationAxis: Queryable[Multiuse[bool]] = ..., locator: Queryable[Multiuse[bool]] = ..., locatorUV: Queryable[Multiuse[bool]] = ..., locatorXYZ: Queryable[Multiuse[bool]] = ..., nCloth: Queryable[Multiuse[bool]] = ..., nParticle: Queryable[Multiuse[bool]] = ..., nParticleShape: Queryable[Multiuse[bool]] = ..., nRigid: Queryable[Multiuse[bool]] = ..., name: str = ..., nonlinear: Queryable[Multiuse[bool]] = ..., nurbsCurve: Queryable[Multiuse[bool]] = ..., nurbsSurface: Queryable[Multiuse[bool]] = ..., objectComponent: bool = ..., orientationLocator: Queryable[Multiuse[bool]] = ..., particle: Queryable[Multiuse[bool]] = ..., particleShape: Queryable[Multiuse[bool]] = ..., plane: Queryable[Multiuse[bool]] = ..., polymesh: Queryable[Multiuse[bool]] = ..., polymeshEdge: Queryable[Multiuse[bool]] = ..., polymeshFace: Queryable[Multiuse[bool]] = ..., polymeshFreeEdge: Queryable[Multiuse[bool]] = ..., polymeshUV: Queryable[Multiuse[bool]] = ..., polymeshVertex: Queryable[Multiuse[bool]] = ..., polymeshVtxFace: Queryable[Multiuse[bool]] = ..., rigidBody: Queryable[Multiuse[bool]] = ..., rigidConstraint: Queryable[Multiuse[bool]] = ..., rotatePivot: Queryable[Multiuse[bool]] = ..., scalePivot: Queryable[Multiuse[bool]] = ..., sculpt: Queryable[Multiuse[bool]] = ..., selectHandle: Queryable[Multiuse[bool]] = ..., setAllowExcessCount: Multiuse[bool] = ..., setAutoComplete: Multiuse[bool] = ..., setAutoToggleSelection: Multiuse[bool] = ..., setDoneSelectionPrompt: Multiuse[str] = ..., setNoSelectionHeadsUp: Multiuse[str] = ..., setNoSelectionPrompt: Multiuse[str] = ..., setSelectionCount: Multiuse[int] = ..., setSelectionHeadsUp: Multiuse[str] = ..., setSelectionPrompt: Multiuse[str] = ..., showManipulators: bool = ..., spring: Queryable[Multiuse[bool]] = ..., springComponent: Queryable[Multiuse[bool]] = ..., stroke: Queryable[Multiuse[bool]] = ..., subdiv: Queryable[Multiuse[bool]] = ..., subdivMeshEdge: Queryable[Multiuse[bool]] = ..., subdivMeshFace: Queryable[Multiuse[bool]] = ..., subdivMeshPoint: Queryable[Multiuse[bool]] = ..., subdivMeshUV: Queryable[Multiuse[bool]] = ..., surfaceEdge: Queryable[Multiuse[bool]] = ..., surfaceFace: Queryable[Multiuse[bool]] = ..., surfaceKnot: Queryable[Multiuse[bool]] = ..., surfaceParameterPoint: Queryable[Multiuse[bool]] = ..., surfaceRange: Queryable[Multiuse[bool]] = ..., surfaceUV: Queryable[Multiuse[bool]] = ..., texture: Queryable[Multiuse[bool]] = ..., title: Queryable[str] = ..., toolCursorType: Queryable[str] = ..., toolFinish: Queryable[Callable[..., Any]] = ..., toolStart: Queryable[Callable[..., Any]] = ..., totalSelectionSets: Queryable[int] = ..., vertex: Queryable[Multiuse[bool]] = ...) -> Union[str, Multiuse[bool], bool, Callable[..., Any], int]:
    """This command allows a user to create their own tools based on
    the selection tool. A number of selection lists can be collected,
    the behaviour of the selection and the selection masks are fully
    customizable, etc.The command is processed prior to being executed.  The keyword
    "$Selection#" where # is a number 1 or greater specifies
    a selection set.  The context can specify several selection sets
    which are substituted in place of the $Selection# keyword in the form
    of a Mel string array.  Items that are specific per set need to
    be specified in each set, if they are going to be specified for any of
    the sets.  See examples below.In addition, in order to specify the type of selection you need
    to be making, any of the selection type flags from "selectType" command
    can be used here.
    Args:
        allComponents (Queryable[Multiuse[bool]]?): Set all component selection masks on/off  
                Properties: create, query, multiuse
        allObjects (Queryable[Multiuse[bool]]?): Set all object selection masks on/off  
                Properties: create, query, multiuse
        animBreakdown (Queryable[Multiuse[bool]]?): Set animation breakdown selection mask on/off.  
                Properties: create, query, multiuse
        animCurve (Queryable[Multiuse[bool]]?): Set animation curve selection mask on/off.  
                Properties: create, query, multiuse
        animInTangent (Queryable[Multiuse[bool]]?): Set animation in-tangent selection mask on/off.  
                Properties: create, query, multiuse
        animKeyframe (Queryable[Multiuse[bool]]?): Set animation keyframe selection mask on/off.  
                Properties: create, query, multiuse
        animOutTangent (Queryable[Multiuse[bool]]?): Set animation out-tangent selection mask on/off.  
                Properties: create, query, multiuse
        baseClassName (Queryable[str]?): This string will be used to produce MEL function names for  
                the property sheets for the tool.  For example, if  
                "myScriptTool" was given, the functions "myScriptToolValues"  
                and "myScriptToolProperties" will be used for the  
                property sheets.  The default is "scriptTool".  
                Properties: create, query, edit
        camera (Queryable[Multiuse[bool]]?): Set camera selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        cluster (Queryable[Multiuse[bool]]?): Set cluster selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        collisionModel (Queryable[Multiuse[bool]]?): Set collision model selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        controlVertex (Queryable[Multiuse[bool]]?): Set control vertex selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        cumulativeLists (bool?): If set, the selection lists will be cumulative.  For example,  
                the second list will contain all the items from the first list,  
                the third all the items from the second list etc.  Make sure  
                your script specified above takes that into account.  Relevant  
                if there is more than one selection set.  
                Properties: create, query, edit
        curve (Queryable[Multiuse[bool]]?): Set curve selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        curveKnot (Queryable[Multiuse[bool]]?): Set curve knot selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        curveOnSurface (Queryable[Multiuse[bool]]?): Set curve-on-surface selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        curveParameterPoint (Queryable[Multiuse[bool]]?): Set curve parameter point selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        dimension (Queryable[Multiuse[bool]]?): Set dimension shape selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        dynamicConstraint (Queryable[Multiuse[bool]]?): Set dynamicConstraint selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        edge (Queryable[Multiuse[bool]]?): Set mesh edge selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        editPoint (Queryable[Multiuse[bool]]?): Set edit-point selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        emitter (Queryable[Multiuse[bool]]?): Set emitter selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        enableRootSelection (bool?): If set, the items to be selected are at their root transform  
                level. Default is false.  
                Properties: create, query, edit
        escToQuit (bool?): If set to true, exit the tool when press "Esc". Default is false.  
                Properties: create, query, edit
        exists (bool?): Returns true or false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
        exitUponCompletion (bool?): If set, completing the last selection set will exit the  
                tool.  Default is true.  
                Properties: create, query, edit
        expandSelectionList (bool?): If set, the selection lists will expand to have a single  
                component in each item.  You probably want this as a default, otherwise  
                two isoparms on the same surface will show up as 1 item.  
              
                To ensure that components on the same object are returned in the order in  
                which they are selected, use the selectPref -trackSelectionOrder on  
                command in your -toolStart script to enable ordered  
                selection, then restore it to its original value in your  
                -toolFinish script.  
                Properties: create, query, edit
        facet (Queryable[Multiuse[bool]]?): Set mesh face selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        field (Queryable[Multiuse[bool]]?): Set field selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        finalCommandScript (Queryable[Callable[..., Any]]?): Supply the script that will be run when the user presses the  
                enter key and the context is completed.  Depending on the  
                number of selection sets you have, the script can make use  
                of variables string $Selection1[], $Selection2[], ...  
                Properties: create, query, edit
        fluid (Queryable[Multiuse[bool]]?): Set fluid selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        follicle (Queryable[Multiuse[bool]]?): Set follicle selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        forceAddSelect (bool?): If set to true, together with -setAutoToggleSelection (see  
                below) on the first selection set, causes the first selection after  
                the computation of the previous result to be "shift" selection,  
                unless a modifier key is pressed.  Default is false.  
                Flags for each selection set.  These flags are multi-use.  
                Properties: create, query, edit
        hairSystem (Queryable[Multiuse[bool]]?): Set hairSystem selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        handle (Queryable[Multiuse[bool]]?): Set object handle selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        history (bool?): If this is a tool command, turn the construction history on  
                for the tool in question.  
                Properties: create
        hull (Queryable[Multiuse[bool]]?): Set hull selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        ignoreInvalidItems (bool?): If you have multiple selection sets, the state of the  
                selection set is recorded at the time you "complete it".  You could  
                then delete some of the items in that list and end up with  
                invalid items in one or more of your selection sets.  If this  
                flag is set, those items will be detected and ignored.  You will  
                never know it happened.  Its as if they were never selected in  
                the first place, except that your selection set now does not  
                have as many items as it may need.  If this flag is not set,  
                you will get a warning and your final command callback script  
                will likely not execute because of an error condition.  
                Properties: create, query, edit
        ikEndEffector (Queryable[Multiuse[bool]]?): Set ik end effector selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        ikHandle (Queryable[Multiuse[bool]]?): Set ik handle selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        image1 (Queryable[str]?): First of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        image2 (Queryable[str]?): Second of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        image3 (Queryable[str]?): Third of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        imagePlane (Queryable[Multiuse[bool]]?): Set image plane selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        implicitGeometry (Queryable[Multiuse[bool]]?): Set implicit geometry selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        isoparm (Queryable[Multiuse[bool]]?): Set surface iso-parm selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        joint (Queryable[Multiuse[bool]]?): Set ik handle selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        jointPivot (Queryable[Multiuse[bool]]?): Set joint pivot selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        lastAutoComplete (bool?): True if auto complete is set for the last selection set,  
                false otherwise.  Mostly used for query, but if present in conjuction  
                with -sac/setAutoComplete flag, -sac flag takes precedence.  
                Properties: create, query, edit
        lattice (Queryable[Multiuse[bool]]?): Set lattice selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        latticePoint (Queryable[Multiuse[bool]]?): Set lattice point selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        light (Queryable[Multiuse[bool]]?): Set light selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        localRotationAxis (Queryable[Multiuse[bool]]?): Set local rotation axis selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        locator (Queryable[Multiuse[bool]]?): Set locator (all types) selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        locatorUV (Queryable[Multiuse[bool]]?): Set uv locator selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        locatorXYZ (Queryable[Multiuse[bool]]?): Set xyz locator selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        nCloth (Queryable[Multiuse[bool]]?): Set nCloth selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        nParticle (Queryable[Multiuse[bool]]?): Set nParticle point selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        nParticleShape (Queryable[Multiuse[bool]]?): Set nParticle shape selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        nRigid (Queryable[Multiuse[bool]]?): Set nRigid selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        nonlinear (Queryable[Multiuse[bool]]?): Set nonlinear selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        nurbsCurve (Queryable[Multiuse[bool]]?): Set nurbs-curve selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        nurbsSurface (Queryable[Multiuse[bool]]?): Set nurbs-surface selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        objectComponent (bool?): Component flags apply to object mode.  
                Properties: create, query
        orientationLocator (Queryable[Multiuse[bool]]?): Set orientation locator selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        particle (Queryable[Multiuse[bool]]?): Set particle point selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        particleShape (Queryable[Multiuse[bool]]?): Set particle shape selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        plane (Queryable[Multiuse[bool]]?): Set sketch plane selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        polymesh (Queryable[Multiuse[bool]]?): Set poly-mesh selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        polymeshEdge (Queryable[Multiuse[bool]]?): Set poly-mesh edge selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        polymeshFace (Queryable[Multiuse[bool]]?): Set poly-mesh face selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        polymeshFreeEdge (Queryable[Multiuse[bool]]?): Set poly-mesh free-edge selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        polymeshUV (Queryable[Multiuse[bool]]?): Set poly-mesh UV point selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        polymeshVertex (Queryable[Multiuse[bool]]?): Set poly-mesh vertex selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        polymeshVtxFace (Queryable[Multiuse[bool]]?): Set poly-mesh vertexFace selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        rigidBody (Queryable[Multiuse[bool]]?): Set rigid body selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        rigidConstraint (Queryable[Multiuse[bool]]?): Set rigid constraint selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        rotatePivot (Queryable[Multiuse[bool]]?): Set rotate pivot selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        scalePivot (Queryable[Multiuse[bool]]?): Set scale pivot selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        sculpt (Queryable[Multiuse[bool]]?): Set sculpt selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        selectHandle (Queryable[Multiuse[bool]]?): Set select handle selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        setAllowExcessCount (Multiuse[bool]?): If set, the number if items is to be interpreted as the minimum.  
                Properties: create, edit, multiuse
        setAutoComplete (Multiuse[bool]?): If set to true, as soon as the specified number of items is  
                selected the tool will start the next selection set or run the command.  
                Properties: create, edit, multiuse
        setAutoToggleSelection (Multiuse[bool]?): If set to true, it is as if "shift" key is pressed when there  
                are no modifiers pressed.  That means that you get the "toggle select"  
                behaviour by default.  This only applies to the 3D view, and the  
                selection done in the hypergraph, outliner or elsewhere is still  
                a subject to the usual rules.  
                Properties: create, edit, multiuse
        setDoneSelectionPrompt (Multiuse[str]?): If setAutoComplete is not set (see below) this string will be  
                shown as soon as the tool has enough items for a particular selection  
                set.  If this is not set, but is needed, the same string as set with  
                -setSelectionPrompt flag will be used.  
                Properties: create, edit, multiuse
        setNoSelectionHeadsUp (Multiuse[str]?): Supply a string that will be shown as a heads up prompt when  
                there is nothing selected.  This must be set separately for each  
                selection set.  
                Properties: create, edit, multiuse
        setNoSelectionPrompt (Multiuse[str]?): Supply a string that will be shown as help when there is  
                nothing selected.  This must be set separately for each  
                selection set.  
                Properties: create, edit, multiuse
        setSelectionCount (Multiuse[int]?): The number of items in this selection set.  0 means as many as  
                you need until completion.  
                Properties: create, edit, multiuse
        setSelectionHeadsUp (Multiuse[str]?): Supply a string that will be shown as a heads up prompt when  
                there is something selected.  This must be set separately for each  
                selection set.  
                Properties: create, edit, multiuse
        setSelectionPrompt (Multiuse[str]?): Supply a string that will be shown as help when there is  
                something selected.  This must be set separately for each  
                selection set.  
                Properties: create, edit, multiuse
        showManipulators (bool?): If set, the manipulators will be shown for any active objects.  
                Basically, it is as if you are in the Show Manipulator tool.  
                Properties: create, query, edit
        spring (Queryable[Multiuse[bool]]?): Set spring shape selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        springComponent (Queryable[Multiuse[bool]]?): Set individual spring selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        stroke (Queryable[Multiuse[bool]]?): Set the Paint Effects stroke selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        subdiv (Queryable[Multiuse[bool]]?): Set subdivision surfaces selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        subdivMeshEdge (Queryable[Multiuse[bool]]?): Set subdivision surfaces mesh edge selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        subdivMeshFace (Queryable[Multiuse[bool]]?): Set subdivision surfaces mesh face selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        subdivMeshPoint (Queryable[Multiuse[bool]]?): Set subdivision surfaces mesh point selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        subdivMeshUV (Queryable[Multiuse[bool]]?): Set subdivision surfaces mesh UV map selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        surfaceEdge (Queryable[Multiuse[bool]]?): Set surface edge selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        surfaceFace (Queryable[Multiuse[bool]]?): Set surface face selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        surfaceKnot (Queryable[Multiuse[bool]]?): Set surface knot selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        surfaceParameterPoint (Queryable[Multiuse[bool]]?): Set surface parameter point selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        surfaceRange (Queryable[Multiuse[bool]]?): Set surface range selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        surfaceUV (Queryable[Multiuse[bool]]?): Set surface uv selection mask on/off. (component flag)  
                Properties: create, query, multiuse
        texture (Queryable[Multiuse[bool]]?): Set texture selection mask on/off. (object flag)  
                Properties: create, query, multiuse
        title (Queryable[str]?): Supply a string that will be used as a precursor to all the  
                messages; i.e., the "name" of the tool.  
                Properties: create, query, edit
        toolCursorType (Queryable[str]?): Supply the string identifier to set the tool cursor type  
                when inside of tool. The following are the valid ids:  
                "create", "dolly", "edit", "pencil", "track", "trackHorizontal",  
                "trackVertical", "transformation", "tumble", "zoom", "zoomIn",  
                "zoomOut", "flyThrough", "dot", "fleur",  
                "leftArrow", "question", "doubleHorizArrow", "doubleVertArrow",  
                "sizing", "dollyIn", "dollyOut", "brush", "camera", "noAccess",  
                "input", "output", "leftCycle", "rightCycle", "rightExpand",  
                "knife".  
                Properties: create, query, edit
        toolFinish (Queryable[Callable[..., Any]]?): Supply the script that will be run when the user exits  
                the script.  
                Properties: create, query, edit
        toolStart (Queryable[Callable[..., Any]]?): Supply the script that will be run when the user first  
                enters the script  
                Properties: create, query, edit
        totalSelectionSets (Queryable[int]?): Total number of selection sets.  
                Properties: create, query, edit
        vertex (Queryable[Multiuse[bool]]?): Set mesh vertex selection mask on/off. (component flag)  
                Properties: create, query, multiuse

    Returns:
        str: Context name

    Example:
    """

