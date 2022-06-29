# from typing import List, Tuple

# def createNode(
#     type_name: str,
#     /,
#     name: str,
#     parent: str,
#     shared: bool,
#     skipSelect: bool,
# ) -> str:
#     """createNode is undoable, **NOT queryable**, and **NOT editable**.

#     This command creates a new node in the dependency graph of the specified type.

#     Args:
#         name: Sets the name of the newly-created node. If it contains namespace path,  the new node will be created under the specified namespace; if the namespace doesn't exist,  we will create the namespace.
#         parent: Specifies the parent in the DAG under which the new node belongs.
#         shared: This node is shared across multiple files,  so only create it if it does not already exist.
#         skipSelect: This node is not to be selected after creation,  the original selection will be preserved.

#     Returns:
#         The name of the new node.

#     Examples:
#         >>> from maya import cmds
#         >>> cmds.createNode('transform', name='transform1')
#         >>> cmds.createNode('nurbsSurface', name='surface1', parent='transform1')
#         >>> cmds.createNode('camera', shared=True, name='top')
#         >>> # This transform will be selected when created
#         >>> cmds.createNode('transform', name='selectedTransform')
#         >>> # This will create a new transform node, but 'selectedTransform'
#         >>> # will still be selected.
#         >>> cmds.createNode('transform', skipSelect=True)
#         >>> # Create node under new namespace
#         >>> cmds.createNode('transform', name='newNS:transform1')
#     """

# def matchTransform(
#     *objects: List[str],
#     scaleBox: bool,
#     pivots: bool,
#     position: bool,
#     positionX: bool,
#     positionY: bool,
#     positionZ: bool,
#     rotation: bool,
#     rotatePivot: bool,
#     rotationX: bool,
#     rotationY: bool,
#     rotationZ: bool,
#     scale: bool,
#     scalePivot: bool,
#     scaleX: bool,
#     scaleY: bool,
#     scaleZ: bool,
# ) -> None:
#     """matchTransform is undoable, *NOT queryable*, and *NOT editable*.

#     This command modifies the source object's transform to match the target object's transform.
#     If no flags are specified then the command will match position, rotation and scaling.

#     Args:
#         - objects: a series of objects. The first objects will be matched to the last one.
#         - pivots: Match the source object(s) scale/rotate pivot positions to the target transform's pivot.
#         - position: Match the source object(s) position to the target object.
#         - positionX: Match the source object(s) X position to the target object.
#         - positionY: Match the source object(s) Y position to the target object.
#         - positionZ: Match the source object(s) Z position to the target object.
#         - rotatePivot: Match the source object(s) rotate pivot position to the target transform's pivot.
#         - rotation: Match the source object(s) rotation to the target object.
#         - rotationX: Match the source object(s) X rotation to the target object.
#         - rotationY: Match the source object(s) Y rotation to the target object.
#         - rotationZ: Match the source object(s) Z rotation to the target object.
#         - scale: Match the source object(s) scale to the target transform.
#         - scaleBox: Use the source/target object's child bounding box size when matching scaling.
#         - scalePivot: Match the source object(s) scale pivot position to the target transform's pivot.
#         - scaleX: Match the source object(s) X scale to the target object.
#         - scaleY: Match the source object(s) Y scale to the target object.
#         - scaleZ: Match the source object(s) Z scale to the target object.

#     Examples:
#         >>> from maya import cmds
#         >>> # create a cone and randomly transform it
#         >>> cmds.polyCone(name='cone1')
#         >>> cmds.scale(0.2, 2.0, 0.2);
#         >>> cmds.rotate(20, 45, 70)
#         >>> cmds.move(-2, 0, 2)
#         >>> # create a cylinder
#         >>> cmds.polyCylinder(name='cylinder1')
#         >>> # modify the cylinder's transform to match the cone
#         >>> cmds.matchTransform('cylinder1','cone1')
#     """

# def parentConstraint(
#     *objects: List[str],
#     createCache: Tuple[float, float],
#     decompRotationToChild: bool,
#     deleteCache: bool,
#     edit: bool,
#     layer: str,
#     maintainOffset: bool,
#     name: str,
#     query: bool,
#     remove: bool,
#     skipRotate: List[str],
#     skipTranslate: List[str],
#     targetList: bool,
#     weight: float,
#     weightAliasList: bool,
# ) -> str:
#     """parentConstraint is undoable, queryable, and editable.

#     Constrain an object's position and rotation so that it behaves as if it were a child of the target object(s). In the case of multiple targets, the overall position and rotation of the constrained object is the weighted average of each target's contribution to the position and rotation of the object.
#     A parentConstraint takes as input one or more "target" DAG transform nodes at which to position and rotate the single "constraint object" DAG transform node. The parentConstraint positions and rotates the constrained object at the weighted average of the world space position, rotation and scale target objects.

#     Args:
#         createCache: This flag is used to generate an animation curve that serves as a cache for the constraint. The two arguments define the start and end frames.  The cache is useful if the constraint has multiple targets and the constraint's interpolation type is set to "no flip". The "no flip" mode prevents flipping during playback, but the result is dependent on the previous frame. Therefore in order to consistently get the same result on a specific frame, a cache must be generated. This flag creates the cache and sets the constraint's interpolation type to "cache". If a cache exists already, it will be deleted and replaced with a new cache.
#         decompRotationToChild: During constraint creation, if the rotation offset between the constrained object and the target object is maintained, this flag indicates close to which object the offset rotation is decomposed. Setting this flag will make the rotation decomposition close to the constrained object instead of the target object, which is the default setting.
#         deleteCache: Delete an existing interpolation cache.
#         layer: Specify the name of the animation layer where the constraint should be added.
#         maintainOffset: If this flag is specified the position and rotation of the constrained object will be maintained.
#         name: Sets the name of the constraint node to the specified name. Default name is constrainedObjectName_constraintType
#         remove: removes the listed target(s) from the constraint.
#         skipRotate: Causes the axis specified not to be considered when constraining rotation. Valid arguments are "x", "y", "z" and "none".
#         skipTranslate: Causes the axis specified not to be considered when constraining translation. Valid arguments are "x", "y", "z" and "none".
#         targetList: Return the list of target objects.
#         weight: Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
#         weightAliasList: Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag

#     Returns:
#         Name of the created constraint node.
#         In query mode, return type is based on queried flag.

#     Examples:
#         >>> from maya import cmds
#         >>> # Position cube1 at the location of cone1
#         >>> # Rotate cube1 to the rotation of cone1
#         >>> cmds.parentConstraint('cone1', 'cube1')
#         >>> # Position cube1 at the average of the locations of cone1 and surf2
#         >>> # Rotate cube1 to the average of the rotations of cone1 and surf2
#         >>> cmds.parentConstraint('cone1', 'surf2', 'cube2', weight=.1)
#         >>> # Sets the weight for cone1's effect on cube2 to 10.
#         >>> cmds.parentConstraint('cone1', 'cube2', edit=True, weight=10.0)
#         >>> # Removes surf2 from cube2's parentConstraint
#         >>> cmds.parentConstraint('surf2', 'cube2', edit=True, remove=True)
#         >>> # Adds surf3 to cube2's parentConstraint with the default weight
#         >>> cmds.parentConstraint('surf3', 'cube2')
#         >>> # Constrain position only in the y-axis with rotation
#         >>> # constraining in all axes
#         >>> cmds.parentConstraint('cone2', 'cube2', skipTranslate=["x","z"])
#     """
