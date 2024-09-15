from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def colorManagementFileRules(*args: str, edit: bool = ..., query: bool = ..., addRule: str = ..., colorSpace: Queryable[str] = ..., colorSpaceDescription: str = ..., colorSpaceFamilies: str = ..., colorSpaceNames: bool = ..., down: str = ..., enabled: bool = ..., evaluate: str = ..., extension: Queryable[str] = ..., listRules: bool = ..., load: bool = ..., moveUp: str = ..., pattern: Queryable[str] = ..., remove: str = ..., restoreDefaults: bool = ..., save: bool = ...) -> Union[bool, str]:
    """This non-undoable action manages the list of rules that Maya uses to assign
    an initial input color space to dependency graph nodes that read in color
    information from a file.  Rules are structured in a chain of
    responsibility, from highest priority rule to lowest priority rule, each
    rule matching a file path pattern and extension.  If a rule matches a given
    file path, its color space is returned as the result of rules evaluation,
    and no further rule is considered.  The lowest priority rule will always
    return a match.
    Rules can be added, removed, and changed in priority in the list.  Each
    rule can have its file path pattern, extension, and color space changed.
    The rule list can be saved to user preferences, and loaded from user
    preferences.color, management
    Args:
        addRule (str?): Add a rule with the argument name to the list of rules, as the  
                highest-priority rule.  If this flag is used, the pattern, extension, and  
                colorSpace flags must be used as well, to specify the file rule pattern,  
                extension, and color space, respectively.  
                Properties: create
        colorSpace (Queryable[str]?): The input color space for the rule.  If the rule matches a file path, this  
                is the color space that is returned.  This color space must match an existing  
                color space in the input color space list.  
                Properties: create, query, edit
        colorSpaceDescription (str?): Returns the description for a specific color space.  
                			In query mode, this flag needs a value.  
                Properties: query
        colorSpaceFamilies (str?): Returns the list of families for a specific color space. Used to add submenus  
                when populating the color spaces UI popup of a rule.  
                			In query mode, this flag needs a value.  
                Properties: query
        colorSpaceNames (bool?): Returns the list of available color spaces. Used to populate the color  
                spaces UI popup of a rule.  
                Properties: query
        down (str?): Move the rule with the argument name down one position towards lower priority.  
                Properties: create
        enabled (bool?): Are the file rules enabled?  
                Properties: query
        evaluate (str?): Evaluates the list of rules and returns the input color space name that  
                corresponds to the argument file path.  
                Properties: create
        extension (Queryable[str]?): The file extension for the rule is case insensitive  
                Properties: create, query, edit
        listRules (bool?): Returns an array of rule name strings, in order, from lowest-priority (rule 0)  
                to highest-priority (last rule in array).  
                Properties: create
        load (bool?): Read the rules from Maya preferences.  Any existing rules are cleared.  
                Properties: create
        moveUp (str?): Move the rule with the argument name up one position towards higher priority.  
                Properties: create
        pattern (Queryable[str]?): The file path pattern for the rule.  This is the substring to match in the  
                file path, expressed as a glob pattern: for example, '*' matches all files.  
                For more information about glob pattern syntax, see  
                http://en.wikipedia.org/wiki/Glob_%28programming%29.  
                Properties: create, query, edit
        remove (str?): Remove the rule with the argument name from the list of rules.  
                Properties: create
        restoreDefaults (bool?): Restore the list of rules to the default ones only.  
                Properties: create
        save (bool?): Save the rules to Maya preferences.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

