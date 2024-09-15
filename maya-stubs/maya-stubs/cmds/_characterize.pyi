from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def characterize(*args: str, edit: bool = ..., query: bool = ..., activatePivot: bool = ..., addAuxEffector: bool = ..., addFloorContactPlane: bool = ..., addMissingEffectors: bool = ..., attributeFromHIKProperty: Queryable[str] = ..., attributeFromHIKPropertyMode: Queryable[str] = ..., autoActivateBodyPart: bool = ..., changePivotPlacement: bool = ..., effectors: str = ..., fkSkeleton: str = ..., name: str = ..., pinHandFeet: bool = ..., placeNewPivot: bool = ..., posture: str = ..., sourceSkeleton: str = ..., stancePose: Queryable[str] = ..., type: str = ...) -> Union[str, bool]:
    """This command is used to scan a joint hierarchy for predefined joint names or
    labels. If the required joints are found, human IK effectors will be created
    to control the skeleton using full-body IK.
    Alternatively, you can manually create all of the components
    required for fullbody IK, and use this command to hook them up.
    Fullbody IK needs 3 major components: the
    user input skeleton (sk), the fk skeleton on which keys are set (fk) and the
    hik effectors (ik).  Together fk and ik provide parameters to the fullbody IK
    engine, which solves for the output and plots it onto sk. This command usage
    is used internally by Maya when importing data from fbx files, but is not generally recommended.Note that a minimum set of required joint names or joint labels  must be
    found in order for the characterize command to succeed. Please refer to the
    Maya documentation for details on properly naming or labeling your skeleton.
    The skeleton should also be z-facing, with its y-axis up, its
    left hand parallel to positive x-axis and right hand parallel to
    negative x-axis.
    END_COMMENTcharacterize, effectors, fullbody, IK
    Args:
        activatePivot (bool?): Activates a pivot that has been properly placed.  After activating this new  
                pivot, you will now be able to rotate and translate about this pivot.  
                A pivot behaves in all ways the same as an effector (it IS an  
                effector, except that it is offset from the normal position of the effector  
                to allow one to rotate about a different point.  
                Properties: edit
        addAuxEffector (bool?): Adds an auxilliary (secondary) effector to an existing effector.  
                Properties: edit
        addFloorContactPlane (bool?): Adds a floor contact plane to one of the hands or feet.  With this plane,  
                you will be able to adjust the floor contact height.  Select a hand or foot  
                effector and then issue the characterize command with this flag.  
                Properties: edit
        addMissingEffectors (bool?): This flag tells the  
                characterize command to look for any effectors that can be added to the  
                skeleton. For example, if the user has deleted some effectors or added fingers  
                to an existing skeleton, "characterize -e -addMissingEffectors" can be used to  
                restore them.  
                Properties: edit
        attributeFromHIKProperty (Queryable[str]?): Query for the attribute name associated with a MotionBuilder property.  
                Properties: query
        attributeFromHIKPropertyMode (Queryable[str]?): Query for the attribute name associated with a MotionBuilder property mode.  
                Properties: query
        autoActivateBodyPart (bool?): Query or change whether auto activation of character nodes representing body parts  
                should be enabled.  
                Properties: query, edit
        changePivotPlacement (bool?): Reverts a pivot back into pivot placement mode.  A pivot that is in placement  
                mode will not participate in full body manipulation until it has been activated  
                with the -activatePivot flag.  
                Properties: edit
        effectors (str?): Specify the effectors to be used by human IK by providing  
                2 pieces of information for each effector:  1) the partial path of the  
                effector and 2) the name of the full body effector this represents.  1) and  
                2) are to be separated by white space, and multiple entries separated by ",".  
                Normally, the effectors are automatically created.  This flag is  
                for advanced users only.  
                Properties: create
        fkSkeleton (str?): Specify the fk skeleton to be used by human IK by providing 2 pieces of  
                information for each joint of the FK skeleton:  1) the partial path of the  
                joint and 2) the name of the full body joint this represents.  1) and 2) are  
                to be separated by white space, and multiple entries separated by ",".  
                Normally, the fk control skeleton is automatically created.  This  
                flag is for advanced users only.  
                Properties: create, edit
        name (str?): At characterization (FBIK creation) time, use this flag to name your FBIK character.  
                This will affect the name of the hikHandle node and the control rig will be put  
                into a namespace that matches the name of your character.  If you do not specify  
                the character name, a default one will be used.  
                At the moment edit and query of the character name is not supported.  
                Properties: create
        pinHandFeet (bool?): When the character is first being characterized, pin the hands and feet by default.  
                Properties: create
        placeNewPivot (bool?): Creates a new pivot and puts it into placement mode.  Note that you will  
                not be able to do full body manipulation about this pivot until you have  
                activated it with the -activatePivot flag. A pivot behaves in all ways the  
                same as an effector (it IS an effector, except that it is offset from the  
                normal position of the effector to allow one to rotate about a different  
                point). A new pivot created with this flag allow you to adjust the offset  
                interactively before activating it.  
                Properties: edit
        posture (str?): Specifies the posture of the character. Valid options are "biped" and  
                "quadruped". The default is "biped".  
                Properties: create
        sourceSkeleton (str?): This flag can be used to characterize a skeleton that has not been named or  
                labelled according to the FBIK guidelines. It specifies the association  
                between the actual joint names and the expected FBIK joint names. The format  
                of the string is as follows: For each  
                joint that the user wants to involve in the solve:  1) the partial path of  
                the joint and 2) the name of the full body joint this represents.  1) and 2)  
                are to be separated by white space, and multiple entries separated by ",".  
                Properties: create, edit
        stancePose (Queryable[str]?): Specify the default stance pose to be used by human IK.  The stance pose is  
                specified by providing 2 pieces of information for each joint involved in  
                the solve:  
                1) the partial path to the joint and 2) 9 numbers representing translation  
                rotation and scale.  
                1) and 2) are to be separated by white space, and multiple entries separated  
                by ",".  
                Normally, the stance pose is taken from the selected skeleton.  This flag is  
                for advanced users only.  
                Properties: create, query
        type (str?): Specifies the technique used by the characterization to identify the joint  
                type. Valid options are "label" and "name". When "label" is used, the joints  
                must be labelled using the guidelines described in the Maya documentation.  
                When name is used, the joint names must follow the naming conventions  
                described in the Maya documentation. The default is "name". This flag  
                cannot be used in conjunction with the sourceSkeleton flag.  
                Properties: create

    Returns:
        str: Names of full body IK effectors that were created.

    Example:
    """

