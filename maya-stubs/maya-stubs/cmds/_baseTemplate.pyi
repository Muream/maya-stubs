from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def baseTemplate(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., exists: bool = ..., fileName: Queryable[str] = ..., force: bool = ..., load: bool = ..., matchFile: str = ..., silent: bool = ..., unload: bool = ..., viewList: Queryable[str] = ...) -> Union[bool, str]:
    """This is the class for the commands that edit and/or query templates.base, template
    Args:
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

