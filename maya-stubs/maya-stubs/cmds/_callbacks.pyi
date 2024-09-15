from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def callbacks(*args: str, addCallback: Callable[..., Any] = ..., clearAllCallbacks: bool = ..., clearCallbacks: bool = ..., describeHooks: bool = ..., dumpCallbacks: bool = ..., executeCallbacks: bool = ..., hook: str = ..., listCallbacks: bool = ..., owner: str = ..., removeCallback: Callable[..., Any] = ...) -> List[str]:
    """This command allows you to add callbacks at key times during UI creation so
    that the Maya UI can be extended.
    The list of standard Maya hooks, as well as the arguments which will be passed
    to the callback based on the context are enumerated in thesection below.
    Custom hooks can also be added if third parties want to add UI extensibility to
    their plugins.ui, callback
    Args:
        addCallback (Callable[..., Any]?): Add a callback for the specified hook. The owner must also be specified  
                when adding callbacks.  
                Properties: create
        clearAllCallbacks (bool?): Clear all the callbacks for all hooks and owners. This is generally  
                only used during plugin development and testing as it affects all callbacks  
                registered by Maya and other third parties.  
                Properties: create
        clearCallbacks (bool?): Clear all the callbacks for the specified owner. If a hook is specified,  
                only the callbacks for that hook and owner will be cleared.  
                Properties: create
        describeHooks (bool?): List the standard Maya hooks. Below is a list of the hooks and their associated arguments  
                and return values. Custom hooks added by third parties are not listed.  
              
              
                hyperShadePanelBuildCreateMenu  
              
                This hook is called to add content to the Hypershade panel create menu. It will  
                be called after the standard Maya node entries have been created.  
              
                This callback does not have any arguments or return values. In order to preserve  
                the desired look in the Maya UI, these callbacks should add a menu item divider just  
                before returning using: menuItem -divider true.  
              
                hyperShadePanelBuildCreateSubMenu  
              
                This hook is called to get a classification string for the custom renderer  
                shading nodes, to prevent them from being listed with the standard Maya nodes.  
              
                This callback does not have any arguments.  
              
                returns: a classification string, such as rendernode/myrenderer  
              
              
                hyperShadePanelPluginChange  
              
                This hook is called when a plugin change event (loading / unloading) has occurred to inform Maya whether the  
                Hypershade panel needs to be rebuilt.  
              
                classification (string): classification string belonging to a plugin node,  
                    possibly from another plugin  
                changeType (string): either loadPlugin or unloadPlugin  
                returns: (int) non-zero if your plugin is responsible for nodes of this classification,  
                    and a Hypershade rebuild is required  
              
              
                createRenderNodeSelectNodeCategories  
              
                This hook is called when the Create Render Node dialog is being constructed, and allows  
                a third party to have their nodes selected by default. A flag of the form -allWithMyRendererUp  
                is the standard form, and the selection can be set up in the tree lister in the callback.  
              
                There is no return value for this callback.  
              
                flag (string): flag passed to the Create Render Node dialog command with the leading minus (-) removed  
                treeLister (string): the tree lister widget which should be affected  
              
              
                For example, your callback might look like:  
              
              
                global proc myRendererCreateRenderNodeSelectNodeCategoriesCallback(string $flag, string $treeLister){  
                    if($flag == "allWithMyRendererUp") {  
                        treeLister -e -selectPath "myrenderer" $treeLister;  
                    }  
                }  
              
              
                createRenderNodePluginChange  
              
                This hook is called when a plugin change event has occurred to decide if the  
                Create Render Node dialog needs to be closed.  
              
                classification (string): classification string belonging to a plugin node,  
                    possibly from another plugin  
                returns: (int) non-zero if your plugin is responsible for nodes of this classification,  
                    and the Create Render Node dialog needs to be closed  
              
              
                renderNodeClassification  
              
                This hook is called to get a classification string for the custom renderer  
                shading nodes.  This is used to determine if a given node type belongs to  
                a plugin renderer.  
              
                This callback does not have any arguments.  
              
                returns: a classification string, such as rendernode/myrenderer  
              
              
                createRenderNodeCommand  
              
                This hook is called to give plugin renderers the chance to register their own command for  
                creating their nodes from the render node treeLister and Node Editor. The callback should  
                determine from the classification of the node type in question if it is theirs, and if so,  
                return the appropriate command for creating new nodes of that type.  
              
              
                postCommand (string): command to be run after the create command  
                type (string): nodeType  
                returns: (string) MEL create command  
              
              
                buildRenderNodeTreeListerContent  
              
                This hook is called to give plugin renderers the chance to add their content to the render node  
                tree lister.  
              
              
                renderNodeTreeLister (string): the render node tree lister  
                postCommand (string): command to be run post-creation  
                filterString (string): a space delimited list of filters  
              
              
                AETemplateCustomContent  
              
                This hook is called to give plugins a chance to add content to the Attribute Editor for nodes which source AEdependNodeTemplate.  
              
              
                nodeName (string): the name of the node for which the Attribute Editor is being constructed  
              
              
                firstConnectedShader  
              
                This hook is called to determine the primary custom shader connected to the given Shading Engine.  
              
              
                nodeName (string): the name of the Shading Engine  
                returns (string): the name of the custom shader if applicable  
              
              
                allConnectedShaders  
              
                This hook is called to determine all the shaders connected to the given Shading Engine.  
              
              
                nodeName (string): the name of the Shading Engine  
                returns (string): a colon separated list of the connected custom shaders (shader1. shader2. shader3)  
              
              
                renderLayerPresetMenu  
              
                This hook is called to give plugins a chance to add presets to a renderLayer node.  
              
              
                nodeName (string): the name of the renderLayer node  
              
              
                addBakingMenuItems  
              
                This hook is called to give plugins a chance to add baking menu items to the global Render - Lighting/Shading menu.  
              
              
                menuItemAnchor (string): the name of the menuItem which the new baking menu items should be inserted after.   
              
              
                addVertexBakingMenuItems  
              
                This hook is called to give plugins a chance to add baking menu items to the global Polygon - Color menu.  
              
              
                addPrelightMenuItems  
              
                This hook is called to give plugins a chance to add pre-lighting menu items to the global Polygon - Color Set Editor menu.  
              
              
                addRMBBakingMenuItems  
              
                This hook is called to give plugins a chance to add baking menu items to the RMB menu.  
              
              
                objectName (string): the name of the object the right mouse button event occured on.  
              
              
                addMayaRenderingPreferences  
              
                This hook is called to give plugins a chance to add custom preferences to the Maya's Rendering Preferences section.  
              
              
                updateMayaRenderingPreferences  
              
                This hook is called to give plugins a chance to update custom preferences of the Maya's Rendering Preferences section.  
              
              
                addMayaMuscleMenuItems  
              
                This hook is called to give plugins a chance to add menu items to the Maya muscle Displace menu.  
              
              
                menuItemAnchor (string): the name of the menuItem which the new Maya muscle menu items should be inserted after.   
              
              
                addMayaMuscleShelfButtons  
              
                This hook is called to give plugins a chance to add items to the Maya muscle shelves.  
              
              
                addBackburnerRendererMenuItems  
              
                This hook is called to give plugins a chance to add items to Maya's Backburner list of available renderers. Note: The menuItem added must be named with the short name equivalent of the renderer. eg: The Maya software renderer adds a menuItem named 'sw'.  
              
              
                provideAETemplateForNodeType  
              
                This hook is called to give plugins a chance to provide a UI template for nodes which do not have a corresponding AE'nodeType'Template procedure.  
              
              
                nodeType (string): the type of the node for which the AE is being constructed.   
                returns (string): the name of a MEL command or procedure to use as the AETemplate for the requested node type.   
              
              
                AEnewMultiHandler  
              
                This hook is called to give plugins a chance to provide a UI creation handler for multi attributes.  
              
              
                nodeName (string): the name of the node for which the AE is being constructed.   
                atributeName (string): the name of the multi attribute.  
                uiName (string): the UI name of the attribute.  
                changedCommand (string): the MEL command or procedure to be executed when the value of the multi attribute is changed.  
                elementIndexString (string): a colon separated list of indices at which the elements of the multi attribute live.  
                returns (string): if the callback handled the attribute then it should return the full name of the topmost UI element that it created, otherwise it should return an empty string.  
              
              
                AEreplaceMultiHandler  
              
                This hook is called to give plugins a chance to provide an update handler for multi attributes.  
              
              
                layoutName (string): the well defined name of the Maya UI component which represents the multi attribute (.  
                nodeName (string): the name of the node for which the AE is being constructed.   
                atributeName (string): the name of the multi attribute.  
                changedCommand (string): the MEL command or procedure to be executed when the value of the multi attribute is changed.  
                elementIndexString (string): a colon separated list of indices at which the elements of the multi attribute live.  
                returns (int): Return 1 if the callback handled the multi attribute, Return 0 if Maya should provide its default handling.  
              
              
                AEnewAttributeHandler  
              
                This hook is called to give plugins a chance to provide a UI creation handler for attributes.  
              
              
                nodeName (string): the name of the node for which the AE is being constructed.   
                atributeName (string): the name of the attribute.  
                uiName (string): the UI name of the attribute.  
                changedCommand (string): the MEL command or procedure to be executed when the value of the attribute is changed.  
                returns (string): if the callback handled the attribute then it should return the full name of the topmost UI element that it created, otherwise it should return an empty string.  
              
              
                AEreplaceAttributeHandler  
              
                This hook is called to give plugins a chance to provide an update handler for attributes.  
              
              
                nodeName (string): the name of the node for which the AE is being constructed.   
                atributeName (string): the name of the attribute.  
                changedCommand (string): the MEL command or procedure to be executed when the value of the attribute is changed.  
                returns (int): Return 1 if the callback handled the attribute, Return 0 if Maya should provide its default handling.  
              
              
                provideClassificationStrings  
              
                This hook must be supplied by all third parties that add nodes to the 'shader/surface' classification namespace.  
              
              
                returns (string): a colon separated list representing the different plugin node classifications.  
              
              
                provideClassificationExclusionStrings  
              
                This hook is called to give plugins a chance to provide a list of classifications which should be filtered out from a nodeTreeLister category. For example a plugin might want to filter out nodes classified as both 'material' and 'legacy' out of the 'material' category.  
              
              
                classification (string): the classification the nodeTreeBuilder is inquiring about.  
                returns (string): a colon separated list representing the different classifications that should be excluded from the classification the nodeTreeBuilder is inquiring about.  
              
              
                provideClassificationStringsForFilteredTreeLister  
              
                This hook is called by 'createAssignNewMaterialTreeLister' and gives plugins a chance to append to the classification filter passed to the Tree Lister builder. It must return a string where each new classification is separated by a white space.  
              
              
                currentFilterString (string): a white-space-separated string representing the current classifications.  
              
              
                nodeCanBeUsedAsMaterial  
              
                The hook is used by the RMB 'Assign Favorite Material' menu to determine which shading nodes can be used as materials. It must return 1 if the node can be used as a material node and 0 otherwise.  
              
              
                nodeId (string): the node Id of the shading node being queried.  
                nodeOwner (string): the name of the plugin the node belongs to.  
              
              
                addHeaderContentToMayaLambertianShadersAE  
              
                This hook is called to give plugins a chance to add content to the header of the Attribute Editor of Maya's Lambertian-â€‹derived shaders.  
              
              
                nodeName (string): the name of the node for which the Attribute Editor is being constructed.  
              
              
                provideNodeToAttrConnection  
              
                This hook is called to give plugins a chance to provide which output attribute should be used when a node is connected to an input attribute.  
                If an input attribute type is given an output attribute of matching type should be returned. If no attribute type is specified (empty string)  
                a preferred output attribute of any type can be returned. If no output attribute of matching type is available an empty string should be returned.  
              
              
                nodeType (string): the node type of the node queried.  
                attributeType (string): the data type of the input attribute.  
                returns (string): the name of the output attribute to use.  
              
              
                provideNodeToNodeConnection  
              
                This hook is called to give plugins a chance to provide which attributes should be connected when a node to node connection is made.  
                Both the source and destination attributes should be returned in a colon separated list, e.g. "src1. dst1. src2. dst2. src3. dst3"  
              
              
                srcType (string): the node type of the source node.  
                dstType (string): the node type of the destination node.  
                returns (string): A colon separated list of source and destination attribute names.  
              
              
                provideOutputAttributeNameForTextureNode  
              
                This hook is called to give plugins a chance to provide a different output attribute name for Texture nodes. If this hook isn't provided 'outColor' is used.  
              
              
                nodeName (string): the name of the texture node queried.  
                returns (string): the output attribute name of the Texture node.  
              
              
                addItemsToHypergraphNodePopupMenu  
              
                This hook is called to give plugins a chance to add items to the Hypergraph node popup menu.  
                Plugins should add a menu item divider (using: menuItem -divider true) before adding any more items to the popup menu.  
              
              
                nodeName (string): the name of the node for which the Hypergraph node menu is being constructed.  
              
              
                addItemsToOutlinerNodePopupMenu  
              
                This hook is called to give plugins a chance to add items to the Outliner node popup menu.  
                Plugins should add a menu item divider (using: menuItem -divider true) before adding any more items to the popup menu.  
              
              
                nodeName (string): the name of the node or Ufe path string for which the Outliner node menu is being constructed.  
              
              
                addItemsToRenderLayerEditorPopupMenu  
              
                This hook is called to give plugins a chance to add items to the Render Layer Editor popup menu.  
                Plugins should add a menu item divider (using: menuItem -divider true) before adding any more items to the popup menu.  
              
              
                layerName (string): the name of the render layer for which the popup menu is being constructed.  
              
              
                preventMaterialDeletionFromCleanUpSceneCommand  
              
                This hook is called by the cleanUpScene command and gives the plugin a chance to communicate that a material node is still in use and shouldn't be deleted. The hook is called once per plug/connection pair of each shader instance.  
              
              
                shader (string): the name of the shader node being deleted.  
                plug (string): the name of the plug queried.  
                connection (string): the name of the connection queried.  
              
              
                connectNodeToNodeOverrideCallback  
              
                This hook is called to give plugins a chance to redefine the behavior of drag and drop.  
              
              
                srcNode (string): the name of the source node (the dragged node).  
                dstNode (string): the name of the destination node (the dropped-on node).  
                returns (int): Return 1 if Maya should perform the operation that would normally result from this connection. Return 0 to override and provide custom behavior.  
              
              
                prepareRenderChanged  
              
                This hook is called after an edit on a traversal set with the prepareRender command.  
              
              
                enableRenderPassMenuOfRenderView  
              
                This hook is called to give plugins a chance to tell Maya it should enable the render pass menu of the render view (under File->Load Render Pass). 'addRenderPassMenuItemsToRenderView' can be used to add items to this menu.  
              
              
                returns (int): Return 1 if the plugin wants the render pass menu of the render view to be enabled. Return 0 otherwise.  
              
              
                addItemsToRenderPassMenuOfRenderView  
              
                This hook is called to give plugins a chance to add menu items to the 'render pass' menu of the render view (under File->Load Render Pass). 'enableRenderPassMenuOfRenderView' can be used to enable the render pass menu of the render view.  
              
              
                addItemsToRMBMenuOfTreeLister  
              
                This hook is called to give plugins a chance to populate the RMB menu of nodes listed in a tree lister. Plugins should add a menu item divider (using: menuItem -divider true) before adding any more items to the RMB menu.  
              
              
                nodeType (string): The node type of the tree lister node for which the RMB menu is being built.  
                scriptCommand (string): The script command associated with the tree lister node for which the RMB menu is being built.  
                returns (int): Return 0 if Maya should append its own items to the menu of the current node type. This should be the return value for all node types a plugin isn't explicitly interested in. Return 1 if Maya shouldn't add any of its items to the menu of the current node type. Note: All menu items related to managing the 'Favorites' section of the tree lister will always be added to the RMB menu regardless of the return value (those are treated as special cases).  
              
              
                saveCustomNodePresetAttributes  
              
                This hook is called to give plugins a chance to store extra commands in the node preset file being saved.  
              
              
                presetNodeToSave (string): The name of the preset node being saved.  
                returns (string): The custom procedure to use to generate the mel script to be appended to the nodePreset -custom flag of the current presetNode save event (see the documentation of the nodePreset command for more information on the format of the -custom flag).  
              
              
                addItemToFileMenu  
              
                This hook is called to give plugins a chance to add menu items to the main File menu.  
              
              
                addItemToCreateLightMenu  
              
                This hook is called to give plugins a chance to add menu items to the create light menu.  
              
                textureReload  
              
                This hook is called to give plugins a chance to update all nodes that reference the texture file.  
              
              
                file (string): the file path of the texture to reload.  
              
              
                renderSettingsBuilt  
              
                This hook is called after the render settings window has been built.  
              
                rendererAddOneTabToGlobalsWindowCreateProc  
              
                This hook is called to allow renderers the opportunity to add renderer specific tabs to the unified render globals window (render settings window).  
              
              
                createProc (string): the name of the procedure used to create the content of the tab.   
              
              
                shouldEarlyReturnFromUpdateMultiCameraBufferNamingMenu  
              
                This hook is called to allow users to early return from the updateMultiCameraBufferNamingMenu() function by returning "true" in the callback handler.  
              
              
                returns (string): Returns "true" if the caller wishes to early return from the updateMultiCameraBufferNamingMenu() function.  
              
              
                shouldEarlyReturnFromUpdateMayaSoftwareImageFormatControl  
              
                This hook is called to allow users to early return from the updateMayaSoftwareImageFormatControl() function by returning "true" in the callback handler.  
              
              
                returns (string): Returns "true" if the caller wishes to early return from the updateMayaSoftwareImageFormatControl() function.  
              
              
                shouldEarlyReturnFromUpdateDefaultTraversalSetMenu  
              
                This hook is called to allow users to early return from the updateDefaultTraversalSetMenu() function by returning "true" in the callback handler.  
              
              
                returns (string): Returns "true" if the caller wishes to early return from the updateDefaultTraversalSetMenu() function.  
              
              
                shouldEarlyReturnFromShouldAppearInNodeCreateUI  
              
                This hook is called to allow users to early return from the shouldAppearInNodeCreateUI() function by returning "true" in the callback handler.  
              
              
                returns (string): Returns "true" if the caller wishes to early return from the shouldAppearInNodeCreateUI() function.  
              
              
                updateAE  
              
                This hook is called at the end of the updateAE() function.  
                Properties: create
        dumpCallbacks (bool?): Gives a list of all the registered callbacks for all hooks and owners. Can be  
                useful for debugging.  
                Properties: create
        executeCallbacks (bool?): Execute the callbacks for the specified hook, passing the extra arguments to  
                each callback when it is executed.  Returns an array (MEL) or list (Python)  
                containing the return values from each callback that was executed.  
                If a callback returns no value, the array will contain an empty string (MEL)  
                or None (Python).  
                Properties: create
        hook (str?): The name of the hook for which the callback should be registered.  
                Properties: create
        listCallbacks (bool?): Get the list of callbacks for the specified hook name. If the owner is  
                specified, only callbacks for the specified hook and owner will be listed.  
                Properties: create
        owner (str?): The name of the owner registering the callback. This is typically a plugin name.  
                Properties: create
        removeCallback (Callable[..., Any]?): Remove an existing callback for the specified hook name. The owner must  
                also be specified when removing a callback.  
                Properties: create

    Returns:
        List[str]: Command result

    Example:
    """

