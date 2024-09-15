from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def containerTemplate(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., addBindingSet: str = ..., addNames: bool = ..., addView: str = ..., allKeyable: bool = ..., attribute: Multiuse[str] = ..., attributeList: Queryable[str] = ..., baseName: Queryable[str] = ..., bindingSetList: Queryable[str] = ..., childAnchor: bool = ..., delete: bool = ..., expandCompounds: bool = ..., fromContainer: str = ..., fromSelection: bool = ..., layoutMode: int = ..., matchName: str = ..., parentAnchor: bool = ..., publishedNodeList: Queryable[str] = ..., removeBindingSet: str = ..., removeView: str = ..., rootTransform: bool = ..., save: bool = ..., searchPath: Queryable[str] = ..., templateList: Queryable[str] = ..., updateBindingSet: str = ..., useHierarchy: bool = ..., exists: bool = ..., fileName: Queryable[str] = ..., force: bool = ..., load: bool = ..., matchFile: str = ..., silent: bool = ..., unload: bool = ..., viewList: Queryable[str] = ...) -> Union[bool, str]:
    """A container template is a description of a container's published interface.
    This command provides the ability to create and save a template file for a
    container or load an existing template file.  Once a template exists,
    the user can query the template information.container, template
    Args:
        addBindingSet (str?): This argument is used to add a new binding set with the given name to a template.  
                A default binding set will be created. If the binding set already exists, the  
                force flag must be used to replace the existing binding set.  
                When used with the fromContainer option, default bindings will be entered based  
                on the current bindings of the designated container.  
                When used without a reference container, the binding set will be made with  
                placeholder entries.  
                The template must be saved before the new binding set is permanently stored with  
                the template file.  
                Properties: create, edit
        addNames (bool?): In edit mode, when used with the fromContainer flag, any published name on the  
                container not present as an attribute on the template will be added to the  
                template.  
                Properties: edit
        addView (str?): This argument is used to add a new view with the given name to a template.  
                By default a view containing a flat list of all template attributes  
                will be created.  The layoutMode flag provides more layout options.  
                The template must be saved before the new view is permanently stored with  
                the template file.  
                Properties: create, edit
        allKeyable (bool?): Used when the fromSelection flag is true and fromContainer is false. If true we will use  
                all keyable attributes to define the template or the view, if false we use the attributes  
                passed in with the attribute flag.  
                Properties: create, edit
        attribute (Multiuse[str]?): If fromSelection is true and allKeyable is false, this  
                attribute name will be used to create an attribute item in the template file.  
                Properties: create, edit, multiuse
        attributeList (Queryable[str]?): Used in query mode, returns a list of attributes contained in the  
                template definition.  
                Properties: create, query, edit
        baseName (Queryable[str]?): Used in query mode, returns the base name of the template.  
                The basename is the template name with any package qualifiers stripped off.  
                Properties: create, query
        bindingSetList (Queryable[str]?): Used in query mode, returns a list of all binding sets defined on the template.  
                Properties: create, query
        childAnchor (bool?): This flag can be optionally specified when querying the publishedNodeList.  
                The resulting list will contain only childAnchor published nodes.  
                Properties: create, query
        delete (bool?): Delete the specified template and its file.  
                All objects that are associated with this template or contained in the  
                same template file will be deleted.  
                To simply unload a template without permanently deleting its file,  
                use unload instead.  
                Properties: create
        expandCompounds (bool?): This argument is used to determine how compound parent attributes  
                and their children will be added to generated views when both are published  
                to the container.  
                When true, the compound parent and all compound child attributes published to the  
                container will be included in the view.  
                When false, only the parent attribute is included in the view.  
                Note: if only the child attributes are published and not the parent, the children  
                will be included in the view, this flag is only used in the situation where both  
                parent and child attributes are published to the container.  
                The default value is false.  
                Properties: create, edit
        fromContainer (str?): This argument is used in create or edit mode to specify a container node  
                to be used for generating the template contents.  
                In template creation mode, the template definition will be created  
                based on the list of published attributes in the specified container.  
                In edit mode, when used with the addNames flag or with no other flag, any  
                published name on the container not present as an attribute  
                on the template will be added to the template.  
                This flag is also used in conjunction with flags such as addView.  
                Properties: create
        fromSelection (bool?): If true, we will use the active selection list to create the template or the view.  
                If allKeyable is also true then we will create the template from all keyable  
                attributes in the selection, otherwise we will create the template using the  
                attributes specified with the attribute flag.  
                Properties: create, edit
        layoutMode (int?): This argument is used to specify the layout mode when creating a view.  
                Values correspond as follows:  
                0. layout in flat list (default when not creating view from container)  
                1. layout grouped by node (default if creating view from container)  
                The fromContainer or fromSelection argument is required to provide the  
                reference container or selection for layout modes that require node  
                information.  Note that views can only refer to defined template attributes.  
                This means that when using the fromContainer or from Selection flag to  
                add a view to an existing template, only attributes that are defined on  
                both the template and the container or the current selection will be  
                included in the view (i.e. published attributes on the container that  
                are not defined in the template will be ignored).  
                Properties: create
        matchName (str?): Used in query mode in conjunction with other flags this flag specifies  
                an optional template name that is to be matched as part of the query operation.  
                The base template name is used for matching, any template with the same  
                basename will be matched even across different packages.  
                			In query mode, this flag needs a value.  
                Properties: query
        parentAnchor (bool?): This flag can be optionally specified when querying the publishedNodeList.  
                The resulting list will contain only parentAnchor published nodes.  
                Properties: create, query
        publishedNodeList (Queryable[str]?): Used in query mode, returns a list of published nodes contained in the  
                template definition.  
                By default all published nodes on the template will be returned.  
                The list of published nodes can be limited to only include certain types of  
                published nodes using one of the childAnchor, parentAnchor or rootTransform flags.  
                If an optional flag is are specified, only nodes of the specified type  
                will be returned.  
                Properties: create, query, edit
        removeBindingSet (str?): This argument is used to remove the named binding set from the template.  
                The template must be saved before the binding set is permanently removed from  
                the template file.  
                Properties: create, edit
        removeView (str?): This argument is used to remove the named view from the template.  
                The template must be saved before the view is permanently removed from  
                the template file.  
                Properties: create, edit
        rootTransform (bool?): This flag can be optionally specified when querying the publishedNodeList.  
                The resulting list will contain only rootTransform published nodes.  
                Properties: create, query
        save (bool?): Save the specified template to a file.  
                If a filename is specified for the template, the entire file  
                (and all templates associated with it) will be saved.  
                If no file name is specified, a default filename will be assumed,  
                based on the template name.  
                Properties: create
        searchPath (Queryable[str]?): The template searchPath is an ordered list of all locations that are being  
                searched to locate template files (first location searched to last location  
                searched).  
                The template search path setting is stored in the current workspace  
                and can also be set and queried as the file rule entry for 'templates'  
                (see the workspace command for more information).  
                In edit mode, this flag allows the search path setting to be customized.  
                When setting the search path value, the list should conform to a path list format  
                expected on the current platform.  This means that paths should be  
                separated by a semicolon (;) on Windows and a colon (:) on Linux and MacOSX.  
                Environment variables can also be used.  
                Additional built-in paths may be added automatically by maya to the customized  
                settings.  
                In query mode, this flag returns the current contents of the search path;  
                all paths, both customized and built-in, will be included in the query return  
                value.  
                Properties: query, edit
        templateList (Queryable[str]?): Used in query mode, returns a list of all loaded templates.  
                This query can be used with optional matchFile and matchName flags.  
                When used with the matchFile flag, the list of templates will be restricted  
                to those associated with the specified file.  When used with the matchName  
                flag, the list of templates will be restricted to those matching the specified  
                template name.  
                Properties: query
        updateBindingSet (str?): This argument is used to update an existing binding set with new bindings.  
                When used with the fromContainer argument binding set entries with be replaced  
                or merged in the binding set based on the bindings of the designated container.  
                If the force flag is used, existing entries in the binding set are replaced  
                with new values.  
                When force is not used, only new entries are merged into the binding set,  
                any existing entries will be left as-is.  
                When used without a reference container, the binding set will be updated  
                with placeholder entries.  
                The template must be saved before the new binding set is permanently stored with  
                the template file.  
                Properties: create, edit
        useHierarchy (bool?): If true, and the fromSelection flag is set, the selection list will expand  
                to include it's hierarchy also.  
                Properties: create, edit
        exists (bool?): Returns true or false depending upon whether the specified template exists.  
                When used with the matchFile argument, the query will return true if the  
                template exists and the filename it was loaded from matches the filename  
                given.  
                Properties: query
        fileName (Queryable[str]?): Specifies the filename associated with the template.  This argument can be  
                used in conjunction with load, save or query modes. If no filename is  
                associated with a template, a default file name based on the template  
                name will be used.  It is recommended but not required that the  
                filename and template name correspond.  
                Properties: create, query
        force (bool?): This flag is used with some actions to allow them to proceed with an  
                overwrite or destructive operation.  
                When used with load, it will allow an existing template to be reloaded  
                from a file.  When used in create mode, it will allow an existing template  
                to be recreated (for example when using fromContainer argument to  
                regenerate a template).  
                Properties: create
        load (bool?): Load an existing template from a file.  
                If a filename is specified for the template, the entire file  
                (and all templates in it) will be loaded.  
                If no file is specified, a default filename will be assumed,  
                based on the template name.
        matchFile (str?): Used in query mode in conjunction with other flags this flag specifies  
                an optional file name that is to be matched as part of the query operation.  
                			In query mode, this flag needs a value.  
                Properties: query
        silent (bool?): Silent mode will suppress any error or warning messages that would normally be  
                reported from the command execution.  The return values are unaffected.  
                Properties: create, query, edit
        unload (bool?): Unload the specified template.  This action will not delete the  
                associated template file if one exists, it merely removes the template  
                definition from the current session.  
                Properties: create
        viewList (Queryable[str]?): Used in query mode, returns a list of all views defined on the template.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

