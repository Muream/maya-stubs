from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def character(*args: str, edit: bool = ..., query: bool = ..., addElement: str = ..., addOffsetObject: Queryable[str] = ..., anyMember: str = ..., characterPlug: bool = ..., clear: str = ..., empty: bool = ..., excludeDynamic: bool = ..., excludeRotate: bool = ..., excludeScale: bool = ..., excludeTranslate: bool = ..., excludeVisibility: bool = ..., flatten: str = ..., forceElement: str = ..., include: str = ..., intersection: Queryable[str] = ..., isIntersecting: Queryable[str] = ..., isMember: Queryable[str] = ..., library: bool = ..., memberIndex: Queryable[int] = ..., name: str = ..., noWarnings: bool = ..., nodesOnly: bool = ..., offsetNode: bool = ..., remove: str = ..., removeOffsetObject: str = ..., root: str = ..., scheduler: bool = ..., split: str = ..., subtract: Queryable[str] = ..., text: Queryable[str] = ..., union: Queryable[str] = ..., userAlias: Queryable[str] = ...) -> Union[str, List[str], bool, int]:
    """This command is used to manage the membership of a character.  Characters
    are a type of set that gathers together the attributes of a node or nodes
    that a user wishes to animate as a single entity.
    Args:
        addElement (str?): Adds the list of items to the given character.  If some of the  
                items cannot be added to the character because they are in another  
                character, the command will fail.  When another character is passed to  
                to -addElement, is is added as a sub character.  When a node is  
                passed in, it is expanded into its keyable attributes, which are  
                then added to the character.  
                Properties: edit
        addOffsetObject (Queryable[str]?): Indicates that the selected character member objects should be used when  
                calculating and applying offsets. The flag argument is used to specify the  
                character.  
                Properties: query, edit
        anyMember (str?): An operation which tests whether any of the given items  
                are members of the given set.  
                Properties: create
        characterPlug (bool?): Returns the plug on the character that corresponds to the  
                specified character member.  
                Properties: query
        clear (str?): An operation which removes all items from the given character.  
                Properties: edit
        empty (bool?): Indicates that the character to be created should be empty. (i.e.  
                it ignores any arguments identifying objects to be added to  
                the character.  
                Properties: create
        excludeDynamic (bool?): When creating the character, exclude dynamic attributes.  
                Properties: create
        excludeRotate (bool?): When creating the character, exclude rotate attributes from  
                transform-type nodes.  
                Properties: create
        excludeScale (bool?): When creating the character, exclude scale attributes from  
                transform-type nodes.  
                Properties: create
        excludeTranslate (bool?): When creating the character, exclude translate attributes from  
                transform-type nodes. For example, if your character contains  
                joints only, perhaps you only want to include rotations in the  
                character.  
                Properties: create
        excludeVisibility (bool?): When creating the character, exclude visibility attribute from  
                transform-type nodes.  
                Properties: create
        flatten (str?): An operation that flattens the structure of the given character. That is,  
                any characters contained by the given character will be replaced by its  
                members so that the character no longer contains other characters but contains  
                the other characters' members.  
                Properties: edit
        forceElement (str?): For use in edit mode only. Forces addition of the items  
                to the character. If the items are in another character which  
                is in the character partition, the items will be removed  
                from the other character in order to keep the characters in the  
                character partition mutually exclusive with respect to membership.  
                Properties: edit
        include (str?): Adds the list of items to the given character.  If some of the  
                items cannot be added to the character, a warning will be issued.  
                This is a less strict version of the -add/addElement operation.  
                Properties: edit
        intersection (Queryable[str]?): An operation that returns a list of items which are members of  
                all the character in the list.  In general, characters should be  
                mutually exclusive.  
                Properties: query
        isIntersecting (Queryable[str]?): An operation which tests whether or not the characters in the list have  
                common members.  In general, characters should be mutually exclusive, so  
                this should always return false.  
                Properties: query
        isMember (Queryable[str]?): An operation which tests whether or not all the given items  
                are members of the given character.  
                Properties: query
        library (bool?): Returns the clip library associated with this character, if there is one. A clip library will only exist if you have created clips on your character.  
                Properties: query
        memberIndex (Queryable[int]?): Returns the memberIndex of the specified character member if used after the query flag. Or if used before the query flag, returns the member that corresponds to the specified index.  
                Properties: query
        name (str?): Assigns string as the name for a new character. Valid for operations that  
                create a new character.  
                Properties: create
        noWarnings (bool?): Indicates that warning messages should not be reported such  
                as when trying to add an invalid item to a character. (used by UI)  
                Properties: create
        nodesOnly (bool?): This flag modifies the results of character membership queries.  
                When listing the attributes (e.g. sphere1.tx) contained in the  
                character, list only the nodes.  Each node will only be listed  
                once, even if more than one attribute or component of the node  
                exists in the character.  
                Properties: query
        offsetNode (bool?): Returns the name of the characterOffset node used to add offsets to the root of the character.  
                Properties: query
        remove (str?): Removes the list of items from the given character.  
                Properties: edit
        removeOffsetObject (str?): Indicates that the selected character offset objects should be removed  
                as offsets. The flag argument is used to specify the character.  
                Properties: edit
        root (str?): Specifies the transform node which will act as the root of the character being created.  
                This creates a characterOffset node in addition to the character node, which can be used to add offsets  
                to the character to change the direction of the character's animtion without inserting additional nodes  
                in its hierarchy.  
                Properties: create
        scheduler (bool?): Returns the scheduler associated with this character, if there is one. A scheduler will only exist if you have created clips on your character.  
                Properties: query
        split (str?): Produces a new set with the list of items and removes  
                each item in the list of items from the given set.  
                Properties: create
        subtract (Queryable[str]?): An operation between two characters which returns the members of the  
                first character that are not in the second character. In general,  
                characters should be mutually exclusive.  
                Properties: query
        text (Queryable[str]?): Defines an annotation string to be stored with the character.  
                Properties: create, query, edit
        union (Queryable[str]?): An operation that returns a list of all the members of all characters  
                listed.  
                Properties: query
        userAlias (Queryable[str]?): Returns the user defined alias for the given attribute on  
                the character or and empty string if there is not one.  Characters  
                automatically alias the attributes where character animation data  
                is stored.  A user alias will exist when the automatic aliases are  
                overridden using the aliasAttr command.  
                Properties: query

    Returns:
        str: For creation operations (name of the character that was created or edited)
        List[str]: For query operation (names of items in the character)
        bool: For isMember operation

    Example:
    """

