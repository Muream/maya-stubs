from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def file(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., absoluteName: bool = ..., activate: bool = ..., activeProxy: bool = ..., add: bool = ..., anyModified: bool = ..., applyTo: str = ..., buildLoadSettings: bool = ..., channels: bool = ..., cleanReference: str = ..., command: Queryable[Tuple[str, str]] = ..., compress: bool = ..., constraints: bool = ..., constructionHistory: bool = ..., copyNumberList: bool = ..., defaultExtensions: bool = ..., defaultNamespace: bool = ..., deferReference: bool = ..., editCommand: str = ..., errorStatus: bool = ..., executeScriptNodes: bool = ..., exists: bool = ..., expandName: bool = ..., exportAll: bool = ..., exportAnim: bool = ..., exportAnimFromReference: bool = ..., exportAsReference: bool = ..., exportAsSegment: bool = ..., exportSelected: bool = ..., exportSelectedAnim: bool = ..., exportSelectedAnimFromReference: bool = ..., exportSelectedNoReference: bool = ..., exportSelectedStrict: bool = ..., exportSnapshotCallback: Tuple[Callable[..., Any], str] = ..., exportUnloadedReferences: bool = ..., expressions: bool = ..., fileMetaData: bool = ..., flushReference: str = ..., force: bool = ..., groupLocator: bool = ..., groupName: str = ..., groupReference: bool = ..., ignoreVersion: bool = ..., i: bool = ..., importFrameRate: bool = ..., importReference: bool = ..., importTimeRange: str = ..., lastFileOption: bool = ..., lastTempFile: bool = ..., list: bool = ..., loadAllDeferred: bool = ..., loadAllReferences: bool = ..., loadNoReferences: bool = ..., loadReference: Queryable[str] = ..., loadReferenceDepth: str = ..., loadReferencePreview: str = ..., loadSettings: str = ..., location: bool = ..., lockContainerUnpublished: bool = ..., lockFile: bool = ..., lockReference: bool = ..., mapPlaceHolderNamespace: Queryable[Multiuse[Tuple[str, str]]] = ..., mergeBaseAnimLayer: bool = ..., mergeNamespaceWithParent: bool = ..., mergeNamespaceWithRoot: bool = ..., mergeNamespacesOnClash: bool = ..., modified: bool = ..., moveSelected: bool = ..., namespace: str = ..., newFile: bool = ..., open: bool = ..., options: Queryable[str] = ..., parentNamespace: bool = ..., postSaveScript: str = ..., preSaveScript: str = ..., preserveName: bool = ..., preserveReferences: bool = ..., preview: bool = ..., prompt: bool = ..., proxyManager: str = ..., proxyTag: str = ..., reference: bool = ..., referenceDepthInfo: int = ..., referenceNode: Queryable[str] = ..., relativeNamespace: str = ..., removeDuplicateNetworks: bool = ..., removeReference: bool = ..., rename: str = ..., renameAll: bool = ..., renameToSave: bool = ..., renamingPrefix: Queryable[str] = ..., renamingPrefixList: bool = ..., replaceName: Queryable[Multiuse[Tuple[str, str]]] = ..., reserveNamespaces: bool = ..., resetError: bool = ..., returnNewNodes: bool = ..., save: bool = ..., saveDiskCache: Queryable[str] = ..., saveReference: bool = ..., saveReferencesUnloaded: bool = ..., saveTextures: Queryable[str] = ..., sceneName: bool = ..., segment: str = ..., selectAll: bool = ..., shader: bool = ..., sharedNodes: Multiuse[str] = ..., sharedReferenceFile: bool = ..., shortName: bool = ..., strict: bool = ..., swapNamespace: Multiuse[Tuple[str, str]] = ..., type: Queryable[str] = ..., uiConfiguration: bool = ..., uiLoadConfiguration: bool = ..., unloadReference: str = ..., unresolvedName: bool = ..., usingNamespaces: bool = ..., withoutCopyNumber: bool = ..., writable: bool = ...) -> Union[str, bool, Tuple[str, str], Multiuse[Tuple[str, str]]]:
    """This command needs a single main flag that specifies the action to take.
    Some of the main flags also take optional secondary flags to modify
    that action.This command needs a single main query flag that specifies the query to take
    and then optional secondary flags to modify that query.When querying a file name there are a number of ways to format the result:When a file is loaded into Maya (e.g., by opening or referencing it),
    the file path provided may not be complete. It could, for example, be
    a relative path (ex: "scenes/myScene.ma"), it could contain environment
    variables (ex: "$PRODUCTION_DIR/myScene.ma"), and it could even be a path
    which simply doesn't exist on the local disk. In each of these cases Maya
    goes through a number of steps to resolve the path and find the file on disk.
    By default the 'file' command will return the resolved file name (i.e., the
    location from which Maya is actually reading the file), but if theflag is used, the unresolved file (e.g., the one that
    was originally specified) will be returned. When providing a file path with
    an environment variable; for example, when using the -rename flag, the
    environment variable should be set to a relative path ( such as "/scenes/scenesSetA"; ).
    Providing a path using an environment variable that is set to an absolute path
    ( for example, "C:/scenes/" ) is not supported.By default the 'file' command will return the full
    path to a file, but if theflag is used just the
    file name will be returned.When the same file is loaded into Maya more
    than once (for example by referencing the same file twice), Maya
    distinguishes between the various copies by appending a copy number to the
    end of the file name. The first time the file is loaded, no copy number is
    appended. The second time the file is loaded a "{1}" is appended, the third
    time a "{2}" is used, and so on. By default the 'file' command will return
    the file name with the copy number appended, but if theflag is used the file name will be returned
    without the copy number.
    Args:
        absoluteName (bool?): This is a general flag which can be used to specify the desired format for  
                the namespace(s) returned by the command.  
                The absolute name of the namespace is a full namespace path, starting from the root namespace ":"  
                and including all parent namespaces.  For example ":ns:ball" is an absolute namespace  
                name while "ns:ball" is not.  
                Properties: create, query
        activate (bool?): This flag is obsolete.
        activeProxy (bool?): This flag is intended for internal use by Maya during file referencing.  
                It specifes which file is the active proxy when the file is loaded when  
                used with the reference flag. It is also used to specify which file is  
                the active proxy in the file referencing preload information when used  
                with the referenceDepthInfo flag.  
                Properties: create
        add (bool?): When used with selectAll it indicates that the specified items should be  
                added to the active list without removing existing  
                items from the active list.  
                Properties: create
        anyModified (bool?): This flag is obsolete. Please use file -q -modified instead.  
                Properties: query
        applyTo (str?): When importing or referencing an offline edit file, apply it to  
                to the given reference (i.e., determine what <main> gets mapped to).  
                Specify the reference node name as argument. To apply the edits to nodes in  
                the main scene (i.e., the root namespace), pass in ":".  
                To collapse <main> (i.e., map it to "None"), pass in "".  
                May only be used with the file -i/import or -r/reference flags.  
                Properties: create
        buildLoadSettings (bool?): When used with the "o/open" flag it indicates that the specified  
                file should be read for reference hierarchy information only.  
                This information will be stored in temporary load settings under  
                the name "implicitLoadSettings". When this flag is used the  
                specified scene file will not be loaded: no objects/nodes will be  
                created or modified.  
                Note: most users will not need to use this flag or the  
                "implicitLoadSettings" it builds. They can access the same  
                functionality by setting the "Selective Load" option in the  
                File > Open Option Box.  
                Properties: create
        channels (bool?): For use with exportSelected to specify whether attached channels should be included in the export.  
                Properties: create, query
        cleanReference (str?): Remove edits from the passed in reference node.  
                The reference must be in an unloaded state. To remove a particular  
                type of edit, use the editCommand flag. If no flag is specified,  
                all edits will be removed.  
                Properties: create
        command (Queryable[Tuple[str, str]]?): Specifies the callback to execute before any file operation.  
                This is an internal flag used only in the file format.  
                Properties: create, query
        compress (bool?): When used with save, it will compress (gzip) the file on output.  
                Properties: create
        constraints (bool?): For use with exportSelected to specify whether attached constraints should be included in the export.  
                Properties: create, query
        constructionHistory (bool?): For use with exportSelected to specify whether attached construction history should be included in the export.  
                Properties: create, query
        copyNumberList (bool?): When queried, this flag returns a string array containing  
                a number that uniquely identifies each instance the file  
                is used.  
                Properties: query
        defaultExtensions (bool?): Use the default extensions to rename the files. This defaults to true, but  
                is a persistent setting within a given session of Maya, meaning that if  
                you set it to true or false, that value will  
                continue to be used in subsequent file commands until a new value is set.  
                Properties: create, query
        defaultNamespace (bool?): Use the default name space for import and referencing.  This is  
                an advanced option.  If set, then on import or reference, Maya will  
                attempt to place all nodes from the imported or referenced file  
                directly into the root (default) name space, without invoking any  
                name clash resolution algorithms.  If the names of any of the new  
                objects    already exist in the root namespace, then errors will result.  
                The user of this flag is responsible for creating a name clash  
                resolution mechanism outside of Maya to avoid such errors.  
                Note: This flag    is intended only for use with custom file  
                translators written through    the API. Use at your own risk.  
                Properties: create
        deferReference (bool?): When used in conjunction with the -reference flag, this  
                flag determines if the reference is loaded, or if loading is  
                deferred.  
                C: The default is false.  
                Q: When queried, this flag returns true if the reference is deferred,  
                or false if the reference is not deferred. If this is used  
                with -rfn/referenceNode, the -rfn flag must come before -q.  
                Properties: create, query
        editCommand (str?): For use with cleanReference. Remove only this type of edit.  
                Supported edits are: setAttr addAttr deleteAttr connectAttr  
                disconnectAttr and parent  
                Properties: create
        errorStatus (bool?): Query the error status of the last file read. Returns true if and error occurred during the last file read.  
                Properties: query
        executeScriptNodes (bool?): If true, allow the appropriate script nodes to execute. If false,  
                do not allow any script node scripts to run.  
                For more information, see the documentation for script nodes.  
                Default: true.  
                Properties: create
        exists (bool?): Query if the file exists. Returns true if the file exists.  
                Properties: query
        expandName (bool?): This is a query only flag that can be used to query for the  
                file path name of the file.  
                Properties: query
        exportAll (bool?): Export everything into a single file.  
                Returns the name of the exported file.  
                Properties: create
        exportAnim (bool?): Export all animation nodes and animation helper nodes from all objects in the  
                scene.  
                The resulting animation export file will contain connections to objects that are  
                not included in the animation file. As a result, importing/referencing this file  
                back in will require objects of the same name to be present, else errors will occur.  
                The -sns/swapNamespace flag is available for swapping the namespaces of given objects  
                to another namespace. This use of namespaces can be used to re-purpose the animation  
                file to multiple targets using a consistent naming scheme.  
              
                The exportAnim flag will not export animation layers. For generalized file export of  
                animLayers and other types of nodes,  
                refer to the exportEdits command. Or  
                use the Export Layers functionality.  
                Properties: create
        exportAnimFromReference (bool?): Export the main scene animation nodes and animation helper nodes from all referenced  
                objects. This flag, when used in conjunction with the -rfn/referenceNode flag,  
                can be constrained to only export animation nodes from the specified reference  
                file. See -ean/exportAnim flag description for details on usage of animation files.  
                Properties: create
        exportAsReference (bool?): Export the selected objects into a reference file with the given  
                name. The file is saved on disk during the process.  
                Returns the name of the reference created.  
                Properties: create
        exportAsSegment (bool?): This flag is obsolete.
        exportSelected (bool?): Export the selected items into the specified file.  
                Returns the name of the exported file.  
                Properties: create
        exportSelectedAnim (bool?): Export all animation nodes and animation helper nodes from the selected objects  
                in the scene. See -ean/exportAnim flag description for details on usage of animation  
                files.  
                Properties: create
        exportSelectedAnimFromReference (bool?): Export the main scene animation nodes and animation helper nodes from the selected  
                referenced objects. This flag, when used in conjunction with the -rfn/referenceNode  
                flag, can be constrained to only export animation nodes from the selected nodes  
                of a specified reference file. See -ean/exportAnim flag description for details on  
                usage of animation files.  
                Properties: create
        exportSelectedNoReference (bool?): This flag is obsolete.
        exportSelectedStrict (bool?): Export the selected items into the specified file. This flag differs from exportSelected  
                in that it will only export the nodes that are explicitly on the selection list. Related  
                nodes (both history and DAG related) are not automatically exported unless those nodes  
                are also on the selection list. Node relationships are only preserved if both nodes in the  
                relationship (parent/child, source/destination) are exported.  
                It is important to note that there is potential for scene data loss in the exported  
                scene since not all related nodes are not exported by default. The user is responsible for  
                selecting all relevant nodes before exporting.  
                Returns the name of the exported file.  
                Properties: create
        exportSnapshotCallback (Tuple[Callable[..., Any], str]?): When specified alongside -ea/exportAll, es/exportSelected and -ess/exportSelectedStrict,  
                this flag enables Maya to temporarily duplicate the export targets into a specified  
                namespace and invoke a callback to interact with the duplicate export targets before  
                writing the duplicate export targets to disk. Once written to disk, the duplicate  
                export targets, new nodes created by the callback and temporary namespace are removed  
                from the scene. Implicitly created nodes (eg. persp, top, etc.) are not duplicated.  
              
                For the duration of the callback:  
                1. The specified namespace will be made current.  
                2. All nodes added by the callback are tracked as a temporary export target.  
                3. Although the intent of the callback is to only operate on the duplicate export  
                targets, there is nothing limiting the callback from modifying the main scene.  
                Thus, the callback should be written with care.  
              
                This flag accepts two arguments:  
                a. [string] Callback to invoke prior to write to disk.  
                b. [string] Temporary namespace to store duplicate export targets.  
              
                This flag can only be used in conjunction with -ea/exportAll, -es/exportSelected and  
                -ess/exportSelectedStrict.  
              
                Note that the -pv/preview flag still only previews the contents of the export targets  
                _prior_ to the snapshot duplication. It does not preview the final output after the  
                callback.  
              
                Referenced nodes are duplicated in the same manner as duplicating those nodes  
                manually in the scene. Similarly, scene assembly nodes will duplicate as they would  
                if manually duplicated, however scene assembly nodes have special duplication  
                behavior, so the callback should be aware of these differences when anticipating  
                the duplicate export targets.  
                Properties: create
        exportUnloadedReferences (bool?): Only effective when preserveReferences is used.  
                When used with the exportAll flag, tells the exporter to  
                include all unloaded references in the export.  
                When used with the exportSelected flag, tells the exporter to  
                include all unloaded proxy references that are related to  
                any node in the selection.  
                Properties: create
        expressions (bool?): For use with exportSelected to specify whether attached expressions should be included in the export.  
                Properties: create, query
        fileMetaData (bool?): This is a query only flag to get the file metadata for audio files. It returns the referenceTime. This field is only extracted from BWAVE files,  
                for other files it returns 0  
                Properties: query
        flushReference (str?): This flag will unload the reference file associated with the  
                passed reference node, retaining all associated reference nodes  
                and scene files. ** This option only works when using namespaces **.  
                More Details: This flag is primarily intended to be  
                used as part of a custom asset management system. It can be used to  
                defer loading of a reference which contains child references without  
                losing information about those child references. Prior to reloading a  
                flushed    reference which contains child references, the  
                'createNode reference' lines should be manually removed from the  
                children's Maya ASCII files. If this is not done, extra reference  
                nodes will be created.  
                Properties: create
        force (bool?): Force an action to take place.  
                (new, open, save, remove reference, unload reference)  
                Used with removeReference to force remove reference namespace even if it has contents.  
                Cannot be used with removeReference if the reference resides in the root namespace.  
                Used with unloadReference to force unload reference even if the reference node is locked,  
                without prompting a dialog that warns user about the lost of edits.  
                Properties: create
        groupLocator (bool?): Used only with the -r and the -gr flag.  
                Used to group the output of groupReference under a locator  
                Properties: create
        groupName (str?): Used only with the -gr flag.  
                Optionally used to set the name of the transform node that the imported/referenced  
                items will be grouped under.  
                Properties: create
        groupReference (bool?): Used only with the -r or the -i flag.  
                Used to group all the imported/referenced items under a single transform.  
                Properties: create
        ignoreVersion (bool?): Used to open files with versions other than those officially supported.  
                Success is not guaranteed. Data loss, data corruption or failure to open are all possible outcomes.  
                Can only be used with the -o and -i flags.  
                Properties: create
        i (bool?): Import the specified file.  
                Returns the name of the imported file.  
                Properties: create
        importFrameRate (bool?): Used only with the -i flag.  
                Used to import the frame rate and set it as Maya's frame rate.  
                Properties: create
        importReference (bool?): Remove the encapsulation of the reference around the data within  
                the specified file.    This makes the contents of the specified file  
                part of the current scene and all references to the original file  
                are lost.  
                Returns the name of the reference that was imported.  
                Properties: create
        importTimeRange (str?): Used only with the -i flag.  
                Used to import the time range and apply it to Maya's playback range in one  
                of three different ways as specified by the string.  The valid strings are  
                "keep", which keeps Maya's playback range untouched, "override", which overrides  
                Maya's playback range with the imported range, and "combine", which extends Maya's  
                playback range to encompass the imported range.  
                Properties: create
        lastFileOption (bool?): On query, returns the last option string used by the file command.  
                Properties: query
        lastTempFile (bool?): When queried, this flag returns the temp file name used during  
                file save. The temp file will be left in the same directory  
                as the intended file name if the save fails.  
                Properties: query
        list (bool?): List all files.  
                Returns a string array of the names of all segment/reference files.  
                Duplicates will be removed. So if a file is referenced more than  
                once, and the -withoutCopyNumber flag is set, it will only be listed once.  
                in the scene.  
                Properties: query
        loadAllDeferred (bool?): This flag is obsolete, and has been replaced by  
                the loadReferenceDepth flag. When used with the -open flag, determines  
                if the -deferReference flag is respected when reading in the file. If  
                true is passed, all of the references are loaded. If false is passed,  
                the -deferReference flag is respected.  
                Properties: create
        loadAllReferences (bool?): This flag is obsolete and has been replaced with the  
                loadReferenceDepth flag. When used with the -open flag,  
                this will cause all references to be loaded.  
                Properties: create
        loadNoReferences (bool?): This flag is obsolete and has been replaced witht the  
                loadReferenceDepth flag. When used with the -open flag,  
                no references will be loaded. When used with -i/import,  
                -r/reference or -lr/loadReference flags, will load the  
                top-most reference only.  
                Properties: create
        loadReference (Queryable[str]?): This flag loads a file and associates it with the passed reference  
                node. If the reference node does not exist, the command will fail. If  
                the file is already loaded, then this flag will reload the same file.  
                If a file is not given, the command will load (or reload) the last used  
                reference file.  
                Properties: create, query
        loadReferenceDepth (str?): Used to specify which references should be loaded. Valid types are  
                "all", "none" and "topOnly", which will load all references,  
                no references and top-level references only, respectively. May only be used  
                with the -o/open, -i/import, -r/reference or -lr/loadReference flags.  
                When "none"  
                is used with -lr/loadReference, only path validation is performed. This  
                can be used to replace a reference without triggering reload. Not using  
                loadReferenceDepth will load references in the same loaded or  
                unloaded state that they were in when the file was saved.  
                Additionally, the -lr/loadReference flag supports a fourth type, "asPrefs".  
                This will force any nested references to be loaded according to the  
                state (if any) stored in the current scene file, rather than according to the  
                state saved in the reference file itself.  
                Properties: create
        loadReferencePreview (str?): This flag will perform a special preview-only load of a reference file.  
                A preview-only reference file is not completely loaded, but instead is  
                partially loaded so that certain information, such as nested references  
                it contains, can be determined.  
                Nested references that are previewed remain in a special preview-only state.  
                Properties: create
        loadSettings (str?): When used with the "o/open" flag this flag specifies which reference  
                load settings should be used. Reference load settings specify which  
                references should be brought in loaded and which unloaded. Those  
                reference files that are brought in unloaded will usually not need  
                to be read and interpreted by Maya. This can potentially reduce the  
                time it takes Maya to load the whole scene.  
                If no "ls/loadSettings" flag is specified, or the empty string ("") is  
                used as the flag argument, the default load settings are used. The  
                default load settings represent the state of all references when the file  
                was last saved. The load settings "implicitLoadSettings" refer to the  
                temporary load settings generated by the "bls/buildLoadSettings" flag and  
                edited with the "loadSettings" command.  
                Currently on the default and implicit load settings are supported.  
                Properties: create
        location (bool?): Query the location of the given file name.  
                Properties: query
        lockContainerUnpublished (bool?): Set the unpublised lock state for all containers in this file. This will not lock  
                the attributes in the main scene directly, but any file that references this scene  
                will have all its containers come in as unpublished locked.  
                Properties: create
        lockFile (bool?): Lock or unlock the main scene. Any file referencing this scene will  
                automatically lock all attributes and nodes. Also prevents reference  
                edits from being saved to it from a parent file.  
                Properties: create
        lockReference (bool?): Locks attributes and nodes from the referenced file.  
                Properties: create
        mapPlaceHolderNamespace (Queryable[Multiuse[Tuple[str, str]]]?): Map a placeHolderNamespace to the given reference. Must be  
                used with the file -i/import, -r/reference flags in create mode.  
                The first string is the place holder namespace, including the angle  
                brackets (ex: "<foo>"). The second string is the reference node  
                whose namespace it should be mapped to (ex: "refRN"). If the namespace  
                should be mapped to the root namespace, use ":".  
                To collapse the namespace (i.e., map it to "None"), use "".  
                When queried, namespaces that are mapped to "None" will return "(None)" for clarity.  
                Properties: create, query, edit, multiuse
        mergeBaseAnimLayer (bool?): When set, Maya will merge the base animation layer imported from the file with  
                the base layer already existing in the scene.  
                Properties: create
        mergeNamespaceWithParent (bool?): Used with the removeReference flag.  
                When removing a file reference and its namespace, move the rest of the namespace  
                content to parent namespace.  
                Cannot be used if the reference resides in the root namespace.  
                Properties: create
        mergeNamespaceWithRoot (bool?): Used with the removeReference flag.  
                When removing a file reference and its namespace, move the rest of the namespace  
                content to root namespace.  
                Cannot be used if the reference resides in the root namespace.  
                Properties: create
        mergeNamespacesOnClash (bool?): Used with the import, reference or edit flags, this option will prevent new namespaces  
                from being created when namespaces of the same name already exist within Maya.  
                The default value is false.  
                For example, if an object "pSphere1", which is being imported, refers to the  
                namespace "ref" and there is already a namespace called "ref" defined in Maya.  
                If mergeNamespacesOnClash is true, the existing "ref" namespace will be reused  
                and pSphere1 will be moved into the existing namespace; and if the namespace has  
                another object which is also named "pSphere1", then the imported one will be  
                renamed with an incremental number("pSphere2"). On the other hand, if  
                mergeNamespacesOnClash is false, a new namespace will be created with an incremental  
                number (in first case is "ref1") and pSphere1 will be moved into the "ref1" namespace.  
                This flag also support nested namespace, for example, if an object "pSphere1" which is  
                imported and refers to namespace "ref:foo" and mergeNamespacesOnClash  
                is true this time, then the existing "ref:foo" will be reused and the object will be  
                moved into "ref:foo". Also if mergeNamespacesOnClash is false, then a new namespace  
                "ref:foo1" will be created and "pSphere1" will be moved into that new namespace.  
                Properties: create
        modified (bool?): Set the modified state of the entire scene. If the scene is modified  
                it will need to be saved before a new file is opened or created.  
                Normally there is no need to edit this flag as the state of the file  
                is updated automatically whenever an object is created or modified.  
                If editing of the state is desired, it is done without use of  
                the edit flag as covered in the example section below.  
                In query mode, if the scene has been modified 1 is returned. Otherwise 0  
                is returned.  
                Properties: create, query
        moveSelected (bool?): This flag is obsolete.  
                Properties: edit
        namespace (str?): The namespace name to use that will group all objects during  
                importing and referencing.  
                Change the namespace used to group all the objects from  
                the specified referenced file. The reference must have been created  
                with the "Using Namespaces" option, and must be loaded. Non-referenced  
                nodes contained in the existing namespace will also be moved to the new  
                namespace. The new namespace will be created by this command and can  
                not already exist. The old namespace will be removed.  
                Properties: edit
        newFile (bool?): Initialize the scene.  
                Returns untitled scene with default location.  
                Properties: create
        open (bool?): Open the specified file.  
                Returns the name of the opened file.  
                Properties: create
        options (Queryable[str]?): Set/query the currently set file options.  
                file options are used while saving a maya file.  
                Two file option flags supported in current file command are v and p.  
              
                v(verbose) indicates whether long or short attribute names and command flags names are used  
                when saving the file. Used by both maya ascii and maya binary file formats.  
                It only can be 0 or 1.  
                Setting v=1 indicates that long attribute names and command flag names will be used.  
                By default, or by setting v=0, short attribute names will be used.  
              
              
                p(precision) defines the maya file IO's precision when saving the file. Only used by maya ascii file format.  
                It is an integer value. The default value is 17.  
              
                The option format is "flag1=XXX;flag2=XXX".Maya uses the last v and p as the final result.  
                Note:  
                1. Use a semicolon(";") to separate several flags.  
                2. No blank space(" ") in option string.  
                Properties: create, query
        parentNamespace (bool?): Returns the name(s) of a referenced file's parent namespaces.  
                Properties: query
        postSaveScript (str?): When used with the save flag, the specified script will be executed  
                after the file is saved.  
                Properties: create
        preSaveScript (str?): When used with the save flag, the specified script will be executed  
                before the file is saved.  
                Properties: create
        preserveName (bool?): When used with compress, it will retain the regular extension rather than appending .gz.  
                Properties: create
        preserveReferences (bool?): Modifies the various import/export flags such that  
                references are imported/exported as actual references  
                rather than copies of those references.  
                Properties: create
        preview (bool?): Used in conjunction with any of the -exportXXX flags, causes Maya  
                to return a list of the nodes that would be exported, without  
                actually writing the exported file to disk.  
                Properties: create
        prompt (bool?): This flag controls the display of file prompting dialogs.  
                Some examples of file prompting dialogs include error  
                messages that require user confirmation and missing file  
                reference dialogs. Once this flag is used, every instance  
                of the file command will use the last set value of this flag.  
                Some interactive file operations may post dialogs even when  
                the flag is set to false, but every scripted file command  
                will not display any dialogs when this flag is set to  
                false.  The default value is true.  
                Properties: create, query
        proxyManager (str?): When a one or more proxy references are added to an existing file reference,  
                the proxy manage node is used to define the proxies associated with that  
                reference. This flag is used in conjunction with the activeProxy and proxyTag  
                flag to specify the proxyManager of interest. This flag is also used to  
                specify the proxyManager for a proxy reference in the file referencing  
                preload information, when used in conjunction with the referenceDepthInfo flag.  
                Properties: create
        proxyTag (str?): This flag is intended for internal use only during file load or preload.  
                Proxy tags are names you assign to proxy references to more easily  
                manage the proxy references from the reference editor. Proxy tags are  
                unique within a given proxy set.  
                This flag must be  used in conjunction with the proxyManager flag.  
                Properties: create
        reference (bool?): Create a reference to the specified file. Returns the  
                name of the file referenced.  
                Query all file references from the specified file.  
                Properties: query
        referenceDepthInfo (int?): This flag is used to store reference loading preferences  
                associated with a Maya ascii file (.ma). This flag is only useful  
                during file I/O so users should not have any need to use this flag.  
                Properties: create
        referenceNode (Queryable[str]?): This flag is only used during queries. In MEL, if it appears before -query  
                then it must be followed by the name of one of the scene's reference  
                nodes. That will determine the reference to be queried by whatever flags  
                appear after -query. If the named reference node does not exist within  
                the scene the command will fail with an error.  
              
                In Python the equivalent behavior is obtained by passing the name of the  
                reference node as the flag's value.  
              
                In MEL, if this flag appears after -query then it takes no argument and will  
                cause the command to return the name of the reference node associated with the  
                file given as the command's argument. If the file is not a reference or  
                for some reason does not have a reference node (e.g., the user deleted it)  
                then an empty string will be returned. If the file is not part of the  
                current scene then the command will fail with an error.  
              
                In Python the equivalent behavior is obtained by passing True as the flag's  
                value.  
                      In query mode, this flag can accept a value.  
                Properties: query
        relativeNamespace (str?): This flag can be used with the exportSelected, exportSelectedStrict and exportAll operations to specify  
                that the nodes in the exported file are to be written out relative to a specified  
                namespace. This provides the ability to remove undesired levels of namespacing from  
                the node names as they are exported. The relativeNamespace value specifies the  
                namespace to use as the relative root for the exported nodes, and must be specified  
                as an absolute namespace. Nodes in the exported file not residing within the specified  
                relative namespace will be written out using absolute namespace names.  
                Note: this flag cannot be used in conjunction with the preserveReferences flag.  
                Properties: create
        removeDuplicateNetworks (bool?): When set, Maya will remove imported networks if the same network is also  
                detected in the current scene. You can explicitly specify that certain types of  
                networks be exempted from removal by this flag. For example, if you set to the  
                optionVar removeDuplicateShadingNetworksOnImport to 0 (or disable the option  
                Remove Duplicate Shading Networks from the File > Import options), then shading  
                networks will be exempted from removal by this flag.This flag can only be used  
                in conjunction with the -i/import flag.  
                Properties: create
        removeReference (bool?): Remove the given file reference from its parent. This will also  
                Remove everything this file references.  
                Returns the name of the file removed.  
                If the reference is alone in its namespace, remove the namespace.  
                If there are objects remaining in the namespace after the file reference is removed,  
                by default, keep the remaining objects in the namespace.  
                To merge the objects remaining in the namespace to the parent or root  
                namespace, use flags mergeNamespaceWithParent  
                or mergeNamespaceWithRoot. The empty file reference namespace is then removed.  
                To forcibly delete all objects, use flag force. The empty file reference namespace is then removed.  
                Properties: create
        rename (str?): Rename the scene.  
                Used mostly during save to set the saveAs name.  
                Returns the new name of the scene.  
                Properties: create
        renameAll (bool?): If true, rename all newly-created  
                nodes, not just those whose names clash with existing nodes.  
                Only available with -i/import.  
                Properties: create
        renameToSave (bool?): If true, the scene will need to be renamed before it can be  
                saved. When queried this flag returns true if the scene must be  
                renamed before it can be saved.   
                The default is false.  
                Properties: create, query
        renamingPrefix (Queryable[str]?): The string to use as a prefix for all objects from this file.  
                This flag has been replaced by -ns/namespace.  
                Properties: create, query
        renamingPrefixList (bool?): This flag returns a list of all of the renaming prefixes used  
                by the file.  
                Properties: query
        replaceName (Queryable[Multiuse[Tuple[str, str]]]?): Define a search and replace string. Will apply search and replace to  
                leaf node names. The search string can include namespaces and wild-cards,  
                but will only apply to leaf nodes in a dag hierarchy. Intended for use  
                with offline edits files. May only be used with file -i/import  
                or -r/reference. If a nested reference also defines a substitution, it  
                will become the active substitution table while loading the nested reference.  
                Note: if used with the -e/edit flag, the replacement will only be applied  
                the next time the reference is loaded  
                Examples: -replace "*pCube1" "prop" will change "foo:pCube1" to  
                "foo:prop" and "|A:pCube1|B:pCube1" to "|A:pCube1|prop".  
                Properties: create, query, edit, multiuse
        reserveNamespaces (bool?): When this flag is enabled namespaces for unloaded references will be  
                created after loading the file to reduce the chances of unexpected  
                namespace collisions when loading or adding references later on.  
                Properties: create
        resetError (bool?): Turn off any pre-existing global file errors.  
                Properties: create
        returnNewNodes (bool?): Used to control the return value in open, import, loadReference,  
                and reference operations. It will force the file command to return  
                a list of new nodes added to the current scene.  
                Properties: create
        save (bool?): Save the specified file.  
                Returns the name of the saved file.  
                Properties: create
        saveDiskCache (Queryable[str]?): This flag sets the saveAs option for Jiggle disk caches.  
                The valid inputs are "always" - always copy a file texture to a  
                new location, "never" - do not copy at all.   
                C: The default is "always".   
                Q: When queried it returns a string ("always", "never").  
                Properties: create, query
        saveReference (bool?): Save reference node edits and connections to reference file.  
                This includes newly added history and animation, provided that  
                these do not apply to any objects outside the reference being saved.  
                Properties: create
        saveReferencesUnloaded (bool?): This flag can only be used in conjunction with the save flag. It specifies  
                that the saved file will be saved with all references unloaded.  
                Properties: create
        saveTextures (Queryable[str]?): This flag sets the saveAs option for 3d Paint file textures.  
                The valid inputs are "always" - always copy a file texture to a  
                new location, "unlessRef" - copy only if this is not a referenced  
                file texture, "never" - do not copy at all.   
                C: The default is "unlessRef".   
                Q: When queried it returns a string ("always", unlessRef", "never").  
                Properties: create, query
        sceneName (bool?): return the name of the current scene.  
                Properties: query
        segment (str?): This flag is obsolete.
        selectAll (bool?): Select all the components of this file as well as its child  
                files.  Note that the file specified must be one that is  
                already opened in this Maya session.  
                The default behavior is to replace the existing selection.  
                Use with the "add" flag to keep the active selection list.  
                Properties: create
        shader (bool?): For use with exportSelected to specify whether attached shaders should be included in the export.  
                Properties: create, query
        sharedNodes (Multiuse[str]?): This flag modifies the '-r/reference' flag to indicate that  
                certain    types of nodes within that reference should be treated as  
                shared nodes. All shared nodes will be placed in the default  
                namespace. New copies of those nodes will not be created if a copy  
                already exists in the default namespace, instead the shared node  
                will be merged with the    existing node. The specifics of what  
                happens when two nodes are merged depends on the node type. In  
                general attribute values will not be merged, meaning the values set  
                on any existing shared nodes will be retained, and the values of  
                the nodes being merged in will be ignored.  
                The valid options are "displayLayers", "shadingNetworks",  
                "renderLayersByName", and "renderLayersById". This flag is  
                multi-use; it may be specified multiple times to for  
                example, share both display layers and shading networks.  
                Two shading networks will only be merged if    they are identical:  
                the network    of nodes feeding into the shading group must be  
                arranged identically with equivalent nodes have the same name and  
                node type. Additionally if a network is animated or contains a DAG  
                object or expression it will not be mergeable.  
                This flag cannot be used in conjunction with -srf/sharedReferenceFile.  
                Properties: create, multiuse
        sharedReferenceFile (bool?): Can only be used in conjunction with the -r/reference flag and  
                the -ns/namespace flag (there is no prefix support). This flag modifies  
                the '-r/reference' flag to indicate that all nodes within that  
                reference should be treated as shared nodes. New copies    of  
                those nodes will not be created if a copy already exists. Instead,  
                the shared node will be merged with the existing node. The specifics of  
                what happens when two nodes are merged depends on the node type.  
                This flag cannot be used in conjunction with -shd/sharedNodes.  
                Properties: create
        shortName (bool?): When used with a main query flag it indicates that the file name  
                returned will be the short name (i.e., just a file name without  
                any directory paths). If this flag is not present, the full name  
                and directory path will be returned.  
                Properties: query
        strict (bool?): Set strict file path resolution. If true, all paths will be matched  
                exactly, both relative and absolute. Relative paths will be considered  
                relative to the project root directory. May only be used with the -o/open,  
                -i/import, -ir/importReference or -r/reference flags.  
                Properties: create
        swapNamespace (Multiuse[Tuple[str, str]]?): Can only be used in conjunction with the -r/reference or -i/import  
                flags. This flag will replace any occurrences of a given namespace to  
                an alternate specified namespace. This namespace "swap" will occur  
                as the file is referenced in. It takes in two string arguments. The  
                first argument specifies the namespace to replace. The second argument  
                specifies the replacement namespace. Use of this flag, implicitly  
                enables the use of namespaces and cannot be used with deferReference.  
                Properties: create, multiuse
        type (Queryable[str]?): Set the type of this file.  By default this can be any one of:  
                "mayaAscii", "mayaBinary", "mel",  "OBJ", "directory", "plug-in", "audio", "move", "EPS", "Adobe(R) Illustrator(R)", "image"  
                plug-ins may define their own types as well.  
                Return a string array of file types that match this file.  
                Properties: create, query
        uiConfiguration (bool?): Save the ui configuration with the scene in a uiConfiguration  
                script node. (eg. panes, etc.)  
                The current default is on and is set in initialStartup.mel.  
                Properties: create, query
        uiLoadConfiguration (bool?): Load the scene's ui configuration. (eg. panes, etc.)  
                The current default is on and is set in initialStartup.mel.  
                Properties: create, query
        unloadReference (str?): This flag will unload the reference file associated with the  
                passed reference node.  
                Properties: create
        unresolvedName (bool?): When used with a main query flag it indicates that the file name  
                returned will be unresolved (i.e., it will be the path originally  
                specified when the file was loaded into Maya; this path may  
                contain environment variables and may not exist on disk). If this  
                flag is not present, the resolved name will be returned.  
                Properties: query
        usingNamespaces (bool?): Returns boolean.  
                Queries whether the specified reference file uses namespaces  
                or renaming prefixes.  
                Properties: query
        withoutCopyNumber (bool?): When used with a main query flag it indicates that the file name  
                returned will not have a copy number appended to the end. If this  
                flag is not present, the file name returned may have a copy number  
                appended to the end.  
                Properties: query
        writable (bool?): Query whether the given file is writable in the current scene. For  
                main scene files this indicates writable to the file system by the  
                current user. Files referenced by the main scene file are always not  
                writable (referenced files are by nature read only). Files not present  
                in the current scene always return false.  
                Properties: query

    Returns:
        str: The name of the specified file for most actions. When the returnNewNodes flag is used, an array of strings will be returned indicating the names of the nodes that were read.

    Example:
    """

