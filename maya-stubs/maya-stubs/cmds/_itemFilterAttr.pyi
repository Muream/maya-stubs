from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def itemFilterAttr(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., byName: Queryable[str] = ..., byNameString: Queryable[Multiuse[str]] = ..., byScript: Queryable[str] = ..., classification: Queryable[str] = ..., dynamic: bool = ..., exists: bool = ..., hasCurve: bool = ..., hasDrivenKey: bool = ..., hasExpression: bool = ..., hidden: bool = ..., intersect: Queryable[Tuple[str, str]] = ..., keyable: bool = ..., listBuiltInFilters: bool = ..., listOtherFilters: bool = ..., listUserFilters: bool = ..., negate: bool = ..., parent: str = ..., published: bool = ..., readable: bool = ..., scaleRotateTranslate: bool = ..., secondScript: Queryable[str] = ..., text: Queryable[str] = ..., union: Queryable[Tuple[str, str]] = ..., writable: bool = ...) -> Union[str, List[str], Multiuse[str], bool, Tuple[str, str]]:
    """This command creates a named itemFilterAttr object.  This object
    can be attached to editors, in order to filter the attributes
    going through them.
    Using union and intersection filters, complex composite filters can
    be created.
    Args:
        byName (Queryable[str]?): The filter will only pass items whose names match the given regular  
                expression string.  This string can contain the special  
                characters * and ?.  '?' matches any one character, and '*'  
                matches any substring.  
                This flag cannot be used in conjunction with the -byScript or -secondScript flags.  
                Properties: create, query, edit
        byNameString (Queryable[Multiuse[str]]?): The filter will only pass items whose names match the given string.  
                This is a multi-use flag which allows the user to specify several strings.  
                The filter will pass items that match any of the strings.  
                This flag cannot be used in conjunction with the -byScript or -secondScript flags.  
                Properties: create, query, edit, multiuse
        byScript (Queryable[str]?): The filter will run a MEL script named by the given string on each  
                attribute name.  Attributes will pass the filter if the script  
                returns a non-zero value.  
                The script name string must be the name of a proc whose signature  
                is:  
                global proc int procName( string $nodeName string $attrName )  
                This flag cannot be used in conjunction with the -byName or -byNameString flags.  
                Properties: create, query, edit
        classification (Queryable[str]?): Indicates whether the filter is a built-in or user filter.  
                The string argument must be either "builtIn" or "user".  
                The "other" filter classification is deprecated. Use "user"  
                instead.  
              
                Filters created by Maya should be classified as "builtIn".  
                Filters created by plugins or user scripts should be classified  
                as "user".  
              
                Filters will not be deleted by a file new. Filter nodes will  
                be hidden from the UI (ex: Attribute Editor, Hypergraph etc) and  
                will not be accessible from the command-line.  
                Properties: create, query, edit
        dynamic (bool?): The filter will only pass dynamic attributes  
                Properties: create, query, edit
        exists (bool?): The filter will only pass attributs that exist  
                Properties: create, query, edit
        hasCurve (bool?): The filter will only pass attributes that are driven by animation  
                curves.  
                Properties: create, query, edit
        hasDrivenKey (bool?): The filter will only pass attributes that are driven by driven keys  
                Properties: create, query, edit
        hasExpression (bool?): The filter will only pass attributes that are driven by expressions  
                Properties: create, query, edit
        hidden (bool?): The filter will only pass attributes that are hidden to the user  
                Properties: create, query, edit
        intersect (Queryable[Tuple[str, str]]?): The filter will consist of the intersection of two other filters,  
                whose names are the given strings.  
                Attributes will pass this filter if and only if they pass both of  
                the contained filters.  
                Properties: create, query, edit
        keyable (bool?): The filter will only pass attributes that are keyable  
                Properties: create, query, edit
        listBuiltInFilters (bool?): Returns an array of all attribute filters with classification "builtIn".  
                Properties: query
        listOtherFilters (bool?): The "other" classification has been deprecated. Use "user" instead.  
                Returns an array of all attribute filters with classification "other".  
                Properties: query
        listUserFilters (bool?): Returns an array of all attribute filters with classification "user".  
                Properties: query
        negate (bool?): This flag can be used to cause the filter to invert itself,  
                and reverse what passes and what fails.  
                Properties: create, query, edit
        parent (str?): This flag is no longer supported.
        published (bool?): The filter will only pass attributes that are published on the container.  
                Properties: create, query, edit
        readable (bool?): The filter will only pass attributes that are readable (outputs)  
                Properties: create, query, edit
        scaleRotateTranslate (bool?): The filter will show only SRT attributes: scale, rotate, translate and  
                their children  
                Properties: create, query, edit
        secondScript (Queryable[str]?): Can be used in conjunction with the -bs flag.  The second  
                script is for filtering whole lists at once, rather than  
                individually.  Its signature must be:  
                global proc string[] procName( string[] $nodeName string[] $attrName )  
                It should take in a list of attributes, and return a filtered list  
                of attributes.  
                This flag cannot be used in conjunction with the -byName or -byNameString flags.  
                Properties: create, query, edit
        text (Queryable[str]?): Defines an annotation string to be stored with the filter  
                Properties: create, query, edit
        union (Queryable[Tuple[str, str]]?): The filter will consist of the union of two other filters, whose  
                names are the given strings.  
                Attributes will pass this filter if they pass at least one of the  
                contained filters.  
                Properties: create, query, edit
        writable (bool?): The filter will only pass attributes that are writable (inputs)  
                Properties: create, query, edit

    Returns:
        str: Single command result
        List[str]: Multiple command result

    Example:
    """

