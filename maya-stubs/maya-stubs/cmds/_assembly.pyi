from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def assembly(*args: str, edit: bool = ..., query: bool = ..., active: Queryable[str] = ..., activeLabel: Queryable[str] = ..., canCreate: Queryable[str] = ..., createOptionBoxProc: Queryable[Callable[..., Any]] = ..., createRepresentation: str = ..., defaultType: Queryable[str] = ..., deleteRepresentation: str = ..., deregister: str = ..., input: str = ..., isAType: Queryable[str] = ..., isTrackingMemberEdits: Queryable[str] = ..., label: Queryable[str] = ..., listRepTypes: bool = ..., listRepTypesProc: Queryable[Callable[..., Any]] = ..., listRepresentations: bool = ..., listTypes: bool = ..., name: str = ..., newRepLabel: str = ..., postCreateUIProc: Queryable[Callable[..., Any]] = ..., proc: Callable[..., Any] = ..., renameRepresentation: str = ..., repLabel: str = ..., repName: str = ..., repNamespace: Queryable[str] = ..., repPostCreateUIProc: str = ..., repPreCreateUIProc: str = ..., repType: str = ..., repTypeLabel: str = ..., repTypeLabelProc: Queryable[Callable[..., Any]] = ..., type: str = ...) -> Union[bool, str, Callable[..., Any]]:
    """Command to register assemblies for the scene assembly
    framework, to create them, and to edit and query them.
    Assembly nodes are DAG nodes, and are therefore shown in the various
    DAG editors (Outliner, Hypergraph, Node Editor). At assembly creation time,
    the node name defaults to the node type name.
    The assembly command can create any node that is derived from the assembly
    node base class.  It also acts as a registry of these types, so that various
    scripting callbacks can be defined and registered with the assembly
    command.  These callbacks are invoked by Maya during operations on
    assembly nodes, and can be used to customize behavior.When defining a new type of assembly derived from the assembly node
    base class, a number of procedures can be defined through the assembly
    command to properly integrate the new assembly node type into Maya.
    Most of these procedures are used to integrate the assembly type with the
    Maya user interface, and are not required for non-interactive
    scripting use.  For more information, see the MPxAssembly class
    description in the Maya API documentation.
    Some of the important procedures that can be registered through the assembly
    command are the following:representation, assembly
    Args:
        active (Queryable[str]?): Set the active representation by name, or query the name of the active representation.  
                Edit mode can be applied to more than one assembly.  
                Query mode will return a single string when only a single assembly is specified,  
                and will return an array of strings when multiple assemblies are specified.  
                Using an empty string as name means to inactivate the currently active representation.  
                Properties: query, edit
        activeLabel (Queryable[str]?): Set the active representation by label, or query the label of the active representation.  
                Edit mode can be applied to more than one assembly.  
                Query mode will return a single string when only a single assembly is specified,  
                and will return an array of strings when multiple assemblies are specified.  
                Properties: query, edit
        canCreate (Queryable[str]?): Query the representation types the specific assembly can create.  
                Properties: query
        createOptionBoxProc (Queryable[Callable[..., Any]]?): Set or query the option box menu procedure for a specific assembly type.  
                The assembly type will be the default type, unless  
                the -type flag is used to specify an explicit assembly type.  
                Properties: query, edit
        createRepresentation (str?): Create and add a specific type of representation for an assembly.  
                If the representation type needs additional parameters, they  
                must be specified using the "input" flag. For example, the Maya  
                scene assembly reference implementation Cache and Scene  
                representations need an input file.  
                Properties: edit
        defaultType (Queryable[str]?): Set or query the default type of assembly.  When the assembly  
                command is used to perform an operation on an assembly type rather  
                than on an assembly object, it will be performed on the default  
                type, unless the -type flag is used to specify an explicit assembly type.  
                Properties: query, edit
        deleteRepresentation (str?): Delete a specific representation from an assembly.  
                Properties: edit
        deregister (str?): Deregister a registered assembly type.  
                If the deregistered type is the default type,  
                the default type will be set to the empty string.  
                Properties: edit
        input (str?): Specify the additional parameters of representation creation procedure  
                when creating a representation.  
                This flag must be used with createRepresentation flag.  
                Properties: edit
        isAType (Queryable[str]?): Query whether the given object is of an assembly type.  
                Properties: query
        isTrackingMemberEdits (Queryable[str]?): Query whether the given object is tracking member edits.  
                Properties: query
        label (Queryable[str]?): Set or query the label for an assembly type. Assembly type is specified  
                with flag "type". If no type specified, the default type is used.  
                Properties: query, edit
        listRepTypes (bool?): Query the supported representation types for a given assembly type.  The  
                assembly type will be the default type, unless the -type flag is used to  
                specify an explicit assembly type.  
                Properties: query
        listRepTypesProc (Queryable[Callable[..., Any]]?): Set or query the procedure that provides the representation type list which  
                an assembly type supports.  This procedure takes no argument, and  
                returns a string array of representation types that represents the full set  
                of representation types this assembly type can create.  The assembly type  
                for which this procedure applies will be the default type, unless the type  
                flag is used to specify an explicit assembly type.  
                Properties: query, edit
        listRepresentations (bool?): Query the created representations list for a specific assembly.  The -repType  
                flag can be used to filter the list and return representations for a  
                single representation type.  If the -repType flag is not used, all created  
                representations will be returned.  
                Properties: query
        listTypes (bool?): Query the supported assembly types.  
                Properties: query
        name (str?): Specify the name of the assembly when creating it.  
                Properties: create
        newRepLabel (str?): Specify the representation label to set on representation label edit.  
                Properties: edit
        postCreateUIProc (Queryable[Callable[..., Any]]?): Set or query the UI post-creation procedure for a given assembly type.  
                This procedure will be invoked by Maya immediately after an assembly of the  
                specified type is created from the UI, but not through scripting.  It can be  
                used to invoke a dialog, to obtain and set initial parameters on a  
                newly-created assembly.  The assembly type will be the default type, unless  
                the -type flag is used to specify an explicit assembly type.  
                Properties: query, edit
        proc (Callable[..., Any]?): Specify the procedure when setting the representation UI post- or  
                pre-creation procedure, for a given assembly type.  The assembly  
                type will be the default type, unless the -type flag is used to specify  
                an explicit assembly type.  
                Properties: edit
        renameRepresentation (str?): Renames the representation that is the argument to this flag.  The  
                repName flag must be used to provide the new name.  
                Properties: edit
        repLabel (str?): Query or edit the label of the representation that is the argument to this  
                flag, for a given assembly.  In both query and edit modes, the -repLabel flag  
                specifies the name of the representation.  In edit mode, the -newRepLabel flag  
                must be used to specify the new representation label.  
                			In query mode, this flag needs a value.  
                Properties: query, edit
        repName (str?): Specify the representation name to set on representation creation or rename.  
                This flag is optional with the createRepresentation flag: if omitted, the  
                assembly will name the representation.  It is mandatory with the  
                renameRepresentation flag.  
                Properties: edit
        repNamespace (Queryable[str]?): Query the representation namespace of this assembly node.  
                The value returned is used by Maya for creating the namespace where nodes created  
                by the activation of a representation will be added. If a name clash occurs when the  
                namespace is added to its parent namespace, Maya will update repNamespace with the new  
                name.  
                Two namespaces are involved when dealing with an assembly node: the namespace of the  
                assembly node itself (which this flag does not affect or query), and the namespace  
                of its representations. The representation namespace is a child of its assembly node's  
                namespace. The assembly node's namespace is set by its containing assembly, if it  
                is nested, or by the top-level file. Either the assembly node's namespace, or the  
                representation namespace, or both, can be the empty string.  
                It should be noted that if the assembly node is nested, the assembly  
                node's namespace will be (by virtue of its nesting) the  
                representation namespace of its containing assembly.  
                Properties: query
        repPostCreateUIProc (str?): Set or query the UI post-creation procedure for a specific representation type,  
                and for a specific assembly type.  This procedure takes two arguments, the  
                first the DAG path to the assembly, and the second the name of the  
                representation.  It returns no value.  It will be invoked by Maya  
                immediately after a representation of the specified type is created  
                from the UI, but not through scripting.  It can be used to invoke a  
                dialog, to obtain and set initial parameters on a newly-created  
                representation.  The representation type is the argument of this flag.  
                The -proc flag must be used to specify the procedure name.  The  
                assembly type will be the default type, unless the -type flag is used  
                to specify an explicit assembly type.  
                			In query mode, this flag needs a value.  
                Properties: query, edit
        repPreCreateUIProc (str?): Set or query the UI pre-creation procedure for a specific representation type,  
                and for a specific assembly type.  This procedure takes no argument, and  
                returns a string that is passed as an argument to the -input flag  
                when Maya invokes the assembly command with the -createRepresentation flag.  
                The representation pre-creation procedure is invoked by Maya  
                immediately before creating a representation of the specified type from the  
                UI, but not through scripting.  It can be used to invoke a dialog, to obtain  
                the creation argument for a new representation.  The representation type is  
                the argument of this flag.  The -proc flag must be used to specify the  
                procedure name.  The assembly type will be the default type, unless the  
                -type flag is used to specify an explicit assembly type.  
                			In query mode, this flag needs a value.  
                Properties: query, edit
        repType (str?): Specify a representation type to use as a filter for the -listRepresentations  
                query.  The representation type is the argument to this flag.  
                			In query mode, this flag needs a value.  
                Properties: query
        repTypeLabel (str?): Query the label of the specific representation type.  
                			In query mode, this flag needs a value.  
                Properties: query
        repTypeLabelProc (Queryable[Callable[..., Any]]?): Set or query the procedure that provides the representation type label,  
                for a given assembly type.  The procedure takes the representation type as  
                its sole argument, and returns a localized representation type label.  
                The assembly type for which this procedure applies will be the  
                default type, unless the -type flag is used to specify an explicit  
                assembly type.  
                Properties: query, edit
        type (str?): Set or query properties for the specified registered assembly type.  
                			In query mode, this flag needs a value.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

