from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def pluginInfo(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., activeFile: bool = ..., allEvaluators: bool = ..., animCurveInterp: Queryable[str] = ..., apiVersion: bool = ..., autoload: bool = ..., cacheFormat: bool = ..., changedCommand: Callable[..., Any] = ..., command: Queryable[Multiuse[str]] = ..., constraintCommand: bool = ..., controlCommand: bool = ..., data: Queryable[Multiuse[Tuple[str, str]]] = ..., dependNode: Queryable[Multiuse[bool]] = ..., dependNodeByType: Queryable[str] = ..., dependNodeId: Queryable[str] = ..., device: bool = ..., dragAndDropBehavior: bool = ..., evaluator: bool = ..., iksolver: bool = ..., listPlugins: bool = ..., listPluginsPath: bool = ..., loadPluginPrefs: bool = ..., loaded: bool = ..., modelEditorCommand: bool = ..., name: Queryable[str] = ..., path: Queryable[str] = ..., pluginsInUse: bool = ..., referenceTranslators: bool = ..., registered: bool = ..., remove: bool = ..., renderer: bool = ..., savePluginPrefs: bool = ..., serviceDescriptions: bool = ..., settings: bool = ..., tool: Queryable[Multiuse[str]] = ..., translator: bool = ..., unloadOk: bool = ..., userNamed: bool = ..., vendor: Queryable[str] = ..., version: bool = ..., writeRequires: bool = ...) -> Union[Any, bool, str, Multiuse[str], Multiuse[Tuple[str, str]], Multiuse[bool]]:
    """This command provides access to the plug-in registry of the
    application. It is used mainly to query the characteristics of
    registered plug-ins. Plugins automatically become registered the first
    time that they are loaded.The argument is either the internal name of the plug-in or the path to
    access it.
    Args:
        activeFile (bool?): Restricts the command to the active file only, not the entire scene.  
                This only affects the dependNode/dn and pluginsInUse/pu flags.  
                For use during export selected.  
                Properties: query
        allEvaluators (bool?): Returns a string array containing the names of all of the  
                evaluator types registered to any plug-in.  
                Properties: query
        animCurveInterp (Queryable[str]?): Returns a string array containing the names of all of the  
                animation curve interpolators registered by this plug-in.  
                Properties: query
        apiVersion (bool?): Returns a string containing the version of the API that this  
                plug-in was compiled with.  See the comments in MTypes.h for the  
                details on how to interpret this value.  
                Properties: query
        autoload (bool?): Sets whether or not this plug-in should be loaded every  
                time the application starts up. Returns a boolean in query mode.  
                Properties: create, query, edit
        cacheFormat (bool?): Returns a string array containing the names of all of the  
                registered geometry cache formats  
                Properties: query
        changedCommand (Callable[..., Any]?): Adds a callback that will get executed every time the plug-in  
                registry changes. Any other previously registered callbacks will  
                also get called.  
                Properties: create
        command (Queryable[Multiuse[str]]?): Returns a string array containing the names of all of the  
                normal commands registered by this plug-in.  
                Constraint, control, context and model editor commands are not included.  
                Properties: query, multiuse
        constraintCommand (bool?): Returns a string array containing the names of all of the  
                constraint commands registered by this plug-in.  
                Properties: query
        controlCommand (bool?): Returns a string array containing the names of all of the  
                control commands registered by this plug-in.  
                Properties: query
        data (Queryable[Multiuse[Tuple[str, str]]]?): Returns a string array containing the names of all of the  
                data types registered by this plug-in.  
                Properties: query, multiuse
        dependNode (Queryable[Multiuse[bool]]?): Returns a string array containing the names of all of the  
                custom nodes types registered by this plug-in.  
                Properties: query, multiuse
        dependNodeByType (Queryable[str]?): Returns a string array of all registered node types within a specified  
                class of nodes.  Each custom node type registered by a plug-in belongs  
                to a more general class of node types as specified by its  
                MPxNode::Type. The flag's argument is an MPxNode::Type as a string.  For  
                example, if you want to list all registered Locator nodes, you should  
                specify kLocatorNode as a argument to this flag.  
                Properties: query
        dependNodeId (Queryable[str]?): Returns an integer array containing the ids of all of the  
                custom node types registered by this plug-in.  
                Properties: query
        device (bool?): Returns a string array containing the names of all of the  
                devices registered by this plug-in.  
                Properties: query
        dragAndDropBehavior (bool?): Returns a string array containing the names of all of the  
                drag and drop behaviors registered by this plug-in.  
                Properties: query
        evaluator (bool?): Returns a string array containing the names of all of the  
                evaluator types registered by this plug-in.  
                Properties: query
        iksolver (bool?): Returns a string array containing the names of all of the  
                ik solvers registered by this plug-in.  
                Properties: query
        listPlugins (bool?): Returns a string array containing all the plug-ins that are  
                currently loaded.  
                Properties: query
        listPluginsPath (bool?): Returns a string array containing the full paths of all the plug-ins that are  
                currently loaded.  
                Properties: query
        loadPluginPrefs (bool?): Loads the plug-in preferences (ie. autoload) from pluginPrefs.mel into Maya.  
                Properties: create
        loaded (bool?): Returns a boolean specifying whether or not the plug-in is loaded.  
                Properties: query
        modelEditorCommand (bool?): Returns a string array containing the names of all of the  
                model editor commands registered by this plug-in.  
                Properties: query
        name (Queryable[str]?): Returns a string containing the internal name by which the  
                plug-in is registered.  
                Properties: query
        path (Queryable[str]?): Returns a string containing the absolute path name to the plug-in.  
                Properties: query
        pluginsInUse (bool?): Returns a string array containing all the plug-ins that are  
                currently being used in the scene.  
                Properties: query
        referenceTranslators (bool?): If this flag is used in conjunction with the pluginsInUse/pu flag  
                then it will modify the output. When true it will only show plug-ins currently in use  
                containing translators that are used to load referenced files. When false it  
                will only show plug-ins not containing such translators.  
                Properties: query
        registered (bool?): Returns a boolean specifying whether or not plug-in is currently  
                registered with the system.  
                Properties: query
        remove (bool?): Removes the given plug-in's record from the registry.  
                There is no return value.  
                Properties: edit
        renderer (bool?): Returns a string array containing the names of all of the  
                renderers registered by this plug-in.  
                Properties: query
        savePluginPrefs (bool?): Saves the plug-in preferences (ie. autoload) out to pluginPrefs.mel  
                Properties: create
        serviceDescriptions (bool?): If there are services in use, then this flag will return a string  
                array containing short descriptions saying what those services are.  
                Properties: query
        settings (bool?): Returns an array of values with the loaded, autoload, registered flags  
                Properties: query
        tool (Queryable[Multiuse[str]]?): Returns a string array containing the names of all of the  
                tool contexts registered by this plug-in.  
                Properties: query, multiuse
        translator (bool?): Returns a string array containing the names of all of the  
                file translators registered by this plug-in.  
                Properties: query
        unloadOk (bool?): Returns a boolean that specifies whether or not the plug-in can  
                be safely unloaded.  It will return false if the plug-in is currently  
                in use.  For example, if the plug-in adds a new dependency node type,  
                and an instance of that node type is present in the scene, then this  
                query will return false.  
                Properties: query
        userNamed (bool?): Returns a boolean specifying whether or not the plug-in has  
                been assigned a name by the user.  
                Properties: query
        vendor (Queryable[str]?): Returns a string containing the vendor of the plug-in.  
                Properties: query
        version (bool?): Returns a string containing the version the plug-in.  
                Properties: query
        writeRequires (bool?): Sets whether or not this plug-in should write "requires" command  
                into the saved file. "requires" command could autoload  
                the plug-in when you open or import that saved file.  
                This way, Maya will load the plug-in  
                when a file is being loaded for some specified reason,  
                such as to create a customized UI or to load some plug-in data  
                that is not saved in any node or attributes.  
                For example, "stereoCamera" is using this flag for its customized UI.  
                Properties: create, query, edit

    Returns:
        Any: Dependent upon the action requested.

    Example:
    """

