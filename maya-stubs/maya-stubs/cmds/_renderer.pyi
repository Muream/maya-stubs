from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def renderer(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., addGlobalsNode: Queryable[str] = ..., addGlobalsTab: Tuple[str, str, str] = ..., batchRenderOptionsProcedure: Queryable[str] = ..., batchRenderOptionsStringProcedure: Queryable[str] = ..., batchRenderProcedure: Queryable[str] = ..., cancelBatchRenderProcedure: Queryable[str] = ..., changeIprRegionProcedure: Queryable[str] = ..., commandRenderProcedure: Queryable[str] = ..., exists: bool = ..., globalsNodes: bool = ..., globalsTabCreateProcNames: bool = ..., globalsTabLabels: bool = ..., globalsTabUpdateProcNames: bool = ..., iprOptionsMenuLabel: Queryable[str] = ..., iprOptionsProcedure: Queryable[str] = ..., iprOptionsSubMenuProcedure: Queryable[str] = ..., iprRenderProcedure: Queryable[str] = ..., iprRenderSubMenuProcedure: Queryable[str] = ..., isRunningIprProcedure: Queryable[str] = ..., logoCallbackProcedure: Queryable[str] = ..., logoImageName: Queryable[str] = ..., materialViewRendererList: bool = ..., materialViewRendererPause: bool = ..., materialViewRendererSuspend: bool = ..., namesOfAvailableRenderers: bool = ..., pauseIprRenderProcedure: Queryable[str] = ..., polyPrelightProcedure: Queryable[str] = ..., refreshIprRenderProcedure: Queryable[str] = ..., renderDiagnosticsProcedure: Queryable[str] = ..., renderGlobalsProcedure: Queryable[str] = ..., renderMenuProcedure: Queryable[str] = ..., renderOptionsProcedure: Queryable[str] = ..., renderProcedure: Queryable[str] = ..., renderRegionProcedure: Queryable[str] = ..., renderSequenceProcedure: Queryable[str] = ..., rendererUIName: Queryable[str] = ..., renderingEditorsSubMenuProcedure: Queryable[str] = ..., showBatchRenderLogProcedure: Queryable[str] = ..., showBatchRenderProcedure: Queryable[str] = ..., showRenderLogProcedure: Queryable[str] = ..., startIprRenderProcedure: Queryable[str] = ..., stopIprRenderProcedure: Queryable[str] = ..., supportColorManagement: bool = ..., textureBakingProcedure: Queryable[str] = ..., unregisterRenderer: bool = ...) -> Union[bool, str]:
    """Command to register renders.  This command allows you to
    specify the UI name and procedure names for renderers.
    The command also allow you to query the UI name and the procedure
    names for the registered renders.renderer, registration
    Args:
        addGlobalsNode (Queryable[str]?): This flag allows the user to add a globals node the specified  
                renderer uses.  
                Properties: create, query, edit
        addGlobalsTab (Tuple[str, str, str]?): Add a tab associated with the specified renderer for the  
                unified render globals window.  
                Properties: create, edit
        batchRenderOptionsProcedure (Queryable[str]?): Set or query the batch render options procedure associated with the  
                specified renderer.  
                Properties: create, query, edit
        batchRenderOptionsStringProcedure (Queryable[str]?): Set or query the argument string that will be used with the command  
                line utility 'Render' when doing a batch render  
                Properties: create, query, edit
        batchRenderProcedure (Queryable[str]?): Set or query the batch render procedure associated with the  
                specified renderer.  
                Properties: create, query, edit
        cancelBatchRenderProcedure (Queryable[str]?): Set or query returns the cancel batch render procedure associated  
                with the specified renderer.  
                Properties: create, query, edit
        changeIprRegionProcedure (Queryable[str]?): Set or query the change IPR region procedure associated with the  
                specified renderer.  
                Properties: create, query, edit
        commandRenderProcedure (Queryable[str]?): Set or query the command line rendering procedure associated with the  
                specified renderer.  
                Properties: create, query, edit
        exists (bool?): The flag returns true if the specified renderer is registered  
                in the registry, and it returns false otherwise.  
                Properties: query, edit
        globalsNodes (bool?): This flag returns the list of render globals nodes the  
                specified renderer uses.  
                Properties: create, query, edit
        globalsTabCreateProcNames (bool?): This flag returns the names of procedures that are used to  
                create the unified render globals window tabs  
                that are associated with the specified renderer.  
                Properties: create, query, edit
        globalsTabLabels (bool?): This flag returns the labels of unified render globals window tabs  
                that are associated with the specified renderer.  
                Properties: create, query, edit
        globalsTabUpdateProcNames (bool?): This flag returns the names of procedures that are used to  
                update the unified render globals window tabs  
                that are associated with the specified renderer.  
                Properties: create, query, edit
        iprOptionsMenuLabel (Queryable[str]?): Set or query the label for the IPR update options menu which is under  
                the render view's IPR menu.  
                Properties: create, query, edit
        iprOptionsProcedure (Queryable[str]?): Set or query the IPR render options procedure associated with the  
                specified renderer.  
                Properties: create, query, edit
        iprOptionsSubMenuProcedure (Queryable[str]?): Set or query the procedure for creating the sub menu for the IPR  
                update options menu which is under the render view's IPR menu.  
                Properties: create, query, edit
        iprRenderProcedure (Queryable[str]?): Set or query the IPR render command associated with the  
                specified renderer.  
                Properties: create, query, edit
        iprRenderSubMenuProcedure (Queryable[str]?): Set or query the procedure for creating the sub menu for the IPR  
                render menu which is under the render view's IPR menu.  
                Properties: create, query, edit
        isRunningIprProcedure (Queryable[str]?): Set or query the isRunningIpr command associated with the  
                specified renderer.  
                Properties: create, query, edit
        logoCallbackProcedure (Queryable[str]?): Set or query the procedure which is a callback associated to the  
                logo for the specified renderer.   For example, the logo and the  
                callback can be used in the unified render globals window beside  
                the "Render Using" optionMenu.  
                Properties: create, query, edit
        logoImageName (Queryable[str]?): Set or query the logo image name for the specified renderer.  
                The logo is a image representing the renderer.  
                Properties: create, query, edit
        materialViewRendererList (bool?): Returns the names of material view renderers that are currently registered.  
                Properties: query, edit
        materialViewRendererPause (bool?): Specifies whether to pause the material viewer.  
                Useful for globally halting updates to the material viewer.  
                The material view renderer will remain suspended while the viewer is paused.  
                Properties: query, edit
        materialViewRendererSuspend (bool?): Specifies whether to suspend or resume the material view renderer.  
                Useful for temporarily stopping the material view renderer while another  
                rendering task is running.  
                Properties: query, edit
        namesOfAvailableRenderers (bool?): Returns the names of renderers that are currently registered.  
                Properties: query, edit
        pauseIprRenderProcedure (Queryable[str]?): Set or query the pause IPR render procedure associated with the  
                specified renderer.  
                Properties: create, query, edit
        polyPrelightProcedure (Queryable[str]?): Set or query the polygon prelight procedure associated with  
                the specified renderer.  
                Properties: create, query, edit
        refreshIprRenderProcedure (Queryable[str]?): Set or query the refresh IPR render procedure associated with the  
                specified renderer.  
                Properties: create, query, edit
        renderDiagnosticsProcedure (Queryable[str]?): Set or query the render diagnostics procedure associated with the  
                specified renderer.  
                Properties: create, query, edit
        renderGlobalsProcedure (Queryable[str]?): This flag is obsolete.  It will be removed in the next release.  
                Properties: create, query, edit
        renderMenuProcedure (Queryable[str]?): This flag is obsolete. It will be removed in the next release.  
                Properties: create, query, edit
        renderOptionsProcedure (Queryable[str]?): Set or query the render options procedure associated with the  
                specified renderer.  
                Properties: create, query, edit
        renderProcedure (Queryable[str]?): Set or query the render command associated with the specified renderer.  
                Properties: create, query, edit
        renderRegionProcedure (Queryable[str]?): Set or query the render region procedure associated with the specified  
                renderer.  
                Properties: create, query, edit
        renderSequenceProcedure (Queryable[str]?): Set or query the sequence rendering procedure associated with the  
                specified renderer.  
                Properties: create, query, edit
        rendererUIName (Queryable[str]?): Set or query the rendererUIName for the specified renderer.  
                The rendererUIName is the name of the renderer as it would appear  
                in menus.  
                Properties: create, query, edit
        renderingEditorsSubMenuProcedure (Queryable[str]?): Set or query the procedure reponsible for creating renderer  
                specific editors submenu under the "Rendering Editors" menu  
                for the specified renderer.  
                Properties: create, query, edit
        showBatchRenderLogProcedure (Queryable[str]?): Set or query the log file batch procedure associated with the  
                specified renderer.  
                Properties: create, query, edit
        showBatchRenderProcedure (Queryable[str]?): Set or query the show batch render procedure associated with  
                the specified renderer.  
                Properties: create, query, edit
        showRenderLogProcedure (Queryable[str]?): Set or query the log file render procedure associated with  
                the specified renderer.  
                Properties: create, query, edit
        startIprRenderProcedure (Queryable[str]?): Set or query the start IPR render procedure associated with the  
                specified renderer.  
                Properties: create, query, edit
        stopIprRenderProcedure (Queryable[str]?): Set or query the stop IPR render procedure associated with the  
                specified renderer.  
                Properties: create, query, edit
        supportColorManagement (bool?): Specifies whether the renderer supports color management.  
                Properties: query, edit
        textureBakingProcedure (Queryable[str]?): Set or query the texture baking procedure associated with  
                the specified renderer.  
                Properties: create, query, edit
        unregisterRenderer (bool?): Unregister the specified renderer.  
                Properties: query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

