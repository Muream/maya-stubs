from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def itemFilter(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., byBin: Queryable[Multiuse[str]] = ..., byName: Queryable[str] = ..., byScript: Queryable[str] = ..., byType: Queryable[Multiuse[str]] = ..., category: Queryable[Multiuse[str]] = ..., classification: Queryable[str] = ..., clearByBin: bool = ..., clearByType: bool = ..., difference: Queryable[Tuple[str, str]] = ..., exists: bool = ..., intersect: Queryable[Tuple[str, str]] = ..., listBuiltInFilters: bool = ..., listOtherFilters: bool = ..., listUserFilters: bool = ..., negate: bool = ..., parent: Queryable[str] = ..., pythonModule: Queryable[str] = ..., secondScript: Queryable[str] = ..., text: Queryable[str] = ..., union: Queryable[Tuple[str, str]] = ..., uniqueNodeNames: bool = ...) -> Union[str, List[str], Multiuse[str], Tuple[str, str], bool]:
    """This command creates a named itemFilter object.  This object
    can be attached to selectionConnection objects, or to editors,
    in order to filter the item lists going through them.  Using
    union, intersection and difference filters, complex composite
    filters can be created.
    Args:
        byBin (Queryable[Multiuse[str]]?): The filter will only pass items whose bin list  
                contains the given string as a bin name.  
                This is a multi-use flag.  
                If more than one occurance of this flag is used in a single  
                command, the filter will accept a node if it matches at least  
                one of the given bins (in other words, a union or logical or  
                of all given bins.  
                Properties: create, query, edit, multiuse
        byName (Queryable[str]?): The filter will only pass items whose names match the given regular  
                expression string.  This string can contain the special  
                characters * and ?.  '?' matches any one character, and '*'  
                matches any substring.  
                Properties: create, query, edit
        byScript (Queryable[str]?): The filter will run a MEL script named by the given string on each item name.  Items  
                will pass the filter if the script returns a non-zero value.  
                The script name string must be the name of a proc whose signature  
                is:  
                global proc int procName( string $name ) or  
                def procName(*args, **keywordArgs) if -pym/pythonModule is specified.  
                Note that if -secondScript is also used, it will always take precedence.  
                Properties: create, query, edit
        byType (Queryable[Multiuse[str]]?): The filter will only pass items whose typeName matches the  
                given string.  The typeName of an object can be found using  
                the nodeType command.  This is a multi-use flag.  
                If more than one occurance of this flag is used in a single  
                command, the filter will accept a node if it matches at least  
                one of the given types (in other words, a union or logical or  
                of all given types.  
                Properties: create, query, edit, multiuse
        category (Queryable[Multiuse[str]]?): A string for categorizing the filter.  
                Properties: create, query, edit, multiuse
        classification (Queryable[str]?): Indicates whether the filter is a built-in or user filter.  
                The string argument must be either "builtIn" or "user".  
                The "other" classification is deprecated. Use "user" instead.  
              
                Filters will not be deleted by a file new, and filter nodes will  
                be hidden from the UI (ex: Attribute Editor, Hypergraph etc) and  
                will not be accessible from the command-line.  
                Properties: create, query, edit
        clearByBin (bool?): This flag will clear any existing bins associated with this filter.  
                Properties: create, edit
        clearByType (bool?): This flag will clear any existing typeNames associated with this filter.  
                Properties: create, edit
        difference (Queryable[Tuple[str, str]]?): The filter will consist of the set difference of two other filters,  
                whose names are the given strings.  
                Items will pass this filter if and only if they pass the first filter but  
                not the second filter.  
                Properties: create, query, edit
        exists (bool?): Returns true|false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
        intersect (Queryable[Tuple[str, str]]?): The filter will consist of the intersection of two other filters,  
                whose names are the given strings.  
                Items will pass this filter if and only if they pass both of  
                the contained filters.  
                Properties: create, query, edit
        listBuiltInFilters (bool?): Returns an array of all item filters with classification "builtIn".  
                Properties: query
        listOtherFilters (bool?): The "other" classification is deprecated. Use "user" instead.  
                Returns an array of all item filters with classification "other".  
                Properties: query
        listUserFilters (bool?): Returns an array of all item filters with classification "user".  
                Properties: query
        negate (bool?): This flag can be used to cause the filter to invert itself,  
                and reverse what passes and what fails.  
                Properties: create, query, edit
        parent (Queryable[str]?): Optional.  If specified, the filter's life-span is linked to  
                that of the parent.  When the parent goes out of scope, so  
                does the filter.  If not specified, the filter will exist  
                until explicitly deleted.  
                Properties: create, query, edit
        pythonModule (Queryable[str]?): Treat -bs/byScript and -ss/secondScript as Python functions located in the specified module.  
                Properties: create, query, edit
        secondScript (Queryable[str]?): Cannot be used in conjunction with the -bs flag.  The second  
                script is for filtering whole lists at once, rather than  
                individually.  Its signature must be:  
                global proc string[] procName( string[] $name ) or  
                def procName(*args, **keywordArgs) if -pym/pythonModule is specified.  
                It should take in a list of items, and return a filtered list  
                of items.  
                Properties: create, query, edit
        text (Queryable[str]?): Defines an annotation string to be stored with the filter  
                Properties: create, query, edit
        union (Queryable[Tuple[str, str]]?): The filter will consist of the union of two other filters, whose  
                names are the given strings.  
                Items will pass this filter if they pass at least one of the  
                contained filters.  
                Properties: create, query, edit
        uniqueNodeNames (bool?): Returns unique node names to script filters so there are no naming  
                conflicts.  
                Properties: create, query, edit

    Returns:
        str: Single command result
        List[str]: Multiple command result

    Example:
    """

