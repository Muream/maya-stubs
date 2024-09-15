from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def prepareRender(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., defaultTraversalSet: Queryable[str] = ..., deregister: str = ..., invokePostRender: bool = ..., invokePostRenderFrame: bool = ..., invokePostRenderLayer: bool = ..., invokePreRender: bool = ..., invokePreRenderFrame: bool = ..., invokePreRenderLayer: bool = ..., invokeSettingsUI: bool = ..., label: Queryable[str] = ..., listTraversalSets: bool = ..., postRender: Queryable[Callable[..., Any]] = ..., postRenderFrame: Queryable[Callable[..., Any]] = ..., postRenderLayer: Queryable[Callable[..., Any]] = ..., preRender: Queryable[Callable[..., Any]] = ..., preRenderFrame: Queryable[Callable[..., Any]] = ..., preRenderLayer: Queryable[Callable[..., Any]] = ..., restore: bool = ..., saveAssemblyConfig: bool = ..., settingsUI: Queryable[Callable[..., Any]] = ..., setup: bool = ..., traversalSet: str = ..., traversalSetInit: Queryable[Callable[..., Any]] = ...) -> Union[bool, str, Callable[..., Any]]:
    """This command is used to register, manage and invoke render traversals.
    Render traversals are used to configure a scene to prepare it for rendering.This command has special support for scene assembly nodes.  To render scene
    assembly nodes, a rendering traversal can activate an appropriate
    representation, for each assembly node in the scene.  When rendering is
    done, this command can correspondingly restore the representation that was
    active before rendering on each assembly.
    Render traversals are grouped into traversal sets.  A render traversal set
    includes callbacks, or render traversals, for one or more of the following
    steps of rendering, ordered by decreasing level of granularity.
    A render traversal callback is an arbitrary script, either MEL or Python,
    that can transform the Maya scene for rendering purposes.During a render view or batch render, Maya will run the render traversals from
    the same traversal set, the default traversal set.  Traversal sets are named,
    so multiple traversal sets can be registered with this command, and the
    default render traversal set can be switched to any one of these registered
    traversal sets.  When changing the default traversal set, the different
    render traversal callbacks (preRender, preRenderLayer, preRenderFrame,
    postRender, postRenderLayer, postRenderFrame) are switched as a unit.At render time, the software rendering code invokes the callbacks of the
    default traversal set.  The prepareRender scripting capability allows for the
    development of multiple rendering preparation scripts, including from plugins,
    to provide extensibility rather than being constrained to a single
    implementation.A special traversal set is the "null" traversal set.  It is the initial
    default traversal set, and cannot be deregistered.  It performs no work,
    and does not save and restore the assembly node active representation
    configuration.  It will provide WYSIWYG (What You See Is What You Get)
    rendering of assembly nodes, without switching to a different representation
    to render.Render traversals are invoked by Maya using this command's create mode.
    This is done by Maya's rendering infrastructure, and should not be required
    unless developing new render views or batch render code.  Most uses of this
    command will simply use the edit mode to register render traversals into a
    render traversal set, or the query mode to query the names of the render
    traversals in a render traversal set.Render traversals are similar in intent to the user-specified pre- and
    post-render, pre- and post-render layer, pre- and post-render frame MEL
    script capability.  The difference with the user MEL scripts is
    that prepareRender is in addition to, and does not replace, the user
    MEL scripts, can register multiple render traversal sets and switch them,
    and supports both MEL and Python.  The MEL render scripts are run inside
    the scope of the render traversals, that is, the preRender traversal is
    run before the pre-render MEL script and the postRender traversal is run
    after the post-render MEL script, the preRenderLayer traversal is run before
    the pre-render layer MEL script and the postRenderLayer traversal is run
    after the post-render layer MEL script, and finally the preRenderFrame
    traversal is run before the pre-render frame MEL script and the
    postRenderFrame traversal is run after the post-render frame MEL script.The prepareRender command has support for saving and restoring the active
    representation of assembly nodes in the scene.  Use the saveAssemblyConfig flag
    to indicate that the render traversal set requires saving the assembly node
    active representation before rendering begins, and should restore the
    assembly node active representation after rendering ends.It is the responsibility of render traversals that modify the scene in ways
    other than changing the active representation on assembly nodes to restore the
    scene to its previous state, most likely using the postRender, postRenderLayer,
    and postRenderFrame traversals.Note that Maya does not call the prepareRender -restore command on
    batch render completion, since batch rendering is done on a copy of the
    scene which is discarded once rendering terminates.  Implementors of
    render traversals may wish to check whether they are running in batch mode,
    to implement the same optimization.render, assembly
    Args:
        defaultTraversalSet (Queryable[str]?): Set or query the default traversal set.  The prepareRender  
                command performs operations on the default traversal set, unless the  
                -traversalSet flag is used to specify an explicit traversal set.  
                Properties: query, edit
        deregister (str?): Deregister a registered traversal set.  If the deregistered traversal set is  
                the default traversal set, the new default traversal set will be the "null"  
                traversal set.  
                Properties: edit
        invokePostRender (bool?): Invoke the postRender render traversal for a given traversal  
                set.  The traversal set will be the default traversal set, unless the  
                -traversalSet flag is used to specify an explicit traversal set.  
                Properties: create
        invokePostRenderFrame (bool?): Invoke the postRenderFrame render traversal for a given traversal  
                set.  The traversal set will be the default traversal set, unless the  
                -traversalSet flag is used to specify an explicit traversal set.  
                Properties: create
        invokePostRenderLayer (bool?): Invoke the postRenderLayer render traversal for a given traversal  
                set.  The traversal set will be the default traversal set, unless the  
                -traversalSet flag is used to specify an explicit traversal set.  
                Properties: create
        invokePreRender (bool?): Invoke the preRender render traversal for a given traversal  
                set.  The traversal set will be the default traversal set, unless the  
                -traversalSet flag is used to specify an explicit traversal set.  
                Properties: create
        invokePreRenderFrame (bool?): Invoke the preRenderFrame render traversal for a given traversal  
                set.  The traversal set will be the default traversal set, unless the  
                -traversalSet flag is used to specify an explicit traversal set.  
                Properties: create
        invokePreRenderLayer (bool?): Invoke the preRenderLayer render traversal for a given traversal  
                set.  The traversal set will be the default traversal set, unless the  
                -traversalSet flag is used to specify an explicit traversal set.  
                Properties: create
        invokeSettingsUI (bool?): Invoke the settings UI callback to populate a layout with UI controls,  
                for a given traversal set.  The current UI parent will be a form layout,  
                which the callback can query using the setParent command.  The traversal set  
                will be the default traversal set, unless the -traversalSet flag is used to  
                specify an explicit traversal set.  
                Properties: create
        label (Queryable[str]?): Set or query the label for a given traversal set.  The label is used for UI  
                display purposes, and can be localized.  The traversal set will be the default,  
                unless the -traversalSet flag is used to specify an explicit traversal set.  
                Properties: query, edit
        listTraversalSets (bool?): Query the supported render traversal sets.  
                Properties: query
        postRender (Queryable[Callable[..., Any]]?): Set or query the postRender render traversal for a given traversal  
                set.  This traversal is run after a render.  The traversal set will be the  
                default traversal set, unless the -traversalSet flag is used to specify an  
                explicit traversal set.  
                Properties: query, edit
        postRenderFrame (Queryable[Callable[..., Any]]?): Set or query the postRenderFrame render traversal for a given traversal  
                set.  This traversal is run after the render of a single frame, with a  
                render layer.  The traversal set will be the default traversal set, unless  
                the -traversalSet flag is used to specify an explicit traversal set.  
                Properties: query, edit
        postRenderLayer (Queryable[Callable[..., Any]]?): Set or query the postRenderLayer render traversal for a given traversal  
                set.  This traversal is run after a render layer is rendered, within a  
                render.  The traversal set will be the default traversal set, unless the  
                -traversalSet flag is used to specify an explicit traversal set.  
                Properties: query, edit
        preRender (Queryable[Callable[..., Any]]?): Set or query the preRender render traversal for a given traversal  
                set.  This traversal is run before a render.  The traversal set will be the  
                default traversal set, unless the -traversalSet flag is used to specify an  
                explicit traversal set.  
                Properties: query, edit
        preRenderFrame (Queryable[Callable[..., Any]]?): Set or query the preRenderFrame render traversal for a given traversal  
                set.  This traversal is run before the render of a single frame, with a  
                render layer.  The traversal set will be the default traversal set, unless  
                the -traversalSet flag is used to specify an explicit traversal set.  
                Properties: query, edit
        preRenderLayer (Queryable[Callable[..., Any]]?): Set or query the preRenderLayer render traversal for a given traversal  
                set.  This traversal is run before a render layer is rendered, within a  
                render.  The traversal set will be the default traversal set, unless the  
                -traversalSet flag is used to specify an explicit traversal set.  
                Properties: query, edit
        restore (bool?): Clean up after rendering, including restoring the assembly active  
                representation configuration for the whole scene, if the saveAssemblyConfig  
                flag for the traversal set is true.  The traversal set will be the default  
                traversal set, unless the -traversalSet flag is used to specify an explicit  
                traversal set.  
                Properties: create
        saveAssemblyConfig (bool?): Set or query whether or not the assembly active representation configuration  
                for the whole scene should be saved for a given traversal set.  The traversal  
                set will be the default, unless the -traversalSet flag is used to specify an  
                explicit traversal set.  
                Properties: query, edit
        settingsUI (Queryable[Callable[..., Any]]?): Set or query the settings UI callback for a given traversal set.  The  
                traversal set will be the default traversal set, unless the -traversalSet  
                flag is used to specify an explicit traversal set.  
                Properties: query, edit
        setup (bool?): Setup render preparation, including saving the assembly active representation  
                configuration for the whole scene, if the saveAssemblyConfig flag for  
                the traversal set is true.  Any previously-saved configuration will be  
                overwritten.  The traversal set will be the default traversal set, unless the  
                -traversalSet flag is used to specify an explicit traversal set.  
                Properties: create
        traversalSet (str?): Set or query properties for the specified registered traversal set.  
                			In query mode, this flag needs a value.  
                Properties: create, query, edit
        traversalSetInit (Queryable[Callable[..., Any]]?): Set or query the traversal set initialisation callback for a given traversal set.  
                The traversal set will be the default traversal set, unless the -traversalSet flag  
                is used to specify an explicit traversal set. This callback is invoked whenever  
                the specified traversal set becomes the default.  
                traversal set.  
                Properties: query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

