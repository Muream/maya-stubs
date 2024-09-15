from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def translator(arg0: str = ..., /, *, query: bool = ..., defaultFileRule: bool = ..., defaultOptions: Queryable[str] = ..., extension: bool = ..., fileCompression: Queryable[str] = ..., filter: bool = ..., findTranslator: Tuple[str, int] = ..., list: bool = ..., loaded: bool = ..., objectType: bool = ..., optionsScript: bool = ..., readSupport: bool = ..., writeSupport: bool = ...) -> Union[bool, str]:
    """Set or query parameters associated with the file translators specified
    in as the argument.
    Args:
        defaultFileRule (bool?): Returns the default file rule value, can return "" as well  
                Properties: query
        defaultOptions (Queryable[str]?): Return/set a string of default options used by this translator.  
                Properties: query
        extension (bool?): Returns the default file extension for this translator.  
                Properties: query
        fileCompression (Queryable[str]?): Specifies the compression action to take when a file is saved.  
                Possible values are "compressed", "uncompressed" "asCompressed".  
                Properties: query
        filter (bool?): Returns the filter string used for this translator.  
                Properties: query
        findTranslator (Tuple[str, int]?): Returns the name of the translator that can handle the given file.  
                String argument is a file path.  
                Int argument is read and write attributes.  
                0. A translator that can read  
                1. A translator that can write  
                2. A translator that can read and write  
                Properties: create
        list (bool?): Return a string array of all the translators that are loaded.  
                Properties: query
        loaded (bool?): Returns true if the given translator is currently loaded.  
                Properties: query
        objectType (bool?): This flag is obsolete. This will now return the same results as  
                defaultFileRule going forward.  
                Properties: query
        optionsScript (bool?): Query the name of the options script to use to post the user  
                options UI. When this script is invoked it will expect the name of the  
                parent layout in which the options will be displayed as well as the name  
                of the callback to be invoked once the apply button has been depressed  
                in the options area.  
                Properties: query
        readSupport (bool?): Returns true if this translator supports read operations.  
                Properties: query
        writeSupport (bool?): Returns true if this translator supports write operations.  
                Properties: query

    Returns:
        bool: or string array depending upon which flags are specified.

    Example:
    """

