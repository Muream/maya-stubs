from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def runTimeCommand(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., addKeyword: Multiuse[str] = ..., addTag: Multiuse[str] = ..., annotation: Queryable[str] = ..., category: Queryable[str] = ..., categoryArray: bool = ..., command: Queryable[Callable[..., Any]] = ..., commandArray: bool = ..., commandLanguage: Queryable[str] = ..., default: bool = ..., defaultCommandArray: bool = ..., delete: bool = ..., exists: bool = ..., helpUrl: Queryable[str] = ..., hotkeyCtx: Queryable[str] = ..., image: Queryable[str] = ..., keywords: Queryable[str] = ..., label: Queryable[str] = ..., longAnnotation: Queryable[str] = ..., numberOfCommands: bool = ..., numberOfDefaultCommands: bool = ..., numberOfUserCommands: bool = ..., plugin: Queryable[str] = ..., save: bool = ..., showInHotkeyEditor: bool = ..., tags: Queryable[str] = ..., userCommandArray: bool = ...) -> Union[str, bool, Callable[..., Any]]:
    """Create a MEL command given the specified name. Once the command is created
    you can invoke it like any other MEL command.  When the command is invoked
    it will execute the string attached to theflag.Note that the resulting command takes no arguments, has no flags and
    may not be queried or edited.The command name you provide must be unique. The name itself must
    begin with an alphabetic character or underscore followed by
    alphanumeric characters or underscores.If you create your run time commands in a script which is automatically
    sourced at startup then set theflag to true.  This
    will prevent the application from attempting to save these commands.
    Args:
        addKeyword (Multiuse[str]?): Append one keyword to the keyboard list, which is used by the Search user interface  
                Properties: create, edit, multiuse
        addTag (Multiuse[str]?): Append one keyword to the tag list, which is used by the Search user interface  
                Properties: create, edit, multiuse
        annotation (Queryable[str]?): Description of the command.  
                Properties: create, query, edit
        category (Queryable[str]?): Category for the command.  
                Properties: create, query, edit
        categoryArray (bool?): Return all the run time command categories.  
                Properties: query
        command (Queryable[Callable[..., Any]]?): Command to be executed when runTimeCommand is invoked.  
                Properties: create, query, edit
        commandArray (bool?): Returns an string array containing the names of all the run  
                time commands.  
                Properties: query
        commandLanguage (Queryable[str]?): In edit or create mode, this flag allows the caller to choose a scripting  
                language for a command passed to the "-command" flag.  If this flag is not  
                specified, then the callback will be assumed to be in the language from which  
                the runTimeCommand command was called.  In query mode, the language for this  
                runTimeCommand is returned.  The possible values are "mel" or "python".  
                Properties: create, query, edit
        default (bool?): Indicate that this run time command is a default command.  
                Default run time commands will not be saved to preferences.  
                Properties: create, query
        defaultCommandArray (bool?): Returns an string array containing the names of all the  
                default run time commands.  
                Properties: query
        delete (bool?): Delete the specified user run time command.  
                Properties: edit
        exists (bool?): Returns true|false depending upon whether the specified object  
                exists. Other flags are ignored.  
                Properties: create
        helpUrl (Queryable[str]?): Custom URL for the online documentation of this command. Used in the Search user interface.  
                Properties: create, query, edit
        hotkeyCtx (Queryable[str]?): hotkey Context for the command.  
                Properties: create, query, edit
        image (Queryable[str]?): Image filename for the command.  
                Properties: create, query, edit
        keywords (Queryable[str]?): Keywords for the command. Used for searching for commands in the Search user interface.  
                When multiple keywords, use ; as a separator. (Example: "keyword1;keyword2")  
                Properties: create, query, edit
        label (Queryable[str]?): Label for the command.  
                Properties: create, query, edit
        longAnnotation (Queryable[str]?): Extensive, multi-line description of the command.  
                This will show up in the Search user interface's 'more info' page in addition to the annotation.  
                Properties: create, query, edit
        numberOfCommands (bool?): Return the number of run time commands.  
                Properties: query
        numberOfDefaultCommands (bool?): Return the number of default run time commands.  
                Properties: query
        numberOfUserCommands (bool?): Return the number of user run time commands.  
                Properties: query
        plugin (Queryable[str]?): Name of the plugin this command requires to be loaded.  
                This flag wraps the script provided into a safety check and automatically loads the  
                plugin referenced on execution if it hasn't been loaded.  
                If the plugin fails to load, the command won't be executed.  
                Properties: create, query, edit
        save (bool?): Save all the user run time commands.  
                Properties: edit
        showInHotkeyEditor (bool?): Indicate that this run time command should be shown in the Hotkey Editor.  
                Default value is true.  
                Properties: create, query, edit
        tags (Queryable[str]?): Tags for the command. Used for grouping commands in the Search user interface.  
                When more than one tag, use ; as a separator. (Example: "tag1;tag2")  
                Properties: create, query, edit
        userCommandArray (bool?): Returns an string array containing the names of all the  
                user run time commands.  
                Properties: query

    Returns:
        str: The name of the command on.

    Example:
    """

