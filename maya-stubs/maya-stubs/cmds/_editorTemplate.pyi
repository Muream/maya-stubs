from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def editorTemplate(*args: str, addAdskAssetControls: bool = ..., addComponents: bool = ..., addControl: Tuple[str, Callable[..., Any]] = ..., addDynamicControl: Tuple[str, Callable[..., Any]] = ..., addExtraControls: bool = ..., addSeparator: bool = ..., annotateFieldOnly: bool = ..., annotation: str = ..., beginLayout: str = ..., beginNoOptimize: bool = ..., beginScrollLayout: bool = ..., callCustom: Tuple[Callable[..., Any], Callable[..., Any]] = ..., collapse: bool = ..., debugMode: bool = ..., dimControl: Tuple[str, str, bool] = ..., endLayout: bool = ..., endNoOptimize: bool = ..., endScrollLayout: bool = ..., extraControlsLabel: str = ..., forceRebuild: bool = ..., interruptOptimize: bool = ..., label: str = ..., listExtraAttributes: str = ..., preventOverride: bool = ..., queryControl: Tuple[str, str] = ..., queryLabel: Tuple[str, str] = ..., queryName: Tuple[str, str] = ..., suppress: str = ...) -> str:
    """The editorTemplate command allows the user to specify the
    conceptual layout of an attribute editor and leave the details
    of exactly which UI elements are used in the final result to the
    automatic dialog generation mechanism.
    Args:
        addAdskAssetControls (bool?): Adds controls for dynamic attributes of adskMaterial nodes  
                and organizes them in a layout according to the XML ui  
                description specified in the asset library.  
                Properties: create
        addComponents (bool?): This flag will add a frameLayout with a channel box  
                which will display any selected components for the  
                object.  
                Properties: create
        addControl (Tuple[str, Callable[..., Any]]?): The first argument is the name of the attribute for which  
                you wish to add a control. You can assume that when the editor  
                is created from the template, an appropriate type of control  
                will be used.  
                The second string argument is optional, and can be used  
                to specify a command (or script) to be executed when the  
                attribute is changed.  
                Properties: create
        addDynamicControl (Tuple[str, Callable[..., Any]]?): As -addControl with the exception that the attribute  
                for which the control is to be created/attached is dynamic.  
                [Note: -addControl will also work for dynamic attributes,  
                but will not preserve their order in the attribute editor].  
                Properties: create
        addExtraControls (bool?): By default, if there are attributes of a node which you do  
                not -addControl or -suppress, then controls will be created  
                automatically and appended to the end of editor created from the  
                template. This flag allows you to specify a particular place  
                in the template for such controls to be automatically inserted.  
                If dynamic attributes have not already been addressed  
                with -addControl, they will also be placed here.  A frameLayout  
                will automatically be generated for you when you use this flag.  
                Properties: create
        addSeparator (bool?): Adds a separator to the template.  
                Properties: create
        annotateFieldOnly (bool?): This flag can only be used with the -annotation flag.  By  
                default, for any Attribute Editor controlGroups created by  
                the -addControl flag, the -annotation flag displays its  
                annotation string when the mouse hovers over any control  
                that is part (the label, the value field, etc.) of the  
                group.  Use this flag to limit display of the annotation to  
                only the value field of the controlGroup.  This flag is  
                ignored if the controlGroup has no value field (e.g., checkBoxGrp)  
                Properties: create
        annotation (str?): This flag can only be used with the -addControl or  
                the -addDynamicControl flags. The string will be used as  
                an annotation on the controls created in the attribute editor.  
                Properties: create
        beginLayout (str?): Begins a layout in the template with the title specified  
                by the string argument.  
                Items between this flag and    its corresponding -endLayout flag  
                will be contained within the layout. You can assume that when  
                the editor is created from the template, an appropriate type of  
                layout will be used. (frameLayout).  
                Properties: create
        beginNoOptimize (bool?): Specifies that the layout of items between this flag and its  
                corresponding -endNoOptimize flag is not to be optimized to  
                minimize space.  
                Properties: create
        beginScrollLayout (bool?): Begins a scrollLayout.  Items between this flag and its  
                corresponding -endScrollLayout flag will be contained within  
                the layout.  
                Properties: create
        callCustom (Tuple[Callable[..., Any], Callable[..., Any]]?): Specifies that at this point in the template when building the  
                dialog, the procedure specified by the first argument is to be  
                called to create some UI objects when a new node type is edited.  
                The procedure specified by the second argument is to be called if  
                an attribute editor already exists and another node of the same  
                type is now to be edited. The replacing procedure should connect  
                any controls created by the creating procedure to the equivalent  
                attributes in the new node. A list of zero or more attributes  
                specifies the attributes which the two procedures will involve.  
                The procedures should have the signature:  
              
                proc AEcustomNew(string attributeName1, string attributeName2)  
              
                The number of attributes specified in the call should correspond  
                to the number of attributes in the procedure signature.  
                Properties: create
        collapse (bool?): This flag is only valid when used in conjunction with  
                a -bl/beginLayout flag.  It is used to specify the initial  
                expand/collapse state of the layout.  A true value will cause the  
                layout to be collapsed upon creation, while a false value will  
                expand the layout.  The default is true (ie. collapsed).  
                Properties: create
        debugMode (bool?): Set debugging mode for the template  
                Properties: create
        dimControl (Tuple[str, str, bool]?): This flag is only useful AFTER a control has already been  
                created (using the -addControl flag).  The first argument  
                is the node name and the second is the attribute  
                whose control you wish to affect.  The third argument is a  
                boolean which specifies whether to dim (true) or undim (false)  
                the associated control.  
                Properties: create
        endLayout (bool?): Ends a layout in the template started by -beginLayout.  
                Properties: create
        endNoOptimize (bool?): Ends a set of non-optimized items.  
                Properties: create
        endScrollLayout (bool?): Ends a scrollLayout.  
                Properties: create
        extraControlsLabel (str?): By default the label is "Extra Attributes". Specify an  
                alternate label or an empty string to hide the label. This flag  
                must be used in conjuction with the -aec/addExtraControls flag.  
                Properties: create
        forceRebuild (bool?): Force a template to always destroy/create itself rather  
                than use the replace feature.  Both the default replace  
                behavior and force rebuild preserve the collapse/expand  
                status of all the layout sections.  
                Properties: create
        interruptOptimize (bool?): Enforces a division between two sets of items whose layouts  
                may be optimized.  
                Properties: create
        label (str?): This flag can only be used with the -addControl or  
                the -addDynamicControl flags.  And it must be specified FIRST.  
                The string will override the name of the attribute that  
                will be displayed in the attribute editor.  
                Properties: create
        listExtraAttributes (str?): List extra attributes.This flag is only useful AFTER a control  
                has already been created (using the -addControl flag). The  
                first argument is the node name.  
                Properties: create
        preventOverride (bool?): If true, this flag disallows overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create
        queryControl (Tuple[str, str]?): This flag is only useful AFTER a control has already been  
                created (using the -addControl flag).  The first argument is  
                the node name and the second is the attribute whose control  
                you wish to query.  Note that in most cases, using this  
                flag is identical to issuing a getAttr command, however, in  
                the case of textFields (e.g. for message attributes), the text  
                value currently being displayed will be returned, NOT the actual  
                attribute value.  
                Properties: create
        queryLabel (Tuple[str, str]?): This flag is only useful AFTER a control has already been  
                created (using the -addControl flag).  The first argument is  
                the node name and the second is the attribute whose control  
                label you wish to query.  In most cases this flag  
                returns the same value as the attribute's nice name,  
                but when a -label flag was present on the -addControl command that  
                created the control, -queryLabel will return that value instead  
                Properties: create
        queryName (Tuple[str, str]?): This flag is only useful AFTER a control has already been  
                created (using the -addControl flag).  The first argument is  
                the node name and the second is the attribute whose control name  
                you wish to query.  
                Properties: create
        suppress (str?): Prevent a control for the attribute specified by the  
                string argument from appearing in the editor created from the  
                template.  
                Properties: create

    Returns:
        str: For queryControl, the appropriate attribute type will be
            returned.
            string array
            For listExtraAttributes, extra attributes will be returned.

    Example:
    """

