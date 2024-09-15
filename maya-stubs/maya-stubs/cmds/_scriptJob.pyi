from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def scriptJob(*, allChildren: bool = ..., attributeAdded: Tuple[str, Callable[..., Any]] = ..., attributeChange: Tuple[str, Callable[..., Any]] = ..., attributeDeleted: Tuple[str, Callable[..., Any]] = ..., compressUndo: bool = ..., conditionChange: Tuple[str, Callable[..., Any]] = ..., conditionFalse: Tuple[str, Callable[..., Any]] = ..., conditionTrue: Tuple[str, Callable[..., Any]] = ..., connectionChange: Tuple[str, Callable[..., Any]] = ..., disregardIndex: bool = ..., event: Tuple[str, Callable[..., Any]] = ..., exists: int = ..., force: bool = ..., idleEvent: Callable[..., Any] = ..., kill: Multiuse[int] = ..., killAll: bool = ..., killWithScene: bool = ..., listConditions: bool = ..., listEvents: bool = ..., listJobs: bool = ..., nodeDeleted: Tuple[str, Callable[..., Any]] = ..., nodeNameChanged: Tuple[str, Callable[..., Any]] = ..., optionVarChanged: Tuple[str, Callable[..., Any]] = ..., parent: str = ..., permanent: bool = ..., protected: bool = ..., replacePrevious: bool = ..., runOnce: bool = ..., timeChange: Callable[..., Any] = ..., uiDeleted: Tuple[str, Callable[..., Any]] = ...) -> Union[int, List[str], None, bool]:
    """This command creates a "script job", which is a MEL command
    or script.  This job is attached to
    the named condition, event, or attribute. Each time the condition
    switches to the desired state (or the trigger is triggered, etc),
    the script is run.Script jobs are tied to the event loop in the interactive application.
    They are run during idle events.  This means that script jobs do not
    exist in the batch application.  The scriptJob command does nothing
    in batch mode.This triggering happens very frequently so for speed considerations
    no events are forwarded during playback.  This means that you cannot
    useto alter animation behaviour.
    Use an expression instead, or the rendering callbacks "preRenderMel"
    and "postRenderMel".When setting up jobs for conditions, it is invalid to setup jobs for
    the true state, false state, and state change at the same time.  The
    behaviour is undefined.  The user can only setup jobs for the true
    and/or false state, or only for the state change, but not three at
    the same time. i.e. if you do:This command can also be used to list available conditions
    and events, and to kill running jobs.
    Args:
        allChildren (bool?): This flag can only be used in conjunction with  
                the -ac/attributeChange flag.  If it is specified, and the job  
                is attached to a compound attribute, then the  
                job will run due to changes to the specified attribute  
                as well as changes to its children.  
                Properties: create
        attributeAdded (Tuple[str, Callable[..., Any]]?): Run the script when the named attribute is added.  
                The string must identify both the dependency node and the  
                particular attribute.  If the dependency node is deleted,  
                this job is killed (even if the deletion is undoable).  
                Properties: create
        attributeChange (Tuple[str, Callable[..., Any]]?): Run the script when the named attribute changes value.  
                The string must identify both the dependency node and the  
                particular attribute.  If the dependency node is deleted,  
                this job is killed (even if the deletion is undoable).  
                Properties: create
        attributeDeleted (Tuple[str, Callable[..., Any]]?): Run the script when the named attribute is deleted.  
                The string must identify both the dependency node and the  
                particular attribute.  If the dependency node is deleted,  
                this job is killed (even if the deletion is undoable).  
                Properties: create
        compressUndo (bool?): If this is set to true, and the scriptJob is undoable, then  
                its action will be bundled with the last user action for undo  
                purposes.  For example; if the scriptJob was triggered by a selection  
                change, then pressing undo will undo both the scriptJob and the  
                selection change at the same time.  
                Properties: create
        conditionChange (Tuple[str, Callable[..., Any]]?): Run the script when the named condition changes state.  
                The string must be the name of a pre-defined, or a  
                user-defined boolean condition.  To get a list of what  
                conditions exist, use the -listConditions flag.  
                Properties: create
        conditionFalse (Tuple[str, Callable[..., Any]]?): Run the script when the named condition becomes false.  
                The string must be the name of a pre-defined, or a  
                user-defined boolean condition.  To get a list of what  
                conditions exist, use the -listConditions flag.  
                Properties: create
        conditionTrue (Tuple[str, Callable[..., Any]]?): Run the script when the named condition becomes true.  
                The string must be the name of a pre-defined, or a  
                user-defined boolean condition.  To get a list of what  
                conditions exist, use the -listConditions flag.  
                Properties: create
        connectionChange (Tuple[str, Callable[..., Any]]?): Run the script when the named attribute changes its  
                connectivity.  The string must identify both the dependency  
                node and the particular attribute.  If the dependency node  
                is deleted, this job is killed (even if the deletion is undoable).  
                Properties: create
        disregardIndex (bool?): This flag can only be used in conjunction with  
                the -ac/attributeChange flag.  If it is specified, and the job  
                is attached to a multi (indexed) attribute, then the  
                job will run no matter which attribute in the multi changes.  
                Properties: create
        event (Tuple[str, Callable[..., Any]]?): Run the script when the named event occurs.  This string  
                must be the name of a pre-defined maya event.  To get a list  
                of what events exist, use the -listEvents flag.  
                Properties: create
        exists (int?): Returns true if a scriptJob with the specified "job  
                number" exists, and false otherwise. The "job number"  
                should be a value that was returned on creation of a new  
                scriptJob.  
                Properties: create
        force (bool?): This flag can only be used with -kill, -killAll,  
                or -replacePrevious. It enables the deletion of protected jobs.  
                Properties: create
        idleEvent (Callable[..., Any]?): Run the script every time maya is idle.  WARNING,  
                as long as an idle event is is registered, the application  
                will keep calling it and will use up all available CPU time.  
                Use idleEvents with caution.  
                Properties: create
        kill (Multiuse[int]?): Kills the job with the specified job number. Permanent jobs  
                cannot be killed, however, and protected jobs can only be killed  
                if the -force flag is used in the command.  
                Properties: create, multiuse
        killAll (bool?): Kills all jobs. Permanent jobs will not be deleted, and  
                protected jobs will only be deleted if the -force flag is used.  
                Properties: create
        killWithScene (bool?): Attaches the job to the current scene, and when the scene is  
                emptied. The current scene is emptied by opening a new or  
                existing scene.  
                Properties: create
        listConditions (bool?): This causes the command to return a string array containing  
                the names of all existing conditions.  Below is the descriptions  
                for all the existing conditions:  
                Events Based on Available Maya Features  
                These events are true when the given feature is available.  
              
                Event Name  
                 Maya Feature  
                AnimationExists  
                 Animation   
                AnimationUIExists  
                User Interface for Animation  
                BaseMayaExists  
                 Any Basic Maya   
                BaseUIExists  
                 Any Interactive Maya  
                DatabaseUIExists  
              
                DeformersExists  
                 Deformer Functions   
                DeformersUIExists  
                User Interface for Deformers  
                DevicesExists  
                Device Support  
                DimensionsExists  
                Dimensioning  
                DynamicsExists  
                 Dynamics   
                DynamicsUIExists  
                User Interface for Dynamics  
                ExplorerExists  
                 Explorer   
                ImageUIExists  
                User Interface for Imaging  
                KinematicsExists  
                 Kinematics   
                KinematicsUIExists  
                User Interface for Kinematics  
                ManipsExists  
                Manipulators  
                ModelExists  
                 Basic Modeling Tools  
                ModelUIExists  
                User Interface for Basic Modeling  
                NurbsExists  
                 Nurbs Modeling Tools  
                NurbsUIExists  
                User Interface for Nurbs Modeling  
                PolyCoreExists  
                Basic Polygonal Support  
                PolygonsExists  
                 Polygonal Modeling   
                PolygonsUIExists  
                User Interface for Polygonal Modeling  
                PolyTextureExists  
                 Polygonal Texturing   
                RenderingExists  
                 Built-in Rendering   
                RenderingUIExists  
                User Interface for Rendering  
              
              
                Other Events  
                 autoKeyframeState:  
                true when Maya has autoKeyframing enabled  
                busy:  
                true when Maya is busy.  
                deleteAllCondition:  
                true when in the middle of a delete-all operation  
                flushingScene:  
                true while the scene is being flushed out  
                GoButtonEnabled:  
                true when the Go button in the panel context is enabled.   
                hotkeyListChange:  
                true when the list of hotkey definitions has changed  
                playingBack:  
                true when Maya is playing back animation keyframes.  
                playbackIconsCondition:  
                instance of the playingBack condition used on the  
                time slider  
                readingFile:  
                true when Maya is reading a file.  
                RedoAvailable:  
                true when there are commands available for redo.   
                SomethingSelected:  
                true when some object(s) is selected.  
                UndoAvailable:  
                true when there are commands available for undo.  
                Properties: create
        listEvents (bool?): This causes the command to return a string array containing  
                the names of all existing events.  Below is the descriptions  
                for all the existing events:  
              
                angularToleranceChanged:  
                when the tolerance on angular units is changed.  
                This tolerance can be changed by:  
                 using the MEL command, "tolerance" with the "-angular" flag  
                 changing the pref under Options->GeneralPreferences->  
                Modeling tab->Tangential Tolerance  
              
                angularUnitChanged:  
                when the user changes the angular unit.  
                axisAtOriginChanged:  
                when the axis changes at the origin.  
                  axisInViewChanged:  
                when the axis changes at a particular view.  
                ColorIndexChanged:  
                when the color index values change.  
                constructionHistoryChanged:   
                when construction history is turned on or off.  
                currentContainerChanged:   
                when the user set or unset the current container.  
                currentSoundNodeChanged:  
                whenever the sound displayed in the time slider changes  
                due to:  
                 the sound being removed (or no longer displayed)  
                [RMB in the time slider]  
                a new sound being displayed [RMB in the time slider]  
                sound display being toggled [animation options]  
                sound display mode being changed [animation options]  
              
                DagObjectCreated:  
                when a new DAG object is created.  
                deleteAll:  
                when a file new occurs  
                DisplayColorChanged:  
                when the display color changes.  
                displayLayerChange:  
                when a layer has been created or destroyed.  
                displayLayerManagerChange:  
                when the display layer manager has changed.  
                DisplayRGBColorChanged:  
                when the RGB display color changes.  
                glFrameTrigger:  
                for internal use only.  
                ChannelBoxLabelSelected:  
                when Channel Box label(first column) selection changes.  
                gridDisplayChanged:  
                for internal use only.  
                idle:   
                when Maya is idle and there are no high priority idle tasks  
                idleHigh:   
                when Maya is idle.  This is called before low priority idle  
                tasks.  You should almost always use "idle" instead.  
                lightLinkingChanged:  
                when any change occurs which modifies light linking  
                relationships.  
                lightLinkingChangedNonSG:  
                when any change occurs which modifies light linking  
                relationships, except when the change is a change of shading  
                assignment.  
                linearToleranceChanged:  
                 when the linear tolerance has been changed.  This tolerance  
                can be changed by:  
                 using the MEL command, "tolerance" with the  "-linear" flag  
                 changing the pref under Options->GeneralPreferences->  
                Modeling tab->Positional Tolerance  
              
                linearUnitChanged:   
                when the user changes the linear unit through the Options menu.  
                MenuModeChanged:   
                when the user changes the menu set for the menu bar in the main Maya window  
                (for example, from "Modeling" to "Animation").  
                RecentCommandChanged:   
                for internal use only.  
                NewSceneOpened:  
                when a new scene has been opened.  
                PostSceneRead:  
                after a scene has been read. Specifically after a file open, import or all child  
                references have been read.  
                nurbsToPolygonsPrefsChanged:  
                 when any of the nurbs-to-polygons prefs have changed.  These  
                prefs can be changed by:  
                 using the Mel command, "nurbsToPolygonsPref"  
                 changing the prefs under Polygons->Nurbs To  
                Polygons->Option Box  
              
                playbackRangeChanged:  
                when the playback keyframe range changes.  
                playbackRangeSliderChanged:  
                when the animation start/end range (i.e. the leftmost  
                or rightmost entry cells in the time slider range, the inner  
                ones adjust the playback range) change  
                preferredRendererChanged:  
                when the preferred renderer changes.  
                quitApplication:  
                when the user has chosen to quit, either through the quit MEL  
                command, or through the Exit menu item.  
                Redo:  
                when user has selected redo from the menu and there was something  
                to redo.  This callback can be used for updating UI or local  
                storage.  Do not change the state of the scene or DG during this  
                callback.  
                renderLayerChange:  
                when creation or deletion of a render layer node has occured.  
                renderLayerManagerChange:  
                when the current render layer has changed.  
                RebuildUIValues:  
                for internal use only.  
                SceneOpened:  
                when a scene has been opened.  
                SceneSaved:  
                when a scene has been saved.  
                SelectionChanged:   
                when a new selection is made.  
                UFESelectionChanged:   
                when a new UFE selection is made.  
                SelectModeChanged:   
                when the selection mode changes.  
                SelectPreferenceChanged:   
                for internal use only.  
                SelectPriorityChanged:  
                when the selection priority changes.  
                SelectTypeChanged:   
                when the selection type changes.  
                setEditorChanged:  
                obsolete.  No longer used.  
                SetModified:  
                when the set command is used to modify a set  
                SequencerActiveShotChanged:   
                when the active sequencer shot is changed.  
                snapModeChanged:  
                when the snap mode changes. E.g. changes to grid snapping.   
                timeChanged:  
                when the time changes.  
                timeUnitChanged:   
                when the user changes the time unit.  
                ToolChanged:   
                when the user changes the tool/context.  
                PostToolChanged:   
                after the user changes the tool/context.  
                NameChanged:   
                when the user changes the name of an object with the rename command.  
                Undo:  
                when user has selected undo from the menu and there was  
                something to undo.  This callback can be used for updating UI or local  
                storage.  Do not change the state of the scene or DG during this  
                callback.  
                modelEditorChanged:   
                when the user changes the options of a model editor.  
                colorMgtEnabledChanged:   
                when the global per-scene color management enabled flag changes.  
                colorMgtConfigFileEnableChanged:   
                when the global per-scene color management OCIO configuration enabled  
                flag changes.  
                colorMgtPrefsViewTransformChanged:   
                when the global per-scene color management view transform preferences  
                transform changes.  
                colorMgtWorkingSpaceChanged:   
                when the global per-scene color management working space changes.  
                colorMgtConfigFilePathChanged:   
                when the global per-scene color management OCIO configuration file path  
                changes.  
                colorMgtConfigChanged:   
                when the color management mode changes from native to OCIO, or when  
                a different OCIO configuration is loaded.  
                colorMgtPrefsReloaded:   
                when all the global per-scene color management settings are reloaded.  
                colorMgtUserPrefsChanged:   
                when any user-level color management preference has changed.  
                colorMgtOutputChanged:   
                when the color management transform, or its enabled state, has changed.  
                colorMgtOCIORulesChanged:   
                when the type of rules in OCIO mode has changed.  
                colorMgtRefreshed:   
                when the color management is refreshed to trap environment variable changes.  
                metadataVisualStatusChanged:   
                for internal use only.  
                shapeEditorTreeviewSelectionChanged:   
                when a new selection in shape editor's treeview is made .  
                RenderViewCameraChanged:   
                when the Render View's current camera is changed.  
                tabletModeChanged:   
                Windows only: if your device is a Tablet PC, then the convertible mode has  
                changed.  You can use command about -tabletMode to query if your device  
                is currently running in tablet or laptop (keyboard attached) mode.  
                Properties: create
        listJobs (bool?): This causes the command to return a string array containing  
                a description of all existing jobs, along with their job  
                numbers.  These numbers can be used to kill the jobs later.  
                Properties: create
        nodeDeleted (Tuple[str, Callable[..., Any]]?): Run the script when the named node is deleted  
                Properties: create
        nodeNameChanged (Tuple[str, Callable[..., Any]]?): Run the script when the name of the named node changes  
                Properties: create
        optionVarChanged (Tuple[str, Callable[..., Any]]?): Run the script when the named optionVar changes value.  
                If the optioNVar is deleted, this job is killed (even if the deletion is undoable).  
                Properties: create
        parent (str?): Attaches this job to a piece of maya UI.  When the UI is  
                destroyed, the job will be killed along with it.  
                Properties: create
        permanent (bool?): Makes the job un-killable. Permanent jobs exist for the life  
                of the application, or for the life of their parent object.  
                The -killWithScene flag does apply to permanent jobs.  
                Properties: create
        protected (bool?): Makes the job harder to kill. Protected jobs must be killed  
                or replaced intentionally by using the -force flag.  
                The -killWithScene flag does apply to protected jobs.  
                Properties: create
        replacePrevious (bool?): This flag can only be used with the -parent flag.  Before  
                the new scriptJob is created, any existing scriptJobs that have  
                the same parent are first deleted.  
                Properties: create
        runOnce (bool?): If this is set to true, the script will only be run a single  
                time.  If false (the default) the script will run every time  
                the triggering condition/event occurs.  If the -uid or -nd flags  
                are used, runOnce is turned on automatically.  
                Properties: create
        timeChange (Callable[..., Any]?): Run the script whenever the current time changes. The  
                script will not be executed if the time is changed by clicking on  
                the time slider, whereas scripts triggered by the "timeChanged"  
                condition will be executed.  
                Properties: create
        uiDeleted (Tuple[str, Callable[..., Any]]?): Run the script when the named piece of UI is deleted.  
                Properties: create

    Returns:
        int: The job number, which can be used to kill the job. The job
            number will be a value greater than or equal to zero
        List[str]: A string list when the list flag is used
        None: For the kill flag.
        bool: For the exists flag.

    Example:
    """

