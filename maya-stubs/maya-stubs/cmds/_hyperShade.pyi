from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def hyperShade(*args: Any, assign: str = ..., clearWorkArea: bool = ..., collapse: str = ..., createNode: str = ..., dependGraphArea: bool = ..., downStream: bool = ..., duplicate: bool = ..., fixRenderSize: bool = ..., geometries: Multiuse[str] = ..., incremental: bool = ..., listDownstreamNodes: str = ..., listDownstreamShaderNodes: str = ..., listGeometries: str = ..., listMaterialNodes: bool = ..., listUpstreamNodes: str = ..., name: str = ..., networks: bool = ..., noSGShapes: bool = ..., noShapes: bool = ..., noTransforms: bool = ..., objects: str = ..., renderCreateAndDrop: str = ..., reset: bool = ..., resetGraph: bool = ..., resetSwatch: bool = ..., setAllowsRegraphing: bool = ..., setWorkArea: str = ..., shaderNetwork: str = ..., shaderNetworks: bool = ..., shaderNetworksSelectMaterialNodes: bool = ..., snapShot: bool = ..., uncollapse: str = ..., upStream: bool = ..., useMaterialTemplate: bool = ..., userDefinedLayout: bool = ..., workAreaAddCmd: str = ..., workAreaDeleteCmd: str = ..., workAreaSelectCmd: str = ...) -> str:
    """Commands for shader editing in the hypergraphrender, hypergraph, shader, hypershade
    Args:
        assign (str?): Assign the specified shader node to renderable objects on the active list  
                or the geometries in the -geometries option when specified.  
                The node can either be a shading group or the shader node attached to the  
                shading group.  
                Properties: create
        clearWorkArea (bool?): Push the current work area on to the stack and create a clear work area  
                Properties: create
        collapse (str?): Hide the upstream nodes from the specified node.  
                Properties: create
        createNode (str?): Create a node of the specified type.  This is called when a new rendering  
                node is created using drag and drop from the image browser or from the  
                RMB context sensitive menu on nodes in the Visor Create folders.  
                Properties: create
        dependGraphArea (bool?): When setting a work area, and the work area doesn't already exist this  
                flag inicates a new graph should be created that is either a depend graph  
                or a folder view.  
                Properties: create
        downStream (bool?): Show nodes downstream from the specified node  
                Properties: create
        duplicate (bool?): Duplicate upstream nodes.  If the node is a shader make sure duplicate  
                include the shading group if there is one  
                Properties: create
        fixRenderSize (bool?): If set to true dont rerender swatches when they change size as the user  
                zooms  
                Properties: create
        geometries (Multiuse[str]?): When used in conjunction with the -assign option the shaders will be assigned to geometries specified here.  
                When used in conjunction with the -listMaterialNodes option the material nodes used by the geometries specified here will be listed.  
                Properties: create, multiuse
        incremental (bool?): Enable or disable incremental layout when making new nodes or connections  
                Properties: create
        listDownstreamNodes (str?): List all the downstream render nodes from the specified nodes.  
                Properties: create
        listDownstreamShaderNodes (str?): List all the downstream shader nodes from the specified nodes.  
                Properties: create
        listGeometries (str?): List the geoemtries which are attached to the specified shader node.  
                The shader node can be either the shading group or the shader attached  
                to the shading group.  When this flag's argument is the empty string,  
                we will use the currently selected shader node as the input.  
                Properties: create
        listMaterialNodes (bool?): List all the materials nodes for the geometries in the -geometries option  
                or, if not specified, the currently selected objects.  
                Properties: create
        listUpstreamNodes (str?): List all the upstream render nodes from the specified nodes.  
                Properties: create
        name (str?): Name for the work area created by this command  
                Properties: create
        networks (bool?): Do an incremental layout on all of the nodes in the current selection  
                list and that are in the current work area.  
                Properties: create
        noSGShapes (bool?): Display only shapes that are connected to nodes in the  
                network other than a shading group.  
                Properties: create
        noShapes (bool?): Display no shapes when graphing networks.  
                Properties: create
        noTransforms (bool?): Display no transforms when graphing networks.  
                Properties: create
        objects (str?): Select the objects which are attached to the specified shader node.  
                The shader node can be either the shading group or the shader attached  
                to the shading group.  When this flag's argument is the empty string,  
                we will use the currently selected shder node as the input.  
                Properties: create
        renderCreateAndDrop (str?): Create a render node of the specified type and put user into drag and  
                drop mode to place or connect it.  
                Properties: create
        reset (bool?): Reset the Hypershade panel to its initial state.  In particular delete all  
                the work areas.  
                Properties: create
        resetGraph (bool?): Reset the current graph.  Typically called prior to rebuilding a folder in  
                a Hypershade view.  
                Properties: create
        resetSwatch (bool?): For all selected nodes remove user defined swatches if the node has one  
                Properties: create
        setAllowsRegraphing (bool?): For internal use only.  
                Properties: create
        setWorkArea (str?): Set the work area to the existing named work area  
                Properties: create
        shaderNetwork (str?): Show the shader network for the specified material node.  If the materials  
                shading group has a displacement or volume map these will be shown.  If not  
                then the shading group will not be shown.  
                Properties: create
        shaderNetworks (bool?): Show the shader network for all the objects on the selection list that  
                have shaders.  
                Properties: create
        shaderNetworksSelectMaterialNodes (bool?): Select the material nodes in the shader network for all the  
                objects on the selection list that have shaders.  
                Properties: create
        snapShot (bool?): Put hypergraph in snapshot mode.  This is only for testing  
                Properties: create
        uncollapse (str?): Unhide the upstream nodes from the specified node.  
                Properties: create
        upStream (bool?): Show nodes upstream from the specified node  
                Properties: create
        useMaterialTemplate (bool?): Specifies that a material will be assigned using the materialTemplate method.  
                Properties: create
        userDefinedLayout (bool?): Enable or disable remembrance of user defined layouts.  Default is disabled  
                until this functionality is better tested.  
                Properties: create
        workAreaAddCmd (str?): Set the MEL procedure called when a new work area is added to HyperShade  
                Properties: create
        workAreaDeleteCmd (str?): Set the MEL procedure called when a work area is deleted in HyperShade  
                Properties: create
        workAreaSelectCmd (str?): Set the MEL procedure called when a work area is selected in HyperShade  
                Properties: create

    Returns:
        str: Command result

    Example:
    """

