from typing import *

from typing_extensions import Self

if TYPE_CHECKING:
    from _typeshed import Incomplete
else:
    Incomplete = None


def aaf2fcp(
    deleteFile: bool,
    dstPath: str,
    getFileName: int,
    progress: int,
    srcFile: str,
    terminate: int,
    waitCompletion: int,
) -> Any:
    ...


def about(
    query: bool,
    application: bool,
    apiVersion: bool,
    batch: bool,
    buildDirectory: bool,
    buildVariant: bool,
    cutIdentifier: bool,
    currentDate: bool,
    compositingManager: bool,
    connected: bool,
    codeset: bool,
    currentTime: bool,
    ctime: bool,
    customVersion: bool,
    customVersionClient: bool,
    customVersionMajor: bool,
    customVersionMinor: bool,
    customVersionString: bool,
    date: bool,
    environmentFile: bool,
    evalVersion: bool,
    file: bool,
    fontInfo: bool,
    helpDataDirectory: bool,
    ioVersion: bool,
    irix: bool,
    installedVersion: bool,
    linux64: bool,
    linux: bool,
    languageResources: bool,
    localizedResourceLocation: bool,
    ltVersion: bool,
    liveUpdate: bool,
    macOS: bool,
    majorVersion: bool,
    minorVersion: bool,
    ntOS: bool,
    operatingSystem: bool,
    operatingSystemVersion: bool,
    product: bool,
    preferences: bool,
    macOSppc: bool,
    patchVersion: bool,
    qtVersion: bool,
    tablet: bool,
    tabletMode: bool,
    uiLanguageIsLocalized: bool,
    uiLanguage: bool,
    uiLanguageForStartup: bool,
    uiLocaleLanguage: bool,
    version: bool,
    win64: bool,
    windows: bool,
    windowManager: bool,
    is64: bool,
    macOSx86: bool,
) -> Any:
    ...


def addAttr(
    *args: List[str],
    edit: bool,
    query: bool,
    attributeType: str,
    binaryTag: str,
    cachedInternally: bool,
    category: List[str],
    disconnectBehaviour: int,
    dataType: List[str],
    defaultValue: float,
    enumName: str,
    exists: bool,
    fromPlugin: bool,
    hidden: bool,
    hasMinValue: bool,
    hasSoftMinValue: bool,
    hasSoftMaxValue: bool,
    hasMaxValue: bool,
    indexMatters: bool,
    internalSet: bool,
    keyable: bool,
    longName: str,
    multi: bool,
    maxValue: float,
    minValue: float,
    numberOfChildren: int,
    niceName: str,
    parent: str,
    proxy: str,
    readable: bool,
    storable: bool,
    softMinValue: float,
    softMaxValue: float,
    shortName: str,
    usedAsColor: bool,
    usedAsFilename: bool,
    usedAsProxy: bool,
    writable: bool,
    worldSpace: bool,
) -> Any:
    ...


def addDynamic() -> Any:
    ...


def addDynamicAttribute() -> Any:
    ...


def addExtension(
    edit: bool,
    query: bool,
    attributeType: str,
    binaryTag: str,
    cachedInternally: bool,
    category: List[str],
    disconnectBehaviour: int,
    dataType: List[str],
    defaultValue: float,
    enumName: str,
    exists: bool,
    fromPlugin: bool,
    hidden: bool,
    hasMinValue: bool,
    hasSoftMinValue: bool,
    hasSoftMaxValue: bool,
    hasMaxValue: bool,
    indexMatters: bool,
    internalSet: bool,
    keyable: bool,
    longName: str,
    multi: bool,
    maxValue: float,
    minValue: float,
    numberOfChildren: int,
    niceName: str,
    nodeType: str,
    parent: str,
    proxy: str,
    readable: bool,
    storable: bool,
    softMinValue: float,
    softMaxValue: float,
    shortName: str,
    usedAsColor: bool,
    usedAsFilename: bool,
    usedAsProxy: bool,
    writable: bool,
    worldSpace: bool,
) -> Any:
    ...


def addMetadata(
    *args: List[str],
    query: bool,
    channelType: str,
    channelName: str,
    indexType: str,
    scene: bool,
    streamName: str,
    structure: str,
) -> Any:
    ...


def addPP(*args: List[str], attribute: str) -> Any:
    ...


def adpAnalyticsDialog(activeNotification: bool, desktopAnalytics: bool) -> Any:
    ...


def adpWaypoint(name: str, property: List[str]) -> Any:
    ...


def adskAsset(
    arg0: Incomplete, /, query: bool, assetID: str, library: str, resolved: bool
) -> Any:
    ...


def adskAssetLibrary(*args: List[str], unloadAll: bool, unload: bool) -> Any:
    ...


def adskAssetList(infoType: str) -> Any:
    ...


def adskAssetListUI(
    query: bool, commandSuffix: str, materialLoaded: bool, uiCommand: str
) -> Any:
    ...


def affectedNet(*args: List[str], edit: bool, query: bool, type: str) -> Any:
    ...


def affects(*args: List[Incomplete], type: str) -> Any:
    ...


def agFormatIn(file: str, name: str) -> Any:
    ...


def agFormatOut(*args: List[str], file: str) -> Any:
    ...


def aimConstraint(
    *args: List[str],
    edit: bool,
    query: bool,
    aimVector: Tuple[float, float, float],
    layer: str,
    maintainOffset: bool,
    name: str,
    offset: Tuple[float, float, float],
    remove: bool,
    skip: List[str],
    targetList: bool,
    upVector: Tuple[float, float, float],
    weight: float,
    weightAliasList: bool,
    worldUpVector: Tuple[float, float, float],
    worldUpObject: str,
    worldUpType: str,
) -> Any:
    ...


def air(
    *args: List[str],
    edit: bool,
    query: bool,
    attenuation: float,
    directionX: float,
    directionY: float,
    directionZ: float,
    enableSpread: bool,
    fanSetup: bool,
    inheritRotation: bool,
    inheritVelocity: float,
    magnitude: float,
    maxDistance: float,
    name: str,
    position: List[Tuple[float, float, float]],
    perVertex: bool,
    speed: float,
    spread: float,
    torusSectionRadius: float,
    velocityComponentOnly: bool,
    volumeExclusion: bool,
    volumeOffset: Tuple[float, float, float],
    volumeShape: str,
    volumeSweep: float,
    wakeSetup: bool,
    windSetup: bool,
) -> Any:
    ...


def aliasAttr(*args: List[str], edit: bool, query: bool, remove: bool) -> Any:
    ...


def align(
    *args: List[str],
    alignToLead: bool,
    coordinateSystem: str,
    xAxis: str,
    yAxis: str,
    zAxis: str,
) -> Any:
    ...


def alignCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    align: bool,
    anchorFirstObject: bool,
    history: bool,
    distribute: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
    showAlignTouch: bool,
) -> Any:
    ...


def alignCurve(
    *args: Tuple[str, str],
    edit: bool,
    query: bool,
    attach: bool,
    curvatureContinuity: bool,
    caching: bool,
    constructionHistory: bool,
    curvatureScale1: float,
    curvatureScale2: float,
    frozen: bool,
    joinParameter: float,
    keepMultipleKnots: bool,
    name: str,
    nodeState: int,
    object: bool,
    positionalContinuity: bool,
    positionalContinuityType: int,
    replaceOriginal: bool,
    reverse1: bool,
    reverse2: bool,
    tangentContinuity: bool,
    tangentContinuityType: int,
    tangentScale1: float,
    tangentScale2: float,
) -> Any:
    ...


def alignSurface(
    *args: Tuple[str, str],
    edit: bool,
    query: bool,
    attach: bool,
    curvatureContinuity: bool,
    caching: bool,
    constructionHistory: bool,
    curvatureScale1: float,
    curvatureScale2: float,
    directionU: bool,
    frozen: bool,
    joinParameter: float,
    keepMultipleKnots: bool,
    name: str,
    nodeState: int,
    object: bool,
    positionalContinuity: bool,
    positionalContinuityType: int,
    replaceOriginal: bool,
    reverse1: bool,
    reverse2: bool,
    swap1: bool,
    swap2: bool,
    tangentContinuity: bool,
    tangentContinuityType: int,
    tangentScale1: float,
    tangentScale2: float,
    twist: bool,
) -> Any:
    ...


def allNodeTypes(includeAbstract: bool) -> Any:
    ...


def ambientLight(
    *args: List[str],
    edit: bool,
    query: bool,
    ambientShade: float,
    discRadius: float,
    exclusive: bool,
    intensity: float,
    name: str,
    position: Tuple[float, float, float],
    rotation: Tuple[float, float, float],
    useRayTraceShadows: bool,
    shadowColor: Tuple[float, float, float],
    shadowDither: float,
    shadowSamples: int,
    softShadow: bool,
) -> Any:
    ...


def angleBetween(
    caching: bool,
    constructionHistory: bool,
    euler: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    vector1: Tuple[float, float, float],
    vector1X: float,
    vector1Y: float,
    vector1Z: float,
    vector2: Tuple[float, float, float],
    vector2X: float,
    vector2Y: float,
    vector2Z: float,
) -> Any:
    ...


def animCurveEditor(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    showActiveCurveNames: bool,
    areCurvesSelected: bool,
    autoFit: str,
    autoFitTime: str,
    constrainDrag: int,
    classicMode: bool,
    curvesShown: bool,
    curvesShownForceUpdate: bool,
    clipTime: str,
    control: bool,
    displayActiveKeys: str,
    displayActiveKeyTangents: str,
    denormalizeCurvesCommand: str,
    displayInfinities: str,
    displayKeys: str,
    displayNormalized: bool,
    defineTemplate: str,
    docTag: str,
    displayTangents: str,
    displayValues: str,
    exists: bool,
    filter: str,
    forceMainConnection: str,
    highlightAffectedCurves: bool,
    highlightConnection: str,
    keyMinScale: float,
    keyScale: float,
    keyingTime: str,
    lookAt: str,
    lockMainConnection: bool,
    lockPlayRangeShades: str,
    menu: Callable,
    mainListConnection: str,
    normalizeCurvesCommand: str,
    outliner: str,
    parent: str,
    panel: str,
    preSelectionHighlight: bool,
    renormalizeCurves: bool,
    resultSamples: int,
    resultScreenSamples: int,
    resultUpdate: str,
    smoothness: str,
    showBufferCurves: str,
    stackedCurves: bool,
    stackedCurvesMin: float,
    showCurveNames: bool,
    stackedCurvesSpace: float,
    stackedCurvesMax: float,
    simpleKeyView: bool,
    selectionConnection: str,
    showPlayRangeShades: str,
    showResults: str,
    snapTime: str,
    stateString: bool,
    showUpstreamCurves: bool,
    snapValue: str,
    timelinePositionTop: float,
    unlockMainConnection: bool,
    unParent: bool,
    updateMainConnection: bool,
    useTemplate: str,
    viewLeft: float,
    valueLinesToggle: str,
    viewRight: float,
) -> Any:
    ...


def animDisplay(
    edit: bool,
    query: bool,
    refAnimCurvesEditable: bool,
    timeCode: str,
    timeCodeOffset: str,
    modelUpdate: str,
) -> Any:
    ...


def animLayer(
    *args: List[Incomplete],
    edit: bool,
    query: bool,
    affectedLayers: bool,
    addRelatedKG: bool,
    animCurves: bool,
    addSelectedObjects: bool,
    attribute: List[str],
    baseAnimCurves: bool,
    bestLayer: bool,
    blendNodes: bool,
    bestAnimLayer: bool,
    children: str,
    copyAnimation: str,
    copyNoAnimation: str,
    collapse: bool,
    copy: str,
    extractAnimation: str,
    excludeBoolean: bool,
    excludeDynamic: bool,
    excludeEnum: bool,
    excludeRotate: bool,
    excludeScale: bool,
    excludeTranslate: bool,
    excludeVisibility: bool,
    exists: bool,
    findCurveForPlug: str,
    forceUIRebuild: bool,
    lock: bool,
    layeredPlug: str,
    mute: bool,
    maxLayers: bool,
    moveLayerAfter: str,
    moveLayerBefore: str,
    override: bool,
    parent: str,
    preferred: bool,
    passthrough: bool,
    root: str,
    removeAttribute: List[str],
    removeAllAttributes: bool,
    solo: bool,
    selected: bool,
    forceUIRefresh: bool,
    weight: float,
    writeBlendnodeDestinations: bool,
) -> Any:
    ...


def animView(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    endTime: int,
    maxValue: float,
    minValue: float,
    nextView: bool,
    previousView: bool,
    startTime: int,
) -> Any:
    ...


def annotate(*args: List[str], point: Tuple[float, float, float], text: str) -> Any:
    ...


def appHome(
    edit: bool,
    query: bool,
    instrument: str,
    iconVisible: bool,
    setTab: str,
    toggleVisibility: bool,
    updateRecentFiles: bool,
    visible: bool,
) -> Any:
    ...


def appendListItem() -> Any:
    ...


def applyAttrPattern(*args: List[str], nodeType: str, patternName: str) -> Any:
    ...


def applyMetadata(arg0: Incomplete, /, format: str, scene: bool, value: str) -> Any:
    ...


def applyTake(*args, **kwargs) -> Any:
    ...


def arcLenDimContext(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def arcLengthDimension() -> Any:
    ...


def arclen(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
) -> Any:
    ...


def arrayMapper(
    destAttr: str, inputU: str, inputV: str, mapTo: str, target: List[str], type: str
) -> Any:
    ...


def art3dPaintCtx(*args, **kwargs) -> Any:
    ...


def artAttr() -> Any:
    ...


def artAttrCtx(*args, **kwargs) -> Any:
    ...


def artAttrPaintVertexCtx(*args, **kwargs) -> Any:
    ...


def artAttrSkinPaintCmd(*args, **kwargs) -> Any:
    ...


def artAttrSkinPaintCtx(*args, **kwargs) -> Any:
    ...


def artAttrTool(*args, **kwargs) -> Any:
    ...


def artBaseCtx(*args, **kwargs) -> Any:
    ...


def artBuildPaintMenu() -> Any:
    ...


def artFluidAttr(*args, **kwargs) -> Any:
    ...


def artFluidAttrCtx(*args, **kwargs) -> Any:
    ...


def artPuttyCtx(*args, **kwargs) -> Any:
    ...


def artSelect() -> Any:
    ...


def artSelectCtx(*args, **kwargs) -> Any:
    ...


def artSetPaint() -> Any:
    ...


def artSetPaintCtx(*args, **kwargs) -> Any:
    ...


def artUserPaintCtx(*args, **kwargs) -> Any:
    ...


def arubaNurbsToPoly(
    *args: List[str],
    edit: bool,
    query: bool,
    adaptive: bool,
    caching: bool,
    chordalDeviation: float,
    constructionHistory: bool,
    frozen: bool,
    minChordLength: float,
    localSpace: bool,
    maxChordLength: float,
    name: str,
    nodeState: int,
    normalTolerance: float,
    object: bool,
    samples: int,
    sampleType: int,
    tolerance: float,
    useSurfaceShader: bool,
    worldSpace: bool,
) -> Any:
    ...


def assembly(
    *args: List[str],
    edit: bool,
    query: bool,
    active: str,
    activeLabel: str,
    postCreateUIProc: Callable,
    canCreate: str,
    createOptionBoxProc: Callable,
    createRepresentation: str,
    deregister: str,
    deleteRepresentation: str,
    defaultType: str,
    input: str,
    isAType: str,
    isTrackingMemberEdits: str,
    label: str,
    listRepresentations: bool,
    listRepTypesProc: Callable,
    listRepTypes: bool,
    listTypes: bool,
    name: str,
    newRepLabel: str,
    repPreCreateUIProc: str,
    repPostCreateUIProc: str,
    proc: Callable,
    repLabel: str,
    repName: str,
    renameRepresentation: str,
    repNamespace: str,
    repType: str,
    repTypeLabel: str,
    repTypeLabelProc: Callable,
    type: str,
) -> Any:
    ...


def assignCommand(
    arg0: int,
    /,
    edit: bool,
    query: bool,
    addDivider: str,
    altModifier: bool,
    annotation: str,
    command: Callable,
    commandModifier: bool,
    ctrlModifier: bool,
    delete: int,
    data1: str,
    data2: str,
    data3: str,
    dividerString: str,
    enableCommandRepeat: bool,
    factorySettings: bool,
    index: int,
    keyString: str,
    keyArray: bool,
    keyUp: bool,
    name: bool,
    numDividersPreceding: int,
    numElements: bool,
    optionModifier: bool,
    sortByKey: bool,
    sourceUserCommands: bool,
) -> Any:
    ...


def assignInputDevice(*args, **kwargs) -> Any:
    ...


def assignViewportFactories(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    materialFactory: str,
    nodeType: str,
    textureFactory: str,
) -> Any:
    ...


def attachCache() -> Any:
    ...


def attachCurve(
    *args: List[Incomplete],
    edit: bool,
    query: bool,
    blendBias: float,
    blendKnotInsertion: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    keepMultipleKnots: bool,
    method: int,
    name: str,
    nodeState: int,
    object: bool,
    parameter: float,
    replaceOriginal: bool,
    reverse1: bool,
    reverse2: bool,
) -> Any:
    ...


def attachDeviceAttr(*args, **kwargs) -> Any:
    ...


def attachFluidCache() -> Any:
    ...


def attachGeometryCache() -> Any:
    ...


def attachNclothCache() -> Any:
    ...


def attachSurface(
    *args: Tuple[str, str],
    edit: bool,
    query: bool,
    blendBias: float,
    blendKnotInsertion: bool,
    caching: bool,
    constructionHistory: bool,
    directionU: bool,
    frozen: bool,
    keepMultipleKnots: bool,
    method: int,
    name: str,
    nodeState: int,
    object: bool,
    parameter: float,
    replaceOriginal: bool,
    reverse1: bool,
    reverse2: bool,
    swap1: bool,
    swap2: bool,
    twist: bool,
) -> Any:
    ...


def attrColorSliderGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    alphaValue: float,
    attrNavDecision: Tuple[str, str],
    annotation: str,
    attribute: str,
    backgroundColor: Tuple[float, float, float],
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    hsvValue: Tuple[float, float, float],
    isObscured: bool,
    label: str,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rowAttach: List[Tuple[int, str, int]],
    rgbValue: Tuple[float, float, float],
    showButton: bool,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def attrCompatibility(
    *args: Tuple[str, str],
    addAttr: bool,
    clear: bool,
    dumpTable: bool,
    enable: bool,
    nodeRename: str,
    pluginNode: str,
    renameAttr: str,
    removeAttr: bool,
    type: str,
    version: str,
) -> Any:
    ...


def attrControlGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    attribute: str,
    annotation: str,
    changeCommand: Callable,
    enable: bool,
    exists: bool,
    handlesAttribute: str,
    hideMapButton: bool,
    label: str,
    preventOverride: bool,
) -> Any:
    ...


def attrEnumOptionMenu(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    attribute: str,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enumeratedItem: List[Tuple[int, str]],
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    label: str,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def attrEnumOptionMenuGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    annotation: str,
    attribute: str,
    backgroundColor: Tuple[float, float, float],
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enumeratedItem: List[Tuple[int, str]],
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    label: str,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rowAttach: List[Tuple[int, str, int]],
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def attrFieldGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    annotation: str,
    attribute: str,
    backgroundColor: Tuple[float, float, float],
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    changeCommand: Callable,
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    extraButton: bool,
    extraButtonCommand: Callable,
    enableBackground: bool,
    extraButtonIcon: str,
    enableKeyboardFocus: bool,
    extraLabel: str,
    enable: bool,
    exists: bool,
    forceAddMapButton: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    hideMapButton: bool,
    isObscured: bool,
    label: str,
    manage: bool,
    maxValue: float,
    minValue: float,
    noBackground: bool,
    numberOfFields: int,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    precision: int,
    rowAttach: List[Tuple[int, str, int]],
    step: float,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def attrFieldSliderGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    annotation: str,
    attribute: str,
    backgroundColor: Tuple[float, float, float],
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    changeCommand: Callable,
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    extraButton: bool,
    extraButtonCommand: Callable,
    enableBackground: bool,
    extraButtonIcon: str,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    forceAddMapButton: bool,
    fieldMinValue: float,
    fieldMaxValue: float,
    fullPathName: bool,
    fieldStep: float,
    height: int,
    highlightColor: Tuple[float, float, float],
    hideMapButton: bool,
    isObscured: bool,
    label: str,
    manage: bool,
    maxValue: float,
    minValue: float,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    precision: int,
    rowAttach: List[Tuple[int, str, int]],
    step: float,
    statusBarMessage: str,
    sliderMinValue: float,
    sliderMaxValue: float,
    sliderStep: float,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    vertical: bool,
    width: int,
) -> Any:
    ...


def attrNavigationControlGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    attrNavDecision: Tuple[str, str],
    annotation: str,
    attribute: str,
    backgroundColor: Tuple[float, float, float],
    connectAttrToDropped: str,
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    connectToExisting: str,
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    createNew: str,
    connectNodeToDropped: str,
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    disconnect: str,
    delete: str,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    defaultTraversal: str,
    extraButton: bool,
    extraButtonCommand: Callable,
    enableBackground: bool,
    extraButtonIcon: str,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    ignore: str,
    ignoreNotSupported: bool,
    isObscured: bool,
    label: str,
    manage: bool,
    noBackground: bool,
    notIgnorableMenu: bool,
    notKeyableMenu: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rowAttach: List[Tuple[int, str, int]],
    relatedNodes: str,
    statusBarMessage: str,
    unignore: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def attributeInfo(
    *args: List[str],
    allAttributes: bool,
    logicalAnd: bool,
    bool: bool,
    enumerated: bool,
    hidden: bool,
    internal: bool,
    inherited: bool,
    leaf: bool,
    multi: bool,
    short: bool,
    type: str,
    userInterface: bool,
    writable: bool,
) -> Any:
    ...


def attributeMenu(*args, **kwargs) -> Any:
    ...


def attributeName(
    arg0: Incomplete, /, long: bool, leaf: bool, nice: bool, short: bool
) -> Any:
    ...


def attributeQuery(
    arg0: str,
    /,
    affectsAppearance: bool,
    attributeType: bool,
    affectsWorldspace: bool,
    connectable: bool,
    channelBox: bool,
    cachedInternally: bool,
    categories: bool,
    enum: bool,
    exists: bool,
    hidden: bool,
    internal: bool,
    indeterminant: bool,
    internalGet: bool,
    indexMatters: bool,
    internalSet: bool,
    keyable: bool,
    listChildren: bool,
    listDefault: bool,
    listEnum: bool,
    longName: bool,
    listParent: bool,
    listSiblings: bool,
    localizedListEnum: bool,
    multi: bool,
    maximum: bool,
    minimum: bool,
    minExists: bool,
    message: bool,
    maxExists: bool,
    node: str,
    numberOfChildren: bool,
    niceName: bool,
    range: bool,
    readable: bool,
    rangeExists: bool,
    renderSource: bool,
    softRange: bool,
    softRangeExists: bool,
    softMinExists: bool,
    softMin: bool,
    softMax: bool,
    shortName: bool,
    storable: bool,
    softMaxExists: bool,
    typeExact: str,
    type: str,
    usedAsColor: bool,
    usedAsFilename: bool,
    usesMultiBuilder: bool,
    writable: bool,
    worldspace: bool,
) -> Any:
    ...


def audioTrack(
    *args: List[str],
    edit: bool,
    query: bool,
    insertTrack: int,
    lock: bool,
    mute: bool,
    numTracks: int,
    removeEmptyTracks: bool,
    removeTrack: int,
    solo: bool,
    swapTracks: Tuple[int, int],
    title: str,
    track: int,
) -> Any:
    ...


def autoKeyframe(
    edit: bool,
    query: bool,
    addAttr: str,
    characterOption: str,
    listAttr: bool,
    noReset: bool,
    state: bool,
) -> Any:
    ...


def autoPlace(useMouse: bool) -> Any:
    ...


def autoSave(
    query: bool,
    destinationFolder: bool,
    destination: int,
    enable: bool,
    folder: str,
    interval: float,
    limitBackups: bool,
    maxBackups: int,
    perform: bool,
    prompt: bool,
) -> Any:
    ...


def backgroundEvaluationManager(
    *args: List[str], query: bool, interrupt: bool, mode: str, pause: bool, resume: bool
) -> Any:
    ...


def bakeClip(
    *args: List[str],
    blend: Tuple[int, int],
    clipIndex: List[int],
    keepOriginals: bool,
    name: str,
) -> Any:
    ...


def bakeDeformer(
    colorizeSkeleton: bool,
    dstMeshName: str,
    dstSkeletonName: str,
    hierarchy: bool,
    influences: Incomplete,
    maxInfluences: int,
    pruneWeights: float,
    customRangeOfMotion: Incomplete,
    srcMeshName: str,
    srcSkeletonName: str,
    smoothWeights: int,
) -> Any:
    ...


def bakePartialHistory(
    *args: List[str],
    edit: bool,
    query: bool,
    allShapes: bool,
    postSmooth: bool,
    preCache: bool,
    prePostDeformers: bool,
    preDeformers: bool,
) -> Any:
    ...


def bakeResults(
    *args: List[str],
    edit: bool,
    query: bool,
    animation: str,
    attribute: List[str],
    bakeOnOverrideLayer: bool,
    controlPoints: bool,
    disableImplicitControl: bool,
    destinationLayer: str,
    float: List[Incomplete],
    hierarchy: str,
    index: List[Incomplete],
    includeUpperBound: bool,
    minimizeRotation: bool,
    oversamplingRate: int,
    preserveOutsideKeys: bool,
    removeBakedAttributeFromLayer: bool,
    removeBakedAnimFromLayer: bool,
    resolveWithoutLayer: List[str],
    shape: bool,
    sparseAnimCurveBake: bool,
    sampleBy: int,
    simulation: bool,
    smart: Tuple[Incomplete, bool, float, Incomplete],
    time: List[Incomplete],
) -> Any:
    ...


def bakeSimulation(
    *args: List[str],
    edit: bool,
    query: bool,
    animation: str,
    attribute: List[str],
    bakeOnOverrideLayer: bool,
    controlPoints: bool,
    disableImplicitControl: bool,
    destinationLayer: str,
    float: List[Incomplete],
    hierarchy: str,
    index: List[Incomplete],
    includeUpperBound: bool,
    minimizeRotation: bool,
    oversamplingRate: int,
    preserveOutsideKeys: bool,
    removeBakedAttributeFromLayer: bool,
    removeBakedAnimFromLayer: bool,
    resolveWithoutLayer: List[str],
    shape: bool,
    sparseAnimCurveBake: bool,
    sampleBy: int,
    simulation: bool,
    smart: Tuple[Incomplete, bool, float, Incomplete],
    time: List[Incomplete],
) -> Any:
    ...


def baseTemplate(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    exists: bool,
    force: bool,
    fileName: str,
    load: bool,
    matchFile: str,
    silent: bool,
    unload: bool,
    viewList: str,
) -> Any:
    ...


def baseView(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    itemInfo: str,
    itemList: bool,
    viewLabel: bool,
    viewDescription: bool,
    viewList: bool,
    viewName: str,
) -> Any:
    ...


def batchRender(
    *args: Tuple[str, str, str, str, str],
    filename: str,
    melCommand: str,
    numProcs: int,
    preRenderCommand: str,
    renderCommandOptions: str,
    remoteRenderMachine: str,
    showImage: bool,
    status: str,
    useRemoteRender: bool,
    useStandalone: bool,
    verbosity: int,
) -> Any:
    ...


def bevel(
    *args: Tuple[str, str],
    edit: bool,
    query: bool,
    bevelShapeType: int,
    caching: bool,
    constructionHistory: bool,
    cornerType: int,
    depth: float,
    extrudeDepth: float,
    frozen: bool,
    joinSurfaces: bool,
    name: str,
    nodeState: int,
    numberOfSides: int,
    object: bool,
    polygon: int,
    range: bool,
    tolerance: float,
    width: float,
) -> Any:
    ...


def bevelPlus(
    *args: List[str],
    edit: bool,
    query: bool,
    bevelInside: bool,
    capSides: int,
    caching: bool,
    constructionHistory: bool,
    polyOutChordHeightRatio: float,
    polyOutChordHeight: float,
    depth: float,
    extrudeDepth: float,
    frozen: bool,
    innerStyle: int,
    joinSurfaces: bool,
    name: str,
    nodeState: int,
    normalsOutwards: bool,
    numberOfSides: int,
    outerStyle: int,
    polyOutCurveSamples: int,
    polyOutCurveType: int,
    polyOutExtrusionSamples: int,
    polyOutExtrusionType: int,
    polygon: int,
    polyOutCount: int,
    polyOutMethod: int,
    range: bool,
    tolerance: float,
    polyOutUseChordHeight: bool,
    polyOutUseChordHeightRatio: bool,
    width: float,
) -> Any:
    ...


def bezierAnchorPreset(preset: int) -> Any:
    ...


def bezierAnchorState(even: bool, smooth: bool) -> Any:
    ...


def bezierCurveToNurbs() -> Any:
    ...


def bezierInfo(
    anchorFromCV: int,
    cvFromAnchor: int,
    isAnchorSelected: bool,
    isTangentSelected: bool,
    onlyAnchorsSelected: bool,
    onlyTangentsSelected: bool,
) -> Any:
    ...


def binMembership(
    *args: List[str],
    query: bool,
    addToBin: str,
    exists: str,
    inheritBinsFromNodes: str,
    isValidBinName: str,
    listBins: bool,
    makeExclusive: str,
    notifyChanged: bool,
    removeFromBin: str,
) -> Any:
    ...


def bindSkin(
    *args: List[str],
    edit: bool,
    query: bool,
    byClosestPoint: bool,
    byPartition: bool,
    colorJoints: bool,
    delete: bool,
    doNotDescend: bool,
    enable: bool,
    name: str,
    partition: str,
    toAll: bool,
    toSkeleton: bool,
    toSelectedBones: bool,
    unbind: bool,
    unbindKeepHistory: bool,
    unlock: bool,
) -> Any:
    ...


def blend(
    *args: List[str],
    edit: bool,
    query: bool,
    autoDirection: bool,
    caching: bool,
    crvsInFirstRail: int,
    constructionHistory: bool,
    flipLeft: bool,
    flipRight: bool,
    frozen: bool,
    leftParameter: float,
    multipleKnots: bool,
    name: str,
    nodeState: int,
    object: bool,
    polygon: int,
    positionTolerance: float,
    rightParameter: float,
    tangentTolerance: float,
) -> Any:
    ...


def blend2(
    *args: List[str],
    edit: bool,
    query: bool,
    autoAnchor: bool,
    autoNormal: bool,
    caching: bool,
    crvsInFirstRail: int,
    constructionHistory: bool,
    flipLeftNormal: bool,
    flipRightNormal: bool,
    frozen: bool,
    leftAnchor: float,
    leftEnd: float,
    leftStart: float,
    multipleKnots: bool,
    name: str,
    nodeState: int,
    object: bool,
    polygon: int,
    positionTolerance: float,
    rightAnchor: float,
    rightEnd: float,
    rightStart: float,
    reverseLeft: bool,
    reverseRight: bool,
    tangentTolerance: float,
) -> Any:
    ...


def blendCtx(*args, **kwargs) -> Any:
    ...


def blendShape(
    *args: List[str],
    edit: bool,
    query: bool,
    after: bool,
    afterReference: bool,
    automatic: bool,
    before: bool,
    copyDelta: Tuple[int, int, int],
    copyInBetweenDelta: Tuple[int, int, int, int],
    components: bool,
    selectedComponents: bool,
    copyWeights: Tuple[int, int, int],
    deformerTools: bool,
    envelope: float,
    export: str,
    exportTarget: List[Tuple[int, int]],
    exclusive: str,
    frontOfChain: bool,
    flipTarget: List[Tuple[int, int]],
    geometry: List[str],
    geometryIndices: bool,
    inBetween: bool,
    inBetweenIndex: int,
    inBetweenType: str,
    includeHiddenSelections: bool,
    ip: str,
    ignoreSelected: bool,
    mirrorDirection: int,
    mergeSource: List[int],
    mergeTarget: int,
    mirrorTarget: List[Tuple[int, int]],
    name: str,
    normalizationGroups: bool,
    origin: str,
    parallel: bool,
    prune: bool,
    remove: List[bool],
    resetTargetDelta: List[Tuple[int, int]],
    symmetryAxis: str,
    suppressDialog: bool,
    symmetryEdge: List[str],
    split: bool,
    symmetrySpace: int,
    target: List[Tuple[str, int, str, float]],
    topologyCheck: bool,
    transform: str,
    tangentSpace: bool,
    useComponentTags: bool,
    weight: List[Tuple[int, float]],
    weightCount: int,
) -> Any:
    ...


def blendShapeEditor(*args, **kwargs) -> Any:
    ...


def blendShapePanel(*args, **kwargs) -> Any:
    ...


def blendTwoAttr(
    *args: List[str],
    edit: bool,
    query: bool,
    attribute: List[str],
    attribute0: str,
    attribute1: str,
    blender: str,
    controlPoints: bool,
    driver: int,
    name: str,
    shape: bool,
    time: Incomplete,
) -> Any:
    ...


def blindDataType(
    dataType: List[str],
    typeId: int,
    longDataName: List[str],
    longNames: bool,
    query: bool,
    shortDataName: List[str],
    shortNames: bool,
    typeNames: bool,
) -> Any:
    ...


def boneLattice(
    *args: List[str],
    edit: bool,
    query: bool,
    after: bool,
    afterReference: bool,
    before: bool,
    bicep: float,
    components: bool,
    selectedComponents: bool,
    deformerTools: bool,
    exclusive: str,
    frontOfChain: bool,
    geometry: List[str],
    geometryIndices: bool,
    includeHiddenSelections: bool,
    ignoreSelected: bool,
    joint: str,
    lengthIn: float,
    lengthOut: float,
    name: str,
    parallel: bool,
    prune: bool,
    remove: List[bool],
    split: bool,
    transform: str,
    tricep: float,
    useComponentTags: bool,
    widthLeft: float,
    widthRight: float,
) -> Any:
    ...


def boundary(
    *args: Tuple[str, str, str, str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    endPoint: bool,
    endPointTolerance: float,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    order: bool,
    polygon: int,
    range: bool,
) -> Any:
    ...


def boxDollyCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    alternateContext: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
    toolName: str,
) -> Any:
    ...


def boxZoomCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
    zoomScale: float,
) -> Any:
    ...


def bufferCurve(
    *args: List[str],
    query: bool,
    animation: str,
    attribute: List[str],
    controlPoints: bool,
    exists: bool,
    float: List[Incomplete],
    hierarchy: str,
    index: List[Incomplete],
    includeUpperBound: bool,
    overwrite: bool,
    shape: bool,
    swap: bool,
    time: List[Incomplete],
    useReferencedCurve: bool,
) -> Any:
    ...


def buildBookmarkMenu(arg0: str, /, editor: str, type: str) -> Any:
    ...


def buildKeyframeMenu() -> Any:
    ...


def buildSendToBackburnerDialog() -> Any:
    ...


def button(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    actionIsSubstitute: bool,
    align: str,
    annotation: str,
    actOnPress: bool,
    backgroundColor: Tuple[float, float, float],
    command: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    label: str,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    recomputeSize: bool,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def buttonManip(*args: Tuple[Callable, str], icon: str) -> Any:
    ...


def cacheAppend() -> Any:
    ...


def cacheAppendOpt() -> Any:
    ...


def cacheEvaluator(
    *args: List[str],
    edit: bool,
    query: bool,
    cacheFillMode: str,
    cacheFillOrder: str,
    cachedFrames: bool,
    cacheInvalidate: Incomplete,
    cacheName: str,
    creationParameters: bool,
    cachingPoints: bool,
    dynamicsAsyncRefresh: bool,
    delegateEvaluation: bool,
    dynamicsSupportActive: bool,
    dynamicsSupportEnabled: bool,
    flushCache: str,
    flushCacheRange: Tuple[Incomplete, bool],
    flushCacheSync: bool,
    flushCacheWait: bool,
    hybridCacheMode: str,
    listCachedNodes: bool,
    listCacheNames: bool,
    layeredEvaluationActive: bool,
    layeredEvaluationCachingPoints: bool,
    layeredEvaluationEnabled: bool,
    listValueNames: bool,
    newAction: str,
    newActionParam: str,
    newFilter: str,
    newFilterParam: str,
    newRule: str,
    newRuleParam: str,
    preventFrameSkip: bool,
    pauseInvalidation: bool,
    resumeInvalidation: bool,
    resetRules: bool,
    resourceUsage: bool,
    safeMode: bool,
    safeModeMessages: bool,
    safeModeTriggered: bool,
    valueName: str,
    waitForCache: float,
) -> Any:
    ...


def cacheFile(
    *args: List[str],
    edit: bool,
    query: bool,
    attachFile: bool,
    appendFrame: bool,
    cacheableAttrs: str,
    creationChannelName: List[str],
    createCacheNode: bool,
    cacheFormat: str,
    cacheFileNode: List[str],
    channelIndex: bool,
    cacheInfo: List[str],
    cacheableNode: List[str],
    channelName: List[str],
    deleteCachedFrame: bool,
    descriptionFileName: bool,
    directory: str,
    dataSize: bool,
    doubleToFloat: bool,
    endTime: int,
    fileName: str,
    format: str,
    geometry: bool,
    inAttr: List[str],
    interpEndTime: int,
    interpStartTime: int,
    inTangent: str,
    noBackup: bool,
    outAttr: List[str],
    outTangent: str,
    prefix: bool,
    pointsAndNormals: List[str],
    pointCount: bool,
    convertPc2: bool,
    pc2File: str,
    points: List[str],
    refresh: bool,
    replaceCachedFrame: bool,
    runupFrames: int,
    replaceWithoutSimulating: bool,
    staticCache: bool,
    singleCache: bool,
    simulationRate: int,
    sampleMultiplier: int,
    startTime: int,
    worldSpace: bool,
) -> Any:
    ...


def cacheFileCombine(
    *args: List[str],
    edit: bool,
    query: bool,
    connectCache: str,
    cacheIndex: bool,
    channelName: List[str],
    keepWeights: bool,
    layerNode: bool,
    nextAvailable: bool,
    object: str,
    objectIndex: int,
) -> Any:
    ...


def cacheFileMerge(
    *args: List[str],
    edit: bool,
    query: bool,
    endTime: int,
    geometry: bool,
    startTime: int,
) -> Any:
    ...


def cacheFileTrack(
    *args: List[str],
    edit: bool,
    query: bool,
    insertTrack: int,
    lock: bool,
    mute: bool,
    removeEmptyTracks: bool,
    removeTrack: int,
    solo: bool,
    track: int,
) -> Any:
    ...


def caddyManip(*args, **kwargs) -> Any:
    ...


def callbacks(
    *args: List[str],
    addCallback: Callable,
    clearAllCallbacks: bool,
    clearCallbacks: bool,
    dumpCallbacks: bool,
    describeHooks: bool,
    executeCallbacks: bool,
    hook: str,
    listCallbacks: bool,
    owner: str,
    removeCallback: Callable,
) -> Any:
    ...


def camera(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    aspectRatio: float,
    centerOfInterest: float,
    clippingPlanes: bool,
    cameraScale: float,
    displayFieldChart: bool,
    displayFilmGate: bool,
    displayFilmOrigin: bool,
    displayFilmPivot: bool,
    displayGateMask: bool,
    depthOfField: bool,
    displayResolution: bool,
    displaySafeAction: bool,
    displaySafeTitle: bool,
    farClipPlane: float,
    focusDistance: float,
    filmFit: str,
    farFocusDistance: float,
    filmFitOffset: float,
    focalLength: float,
    filmRollOrder: str,
    filmRollValue: float,
    fStop: float,
    filmTranslateH: float,
    filmTranslateV: float,
    homeCommand: str,
    horizontalFilmAperture: float,
    horizontalFilmOffset: float,
    horizontalFieldOfView: float,
    stereoHorizontalImageTranslate: float,
    horizontalPan: float,
    horizontalRollPivot: float,
    horizontalShake: float,
    journalCommand: bool,
    lensSqueezeRatio: float,
    lockTransform: bool,
    motionBlur: bool,
    name: str,
    nearClipPlane: float,
    nearFocusDistance: float,
    orthographic: bool,
    overscan: float,
    orthographicWidth: float,
    position: Tuple[float, float, float],
    preScale: float,
    postScale: float,
    panZoomEnabled: bool,
    rotation: Tuple[float, float, float],
    renderPanZoom: bool,
    shutterAngle: float,
    startupCamera: bool,
    shakeEnabled: bool,
    stereoHorizontalImageTranslateEnabled: bool,
    shakeOverscan: float,
    shakeOverscanEnabled: bool,
    verticalFilmAperture: float,
    verticalFilmOffset: float,
    verticalFieldOfView: float,
    verticalLock: bool,
    verticalPan: float,
    verticalRollPivot: float,
    verticalShake: float,
    worldCenterOfInterest: Tuple[float, float, float],
    worldUp: Tuple[float, float, float],
    zoom: float,
) -> Any:
    ...


def cameraSet(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    active: bool,
    appendTo: bool,
    camera: str,
    clearDepth: bool,
    deleteLayer: bool,
    deleteAll: bool,
    insertAt: bool,
    layer: int,
    name: str,
    numLayers: bool,
    order: int,
    objectSet: str,
) -> Any:
    ...


def cameraView(
    arg0: str,
    /,
    edit: bool,
    addBookmark: bool,
    animate: bool,
    camera: str,
    name: str,
    removeBookmark: bool,
    setCamera: bool,
    setView: bool,
    bookmarkType: int,
) -> Any:
    ...


def canCreateCaddyManip(*args, **kwargs) -> Any:
    ...


def canCreateManip() -> Any:
    ...


def canvas(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    hsvValue: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    pressCommand: Callable,
    popupMenuArray: bool,
    preventOverride: bool,
    rgbValue: Tuple[float, float, float],
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def changeSubdivComponentDisplayLevel(*args, **kwargs) -> Any:
    ...


def changeSubdivRegion(*args, **kwargs) -> Any:
    ...


def channelBox(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    attrColor: Tuple[float, float, float],
    attributeEditorMode: bool,
    attrFilter: str,
    annotation: str,
    attrRegex: str,
    attrBgColor: Tuple[float, float, float],
    backgroundColor: Tuple[float, float, float],
    containerAtTop: bool,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enableLabelSelection: bool,
    enable: bool,
    exists: bool,
    execute: Tuple[str, bool],
    fixedAttrList: Incomplete,
    fullPathName: bool,
    fieldWidth: int,
    height: int,
    highlightColor: Tuple[float, float, float],
    historyObjectList: bool,
    hyperbolic: bool,
    inputs: bool,
    isObscured: bool,
    longNames: bool,
    labelWidth: int,
    manage: bool,
    maxHeight: int,
    mainListConnection: str,
    useManips: str,
    mainObjectList: bool,
    maxWidth: int,
    noBackground: bool,
    niceNames: bool,
    numberOfPopupMenus: bool,
    nodeRegex: str,
    outputObjectList: bool,
    outputs: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    precision: int,
    select: List[str],
    statusBarMessage: str,
    selectedHistoryAttributes: bool,
    shapes: bool,
    selectedMainAttributes: bool,
    showNamespace: bool,
    selectedOutputAttributes: bool,
    shapeObjectList: bool,
    speed: float,
    selectedShapeAttributes: bool,
    showTransforms: bool,
    takeFocus: bool,
    update: bool,
    ufeFixedAttrList: Tuple[str, Incomplete],
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def character(
    *args: List[str],
    edit: bool,
    query: bool,
    addElement: str,
    anyMember: str,
    addOffsetObject: str,
    clear: str,
    characterPlug: bool,
    excludeDynamic: bool,
    empty: bool,
    excludeRotate: bool,
    excludeScale: bool,
    excludeTranslate: bool,
    excludeVisibility: bool,
    forceElement: str,
    flatten: str,
    isIntersecting: str,
    isMember: str,
    include: str,
    intersection: str,
    library: bool,
    memberIndex: int,
    name: str,
    nodesOnly: bool,
    noWarnings: bool,
    offsetNode: bool,
    remove: str,
    removeOffsetObject: str,
    root: str,
    scheduler: bool,
    split: str,
    subtract: str,
    text: str,
    userAlias: str,
    union: str,
) -> Any:
    ...


def characterMap(
    *args: List[str],
    edit: bool,
    query: bool,
    mapping: str,
    mapAttr: Tuple[str, str],
    mapMethod: str,
    mapNode: Tuple[str, str],
    proposedMapping: bool,
    unmapAttr: Tuple[str, str],
    unmapNode: Tuple[str, str],
) -> Any:
    ...


def characterize(
    *args: List[str],
    edit: bool,
    query: bool,
    autoActivateBodyPart: bool,
    addAuxEffector: bool,
    addFloorContactPlane: bool,
    attributeFromHIKProperty: str,
    addMissingEffectors: bool,
    activatePivot: bool,
    changePivotPlacement: bool,
    effectors: str,
    fkSkeleton: str,
    attributeFromHIKPropertyMode: str,
    name: str,
    pinHandFeet: bool,
    placeNewPivot: bool,
    posture: str,
    sourceSkeleton: str,
    stancePose: str,
    type: str,
) -> Any:
    ...


def checkBox(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    align: str,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    editable: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    label: str,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    offCommand: Callable,
    onCommand: Callable,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    recomputeSize: bool,
    statusBarMessage: str,
    useTemplate: str,
    value: bool,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def checkBoxGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    changeCommand: Callable,
    changeCommand1: Callable,
    changeCommand2: Callable,
    changeCommand3: Callable,
    changeCommand4: Callable,
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    editable: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    enable1: bool,
    enable2: bool,
    enable3: bool,
    enable4: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    label: str,
    label1: str,
    label2: str,
    label3: str,
    label4: str,
    labelArray2: Tuple[str, str],
    labelArray3: Tuple[str, str, str],
    labelArray4: Tuple[str, str, str, str],
    manage: bool,
    noBackground: bool,
    numberOfCheckBoxes: int,
    numberOfPopupMenus: bool,
    offCommand1: Callable,
    offCommand2: Callable,
    offCommand3: Callable,
    offCommand4: Callable,
    offCommand: Callable,
    onCommand1: Callable,
    onCommand2: Callable,
    onCommand3: Callable,
    onCommand4: Callable,
    onCommand: Callable,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rowAttach: List[Tuple[int, str, int]],
    statusBarMessage: str,
    useTemplate: str,
    value1: bool,
    value2: bool,
    value3: bool,
    value4: bool,
    valueArray2: Tuple[bool, bool],
    valueArray3: Tuple[bool, bool, bool],
    valueArray4: Tuple[bool, bool, bool, bool],
    visibleChangeCommand: Callable,
    visible: bool,
    vertical: bool,
    width: int,
) -> Any:
    ...


def checkDefaultRenderGlobals(arg0: str, /, edit: bool, query: bool) -> Any:
    ...


def choice(
    *args: List[str],
    edit: bool,
    query: bool,
    attribute: List[str],
    controlPoints: bool,
    index: int,
    name: str,
    shape: bool,
    sourceAttribute: str,
    selector: str,
    time: List[int],
) -> Any:
    ...


def circle(
    *args: List[str],
    edit: bool,
    query: bool,
    center: Tuple[float, float, float],
    caching: bool,
    constructionHistory: bool,
    centerX: float,
    centerY: float,
    centerZ: float,
    degree: int,
    fixCenter: bool,
    first: Tuple[float, float, float],
    firstPointX: float,
    firstPointY: float,
    firstPointZ: float,
    frozen: bool,
    name: str,
    nodeState: int,
    normal: Tuple[float, float, float],
    normalX: float,
    normalY: float,
    normalZ: float,
    object: bool,
    radius: float,
    sections: int,
    sweep: float,
    tolerance: float,
    useTolerance: bool,
) -> Any:
    ...


def circularFillet(
    *args: Tuple[str, str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    curveOnSurface: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    primaryRadius: float,
    positionTolerance: float,
    secondaryRadius: float,
    tangentTolerance: float,
) -> Any:
    ...


def clearCache(*args: List[str], allNodes: bool, computed: bool, dirty: bool) -> Any:
    ...


def clearDynStartState() -> Any:
    ...


def clearNClothStartState() -> Any:
    ...


def clearShear() -> Any:
    ...


def clip(
    *args: List[str],
    edit: bool,
    query: bool,
    active: str,
    allAbsolute: bool,
    absoluteRotations: bool,
    absolute: bool,
    allClips: bool,
    animCurveRange: bool,
    allRelative: bool,
    allSourceClips: bool,
    addTrack: bool,
    copy: bool,
    character: bool,
    constraint: bool,
    duplicate: bool,
    defaultAbsolute: bool,
    endTime: int,
    expression: bool,
    isolate: bool,
    ignoreSubcharacters: bool,
    leaveOriginal: bool,
    mapMethod: str,
    name: List[str],
    newName: str,
    paste: bool,
    pasteInstance: bool,
    rotationsAbsolute: bool,
    remove: bool,
    rotationOffset: Tuple[float, float, float],
    removeTrack: bool,
    startTime: int,
    scheduleClip: bool,
    sourceClipName: bool,
    split: int,
    translationOffset: Tuple[float, float, float],
    useChannel: List[str],
) -> Any:
    ...


def clipEditor(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    autoFit: str,
    autoFitTime: str,
    clipDropCmd: str,
    characterOutline: str,
    clipStyle: int,
    control: bool,
    deselectAll: bool,
    displayActiveKeys: str,
    displayActiveKeyTangents: str,
    deleteCmd: str,
    displayInfinities: str,
    displayKeys: str,
    defineTemplate: str,
    docTag: str,
    displayTangents: str,
    displayValues: str,
    exists: bool,
    filter: str,
    frameAll: bool,
    forceMainConnection: str,
    frameRange: Tuple[float, float],
    highlightedBlend: Tuple[str, str],
    highlightedClip: Tuple[str, str],
    highlightConnection: str,
    initialized: bool,
    lookAt: str,
    listAllCharacters: bool,
    listCurrentCharacters: bool,
    lockMainConnection: bool,
    menuContext: str,
    mainListConnection: str,
    manageSequencer: bool,
    parent: str,
    panel: str,
    selectBlend: Tuple[str, str, str],
    selectClip: Tuple[str, str],
    selectionConnection: str,
    snapTime: str,
    stateString: bool,
    snapValue: str,
    unlockMainConnection: bool,
    unParent: bool,
    updateMainConnection: bool,
    useTemplate: str,
) -> Any:
    ...


def clipEditorCurrentTimeCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def clipMatching(
    *args: List[str],
    clipDst: Tuple[str, float],
    clipSrc: Tuple[str, float],
    matchRotation: int,
    matchTranslation: int,
) -> Any:
    ...


def clipSchedule(
    *args: List[str],
    edit: bool,
    query: bool,
    allAbsolute: bool,
    allRelative: bool,
    blend: Tuple[int, int],
    blendNode: Tuple[int, int],
    blendUsingNode: str,
    cycle: float,
    character: bool,
    clipIndex: int,
    defaultAbsolute: bool,
    enable: bool,
    groupName: str,
    groupIndex: List[int],
    group: bool,
    instance: str,
    insertTrack: int,
    lock: bool,
    listCurves: bool,
    listPairs: bool,
    mute: bool,
    name: str,
    hold: int,
    postCycle: float,
    preCycle: float,
    rotationsAbsolute: bool,
    removeBlend: Tuple[int, int],
    removeEmptyTracks: bool,
    remove: bool,
    removeTrack: int,
    start: int,
    scale: float,
    sourceClipName: bool,
    sourceEnd: int,
    shift: int,
    shiftIndex: List[int],
    solo: bool,
    sourceStart: int,
    track: int,
    weight: float,
    weightStyle: int,
) -> Any:
    ...


def clipSchedulerOutliner(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    clipScheduler: str,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def closeCurve(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    blendBias: float,
    blendKnotInsertion: bool,
    caching: bool,
    constructionHistory: bool,
    curveOnSurface: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    parameter: float,
    preserveShape: int,
    replaceOriginal: bool,
) -> Any:
    ...


def closeSurface(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    blendBias: float,
    blendKnotInsertion: bool,
    caching: bool,
    constructionHistory: bool,
    direction: int,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    parameter: float,
    preserveShape: int,
    replaceOriginal: bool,
) -> Any:
    ...


def cluster(
    *args: List[str],
    edit: bool,
    query: bool,
    after: bool,
    afterReference: bool,
    before: bool,
    bindState: bool,
    components: bool,
    selectedComponents: bool,
    deformerTools: bool,
    envelope: float,
    exclusive: str,
    frontOfChain: bool,
    geometry: List[str],
    geometryIndices: bool,
    includeHiddenSelections: bool,
    ignoreSelected: bool,
    name: str,
    parallel: bool,
    prune: bool,
    relative: bool,
    resetGeometry: bool,
    remove: List[bool],
    split: bool,
    useComponentTags: bool,
    weightedNode: Tuple[str, str],
) -> Any:
    ...


def cmdFileOutput(
    query: bool, close: int, closeAll: bool, open: str, status: int
) -> Any:
    ...


def cmdScrollFieldExecuter(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    autoCloseBraces: bool,
    annotation: str,
    appendText: str,
    backgroundColor: Tuple[float, float, float],
    commandCompletion: bool,
    currentLine: int,
    clear: bool,
    copySelection: bool,
    cutSelection: bool,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    executeAll: bool,
    execute: bool,
    fileChangedCommand: Callable,
    filterKeyPress: Callable,
    filename: bool,
    fullPathName: bool,
    height: int,
    hasFocus: bool,
    highlightColor: Tuple[float, float, float],
    hasSelection: bool,
    isObscured: bool,
    indentSelection: bool,
    insertText: str,
    load: bool,
    loadContents: str,
    loadFile: str,
    manage: bool,
    modificationChangedCommand: Callable,
    modified: bool,
    noBackground: bool,
    numberOfLines: bool,
    numberOfPopupMenus: bool,
    objectPathCompletion: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    pasteSelection: bool,
    redo: bool,
    receiveFocusCommand: Callable,
    replaceAll: Tuple[str, str],
    removeStoredContents: str,
    searchAndSelect: bool,
    statusBarMessage: str,
    searchDown: bool,
    select: Tuple[int, int],
    selectAll: bool,
    showLineNumbers: bool,
    selectedText: bool,
    searchMatchCase: bool,
    spacesPerTab: int,
    source: bool,
    searchString: str,
    sourceType: str,
    storeContents: str,
    showTooltipHelp: bool,
    showTabsAndSpaces: bool,
    saveSelection: str,
    saveFile: str,
    saveSelectionToShelf: bool,
    searchWraps: bool,
    text: str,
    tabsForIndent: bool,
    textLength: bool,
    undo: bool,
    unindentSelection: bool,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def cmdScrollFieldReporter(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    clear: bool,
    copySelection: bool,
    cutSelection: bool,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    echoAllCommands: bool,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    filterSourceType: str,
    height: int,
    hasFocus: bool,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    lineNumbers: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    pasteSelection: bool,
    receiveFocusCommand: Callable,
    statusBarMessage: str,
    suppressErrors: bool,
    suppressInfo: bool,
    select: Tuple[int, int],
    selectAll: bool,
    suppressResults: bool,
    suppressStackTrace: bool,
    stackTrace: bool,
    saveSelection: str,
    saveSelectionToShelf: bool,
    suppressWarnings: bool,
    text: str,
    textLength: bool,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def cmdShell(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    command: str,
    clear: bool,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfHistoryLines: int,
    numberOfPopupMenus: bool,
    numberOfSavedLines: int,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    prompt: str,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def coarsenSubdivSelectionList(*args, **kwargs) -> Any:
    ...


def collision(
    *args: List[str],
    edit: bool,
    query: bool,
    friction: float,
    name: str,
    offset: float,
    resilience: float,
) -> Any:
    ...


def color(
    *args: List[str], rgbColor: Tuple[float, float, float], userDefined: int
) -> Any:
    ...


def colorAtPoint(
    *args: List[str],
    minU: float,
    minV: float,
    output: str,
    samplesU: int,
    samplesV: int,
    coordU: List[float],
    coordV: List[float],
    maxU: float,
    maxV: float,
) -> Any:
    ...


def colorEditor(
    query: bool,
    alpha: float,
    hsvValue: Tuple[float, float, float],
    mini: bool,
    parent: str,
    position: Tuple[int, int],
    result: bool,
    rgbValue: Tuple[float, float, float],
) -> Any:
    ...


def colorIndex(
    *args: Tuple[int, float, float, float],
    query: bool,
    hueSaturationValue: bool,
    resetToFactory: bool,
    resetToSaved: bool,
) -> Any:
    ...


def colorIndexSliderGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    changeCommand: Callable,
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    dragCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    extraLabel: str,
    enable: bool,
    exists: bool,
    forceDragRefresh: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    invisible: int,
    isObscured: bool,
    label: str,
    manage: bool,
    maxValue: int,
    minValue: int,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rowAttach: List[Tuple[int, str, int]],
    statusBarMessage: str,
    useTemplate: str,
    value: int,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def colorInputWidgetGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    alphaValue: float,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    changeCommand: Callable,
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    hsvValue: float,
    isObscured: bool,
    label: str,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rowAttach: List[Tuple[int, str, int]],
    rgbValue: Tuple[float, float, float],
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def colorManagementCatalog(
    addTransform: str,
    editUserTransformPath: str,
    listSupportedExtensions: bool,
    listTransformConnections: bool,
    path: str,
    queryUserTransformPath: bool,
    removeTransform: str,
    transformConnection: str,
    type: str,
) -> Any:
    ...


def colorManagementConvert(toDisplaySpace: Tuple[float, float, float]) -> Any:
    ...


def colorManagementFileRules(
    *args: List[str],
    edit: bool,
    query: bool,
    addRule: str,
    colorSpace: str,
    colorSpaceDescription: str,
    colorSpaceFamilies: str,
    colorSpaceNames: bool,
    down: str,
    enabled: bool,
    evaluate: str,
    extension: str,
    load: bool,
    listRules: bool,
    pattern: str,
    restoreDefaults: bool,
    remove: str,
    save: bool,
    moveUp: str,
) -> Any:
    ...


def colorManagementPrefs(
    edit: bool,
    query: bool,
    cmConfigFileEnabled: bool,
    configFilePath: str,
    configFileVersion: str,
    colorManageAllNodes: bool,
    cmEnabled: bool,
    colorManagedNodes: bool,
    colorManagePots: bool,
    colorManagementSDKVersion: str,
    defaultInputSpaceName: str,
    displayName: str,
    displayNames: bool,
    exportPolicy: str,
    equalsToPolicyFile: str,
    inhibitEvents: bool,
    inputSpaceDescription: str,
    inputSpaceFamilies: str,
    inputSpaceNames: bool,
    loadedDisplayName: str,
    loadedDefaultInputSpaceName: str,
    loadedOutputTransformName: str,
    loadPolicy: str,
    loadedRenderingSpaceName: str,
    loadedViewName: str,
    loadedViewTransformName: str,
    missingColorSpaceNodes: bool,
    ociov2Enabled: bool,
    ocioRulesEnabled: bool,
    outputTransformUseColorConversion: bool,
    outputTransformEnabled: bool,
    outputTransformName: str,
    outputTransformNames: bool,
    outputTarget: str,
    outputUseViewTransform: bool,
    policyFileName: str,
    popupOnError: bool,
    restoreDefaults: bool,
    refresh: bool,
    renderingSpaceName: str,
    renderingSpaceNames: bool,
    viewDisplayNames: str,
    viewName: str,
    viewNames: bool,
    viewTransformName: str,
    viewTransformNames: bool,
) -> Any:
    ...


def colorSliderButtonGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    alphaValue: float,
    annotation: str,
    buttonCommand: Callable,
    backgroundColor: Tuple[float, float, float],
    buttonLabel: str,
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    changeCommand: Callable,
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    dragCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    forceDragRefresh: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    hsvValue: Tuple[float, float, float],
    image: str,
    isObscured: bool,
    label: str,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rowAttach: List[Tuple[int, str, int]],
    rgbValue: Tuple[float, float, float],
    symbolButtonCommand: Callable,
    symbolButtonDisplay: bool,
    statusBarMessage: str,
    useDisplaySpace: bool,
    useTemplate: str,
    visibleChangeCommand: Callable,
    useVpColorPicker: bool,
    visible: bool,
    width: int,
) -> Any:
    ...


def colorSliderGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    alphaValue: float,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    changeCommand: Callable,
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    dragCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    forceDragRefresh: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    hsvValue: Tuple[float, float, float],
    isObscured: bool,
    label: str,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rowAttach: List[Tuple[int, str, int]],
    rgbValue: Tuple[float, float, float],
    statusBarMessage: str,
    useDisplaySpace: bool,
    useTemplate: str,
    visibleChangeCommand: Callable,
    useVpColorPicker: bool,
    visible: bool,
    width: int,
) -> Any:
    ...


def columnLayout(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    childArray: bool,
    columnAlign: str,
    columnAttach: Tuple[str, int],
    columnOffset: Tuple[str, int],
    columnWidth: int,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfChildren: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rowSpacing: int,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def combinationShape(
    *args: List[Incomplete],
    edit: bool,
    query: bool,
    addDriver: bool,
    allDrivers: bool,
    blendShape: str,
    combineMethod: int,
    combinationTargetIndex: int,
    combinationTargetName: str,
    driverTargetIndex: List[int],
    driverTargetName: List[str],
    exist: bool,
    removeDriver: bool,
) -> Any:
    ...


def commandEcho(
    query: bool,
    addFilter: Incomplete,
    filter: Incomplete,
    lineNumbers: bool,
    state: bool,
) -> Any:
    ...


def commandLine(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    command: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enterCommand: Callable,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    holdFocus: bool,
    highlightColor: Tuple[float, float, float],
    inputAnnotation: str,
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfHistoryLines: int,
    numberOfPopupMenus: bool,
    outputAnnotation: str,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    sourceType: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def commandLogging(
    query: bool,
    historySize: int,
    logCommands: bool,
    logFile: str,
    recordCommands: bool,
    resetLogFile: bool,
) -> Any:
    ...


def commandPort(
    arg0: str,
    /,
    query: bool,
    bufferSize: int,
    close: bool,
    echoOutput: bool,
    listPorts: bool,
    name: str,
    noreturn: bool,
    outputVar: str,
    pickleOutput: bool,
    prefix: str,
    returnNumCommands: bool,
    sourceType: str,
    securityWarning: bool,
) -> Any:
    ...


def componentBox(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    execute: Tuple[str, bool],
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    labelWidth: int,
    manage: bool,
    maxHeight: int,
    maxWidth: int,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    precision: int,
    rowHeight: int,
    statusBarMessage: str,
    selectedAttr: bool,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def componentEditor(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    control: bool,
    defineTemplate: str,
    docTag: str,
    exists: bool,
    filter: str,
    floatField: str,
    forceMainConnection: str,
    floatSlider: str,
    highlightConnection: str,
    hidePathName: bool,
    hideZeroColumns: bool,
    justifyHeaders: int,
    lockMainConnection: bool,
    lockInput: bool,
    mainListConnection: str,
    newTab: Tuple[str, str, str],
    normalizeWeights: int,
    operationCount: bool,
    operationLabels: bool,
    operationType: int,
    parent: str,
    panel: str,
    precision: int,
    removeTab: str,
    sortAlpha: bool,
    selected: bool,
    selectionConnection: str,
    showNamespaces: bool,
    showObjects: bool,
    setOperationLabel: Tuple[int, str],
    showSelected: bool,
    stateString: bool,
    unlockMainConnection: bool,
    unParent: bool,
    updateMainConnection: bool,
    useTemplate: str,
) -> Any:
    ...


def condition(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    dependency: List[str],
    delete: bool,
    initialize: bool,
    script: str,
    state: bool,
) -> Any:
    ...


def cone(
    *args: List[str],
    edit: bool,
    query: bool,
    axis: Tuple[float, float, float],
    caching: bool,
    constructionHistory: bool,
    degree: int,
    endSweep: float,
    frozen: bool,
    heightRatio: float,
    name: str,
    nodeState: int,
    spans: int,
    object: bool,
    useOldInitBehaviour: bool,
    pivot: Tuple[float, float, float],
    polygon: int,
    radius: float,
    sections: int,
    startSweep: float,
    tolerance: float,
    useTolerance: bool,
) -> Any:
    ...


def confirmDialog(
    annotation: List[str],
    button: List[str],
    backgroundColor: Tuple[float, float, float],
    cancelButton: str,
    defaultButton: str,
    dismissString: str,
    icon: str,
    message: str,
    messageAlign: str,
    parent: str,
    title: str,
) -> Any:
    ...


def connectAttr(
    *args: Tuple[str, str],
    force: bool,
    lock: bool,
    nextAvailable: bool,
    referenceDest: str,
) -> Any:
    ...


def connectControl(
    *args: List[Incomplete],
    fileName: bool,
    includeChildren: bool,
    index: int,
    preventContextualMenu: bool,
    preventOverride: bool,
) -> Any:
    ...


def connectDynamic(
    *args: List[str],
    addScriptHandler: Callable,
    collisions: List[str],
    delete: bool,
    emitters: List[str],
    fields: List[str],
    removeScriptHandler: int,
) -> Any:
    ...


def connectJoint(*args: Tuple[str, str], connectMode: bool, parentMode: bool) -> Any:
    ...


def connectionInfo(
    arg0: str,
    /,
    destinationFromSource: bool,
    getExactDestination: bool,
    getExactSource: bool,
    getLockedAncestor: bool,
    isDestination: bool,
    isExactDestination: bool,
    isExactSource: bool,
    isLocked: bool,
    isSource: bool,
    sourceFromDestination: bool,
) -> Any:
    ...


def constrain(
    *args: List[str],
    edit: bool,
    query: bool,
    barrier: bool,
    damping: float,
    directionalHinge: bool,
    hinge: bool,
    interpenetrate: bool,
    name: str,
    nail: bool,
    orientation: Tuple[float, float, float],
    position: Tuple[float, float, float],
    pinConstraint: bool,
    restLength: float,
    spring: bool,
    stiffness: float,
) -> Any:
    ...


def constructionHistory(query: bool, toggle: bool) -> Any:
    ...


def container(
    *args: List[str],
    edit: bool,
    query: bool,
    asset: Incomplete,
    assetMember: str,
    addNode: Incomplete,
    bindAttr: Tuple[str, str],
    current: bool,
    connectionList: bool,
    force: bool,
    findContainer: Incomplete,
    fileName: Incomplete,
    includeHierarchyAbove: bool,
    includeHierarchyBelow: bool,
    includeNetwork: bool,
    includeNetworkDetails: List[str],
    isContainer: bool,
    includeShaders: bool,
    includeShapes: bool,
    includeTransform: bool,
    name: str,
    nodeList: bool,
    nodeNamePrefix: bool,
    preview: bool,
    publishAttr: str,
    publishAsChild: Tuple[str, str],
    publishAsParent: Tuple[str, str],
    parentContainer: bool,
    publishAndBind: Tuple[str, str],
    publishConnections: bool,
    publishName: str,
    publishAsRoot: Tuple[str, bool],
    removeContainer: bool,
    removeNode: Incomplete,
    type: str,
    unbindAttr: Tuple[str, str],
    unbindAndUnpublish: str,
    unpublishName: str,
    unbindChild: str,
    unbindParent: str,
    unpublishChild: str,
    unpublishParent: str,
    unsortedOrder: bool,
) -> Any:
    ...


def containerBind(
    *args: List[str],
    edit: bool,
    query: bool,
    allNames: bool,
    bindingSet: str,
    bindingSetConditions: bool,
    bindingSetList: bool,
    force: bool,
    preview: bool,
) -> Any:
    ...


def containerProxy(
    *args: List[str], edit: bool, query: bool, fromTemplate: str, type: str
) -> Any:
    ...


def containerPublish(
    *args: List[str],
    edit: bool,
    query: bool,
    bindNode: Tuple[str, str],
    bindTemplateStandins: bool,
    inConnections: bool,
    mergeShared: bool,
    outConnections: bool,
    publishNode: Tuple[str, str],
    unbindNode: str,
    unpublishNode: str,
) -> Any:
    ...


def containerTemplate(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    addBindingSet: str,
    allKeyable: bool,
    attributeList: str,
    addNames: bool,
    attribute: List[str],
    addView: str,
    baseName: str,
    bindingSetList: str,
    childAnchor: bool,
    delete: bool,
    expandCompounds: bool,
    exists: bool,
    force: bool,
    fromContainer: str,
    fileName: str,
    fromSelection: bool,
    load: bool,
    layoutMode: int,
    matchFile: str,
    matchName: str,
    parentAnchor: bool,
    publishedNodeList: str,
    removeBindingSet: str,
    rootTransform: bool,
    removeView: str,
    save: bool,
    silent: bool,
    searchPath: str,
    templateList: str,
    unload: bool,
    updateBindingSet: str,
    useHierarchy: bool,
    viewList: str,
) -> Any:
    ...


def containerView(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    itemInfo: str,
    itemList: bool,
    viewLabel: bool,
    viewDescription: bool,
    viewList: bool,
    viewName: str,
) -> Any:
    ...


def contentBrowser(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    addContentPath: str,
    control: bool,
    context: Tuple[str, Incomplete, str, str, Incomplete],
    defineTemplate: str,
    docTag: str,
    exists: bool,
    filter: str,
    forceMainConnection: str,
    highlightConnection: str,
    lockMainConnection: bool,
    location: str,
    mainListConnection: str,
    parent: str,
    panel: str,
    preview: bool,
    removeContentPath: str,
    refreshTreeView: bool,
    saveCurrentContext: bool,
    selectionConnection: str,
    stateString: bool,
    thumbnailView: bool,
    treeView: bool,
    unlockMainConnection: bool,
    unParent: bool,
    updateMainConnection: bool,
    useTemplate: str,
) -> Any:
    ...


def contextInfo(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    c: bool,
    escapeContext: bool,
    exists: bool,
    image1: bool,
    image2: bool,
    image3: bool,
    apiImage1: str,
    title: bool,
) -> Any:
    ...


def control(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def controller(
    *args: List[str],
    edit: bool,
    query: bool,
    allControllers: bool,
    children: bool,
    group: bool,
    isController: str,
    index: int,
    parent: bool,
    pickWalkDown: bool,
    pickWalkLeft: bool,
    pickWalkRight: bool,
    pickWalkUp: bool,
    unparent: bool,
) -> Any:
    ...


def convertIffToPsd(
    query: bool, iffFileName: str, psdFileName: str, xResolution: int, yResolution: int
) -> Any:
    ...


def convertSolidTx(
    *args: List[str],
    edit: bool,
    query: bool,
    antiAlias: bool,
    alpha: bool,
    backgroundColor: Tuple[int, int, int],
    backgroundMode: str,
    camera: str,
    componentRange: bool,
    doubleSided: bool,
    force: bool,
    fileFormat: str,
    fileImageName: str,
    fillTextureSeams: bool,
    fullUvRange: bool,
    name: str,
    pixelFormat: str,
    reuseDepthMap: bool,
    resolutionX: int,
    resolutionY: int,
    shadows: bool,
    samplePlane: bool,
    samplePlaneRange: Tuple[float, float, float, float],
    uvBBoxIntersect: bool,
    uvSetName: str,
    uvRange: Tuple[float, float, float, float],
) -> Any:
    ...


def convertTessellation(*args: List[str], allCameras: bool, camera: str) -> Any:
    ...


def convertUnit(*args: List[Incomplete], fromUnit: str, toUnit: str) -> Any:
    ...


def copyAttr(
    *args: List[str],
    edit: bool,
    query: bool,
    attribute: List[str],
    containerParentChild: bool,
    inConnections: bool,
    keepSourceConnections: bool,
    outConnections: bool,
    renameTargetContainer: bool,
    values: bool,
) -> Any:
    ...


def copyDeformerWeights(
    *args: List[str],
    edit: bool,
    query: bool,
    destinationDeformer: str,
    destinationShape: str,
    mirrorInverse: bool,
    mirrorMode: str,
    noMirror: bool,
    surfaceAssociation: str,
    sourceDeformer: str,
    smooth: bool,
    sourceShape: str,
    uvSpace: Tuple[str, str],
) -> Any:
    ...


def copyFlexor() -> Any:
    ...


def copyKey(
    *args: List[str],
    animLayer: str,
    animation: str,
    attribute: List[str],
    clipboard: str,
    controlPoints: bool,
    float: List[Incomplete],
    forceIndependentEulerAngles: bool,
    hierarchy: str,
    index: List[Incomplete],
    includeUpperBound: bool,
    option: str,
    shape: bool,
    time: List[Incomplete],
) -> Any:
    ...


def copyNode() -> Any:
    ...


def copySkinWeights(
    *args: List[str],
    edit: bool,
    query: bool,
    destinationSkin: str,
    influenceAssociation: List[str],
    mirrorInverse: bool,
    mirrorMode: str,
    noBlendWeight: bool,
    noMirror: bool,
    normalize: bool,
    surfaceAssociation: str,
    smooth: bool,
    sampleSpace: int,
    sourceSkin: str,
    uvSpace: Tuple[str, str],
) -> Any:
    ...


def crashInfo(
    query: bool, crashFile: bool, crashLog: bool, savedBeforeCrash: bool
) -> Any:
    ...


def crashInfoCmd(*args, **kwargs) -> Any:
    ...


def createAttrPatterns(
    patternDefinition: str, patternFile: str, patternType: str
) -> Any:
    ...


def createDisplayLayer(
    *args: List[str],
    empty: bool,
    makeCurrent: bool,
    name: str,
    noRecurse: bool,
    number: int,
) -> Any:
    ...


def createEditor(
    *args: Tuple[str, str], noCloseOnDelete: bool, queueForDelete: bool
) -> Any:
    ...


def createLayeredPsdFile(*args, **kwargs) -> Any:
    ...


def createNode(
    type_name: str, /, name: str, parent: str, shared: bool, skipSelect: bool
) -> str:
    """createNode is undoable, **NOT queryable**, and **NOT editable**.

    This command creates a new node in the dependency graph of the specified type.

    Args:
        name: Sets the name of the newly-created node. If it contains namespace path,  the new node will be created under the specified namespace; if the namespace doesn't exist,  we will create the namespace.
        parent: Specifies the parent in the DAG under which the new node belongs.
        shared: This node is shared across multiple files,  so only create it if it does not already exist.
        skipSelect: This node is not to be selected after creation,  the original selection will be preserved.

    Returns:
        The name of the new node.

    Examples:
        >>> from maya import cmds
        >>> cmds.createNode('transform', n='transform1')
        >>> cmds.createNode('nurbsSurface', n='surface1', p='transform1')
        >>> cmds.createNode('camera', shared=True, n='top')
        >>> # This transform will be selected when created
        >>> cmds.createNode('transform', n='selectedTransform')
        >>> # This will create a new transform node, but 'selectedTransform'
        >>> # will still be selected.
        >>> cmds.createNode('transform', ss=True)
        >>> # Create node under new namespace
        >>> cmds.createNode('transform', n='newNS:transform1')
    """


def createNurbsCircleCtx(*args, **kwargs) -> Any:
    ...


def createNurbsConeCtx(*args, **kwargs) -> Any:
    ...


def createNurbsCubeCtx(*args, **kwargs) -> Any:
    ...


def createNurbsCylinderCtx(*args, **kwargs) -> Any:
    ...


def createNurbsPlaneCtx(*args, **kwargs) -> Any:
    ...


def createNurbsSphereCtx(*args, **kwargs) -> Any:
    ...


def createNurbsSquareCtx(*args, **kwargs) -> Any:
    ...


def createNurbsTorusCtx(*args, **kwargs) -> Any:
    ...


def createPolyConeCtx(*args, **kwargs) -> Any:
    ...


def createPolyCubeCtx(*args, **kwargs) -> Any:
    ...


def createPolyCylinderCtx(*args, **kwargs) -> Any:
    ...


def createPolyHelixCtx(*args, **kwargs) -> Any:
    ...


def createPolyPipeCtx(*args, **kwargs) -> Any:
    ...


def createPolyPlaneCtx(*args, **kwargs) -> Any:
    ...


def createPolyPlatonicSolidCtx(*args, **kwargs) -> Any:
    ...


def createPolyPrismCtx(*args, **kwargs) -> Any:
    ...


def createPolyPyramidCtx(*args, **kwargs) -> Any:
    ...


def createPolySoccerBallCtx(*args, **kwargs) -> Any:
    ...


def createPolySphereCtx(*args, **kwargs) -> Any:
    ...


def createPolyTorusCtx(*args, **kwargs) -> Any:
    ...


def createRenderLayer(
    *args: List[str],
    empty: bool,
    g: bool,
    makeCurrent: bool,
    name: str,
    noRecurse: bool,
    number: int,
) -> Any:
    ...


def createSubdivRegion(*args, **kwargs) -> Any:
    ...


def ctxAbort() -> Any:
    ...


def ctxCompletion() -> Any:
    ...


def ctxEditMode(buttonDown: bool, buttonUp: bool) -> Any:
    ...


def ctxTraverse(down: bool, left: bool, right: bool) -> Any:
    ...


def currentCtx() -> Any:
    ...


def currentTime(arg0: int, /, edit: bool, query: bool, update: bool) -> Any:
    ...


def currentTimeCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def currentUnit(
    *args: List[str],
    query: bool,
    angle: str,
    fullName: bool,
    linear: str,
    time: str,
    updateAnimation: bool,
) -> Any:
    ...


def curve(
    *args: List[str],
    append: bool,
    bezier: bool,
    degree: float,
    editPoint: List[Tuple[float, float, float]],
    knot: List[float],
    name: str,
    objectSpace: bool,
    point: List[Tuple[float, float, float]],
    periodic: bool,
    pointWeight: List[Tuple[float, float, float, float]],
    replace: bool,
    worldSpace: bool,
) -> Any:
    ...


def curveAddPtCtx(*args, **kwargs) -> Any:
    ...


def curveBezierCtx(*args, **kwargs) -> Any:
    ...


def curveCVCtx(*args, **kwargs) -> Any:
    ...


def curveEPCtx(*args, **kwargs) -> Any:
    ...


def curveEditorCtx(*args, **kwargs) -> Any:
    ...


def curveIntersect(
    *args: Tuple[str, str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    direction: Tuple[float, float, float],
    directionX: float,
    directionY: float,
    directionZ: float,
    frozen: bool,
    nodeState: int,
    tolerance: float,
    useDirection: bool,
) -> Any:
    ...


def curveMoveEPCtx(*args, **kwargs) -> Any:
    ...


def curveOnSurface(
    *args: List[Incomplete],
    append: bool,
    degree: float,
    knot: List[float],
    name: str,
    periodic: bool,
    replace: bool,
    positionUV: List[Tuple[float, float]],
) -> Any:
    ...


def curveRGBColor(
    *args: Tuple[str, float, float, float],
    query: bool,
    hueSaturationValue: bool,
    list: bool,
    listNames: bool,
    remove: bool,
    resetToFactory: bool,
    resetToSaved: bool,
) -> Any:
    ...


def curveSketchCtx(*args, **kwargs) -> Any:
    ...


def cutKey(
    *args: List[str],
    animation: str,
    attribute: List[str],
    clear: bool,
    controlPoints: bool,
    float: List[Incomplete],
    hierarchy: str,
    index: List[Incomplete],
    includeUpperBound: bool,
    option: str,
    shape: bool,
    selectKey: bool,
    time: List[Incomplete],
) -> Any:
    ...


def cycleCheck(
    *args: List[str],
    query: bool,
    children: bool,
    evaluation: bool,
    firstCycleOnly: bool,
    firstPlugPerNode: bool,
    list: bool,
    lastPlugPerNode: bool,
    listSeparator: str,
    parents: bool,
    secondary: bool,
    timeLimit: int,
) -> Any:
    ...


def cylinder(
    *args: List[str],
    edit: bool,
    query: bool,
    axis: Tuple[float, float, float],
    caching: bool,
    constructionHistory: bool,
    degree: int,
    endSweep: float,
    frozen: bool,
    heightRatio: float,
    name: str,
    nodeState: int,
    spans: int,
    object: bool,
    pivot: Tuple[float, float, float],
    polygon: int,
    radius: float,
    sections: int,
    startSweep: float,
    tolerance: float,
    useTolerance: bool,
) -> Any:
    ...


def dagCommandWrapper() -> Any:
    ...


def dagObjectCompare(
    *args: List[str],
    attribute: bool,
    bail: str,
    connection: bool,
    namespace: str,
    relative: bool,
    short: bool,
    type: bool,
) -> Any:
    ...


def dagObjectHit(cache: bool, multiple: bool, menu: str, targetSize: int) -> Any:
    ...


def dagPose(
    *args: List[str],
    edit: bool,
    query: bool,
    addToPose: bool,
    atPose: bool,
    bindPose: bool,
    g: bool,
    members: bool,
    name: str,
    restore: bool,
    remove: bool,
    reset: bool,
    save: bool,
    selection: bool,
    worldParent: bool,
) -> Any:
    ...


def dataStructure(
    query: bool,
    asFile: str,
    asString: str,
    dataType: bool,
    format: str,
    listMemberNames: str,
    name: str,
    removeAll: bool,
    remove: bool,
) -> Any:
    ...


def date(date: bool, format: str, shortDate: bool, shortTime: bool, time: bool) -> Any:
    ...


def dbcount(
    enabled: bool,
    file: str,
    keyword: str,
    list: bool,
    maxdepth: int,
    quick: bool,
    reset: bool,
    spreadsheet: bool,
) -> Any:
    ...


def dbfootprint(
    *args: List[str], query: bool, allObjects: bool, outputFile: str, type: str
) -> Any:
    ...


def dbmessage(file: str, list: bool, monitor: bool, type: str) -> Any:
    ...


def dbpeek(
    *args: List[str],
    query: bool,
    argument: List[str],
    allObjects: bool,
    count: int,
    evaluationGraph: bool,
    outputFile: str,
    operation: str,
) -> Any:
    ...


def dbtrace(
    query: bool,
    filter: str,
    info: bool,
    keyword: List[str],
    mark: bool,
    output: str,
    title: str,
    timed: bool,
    verbose: bool,
) -> Any:
    ...


def debug(*args, **kwargs) -> Any:
    ...


def debugNamespace(*args, **kwargs) -> Any:
    ...


def debugVar(*args, **kwargs) -> Any:
    ...


def defaultLightListCheckBox(*args, **kwargs) -> Any:
    ...


def defaultNavigation(
    *args: Tuple[str, str],
    connectToExisting: bool,
    createNew: bool,
    destination: str,
    defaultAttribute: bool,
    delete: bool,
    disconnect: bool,
    defaultTraversal: bool,
    defaultWorkingNode: bool,
    force: bool,
    ignore: bool,
    navigatorDecisionString: str,
    quiet: bool,
    relatedNodes: bool,
    source: str,
    unignore: bool,
) -> Any:
    ...


def defineDataServer(*args, **kwargs) -> Any:
    ...


def defineVirtualDevice(*args, **kwargs) -> Any:
    ...


def deformableShape(
    *args: List[str],
    chain: bool,
    createOriginalGeometry: bool,
    createUpstreamTagInjectionNode: bool,
    createTweakNode: bool,
    deformShapeInAttr: bool,
    deformShapeOutAttr: bool,
    frontOfChain: bool,
    localShapeInAttr: bool,
    localShapeOutAttr: bool,
    nodeChain: bool,
    outputPlugChain: bool,
    originalGeometry: bool,
    plugChain: bool,
    supportsComponentTags: bool,
    tagInjectionNode: bool,
    tagInjectionList: bool,
    tweakNode: bool,
    upstreamTagInjectionNode: bool,
    worldShapeOutAttr: bool,
) -> Any:
    ...


def deformer(
    *args: List[str],
    edit: bool,
    query: bool,
    after: bool,
    afterReference: bool,
    before: bool,
    components: bool,
    selectedComponents: bool,
    deformerTools: bool,
    exclusive: str,
    frontOfChain: bool,
    geometry: List[str],
    geometryIndices: bool,
    includeHiddenSelections: bool,
    ignoreSelected: bool,
    name: str,
    parallel: bool,
    prune: bool,
    remove: List[bool],
    split: bool,
    type: str,
    useComponentTags: bool,
) -> Any:
    ...


def deformerWeights(
    *args: List[str],
    edit: bool,
    query: bool,
    attribute: List[str],
    deformer: List[str],
    defaultValue: float,
    export: bool,
    format: str,
    ignoreName: bool,
    im: bool,
    method: str,
    path: str,
    positionTolerance: float,
    remap: List[str],
    shape: List[str],
    skip: List[str],
    vertexConnections: bool,
    weightPrecision: int,
    worldSpace: bool,
    weightTolerance: float,
) -> Any:
    ...


def delete(
    *args: List[str],
    attribute: List[str],
    channels: bool,
    constructionHistory: bool,
    constraints: bool,
    controlPoints: bool,
    expressions: bool,
    hierarchy: str,
    inputConnectionsAndNodes: bool,
    motionPaths: bool,
    shape: bool,
    staticChannels: bool,
    timeAnimationCurves: bool,
    unitlessAnimationCurves: bool,
) -> Any:
    ...


def deleteAttr(*args: List[str], edit: bool, query: bool, attribute: str) -> Any:
    ...


def deleteAttrPattern(allPatterns: bool, patternName: str, patternType: str) -> Any:
    ...


def deleteExtension(attribute: str, forceDelete: bool, nodeType: str) -> Any:
    ...


def deleteGeometryCache() -> Any:
    ...


def deleteHistoryAheadOfGeomCache() -> Any:
    ...


def deleteNclothCache() -> Any:
    ...


def deleteUI(
    *args: List[str],
    collection: bool,
    control: bool,
    editor: bool,
    layout: bool,
    menu: bool,
    menuItem: bool,
    panelConfig: bool,
    panel: bool,
    radioMenuItemCollection: bool,
    toolContext: bool,
    uiTemplate: bool,
    window: bool,
) -> Any:
    ...


def deltaMush(
    *args: List[str],
    edit: bool,
    query: bool,
    after: bool,
    afterReference: bool,
    before: bool,
    components: bool,
    selectedComponents: bool,
    deformerTools: bool,
    envelope: float,
    exclusive: str,
    frontOfChain: bool,
    geometry: List[str],
    geometryIndices: bool,
    includeHiddenSelections: bool,
    ignoreSelected: bool,
    inwardConstraint: float,
    name: str,
    outwardConstraint: float,
    parallel: bool,
    pinBorderVertices: bool,
    prune: bool,
    remove: List[bool],
    smoothingIterations: int,
    split: bool,
    smoothingStep: float,
    useComponentTags: bool,
) -> Any:
    ...


def detachCurve(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    curveOnSurface: bool,
    frozen: bool,
    keep: List[bool],
    name: str,
    nodeState: int,
    object: bool,
    parameter: List[float],
    replaceOriginal: bool,
) -> Any:
    ...


def detachDeviceAttr(*args, **kwargs) -> Any:
    ...


def detachSurface(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    direction: int,
    frozen: bool,
    keep: List[bool],
    name: str,
    nodeState: int,
    object: bool,
    parameter: List[float],
    replaceOriginal: bool,
) -> Any:
    ...


def deviceEditor(*args, **kwargs) -> Any:
    ...


def deviceManager(*args, **kwargs) -> Any:
    ...


def devicePanel(*args, **kwargs) -> Any:
    ...


def dgControl(*args, **kwargs) -> Any:
    ...


def dgInfo(
    *args: List[str],
    allNodes: bool,
    connections: bool,
    dirty: bool,
    nodes: bool,
    nonDeletable: bool,
    type: str,
    outputFile: str,
    propagation: bool,
    short: bool,
    subgraph: bool,
    size: bool,
) -> Any:
    ...


def dgPerformance(*args, **kwargs) -> Any:
    ...


def dgValidateCurve(*args: List[str], allCurves: bool, verbose: bool) -> Any:
    ...


def dgcontrol(*args: List[str], iomode: bool) -> Any:
    ...


def dgdebug(*args, **kwargs) -> Any:
    ...


def dgdirty(
    *args: List[str],
    query: bool,
    allPlugs: bool,
    clean: bool,
    implicit: bool,
    list: str,
    propagation: bool,
    showTiming: bool,
    verbose: bool,
) -> Any:
    ...


def dgeval(*args: List[Incomplete], verbose: bool) -> Any:
    ...


def dgfilter(*args, **kwargs) -> Any:
    ...


def dgmodified() -> Any:
    ...


def dgstats(*args, **kwargs) -> Any:
    ...


def dgtimer(
    query: bool,
    combineType: bool,
    hierarchy: bool,
    hide: List[str],
    maxDisplay: int,
    name: str,
    noHeader: bool,
    outputFile: str,
    timerOff: bool,
    overhead: bool,
    timerOn: bool,
    reset: bool,
    returnCode: str,
    rangeLower: float,
    rangeUpper: float,
    returnType: str,
    show: List[str],
    sortMetric: str,
    sortType: str,
    type: str,
    threshold: float,
    trace: bool,
    updateHeatMap: int,
    uniqueName: bool,
) -> Any:
    ...


def dimWhen(*args: Tuple[str, str], clear: bool, false: bool, true: bool) -> Any:
    ...


def directConnectPath() -> Any:
    ...


def directKeyCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
    option: str,
    selectedOnly: bool,
) -> Any:
    ...


def directionalLight(
    *args: List[str],
    edit: bool,
    query: bool,
    decayRate: int,
    discRadius: float,
    exclusive: bool,
    intensity: float,
    name: str,
    position: Tuple[float, float, float],
    rotation: Tuple[float, float, float],
    useRayTraceShadows: bool,
    shadowColor: Tuple[float, float, float],
    shadowDither: float,
    shadowSamples: int,
    softShadow: bool,
) -> Any:
    ...


def dirmap(
    arg0: str,
    /,
    query: bool,
    convertDirectory: str,
    enable: bool,
    getAllMappings: bool,
    getMappedDirectory: str,
    mapDirectory: Tuple[str, str],
    unmapDirectory: str,
) -> Any:
    ...


def disable(arg0: str, /, value: bool) -> Any:
    ...


def disableIncorrectNameWarning() -> Any:
    ...


def disconnectAttr(*args: Tuple[str, str], nextAvailable: bool) -> Any:
    ...


def disconnectJoint(
    arg0: Incomplete, /, attachHandleMode: bool, deleteHandleMode: bool
) -> Any:
    ...


def diskCache(
    query: bool,
    append: bool,
    close: str,
    closeAll: bool,
    cacheType: str,
    delete: str,
    deleteAll: bool,
    empty: str,
    emptyAll: bool,
    enabledCachesOnly: bool,
    endTime: int,
    frameRangeType: str,
    overSample: bool,
    samplingRate: int,
    startTime: int,
    tempDir: bool,
) -> Any:
    ...


def dispatchGenericCommand() -> Any:
    ...


def displacementToPoly(
    *args: List[str], edit: bool, query: bool, findBboxOnly: bool
) -> Any:
    ...


def displayAffected(arg0: bool, /, query: bool) -> Any:
    ...


def displayColor(
    *args: Tuple[str, int],
    query: bool,
    active: bool,
    create: bool,
    dormant: bool,
    list: bool,
    queryIndex: int,
    resetToFactory: bool,
    resetToSaved: bool,
) -> Any:
    ...


def displayCull(*args: List[str], query: bool, backFaceCulling: bool) -> Any:
    ...


def displayLevelOfDetail(query: bool, levelOfDetail: bool) -> Any:
    ...


def displayPref(
    query: bool,
    activeObjectPivots: bool,
    displayAffected: bool,
    defaultFontSize: int,
    displayGradient: bool,
    fontSettingMode: int,
    ghostFrames: Tuple[int, int, int],
    lineWidth: float,
    maxHardwareTextureResolution: bool,
    materialLoadingMode: str,
    maxTextureResolution: int,
    purgeExistingTextures: bool,
    regionOfEffect: bool,
    smallFontSize: int,
    shadeTemplates: bool,
    textureDrawPixel: bool,
    wireframeOnShadedActive: str,
) -> Any:
    ...


def displayRGBColor(
    *args: Tuple[str, float, float, float, float],
    query: bool,
    alpha: bool,
    create: bool,
    hueSaturationValue: bool,
    list: bool,
    resetToFactory: bool,
    resetToSaved: bool,
) -> Any:
    ...


def displaySmoothness(
    *args: List[str],
    query: bool,
    boundary: bool,
    defaultCreation: bool,
    divisionsU: int,
    divisionsV: int,
    full: bool,
    hull: bool,
    polygonObject: int,
    pointsShaded: int,
    pointsWire: int,
    renderTessellation: bool,
    simplifyU: int,
    simplifyV: int,
) -> Any:
    ...


def displayStats(query: bool, frameRate: bool) -> Any:
    ...


def displayString(
    *args: Tuple[str, str, str, str],
    query: bool,
    delete: bool,
    exists: bool,
    keys: bool,
    replace: bool,
    value: str,
) -> Any:
    ...


def displaySurface(
    *args: List[str], query: bool, flipNormals: bool, twoSidedLighting: bool, xRay: bool
) -> Any:
    ...


def distanceDimContext(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def distanceDimension(
    *args: List[str],
    endPoint: Tuple[float, float, float],
    startPoint: Tuple[float, float, float],
) -> Any:
    ...


def doBlur(
    colorFile: str,
    length: float,
    smooth: float,
    memCapSize: float,
    smoothColor: bool,
    sharpness: float,
    vectorFile: str,
) -> Any:
    ...


def dockControl(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    area: str,
    allowedArea: List[str],
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    closeCommand: str,
    content: str,
    dragCallback: Callable,
    dropCallback: Callable,
    dockStation: str,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    enablePopupOption: bool,
    exists: bool,
    floatChangeCommand: Callable,
    fixedHeight: bool,
    floating: bool,
    fullPathName: bool,
    fixedWidth: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    label: str,
    manage: bool,
    moveable: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    r: bool,
    retain: bool,
    sizeable: bool,
    statusBarMessage: str,
    splitLayout: str,
    state: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def dolly(
    arg0: str,
    /,
    absolute: bool,
    distance: float,
    dollyTowardsCenter: bool,
    orthoScale: float,
    relative: bool,
) -> Any:
    ...


def dollyCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    alternateContext: bool,
    boxDollyType: str,
    centerOfInterestDolly: bool,
    history: bool,
    dollyTowardsCenter: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    localDolly: bool,
    name: str,
    orthoZoom: bool,
    scale: float,
    toolName: str,
) -> Any:
    ...


def dopeSheetEditor(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    autoFit: str,
    autoFitTime: str,
    control: bool,
    displayActiveKeys: str,
    displayActiveKeyTangents: str,
    displayInfinities: str,
    displayKeys: str,
    defineTemplate: str,
    docTag: str,
    displayTangents: str,
    displayValues: str,
    exists: bool,
    filter: str,
    forceMainConnection: str,
    hierarchyBelow: bool,
    highlightConnection: str,
    lookAt: str,
    lockMainConnection: bool,
    mainListConnection: str,
    outliner: str,
    parent: str,
    panel: str,
    showScene: bool,
    selectionWindow: Tuple[float, float, float, float],
    selectionConnection: str,
    showSummary: bool,
    snapTime: str,
    showTicks: bool,
    stateString: bool,
    snapValue: str,
    unlockMainConnection: bool,
    unParent: bool,
    updateMainConnection: bool,
    useTemplate: str,
) -> Any:
    ...


def doubleProfileBirailSurface(
    *args: List[Incomplete],
    edit: bool,
    query: bool,
    blendFactor: float,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    polygon: int,
    transformMode: int,
    tangentContinuityProfile1: bool,
    tangentContinuityProfile2: bool,
) -> Any:
    ...


def dpBirailCtx(*args, **kwargs) -> Any:
    ...


def drag(
    *args: List[str],
    edit: bool,
    query: bool,
    attenuation: float,
    directionX: float,
    directionY: float,
    directionZ: float,
    magnitude: float,
    maxDistance: float,
    name: str,
    position: List[Tuple[float, float, float]],
    perVertex: bool,
    torusSectionRadius: float,
    useDirection: bool,
    volumeExclusion: bool,
    volumeOffset: Tuple[float, float, float],
    volumeShape: str,
    volumeSweep: float,
) -> Any:
    ...


def dragAttrContext(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    connectTo: List[str],
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
    reset: bool,
) -> Any:
    ...


def draggerContext(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    anchorPoint: Tuple[float, float, float],
    button: int,
    history: bool,
    currentStep: int,
    cursor: str,
    dragCommand: Callable,
    dragPoint: Tuple[float, float, float],
    drawString: str,
    exists: bool,
    finalize: Callable,
    holdCommand: Callable,
    helpString: str,
    image1: str,
    image2: str,
    image3: str,
    initialize: Callable,
    modifier: str,
    name: str,
    pressCommand: Callable,
    plane: Tuple[float, float, float],
    prePressCommand: Callable,
    projection: str,
    releaseCommand: Callable,
    stepsCount: int,
    snapping: bool,
    space: str,
    undoMode: str,
) -> Any:
    ...


def drawExtrudeFacetCtx(*args, **kwargs) -> Any:
    ...


def dropoffLocator() -> Any:
    ...


def duplicate(
    *args: List[str],
    fullPath: bool,
    inputConnections: bool,
    instanceLeaf: bool,
    name: str,
    parentOnly: bool,
    renameChildren: bool,
    returnRootsOnly: bool,
    smartTransform: bool,
    transformsOnly: bool,
    upstreamNodes: bool,
) -> Any:
    ...


def duplicateCurve(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    local: bool,
    maxValue: float,
    mergeItems: bool,
    minValue: float,
    name: str,
    nodeState: int,
    object: bool,
    relative: bool,
    range: bool,
) -> Any:
    ...


def duplicateSurface(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    faceCountU: int,
    faceCountV: int,
    firstFaceU: int,
    firstFaceV: int,
    frozen: bool,
    local: bool,
    mergeItems: bool,
    name: str,
    nodeState: int,
    object: bool,
) -> Any:
    ...


def dynCache() -> Any:
    ...


def dynControl(
    autoCreate: bool,
    oversample: int,
    particleCache: bool,
    particleLOD: float,
    particlesOn: bool,
    rigidOn: bool,
    seed: int,
    startTime: int,
    traceDepth: int,
) -> Any:
    ...


def dynExport(
    *args: List[str],
    allObjects: bool,
    attribute: List[str],
    format: str,
    minFrame: int,
    maxFrame: int,
    overSampling: int,
    onlyUpdateParticles: bool,
    path: str,
) -> Any:
    ...


def dynExpression(
    *args: List[str],
    edit: bool,
    query: bool,
    creation: bool,
    runtime: bool,
    runtimeAfterDynamics: bool,
    runtimeBeforeDynamics: bool,
    string: str,
) -> Any:
    ...


def dynGlobals(
    *args: List[str],
    edit: bool,
    query: bool,
    active: bool,
    listAll: bool,
    overSampling: int,
) -> Any:
    ...


def dynPaintCtx(*args, **kwargs) -> Any:
    ...


def dynPaintEditor(*args, **kwargs) -> Any:
    ...


def dynParticleCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    conserve: float,
    history: bool,
    cursorPlacement: bool,
    exists: bool,
    grid: bool,
    gridSpacing: float,
    image1: str,
    image2: str,
    image3: str,
    jitterRadius: float,
    lowerLeftX: float,
    lowerLeftY: float,
    lowerLeftZ: float,
    name: str,
    nucleus: bool,
    numJitters: int,
    particleName: str,
    sketch: bool,
    sketchInterval: int,
    textPlacement: bool,
    upperRightX: float,
    upperRightY: float,
    upperZ: float,
) -> Any:
    ...


def dynPref(
    query: bool,
    autoCreate: bool,
    echoCollision: bool,
    runupFrom: int,
    runupToCurrentTime: bool,
    saveOnQuit: bool,
    saveRuntimeState: bool,
) -> Any:
    ...


def dynSelectCtx(*args, **kwargs) -> Any:
    ...


def dynTestData(arrayAttrs: bool, verbose: bool) -> Any:
    ...


def dynWireCtx(*args, **kwargs) -> Any:
    ...


def dynamicConstraintRemove() -> Any:
    ...


def dynamicLoad(*args: List[str], query: bool) -> Any:
    ...


def editDisplayLayerGlobals(
    query: bool, baseId: int, currentDisplayLayer: str, mergeType: int, useCurrent: bool
) -> Any:
    ...


def editDisplayLayerMembers(
    *args: List[str], query: bool, fullNames: bool, noRecurse: bool
) -> Any:
    ...


def editImportedStatus() -> Any:
    ...


def editMetadata(
    *args: List[str],
    channelType: str,
    channelName: str,
    endIndex: str,
    indexType: str,
    index: List[str],
    memberName: str,
    remove: bool,
    scene: bool,
    startIndex: str,
    streamName: str,
    stringValue: List[str],
    value: List[float],
) -> Any:
    ...


def editRenderLayerAdjustment(
    *args: List[str],
    query: bool,
    attributeLog: bool,
    layer: str,
    nodeLog: bool,
    remove: bool,
) -> Any:
    ...


def editRenderLayerGlobals(
    query: bool,
    baseId: int,
    currentRenderLayer: str,
    enableAutoAdjustments: bool,
    mergeType: int,
    useCurrent: bool,
) -> Any:
    ...


def editRenderLayerMembers(
    *args: List[Incomplete], query: bool, fullNames: bool, noRecurse: bool, remove: bool
) -> Any:
    ...


def editor(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    control: bool,
    defineTemplate: str,
    docTag: str,
    exists: bool,
    filter: str,
    forceMainConnection: str,
    highlightConnection: str,
    lockMainConnection: bool,
    mainListConnection: str,
    parent: str,
    panel: str,
    selectionConnection: str,
    stateString: bool,
    unlockMainConnection: bool,
    unParent: bool,
    updateMainConnection: bool,
    useTemplate: str,
) -> Any:
    ...


def editorTemplate(
    *args: List[str],
    addAdskAssetControls: bool,
    addControl: Tuple[Incomplete, str, Callable, Incomplete],
    addComponents: bool,
    addDynamicControl: Tuple[Incomplete, str, Callable, Incomplete],
    addExtraControls: bool,
    annotateFieldOnly: bool,
    annotation: str,
    addSeparator: bool,
    beginLayout: str,
    beginNoOptimize: bool,
    beginScrollLayout: bool,
    callCustom: Tuple[Callable, Callable],
    collapse: bool,
    debugMode: bool,
    dimControl: Tuple[str, str, bool],
    extraControlsLabel: str,
    endLayout: bool,
    endNoOptimize: bool,
    endScrollLayout: bool,
    forceRebuild: bool,
    interruptOptimize: bool,
    label: str,
    listExtraAttributes: str,
    preventOverride: bool,
    queryControl: Tuple[str, str],
    queryLabel: Tuple[str, str],
    queryName: Tuple[str, str],
    suppress: str,
) -> Any:
    ...


def effector(
    arg0: Incomplete, /, edit: bool, query: bool, hide: bool, name: str
) -> Any:
    ...


def emit(
    attribute: List[str],
    floatValue: List[float],
    object: str,
    position: List[Tuple[float, float, float]],
    vectorValue: List[Tuple[float, float, float]],
) -> Any:
    ...


def emitter(
    *args: List[str],
    edit: bool,
    query: bool,
    awayFromCenter: float,
    awayFromAxis: float,
    alongAxis: float,
    aroundAxis: float,
    cycleEmission: str,
    cycleInterval: int,
    directionalSpeed: float,
    directionX: float,
    directionY: float,
    directionZ: float,
    minDistance: float,
    maxDistance: float,
    name: str,
    normalSpeed: float,
    needParentUV: bool,
    position: List[Tuple[float, float, float]],
    rate: float,
    randomDirection: float,
    spread: float,
    speed: float,
    speedRandom: float,
    scaleRateByObjectSize: bool,
    scaleSpeedBySize: bool,
    tangentSpeed: float,
    torusSectionRadius: float,
    type: str,
    volumeOffset: Tuple[float, float, float],
    volumeShape: str,
    volumeSweep: float,
) -> Any:
    ...


def enableDevice(*args, **kwargs) -> Any:
    ...


def encodeString() -> Any:
    ...


def error(*args: List[str], noContext: bool, showLineNumber: bool) -> Any:
    ...


def eval(arg0: str, /, undoEnabled: bool) -> Any:
    ...


def evalContinue() -> Any:
    ...


def evalDeferred(
    arg0: Callable,
    /,
    evaluateNext: bool,
    lowPriority: bool,
    lowestPriority: bool,
    list: bool,
) -> Any:
    ...


def evalEcho() -> Any:
    ...


def evalNoSelectNotify() -> Any:
    ...


def evaluationManager(
    *args: List[str],
    query: bool,
    cycleCluster: str,
    disableInfo: str,
    downstreamFrom: str,
    enabled: bool,
    fallbackTriggered: bool,
    idleAction: int,
    idleBuild: bool,
    invalidate: bool,
    mode: str,
    manipulation: bool,
    manipulationPrevalidation: bool,
    manipulationReady: bool,
    empty: bool,
    nodeTypeGloballySerialize: bool,
    nodeTypeParallel: bool,
    nodeTypeSerialize: bool,
    nodeTypeUntrusted: bool,
    reduceGraphRebuild: bool,
    safeMode: bool,
    upstreamFrom: str,
) -> Any:
    ...


def evaluationManagerInternal(
    *args: List[str], query: bool, dataSharing: bool, dataTypeShare: bool
) -> Any:
    ...


def evaluator(
    *args: List[str],
    query: bool,
    configuration: List[str],
    clusters: bool,
    enable: bool,
    info: bool,
    name: str,
    nodeType: List[str],
    nodeTypeChildren: bool,
    priority: int,
    valueName: str,
) -> Any:
    ...


def evaluatorInternal(*args: List[str], query: bool, name: str, ready: bool) -> Any:
    ...


def event(
    *args: List[str],
    edit: bool,
    query: bool,
    count: int,
    delete: bool,
    dieAtCollision: bool,
    emit: int,
    idNumber: int,
    list: bool,
    name: str,
    proc: Callable,
    random: bool,
    rename: str,
    select: bool,
    spread: float,
    split: int,
    target: str,
) -> Any:
    ...


def exactWorldBoundingBox(
    *args: List[str], calculateExactly: bool, ignoreInvisible: bool
) -> Any:
    ...


def exclusiveLightCheckBox(*args, **kwargs) -> Any:
    ...


def expandedSelection(*args: List[str], depth: int, expansionType: str) -> Any:
    ...


def exportEdits(
    *args: List[str],
    query: bool,
    editCommand: List[str],
    excludeHierarchy: bool,
    excludeNode: List[str],
    exportSelected: bool,
    force: bool,
    includeAnimation: bool,
    includeConstraints: bool,
    includeDeformers: bool,
    includeNode: List[str],
    includeNetwork: bool,
    includeSetAttrs: bool,
    includeShaders: bool,
    onReferenceNode: List[str],
    includeSetDrivenKeys: bool,
    selected: bool,
    type: str,
) -> Any:
    ...


def expression(
    *args: List[str],
    edit: bool,
    query: bool,
    attribute: str,
    alwaysEvaluate: int,
    animated: int,
    name: str,
    object: str,
    string: str,
    safe: bool,
    shortNames: bool,
    timeDependent: bool,
    unitConversion: str,
) -> Any:
    ...


def expressionEditorListen(
    listenForAttr: str,
    listenForExpression: str,
    listenFile: str,
    listenForName: str,
    stopListenForAttr: str,
    stopListenForExpression: str,
    stopListenForName: str,
) -> Any:
    ...


def extendCurve(
    *args: Tuple[str, str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    curveOnSurface: bool,
    distance: float,
    extendMethod: int,
    extensionType: int,
    frozen: bool,
    inputPoint: Tuple[float, float, float],
    join: bool,
    name: str,
    noChanges: bool,
    nodeState: int,
    object: bool,
    pointX: float,
    pointY: float,
    pointZ: float,
    removeMultipleKnots: bool,
    range: bool,
    replaceOriginal: bool,
    start: int,
) -> Any:
    ...


def extendFluid(
    *args: List[str],
    edit: bool,
    query: bool,
    endD: int,
    endH: int,
    endW: int,
    startD: int,
    startH: int,
    startW: int,
) -> Any:
    ...


def extendSurface(
    *args: Tuple[str, str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    distance: float,
    extendDirection: int,
    extendMethod: int,
    extendSide: int,
    extensionType: int,
    frozen: bool,
    join: bool,
    name: str,
    noChanges: bool,
    nodeState: int,
    object: bool,
    replaceOriginal: bool,
) -> Any:
    ...


def extrude(
    *args: Tuple[str, str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    direction: Tuple[float, float, float],
    degreeAlongLength: int,
    directionX: float,
    directionY: float,
    directionZ: float,
    extrudeType: int,
    fixedPath: bool,
    frozen: bool,
    length: float,
    mergeItems: bool,
    name: str,
    nodeState: int,
    object: bool,
    pivot: Tuple[float, float, float],
    polygon: int,
    rebuild: bool,
    range: bool,
    rotation: float,
    reverseSurfaceIfPathReversed: bool,
    scale: float,
    subCurveSubSurface: bool,
    useComponentPivot: int,
    useProfileNormal: bool,
) -> Any:
    ...


def falloffCurve(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    addControlVertex: str,
    annotation: str,
    asString: str,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    customCurveWidget: int,
    currentKey: int,
    currentKeyValue: Tuple[float, float],
    deleteControlVertex: int,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    optionVar: str,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    readOnly: int,
    statusBarMessage: str,
    snapToGrid: int,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def falloffCurveAttr(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    addControlVertex: str,
    annotation: str,
    asString: str,
    attribute: str,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    customCurveWidget: int,
    currentKey: int,
    currentKeyValue: Tuple[float, float],
    deleteControlVertex: int,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    readOnly: int,
    statusBarMessage: str,
    selectedPositionControl: str,
    snapToGrid: int,
    selectedValueControl: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def fcheck() -> Any:
    ...


def file(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    activate: bool,
    anyModified: bool,
    absoluteName: bool,
    activeProxy: bool,
    applyTo: str,
    buildLoadSettings: bool,
    command: Tuple[str, str],
    constructionHistory: bool,
    channels: bool,
    compress: bool,
    copyNumberList: bool,
    constraints: bool,
    cleanReference: str,
    defaultExtensions: bool,
    defaultNamespace: bool,
    deferReference: bool,
    exportAll: bool,
    exportAnim: bool,
    exportAnimFromReference: bool,
    exportSelectedAnim: bool,
    editCommand: str,
    exportAsReference: bool,
    errorStatus: bool,
    exportSelected: bool,
    exportSelectedAnimFromReference: bool,
    exportSnapshotCallback: Tuple[Callable, str],
    executeScriptNodes: bool,
    exportSelectedNoReference: bool,
    exportSelectedStrict: bool,
    exportUnloadedReferences: bool,
    exists: bool,
    expandName: bool,
    expressions: bool,
    exportAsSegment: bool,
    force: bool,
    fileMetaData: bool,
    flushReference: str,
    groupLocator: bool,
    groupName: str,
    groupReference: bool,
    i: bool,
    importFrameRate: bool,
    importReference: bool,
    importTimeRange: str,
    ignoreVersion: bool,
    list: bool,
    loadAllDeferred: bool,
    loadAllReferences: bool,
    lockReference: bool,
    lockContainerUnpublished: bool,
    lockFile: bool,
    lastFileOption: bool,
    loadNoReferences: bool,
    location: bool,
    loadReference: str,
    loadReferenceDepth: str,
    loadReferencePreview: str,
    loadSettings: str,
    lastTempFile: bool,
    mergeBaseAnimLayer: bool,
    modified: bool,
    mergeNamespacesOnClash: bool,
    mergeNamespaceWithParent: bool,
    mergeNamespaceWithRoot: bool,
    mapPlaceHolderNamespace: List[Tuple[str, str]],
    moveSelected: bool,
    newFile: bool,
    namespace: str,
    open: bool,
    options: str,
    proxyManager: str,
    prompt: bool,
    preserveName: bool,
    parentNamespace: bool,
    postSaveScript: str,
    preserveReferences: bool,
    preSaveScript: str,
    proxyTag: str,
    preserveUndo: bool,
    preview: bool,
    reference: bool,
    renameAll: bool,
    referenceDepthInfo: int,
    removeDuplicateNetworks: bool,
    replaceName: List[Tuple[str, str]],
    resetError: bool,
    referenceNode: str,
    rename: str,
    returnNewNodes: bool,
    relativeNamespace: str,
    renamingPrefixList: bool,
    renamingPrefix: str,
    removeReference: bool,
    renameToSave: bool,
    reserveNamespaces: bool,
    save: bool,
    selectAll: bool,
    saveDiskCache: str,
    segment: str,
    shader: bool,
    sharedNodes: List[str],
    shortName: bool,
    sceneName: bool,
    swapNamespace: List[Tuple[str, str]],
    saveReference: bool,
    sharedReferenceFile: bool,
    saveReferencesUnloaded: bool,
    strict: bool,
    saveTextures: str,
    type: str,
    uiConfiguration: bool,
    uiLoadConfiguration: bool,
    unresolvedName: bool,
    usingNamespaces: bool,
    unloadReference: str,
    writable: bool,
    withoutCopyNumber: bool,
) -> Any:
    ...


def fileBrowserDialog(
    actionName: str,
    dialogStyle: int,
    fileCommand: Callable,
    filterList: List[str],
    fileType: str,
    includeName: str,
    mode: int,
    operationMode: str,
    tipMessage: str,
    windowTitle: str,
) -> Any:
    ...


def fileDialog(
    application: bool, defaultFileName: str, directoryMask: str, mode: int, title: str
) -> Any:
    ...


def fileDialog2(
    buttonBoxOrientation: int,
    caption: str,
    cancelCaption: str,
    startingDirectory: str,
    dialogStyle: int,
    fileFilter: str,
    fileMode: int,
    fileTypeChanged: Callable,
    hideFileExtensions: bool,
    hideNameEdit: bool,
    optionsUICommit2: Callable,
    optionsUICancel: Callable,
    optionsUICommit: Callable,
    optionsUICreate: Callable,
    optionsUIInit: Callable,
    okCaption: str,
    optionsUITitle: str,
    returnFilter: bool,
    selectionChanged: Callable,
    selectFileFilter: str,
    setProjectBtnEnabled: bool,
) -> Any:
    ...


def fileInfo(
    *args: Tuple[str, str], query: bool, referenceNode: str, remove: str
) -> Any:
    ...


def filePathEditor(
    *args: List[str],
    query: bool,
    attributeOnly: bool,
    attributeType: str,
    byType: str,
    copyAndRepath: Tuple[str, str],
    deregisterType: str,
    force: bool,
    listDirectories: str,
    listFiles: str,
    listRegisteredTypes: bool,
    preview: bool,
    repath: str,
    replaceAll: bool,
    recursive: bool,
    relativeNames: bool,
    refresh: bool,
    replaceField: str,
    replaceString: Tuple[str, str],
    registerType: str,
    status: bool,
    typeLabel: str,
    temporary: bool,
    unresolved: bool,
    withAttribute: bool,
) -> Any:
    ...


def filletCurve(
    *args: Tuple[str, str],
    edit: bool,
    query: bool,
    bias: float,
    blendControl: bool,
    caching: bool,
    constructionHistory: bool,
    circular: bool,
    curveParameter1: float,
    curveParameter2: float,
    depth: float,
    freeformBlend: bool,
    frozen: bool,
    join: bool,
    name: str,
    nodeState: int,
    object: bool,
    radius: float,
    replaceOriginal: bool,
    trim: bool,
) -> Any:
    ...


def filter(*args, **kwargs) -> Any:
    ...


def filterButterworthCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    apply: bool,
    history: bool,
    cutoffFrequency: float,
    endTime: int,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    keepKeysOnFrame: bool,
    name: str,
    preserveKeyTangent: List[str],
    startTime: int,
    selectedKeys: bool,
    samplingRate: float,
) -> Any:
    ...


def filterCurve(
    *args: List[str],
    cutoffFrequency: float,
    endTime: int,
    filter: str,
    kernel: str,
    keepKeysOnFrame: bool,
    keySync: bool,
    minTimeStep: float,
    maxTimeStep: float,
    period: float,
    preserveKeyTangent: List[str],
    precisionMode: int,
    precision: float,
    startTime: int,
    sampleCount: int,
    selectedKeys: bool,
    samplingRate: float,
    tolerance: float,
    timeTolerance: float,
    useQuaternion: bool,
    width: int,
) -> Any:
    ...


def filterExpand(
    *args: List[str],
    expand: bool,
    fullPath: bool,
    selectionMask: List[int],
    symActive: bool,
    symNegative: bool,
    symPositive: bool,
    symSeam: bool,
) -> Any:
    ...


def filterGaussianCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    apply: bool,
    history: bool,
    endTime: int,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
    startTime: int,
    sampleCount: int,
    selectedKeys: bool,
    useQuaternion: bool,
    width: int,
) -> Any:
    ...


def filterInstances(*args: List[str], query: bool, shapes: bool) -> Any:
    ...


def filterKeyReducerCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    apply: bool,
    history: bool,
    endTime: int,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    keySync: bool,
    name: str,
    preserveKeyTangent: List[str],
    precisionMode: int,
    precision: float,
    startTime: int,
    selectedKeys: bool,
) -> Any:
    ...


def filterPeakRemoverCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    apply: bool,
    history: bool,
    endTime: int,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
    startTime: int,
    selectedKeys: bool,
) -> Any:
    ...


def findDeformers() -> Any:
    ...


def findKeyframe(
    *args: List[str],
    animation: str,
    attribute: List[str],
    curve: bool,
    controlPoints: bool,
    float: List[Incomplete],
    hierarchy: str,
    index: List[Incomplete],
    includeUpperBound: bool,
    shape: bool,
    time: List[Incomplete],
    timeSlider: bool,
    which: str,
) -> Any:
    ...


def findType(
    *args: List[str], deep: bool, exact: bool, forward: bool, type: str
) -> Any:
    ...


def fitBspline(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    keepRange: int,
    name: str,
    nodeState: int,
    object: bool,
    tolerance: float,
) -> Any:
    ...


def flagTest(
    *args: Tuple[
        str, float, int, str, str, Incomplete, Incomplete, Incomplete, Incomplete
    ],
    edit: bool,
    query: bool,
    floatRange: List[Incomplete],
    indexRange: List[Incomplete],
    multiUse: List[Tuple[float, int, str]],
    noReport: bool,
    optionalQueryArgsFlag: Tuple[float, int, str],
    pythonOptionalQueryArgsFlag: Tuple[float, int, str],
    pythonQueryArgsFlag: Tuple[float, int, str],
    queryArgsFlag: Tuple[float, int, str],
    simpleFlag: bool,
    stringArrayFlag: Incomplete,
    stringFlag: str,
    tripleFloat: Tuple[float, float, float],
    timeRange: List[Incomplete],
) -> Any:
    ...


def flexor(
    *args: List[str],
    edit: bool,
    query: bool,
    atBones: bool,
    atJoints: bool,
    deformerCommand: str,
    list: bool,
    name: str,
    noScale: bool,
    toSkeleton: bool,
    type: str,
) -> Any:
    ...


def floatField(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    dragCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enterCommand: Callable,
    editable: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    maxValue: float,
    minValue: float,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    precision: int,
    receiveFocusCommand: Callable,
    step: float,
    statusBarMessage: str,
    showTrailingZeros: bool,
    useTemplate: str,
    value: float,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def floatFieldGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    changeCommand: Callable,
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    dragCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    extraLabel: str,
    enable: bool,
    enable1: bool,
    enable2: bool,
    enable3: bool,
    enable4: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    label: str,
    manage: bool,
    noBackground: bool,
    numberOfFields: int,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    precision: int,
    rowAttach: List[Tuple[int, str, int]],
    step: float,
    statusBarMessage: str,
    showTrailingZeros: bool,
    useTemplate: str,
    value: Tuple[float, float, float, float],
    value1: float,
    value2: float,
    value3: float,
    value4: float,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def floatScrollBar(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    dragCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    horizontal: bool,
    isObscured: bool,
    largeStep: float,
    manage: bool,
    maxValue: float,
    minValue: float,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    step: float,
    statusBarMessage: str,
    useTemplate: str,
    value: float,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def floatSlider(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    dragCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    horizontal: bool,
    isObscured: bool,
    manage: bool,
    maxValue: float,
    minValue: float,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    step: float,
    statusBarMessage: str,
    useTemplate: str,
    value: float,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def floatSlider2(*args, **kwargs) -> Any:
    ...


def floatSliderButtonGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    annotation: str,
    buttonCommand: Callable,
    backgroundColor: Tuple[float, float, float],
    buttonLabel: str,
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    changeCommand: Callable,
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    dragCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    extraLabel: str,
    enable: bool,
    exists: bool,
    field: bool,
    fieldMinValue: float,
    fieldMaxValue: float,
    fullPathName: bool,
    fieldStep: float,
    height: int,
    highlightColor: Tuple[float, float, float],
    image: str,
    isObscured: bool,
    label: str,
    manage: bool,
    maxValue: float,
    minValue: float,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    precision: int,
    rowAttach: List[Tuple[int, str, int]],
    step: float,
    symbolButtonCommand: Callable,
    symbolButtonDisplay: bool,
    statusBarMessage: str,
    sliderStep: float,
    useTemplate: str,
    value: float,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def floatSliderGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    changeCommand: Callable,
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    dragCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    extraLabel: str,
    enable: bool,
    exists: bool,
    field: bool,
    fieldMinValue: float,
    fieldMaxValue: float,
    fullPathName: bool,
    fieldStep: float,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    label: str,
    manage: bool,
    maxValue: float,
    minValue: float,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    precision: int,
    rowAttach: List[Tuple[int, str, int]],
    step: float,
    statusBarMessage: str,
    sliderStep: float,
    useTemplate: str,
    value: float,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def flow(
    *args: List[str],
    edit: bool,
    query: bool,
    divisions: Tuple[int, int, int],
    localCompute: bool,
    localDivisions: Tuple[int, int, int],
    objectCentered: bool,
) -> Any:
    ...


def flowLayout(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    childArray: bool,
    columnSpacing: int,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    horizontal: bool,
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfChildren: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    useTemplate: str,
    vertical: bool,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
    wrap: bool,
) -> Any:
    ...


def fluidAppend() -> Any:
    ...


def fluidAppendOpt() -> Any:
    ...


def fluidCacheInfo(
    *args: List[str],
    edit: bool,
    query: bool,
    attribute: str,
    endFrame: bool,
    hasCache: bool,
    hasData: bool,
    initialConditions: bool,
    playback: bool,
    resolution: bool,
    startFrame: bool,
    cacheTime: int,
) -> Any:
    ...


def fluidDeleteCache() -> Any:
    ...


def fluidDeleteCacheFrames() -> Any:
    ...


def fluidDeleteCacheFramesOpt() -> Any:
    ...


def fluidDeleteCacheOpt() -> Any:
    ...


def fluidEmitter(
    *args: List[str],
    edit: bool,
    query: bool,
    cycleEmission: str,
    cycleInterval: int,
    densityEmissionRate: float,
    fluidDropoff: float,
    fuelEmissionRate: float,
    heatEmissionRate: float,
    minDistance: float,
    maxDistance: float,
    name: str,
    position: List[Tuple[float, float, float]],
    rate: float,
    torusSectionRadius: float,
    type: str,
    volumeOffset: Tuple[float, float, float],
    volumeShape: str,
    volumeSweep: float,
) -> Any:
    ...


def fluidMergeCache() -> Any:
    ...


def fluidMergeCacheOpt() -> Any:
    ...


def fluidReplaceCache() -> Any:
    ...


def fluidReplaceCacheOpt() -> Any:
    ...


def fluidReplaceFrames() -> Any:
    ...


def fluidReplaceFramesOpt() -> Any:
    ...


def fluidVoxelInfo(
    *args: List[str],
    checkBounds: bool,
    inBounds: Tuple[int, int, int],
    objectSpace: bool,
    radius: float,
    voxel: Tuple[float, float, float],
    voxelCenter: bool,
    xIndex: int,
    yIndex: int,
    zIndex: int,
) -> Any:
    ...


def flushIdleQueue(resume: bool) -> Any:
    ...


def flushThumbnailCache(*args, **kwargs) -> Any:
    ...


def flushUndo() -> Any:
    ...


def fontDialog(FontList: bool, scalable: bool) -> Any:
    ...


def formLayout(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    attachControl: List[Tuple[str, str, int, str]],
    attachForm: List[Tuple[str, str, int]],
    attachNone: List[Tuple[str, str]],
    annotation: str,
    attachOppositeControl: List[Tuple[str, str, int, str]],
    attachOppositeForm: List[Tuple[str, str, int]],
    attachPosition: List[Tuple[str, str, int, int]],
    backgroundColor: Tuple[float, float, float],
    childArray: bool,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfChildren: bool,
    numberOfDivisions: int,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def format(arg0: str, /, stringArg: List[str]) -> Any:
    ...


def frameBufferName(
    autoTruncate: bool, camera: str, renderLayer: str, renderPass: str
) -> Any:
    ...


def frameLayout(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    backgroundShade: bool,
    borderStyle: str,
    borderVisible: bool,
    childArray: bool,
    collapseCommand: Callable,
    collapse: bool,
    collapsable: bool,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    expandCommand: Callable,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    font: str,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    label: str,
    labelAlign: str,
    labelIndent: int,
    labelVisible: bool,
    labelWidth: int,
    manage: bool,
    marginHeight: int,
    marginWidth: int,
    noBackground: bool,
    numberOfChildren: bool,
    numberOfPopupMenus: bool,
    parent: str,
    preCollapseCommand: Callable,
    preExpandCommand: Callable,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def framelessDialog(
    button: List[str],
    message: str,
    messageAlign: str,
    parent: str,
    path: str,
    primary: List[str],
    title: str,
) -> Any:
    ...


def freeFormFillet(
    *args: Tuple[str, str],
    edit: bool,
    query: bool,
    bias: float,
    caching: bool,
    constructionHistory: bool,
    depth: float,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    polygon: int,
    positionTolerance: float,
    range: bool,
    tangentTolerance: float,
) -> Any:
    ...


def freezeOptions(
    query: bool,
    displayLayers: bool,
    downstream: str,
    explicitPropagation: bool,
    invisible: bool,
    referencedNodes: bool,
    runtimePropagation: bool,
    upstream: str,
) -> Any:
    ...


def geomBind(
    *args: List[str],
    edit: bool,
    query: bool,
    bindMethod: int,
    falloff: float,
    geodesicVoxelParams: Tuple[int, bool],
    maxInfluences: int,
) -> Any:
    ...


def geomToBBox(
    *args: List[str],
    bakeAnimation: bool,
    combineMesh: bool,
    endTime: int,
    keepOriginal: bool,
    name: str,
    nameSuffix: str,
    single: bool,
    sampleBy: int,
    shaderColor: Tuple[float, float, float],
    startTime: int,
) -> Any:
    ...


def geometryAppendCache() -> Any:
    ...


def geometryAppendCacheOpt() -> Any:
    ...


def geometryAttrInfo(
    *args: List[Incomplete],
    boundingBox: bool,
    componentTagCategory: bool,
    componentTagExpression: str,
    componentTagHistoryHash: bool,
    components: bool,
    componentTagNames: bool,
    castToEdges: bool,
    castToFaces: bool,
    componentTagHistory: bool,
    castToVerts: bool,
    deformerChain: bool,
    elementCount: bool,
    groupId: int,
    componentTagHash: bool,
    matrix: bool,
    nodeChain: bool,
    outputPlugChain: bool,
    originalGeometry: bool,
    pointCount: bool,
    plugChain: bool,
    pointIndices: bool,
    points: bool,
    subsetState: bool,
) -> Any:
    ...


def geometryCache() -> Any:
    ...


def geometryCacheOpt() -> Any:
    ...


def geometryConstraint(
    *args: List[str],
    edit: bool,
    query: bool,
    name: str,
    remove: bool,
    targetList: bool,
    weight: float,
    weightAliasList: bool,
) -> Any:
    ...


def geometryDeleteCacheFrames() -> Any:
    ...


def geometryDeleteCacheFramesOpt() -> Any:
    ...


def geometryDeleteCacheOpt() -> Any:
    ...


def geometryExportCache() -> Any:
    ...


def geometryExportCacheOpt() -> Any:
    ...


def geometryMergeCache() -> Any:
    ...


def geometryMergeCacheOpt() -> Any:
    ...


def geometryReplaceCache() -> Any:
    ...


def geometryReplaceCacheFrames() -> Any:
    ...


def geometryReplaceCacheFramesOpt() -> Any:
    ...


def geometryReplaceCacheOpt() -> Any:
    ...


def getAttr(
    *args: List[Incomplete],
    asString: bool,
    caching: bool,
    channelBox: bool,
    keyable: bool,
    lock: bool,
    multiIndices: bool,
    size: bool,
    settable: bool,
    silent: bool,
    time: int,
    type: bool,
    expandEnvironmentVariables: bool,
) -> Any:
    ...


def getClassification(arg0: str, /, satisfies: str) -> Any:
    ...


def getDefaultBrush() -> Any:
    ...


def getFileList(folder: str, filespec: str) -> Any:
    ...


def getFluidAttr(
    *args: List[str],
    attribute: str,
    lowerFace: bool,
    xvalue: bool,
    xIndex: int,
    yvalue: bool,
    yIndex: int,
    zvalue: bool,
    zIndex: int,
) -> Any:
    ...


def getInputDeviceRange(*args, **kwargs) -> Any:
    ...


def getLastError() -> Any:
    ...


def getMetadata(
    *args: List[str],
    channelType: str,
    channelName: str,
    dataType: bool,
    endIndex: str,
    indexType: str,
    index: List[str],
    listChannelNames: bool,
    listMemberNames: bool,
    listStreamNames: bool,
    memberName: str,
    scene: bool,
    startIndex: str,
    streamName: str,
) -> Any:
    ...


def getModifiers() -> Any:
    ...


def getModulePath(moduleName: str) -> Any:
    ...


def getPanel(
    allConfigs: bool,
    allPanels: bool,
    atPosition: Tuple[int, int],
    allScriptedTypes: bool,
    allTypes: bool,
    containing: str,
    configWithLabel: str,
    invisiblePanels: bool,
    scriptType: str,
    typeOf: str,
    type: str,
    underPointer: bool,
    visiblePanels: bool,
    withFocus: bool,
    withLabel: str,
) -> Any:
    ...


def getParticleAttr(*args: List[str], array: bool, attribute: str, object: str) -> Any:
    ...


def getProcArguments() -> Any:
    ...


def getRenderDependencies() -> Any:
    ...


def getRenderTasks(arg0: str, /, camera: str, renderLayer: str) -> Any:
    ...


def ghosting(
    *args: List[str],
    edit: bool,
    query: bool,
    allInRange: bool,
    action: str,
    allGhostedObjects: bool,
    customFrames: List[int],
    enable: bool,
    frames: bool,
    farOpacity: float,
    geometryFilter: bool,
    ghostedObjects: bool,
    ghostsStep: int,
    hierarchy: bool,
    jointFilter: bool,
    locatorFilter: bool,
    mode: str,
    nearOpacity: float,
    preset: str,
    postColor: Tuple[float, float, float],
    postFrames: int,
    preColor: Tuple[float, float, float],
    preFrames: int,
    resetAll: bool,
    useDriver: bool,
) -> Any:
    ...


def glRender(
    edit: bool,
    query: bool,
    antiAliasMethod: str,
    accumBufferPasses: int,
    alphaSource: str,
    clearClr: Tuple[float, float, float],
    crossingEffect: bool,
    currentFrame: bool,
    cameraIcons: bool,
    collisionIcons: bool,
    drawStyle: str,
    emitterIcons: bool,
    edgeSmoothness: float,
    flipbookCallback: str,
    frameEnd: int,
    frameIncrement: int,
    fieldIcons: bool,
    fullResolution: bool,
    frameStart: int,
    grid: bool,
    imageDirectory: str,
    imageName: str,
    imageSize: Tuple[int, int, float],
    lightIcons: bool,
    lightingMode: str,
    lineSmoothing: bool,
    offScreen: bool,
    renderFrame: str,
    renderSequence: str,
    shutterAngle: float,
    sharpness: float,
    transformIcons: bool,
    textureDisplay: bool,
    useAccumBuffer: bool,
    viewport: Tuple[int, int, float],
    writeDepthMap: bool,
) -> Any:
    ...


def glRenderEditor(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    control: bool,
    defineTemplate: str,
    docTag: str,
    exists: bool,
    filter: str,
    forceMainConnection: str,
    highlightConnection: str,
    lockMainConnection: bool,
    lookThru: str,
    mainListConnection: str,
    parent: str,
    panel: str,
    selectionConnection: str,
    stateString: bool,
    unlockMainConnection: bool,
    unParent: bool,
    updateMainConnection: bool,
    useTemplate: str,
    viewCameraName: bool,
) -> Any:
    ...


def globalStitch(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    lockSurface: List[bool],
    modificationResistance: float,
    maxSeparation: float,
    name: str,
    nodeState: int,
    object: bool,
    replaceOriginal: bool,
    sampling: int,
    stitchCorners: int,
    stitchEdges: int,
    stitchPartialEdges: bool,
    stitchSmoothness: int,
) -> Any:
    ...


def goal(
    *args: List[str],
    query: bool,
    goal: List[str],
    index: bool,
    useTransformAsGoal: bool,
    weight: float,
) -> Any:
    ...


def grabColor(alpha: bool, hsvValue: bool, rgbValue: bool) -> Any:
    ...


def gradientControl(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    adaptiveScaling: bool,
    attribute: str,
    backgroundColor: Tuple[float, float, float],
    clearAttribute: bool,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfControls: int,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    refreshOnRelease: int,
    statusBarMessage: str,
    selectedColorControl: str,
    selectedInterpControl: str,
    staticNumberOfControls: bool,
    staticPositions: bool,
    selectedPositionControl: str,
    upperLimitControl: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    verticalLayout: bool,
    width: int,
) -> Any:
    ...


def gradientControlNoAttr(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    asString: str,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    currentKeyInterpValue: int,
    currentKey: int,
    currentKeyChanged: Callable,
    currentKeyColorValue: Tuple[float, float, float],
    currentKeyCurveValue: bool,
    dragCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    optionVar: str,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rampAsColor: bool,
    statusBarMessage: str,
    useTemplate: str,
    valueAtPoint: float,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def graphDollyCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def graphSelectContext(*args, **kwargs) -> Any:
    ...


def graphTrackCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def gravity(
    *args: List[str],
    edit: bool,
    query: bool,
    attenuation: float,
    directionX: float,
    directionY: float,
    directionZ: float,
    magnitude: float,
    maxDistance: float,
    name: str,
    position: List[Tuple[float, float, float]],
    perVertex: bool,
    torusSectionRadius: float,
    volumeExclusion: bool,
    volumeOffset: Tuple[float, float, float],
    volumeShape: str,
    volumeSweep: float,
) -> Any:
    ...


def grid(
    *args: List[str],
    query: bool,
    divisions: int,
    displayAxes: bool,
    displayAxesBold: bool,
    displayDivisionLines: bool,
    default: bool,
    displayGridLines: bool,
    displayOrthographicLabels: bool,
    displayPerspectiveLabels: bool,
    orthographicLabelPosition: str,
    perspectiveLabelPosition: str,
    reset: bool,
    size: float,
    spacing: float,
    style: int,
    toggle: bool,
) -> Any:
    ...


def gridLayout(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    allowEmptyCells: bool,
    autoGrow: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    childArray: bool,
    cellHeight: int,
    columnsResizable: bool,
    cellWidth: int,
    cellWidthHeight: Tuple[int, int],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    gridOrder: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfColumns: int,
    numberOfChildren: bool,
    numberOfPopupMenus: bool,
    numberOfRows: int,
    numberOfRowsColumns: Tuple[int, int],
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    position: List[Tuple[str, int]],
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def group(
    *args: List[str],
    absolute: bool,
    empty: bool,
    name: str,
    parent: str,
    relative: bool,
    useAsGroup: str,
    world: bool,
) -> Any:
    ...


def groupParts() -> Any:
    ...


def hardenPointCurve(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    multiplicity: int,
    name: str,
    nodeState: int,
    object: bool,
    replaceOriginal: bool,
) -> Any:
    ...


def hardware(
    brdType: bool,
    cpuType: bool,
    graphicsType: bool,
    megaHertz: bool,
    numProcessors: bool,
) -> Any:
    ...


def hardwareRenderPanel(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    camera: str,
    copy: str,
    createString: bool,
    control: bool,
    defineTemplate: str,
    docTag: str,
    editString: bool,
    exists: bool,
    glRenderEditor: bool,
    init: bool,
    isUnique: bool,
    label: str,
    menuBarVisible: bool,
    menuBarRepeatLast: bool,
    needsInit: bool,
    parent: str,
    popupMenuProcedure: Callable,
    replacePanel: str,
    tearOff: bool,
    tearOffCopy: str,
    tearOffRestore: bool,
    unParent: bool,
    useTemplate: str,
) -> Any:
    ...


def hasMetadata(
    *args: List[str],
    asList: bool,
    channelType: str,
    channelName: str,
    endIndex: str,
    ignoreDefault: bool,
    indexType: str,
    index: List[str],
    memberName: str,
    scene: bool,
    startIndex: str,
    streamName: str,
) -> Any:
    ...


def headsUpDisplay(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    attributeChange: str,
    allDescendants: bool,
    allowOverlap: bool,
    attachToRefresh: bool,
    block: int,
    blockAlignment: str,
    blockSize: str,
    command: Callable,
    conditionChange: str,
    conditionFalse: str,
    connectionChange: str,
    conditionTrue: str,
    dataAlignment: str,
    dataFontSize: str,
    disregardIndex: bool,
    decimalPrecision: int,
    dataWidth: int,
    event: str,
    exists: bool,
    gridColor: int,
    label: str,
    listConditions: bool,
    listEvents: bool,
    labelFontSize: str,
    listHeadsUpDisplays: bool,
    listNodeChanges: bool,
    lastOccupiedBlock: int,
    listPresets: bool,
    layoutVisibility: bool,
    labelWidth: int,
    name: str,
    nodeChanges: List[str],
    nextFreeBlock: int,
    getOption: str,
    padding: int,
    preset: str,
    refresh: bool,
    remove: bool,
    removeID: int,
    resetNodeChanges: List[str],
    removePosition: Tuple[int, int],
    section: int,
    showGrid: bool,
    setOption: Tuple[str, str],
    scriptResult: bool,
    visible: bool,
) -> Any:
    ...


def headsUpMessage(*args, **kwargs) -> Any:
    ...


def help(
    arg0: str,
    /,
    query: bool,
    documentation: bool,
    list: bool,
    language: str,
    popupDisplayTime: int,
    popupMode: bool,
    popupPauseTime: int,
    popupSimpleMode: bool,
    rolloverMode: bool,
    syntaxOnly: bool,
) -> Any:
    ...


def helpLine(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def hide(
    *args: List[str],
    allObjects: bool,
    clearLastHidden: bool,
    clearSelection: bool,
    invertComponents: bool,
    returnHidden: bool,
    testVisibility: bool,
) -> Any:
    ...


def hikGlobals(edit: bool, query: bool, releaseAllPinning: bool) -> Any:
    ...


def hilite(*args: List[str], replace: bool, toggle: bool, unHilite: bool) -> Any:
    ...


def hitTest() -> Any:
    ...


def hotBox(
    query: bool,
    showAllToggleMenus: bool,
    animationOnlyMenus: bool,
    animationToggleMenus: bool,
    clothOnlyMenus: bool,
    clothToggleMenus: bool,
    commonOnlyMenus: bool,
    customMenuSetsToggleMenus: bool,
    commonToggleMenus: bool,
    displayCenterOnly: bool,
    displayHotbox: bool,
    dynamicsOnlyMenus: bool,
    displayStyle: bool,
    dynamicsToggleMenus: bool,
    displayZonesOnly: bool,
    liveOnlyMenus: bool,
    liveToggleMenus: bool,
    modelingOnlyMenus: bool,
    modelingToggleMenus: bool,
    menuSetOnly: str,
    menuSetToggle: Tuple[str, bool],
    noClickCommand: Callable,
    noClickDelay: float,
    noClickPosition: bool,
    noKeyPress: bool,
    polygonsOnlyMenus: bool,
    polygonsToggleMenus: bool,
    PaneOnlyMenus: bool,
    position: Tuple[int, int],
    PaneToggleMenus: bool,
    riggingOnlyMenus: bool,
    riggingToggleMenus: bool,
    release: bool,
    rmbPopups: bool,
    renderingOnlyMenus: bool,
    renderingToggleMenus: bool,
    surfacesOnlyMenus: bool,
    surfacesToggleMenus: bool,
    transparenyLevel: int,
    updateMenus: bool,
) -> Any:
    ...


def hotkey(
    arg0: str,
    /,
    query: bool,
    altModifier: bool,
    autoSave: bool,
    ctxClient: str,
    commandModifier: bool,
    ctrlModifier: bool,
    dragPress: bool,
    factorySettings: bool,
    keyShortcut: str,
    isModifier: bool,
    name: str,
    pressCommandRepeat: bool,
    releaseCommandRepeat: bool,
    releaseName: str,
    shiftModifier: bool,
    sourceUserHotkeys: bool,
) -> Any:
    ...


def hotkeyCheck(
    altModifier: bool,
    commandModifier: bool,
    ctrlModifier: bool,
    isRepeatable: bool,
    keyString: str,
    toBeRemovedInFutureMayaRelease: str,
    keyUp: bool,
    optionModifier: bool,
) -> Any:
    ...


def hotkeyCtx(
    query: bool,
    addClient: List[str],
    clientArray: bool,
    currentClient: str,
    insertTypeAt: Tuple[str, str],
    removeAllClients: bool,
    removeClient: List[str],
    removeType: str,
    type: str,
    typeArray: bool,
    typeExists: str,
) -> Any:
    ...


def hotkeyEditor(*args, **kwargs) -> Any:
    ...


def hotkeyEditorPanel(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def hotkeyMapSet(*args, **kwargs) -> Any:
    ...


def hotkeySet(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    current: bool,
    delete: bool,
    export: str,
    exists: bool,
    hotkeySetArray: bool,
    ip: str,
    rename: str,
    source: str,
) -> Any:
    ...


def hudButton(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    allowOverlap: bool,
    block: int,
    blockAlignment: str,
    blockSize: str,
    buttonShape: str,
    buttonWidth: int,
    label: str,
    labelFontSize: str,
    padding: int,
    pressCommand: Callable,
    releaseCommand: Callable,
    section: int,
    visible: bool,
) -> Any:
    ...


def hudSlider(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    allowOverlap: bool,
    block: int,
    blockAlignment: str,
    blockSize: str,
    dragCommand: Callable,
    decimalPrecision: int,
    internalPadding: int,
    label: str,
    labelFontSize: str,
    labelWidth: int,
    maxValue: float,
    minValue: float,
    padding: int,
    pressCommand: Callable,
    releaseCommand: Callable,
    section: int,
    sliderIncrement: float,
    sliderLength: int,
    type: str,
    value: float,
    valueAlignment: str,
    valueFontSize: str,
    visible: bool,
    valueWidth: int,
) -> Any:
    ...


def hudSliderButton(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    allowOverlap: bool,
    block: int,
    blockAlignment: str,
    buttonLabelFontSize: str,
    buttonLabel: str,
    buttonPressCommand: Callable,
    buttonReleaseCommand: Callable,
    blockSize: str,
    buttonShape: str,
    buttonWidth: int,
    decimalPrecision: int,
    internalPadding: int,
    maxValue: float,
    minValue: float,
    padding: int,
    section: int,
    sliderDragCommand: Callable,
    sliderLabelFontSize: str,
    sliderIncrement: float,
    sliderLabel: str,
    sliderLength: int,
    sliderLabelWidth: int,
    sliderPressCommand: Callable,
    sliderReleaseCommand: Callable,
    type: str,
    value: float,
    valueAlignment: str,
    valueFontSize: str,
    visible: bool,
    valueWidth: int,
) -> Any:
    ...


def hwReflectionMap(
    *args: List[str],
    edit: bool,
    query: bool,
    backTextureName: str,
    bottomTextureName: str,
    cubeMap: bool,
    decalMode: bool,
    enable: bool,
    frontTextureName: str,
    leftTextureName: str,
    rightTextureName: str,
    sphereMapTextureName: str,
    topTextureName: str,
) -> Any:
    ...


def hwRender(
    *args: List[str],
    query: bool,
    writeAlpha: bool,
    acceleratedMultiSampleSupport: bool,
    activeTextureCount: bool,
    camera: str,
    currentFrame: bool,
    currentView: bool,
    writeDepth: bool,
    edgeAntiAliasing: Tuple[int, int],
    frame: float,
    fixFileNameNumberPattern: bool,
    fullRenderSupport: bool,
    height: int,
    imageFileName: bool,
    layer: str,
    lowQualityLighting: bool,
    limitedRenderSupport: bool,
    noRenderView: bool,
    notWriteToFile: bool,
    printGeometry: bool,
    renderRegion: Tuple[int, int, int, int],
    textureResolution: int,
    renderHardwareName: bool,
    renderSelected: bool,
    width: int,
) -> Any:
    ...


def hwRenderLoad() -> Any:
    ...


def hyperGraph(*args, **kwargs) -> Any:
    ...


def hyperPanel(*args, **kwargs) -> Any:
    ...


def hyperShade(*args, **kwargs) -> Any:
    ...


def iconTextButton(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    actionIsSubstitute: bool,
    align: str,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    command: Callable,
    doubleClickCommand: Callable,
    dragCallback: Callable,
    disabledImage: str,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    flat: bool,
    font: str,
    fullPathName: bool,
    flipX: float,
    flipY: float,
    height: int,
    highlightImage: str,
    highlightColor: Tuple[float, float, float],
    handleNodeDropCallback: Callable,
    image: str,
    image1: str,
    image2: str,
    image3: str,
    isObscured: bool,
    imageOverlayLabel: str,
    label: str,
    labelEditingCallback: Callable,
    labelOffset: int,
    manage: bool,
    marginHeight: int,
    marginWidth: int,
    noBackground: bool,
    numberOfPopupMenus: bool,
    overlayLabelBackColor: Tuple[float, float, float, float],
    overlayLabelColor: Tuple[float, float, float],
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rotation: float,
    commandRepeatable: bool,
    statusBarMessage: str,
    selectionImage: str,
    scaleIcon: bool,
    style: str,
    sourceType: str,
    useAlpha: float,
    useTemplate: str,
    visibleChangeCommand: Callable,
    version: str,
    visible: bool,
    width: int,
) -> Any:
    ...


def iconTextCheckBox(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    align: str,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    dragCallback: Callable,
    disabledImage: str,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    flat: bool,
    font: str,
    fullPathName: bool,
    flipX: float,
    flipY: float,
    height: int,
    highlightImage: str,
    highlightColor: Tuple[float, float, float],
    image: str,
    image1: str,
    image2: str,
    image3: str,
    isObscured: bool,
    imageOverlayLabel: str,
    label: str,
    labelOffset: int,
    manage: bool,
    marginHeight: int,
    marginWidth: int,
    noBackground: bool,
    numberOfPopupMenus: bool,
    offCommand: Callable,
    overlayLabelBackColor: Tuple[float, float, float, float],
    overlayLabelColor: Tuple[float, float, float],
    onCommand: Callable,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rotation: float,
    statusBarMessage: str,
    selectionHighlightImage: str,
    selectionImage: str,
    style: str,
    useAlpha: float,
    useTemplate: str,
    value: bool,
    visibleChangeCommand: Callable,
    version: str,
    visible: bool,
    width: int,
) -> Any:
    ...


def iconTextRadioButton(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    align: str,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    collection: str,
    dragCallback: Callable,
    disabledImage: str,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    flat: bool,
    font: str,
    fullPathName: bool,
    flipX: float,
    flipY: float,
    height: int,
    highlightImage: str,
    highlightColor: Tuple[float, float, float],
    image: str,
    image1: str,
    image2: str,
    image3: str,
    isObscured: bool,
    imageOverlayLabel: str,
    label: str,
    labelOffset: int,
    manage: bool,
    marginHeight: int,
    marginWidth: int,
    noBackground: bool,
    numberOfPopupMenus: bool,
    offCommand: Callable,
    overlayLabelBackColor: Tuple[float, float, float, float],
    overlayLabelColor: Tuple[float, float, float],
    onCommand: Callable,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rotation: float,
    statusBarMessage: str,
    selectionHighlightImage: str,
    selectionImage: str,
    select: bool,
    style: str,
    useAlpha: float,
    useTemplate: str,
    visibleChangeCommand: Callable,
    version: str,
    visible: bool,
    width: int,
) -> Any:
    ...


def iconTextRadioCollection(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    collectionItemArray: bool,
    disableCommands: bool,
    defineTemplate: str,
    exists: bool,
    gl: bool,
    numberOfCollectionItems: bool,
    parent: str,
    select: str,
    useTemplate: str,
) -> Any:
    ...


def iconTextScrollList(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    append: List[str],
    allowMultiSelection: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    deselectAll: bool,
    doubleClickCommand: Callable,
    dragFeedbackVisible: bool,
    dragCallback: Callable,
    dropCallback: Callable,
    dropRectCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    editable: bool,
    editIndexed: int,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    itemAt: Tuple[int, int],
    isObscured: bool,
    itemTextColor: List[Tuple[int, float, float, float]],
    manage: bool,
    noBackground: bool,
    numberOfIcons: int,
    numberOfPopupMenus: bool,
    numberOfRows: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    removeAll: bool,
    statusBarMessage: str,
    selectCommand: Callable,
    selectItem: List[str],
    selectIndexedItem: List[int],
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    visualRectAt: Tuple[int, int],
    width: int,
) -> Any:
    ...


def iconTextStaticLabel(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    align: str,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    dragCallback: Callable,
    disabledImage: str,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    font: str,
    fullPathName: bool,
    flipX: float,
    flipY: float,
    height: int,
    highlightColor: Tuple[float, float, float],
    image: str,
    image1: str,
    image2: str,
    image3: str,
    isObscured: bool,
    imageOverlayLabel: str,
    label: str,
    labelOffset: int,
    manage: bool,
    marginHeight: int,
    marginWidth: int,
    noBackground: bool,
    numberOfPopupMenus: bool,
    overlayLabelBackColor: Tuple[float, float, float, float],
    overlayLabelColor: Tuple[float, float, float],
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rotation: float,
    statusBarMessage: str,
    style: str,
    useAlpha: float,
    useTemplate: str,
    visibleChangeCommand: Callable,
    version: str,
    visible: bool,
    width: int,
) -> Any:
    ...


def ikHandle(
    *args: List[str],
    edit: bool,
    query: bool,
    autoPriority: bool,
    curve: str,
    createCurve: bool,
    connectEffector: bool,
    createRootAxis: bool,
    disableHandles: bool,
    endEffector: str,
    enableHandles: bool,
    exists: str,
    freezeJoints: bool,
    forceSolver: bool,
    jointList: bool,
    name: str,
    numSpans: int,
    priority: int,
    parentCurve: bool,
    positionWeight: float,
    rootOnCurve: bool,
    rootTwistMode: bool,
    sticky: str,
    simplifyCurve: bool,
    snapHandleToEffector: bool,
    snapHandleFlagToggle: bool,
    startJoint: str,
    snapCurve: bool,
    solver: str,
    setupForRPsolver: bool,
    twistType: str,
    weight: float,
) -> Any:
    ...


def ikHandleCtx(*args, **kwargs) -> Any:
    ...


def ikHandleDisplayScale(*args, **kwargs) -> Any:
    ...


def ikSolver(
    *args: List[str],
    edit: bool,
    query: bool,
    epsilon: float,
    maxIterations: int,
    name: str,
    solverType: str,
) -> Any:
    ...


def ikSplineHandleCtx(*args, **kwargs) -> Any:
    ...


def ikSystem(
    edit: bool,
    query: bool,
    autoPriority: bool,
    autoPriorityMC: bool,
    autoPrioritySC: bool,
    allowRotation: bool,
    list: Tuple[int, int],
    snap: bool,
    solve: bool,
    solverTypes: bool,
) -> Any:
    ...


def ikSystemInfo(arg0: bool, /, query: bool, globalSnapHandle: bool) -> Any:
    ...


def ikfkDisplayMethod(query: bool, display: str) -> Any:
    ...


def illustratorCurves(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    illustratorFilename: str,
    name: str,
    nodeState: int,
    object: bool,
    scaleFactor: float,
    tolerance: float,
) -> Any:
    ...


def image(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    image: str,
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def imagePlane(
    *args: List[str],
    edit: bool,
    query: bool,
    camera: str,
    counter: bool,
    detach: bool,
    dropFrame: bool,
    frameDuration: int,
    fileName: str,
    height: float,
    imageSize: Tuple[int, int],
    lookThrough: str,
    maintainRatio: bool,
    name: str,
    numFrames: int,
    negTimesOK: bool,
    quickTime: bool,
    showInAllViews: bool,
    timeCode: int,
    twentyFourHourMax: bool,
    timeScale: int,
    timeCodeTrack: bool,
    width: float,
) -> Any:
    ...


def imageWindowEditor(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    autoResize: bool,
    changeCommand: Tuple[str, str, str, str],
    clear: Tuple[int, int, float, float, float],
    control: bool,
    drawAxis: bool,
    doubleBuffer: bool,
    displayImage: int,
    displayStyle: str,
    defineTemplate: str,
    docTag: str,
    exists: bool,
    filter: str,
    frameImage: bool,
    forceMainConnection: str,
    frameRegion: bool,
    highlightConnection: str,
    lockMainConnection: bool,
    loadImage: str,
    mainListConnection: str,
    marquee: Tuple[float, float, float, float],
    nbImages: bool,
    parent: str,
    panel: str,
    removeAllImages: bool,
    refresh: bool,
    removeImage: bool,
    realSize: bool,
    scaleBlue: float,
    singleBuffer: bool,
    scaleGreen: float,
    saveImage: bool,
    selectionConnection: str,
    scaleRed: float,
    showRegion: Tuple[int, int],
    stateString: bool,
    toggle: bool,
    unlockMainConnection: bool,
    unParent: bool,
    updateMainConnection: bool,
    useTemplate: str,
    writeImage: str,
) -> Any:
    ...


def imfPlugins(
    arg0: str,
    /,
    query: bool,
    extension: str,
    keyword: str,
    multiFrameSupport: str,
    pluginName: str,
    readSupport: str,
    writeSupport: str,
) -> Any:
    ...


def inViewMessage(
    alpha: float,
    assistMessage: str,
    backColor: int,
    clickKill: bool,
    clear: str,
    dragKill: bool,
    fade: bool,
    fadeInTime: int,
    frameOffset: int,
    fadeOutTime: int,
    fadeStayTime: int,
    font: str,
    fontSize: int,
    hide: bool,
    minimize: bool,
    message: str,
    position: str,
    restore: bool,
    show: bool,
    statusMessage: str,
    textAlpha: float,
    textOffset: int,
    uvEditor: bool,
) -> Any:
    ...


def inheritTransform(
    *args: List[str], query: bool, preserve: bool, toggle: bool
) -> Any:
    ...


def insertJoint() -> Any:
    ...


def insertJointCtx(*args, **kwargs) -> Any:
    ...


def insertKeyCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    breakdown: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
    preserveTangent: bool,
) -> Any:
    ...


def insertKnotCurve(
    *args: List[str],
    edit: bool,
    query: bool,
    addKnots: bool,
    caching: bool,
    constructionHistory: bool,
    curveOnSurface: bool,
    frozen: bool,
    insertBetween: bool,
    name: str,
    nodeState: int,
    numberOfKnots: List[int],
    object: bool,
    parameter: List[float],
    replaceOriginal: bool,
) -> Any:
    ...


def insertKnotSurface(
    *args: List[str],
    edit: bool,
    query: bool,
    addKnots: bool,
    caching: bool,
    constructionHistory: bool,
    direction: int,
    frozen: bool,
    insertBetween: bool,
    name: str,
    nodeState: int,
    numberOfKnots: List[int],
    object: bool,
    parameter: List[float],
    replaceOriginal: bool,
) -> Any:
    ...


def insertListItem() -> Any:
    ...


def insertListItemBefore() -> Any:
    ...


def instance(*args: List[str], leaf: bool, name: str, smartTransform: bool) -> Any:
    ...


def instanceable(
    *args: List[str], query: bool, allow: bool, recursive: bool, shape: bool
) -> Any:
    ...


def instancer(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    addObject: bool,
    cycle: str,
    cycleStep: float,
    cycleStepUnits: str,
    index: int,
    levelOfDetail: str,
    name: str,
    object: List[str],
    objectPosition: str,
    objectRotation: str,
    objectScale: str,
    pointDataSource: bool,
    removeObject: bool,
    rotationOrder: str,
    rotationUnits: str,
    valueName: str,
) -> Any:
    ...


def intField(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    dragCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enterCommand: Callable,
    editable: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    maxValue: int,
    minValue: int,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    receiveFocusCommand: Callable,
    step: int,
    statusBarMessage: str,
    useTemplate: str,
    value: int,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def intFieldGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    changeCommand: Callable,
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    dragCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    extraLabel: str,
    enable: bool,
    enable1: bool,
    enable2: bool,
    enable3: bool,
    enable4: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    label: str,
    manage: bool,
    noBackground: bool,
    numberOfFields: int,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rowAttach: List[Tuple[int, str, int]],
    statusBarMessage: str,
    useTemplate: str,
    value: Tuple[int, int, int, int],
    value1: int,
    value2: int,
    value3: int,
    value4: int,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def intScrollBar(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    dragCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    horizontal: bool,
    isObscured: bool,
    largeStep: int,
    manage: bool,
    maxValue: int,
    minValue: int,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    step: int,
    statusBarMessage: str,
    useTemplate: str,
    value: int,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def intSlider(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    dragCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    horizontal: bool,
    isObscured: bool,
    manage: bool,
    maxValue: int,
    minValue: int,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    step: int,
    statusBarMessage: str,
    useTemplate: str,
    value: int,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def intSliderGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    changeCommand: Callable,
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    dragCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    extraLabel: str,
    enable: bool,
    exists: bool,
    field: bool,
    fieldMinValue: int,
    fieldMaxValue: int,
    fullPathName: bool,
    fieldStep: int,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    label: str,
    manage: bool,
    maxValue: int,
    minValue: int,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rowAttach: List[Tuple[int, str, int]],
    step: int,
    statusBarMessage: str,
    sliderStep: int,
    useTemplate: str,
    value: int,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def interactionStyle(query: bool, style: str) -> Any:
    ...


def internalVar(
    mayaInstallDir: bool,
    userAppDir: bool,
    userBitmapsDir: bool,
    userHotkeyDir: bool,
    userMarkingMenuDir: bool,
    userPrefDir: bool,
    userPresetsDir: bool,
    userScriptDir: bool,
    userShelfDir: bool,
    userTmpDir: bool,
    userWorkspaceDir: bool,
) -> Any:
    ...


def intersect(
    *args: Tuple[str, str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    curveOnSurface: bool,
    firstSurface: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    tolerance: float,
) -> Any:
    ...


def invertShape() -> Any:
    ...


def iprEngine(*args, **kwargs) -> Any:
    ...


def isConnected(*args: Tuple[str, str], ignoreUnitConversion: bool) -> Any:
    ...


def isDirty(*args: List[Incomplete], connection: bool, datablock: bool) -> Any:
    ...


def isTrue() -> Any:
    ...


def isolateSelect(
    arg0: str,
    /,
    query: bool,
    addDagObject: str,
    addSelected: bool,
    addSelectedObjects: bool,
    loadSelected: bool,
    removeDagObject: str,
    removeSelected: bool,
    state: bool,
    update: bool,
    viewObjects: bool,
) -> Any:
    ...


def itemFilter(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    byBin: List[str],
    byName: str,
    byScript: str,
    byType: List[str],
    category: List[str],
    clearByBin: bool,
    clearByType: bool,
    classification: str,
    difference: Tuple[str, str],
    exists: bool,
    intersect: Tuple[str, str],
    listBuiltInFilters: bool,
    listOtherFilters: bool,
    listUserFilters: bool,
    negate: bool,
    parent: str,
    pythonModule: str,
    secondScript: str,
    text: str,
    union: Tuple[str, str],
    uniqueNodeNames: bool,
) -> Any:
    ...


def itemFilterAttr(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    byName: str,
    byNameString: List[str],
    byScript: str,
    classification: str,
    dynamic: bool,
    exists: bool,
    hidden: bool,
    hasCurve: bool,
    hasDrivenKey: bool,
    hasExpression: bool,
    intersect: Tuple[str, str],
    keyable: bool,
    listBuiltInFilters: bool,
    listOtherFilters: bool,
    listUserFilters: bool,
    negate: bool,
    parent: str,
    published: bool,
    readable: bool,
    scaleRotateTranslate: bool,
    secondScript: str,
    text: str,
    union: Tuple[str, str],
    writable: bool,
) -> Any:
    ...


def itemFilterRender(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    anyTextures: bool,
    category: List[str],
    classification: str,
    exists: bool,
    exclusiveLights: bool,
    lights: bool,
    listBuiltInFilters: bool,
    linkedLights: bool,
    listOtherFilters: bool,
    lightSets: bool,
    listUserFilters: bool,
    nodeClassification: List[str],
    negate: bool,
    nonIlluminatingLights: bool,
    nonExclusiveLights: bool,
    parent: str,
    postProcess: bool,
    renderingNode: bool,
    renderableObjectSets: bool,
    renderUtilityNode: bool,
    shaders: bool,
    text: str,
    textures2d: bool,
    textures3d: bool,
    texturesProcedural: bool,
) -> Any:
    ...


def itemFilterType(arg0: str, /, edit: bool, query: bool, text: str, type: bool) -> Any:
    ...


def iterOnNurbs(*args, **kwargs) -> Any:
    ...


def joint(
    *args: List[str],
    edit: bool,
    query: bool,
    absolute: bool,
    automaticLimits: bool,
    assumePreferredAngles: bool,
    angleX: float,
    angleY: float,
    angleZ: float,
    children: bool,
    component: bool,
    degreeOfFreedom: str,
    exists: str,
    limitSwitchX: bool,
    limitSwitchY: bool,
    limitSwitchZ: bool,
    limitX: Tuple[float, float],
    limitY: Tuple[float, float],
    limitZ: Tuple[float, float],
    name: str,
    orientation: Tuple[float, float, float],
    orientJoint: str,
    position: Tuple[float, float, float],
    relative: bool,
    radius: float,
    rotationOrder: str,
    scale: Tuple[float, float, float],
    symmetryAxis: str,
    secondaryAxisOrient: str,
    scaleCompensate: bool,
    scaleOrientation: Tuple[float, float, float],
    setPreferredAngles: bool,
    stiffnessX: float,
    stiffnessY: float,
    stiffnessZ: float,
    symmetry: bool,
    zeroScaleOrient: bool,
) -> Any:
    ...


def jointCluster(
    *args: List[str],
    edit: bool,
    query: bool,
    aboveBound: float,
    aboveCluster: bool,
    aboveDropoffType: str,
    aboveValue: float,
    belowBound: float,
    belowCluster: bool,
    belowDropoffType: str,
    belowValue: float,
    deformerTools: bool,
    joint: str,
    name: str,
) -> Any:
    ...


def jointCtx(*args, **kwargs) -> Any:
    ...


def jointDisplayScale(arg0: float, /, query: bool, absolute: bool, ikfk: bool) -> Any:
    ...


def jointLattice(
    *args: List[str],
    edit: bool,
    query: bool,
    after: bool,
    afterReference: bool,
    before: bool,
    components: bool,
    selectedComponents: bool,
    creasing: float,
    deformerTools: bool,
    exclusive: str,
    frontOfChain: bool,
    geometry: List[str],
    geometryIndices: bool,
    includeHiddenSelections: bool,
    ignoreSelected: bool,
    joint: str,
    lowerBindSkin: str,
    lengthIn: float,
    lengthOut: float,
    lowerTransform: str,
    name: str,
    parallel: bool,
    prune: bool,
    remove: List[bool],
    rounding: float,
    split: bool,
    upperBindSkin: str,
    useComponentTags: bool,
    upperTransform: str,
    widthLeft: float,
    widthRight: float,
) -> Any:
    ...


def journal(
    query: bool, comment: str, flush: bool, highPrecision: bool, state: bool
) -> Any:
    ...


def keyTangent(
    *args: List[str],
    edit: bool,
    query: bool,
    absolute: bool,
    animation: str,
    attribute: List[str],
    controlPoints: bool,
    float: List[Incomplete],
    g: bool,
    hierarchy: str,
    inAngle: float,
    index: List[Incomplete],
    inTangentType: str,
    includeUpperBound: bool,
    inWeight: float,
    lock: bool,
    outAngle: float,
    outTangentType: str,
    outWeight: float,
    pluginTangentTypes: str,
    relative: bool,
    shape: bool,
    stepAttributes: bool,
    time: List[Incomplete],
    unify: bool,
    weightLock: bool,
    weightedTangents: bool,
) -> Any:
    ...


def keyframe(
    *args: List[str],
    edit: bool,
    query: bool,
    absolute: bool,
    adjustBreakdown: bool,
    animation: str,
    attribute: List[str],
    breakdown: bool,
    controlPoints: bool,
    clipTime: Tuple[int, int, float],
    eval: bool,
    float: List[Incomplete],
    floatChange: float,
    hierarchy: str,
    index: List[Incomplete],
    includeUpperBound: bool,
    indexValue: bool,
    keyframeCount: bool,
    lastSelected: bool,
    name: bool,
    option: str,
    relative: bool,
    shape: bool,
    selected: bool,
    time: List[Incomplete],
    timeChange: int,
    tickDrawSpecial: bool,
    valueChange: float,
) -> Any:
    ...


def keyframeOutliner(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    animCurve: str,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    dragCallback: Callable,
    dropCallback: Callable,
    display: str,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def keyframeRegionCurrentTimeCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def keyframeRegionDirectKeyCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
    option: str,
) -> Any:
    ...


def keyframeRegionDollyCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def keyframeRegionInsertKeyCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    breakdown: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def keyframeRegionMoveKeyCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
    option: str,
) -> Any:
    ...


def keyframeRegionScaleKeyCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
    scaleSpecifiedKeys: bool,
    type: str,
) -> Any:
    ...


def keyframeRegionSelectKeyCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def keyframeRegionSetKeyCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    breakdown: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def keyframeRegionTrackCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def keyframeStats(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    animEditor: str,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    classicMode: bool,
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    precision: int,
    rowAttach: List[Tuple[int, str, int]],
    statusBarMessage: str,
    timeAnnotation: str,
    useTemplate: str,
    valueAnnotation: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def keyingGroup(
    *args: List[str],
    edit: bool,
    query: bool,
    activator: str,
    addElement: str,
    afterFilters: bool,
    anyMember: str,
    category: str,
    clear: str,
    color: int,
    copy: str,
    excludeDynamic: bool,
    edges: bool,
    empty: bool,
    editPoints: bool,
    excludeRotate: bool,
    excludeScale: bool,
    excludeTranslate: bool,
    excludeVisibility: bool,
    facets: bool,
    forceElement: str,
    setActiveFilter: str,
    flatten: str,
    isIntersecting: str,
    isMember: str,
    include: str,
    intersection: str,
    layer: bool,
    minimizeRotation: bool,
    name: str,
    noIntermediate: bool,
    nodesOnly: bool,
    noSurfaceShader: bool,
    noWarnings: bool,
    renderable: bool,
    removeActivator: str,
    remove: str,
    size: bool,
    split: str,
    subtract: str,
    text: str,
    union: str,
    vertices: bool,
) -> Any:
    ...


def lassoContext(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    drawClosed: bool,
    exists: bool,
    fastComponents: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def lattice(
    *args: List[str],
    edit: bool,
    query: bool,
    after: bool,
    afterReference: bool,
    before: bool,
    components: bool,
    selectedComponents: bool,
    commonParent: bool,
    dualBase: bool,
    deformerTools: bool,
    divisions: Tuple[int, int, int],
    exclusive: str,
    freezeMapping: bool,
    frontOfChain: bool,
    geometry: List[str],
    geometryIndices: bool,
    includeHiddenSelections: bool,
    ignoreSelected: bool,
    ldivisions: Tuple[int, int, int],
    latticeReset: bool,
    name: str,
    objectCentered: bool,
    outsideFalloffDistance: float,
    outsideLattice: int,
    parallel: bool,
    position: Tuple[float, float, float],
    prune: bool,
    remove: List[bool],
    rotation: Tuple[float, float, float],
    removeTweaks: bool,
    scale: Tuple[float, float, float],
    split: bool,
    useComponentTags: bool,
) -> Any:
    ...


def latticeDeformKeyCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    envelope: float,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    latticeColumns: int,
    latticeRows: int,
    name: str,
    scaleLatticePts: bool,
) -> Any:
    ...


def launch(directory: str, movie: str, pdfFile: str, webPage: str) -> Any:
    ...


def launchImageEditor(editImageFile: str, viewImageFile: str) -> Any:
    ...


def layerButton(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    command: Callable,
    changeCommand: Callable,
    color: Tuple[float, float, float],
    current: bool,
    doubleClickCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    layerHideOnPlayback: bool,
    hideOnPlaybackCommand: Callable,
    identification: int,
    isObscured: bool,
    label: str,
    layerState: str,
    layerVisible: bool,
    labelWidth: bool,
    manage: bool,
    name: str,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    renameCommand: str,
    select: bool,
    statusBarMessage: str,
    transparent: bool,
    typeCommand: Callable,
    useTemplate: str,
    visibleCommand: Callable,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def layeredShaderPort(*args, **kwargs) -> Any:
    ...


def layeredTexturePort(*args, **kwargs) -> Any:
    ...


def layout(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    childArray: bool,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfChildren: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def layoutDialog(
    backgroundColor: Tuple[float, float, float],
    dismiss: str,
    parent: str,
    title: str,
    uiScript: Callable,
) -> Any:
    ...


def license(
    borrow: bool,
    info: bool,
    isBorrowed: bool,
    isExported: bool,
    isTrial: bool,
    licenseMethod: bool,
    productChoice: bool,
    r: bool,
    status: bool,
    showBorrowInfo: bool,
    showProductInfoDialog: bool,
    usage: bool,
) -> Any:
    ...


def licenseCheck(mode: str, type: str) -> Any:
    ...


def lightList(*args: List[str], edit: bool, query: bool, remove: str) -> Any:
    ...


def lightlink(
    *args: List[str],
    b: bool,
    hierarchy: bool,
    light: List[str],
    make: bool,
    object: List[str],
    query: bool,
    sets: bool,
    shadow: bool,
    shapes: bool,
    transforms: bool,
    useActiveLights: bool,
    useActiveObjects: bool,
) -> Any:
    ...


def linearPrecision(arg0: int, /, query: bool) -> Any:
    ...


def listAnimatable(
    *args: List[str],
    active: bool,
    manip: bool,
    manipHandle: bool,
    shape: bool,
    type: bool,
) -> Any:
    ...


def listAttr(
    *args: List[str],
    array: bool,
    connectable: bool,
    caching: bool,
    channelBox: bool,
    changedSinceFileOpen: bool,
    category: List[str],
    extension: bool,
    fromPlugin: bool,
    hasData: bool,
    hasNullData: bool,
    inUse: bool,
    keyable: bool,
    locked: bool,
    leaf: bool,
    multi: bool,
    output: bool,
    read: bool,
    ramp: bool,
    readOnly: bool,
    scalar: bool,
    scalarAndArray: bool,
    settable: bool,
    shortNames: bool,
    string: List[str],
    unlocked: bool,
    userDefined: bool,
    usedAsFilename: bool,
    visible: bool,
    write: bool,
) -> Any:
    ...


def listAttrPatterns(patternType: bool, verbose: bool) -> Any:
    ...


def listCameras(orthographic: bool, perspective: bool, ufeCameras: bool) -> Any:
    ...


def listConnections(
    *args: List[str],
    connections: bool,
    destination: bool,
    exactType: bool,
    plugs: bool,
    source: bool,
    skipConversionNodes: bool,
    shapes: bool,
    type: str,
) -> Any:
    ...


def listDeviceAttachments(*args, **kwargs) -> Any:
    ...


def listHistory(
    *args: List[str],
    query: bool,
    allConnections: bool,
    allFuture: bool,
    allGraphs: bool,
    breadthFirst: bool,
    future: bool,
    fastIteration: bool,
    futureLocalAttr: bool,
    futureWorldAttr: bool,
    groupLevels: bool,
    historyAttr: bool,
    interestLevel: int,
    leaf: bool,
    levels: int,
    pruneDagObjects: bool,
) -> Any:
    ...


def listInputDeviceAxes(*args, **kwargs) -> Any:
    ...


def listInputDeviceButtons(*args, **kwargs) -> Any:
    ...


def listInputDevices(*args, **kwargs) -> Any:
    ...


def listNodeTypes(arg0: str, /, exclude: str) -> Any:
    ...


def listNodesWithIncorrectNames() -> Any:
    ...


def listRelatives(
    *args: List[str],
    allDescendents: bool,
    allParents: bool,
    children: bool,
    fullPath: bool,
    noIntermediate: bool,
    parent: bool,
    path: bool,
    shapes: bool,
    type: List[str],
) -> Any:
    ...


def listSets(allSets: bool, extendToShape: bool, object: str, type: int) -> Any:
    ...


def loadFluid(
    *args: List[str],
    edit: bool,
    query: bool,
    currentTime: bool,
    frame: float,
    initialConditions: bool,
) -> Any:
    ...


def loadModule(allModules: bool, load: str, scan: bool) -> Any:
    ...


def loadPlugin(
    *args: List[str],
    allPlugins: bool,
    addCallback: Callable,
    name: str,
    qObsolete: bool,
    quiet: bool,
    removeCallback: Callable,
) -> Any:
    ...


def loadPrefObjects() -> Any:
    ...


def loadUI(
    uiFile: str, listTypes: bool, uiString: str, verbose: bool, workingDirectory: str
) -> Any:
    ...


def lockNode(
    *args: List[str],
    query: bool,
    ignoreComponents: bool,
    lock: bool,
    lockName: bool,
    lockUnpublished: bool,
) -> Any:
    ...


def loft(
    *args: List[str],
    edit: bool,
    query: bool,
    autoReverse: bool,
    close: bool,
    createCusp: List[bool],
    caching: bool,
    constructionHistory: bool,
    degree: int,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    polygon: int,
    reverse: List[bool],
    rebuild: bool,
    range: bool,
    reverseSurfaceNormals: bool,
    sectionSpans: int,
    uniform: bool,
) -> Any:
    ...


def lookThru(
    *args: Tuple[str, str], query: bool, farClip: float, nearClip: float
) -> Any:
    ...


def ls(
    *args: List[str],
    absoluteName: bool,
    allPaths: bool,
    assemblies: bool,
    cameras: bool,
    containers: bool,
    containerType: List[str],
    dagObjects: bool,
    dependencyNodes: bool,
    defaultNodes: bool,
    exactType: List[str],
    excludeType: List[str],
    flatten: bool,
    geometry: bool,
    ghost: bool,
    head: int,
    hilite: bool,
    intermediateObjects: bool,
    invisible: bool,
    long: bool,
    leaf: bool,
    lockedNodes: bool,
    lights: bool,
    live: bool,
    materials: bool,
    modified: bool,
    noIntermediate: bool,
    nodeTypes: bool,
    objectsOnly: bool,
    orderedSelection: bool,
    planes: bool,
    persistentNodes: bool,
    partitions: bool,
    preSelectHilite: bool,
    recursive: bool,
    references: bool,
    renderGlobals: bool,
    referencedNodes: bool,
    readOnly: bool,
    renderQualities: bool,
    renderResolutions: bool,
    renderSetups: bool,
    shapes: bool,
    sets: bool,
    selection: bool,
    shortNames: bool,
    showNamespace: bool,
    showType: bool,
    textures: bool,
    tail: int,
    templated: bool,
    transforms: bool,
    type: List[str],
    undeletable: bool,
    ufeObjects: bool,
    uuid: bool,
    untemplated: bool,
    visible: bool,
) -> Any:
    ...


def lsThroughFilter(
    *args: List[Incomplete],
    item: List[str],
    nodeArray: bool,
    reverse: bool,
    selection: bool,
    sort: str,
) -> Any:
    ...


def lsUI(
    *args: List[str],
    controlLayouts: bool,
    collection: bool,
    cmdTemplates: bool,
    controls: bool,
    contexts: bool,
    dumpWidgets: bool,
    editors: bool,
    head: int,
    long: bool,
    menus: bool,
    menuItems: bool,
    numWidgets: bool,
    panels: bool,
    radioMenuItemCollections: bool,
    tail: int,
    type: List[str],
    workspaceControls: bool,
    windows: bool,
) -> Any:
    ...


def makeIdentity(
    *args: List[str],
    apply: bool,
    jointOrient: bool,
    normal: int,
    preserveNormals: bool,
    rotate: bool,
    scale: bool,
    translate: bool,
) -> Any:
    ...


def makeLive(*args: List[str], none: bool) -> Any:
    ...


def makePaintable(
    *args: Tuple[str, str],
    query: bool,
    altAttribute: List[str],
    activate: bool,
    activateAll: bool,
    attrType: str,
    clearAll: bool,
    remove: bool,
    shapeMode: str,
    uiName: str,
) -> Any:
    ...


def makeSingleSurface(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    chordHeightRatio: float,
    chordHeight: float,
    delta: float,
    edgeSwap: bool,
    format: int,
    fractionalTolerance: float,
    frozen: bool,
    minEdgeLength: float,
    matchNormalDir: bool,
    name: str,
    nodeState: int,
    normalizeTrimmedUVRange: bool,
    object: bool,
    polygonCount: int,
    polygonType: int,
    stitchTolerance: float,
    useChordHeight: bool,
    useChordHeightRatio: bool,
    uNumber: int,
    uType: int,
    vNumber: int,
    vType: int,
) -> Any:
    ...


def makebot(
    checkdepends: bool,
    input: str,
    nooverwrite: bool,
    output: str,
    checkres: int,
    verbose: bool,
) -> Any:
    ...


def manipComponentPivot(*args, **kwargs) -> Any:
    ...


def manipComponentUpdate() -> Any:
    ...


def manipMoveContext(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    alignAlong: Tuple[float, float, float],
    activeHandle: int,
    activeHandleNormal: int,
    bakePivotOri: bool,
    currentActiveHandle: int,
    editPivotMode: bool,
    editPivotPosition: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    interactiveUpdate: bool,
    lastMode: int,
    mode: int,
    orientAxes: Tuple[float, float, float],
    orientJoint: str,
    orientJointEnabled: bool,
    orientObject: str,
    orientTowards: Tuple[float, float, float],
    position: bool,
    preserveChildPosition: bool,
    pinPivot: bool,
    postDragCommand: Tuple[Callable, str],
    pivotOriHandle: bool,
    preCommand: Callable,
    preDragCommand: Tuple[Callable, str],
    postCommand: Callable,
    preserveUV: bool,
    reflectionAbout: int,
    reflectionAxis: int,
    reflection: bool,
    reflectionTolerance: float,
    snap: bool,
    secondaryAxisOrient: str,
    snapComponentsRelative: bool,
    snapLiveFaceCenter: bool,
    snapLivePoint: bool,
    snapPivotOri: bool,
    snapPivotPos: bool,
    snapRelative: bool,
    snapValue: float,
    translate: Tuple[float, float, float],
    tweakMode: bool,
    manipVisible: bool,
    xformConstraint: str,
    constrainAlongNormal: bool,
) -> Any:
    ...


def manipMoveLimitsCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def manipOptions(
    query: bool,
    enableSmartDuplicate: bool,
    enableSmartExtrude: bool,
    forceRefresh: bool,
    hideManipOnCtrl: bool,
    hideManipOnShift: bool,
    handleSize: float,
    hideManipOnShiftCtrl: bool,
    linePick: float,
    lineSize: float,
    middleMouseRepositioning: bool,
    planeHandleOffset: int,
    pivotRotateHandleOffset: int,
    pointSize: float,
    preselectHighlight: bool,
    relative: bool,
    rememberActiveHandle: bool,
    rememberActiveHandleAfterToolSwitch: bool,
    refreshMode: int,
    scale: float,
    smartDuplicateType: int,
    showExtrudeSliders: bool,
    showPlaneHandles: bool,
    showPivotRotateHandle: bool,
) -> Any:
    ...


def manipPivot(
    query: bool,
    bakeOri: bool,
    moveToolOri: int,
    orientation: Tuple[float, float, float],
    oriValid: bool,
    position: Tuple[float, float, float],
    pinPivot: bool,
    posValid: bool,
    reset: bool,
    resetOri: bool,
    resetPos: bool,
    rotateToolOri: int,
    snapOri: bool,
    snapPos: bool,
    scaleToolOri: int,
    valid: bool,
) -> Any:
    ...


def manipRotateContext(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    alignAlong: Tuple[float, float, float],
    activeHandle: int,
    bakePivotOri: bool,
    currentActiveHandle: int,
    centerTrackball: bool,
    editPivotMode: bool,
    editPivotPosition: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    lastMode: int,
    mode: int,
    modifyTranslation: bool,
    orientAxes: Tuple[float, float, float],
    orientObject: str,
    orientTowards: Tuple[float, float, float],
    position: bool,
    preserveChildPosition: bool,
    pinPivot: bool,
    postDragCommand: Tuple[Callable, str],
    pivotOriHandle: bool,
    preCommand: Callable,
    preDragCommand: Tuple[Callable, str],
    postCommand: Callable,
    preserveUV: bool,
    reflectionAbout: int,
    reflectionAxis: int,
    reflection: bool,
    reflectionTolerance: float,
    rotate: Tuple[float, float, float],
    snap: bool,
    snapPivotOri: bool,
    snapPivotPos: bool,
    snapRelative: bool,
    snapValue: float,
    tweakMode: bool,
    useCenterPivot: bool,
    useManipPivot: bool,
    useObjectPivot: bool,
    manipVisible: bool,
    xformConstraint: str,
    constrainAlongNormal: bool,
) -> Any:
    ...


def manipRotateLimitsCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def manipScaleContext(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    alignAlong: Tuple[float, float, float],
    activeHandle: int,
    bakePivotOri: bool,
    currentActiveHandle: int,
    editPivotMode: bool,
    editPivotPosition: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    lastMode: int,
    mode: int,
    orientAxes: Tuple[float, float, float],
    orientObject: str,
    orientTowards: Tuple[float, float, float],
    position: bool,
    preserveChildPosition: bool,
    pinPivot: bool,
    preventNegativeScale: bool,
    postDragCommand: Tuple[Callable, str],
    pivotOriHandle: bool,
    preCommand: Callable,
    preDragCommand: Tuple[Callable, str],
    postCommand: Callable,
    preserveUV: bool,
    reflectionAbout: int,
    reflectionAxis: int,
    reflection: bool,
    reflectionTolerance: float,
    snap: bool,
    scale: Tuple[float, float, float],
    snapPivotOri: bool,
    snapPivotPos: bool,
    snapRelative: bool,
    snapValue: float,
    tweakMode: bool,
    useManipPivot: bool,
    useObjectPivot: bool,
    manipVisible: bool,
    xformConstraint: str,
    constrainAlongNormal: bool,
) -> Any:
    ...


def manipScaleLimitsCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def marker(
    *args: List[str],
    edit: bool,
    query: bool,
    attach: bool,
    detach: bool,
    frontTwist: float,
    orientationMarker: bool,
    positionMarker: bool,
    sideTwist: float,
    time: int,
    valueU: float,
    upTwist: float,
) -> Any:
    ...


def matchTransform(
    *objects: List[str],
    scaleBox: bool,
    pivots: bool,
    position: bool,
    positionX: bool,
    positionY: bool,
    positionZ: bool,
    rotation: bool,
    rotatePivot: bool,
    rotationX: bool,
    rotationY: bool,
    rotationZ: bool,
    scale: bool,
    scalePivot: bool,
    scaleX: bool,
    scaleY: bool,
    scaleZ: bool,
) -> None:
    """matchTransform is undoable, *NOT queryable*, and *NOT editable*.

    This command modifies the source object's transform to match the target object's transform.
    If no flags are specified then the command will match position, rotation and scaling.

    Args:
        - objects: a series of objects. The first objects will be matched to the last one.
        - pivots: Match the source object(s) scale/rotate pivot positions to the target transform's pivot.
        - position: Match the source object(s) position to the target object.
        - positionX: Match the source object(s) X position to the target object.
        - positionY: Match the source object(s) Y position to the target object.
        - positionZ: Match the source object(s) Z position to the target object.
        - rotatePivot: Match the source object(s) rotate pivot position to the target transform's pivot.
        - rotation: Match the source object(s) rotation to the target object.
        - rotationX: Match the source object(s) X rotation to the target object.
        - rotationY: Match the source object(s) Y rotation to the target object.
        - rotationZ: Match the source object(s) Z rotation to the target object.
        - scale: Match the source object(s) scale to the target transform.
        - scaleBox: Use the source/target object's child bounding box size when matching scaling.
        - scalePivot: Match the source object(s) scale pivot position to the target transform's pivot.
        - scaleX: Match the source object(s) X scale to the target object.
        - scaleY: Match the source object(s) Y scale to the target object.
        - scaleZ: Match the source object(s) Z scale to the target object.

    Examples:
        >>> from maya import cmds
        >>> # create a cone and randomly transform it
        >>> cmds.polyCone(n='cone1')
        >>> cmds.scale(0.2, 2.0, 0.2);
        >>> cmds.rotate(20, 45, 70)
        >>> cmds.move(-2, 0, 2)
        >>> # create a cylinder
        >>> cmds.polyCylinder(n='cylinder1')
        >>> # modify the cylinder's transform to match the cone
        >>> cmds.matchTransform('cylinder1','cone1')
    """


def mateCtx(*args, **kwargs) -> Any:
    ...


def matrix() -> Any:
    ...


def matrixUtil(
    *args: Tuple[
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
    ],
    edit: bool,
    query: bool,
    inverse: bool,
    quaternion: Tuple[float, float, float, float],
    rotation: Tuple[float, float, float],
    relative: bool,
    scale: Tuple[float, float, float],
    shear: Tuple[float, float, float],
    translation: Tuple[float, float, float],
    transpose: bool,
) -> Any:
    ...


def mayaDpiSetting(
    query: bool, mode: int, realScaleValue: bool, systemDpi: bool, scaleValue: float
) -> Any:
    ...


def mayaDpiSettingAction(*args, **kwargs) -> Any:
    ...


def mayaHasRenderSetup(
    edit: bool, query: bool, enableCurrentSession: bool, enableDuringTests: bool
) -> Any:
    ...


def mayaPreviewRenderIntoNewWindow() -> Any:
    ...


def melInfo() -> Any:
    ...


def melOptions(query: bool, duplicateVariableWarnings: bool) -> Any:
    ...


def memory(
    asFloat: bool,
    adjustedVirtualMemory: bool,
    debug: bool,
    freeMemory: bool,
    gigaByte: bool,
    heapMemory: bool,
    kiloByte: bool,
    megaByte: bool,
    pageFaults: bool,
    physicalMemory: bool,
    pageReclaims: bool,
    processResidentMemory: bool,
    processVirtualMemory: bool,
    summary: bool,
    swaps: bool,
    swapFree: bool,
    swapLogical: bool,
    swapMax: bool,
    swapPhysical: bool,
    swapReserved: bool,
    swapVirtual: bool,
) -> Any:
    ...


def menu(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    allowOptionBoxes: bool,
    deleteAllItems: bool,
    defineTemplate: str,
    docTag: str,
    enable: bool,
    exists: bool,
    familyImage: str,
    helpMenu: bool,
    itemArray: bool,
    label: str,
    mnemonic: str,
    numberOfItems: bool,
    parent: str,
    postMenuCommand: Callable,
    postMenuCommandOnce: bool,
    scrollable: bool,
    tearOff: bool,
    useTemplate: str,
    version: str,
    visible: bool,
) -> Any:
    ...


def menuBarLayout(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    childArray: bool,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    menuArray: bool,
    menuBarVisible: bool,
    menuIndex: Tuple[str, int],
    noBackground: bool,
    numberOfChildren: bool,
    numberOfMenus: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def menuEditor(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    command: Tuple[str, str, int],
    checkBoxPresent: Tuple[bool, str, int],
    checkBoxState: Tuple[bool, str, int],
    cellHeight: int,
    cellWidth: int,
    cellWidthHeight: Tuple[int, int],
    delete: Tuple[str, int],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    image: Tuple[str, str, int],
    iconMenuCallback: str,
    isObscured: bool,
    label: Tuple[str, str, int],
    manage: bool,
    menuItemTypes: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    optionBoxCommand: Tuple[str, str, int],
    optionBoxPresent: Tuple[bool, str, int],
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    radioButtonPresent: Tuple[bool, str, int],
    radioButtonState: Tuple[bool, str, int],
    statusBarMessage: str,
    subMenuEditorsOpen: bool,
    subMenuEditorWindow: str,
    subMenuAt: Tuple[str, int],
    subMenuOf: Tuple[str, str, int],
    separator: Tuple[str, int],
    style: str,
    topLevelMenu: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def menuItem(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    altModifier: bool,
    annotation: str,
    allowOptionBoxes: bool,
    boldFont: bool,
    command: Callable,
    checkBox: bool,
    collection: str,
    commandModifier: bool,
    ctrlModifier: bool,
    divider: bool,
    data: int,
    dragDoubleClickCommand: Callable,
    dividerLabel: str,
    dragMenuCommand: Callable,
    defineTemplate: str,
    docTag: str,
    echoCommand: bool,
    enableCommandRepeat: bool,
    enable: bool,
    exists: bool,
    familyImage: str,
    image: str,
    insertAfter: str,
    isCheckBox: bool,
    isOptionBox: bool,
    imageOverlayLabel: str,
    isRadioButton: bool,
    italicized: bool,
    keyEquivalent: str,
    label: str,
    longDivider: bool,
    mnemonic: str,
    optionBox: bool,
    optionBoxIcon: str,
    optionModifier: bool,
    parent: str,
    postMenuCommand: Callable,
    postMenuCommandOnce: bool,
    radioButton: bool,
    radialPosition: str,
    runTimeCommand: str,
    shiftModifier: bool,
    subMenu: bool,
    sourceType: str,
    tearOff: bool,
    useTemplate: str,
    version: str,
    visible: bool,
) -> Any:
    ...


def menuSet(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    addMenu: str,
    allMenuSets: bool,
    currentMenuSet: str,
    exists: str,
    hotBoxVisible: bool,
    insertMenu: Tuple[str, int],
    label: str,
    menuArray: Incomplete,
    moveMenu: Tuple[str, int],
    moveMenuSet: Tuple[str, int],
    numberOfMenus: bool,
    numberOfMenuSets: bool,
    permanent: bool,
    removeMenu: str,
    removeMenuSet: str,
) -> Any:
    ...


def menuSetPref(
    edit: bool,
    query: bool,
    exists: bool,
    force: bool,
    loadAll: bool,
    removeAll: bool,
    saveAll: bool,
    saveBackup: bool,
    version: bool,
) -> Any:
    ...


def meshIntersectTest(*args, **kwargs) -> Any:
    ...


def messageLine(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def mimicManipulation(manipulations: str, prevalidation: bool, refresh: bool) -> Any:
    ...


def mimicMnipulation(*args, **kwargs) -> Any:
    ...


def minimizeApp() -> Any:
    ...


def mirrorJoint(
    arg0: Incomplete,
    /,
    mirrorBehavior: bool,
    mirrorXY: bool,
    mirrorXZ: bool,
    mirrorYZ: bool,
    searchReplace: Tuple[str, str],
) -> Any:
    ...


def mirrorShape(*args: Tuple[str, str], mirrorAxis: str) -> Any:
    ...


def modelCurrentTimeCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
    percent: float,
) -> Any:
    ...


def modelEditor(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    activeCustomEnvironment: str,
    activeCustomGeometry: str,
    activeCustomLighSet: str,
    activeCustomRenderer: str,
    activeComponentsXray: bool,
    allObjects: bool,
    activeOnly: bool,
    addObjects: str,
    activeCustomOverrideGeometry: str,
    addSelected: bool,
    activeShadingGraph: str,
    addSelectedObjects: bool,
    activeView: bool,
    backfaceCulling: bool,
    bufferMode: str,
    bumpResolution: Tuple[int, int],
    cameras: bool,
    camera: str,
    clipGhosts: bool,
    colorMap: bool,
    cmEnabled: bool,
    cameraName: str,
    cullingOverride: str,
    capture: str,
    colorResolution: Tuple[int, int],
    cameraSetup: bool,
    captureSequenceNumber: int,
    cameraSet: str,
    control: bool,
    controllers: bool,
    controlVertices: bool,
    default: bool,
    displayAppearance: str,
    dynamicConstraints: bool,
    deformers: bool,
    dimensions: bool,
    interactiveDisableShadows: bool,
    displayLights: str,
    depthOfFieldPreview: bool,
    defineTemplate: str,
    docTag: str,
    displayTextures: bool,
    dynamics: bool,
    editorChanged: Callable,
    exists: bool,
    exposure: float,
    filter: str,
    fogColor: Tuple[float, float, float, float],
    fogDensity: float,
    fogEnd: float,
    fogging: bool,
    fluids: bool,
    forceMainConnection: str,
    fogMode: str,
    follicles: bool,
    filteredObjectList: bool,
    fogSource: str,
    fogStart: float,
    gamma: float,
    greasePencils: bool,
    grid: bool,
    height: int,
    handles: bool,
    highlightConnection: str,
    holdOuts: bool,
    hairSystems: bool,
    hulls: bool,
    headsUpDisplay: bool,
    interactive: bool,
    interactiveBackFaceCull: bool,
    isFiltered: bool,
    ikHandles: bool,
    imagePlane: bool,
    useRGBImagePlane: bool,
    ignorePanZoom: bool,
    joints: bool,
    jointXray: bool,
    locators: bool,
    lockMainConnection: bool,
    lowQualityLighting: bool,
    lights: bool,
    lineWidth: float,
    manipulators: bool,
    maxConstantTransparency: float,
    maximumNumHardwareLights: bool,
    mainListConnection: str,
    modelPanel: str,
    motionTrails: bool,
    nurbsCurves: bool,
    nCloths: bool,
    nParticles: bool,
    nRigids: bool,
    nurbsSurfaces: bool,
    noUndo: bool,
    objectFilter: str,
    objectFilterUI: str,
    occlusionCulling: bool,
    objectFilterList: bool,
    objectFilterShowInHUD: bool,
    objectFilterListUI: bool,
    parent: str,
    particleInstancers: bool,
    planes: bool,
    polymeshes: bool,
    panel: str,
    pluginObjects: List[Tuple[str, bool]],
    pluginShapes: bool,
    pivots: bool,
    queryPluginObjects: str,
    resetCustomCamera: bool,
    rendererDeviceName: bool,
    rendererList: bool,
    rendererListUI: bool,
    rendererName: str,
    rendererOverrideList: bool,
    rendererOverrideName: str,
    rendererOverrideListUI: bool,
    removeSelected: bool,
    stereoDrawMode: bool,
    subdivSurfaces: bool,
    shadows: bool,
    selectionHiliteDisplay: bool,
    selectionConnection: str,
    shadingModel: int,
    smallObjectCulling: bool,
    smallObjectThreshold: float,
    sceneRenderFilter: str,
    setSelected: bool,
    sortTransparent: bool,
    strokes: bool,
    stateString: bool,
    smoothWireframe: bool,
    textureAnisotropic: bool,
    transparencyAlgorithm: str,
    textureCompression: bool,
    textureDisplay: str,
    textureEnvironmentMap: bool,
    toggleExposure: bool,
    toggleGamma: bool,
    textureHilight: bool,
    transpInShadows: bool,
    textureMaxSize: int,
    textureMemoryUsed: bool,
    textureSampling: int,
    twoSidedLighting: bool,
    textures: bool,
    useBaseRenderer: bool,
    useColorIndex: bool,
    updateColorMode: bool,
    useDefaultMaterial: bool,
    useInteractiveMode: bool,
    unlockMainConnection: bool,
    userNode: str,
    unParent: bool,
    updateMainConnection: bool,
    useReducedRenderer: bool,
    useTemplate: str,
    viewObjects: bool,
    viewSelected: bool,
    viewType: bool,
    viewTransformName: str,
    width: int,
    wireframeBackingStore: bool,
    wireframeOnShaded: bool,
    xray: bool,
) -> Any:
    ...


def modelPanel(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    barLayout: bool,
    camera: str,
    copy: str,
    createString: bool,
    control: bool,
    defineTemplate: str,
    docTag: str,
    editString: bool,
    exists: bool,
    init: bool,
    isUnique: bool,
    label: str,
    menuBarVisible: bool,
    modelEditor: bool,
    menuBarRepeatLast: bool,
    needsInit: bool,
    parent: str,
    popupMenuProcedure: Callable,
    replacePanel: str,
    tearOff: bool,
    tearOffCopy: str,
    tearOffRestore: bool,
    unParent: bool,
    useTemplate: str,
) -> Any:
    ...


def modelingToolkitSuperCtx(*args, **kwargs) -> Any:
    ...


def moduleInfo(
    definition: bool, listModules: bool, moduleName: str, path: bool, version: bool
) -> Any:
    ...


def mouldMesh(*args, **kwargs) -> Any:
    ...


def mouldSrf() -> Any:
    ...


def mouldSubdiv(*args, **kwargs) -> Any:
    ...


def mouse(
    enableScrollWheel: bool,
    mouseButtonTrackingStatus: bool,
    mouseButtonTracking: int,
    scrollWheelStatus: bool,
) -> Any:
    ...


def movIn(*args: List[str], file: str, startTime: int) -> Any:
    ...


def movOut(
    *args: List[str], comment: bool, file: str, precision: int, time: Incomplete
) -> Any:
    ...


def move(
    *args: List[Incomplete],
    absolute: bool,
    componentOffset: bool,
    componentSpace: bool,
    deletePriorHistory: bool,
    localSpace: bool,
    orientJoint: str,
    objectSpace: bool,
    parameter: bool,
    preserveChildPosition: bool,
    preserveGeometryPosition: bool,
    preserveUV: bool,
    relative: bool,
    reflectionAboutBBox: bool,
    reflectionAboutOrigin: bool,
    reflectionAboutX: bool,
    reflectionAboutY: bool,
    reflectionAboutZ: bool,
    reflection: bool,
    reflectionTolerance: float,
    rotatePivotRelative: bool,
    secondaryAxisOrient: str,
    symNegative: bool,
    scalePivotRelative: bool,
    ufeRotatePivot: bool,
    ufeScalePivot: bool,
    worldSpaceDistance: bool,
    worldSpace: bool,
    moveX: bool,
    xformConstraint: str,
    constrainAlongNormal: bool,
    moveXY: bool,
    moveXYZ: bool,
    moveXZ: bool,
    moveY: bool,
    moveYZ: bool,
    moveZ: bool,
) -> Any:
    ...


def moveKeyCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    moveFunction: str,
    name: str,
    option: str,
) -> Any:
    ...


def moveVertexAlongDirection(
    *args: List[str],
    direction: List[Tuple[float, float, float]],
    magnitude: List[float],
    normalDirection: List[float],
    uDirection: List[float],
    uvNormalDirection: List[Tuple[float, float, float]],
    vDirection: List[float],
) -> Any:
    ...


def movieCompressor(*args, **kwargs) -> Any:
    ...


def movieInfo(
    arg0: str,
    /,
    counter: bool,
    dropFrame: bool,
    frameCount: bool,
    frameDuration: bool,
    height: bool,
    movieTexture: bool,
    numFrames: bool,
    negTimesOK: bool,
    quickTime: bool,
    timeCode: bool,
    twentyFourHourMax: bool,
    timeScale: bool,
    timeCodeTrack: bool,
    width: bool,
) -> Any:
    ...


def mpBirailCtx(*args, **kwargs) -> Any:
    ...


def mrMapVisualizer() -> Any:
    ...


def mrShaderManager() -> Any:
    ...


def multiProfileBirailSurface(
    *args: List[Incomplete],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    polygon: int,
    transformMode: int,
    tangentContinuityProfile1: bool,
    tangentContinuityProfile2: bool,
) -> Any:
    ...


def multiTouch(*args, **kwargs) -> Any:
    ...


def mute(*args: List[str], query: bool, disable: bool, force: bool) -> Any:
    ...


def myTestCmd(*args, **kwargs) -> Any:
    ...


def nBase(
    *args: List[str],
    edit: bool,
    query: bool,
    clearCachedTextureMap: str,
    clearStart: bool,
    stuffStart: bool,
    textureToVertex: str,
) -> Any:
    ...


def nClothAppend() -> Any:
    ...


def nClothAppendOpt() -> Any:
    ...


def nClothCache() -> Any:
    ...


def nClothCacheOpt() -> Any:
    ...


def nClothCreate() -> Any:
    ...


def nClothCreateOptions() -> Any:
    ...


def nClothDeleteCacheFrames() -> Any:
    ...


def nClothDeleteCacheFramesOpt() -> Any:
    ...


def nClothDeleteCacheOpt() -> Any:
    ...


def nClothDeleteHistory() -> Any:
    ...


def nClothDeleteHistoryOpt() -> Any:
    ...


def nClothDisplayCurrentMesh() -> Any:
    ...


def nClothDisplayInputMesh() -> Any:
    ...


def nClothLocalToWorld() -> Any:
    ...


def nClothMakeCollide() -> Any:
    ...


def nClothMakeCollideOptions() -> Any:
    ...


def nClothMergeCache() -> Any:
    ...


def nClothMergeCacheOpt() -> Any:
    ...


def nClothRemove() -> Any:
    ...


def nClothReplaceCache() -> Any:
    ...


def nClothReplaceCacheOpt() -> Any:
    ...


def nClothReplaceFrames() -> Any:
    ...


def nClothReplaceFramesOpt() -> Any:
    ...


def nClothRestToInput() -> Any:
    ...


def nClothRestToInputStart() -> Any:
    ...


def nClothRestToMesh() -> Any:
    ...


def nClothWorldToLocal() -> Any:
    ...


def nConstraintAddMembers() -> Any:
    ...


def nConstraintAttractToMatch() -> Any:
    ...


def nConstraintAttractToMatchOptions() -> Any:
    ...


def nConstraintCollisionExclusion() -> Any:
    ...


def nConstraintCollisionExclusionOptions() -> Any:
    ...


def nConstraintComponent() -> Any:
    ...


def nConstraintComponentOptions() -> Any:
    ...


def nConstraintComponentToComponent() -> Any:
    ...


def nConstraintComponentToComponentOptions() -> Any:
    ...


def nConstraintConstraintMembershipTool() -> Any:
    ...


def nConstraintDisableCollision() -> Any:
    ...


def nConstraintDisableCollisionOptions() -> Any:
    ...


def nConstraintForceField() -> Any:
    ...


def nConstraintForceFieldOptions() -> Any:
    ...


def nConstraintPointToSurface() -> Any:
    ...


def nConstraintPointToSurfaceOptions() -> Any:
    ...


def nConstraintRemoveMembers() -> Any:
    ...


def nConstraintReplaceMembers() -> Any:
    ...


def nConstraintSelectMembers() -> Any:
    ...


def nConstraintSlideOnSurface() -> Any:
    ...


def nConstraintSlideOnSurfaceOptions() -> Any:
    ...


def nConstraintTearableSurface() -> Any:
    ...


def nConstraintTearableSurfaceOptions() -> Any:
    ...


def nConstraintTransform() -> Any:
    ...


def nConstraintTransformOptions() -> Any:
    ...


def nConstraintWeldBorders() -> Any:
    ...


def nConstraintWeldBordersOptions() -> Any:
    ...


def nParticle(
    *args: List[str],
    edit: bool,
    query: bool,
    attribute: str,
    conserve: float,
    cache: bool,
    count: bool,
    dynamicAttrList: bool,
    deleteCache: bool,
    floatValue: float,
    gridSpacing: List[float],
    inherit: float,
    particleId: int,
    jitterBasePoint: List[Tuple[float, float, float]],
    jitterRadius: List[float],
    lowerLeft: List[Tuple[float, float, float]],
    name: str,
    numJitters: List[int],
    order: int,
    position: List[Tuple[float, float, float]],
    perParticleDouble: bool,
    perParticleVector: bool,
    shapeName: str,
    upperRight: List[Tuple[float, float, float]],
    vectorValue: Tuple[float, float, float],
) -> Any:
    ...


def nSoft(
    *args: List[str],
    query: bool,
    convert: bool,
    duplicate: bool,
    duplicateHistory: bool,
    goal: float,
    hideOriginal: bool,
    name: str,
) -> Any:
    ...


def nameCommand(
    arg0: str,
    /,
    annotation: str,
    command: Callable,
    default: bool,
    data1: str,
    data2: str,
    data3: str,
    sourceType: str,
) -> Any:
    ...


def nameField(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    dragCallback: Callable,
    drawInactiveFrame: bool,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    nameChangeCommand: Callable,
    numberOfPopupMenus: bool,
    object: str,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    receiveFocusCommand: Callable,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def namespace(
    query: bool,
    addNamespace: str,
    absoluteName: bool,
    collapseAncestors: str,
    deleteNamespaceContent: bool,
    exists: str,
    force: bool,
    isRootNamespace: str,
    mergeNamespaceWithOther: str,
    mergeNamespaceWithParent: bool,
    mergeNamespaceWithRoot: bool,
    moveNamespace: Tuple[str, str],
    parent: str,
    recurse: bool,
    relativeNames: bool,
    rename: Tuple[str, str],
    removeNamespace: str,
    setNamespace: str,
    validateName: str,
) -> Any:
    ...


def namespaceInfo(
    arg0: str,
    /,
    absoluteName: bool,
    baseName: bool,
    currentNamespace: bool,
    dagPath: bool,
    fullName: bool,
    internal: bool,
    isRootNamespace: bool,
    listOnlyDependencyNodes: bool,
    listOnlyNamespaces: bool,
    listNamespace: bool,
    parent: bool,
    recurse: bool,
    shortName: bool,
) -> Any:
    ...


def newton(
    *args: List[str],
    edit: bool,
    query: bool,
    attenuation: float,
    magnitude: float,
    minDistance: float,
    maxDistance: float,
    name: str,
    position: List[Tuple[float, float, float]],
    perVertex: bool,
    torusSectionRadius: float,
    volumeExclusion: bool,
    volumeOffset: Tuple[float, float, float],
    volumeShape: str,
    volumeSweep: float,
) -> Any:
    ...


def nodeCast(
    *args: Tuple[str, str],
    copyDynamicAttrs: bool,
    disableAPICallbacks: bool,
    disableScriptJobCallbacks: bool,
    disconnectUnmatchedAttrs: bool,
    force: bool,
    swapNames: bool,
    swapValues: bool,
) -> Any:
    ...


def nodeGrapher(*args, **kwargs) -> Any:
    ...


def nodeIconButton(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    align: str,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    command: Callable,
    dragCallback: Callable,
    disabledImage: str,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    font: str,
    fullPathName: bool,
    flipX: float,
    flipY: float,
    height: int,
    highlightColor: Tuple[float, float, float],
    image: str,
    image1: str,
    image2: str,
    image3: str,
    isObscured: bool,
    imageOverlayLabel: str,
    label: str,
    labelOffset: int,
    manage: bool,
    marginHeight: int,
    marginWidth: int,
    noBackground: bool,
    numberOfPopupMenus: bool,
    overlayLabelBackColor: Tuple[float, float, float, float],
    overlayLabelColor: Tuple[float, float, float],
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rotation: float,
    statusBarMessage: str,
    style: str,
    useAlpha: float,
    useTemplate: str,
    visibleChangeCommand: Callable,
    version: str,
    visible: bool,
    width: int,
) -> Any:
    ...


def nodeOutliner(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    addObject: str,
    attrAlphaOrder: str,
    addCommand: Callable,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    connectivity: str,
    currentSelection: bool,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    lastClickedNode: bool,
    lastMenuChoice: str,
    longNames: bool,
    manage: bool,
    menuCommand: Callable,
    menuMultiOption: bool,
    multiSelect: bool,
    noBackground: bool,
    noConnectivity: bool,
    nodesDisplayed: bool,
    niceNames: bool,
    numberOfPopupMenus: bool,
    parent: str,
    pressHighlightsUnconnected: bool,
    popupMenuArray: bool,
    preventOverride: bool,
    redraw: bool,
    remove: List[str],
    removeAll: bool,
    replace: str,
    redrawRow: bool,
    statusBarMessage: str,
    selectCommand: Callable,
    showConnectedOnly: bool,
    showHidden: bool,
    showInputs: bool,
    showNonConnectable: bool,
    showNonKeyable: bool,
    showOutputs: bool,
    showPublished: bool,
    showReadOnly: bool,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def nodePreset(
    attributes: str,
    custom: str,
    delete: Tuple[str, str],
    exists: Tuple[str, str],
    isValidName: str,
    load: Tuple[str, str],
    list: str,
    save: Tuple[str, str],
) -> Any:
    ...


def nodeTreeLister(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    addItem: List[Tuple[str, str, Callable]],
    addFavorite: List[str],
    annotation: str,
    addVnnItem: List[Tuple[str, str, str, str]],
    backgroundColor: Tuple[float, float, float],
    clearContents: bool,
    collapsePath: List[str],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    executeItem: str,
    enableKeyboardFocus: bool,
    enable: bool,
    expandPath: List[str],
    expandToDepth: int,
    exists: bool,
    favoritesCallback: Callable,
    favoritesList: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    itemScript: str,
    manage: bool,
    noBackground: bool,
    nodeLibrary: str,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    refreshCommand: Callable,
    removeItem: List[str],
    removeFavorite: List[str],
    resultsPathUnderCursor: bool,
    statusBarMessage: str,
    selectPath: List[str],
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    vnnString: bool,
    width: int,
) -> Any:
    ...


def nodeType(
    arg0: str,
    /,
    apiType: bool,
    derived: bool,
    inherited: bool,
    isTypeName: bool,
    ufeRuntimeName: bool,
) -> Any:
    ...


def nonLinear(
    *args: List[str],
    edit: bool,
    query: bool,
    after: bool,
    autoParent: bool,
    afterReference: bool,
    before: bool,
    components: bool,
    selectedComponents: bool,
    commonParent: bool,
    defaultScale: bool,
    deformerTools: bool,
    exclusive: str,
    frontOfChain: bool,
    geometry: List[str],
    geometryIndices: bool,
    includeHiddenSelections: bool,
    ignoreSelected: bool,
    name: str,
    parallel: bool,
    prune: bool,
    remove: List[bool],
    split: bool,
    type: str,
    useComponentTags: bool,
) -> Any:
    ...


def nop(*args, **kwargs) -> Any:
    ...


def normalConstraint(
    *args: List[str],
    edit: bool,
    query: bool,
    aimVector: Tuple[float, float, float],
    name: str,
    remove: bool,
    targetList: bool,
    upVector: Tuple[float, float, float],
    weight: float,
    weightAliasList: bool,
    worldUpVector: Tuple[float, float, float],
    worldUpObject: str,
    worldUpType: str,
) -> Any:
    ...


def notifyDecorator() -> Any:
    ...


def notifyPostRedo() -> Any:
    ...


def notifyPostUndo() -> Any:
    ...


def nucleusDisplayDynamicConstraintNodes() -> Any:
    ...


def nucleusDisplayMaterialNodes() -> Any:
    ...


def nucleusDisplayNComponentNodes() -> Any:
    ...


def nucleusDisplayOtherNodes() -> Any:
    ...


def nucleusDisplayTextureNodes() -> Any:
    ...


def nucleusDisplayTransformNodes() -> Any:
    ...


def nucleusGetEffectsAsset() -> Any:
    ...


def nucleusGetnClothExample() -> Any:
    ...


def nucleusGetnParticleExample() -> Any:
    ...


def nurbsBoolean(
    *args: List[Incomplete],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    nsrfsInFirstShell: int,
    object: bool,
    operation: int,
    smartConnection: bool,
    tolerance: float,
) -> Any:
    ...


def nurbsCopyUVSet(*args: List[str], edit: bool, query: bool) -> Any:
    ...


def nurbsCube(
    *args: List[str],
    edit: bool,
    query: bool,
    axis: Tuple[float, float, float],
    caching: bool,
    constructionHistory: bool,
    degree: int,
    frozen: bool,
    heightRatio: float,
    lengthRatio: float,
    name: str,
    nodeState: int,
    object: bool,
    pivot: Tuple[float, float, float],
    polygon: int,
    patchesU: int,
    patchesV: int,
    width: float,
) -> Any:
    ...


def nurbsCurveRebuildPref(
    query: bool,
    degree: int,
    endKnots: int,
    fitRebuild: int,
    keepControlPoints: bool,
    keepEndPoints: bool,
    keepRange: int,
    keepTangents: bool,
    rebuildType: int,
    spans: int,
    smartSurfaceCurve: bool,
    tolerance: float,
) -> Any:
    ...


def nurbsCurveToBezier() -> Any:
    ...


def nurbsEditUV(
    *args: List[str],
    query: bool,
    angle: float,
    pivotU: float,
    pivotV: float,
    relative: bool,
    rotation: bool,
    rotateRatio: float,
    scale: bool,
    scaleU: float,
    scaleV: float,
    uValue: float,
    vValue: float,
) -> Any:
    ...


def nurbsPlane(
    *args: List[str],
    edit: bool,
    query: bool,
    axis: Tuple[float, float, float],
    caching: bool,
    constructionHistory: bool,
    degree: int,
    frozen: bool,
    lengthRatio: float,
    name: str,
    nodeState: int,
    object: bool,
    pivot: Tuple[float, float, float],
    polygon: int,
    patchesU: int,
    patchesV: int,
    width: float,
) -> Any:
    ...


def nurbsSelect(
    *args: List[str],
    bottomBorder: bool,
    borderSelection: bool,
    growSelection: int,
    leftBorder: bool,
    rightBorder: bool,
    shrinkSelection: int,
    topBorder: bool,
) -> Any:
    ...


def nurbsSquare(
    *args: List[str],
    edit: bool,
    query: bool,
    center: Tuple[float, float, float],
    caching: bool,
    constructionHistory: bool,
    centerX: float,
    centerY: float,
    centerZ: float,
    degree: int,
    frozen: bool,
    name: str,
    nodeState: int,
    normal: Tuple[float, float, float],
    normalX: float,
    normalY: float,
    normalZ: float,
    object: bool,
    sideLength1: float,
    sideLength2: float,
    spansPerSide: int,
) -> Any:
    ...


def nurbsToPoly(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    chordHeightRatio: float,
    chordHeight: float,
    curvatureTolerance: int,
    delta: float,
    edgeSwap: bool,
    smoothEdgeRatio: float,
    explicitTessellationAttributes: bool,
    format: int,
    fractionalTolerance: float,
    frozen: bool,
    minEdgeLength: float,
    matchNormalDir: bool,
    matchRenderTessellation: bool,
    name: str,
    nodeState: int,
    normalizeTrimmedUVRange: bool,
    uDivisionsFactor: float,
    vDivisionsFactor: float,
    object: bool,
    polygonCount: int,
    polygonType: int,
    useChordHeight: bool,
    useChordHeightRatio: bool,
    smoothEdge: bool,
    uNumber: int,
    useSurfaceShader: bool,
    uType: int,
    vNumber: int,
    vType: int,
) -> Any:
    ...


def nurbsToPolygonsPref(
    query: bool,
    chordHeightRatio: float,
    chordHeight: float,
    delta3D: float,
    edgeSwap: bool,
    format: int,
    fraction: float,
    merge: int,
    minEdgeLen: float,
    matchRenderTessellation: int,
    mergeTolerance: float,
    polyCount: int,
    polyType: int,
    useChordHeight: bool,
    useChordHeightRatio: bool,
    uNumber: int,
    uType: int,
    vNumber: int,
    vType: int,
) -> Any:
    ...


def nurbsToSubdiv(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    addUnderTransform: bool,
    caching: bool,
    constructionHistory: bool,
    collapsePoles: bool,
    frozen: bool,
    matchPeriodic: bool,
    maxPolyCount: int,
    name: str,
    nodeState: int,
    object: bool,
    reverseNormal: bool,
) -> Any:
    ...


def nurbsToSubdivPref(
    query: bool,
    bridge: int,
    collapsePoles: bool,
    capType: int,
    matchPeriodic: bool,
    maxPolyCount: int,
    offset: float,
    reverseNormal: bool,
    solidType: int,
    trans00: float,
    trans01: float,
    trans02: float,
    trans10: float,
    trans11: float,
    trans12: float,
    trans20: float,
    trans21: float,
    trans22: float,
    trans30: float,
    trans31: float,
    trans32: float,
) -> Any:
    ...


def nurbsUVSet(
    *args: List[str], edit: bool, query: bool, create: bool, useExplicit: bool
) -> Any:
    ...


def objExists() -> Any:
    ...


def objectCenter(arg0: Incomplete, /, gl: bool, local: bool) -> Any:
    ...


def objectType(
    arg0: str,
    /,
    convertTag: str,
    isType: str,
    isAType: str,
    tagFromType: str,
    typeFromTag: int,
    typeTag: bool,
) -> Any:
    ...


def objectTypeUI(arg0: str, /, isType: str, listAll: bool, superClasses: bool) -> Any:
    ...


def offsetCurve(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    connectBreaks: int,
    caching: bool,
    constructionHistory: bool,
    cutLoop: bool,
    cutRadius: float,
    distance: float,
    frozen: bool,
    name: str,
    nodeState: int,
    normal: Tuple[float, float, float],
    object: bool,
    range: bool,
    reparameterize: bool,
    subdivisionDensity: int,
    stitch: bool,
    tolerance: float,
    useGivenNormal: bool,
) -> Any:
    ...


def offsetCurveOnSurface(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    connectBreaks: int,
    caching: bool,
    constructionHistory: bool,
    cutLoop: bool,
    checkPoints: int,
    distance: float,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    range: bool,
    subdivisionDensity: int,
    stitch: bool,
    tolerance: float,
) -> Any:
    ...


def offsetSurface(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    distance: float,
    frozen: bool,
    method: int,
    name: str,
    nodeState: int,
    object: bool,
) -> Any:
    ...


def ogs(
    query: bool,
    deviceInformation: bool,
    disposeReleasableTextures: bool,
    dumpTexture: str,
    fragmentEditor: str,
    gpuMemoryTotal: int,
    gpuMemoryUsed: bool,
    enableHardwareInstancing: bool,
    isWinRemoteSession: bool,
    isLegacyViewportEnabled: bool,
    pause: bool,
    reset: bool,
    rebakeTextures: bool,
    isRemoteGLSessionEnabled: bool,
    reloadTextures: bool,
    regenerateUVTilePreview: str,
    shaderSource: str,
    traceRenderPipeline: bool,
    toggleTexturePaging: bool,
    fragmentXML: str,
) -> Any:
    ...


def ogsRender(
    *args: List[str],
    edit: bool,
    query: bool,
    availableFloatingPointTargetFormat: bool,
    availableMultisampleType: bool,
    availableRenderOverrides: bool,
    camera: str,
    currentFrame: bool,
    activeRenderOverride: str,
    currentView: bool,
    enableFloatingPointRenderTarget: bool,
    enableMultisample: bool,
    frame: float,
    activeRenderTargetFormat: str,
    height: int,
    layer: str,
    activeMultisampleType: str,
    noRenderView: bool,
    width: int,
) -> Any:
    ...


def ogsdebug(count: int, debug: str, timing: str, verbose: bool) -> Any:
    ...


def openCLInfo(
    *args: List[str], query: bool, minVertexBuffer: bool, valid: bool
) -> Any:
    ...


def openGLExtension(
    *args: List[str], extension: str, renderer: bool, version: bool, vendor: bool
) -> Any:
    ...


def openMayaPref(
    edit: bool, query: bool, errlog: bool, lazyLoad: bool, oldPluginWarning: bool
) -> Any:
    ...


def optionMenu(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    alwaysCallChangeCommand: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    beforeShowPopup: Callable,
    changeCommand: Callable,
    deleteAllItems: bool,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    itemListLong: bool,
    itemListShort: bool,
    isObscured: bool,
    label: str,
    manage: bool,
    maxVisibleItems: int,
    noBackground: bool,
    numberOfItems: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    postMenuCommand: Callable,
    postMenuCommandOnce: bool,
    preventOverride: bool,
    statusBarMessage: str,
    select: int,
    useTemplate: str,
    value: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def optionMenuGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    changeCommand: Callable,
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    deleteAllItems: bool,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    extraLabel: str,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    itemListLong: bool,
    itemListShort: bool,
    isObscured: bool,
    label: str,
    manage: bool,
    noBackground: bool,
    numberOfItems: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    postMenuCommand: Callable,
    postMenuCommandOnce: bool,
    preventOverride: bool,
    rowAttach: List[Tuple[int, str, int]],
    statusBarMessage: str,
    select: int,
    useTemplate: str,
    value: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def optionVar(
    arraySize: str,
    clearArray: List[str],
    category: str,
    clearStash: List[str],
    default: bool,
    exists: str,
    floatArray: List[str],
    floatValue: List[Tuple[str, float]],
    floatValue2: List[Tuple[str, float, float]],
    floatValue3: List[Tuple[str, float, float, float]],
    floatValue4: List[Tuple[str, float, float, float, float]],
    floatValueAppend: List[Tuple[str, float]],
    intArray: List[str],
    init: bool,
    intValue: List[Tuple[str, int]],
    intValue2: List[Tuple[str, int, int]],
    intValue3: List[Tuple[str, int, int, int]],
    intValue4: List[Tuple[str, int, int, int, int]],
    intValueAppend: List[Tuple[str, int]],
    list: bool,
    listCategories: bool,
    listModified: bool,
    prefFile: str,
    query: str,
    removeFromArray: List[Tuple[str, int]],
    remove: List[str],
    stringArray: List[str],
    stash: List[str],
    stringValue: List[Tuple[str, str]],
    stringValueAppend: List[Tuple[str, str]],
    transient: bool,
    unstash: List[str],
    version: int,
) -> Any:
    ...


def orbit(
    arg0: str,
    /,
    horizontalAngle: float,
    pivotPoint: Tuple[float, float, float],
    rotationAngles: Tuple[float, float],
    verticalAngle: float,
) -> Any:
    ...


def orbitCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    alternateContext: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    localOrbit: bool,
    name: str,
    orbitScale: float,
    toolName: str,
) -> Any:
    ...


def orientConstraint(
    *args: List[str],
    edit: bool,
    query: bool,
    createCache: Tuple[float, float],
    deleteCache: bool,
    layer: str,
    maintainOffset: bool,
    name: str,
    offset: Tuple[float, float, float],
    remove: bool,
    skip: List[str],
    targetList: bool,
    weight: float,
    weightAliasList: bool,
) -> Any:
    ...


def outlinerEditor(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    showAssets: bool,
    attrAlphaOrder: str,
    showAnimCurvesOnly: bool,
    autoExpandLayers: bool,
    attrFilter: str,
    animLayerFilterOptions: str,
    allowMultiSelection: bool,
    autoSelectNewObjects: bool,
    showAttributes: bool,
    alwaysToggleSelect: bool,
    showAttrValues: bool,
    containersIgnoreFilters: bool,
    showCompounds: bool,
    showConnected: bool,
    control: bool,
    showDagOnly: bool,
    dropIsParent: bool,
    displayMode: str,
    doNotSelectNewObjects: bool,
    directSelect: bool,
    defineTemplate: str,
    docTag: str,
    expandAllItems: bool,
    editAttrName: bool,
    expandAllSelectedItems: bool,
    expandAttribute: bool,
    expandObjects: bool,
    exists: bool,
    filter: str,
    feedbackItemName: bool,
    feedbackRowNumber: bool,
    forceMainConnection: str,
    getCurrentSetOfItem: int,
    highlightActive: bool,
    ignoreDagHierarchy: bool,
    highlightConnection: str,
    highlightSecondary: bool,
    isChildSelected: str,
    ignoreHiddenAttribute: bool,
    ignoreOutlinerColor: bool,
    isSet: int,
    isSetMember: int,
    isUfeItem: int,
    showLeafs: bool,
    lockMainConnection: bool,
    longNames: bool,
    mainListConnection: str,
    mapMotionTrails: bool,
    masterOutliner: str,
    niceNames: bool,
    showNumericAttrsOnly: bool,
    organizeByClip: bool,
    object: str,
    organizeByLayer: bool,
    parent: str,
    pinPlug: str,
    panel: str,
    parentObject: bool,
    removeFromCurrentSet: int,
    renderFilterActive: bool,
    renderFilterIndex: int,
    refresh: bool,
    renderFilterVisible: bool,
    showReferenceMembers: bool,
    showReferenceNodes: bool,
    renameItem: int,
    renameSelectedItem: bool,
    showAssignedMaterials: bool,
    showAnimLayerWeight: bool,
    showSelected: bool,
    showContainerContents: bool,
    showContainedOnly: bool,
    selectCommand: Callable,
    setFilter: str,
    showShapes: bool,
    setsIgnoreFilters: bool,
    selectionConnection: str,
    showMuteInfo: bool,
    showNamespace: bool,
    sortOrder: str,
    sortCommand: Callable,
    selectionOrder: str,
    showParentContainers: bool,
    showPublishedAsConnected: bool,
    showPinIcons: bool,
    showSetMembers: bool,
    showTimeEditor: bool,
    stateString: bool,
    showUnitlessCurves: bool,
    showUpstreamCurves: bool,
    transmitFilters: bool,
    showTextureNodesOnly: bool,
    ufeFilter: Tuple[str, str],
    ufeFilterValue: bool,
    unlockMainConnection: bool,
    unpinPlug: str,
    unParent: bool,
    updateMainConnection: bool,
    useTemplate: str,
    showUVAttrsOnly: bool,
    autoExpandAnimatedShapes: bool,
    expandConnections: bool,
    autoExpand: bool,
) -> Any:
    ...


def outlinerPanel(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    copy: str,
    createString: bool,
    control: bool,
    divider: int,
    defineTemplate: str,
    docTag: str,
    editString: bool,
    exists: bool,
    init: bool,
    isUnique: bool,
    label: str,
    menuBarVisible: bool,
    menuBarRepeatLast: bool,
    needsInit: bool,
    outlinerEditor: bool,
    parent: str,
    popupMenuProcedure: Callable,
    replacePanel: str,
    tearOff: bool,
    tearOffCopy: str,
    tearOffRestore: bool,
    unParent: bool,
    useTemplate: str,
) -> Any:
    ...


def outputWindow(query: bool, show: bool) -> Any:
    ...


def overrideModifier(*args, **kwargs) -> Any:
    ...


def paint3d() -> Any:
    ...


def paintEffectsDisplay(query: bool, meshDrawEnable: bool) -> Any:
    ...


def pairBlend(
    *args: List[str],
    edit: bool,
    query: bool,
    attribute: List[str],
    input1: bool,
    input2: bool,
    node: str,
) -> Any:
    ...


def palettePort(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    actualTotal: int,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    colorEdited: Callable,
    colorEditable: bool,
    dragCallback: Callable,
    dimensions: Tuple[int, int],
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    editable: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    hsvValue: Tuple[int, int, float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    redraw: bool,
    rgbValue: Tuple[int, float, float, float],
    statusBarMessage: str,
    setCurCell: int,
    transparent: int,
    topDown: bool,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def panZoom(
    arg0: str,
    /,
    absolute: bool,
    downDistance: float,
    leftDistance: float,
    rightDistance: float,
    relative: bool,
    upDistance: float,
    zoomRatio: float,
) -> Any:
    ...


def panZoomCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    alternateContext: bool,
    buttonDown: bool,
    buttonUp: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
    panMode: bool,
    toolName: str,
    zoomMode: bool,
    zoomScale: float,
) -> Any:
    ...


def paneLayout(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    activeFrameThickness: int,
    annotation: str,
    activePane: str,
    activePaneIndex: int,
    backgroundColor: Tuple[float, float, float],
    childArray: bool,
    configuration: str,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfChildren: bool,
    numberOfPopupMenus: bool,
    numberOfVisiblePanes: bool,
    parent: str,
    pane1: bool,
    pane2: bool,
    pane3: bool,
    pane4: bool,
    popupMenuArray: bool,
    preventOverride: bool,
    paneSize: List[Tuple[int, int, int]],
    paneUnderPointer: bool,
    statusBarMessage: str,
    staticHeightPane: int,
    separatorMovedCommand: Callable,
    setPane: List[Tuple[str, int]],
    separatorThickness: int,
    staticWidthPane: int,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def panel(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    copy: str,
    createString: bool,
    control: bool,
    defineTemplate: str,
    docTag: str,
    editString: bool,
    exists: bool,
    init: bool,
    isUnique: bool,
    label: str,
    menuBarVisible: bool,
    menuBarRepeatLast: bool,
    needsInit: bool,
    parent: str,
    popupMenuProcedure: Callable,
    replacePanel: str,
    tearOff: bool,
    tearOffCopy: str,
    tearOffRestore: bool,
    unParent: bool,
    useTemplate: str,
) -> Any:
    ...


def panelConfiguration(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    addPanel: List[Tuple[bool, str, str, str, str]],
    configString: str,
    createStrings: bool,
    defaultImage: str,
    defineTemplate: str,
    editStrings: bool,
    exists: bool,
    image: str,
    isFixedState: bool,
    label: str,
    labelStrings: bool,
    numberOfPanels: bool,
    removeAllPanels: bool,
    replaceCreateString: Tuple[int, str],
    replaceEditString: Tuple[int, str],
    replaceFixedState: Tuple[int, bool],
    replaceLabel: Tuple[int, str],
    removeLastPanel: bool,
    replacePanel: Tuple[int, bool, str, str, str, str],
    replaceTypeString: Tuple[int, str],
    sceneConfig: bool,
    typeStrings: bool,
    userCreated: bool,
    useTemplate: str,
) -> Any:
    ...


def panelHistory(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    back: bool,
    clear: bool,
    defineTemplate: str,
    exists: bool,
    forward: bool,
    historyDepth: int,
    isEmpty: bool,
    suspend: bool,
    targetPane: str,
    useTemplate: str,
    wrap: bool,
) -> Any:
    ...


def paramDimContext(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def paramDimension() -> Any:
    ...


def paramLocator(*args: List[str], edit: bool, query: bool, position: bool) -> Any:
    ...


def parent(
    *args: List[str],
    absolute: bool,
    addObject: bool,
    noConnections: bool,
    noInvScale: bool,
    relative: bool,
    removeObject: bool,
    shape: bool,
    world: bool,
) -> Any:
    ...


def parentConstraint(
    *objects: List[str],
    createCache: Tuple[float, float],
    decompRotationToChild: bool,
    deleteCache: bool,
    edit: bool,
    layer: str,
    maintainOffset: bool,
    name: str,
    query: bool,
    remove: bool,
    skipRotate: List[str],
    skipTranslate: List[str],
    targetList: bool,
    weight: float,
    weightAliasList: bool,
) -> str:
    """parentConstraint is undoable, queryable, and editable.

    Constrain an object's position and rotation so that it behaves as if it were a child of the target object(s). In the case of multiple targets, the overall position and rotation of the constrained object is the weighted average of each target's contribution to the position and rotation of the object.
    A parentConstraint takes as input one or more "target" DAG transform nodes at which to position and rotate the single "constraint object" DAG transform node. The parentConstraint positions and rotates the constrained object at the weighted average of the world space position, rotation and scale target objects.

    Args:
        createCache: This flag is used to generate an animation curve that serves as a cache for the constraint. The two arguments define the start and end frames.  The cache is useful if the constraint has multiple targets and the constraint's interpolation type is set to "no flip". The "no flip" mode prevents flipping during playback, but the result is dependent on the previous frame. Therefore in order to consistently get the same result on a specific frame, a cache must be generated. This flag creates the cache and sets the constraint's interpolation type to "cache". If a cache exists already, it will be deleted and replaced with a new cache.
        decompRotationToChild: During constraint creation, if the rotation offset between the constrained object and the target object is maintained, this flag indicates close to which object the offset rotation is decomposed. Setting this flag will make the rotation decomposition close to the constrained object instead of the target object, which is the default setting.
        deleteCache: Delete an existing interpolation cache.
        layer: Specify the name of the animation layer where the constraint should be added.
        maintainOffset: If this flag is specified the position and rotation of the constrained object will be maintained.
        name: Sets the name of the constraint node to the specified name. Default name is constrainedObjectName_constraintType
        remove: removes the listed target(s) from the constraint.
        skipRotate: Causes the axis specified not to be considered when constraining rotation. Valid arguments are "x", "y", "z" and "none".
        skipTranslate: Causes the axis specified not to be considered when constraining translation. Valid arguments are "x", "y", "z" and "none".
        targetList: Return the list of target objects.
        weight: Sets the weight value for the specified target(s). If not given at creation time, the default value of 1.0 is used.
        weightAliasList: Returns the names of the attributes that control the weight of the target objects. Aliases are returned in the same order as the targets are returned by the targetList flag

    Returns:
        Name of the created constraint node.
        In query mode, return type is based on queried flag.

    Examples:
        >>> from maya import cmds
        >>> # Position cube1 at the location of cone1
        >>> # Rotate cube1 to the rotation of cone1
        >>> cmds.parentConstraint( 'cone1', 'cube1' )
        >>> # Position cube1 at the average of the locations of cone1 and surf2
        >>> # Rotate cube1 to the average of the rotations of cone1 and surf2
        >>> cmds.parentConstraint( 'cone1', 'surf2', 'cube2', w=.1 )
        >>> # Sets the weight for cone1's effect on cube2 to 10.
        >>> cmds.parentConstraint( 'cone1', 'cube2', e=True, w=10.0 )
        >>> # Removes surf2 from cube2's parentConstraint
        >>> cmds.parentConstraint( 'surf2', 'cube2', e=True, rm=True )
        >>> # Adds surf3 to cube2's parentConstraint with the default weight
        >>> cmds.parentConstraint( 'surf3', 'cube2' )
        >>> # Constrain position only in the y-axis with rotation
        >>> # constraining in all axes
        >>> cmds.parentConstraint( 'cone2', 'cube2', st=["x","z"] )
    """


def particle(
    *args: List[str],
    edit: bool,
    query: bool,
    attribute: str,
    conserve: float,
    cache: bool,
    count: bool,
    dynamicAttrList: bool,
    deleteCache: bool,
    floatValue: float,
    gridSpacing: List[float],
    inherit: float,
    particleId: int,
    jitterBasePoint: List[Tuple[float, float, float]],
    jitterRadius: List[float],
    lowerLeft: List[Tuple[float, float, float]],
    name: str,
    numJitters: List[int],
    order: int,
    position: List[Tuple[float, float, float]],
    perParticleDouble: bool,
    perParticleVector: bool,
    shapeName: str,
    upperRight: List[Tuple[float, float, float]],
    vectorValue: Tuple[float, float, float],
) -> Any:
    ...


def particleExists() -> Any:
    ...


def particleFill(
    *args: List[str],
    closePacking: bool,
    doubleWalled: bool,
    minX: float,
    minY: float,
    minZ: float,
    maxX: float,
    maxY: float,
    maxZ: float,
    particleDensity: float,
    resolution: int,
) -> Any:
    ...


def particleInstancer(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    addObject: bool,
    aimAxis: str,
    aimDirection: str,
    particleAge: str,
    attributeMapping: bool,
    aimPosition: str,
    aimUpAxis: str,
    aimWorldUp: str,
    cycle: str,
    cycleStep: float,
    cycleStepUnits: str,
    index: int,
    instanceId: str,
    levelOfDetail: str,
    name: str,
    object: List[str],
    objectIndex: str,
    position: str,
    rotation: str,
    removeObject: bool,
    rotationOrder: str,
    rotationType: str,
    rotationUnits: str,
    scale: str,
    shear: str,
    cycleStartObject: str,
    visibility: str,
) -> Any:
    ...


def particleRenderInfo(
    query: bool, attrList: int, attrListAll: bool, name: int, renderTypeCount: bool
) -> Any:
    ...


def partition(
    *args: List[str],
    edit: bool,
    query: bool,
    addSet: str,
    name: str,
    render: bool,
    removeSet: str,
) -> Any:
    ...


def pasteKey(
    *args: List[str],
    edit: bool,
    query: bool,
    animLayer: str,
    animation: str,
    attribute: List[str],
    connect: bool,
    clipboard: str,
    copies: int,
    float: Incomplete,
    floatOffset: float,
    index: Incomplete,
    includeUpperBound: bool,
    matchByName: bool,
    option: str,
    time: Incomplete,
    timeOffset: int,
    valueOffset: float,
) -> Any:
    ...


def pathAnimation(
    *args: List[str],
    edit: bool,
    query: bool,
    bank: bool,
    bankScale: float,
    bankThreshold: float,
    curve: str,
    endTimeU: List[int],
    endU: float,
    follow: bool,
    followAxis: str,
    fractionMode: bool,
    inverseFront: bool,
    inverseUp: bool,
    name: str,
    startTimeU: List[int],
    startU: float,
    upAxis: str,
    useNormal: bool,
    worldUpVector: Tuple[float, float, float],
    worldUpObject: str,
    worldUpType: str,
) -> Any:
    ...


def pause(seconds: int) -> Any:
    ...


def perCameraVisibility(
    *args: List[str],
    query: bool,
    camera: str,
    exclusive: bool,
    hide: bool,
    removeAll: bool,
    removeCamera: bool,
    remove: bool,
) -> Any:
    ...


def percent(
    *args: List[Incomplete],
    query: bool,
    addPercent: bool,
    dropoffAxis: Tuple[float, float, float],
    dropoffCurve: str,
    dropoffDistance: float,
    dropoffPosition: Tuple[float, float, float],
    dropoffType: str,
    multiplyPercent: bool,
    value: float,
) -> Any:
    ...


def performanceOptions(
    query: bool,
    clusterResolution: float,
    disableStitch: str,
    disableTrimDisplay: str,
    disableTrimBoundaryDisplay: str,
    latticeResolution: float,
    passThroughBindSkinAndFlexors: str,
    passThroughBlendShape: str,
    passThroughCluster: str,
    passThroughDeltaMush: str,
    passThroughFlexors: str,
    passThroughLattice: str,
    passThroughMeshBoolean: str,
    passThroughPaintEffects: str,
    passThroughSculpt: str,
    passThroughWire: str,
    regionOfEffect: str,
    skipHierarchyTraversal: bool,
    useClusterResolution: str,
    useLatticeResolution: str,
) -> Any:
    ...


def pfxstrokes(filename: str, postCallback: bool, selected: bool) -> Any:
    ...


def pickWalk(*args: List[str], direction: str, recurse: bool, type: str) -> Any:
    ...


def picture(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    image: str,
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    tile: bool,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def pixelMove() -> Any:
    ...


def planarSrf(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    degree: int,
    frozen: bool,
    keepOutside: bool,
    name: str,
    nodeState: int,
    object: bool,
    polygon: int,
    range: bool,
    tolerance: float,
) -> Any:
    ...


def plane(
    length: float,
    name: str,
    position: Tuple[float, float, float],
    rotation: Tuple[float, float, float],
    size: float,
    width: float,
) -> Any:
    ...


def play(
    query: bool,
    forward: bool,
    playSound: bool,
    record: bool,
    sound: str,
    state: bool,
    wait: bool,
) -> Any:
    ...


def playbackOptions(
    edit: bool,
    query: bool,
    animationEndTime: int,
    animationStartTime: int,
    blockingAnim: bool,
    framesPerSecond: bool,
    loop: str,
    maxTime: int,
    minTime: int,
    maxPlaybackSpeed: float,
    playbackSpeed: float,
    stepLoop: bool,
    view: str,
) -> Any:
    ...


def playblast(
    query: bool,
    activeEditor: bool,
    compression: str,
    clearCache: bool,
    completeFilename: str,
    codecOptions: bool,
    cameraSetup: List[Tuple[str, str]],
    combineSound: bool,
    editorPanelName: str,
    endTime: int,
    filename: str,
    format: str,
    forceOverwrite: bool,
    framePadding: int,
    frame: List[int],
    height: int,
    indexFromZero: bool,
    options: bool,
    showOrnaments: bool,
    offScreen: bool,
    offScreenViewportUpdate: bool,
    percent: int,
    quality: int,
    replaceAudioOnly: bool,
    replaceEndTime: int,
    replaceFilename: str,
    rawFrameNumbers: bool,
    replaceStartTime: int,
    sound: str,
    saveDepth: bool,
    sequenceTime: bool,
    startTime: int,
    throwOnError: bool,
    useTraxSounds: bool,
    viewer: bool,
    width: int,
    widthHeight: Tuple[int, int],
) -> Any:
    ...


def pluginDisplayFilter(
    arg0: str,
    /,
    query: bool,
    classification: str,
    deregister: bool,
    exists: bool,
    label: str,
    listFilters: bool,
    register: bool,
) -> Any:
    ...


def pluginInfo(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    autoload: bool,
    animCurveInterp: Tuple[str, str],
    allEvaluators: bool,
    activeFile: bool,
    apiVersion: bool,
    command: List[str],
    changedCommand: Callable,
    cacheFormat: bool,
    constraintCommand: bool,
    controlCommand: bool,
    data: List[Tuple[str, str]],
    dragAndDropBehavior: bool,
    dependNode: List[bool],
    dependNodeId: str,
    dependNodeByType: str,
    device: bool,
    evaluator: bool,
    iksolver: bool,
    loaded: bool,
    loadPluginPrefs: bool,
    listPlugins: bool,
    listPluginsPath: bool,
    modelEditorCommand: bool,
    name: str,
    path: str,
    pluginsInUse: bool,
    registered: bool,
    renderer: bool,
    remove: bool,
    referenceTranslators: bool,
    serviceDescriptions: bool,
    settings: bool,
    savePluginPrefs: bool,
    tool: List[str],
    translator: bool,
    userNamed: bool,
    unloadOk: bool,
    version: bool,
    vendor: str,
    writeRequires: bool,
) -> Any:
    ...


def pointConstraint(
    *args: List[str],
    edit: bool,
    query: bool,
    layer: str,
    maintainOffset: bool,
    name: str,
    offset: Tuple[float, float, float],
    remove: bool,
    skip: List[str],
    targetList: bool,
    weight: float,
    weightAliasList: bool,
) -> Any:
    ...


def pointCurveConstraint(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    position: Tuple[float, float, float],
    pointConstraintUVW: Tuple[float, float, float],
    pointWeight: float,
    replaceOriginal: bool,
    weight: float,
) -> Any:
    ...


def pointLight(
    *args: List[str],
    edit: bool,
    query: bool,
    decayRate: int,
    discRadius: float,
    exclusive: bool,
    intensity: float,
    name: str,
    position: Tuple[float, float, float],
    rotation: Tuple[float, float, float],
    useRayTraceShadows: bool,
    shadowColor: Tuple[float, float, float],
    shadowDither: float,
    shadowSamples: int,
    softShadow: bool,
) -> Any:
    ...


def pointOnCurve(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    curvatureCenter: bool,
    caching: bool,
    constructionHistory: bool,
    curvatureRadius: bool,
    frozen: bool,
    nodeState: int,
    normalizedNormal: bool,
    normal: bool,
    normalizedTangent: bool,
    position: bool,
    parameter: float,
    tangent: bool,
    turnOnPercentage: bool,
) -> Any:
    ...


def pointOnPolyConstraint(
    *args: List[str],
    edit: bool,
    query: bool,
    layer: str,
    maintainOffset: bool,
    name: str,
    offset: Tuple[float, float, float],
    remove: bool,
    skip: List[str],
    targetList: bool,
    weight: float,
    weightAliasList: bool,
) -> Any:
    ...


def pointOnSurface(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    nodeState: int,
    normalizedNormal: bool,
    normal: bool,
    normalizedTangentU: bool,
    normalizedTangentV: bool,
    position: bool,
    turnOnPercentage: bool,
    tangentU: bool,
    tangentV: bool,
    parameterU: float,
    parameterV: float,
) -> Any:
    ...


def pointPosition(arg0: Incomplete, /, local: bool, world: bool) -> Any:
    ...


def poleVectorConstraint(
    *args: List[str],
    edit: bool,
    query: bool,
    name: str,
    remove: bool,
    targetList: bool,
    weight: float,
    weightAliasList: bool,
) -> Any:
    ...


def polyAppend(
    *args: List[str],
    edit: bool,
    query: bool,
    append: List[Tuple[Incomplete, float, float, float, Incomplete]],
    constructionHistory: bool,
    edge: List[int],
    hole: List[bool],
    name: str,
    point: List[Tuple[float, float, float]],
    subdivision: int,
    texture: int,
) -> Any:
    ...


def polyAppendFacetCtx(*args, **kwargs) -> Any:
    ...


def polyAppendVertex(
    *args: List[str],
    edit: bool,
    query: bool,
    append: List[Tuple[Incomplete, float, float, float, Incomplete]],
    constructionHistory: bool,
    hole: List[bool],
    name: str,
    point: List[Tuple[float, float, float]],
    texture: int,
    vertex: List[int],
) -> Any:
    ...


def polyAutoProjection(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    createNewMap: bool,
    frozen: bool,
    insertBeforeDeformers: bool,
    layout: int,
    layoutMethod: int,
    name: str,
    nodeState: int,
    optimize: int,
    planes: int,
    projectBothDirections: bool,
    percentageSpace: float,
    pivot: Tuple[float, float, float],
    pivotX: float,
    pivotY: float,
    pivotZ: float,
    rotate: Tuple[float, float, float],
    rotateX: float,
    rotateY: float,
    rotateZ: float,
    scale: Tuple[float, float, float],
    scaleMode: int,
    skipIntersect: bool,
    scaleX: float,
    scaleY: float,
    scaleZ: float,
    translate: Tuple[float, float, float],
    translateX: float,
    translateY: float,
    translateZ: float,
    uvSetName: str,
    worldSpace: bool,
) -> Any:
    ...


def polyAverageNormal(
    *args: List[str],
    allowZeroNormal: bool,
    distance: float,
    postnormalize: bool,
    prenormalize: bool,
    replaceNormalXYZ: Tuple[float, float, float],
) -> Any:
    ...


def polyAverageVertex(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    iterations: int,
    name: str,
    nodeState: int,
    worldSpace: bool,
) -> Any:
    ...


def polyBevel(
    *args: List[str],
    edit: bool,
    query: bool,
    autoFit: bool,
    angleTolerance: float,
    caching: bool,
    constructionHistory: bool,
    useLegacyBevelAlgorithm: bool,
    fraction: float,
    fillNgons: bool,
    frozen: bool,
    maya2015: bool,
    miteringAngle: float,
    mergeVertices: bool,
    mergeVertexTolerance: float,
    name: str,
    nodeState: int,
    offset: float,
    offsetAsFraction: bool,
    roundness: float,
    smoothingAngle: float,
    segments: int,
    uvAssignment: int,
    worldSpace: bool,
) -> Any:
    ...


def polyBevel3(
    *args: List[str],
    edit: bool,
    query: bool,
    autoFit: bool,
    angleTolerance: float,
    chamfer: bool,
    caching: bool,
    constructionHistory: bool,
    depth: float,
    fraction: float,
    fillNgons: bool,
    forceParallel: bool,
    frozen: bool,
    mitering: int,
    maya2015: bool,
    maya2016SP3: bool,
    maya2017Update1: bool,
    miteringAngle: float,
    miterAlong: int,
    mergeVertices: bool,
    mergeVertexTolerance: float,
    name: str,
    nodeState: int,
    offset: float,
    offsetAsFraction: bool,
    roundness: float,
    smoothingAngle: float,
    segments: int,
    subdivideNgons: bool,
    worldSpace: bool,
) -> Any:
    ...


def polyBlendColor(
    *args: List[str],
    edit: bool,
    query: bool,
    baseColorName: str,
    blendFunc: int,
    blendWeightA: float,
    blendWeightB: float,
    blendWeightC: float,
    blendWeightD: float,
    caching: bool,
    constructionHistory: bool,
    dstColorName: str,
    frozen: bool,
    name: str,
    nodeState: int,
    srcColorName: str,
) -> Any:
    ...


def polyBlindData(
    *args: List[str],
    edit: bool,
    associationType: str,
    booleanData: List[bool],
    binaryData: List[str],
    doubleData: List[float],
    delete: bool,
    typeId: int,
    intData: List[int],
    longDataName: List[str],
    int64Data: List[int],
    rescan: bool,
    reset: bool,
    stringData: List[str],
    shortDataName: List[str],
    shape: bool,
) -> Any:
    ...


def polyBoolOp(
    *args: Tuple[str, str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    classification: int,
    faceAreaThreshold: float,
    frozen: bool,
    mergeUVSets: int,
    name: str,
    nodeState: int,
    object: bool,
    operation: int,
    preserveColor: bool,
    useThresholds: bool,
    vertexDistanceThreshold: float,
) -> Any:
    ...


def polyBridgeEdge(
    *args: List[str],
    edit: bool,
    query: bool,
    bridgeOffset: int,
    caching: bool,
    taperCurve_FloatValue: float,
    constructionHistory: bool,
    taperCurve_Interp: int,
    taperCurve_Position: float,
    curveType: int,
    direction: int,
    divisions: int,
    frozen: bool,
    inputCurve: str,
    name: str,
    nodeState: int,
    reverse: bool,
    sourceDirection: int,
    smoothingAngle: float,
    startVert1: int,
    startVert2: int,
    targetDirection: int,
    taper: float,
    twist: float,
    worldSpace: bool,
) -> Any:
    ...


def polyCBoolOp(
    *args: List[Incomplete],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    classification: int,
    edgeInterpolation: bool,
    faceAreaThreshold: float,
    frozen: bool,
    mergeUVSets: int,
    name: str,
    nodeState: int,
    object: bool,
    operation: int,
    preserveColor: bool,
    planarTolerance: float,
    sortOutput: bool,
    tagIntersection: bool,
    useCarveBooleans: bool,
    useThresholds: bool,
    vertexDistanceThreshold: float,
) -> Any:
    ...


def polyCacheMonitor(cacheValue: bool, nodeName: str) -> Any:
    ...


def polyCanBridgeEdge() -> Any:
    ...


def polyCheck(
    *args: List[str], edge: bool, face: bool, faceOffset: bool, openFile: str
) -> Any:
    ...


def polyChipOff(
    *args: List[str],
    edit: bool,
    query: bool,
    attraction: float,
    caching: bool,
    constructionHistory: bool,
    duplicate: bool,
    frozen: bool,
    gravity: Tuple[float, float, float],
    gain: List[float],
    gravityX: float,
    gravityY: float,
    gravityZ: float,
    keepFacesTogether: bool,
    localCenter: int,
    localDirection: Tuple[float, float, float],
    localDirectionX: float,
    localDirectionY: float,
    localDirectionZ: float,
    localRotate: Tuple[float, float, float],
    localRotateX: float,
    localRotateY: float,
    localRotateZ: float,
    localScale: Tuple[float, float, float],
    localScaleX: float,
    localScaleY: float,
    localScaleZ: float,
    localTranslate: Tuple[float, float, float],
    localTranslateX: float,
    localTranslateY: float,
    localTranslateZ: float,
    magnet: Tuple[float, float, float],
    magnX: float,
    magnY: float,
    magnZ: float,
    name: str,
    nodeState: int,
    offset: float,
    pivot: Tuple[float, float, float],
    pivotX: float,
    pivotY: float,
    pivotZ: float,
    random: float,
    rotate: Tuple[float, float, float],
    rotateX: float,
    rotateY: float,
    rotateZ: float,
    scale: Tuple[float, float, float],
    scaleX: float,
    scaleY: float,
    scaleZ: float,
    translate: Tuple[float, float, float],
    translateX: float,
    translateY: float,
    translateZ: float,
    weight: float,
    worldSpace: bool,
    keepFacetTogether: bool,
) -> Any:
    ...


def polyCircularize(
    *args: List[str],
    edit: bool,
    query: bool,
    alignment: int,
    caching: bool,
    constructionHistory: bool,
    divisions: int,
    evenlyDistribute: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    normalOffset: float,
    normalOrientation: int,
    relaxInterior: float,
    radialOffset: float,
    smoothingAngle: float,
    supportingEdges: int,
    twist: float,
    worldSpace: bool,
) -> Any:
    ...


def polyCircularizeEdge(
    *args: List[str],
    edit: bool,
    query: bool,
    alignment: int,
    caching: bool,
    constructionHistory: bool,
    divisions: int,
    evenlyDistribute: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    normalOffset: float,
    normalOrientation: int,
    relaxInterior: float,
    radialOffset: float,
    smoothingAngle: float,
    supportingEdges: int,
    twist: float,
    worldSpace: bool,
) -> Any:
    ...


def polyCircularizeFace(
    *args: List[str],
    edit: bool,
    query: bool,
    alignment: int,
    caching: bool,
    constructionHistory: bool,
    divisions: int,
    evenlyDistribute: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    normalOffset: float,
    normalOrientation: int,
    relaxInterior: float,
    radialOffset: float,
    smoothingAngle: float,
    supportingEdges: int,
    twist: float,
    worldSpace: bool,
) -> Any:
    ...


def polyClean(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    cleanEdges: bool,
    constructionHistory: bool,
    cleanPartialUVMapping: bool,
    cleanUVs: bool,
    cleanVertices: bool,
    frozen: bool,
    name: str,
    nodeState: int,
) -> Any:
    ...


def polyClipboard(
    *args: List[str],
    clear: bool,
    color: bool,
    copy: bool,
    paste: bool,
    shader: bool,
    uvCoordinates: bool,
) -> Any:
    ...


def polyCloseBorder(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
) -> Any:
    ...


def polyCollapseEdge(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
) -> Any:
    ...


def polyCollapseFacet(
    *args: List[str],
    edit: bool,
    query: bool,
    areaThreshold: float,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    useAreaThreshold: bool,
) -> Any:
    ...


def polyCollapseTweaks(arg0: Incomplete, /, query: bool, hasVertexTweaks: bool) -> Any:
    ...


def polyColorBlindData(*args, **kwargs) -> Any:
    ...


def polyColorDel(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    colorSetName: str,
    frozen: bool,
    name: str,
    nodeState: int,
) -> Any:
    ...


def polyColorMod(
    *args: List[str],
    edit: bool,
    query: bool,
    alphaScale_FloatValue: float,
    alphaScale_Interp: int,
    alphaScale_Position: float,
    baseColorName: str,
    blueScale_FloatValue: float,
    blueScale_Interp: int,
    blueScale_Position: float,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    greenScale_FloatValue: float,
    greenScale_Interp: int,
    greenScale_Position: float,
    huev: float,
    name: str,
    nodeState: int,
    intensityScale_FloatValue: float,
    intensityScale_Interp: int,
    intensityScale_Position: float,
    redScale_FloatValue: float,
    redScale_Interp: int,
    redScale_Position: float,
    satv: float,
    value: float,
) -> Any:
    ...


def polyColorPerVertex(
    *args: List[str],
    edit: bool,
    query: bool,
    alpha: float,
    colorB: float,
    colorDisplayOption: bool,
    clamped: bool,
    colorG: float,
    notUndoable: bool,
    colorR: float,
    relative: bool,
    remove: bool,
    colorRGB: Tuple[float, float, float],
    representation: int,
) -> Any:
    ...


def polyColorSet(
    *args: List[str],
    edit: bool,
    query: bool,
    allColorSets: bool,
    currentColorSet: bool,
    clamped: bool,
    copy: bool,
    currentPerInstanceSet: bool,
    create: bool,
    colorSet: str,
    delete: bool,
    newColorSet: str,
    perInstance: bool,
    rename: bool,
    representation: str,
    shareInstances: bool,
    unshared: bool,
) -> Any:
    ...


def polyColorSetCmdWrapper(*args, **kwargs) -> Any:
    ...


def polyCompare(
    *args: List[str],
    colorSets: bool,
    edges: bool,
    faceDesc: bool,
    colorSetIndices: bool,
    uvSetIndices: bool,
    userNormals: bool,
    uvSets: bool,
    vertices: bool,
) -> Any:
    ...


def polyCone(
    *args: List[str],
    edit: bool,
    query: bool,
    axis: Tuple[float, float, float],
    caching: bool,
    constructionHistory: bool,
    componentTagCreate: bool,
    createUVs: int,
    frozen: bool,
    height: float,
    heightBaseline: float,
    name: str,
    nodeState: int,
    object: bool,
    radius: float,
    roundCap: bool,
    subdivisionsAxis: int,
    subdivisionsCap: int,
    subdivisionsHeight: int,
    subdivisionsX: int,
    subdivisionsY: int,
    subdivisionsZ: int,
    texture: bool,
) -> Any:
    ...


def polyConnectComponents(
    *args: List[str],
    edit: bool,
    query: bool,
    adjustEdgeFlow: float,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    insertWithEdgeFlow: bool,
    name: str,
    nodeState: int,
) -> Any:
    ...


def polyContourProjection(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    createNewMap: bool,
    flipRails: bool,
    frozen: bool,
    insertBeforeDeformers: bool,
    method: int,
    name: str,
    nodeState: int,
    offset0: float,
    offset1: float,
    offset2: float,
    offset3: float,
    reduceShear: float,
    smoothness0: float,
    smoothness1: float,
    smoothness2: float,
    smoothness3: float,
    userDefinedCorners: bool,
    uvSetName: str,
    worldSpace: bool,
) -> Any:
    ...


def polyCopyUV(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    createNewMap: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    uvSetNameInput: str,
    uvSetName: str,
    worldSpace: bool,
) -> Any:
    ...


def polyCrease(
    *args: List[str],
    edit: bool,
    query: bool,
    createHistory: bool,
    operation: int,
    relativeValue: float,
    value: List[float],
    vertexValue: List[float],
) -> Any:
    ...


def polyCreaseCtx(*args, **kwargs) -> Any:
    ...


def polyCreateFacet(
    *args: List[str],
    edit: bool,
    query: bool,
    constructionHistory: bool,
    hole: List[bool],
    name: str,
    point: List[Tuple[Incomplete, float, float, float, Incomplete]],
    subdivision: int,
    texture: int,
) -> Any:
    ...


def polyCreateFacetCtx(*args, **kwargs) -> Any:
    ...


def polyCube(
    *args: List[str],
    edit: bool,
    query: bool,
    axis: Tuple[float, float, float],
    caching: bool,
    constructionHistory: bool,
    componentTagCreate: bool,
    createUVs: int,
    depth: float,
    frozen: bool,
    height: float,
    heightBaseline: float,
    name: str,
    nodeState: int,
    object: bool,
    subdivisionsDepth: int,
    subdivisionsHeight: int,
    subdivisionsWidth: int,
    subdivisionsX: int,
    subdivisionsY: int,
    subdivisionsZ: int,
    texture: int,
    width: float,
) -> Any:
    ...


def polyCut(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    cuttingDirection: str,
    constructionHistory: bool,
    deleteFaces: bool,
    extractFaces: bool,
    extractOffset: Tuple[float, float, float],
    extractOffsetX: float,
    extractOffsetY: float,
    extractOffsetZ: float,
    frozen: bool,
    name: str,
    nodeState: int,
    onObject: bool,
    cutPlaneCenter: Tuple[float, float, float],
    cutPlaneCenterX: float,
    cutPlaneCenterY: float,
    cutPlaneCenterZ: float,
    cutPlaneHeight: float,
    cutPlaneSize: Tuple[float, float],
    cutPlaneWidth: float,
    cutPlaneRotate: Tuple[float, float, float],
    cutPlaneRotateX: float,
    cutPlaneRotateY: float,
    cutPlaneRotateZ: float,
    worldSpace: bool,
) -> Any:
    ...


def polyCutCtx(*args, **kwargs) -> Any:
    ...


def polyCutUVCtx(*args, **kwargs) -> Any:
    ...


def polyCylinder(
    *args: List[str],
    edit: bool,
    query: bool,
    axis: Tuple[float, float, float],
    caching: bool,
    constructionHistory: bool,
    componentTagCreate: bool,
    createUVs: int,
    frozen: bool,
    height: float,
    heightBaseline: float,
    name: str,
    nodeState: int,
    object: bool,
    radius: float,
    roundCapHeightCompensation: bool,
    roundCap: bool,
    subdivisionsAxis: int,
    subdivisionsCaps: int,
    subdivisionsHeight: int,
    subdivisionsX: int,
    subdivisionsY: int,
    subdivisionsZ: int,
    texture: int,
) -> Any:
    ...


def polyCylindricalProjection(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    createNewMap: bool,
    frozen: bool,
    insertBeforeDeformers: bool,
    imageCenter: Tuple[float, float],
    imageCenterX: float,
    imageCenterY: float,
    imageScale: Tuple[float, float],
    imageScaleU: float,
    imageScaleV: float,
    keepImageRatio: bool,
    mapDirection: str,
    name: str,
    nodeState: int,
    projectionCenter: Tuple[float, float, float],
    projectionCenterX: float,
    projectionCenterY: float,
    projectionCenterZ: float,
    projectionHeight: float,
    projectionHorizontalSweep: float,
    perInstance: bool,
    projectionScale: Tuple[float, float],
    projectionScaleU: float,
    projectionScaleV: float,
    radius: float,
    rotationAngle: float,
    rotate: Tuple[float, float, float],
    rotateX: float,
    rotateY: float,
    rotateZ: float,
    seamCorrect: bool,
    smartFit: bool,
    worldSpace: bool,
) -> Any:
    ...


def polyDelEdge(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    cleanVertices: bool,
    frozen: bool,
    name: str,
    nodeState: int,
) -> Any:
    ...


def polyDelFacet(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
) -> Any:
    ...


def polyDelVertex(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
) -> Any:
    ...


def polyDuplicateAndConnect(
    *args: List[str], renameChildren: bool, removeOriginalFromShaders: bool
) -> Any:
    ...


def polyDuplicateEdge(
    *args: List[str],
    edit: bool,
    query: bool,
    adjustEdgeFlow: float,
    caching: bool,
    constructionHistory: bool,
    deleteEdge: bool,
    endVertexOffset: float,
    frozen: bool,
    insertWithEdgeFlow: bool,
    name: str,
    nodeState: int,
    offset: float,
    smoothingAngle: float,
    splitType: int,
    startVertexOffset: float,
) -> Any:
    ...


def polyEditEdgeFlow(
    *args: List[str],
    edit: bool,
    query: bool,
    adjustEdgeFlow: float,
    caching: bool,
    constructionHistory: bool,
    edgeFlow: bool,
    frozen: bool,
    name: str,
    nodeState: int,
) -> Any:
    ...


def polyEditUV(
    *args: List[str],
    query: bool,
    angle: float,
    pivotU: float,
    pivotV: float,
    relative: bool,
    rotation: bool,
    rotateRatio: float,
    scale: bool,
    scaleU: float,
    scaleV: float,
    uValue: float,
    uvSetName: str,
    vValue: float,
) -> Any:
    ...


def polyEditUVShell(
    *args: List[str],
    query: bool,
    angle: float,
    pivotU: float,
    pivotV: float,
    relative: bool,
    rotation: bool,
    rotateRatio: float,
    scale: bool,
    scaleU: float,
    scaleV: float,
    uValue: float,
    uvSetName: str,
    vValue: float,
) -> Any:
    ...


def polyEvaluate(
    *args: List[str],
    area: bool,
    accurateEvaluation: bool,
    activeShells: bool,
    activeUVShells: bool,
    boundingBox: bool,
    boundingBox2d: bool,
    boundingBoxComponent: bool,
    boundingBoxComponent2d: bool,
    displayStats: bool,
    edge: bool,
    edgeComponent: bool,
    face: bool,
    faceArea: bool,
    faceComponent: bool,
    format: bool,
    shell: bool,
    triangle: bool,
    triangleComponent: bool,
    uvEdgePairs: bool,
    uvFaceArea: bool,
    uvsInShell: int,
    uvShell: bool,
    uvShellIds: bool,
    uvcoord: bool,
    uvArea: bool,
    uvComponent: bool,
    uvSetName: str,
    vertex: bool,
    vertexComponent: bool,
    worldArea: bool,
    worldFaceArea: bool,
) -> Any:
    ...


def polyExtrudeEdge(
    *args: List[str],
    edit: bool,
    query: bool,
    createCurve: bool,
    caching: bool,
    taperCurve_FloatValue: float,
    constructionHistory: bool,
    taperCurve_Interp: int,
    taperCurve_Position: float,
    divisions: int,
    frozen: bool,
    gain: List[float],
    inputCurve: str,
    keepFacesTogether: bool,
    localCenter: int,
    localDirection: Tuple[float, float, float],
    localDirectionX: float,
    localDirectionY: float,
    localDirectionZ: float,
    localRotate: Tuple[float, float, float],
    localRotateX: float,
    localRotateY: float,
    localRotateZ: float,
    localScale: Tuple[float, float, float],
    localScaleX: float,
    localScaleY: float,
    localScaleZ: float,
    localTranslate: Tuple[float, float, float],
    localTranslateX: float,
    localTranslateY: float,
    localTranslateZ: float,
    name: str,
    nodeState: int,
    offset: float,
    pivot: Tuple[float, float, float],
    pivotX: float,
    pivotY: float,
    pivotZ: float,
    random: float,
    rotate: Tuple[float, float, float],
    rotateX: float,
    rotateY: float,
    rotateZ: float,
    scale: Tuple[float, float, float],
    smoothingAngle: float,
    scaleX: float,
    scaleY: float,
    scaleZ: float,
    translate: Tuple[float, float, float],
    thickness: float,
    taper: float,
    twist: float,
    translateX: float,
    translateY: float,
    translateZ: float,
    worldSpace: bool,
) -> Any:
    ...


def polyExtrudeFacet(
    *args: List[str],
    edit: bool,
    query: bool,
    attraction: float,
    createCurve: bool,
    caching: bool,
    taperCurve_FloatValue: float,
    constructionHistory: bool,
    taperCurve_Interp: int,
    taperCurve_Position: float,
    divisions: int,
    frozen: bool,
    gravity: Tuple[float, float, float],
    gain: List[float],
    gravityX: float,
    gravityY: float,
    gravityZ: float,
    inputCurve: str,
    keepFacesTogether: bool,
    localCenter: int,
    localDirection: Tuple[float, float, float],
    localDirectionX: float,
    localDirectionY: float,
    localDirectionZ: float,
    localRotate: Tuple[float, float, float],
    localRotateX: float,
    localRotateY: float,
    localRotateZ: float,
    localScale: Tuple[float, float, float],
    localScaleX: float,
    localScaleY: float,
    localScaleZ: float,
    localTranslate: Tuple[float, float, float],
    localTranslateX: float,
    localTranslateY: float,
    localTranslateZ: float,
    magnet: Tuple[float, float, float],
    maya2012: bool,
    maya2018: bool,
    maya2023: bool,
    magnX: float,
    magnY: float,
    magnZ: float,
    name: str,
    nodeState: int,
    newThickness: bool,
    offset: float,
    pivot: Tuple[float, float, float],
    pivotX: float,
    pivotY: float,
    pivotZ: float,
    reverseAllFaces: bool,
    random: float,
    rotate: Tuple[float, float, float],
    rotateX: float,
    rotateY: float,
    rotateZ: float,
    scale: Tuple[float, float, float],
    smoothingAngle: float,
    scaleX: float,
    scaleY: float,
    scaleZ: float,
    translate: Tuple[float, float, float],
    thickness: float,
    taper: float,
    twist: float,
    translateX: float,
    translateY: float,
    translateZ: float,
    weight: float,
    worldSpace: bool,
    keepFacetTogether: bool,
) -> Any:
    ...


def polyExtrudeVertex(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    divisions: int,
    frozen: bool,
    length: float,
    name: str,
    nodeState: int,
    width: float,
    worldSpace: bool,
) -> Any:
    ...


def polyFlipEdge(*args: List[str], edit: bool, query: bool) -> Any:
    ...


def polyFlipUV(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    createNewMap: bool,
    cutUV: bool,
    flipType: int,
    frozen: bool,
    insertBeforeDeformers: bool,
    local: bool,
    name: str,
    nodeState: int,
    pivotU: float,
    pivotV: float,
    usePivot: bool,
    uvSetName: str,
    worldSpace: bool,
) -> Any:
    ...


def polyForceUV(
    *args: List[str],
    createNewMap: bool,
    cameraProjection: bool,
    flipHorizontal: bool,
    flipVertical: bool,
    g: bool,
    local: bool,
    numItems: int,
    normalize: str,
    preserveAspectRatio: bool,
    unshare: bool,
    unitize: bool,
    uvSetName: str,
) -> Any:
    ...


def polyGeoSampler(*args, **kwargs) -> Any:
    ...


def polyHelix(
    *args: List[str],
    edit: bool,
    query: bool,
    axis: Tuple[float, float, float],
    coils: float,
    caching: bool,
    constructionHistory: bool,
    componentTagCreate: bool,
    createUVs: int,
    direction: int,
    frozen: bool,
    height: float,
    heightBaseline: float,
    name: str,
    nodeState: int,
    object: bool,
    useOldInitBehaviour: bool,
    radius: float,
    roundCap: bool,
    subdivisionsAxis: int,
    subdivisionsCaps: int,
    subdivisionsCoil: int,
    texture: int,
    width: float,
) -> Any:
    ...


def polyHole(
    *args: List[str], edit: bool, query: bool, assignHole: bool, createHistory: bool
) -> Any:
    ...


def polyInfo(
    *args: List[str],
    edgeToFace: bool,
    edgeToVertex: bool,
    faceToEdge: bool,
    faceNormals: bool,
    faceToVertex: bool,
    invalidEdges: bool,
    invalidVertices: bool,
    laminaFaces: bool,
    nonManifoldEdges: bool,
    nonManifoldVertices: bool,
    nonManifoldUVEdges: bool,
    nonManifoldUVs: bool,
    vertexToEdge: bool,
    vertexToFace: bool,
) -> Any:
    ...


def polyInstallAction(*args, **kwargs) -> Any:
    ...


def polyIterOnPoly(*args, **kwargs) -> Any:
    ...


def polyLayoutUV(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    flipReversed: bool,
    frozen: bool,
    gridU: int,
    gridV: int,
    layout: int,
    layoutMethod: int,
    name: str,
    nodeState: int,
    percentageSpace: float,
    rotateForBestFit: int,
    scale: int,
    separate: int,
    uvSetName: str,
    worldSpace: bool,
) -> Any:
    ...


def polyListComponentConversion(
    *args: List[str],
    border: bool,
    fromEdge: bool,
    fromFace: bool,
    fromUV: bool,
    fromVertex: bool,
    fromVertexFace: bool,
    internal: bool,
    toEdge: bool,
    toFace: bool,
    toUV: bool,
    toVertex: bool,
    toVertexFace: bool,
    uvShell: bool,
    vertexFaceAllEdges: bool,
) -> Any:
    ...


def polyMapCut(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    moveRatio: float,
    moveratio: float,
    name: str,
    nodeState: int,
    usePinning: bool,
) -> Any:
    ...


def polyMapDel(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
) -> Any:
    ...


def polyMapSew(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    usePinning: bool,
) -> Any:
    ...


def polyMapSewMove(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    limitPieceSize: bool,
    name: str,
    nodeState: int,
    numberFaces: int,
    uvSetName: str,
    worldSpace: bool,
) -> Any:
    ...


def polyMergeEdge(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    firstEdge: int,
    frozen: bool,
    mergeMode: int,
    mergeTexture: bool,
    name: str,
    nodeState: int,
    secondEdge: int,
) -> Any:
    ...


def polyMergeEdgeCtx(*args, **kwargs) -> Any:
    ...


def polyMergeFacet(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    firstFacet: int,
    frozen: bool,
    mergeMode: int,
    name: str,
    nodeState: int,
    secondFacet: int,
) -> Any:
    ...


def polyMergeFacetCtx(*args, **kwargs) -> Any:
    ...


def polyMergeUV(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    distance: float,
    frozen: bool,
    name: str,
    nodeState: int,
    uvSetName: str,
    worldSpace: bool,
) -> Any:
    ...


def polyMergeVertex(
    *args: List[str],
    edit: bool,
    query: bool,
    alwaysMergeTwoVertices: bool,
    caching: bool,
    constructionHistory: bool,
    distance: float,
    frozen: bool,
    mergeToComponents: str,
    name: str,
    nodeState: int,
    texture: bool,
    worldSpace: bool,
) -> Any:
    ...


def polyMirrorFace(
    *args: List[str],
    edit: bool,
    query: bool,
    axis: int,
    axisDirection: int,
    caching: bool,
    constructionHistory: bool,
    cutMesh: bool,
    direction: int,
    firstNewFace: int,
    flipUVs: int,
    frozen: bool,
    keepVertexIDs: bool,
    lastNewFace: int,
    mirrorAxis: int,
    mergeMode: int,
    mirrorPosition: float,
    mergeThreshold: float,
    mergeThresholdType: int,
    name: str,
    nodeState: int,
    pivot: Tuple[float, float, float],
    mirrorPlaneCenter: Tuple[float, float, float],
    mirrorPlaneCenterX: float,
    mirrorPlaneCenterY: float,
    mirrorPlaneCenterZ: float,
    userSpecifiedPivot: bool,
    pivotX: float,
    pivotY: float,
    pivotZ: float,
    mirrorPlaneRotate: Tuple[float, float, float],
    mirrorPlaneRotateX: float,
    mirrorPlaneRotateY: float,
    mirrorPlaneRotateZ: float,
    smoothingAngle: float,
    scalePivotX: float,
    scalePivotY: float,
    scalePivotZ: float,
    worldSpace: bool,
) -> Any:
    ...


def polyMoveEdge(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    gain: List[float],
    localCenter: int,
    localDirection: Tuple[float, float, float],
    localDirectionX: float,
    localDirectionY: float,
    localDirectionZ: float,
    localRotate: Tuple[float, float, float],
    localRotateX: float,
    localRotateY: float,
    localRotateZ: float,
    localScale: Tuple[float, float, float],
    localScaleX: float,
    localScaleY: float,
    localScaleZ: float,
    localTranslate: Tuple[float, float, float],
    localTranslateX: float,
    localTranslateY: float,
    localTranslateZ: float,
    name: str,
    nodeState: int,
    pivot: Tuple[float, float, float],
    pivotX: float,
    pivotY: float,
    pivotZ: float,
    random: float,
    rotate: Tuple[float, float, float],
    rotateX: float,
    rotateY: float,
    rotateZ: float,
    scale: Tuple[float, float, float],
    scaleX: float,
    scaleY: float,
    scaleZ: float,
    translate: Tuple[float, float, float],
    translateX: float,
    translateY: float,
    translateZ: float,
    worldSpace: bool,
) -> Any:
    ...


def polyMoveFacet(
    *args: List[str],
    edit: bool,
    query: bool,
    attraction: float,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    gravity: Tuple[float, float, float],
    gain: List[float],
    gravityX: float,
    gravityY: float,
    gravityZ: float,
    localCenter: int,
    localDirection: Tuple[float, float, float],
    localDirectionX: float,
    localDirectionY: float,
    localDirectionZ: float,
    localRotate: Tuple[float, float, float],
    localRotateX: float,
    localRotateY: float,
    localRotateZ: float,
    localScale: Tuple[float, float, float],
    localScaleX: float,
    localScaleY: float,
    localScaleZ: float,
    localTranslate: Tuple[float, float, float],
    localTranslateX: float,
    localTranslateY: float,
    localTranslateZ: float,
    magnet: Tuple[float, float, float],
    magnX: float,
    magnY: float,
    magnZ: float,
    name: str,
    nodeState: int,
    offset: float,
    pivot: Tuple[float, float, float],
    pivotX: float,
    pivotY: float,
    pivotZ: float,
    random: float,
    rotate: Tuple[float, float, float],
    rotateX: float,
    rotateY: float,
    rotateZ: float,
    scale: Tuple[float, float, float],
    scaleX: float,
    scaleY: float,
    scaleZ: float,
    translate: Tuple[float, float, float],
    translateX: float,
    translateY: float,
    translateZ: float,
    weight: float,
    worldSpace: bool,
) -> Any:
    ...


def polyMoveFacetUV(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    axisLen: Tuple[float, float],
    axisLenX: float,
    axisLenY: float,
    name: str,
    nodeState: int,
    pivot: Tuple[float, float],
    pivotU: float,
    pivotV: float,
    rotationAngle: float,
    random: float,
    scale: Tuple[float, float],
    scaleU: float,
    scaleV: float,
    translate: Tuple[float, float],
    translateU: float,
    translateV: float,
) -> Any:
    ...


def polyMoveUV(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    axisLen: Tuple[float, float],
    axisLenX: float,
    axisLenY: float,
    name: str,
    nodeState: int,
    pivot: Tuple[float, float],
    pivotU: float,
    pivotV: float,
    rotationAngle: float,
    random: float,
    scale: Tuple[float, float],
    scaleU: float,
    scaleV: float,
    translate: Tuple[float, float],
    translateU: float,
    translateV: float,
) -> Any:
    ...


def polyMoveVertex(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    gain: List[float],
    localDirection: Tuple[float, float, float],
    localDirectionX: float,
    localDirectionY: float,
    localDirectionZ: float,
    localTranslate: Tuple[float, float, float],
    localTranslateX: float,
    localTranslateY: float,
    localTranslateZ: float,
    name: str,
    nodeState: int,
    pivot: Tuple[float, float, float],
    pivotX: float,
    pivotY: float,
    pivotZ: float,
    random: float,
    rotate: Tuple[float, float, float],
    rotateX: float,
    rotateY: float,
    rotateZ: float,
    scale: Tuple[float, float, float],
    scaleX: float,
    scaleY: float,
    scaleZ: float,
    translate: Tuple[float, float, float],
    translateX: float,
    translateY: float,
    translateZ: float,
    worldSpace: bool,
) -> Any:
    ...


def polyMultiLayoutUV(
    *args: List[str],
    flipReversed: bool,
    gridU: int,
    gridV: int,
    layout: int,
    layoutMethod: int,
    offsetU: float,
    offsetV: float,
    percentageSpace: float,
    prescale: int,
    rotateForBestFit: int,
    scale: int,
    sizeU: float,
    sizeV: float,
    uvSetName: str,
) -> Any:
    ...


def polyNormal(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    normalMode: int,
    userNormalMode: bool,
) -> Any:
    ...


def polyNormalPerVertex(
    *args: List[str],
    edit: bool,
    query: bool,
    allLocked: bool,
    deformable: bool,
    freezeNormal: bool,
    relative: bool,
    unFreezeNormal: bool,
    normalX: float,
    normalXYZ: List[Tuple[float, float, float]],
    normalY: float,
    normalZ: float,
) -> Any:
    ...


def polyNormalizeUV(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    createNewMap: bool,
    centerOnTile: bool,
    frozen: bool,
    insertBeforeDeformers: bool,
    name: str,
    normalizeDirection: int,
    nodeState: int,
    normalizeType: int,
    preserveAspectRatio: bool,
    uvSetName: str,
    worldSpace: bool,
) -> Any:
    ...


def polyOptUvs(
    *args: List[str],
    edit: bool,
    query: bool,
    applyToShell: bool,
    areaWeight: float,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    globalBlend: float,
    globalMethodBlend: float,
    iterations: int,
    name: str,
    nodeState: int,
    optimizeAxis: int,
    pinSelected: bool,
    pinUvBorder: bool,
    scale: float,
    stoppingThreshold: float,
    useScale: bool,
    uvSetName: str,
    worldSpace: bool,
) -> Any:
    ...


def polyOptions(*args, **kwargs) -> Any:
    ...


def polyOutput(
    *args: List[str],
    allValues: bool,
    color: bool,
    colorDesc: bool,
    edge: bool,
    edgeFace: bool,
    face: bool,
    faceNorm: bool,
    force: bool,
    group: bool,
    normDesc: bool,
    noOutput: bool,
    outputFile: str,
    triangle: bool,
    uvValue: bool,
    uvDesc: bool,
    vert: bool,
    vertEdge: bool,
    vertNorm: bool,
) -> Any:
    ...


def polyPinUV(
    *args: List[str],
    edit: bool,
    query: bool,
    createHistory: bool,
    operation: int,
    unpinned: bool,
    uvSetName: str,
    value: List[float],
) -> Any:
    ...


def polyPipe(
    *args: List[str],
    edit: bool,
    query: bool,
    axis: Tuple[float, float, float],
    caching: bool,
    constructionHistory: bool,
    componentTagCreate: bool,
    createUVs: bool,
    frozen: bool,
    height: float,
    heightBaseline: float,
    name: str,
    nodeState: int,
    object: bool,
    radius: float,
    roundCapHeightCompensation: bool,
    roundCap: bool,
    subdivisionsAxis: int,
    subdivisionsCaps: int,
    subdivisionsHeight: int,
    thickness: float,
    texture: bool,
) -> Any:
    ...


def polyPlanarProjection(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    createNewMap: bool,
    frozen: bool,
    insertBeforeDeformers: bool,
    imageCenter: Tuple[float, float],
    imageCenterX: float,
    imageCenterY: float,
    imageScale: Tuple[float, float],
    imageScaleU: float,
    imageScaleV: float,
    keepImageRatio: bool,
    mapDirection: str,
    name: str,
    nodeState: int,
    projectionCenter: Tuple[float, float, float],
    projectionCenterX: float,
    projectionCenterY: float,
    projectionCenterZ: float,
    projectionHeight: float,
    projectionHorizontalSweep: float,
    perInstance: bool,
    projectionScale: Tuple[float, float],
    projectionScaleU: float,
    projectionScaleV: float,
    radius: float,
    rotationAngle: float,
    rotate: Tuple[float, float, float],
    rotateX: float,
    rotateY: float,
    rotateZ: float,
    seamCorrect: bool,
    smartFit: bool,
    worldSpace: bool,
) -> Any:
    ...


def polyPlane(
    *args: List[str],
    edit: bool,
    query: bool,
    axis: Tuple[float, float, float],
    caching: bool,
    constructionHistory: bool,
    componentTagCreate: bool,
    createUVs: int,
    frozen: bool,
    height: float,
    heightBaseline: float,
    name: str,
    nodeState: int,
    object: bool,
    subdivisionsHeight: int,
    subdivisionsWidth: int,
    subdivisionsX: int,
    subdivisionsY: int,
    texture: int,
    width: float,
) -> Any:
    ...


def polyPlatonicSolid(
    *args: List[str],
    edit: bool,
    query: bool,
    axis: Tuple[float, float, float],
    caching: bool,
    constructionHistory: bool,
    componentTagCreate: bool,
    createUVs: int,
    frozen: bool,
    heightBaseline: float,
    sideLength: float,
    name: str,
    nodeState: int,
    object: bool,
    radius: float,
    solidType: int,
    texture: int,
) -> Any:
    ...


def polyPoke(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    localTranslate: Tuple[float, float, float],
    localTranslateX: float,
    localTranslateY: float,
    localTranslateZ: float,
    name: str,
    nodeState: int,
    translate: Tuple[float, float, float],
    translateX: float,
    translateY: float,
    translateZ: float,
    worldSpace: bool,
) -> Any:
    ...


def polyPrimitive(
    *args: List[str],
    edit: bool,
    query: bool,
    axis: Tuple[float, float, float],
    caching: bool,
    constructionHistory: bool,
    componentTagCreate: bool,
    createUVs: int,
    frozen: bool,
    heightBaseline: float,
    sideLength: float,
    name: str,
    nodeState: int,
    object: bool,
    polyType: int,
    radius: float,
    texture: int,
) -> Any:
    ...


def polyPrimitiveMisc(*args, **kwargs) -> Any:
    ...


def polyPrism(
    *args: List[str],
    edit: bool,
    query: bool,
    axis: Tuple[float, float, float],
    caching: bool,
    constructionHistory: bool,
    componentTagCreate: bool,
    createUVs: int,
    frozen: bool,
    heightBaseline: float,
    length: float,
    name: str,
    nodeState: int,
    numberOfSides: int,
    numderOfSides: int,
    object: bool,
    subdivisionsCaps: int,
    subdivisionsHeight: int,
    texture: int,
    sideLength: float,
) -> Any:
    ...


def polyProjectCurve(
    *args: Tuple[str, str],
    edit: bool,
    query: bool,
    automatic: bool,
    addUnderTransform: bool,
    baryCoord: Tuple[float, float, float],
    baryCoord1: float,
    baryCoord2: float,
    baryCoord3: float,
    caching: bool,
    constructionHistory: bool,
    curveSamples: int,
    direction: Tuple[float, float, float],
    directionX: float,
    directionY: float,
    directionZ: float,
    face: int,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    pointsOnEdges: bool,
    triangle: int,
    tolerance: float,
) -> Any:
    ...


def polyProjection(
    *args: List[str],
    constructionHistory: bool,
    createNewMap: bool,
    insertBeforeDeformers: bool,
    imageCenterX: float,
    imageCenterY: float,
    imageScaleU: float,
    imageScaleV: float,
    keepImageRatio: bool,
    mapDirection: str,
    projectionCenterX: float,
    projectionCenterY: float,
    projectionCenterZ: float,
    projectionScaleU: float,
    projectionScaleV: float,
    rotationAngle: float,
    rotateX: float,
    rotateY: float,
    rotateZ: float,
    seamCorrect: bool,
    smartFit: bool,
    type: str,
    uvSetName: str,
) -> Any:
    ...


def polyPyramid(
    *args: List[str],
    edit: bool,
    query: bool,
    axis: Tuple[float, float, float],
    caching: bool,
    constructionHistory: bool,
    componentTagCreate: bool,
    createUVs: int,
    frozen: bool,
    heightBaseline: float,
    name: str,
    nodeState: int,
    numberOfSides: int,
    numderOfSides: int,
    object: bool,
    subdivisionsCaps: int,
    subdivisionsHeight: int,
    texture: bool,
    sideLength: float,
) -> Any:
    ...


def polyQuad(
    *args: List[str],
    edit: bool,
    query: bool,
    angle: float,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    keepGroupBorder: bool,
    keepHardEdges: bool,
    keepTextureBorders: bool,
    name: str,
    nodeState: int,
    worldSpace: bool,
) -> Any:
    ...


def polyQueryBlindData(
    *args: List[str],
    associationType: str,
    booleanData: bool,
    binaryData: str,
    doubleData: float,
    typeId: int,
    intData: int,
    longDataName: List[str],
    maxValue: float,
    minValue: float,
    showComp: bool,
    stringData: str,
    shortDataName: List[str],
    subString: str,
) -> Any:
    ...


def polyReduce(
    *args: List[str],
    edit: bool,
    query: bool,
    border: float,
    caching: bool,
    keepCreaseEdgeWeight: float,
    constructionHistory: bool,
    compactness: float,
    cachingReduce: bool,
    colorWeights: float,
    detail: float,
    frozen: bool,
    geomWeights: float,
    invertVertexWeights: bool,
    keepBorder: bool,
    keepBorderWeight: float,
    keepColorBorder: bool,
    keepCreaseEdge: bool,
    keepColorBorderWeight: float,
    keepOriginalVertices: bool,
    keepFaceGroupBorder: bool,
    keepFaceGroupBorderWeight: float,
    keepHardEdge: bool,
    keepHardEdgeWeight: float,
    keepMapBorder: bool,
    keepMapBorderWeight: float,
    keepQuadsWeight: float,
    line: float,
    name: str,
    nodeState: int,
    percentage: float,
    preserveLocation: bool,
    replaceOriginal: bool,
    sharpness: float,
    symmetryTolerance: float,
    symmetryPlaneW: float,
    symmetryPlaneX: float,
    symmetryPlaneY: float,
    symmetryPlane: Tuple[float, float, float, float],
    symmetryPlaneZ: float,
    triangulate: bool,
    triangleCount: int,
    preserveTopology: bool,
    termination: int,
    useVirtualSymmetry: int,
    uvWeights: float,
    vertexCount: int,
    version: int,
    vertexMapName: str,
    vertexWeightCoefficient: float,
    weightCoefficient: float,
) -> Any:
    ...


def polyRemesh(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    collapseThreshold: float,
    frozen: bool,
    interpolationType: int,
    maxEdgeLength: float,
    maxTriangleCount: int,
    name: str,
    nodeState: int,
    smoothStrength: float,
    tessellateBorders: bool,
    useRelativeValues: bool,
    worldSpace: bool,
) -> Any:
    ...


def polyRetopo(
    *args: List[str],
    edit: bool,
    query: bool,
    anisotropy: float,
    caching: bool,
    constructionHistory: bool,
    curveInfluenceDirection: float,
    curveSingularitySeparation: float,
    featureTags: str,
    faceUniformity: float,
    frozen: bool,
    name: str,
    nodeState: int,
    preserveHardEdges: bool,
    preprocessMesh: bool,
    replaceOriginal: bool,
    targetEdgeDeviation: float,
    targetFaceCount: int,
    targetFaceCountTolerance: int,
    topologyRegularity: float,
) -> Any:
    ...


def polyRetopoCtx(*args, **kwargs) -> Any:
    ...


def polySelect(
    *args: List[str],
    query: bool,
    addFirst: bool,
    asSelectString: bool,
    edgeBorderPattern: List[Tuple[int, int]],
    deselect: bool,
    edgeBorder: List[int],
    edgeBorderPath: List[Tuple[int, int]],
    edgeLoop: List[int],
    edgeLoopOrBorder: List[int],
    edgeLoopPath: List[Tuple[int, int]],
    everyN: int,
    edgeRing: List[int],
    edgeRingPath: List[Tuple[int, int]],
    extendToShell: List[int],
    edgeUVLoopOrBorder: List[int],
    edgeLoopOrBorderPattern: List[Tuple[int, int]],
    edgeLoopPattern: List[Tuple[int, int]],
    noSelection: bool,
    replace: bool,
    edgeRingPattern: List[Tuple[int, int]],
    shortestEdgePath: List[Tuple[int, int]],
    shortestFacePath: List[Tuple[int, int]],
    shortestEdgePathUV: List[Tuple[int, int]],
    toggle: bool,
) -> Any:
    ...


def polySelectConstraint(
    query: bool,
    angle: int,
    anglebound: Tuple[float, float],
    anglePropagation: bool,
    angleTolerance: float,
    border: bool,
    borderPropagation: bool,
    convexity: int,
    crease: bool,
    dist: int,
    distaxis: Tuple[float, float, float],
    distbound: Tuple[float, float],
    disable: bool,
    distpoint: Tuple[float, float, float],
    edgeDistance: int,
    geometricarea: int,
    geometricareabound: Tuple[float, float],
    holes: int,
    length: int,
    lengthbound: Tuple[float, float],
    loopPropagation: bool,
    mode: int,
    max2dAngle: float,
    max3dAngle: float,
    nonmanifold: int,
    orient: int,
    orientaxis: Tuple[float, float, float],
    orientbound: Tuple[float, float],
    oppositeEdges: bool,
    order: int,
    orderbound: Tuple[int, int],
    planarity: int,
    propagate: int,
    random: int,
    ringPropagation: bool,
    randomratio: float,
    returnSelection: int,
    shell: bool,
    smoothness: int,
    stateString: bool,
    size: int,
    type: int,
    texturedarea: int,
    texturedareabound: Tuple[float, float],
    topology: int,
    textureshared: int,
    textured: int,
    uvBorderSelection: bool,
    uvFaceOrientation: int,
    uvEdgeLoopPropagation: bool,
    uvEdgeRingPropagation: bool,
    uvShell: bool,
    uvConstraint: bool,
    visibility: int,
    visibilityangle: float,
    visibilitypoint: Tuple[float, float, float],
    where: int,
    wholeSensitive: bool,
) -> Any:
    ...


def polySelectConstraintMonitor(*args, **kwargs) -> Any:
    ...


def polySelectCtx(*args, **kwargs) -> Any:
    ...


def polySelectEditCtx(*args, **kwargs) -> Any:
    ...


def polySelectEditCtxDataCmd(*args, **kwargs) -> Any:
    ...


def polySelectSp(*args: List[str], query: bool, loop: bool, ring: bool) -> Any:
    ...


def polySeparate(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    endFace: int,
    frozen: bool,
    inPlace: bool,
    name: str,
    nodeState: int,
    object: bool,
    removeShells: bool,
    startFace: int,
    separateSpecificShell: List[int],
    userSpecifiedShells: bool,
) -> Any:
    ...


def polySetToFaceNormal(*args: List[str], setUserNormal: bool) -> Any:
    ...


def polySetVertices() -> Any:
    ...


def polySewEdge(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    tolerance: float,
    texture: bool,
    worldSpace: bool,
) -> Any:
    ...


def polyShortestPathCtx(*args, **kwargs) -> Any:
    ...


def polySlideEdge(
    *args: List[str],
    absolute: bool,
    direction: int,
    edgeDirection: float,
    symmetry: bool,
) -> Any:
    ...


def polySlideEdgeCtx(*args, **kwargs) -> Any:
    ...


def polySmooth(
    *args: List[str],
    edit: bool,
    query: bool,
    boundaryRule: int,
    continuity: float,
    caching: bool,
    constructionHistory: bool,
    degree: int,
    divisionsPerEdge: int,
    divisions: int,
    frozen: bool,
    keepBorder: bool,
    keepHardEdge: bool,
    keepMapBorders: int,
    keepSelectionBorder: bool,
    keepTessellation: bool,
    method: int,
    name: str,
    nodeState: int,
    osdCreaseMethod: int,
    osdFvarBoundary: int,
    osdFvarPropagateCorners: bool,
    osdSmoothTriangles: bool,
    osdVertBoundary: int,
    propagateEdgeHardness: bool,
    pushStrength: float,
    roundness: float,
    subdivisionType: int,
    subdivisionLevels: int,
    smoothUVs: bool,
    keepTesselation: bool,
) -> Any:
    ...


def polySoftEdge(
    *args: List[str],
    edit: bool,
    query: bool,
    angle: float,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    worldSpace: bool,
) -> Any:
    ...


def polySphere(
    *args: List[str],
    edit: bool,
    query: bool,
    axis: Tuple[float, float, float],
    caching: bool,
    constructionHistory: bool,
    componentTagCreate: bool,
    createUVs: int,
    frozen: bool,
    heightBaseline: float,
    name: str,
    nodeState: int,
    object: bool,
    radius: float,
    subdivisionsAxis: int,
    subdivisionsHeight: int,
    subdivisionsX: int,
    subdivisionsY: int,
    texture: int,
) -> Any:
    ...


def polySphericalProjection(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    createNewMap: bool,
    frozen: bool,
    insertBeforeDeformers: bool,
    imageCenter: Tuple[float, float],
    imageCenterX: float,
    imageCenterY: float,
    imageScale: Tuple[float, float],
    imageScaleU: float,
    imageScaleV: float,
    keepImageRatio: bool,
    mapDirection: str,
    name: str,
    nodeState: int,
    projectionCenter: Tuple[float, float, float],
    projectionCenterX: float,
    projectionCenterY: float,
    projectionCenterZ: float,
    projectionHeight: float,
    projectionHorizontalSweep: float,
    perInstance: bool,
    projectionScale: Tuple[float, float],
    projectionScaleU: float,
    projectionScaleV: float,
    radius: float,
    rotationAngle: float,
    rotate: Tuple[float, float, float],
    rotateX: float,
    rotateY: float,
    rotateZ: float,
    seamCorrect: bool,
    smartFit: bool,
    worldSpace: bool,
) -> Any:
    ...


def polySpinEdge(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    offset: int,
    reverse: bool,
) -> Any:
    ...


def polySplit(
    *args: List[str],
    edit: bool,
    query: bool,
    adjustEdgeFlow: float,
    constructionHistory: bool,
    detachEdges: bool,
    edgepoint: List[Tuple[int, float]],
    facepoint: List[Tuple[int, float, float, float]],
    insertWithEdgeFlow: bool,
    insertpoint: List[Tuple[int, float, Incomplete, float, float, Incomplete]],
    name: str,
    projectedCurve: List[str],
    projectedCurveTolerance: float,
    subdivision: int,
    smoothingangle: float,
) -> Any:
    ...


def polySplitCtx(*args, **kwargs) -> Any:
    ...


def polySplitCtx2(*args, **kwargs) -> Any:
    ...


def polySplitEdge(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    operation: int,
) -> Any:
    ...


def polySplitRing(
    *args: List[str],
    edit: bool,
    query: bool,
    adjustEdgeFlow: float,
    caching: bool,
    constructionHistory: bool,
    divisions: int,
    direction: bool,
    enableProfileCurve: bool,
    useFaceNormalsAtEnds: bool,
    fixQuads: bool,
    frozen: bool,
    insertWithEdgeFlow: bool,
    name: str,
    nodeState: int,
    profileCurve_FloatValue: float,
    profileCurve_Interp: int,
    profileCurveInputOffset: float,
    profileCurveInputScale: float,
    profileCurve_Position: float,
    rootEdge: int,
    smoothingAngle: float,
    splitType: int,
    useEqualMultiplier: bool,
    worldSpace: bool,
    weight: float,
) -> Any:
    ...


def polySplitVertex(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    worldSpace: bool,
) -> Any:
    ...


def polyStraightenUVBorder(
    *args: List[str],
    edit: bool,
    query: bool,
    blendOriginal: float,
    curvature: float,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    gapTolerance: int,
    name: str,
    nodeState: int,
    preserveLength: float,
    uvSetName: str,
    worldSpace: bool,
) -> Any:
    ...


def polySubdivideEdge(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    divisions: int,
    frozen: bool,
    name: str,
    nodeState: int,
    size: float,
    worldSpace: bool,
) -> Any:
    ...


def polySubdivideFacet(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    divisionsU: int,
    divisions: int,
    divisionsV: int,
    frozen: bool,
    mode: int,
    name: str,
    nodeState: int,
    subdMethod: int,
) -> Any:
    ...


def polySuperCtx(*args, **kwargs) -> Any:
    ...


def polyTestPop(*args, **kwargs) -> Any:
    ...


def polyToCurve(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    addUnderTransform: bool,
    caching: bool,
    constructionHistory: bool,
    degree: int,
    displaySmoothMesh: int,
    form: int,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    conformToSmoothMeshPreview: bool,
) -> Any:
    ...


def polyToSubdiv(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    applyMatrixToResult: bool,
    absolutePosition: bool,
    addUnderTransform: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    maxEdgesPerVert: int,
    maxPolyCount: int,
    name: str,
    nodeState: int,
    object: bool,
    preserveVertexOrdering: bool,
    quickConvert: bool,
    uvPoints: List[Tuple[float, float]],
    uvTreatment: int,
    uvPointsU: float,
    uvPointsV: float,
) -> Any:
    ...


def polyTorus(
    *args: List[str],
    edit: bool,
    query: bool,
    axis: Tuple[float, float, float],
    caching: bool,
    constructionHistory: bool,
    componentTagCreate: bool,
    createUVs: bool,
    frozen: bool,
    heightBaseline: float,
    name: str,
    nodeState: int,
    object: bool,
    radius: float,
    subdivisionsAxis: int,
    subdivisionsHeight: int,
    sectionRadius: float,
    subdivisionsX: int,
    subdivisionsY: int,
    twist: float,
    texture: bool,
) -> Any:
    ...


def polyTransfer(
    *args: List[str],
    edit: bool,
    query: bool,
    alternateObject: str,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    uvSets: bool,
    vertices: bool,
    vertexColor: bool,
) -> Any:
    ...


def polyTriangulate(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
) -> Any:
    ...


def polyUVCoverage(*args: List[str], uvRange: Tuple[float, float, float, float]) -> Any:
    ...


def polyUVOverlap(
    *args: List[str], nonOverlappingComponents: bool, overlappingComponents: bool
) -> Any:
    ...


def polyUVRectangle(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
) -> Any:
    ...


def polyUVSet(
    *args: List[str],
    edit: bool,
    query: bool,
    allUVSets: bool,
    allUVSetsWithCount: bool,
    copy: bool,
    currentPerInstanceUVSet: bool,
    create: bool,
    currentUVSet: bool,
    delete: bool,
    genNewUVSet: bool,
    currentLastUVSet: bool,
    newUVSet: str,
    perInstance: bool,
    projections: bool,
    rename: bool,
    reorder: bool,
    shareInstances: bool,
    unshared: bool,
    allUVSetsIndices: bool,
    uvSet: str,
) -> Any:
    ...


def polyUVStackSimilarShells(
    *args: List[str], onlyMatch: bool, tolerance: float
) -> Any:
    ...


def polyUVStackSimilarShellsCmd(*args, **kwargs) -> Any:
    ...


def polyUnite(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    centerPivot: bool,
    frozen: bool,
    mergeUVSets: int,
    name: str,
    nodeState: int,
    object: bool,
    objectPivot: bool,
) -> Any:
    ...


def polyUniteSkinned(
    *args: List[str],
    edit: bool,
    query: bool,
    constructionHistory: bool,
    centerPivot: bool,
    mergeUVSets: int,
    objectPivot: bool,
) -> Any:
    ...


def polyVertexNormalCtx(*args, **kwargs) -> Any:
    ...


def polyWarpImage(
    *args: List[str],
    bilinear: bool,
    background: Tuple[int, int, int],
    fileFormat: str,
    inputName: str,
    inputUvSetName: str,
    noAlpha: bool,
    overwrite: bool,
    outputName: str,
    outputUvSetName: str,
    tiled: bool,
    xResolution: int,
    yResolution: int,
) -> Any:
    ...


def polyWedgeFace(
    *args: List[str],
    edit: bool,
    query: bool,
    axis: Tuple[float, float, float],
    axisX: float,
    axisY: float,
    axisZ: float,
    caching: bool,
    constructionHistory: bool,
    center: Tuple[float, float, float],
    centerX: float,
    centerY: float,
    centerZ: float,
    divisions: int,
    edge: List[int],
    frozen: bool,
    name: str,
    nodeState: int,
    wedgeAngle: float,
    worldSpace: bool,
) -> Any:
    ...


def popListItem() -> Any:
    ...


def popupMenu(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    altModifier: bool,
    allowOptionBoxes: bool,
    button: int,
    ctrlModifier: bool,
    deleteAllItems: bool,
    defineTemplate: str,
    exists: bool,
    itemArray: bool,
    markingMenu: bool,
    numberOfItems: bool,
    parent: str,
    postMenuCommand: Callable,
    postMenuCommandOnce: bool,
    shiftModifier: bool,
    useTemplate: str,
) -> Any:
    ...


def pose(
    *args: List[str], edit: bool, query: bool, apply: bool, allPoses: bool, name: str
) -> Any:
    ...


def poseEditor(*args, **kwargs) -> Any:
    ...


def poseInterpolator(
    *args: Tuple[str, str, Incomplete, Incomplete, Incomplete, Incomplete],
    edit: bool,
    query: bool,
    addPose: str,
    drivers: bool,
    deletePose: str,
    exportPoses: str,
    goToPose: str,
    index: bool,
    importPoses: str,
    kernelWidth: str,
    mirror: List[str],
    name: str,
    pose: List[Tuple[str, str]],
    poseNames: bool,
    rename: Tuple[str, str],
    searchAndReplace: Tuple[str, str],
    updatePose: str,
) -> Any:
    ...


def posePanel(*args, **kwargs) -> Any:
    ...


def preferredRenderer(
    arg0: str, /, query: bool, fallback: str, makeCurrent: bool
) -> Any:
    ...


def preloadRefEd(*args, **kwargs) -> Any:
    ...


def prepareRender(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    deregister: str,
    defaultTraversalSet: str,
    invokePostRenderFrame: bool,
    invokePostRenderLayer: bool,
    invokePostRender: bool,
    invokePreRenderFrame: bool,
    invokePreRenderLayer: bool,
    invokePreRender: bool,
    invokeSettingsUI: bool,
    label: str,
    listTraversalSets: bool,
    postRenderFrame: Callable,
    postRenderLayer: Callable,
    postRender: Callable,
    preRenderFrame: Callable,
    preRenderLayer: Callable,
    preRender: Callable,
    restore: bool,
    saveAssemblyConfig: bool,
    setup: bool,
    settingsUI: Callable,
    traversalSet: str,
    traversalSetInit: Callable,
) -> Any:
    ...


def prependListItem() -> Any:
    ...


def profiler(
    query: bool,
    addCategory: str,
    allCategories: bool,
    bufferSize: int,
    clearAllMelInstrumentation: bool,
    categoryInfo: str,
    categoryIndex: int,
    categoryIndexToName: int,
    categoryName: str,
    categoryNameToIndex: str,
    colorIndex: int,
    categoryRecording: bool,
    eventCount: bool,
    eventCategory: bool,
    eventCPUId: bool,
    eventColor: bool,
    eventDescription: bool,
    eventDuration: bool,
    eventIndex: int,
    eventName: bool,
    eventStartTime: bool,
    eventThreadId: bool,
    instrumentMel: bool,
    load: str,
    output: str,
    procedureDescription: str,
    procedureName: str,
    reset: bool,
    removeCategory: str,
    sampling: bool,
    signalEvent: bool,
    signalMelEvent: bool,
) -> Any:
    ...


def profilerTool(*args, **kwargs) -> Any:
    ...


def progressBar(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    beginProgress: bool,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    endProgress: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isCancelled: bool,
    isInterruptable: bool,
    isMainProgressBar: bool,
    isObscured: bool,
    manage: bool,
    maxValue: int,
    minValue: int,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    progress: int,
    step: int,
    statusBarMessage: str,
    status: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def progressWindow(
    edit: bool,
    query: bool,
    endProgress: bool,
    isCancelled: bool,
    isInterruptable: bool,
    maxValue: int,
    minValue: int,
    progress: int,
    step: int,
    status: str,
    title: str,
) -> Any:
    ...


def projectCurve(
    *args: Tuple[str, str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    direction: Tuple[float, float, float],
    directionX: float,
    directionY: float,
    directionZ: float,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    range: bool,
    tolerance: float,
    useNormal: bool,
) -> Any:
    ...


def projectTangent(
    *args: Tuple[str, str, str],
    edit: bool,
    query: bool,
    curvature: bool,
    caching: bool,
    constructionHistory: bool,
    curvatureScale: float,
    frozen: bool,
    ignoreEdges: bool,
    name: str,
    nodeState: int,
    object: bool,
    rotate: float,
    replaceOriginal: bool,
    reverseTangent: bool,
    tangentDirection: int,
    tangentScale: float,
) -> Any:
    ...


def projectionContext(*args, **kwargs) -> Any:
    ...


def projectionManip(query: bool, fitBBox: bool, projType: int, switchType: bool) -> Any:
    ...


def promptDialog(
    query: bool,
    button: List[str],
    backgroundColor: Tuple[float, float, float],
    cancelButton: str,
    defaultButton: str,
    dismissString: str,
    message: str,
    messageAlign: str,
    parent: str,
    scrollableField: bool,
    style: str,
    title: str,
    text: str,
) -> Any:
    ...


def propModCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    animCurve: str,
    animCurveFalloff: Tuple[float, float],
    animCurveParam: str,
    direction: Tuple[float, float, float],
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    linear: float,
    linearParam: Tuple[float, float],
    nurbsCurve: str,
    powerCutoff: float,
    powerCutoffParam: Tuple[float, float],
    powerDegree: float,
    powerDegreeParam: float,
    script: str,
    scriptParam: str,
    type: int,
    worldspace: bool,
) -> Any:
    ...


def propMove(
    *args: List[Incomplete],
    percent: List[float],
    pivot: Tuple[float, float, float],
    percentX: List[float],
    percentY: List[float],
    percentZ: List[float],
    rotate: Tuple[float, float, float],
    scale: Tuple[float, float, float],
    translate: Tuple[float, float, float],
    worldSpace: bool,
) -> Any:
    ...


def psdChannelOutliner(*args, **kwargs) -> Any:
    ...


def psdConvSolidTxOptions(*args, **kwargs) -> Any:
    ...


def psdEditTextureFile(*args, **kwargs) -> Any:
    ...


def psdExport(*args, **kwargs) -> Any:
    ...


def psdTextureFile(*args, **kwargs) -> Any:
    ...


def python() -> Any:
    ...


def querySubdiv(*args, **kwargs) -> Any:
    ...


def quit(abort: bool, exitCode: int, force: bool) -> Any:
    ...


def radial(
    *args: List[str],
    edit: bool,
    query: bool,
    attenuation: float,
    magnitude: float,
    maxDistance: float,
    name: str,
    position: List[Tuple[float, float, float]],
    perVertex: bool,
    torusSectionRadius: float,
    type: float,
    volumeExclusion: bool,
    volumeOffset: Tuple[float, float, float],
    volumeShape: str,
    volumeSweep: float,
) -> Any:
    ...


def radioButton(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    align: str,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    collection: str,
    data: int,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    editable: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    label: str,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    offCommand: Callable,
    onCommand: Callable,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    recomputeSize: bool,
    statusBarMessage: str,
    select: bool,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def radioButtonGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    annotation1: str,
    annotation2: str,
    annotation3: str,
    annotation4: str,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    changeCommand: Callable,
    changeCommand1: Callable,
    changeCommand2: Callable,
    changeCommand3: Callable,
    changeCommand4: Callable,
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    data1: int,
    data2: int,
    data3: int,
    data4: int,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    editable: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    enable1: bool,
    enable2: bool,
    enable3: bool,
    enable4: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    label: str,
    label1: str,
    label2: str,
    label3: str,
    label4: str,
    labelAnnotation: str,
    labelArray2: Tuple[str, str],
    labelArray3: Tuple[str, str, str],
    labelArray4: Tuple[str, str, str, str],
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    numberOfRadioButtons: int,
    offCommand1: Callable,
    offCommand2: Callable,
    offCommand3: Callable,
    offCommand4: Callable,
    offCommand: Callable,
    onCommand1: Callable,
    onCommand2: Callable,
    onCommand3: Callable,
    onCommand4: Callable,
    onCommand: Callable,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rowAttach: List[Tuple[int, str, int]],
    statusBarMessage: str,
    shareCollection: str,
    select: int,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    vertical: bool,
    width: int,
) -> Any:
    ...


def radioCollection(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    collectionItemArray: bool,
    defineTemplate: str,
    exists: bool,
    gl: bool,
    numberOfCollectionItems: bool,
    parent: str,
    select: str,
    useTemplate: str,
) -> Any:
    ...


def radioMenuItemCollection(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    defineTemplate: str,
    exists: bool,
    gl: bool,
    parent: str,
    useTemplate: str,
) -> Any:
    ...


def rampColorPort(*args, **kwargs) -> Any:
    ...


def rampWidget(*args, **kwargs) -> Any:
    ...


def rampWidgetAttrless(*args, **kwargs) -> Any:
    ...


def rangeControl(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    changedCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    maxRange: int,
    minRange: int,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
    widthHeight: Tuple[int, int],
) -> Any:
    ...


def readPDC(*args: List[str], file: str, test: bool) -> Any:
    ...


def readTake(*args, **kwargs) -> Any:
    ...


def rebuildCurve(
    *args: Tuple[str, str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    degree: int,
    endKnots: int,
    fitRebuild: bool,
    frozen: bool,
    keepControlPoints: bool,
    keepEndPoints: bool,
    keepRange: int,
    keepTangents: bool,
    name: str,
    noChanges: bool,
    nodeState: int,
    object: bool,
    range: bool,
    replaceOriginal: bool,
    rebuildType: int,
    spans: int,
    smartSurfaceCurveRebuild: bool,
    smooth: float,
    tolerance: float,
) -> Any:
    ...


def rebuildSurface(
    *args: Tuple[str, str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    direction: int,
    degreeU: int,
    degreeV: int,
    endKnots: int,
    fitRebuild: int,
    frozen: bool,
    keepCorners: bool,
    keepControlPoints: bool,
    keepRange: int,
    name: str,
    noChanges: bool,
    nodeState: int,
    object: bool,
    polygon: int,
    replaceOriginal: bool,
    rebuildType: int,
    spansU: int,
    spansV: int,
    tolerance: float,
) -> Any:
    ...


def recordAttr(
    *args: List[str], edit: bool, query: bool, attribute: List[str], delete: bool
) -> Any:
    ...


def recordDevice(*args, **kwargs) -> Any:
    ...


def redo() -> Any:
    ...


def reference(
    *args: List[str],
    query: bool,
    connectionsBroken: bool,
    connectionsMade: bool,
    dagPath: bool,
    editCommand: str,
    filename: str,
    isNodeReferenced: bool,
    longName: bool,
    node: str,
    referenceNode: str,
    shortName: bool,
) -> Any:
    ...


def referenceEdit(
    *args: List[str],
    applyFailedEdits: bool,
    changeEditTarget: Tuple[str, str],
    editCommand: List[str],
    failedEdits: bool,
    onReferenceNode: List[str],
    removeEdits: bool,
    successfulEdits: bool,
) -> Any:
    ...


def referenceQuery(
    *args: List[str],
    child: bool,
    dagPath: bool,
    editAttrs: bool,
    editCommand: List[str],
    editNodes: bool,
    editStrings: bool,
    filename: bool,
    failedEdits: bool,
    isExportEdits: bool,
    isLoaded: bool,
    isNodeReferenced: bool,
    isPreviewOnly: bool,
    liveEdits: bool,
    nodes: bool,
    namespace: bool,
    onReferenceNode: List[str],
    parent: bool,
    parentNamespace: bool,
    referenceNode: bool,
    successfulEdits: bool,
    showDagPath: bool,
    showFullPath: bool,
    shortName: bool,
    showNamespace: bool,
    topReference: bool,
    unresolvedName: bool,
    withoutCopyNumber: bool,
) -> Any:
    ...


def refineSubdivSelectionList(*args, **kwargs) -> Any:
    ...


def refresh(
    currentView: bool, force: bool, fileExtension: str, filename: str, suspend: bool
) -> Any:
    ...


def refreshEditorTemplates() -> Any:
    ...


def regionSelectKeyCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    bottomManip: float,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    leftManip: float,
    name: str,
    rightManip: float,
    topManip: float,
) -> Any:
    ...


def rehash() -> Any:
    ...


def relationship(
    *args: List[Incomplete],
    edit: bool,
    query: bool,
    b: bool,
    relationshipData: List[str],
) -> Any:
    ...


def reloadImage() -> Any:
    ...


def rememberCtxSettings() -> Any:
    ...


def removeJoint() -> Any:
    ...


def removeListItem() -> Any:
    ...


def removeMultiInstance(arg0: str, /, allChildren: bool, b: bool) -> Any:
    ...


def rename(*args: Tuple[str, str], ignoreShape: bool, uuid: bool) -> Any:
    ...


def renameAttr() -> Any:
    ...


def renameUI() -> Any:
    ...


def render(
    *args: Tuple[str, str, Incomplete, Incomplete, Incomplete, Incomplete],
    abortMissingTexture: bool,
    batch: bool,
    keepPreImage: bool,
    layer: str,
    nglowpass: bool,
    nshadows: bool,
    replace: bool,
    xresolution: int,
    yresolution: int,
) -> Any:
    ...


def renderGlobalsNode(
    arg0: str,
    /,
    name: str,
    parent: str,
    renderQuality: str,
    renderResolution: str,
    shared: bool,
    skipSelect: bool,
) -> Any:
    ...


def renderInfo(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    chordHeight: float,
    chordHeightRatio: float,
    castShadows: bool,
    doubleSided: bool,
    edgeSwap: bool,
    minScreen: float,
    name: str,
    opposite: bool,
    smoothShading: bool,
    useChordHeight: bool,
    useChordHeightRatio: bool,
    useDefaultLights: bool,
    useMinScreen: bool,
    unum: int,
    utype: int,
    vnum: int,
    vtype: int,
) -> Any:
    ...


def renderLayerMembers() -> Any:
    ...


def renderLayerPostProcess(query: bool, keepImages: bool, sceneName: str) -> Any:
    ...


def renderManip(
    *args: List[str],
    edit: bool,
    query: bool,
    camera: Tuple[bool, bool, bool, bool, bool],
    light: Tuple[bool, bool, bool],
    spotLight: Tuple[bool, bool, bool, bool, bool, bool, bool],
    state: bool,
) -> Any:
    ...


def renderPartition(arg0: Incomplete, /, query: bool) -> Any:
    ...


def renderPassRegistry(
    channels: int,
    isPassSupported: bool,
    passID: str,
    passName: bool,
    supportedPassSemantics: bool,
    renderer: str,
    supportedChannelCounts: bool,
    supportedDataTypes: bool,
    supportedRenderPassNames: bool,
    supportedRenderPasses: bool,
) -> Any:
    ...


def renderQualityNode(
    arg0: str, /, name: str, parent: str, shared: bool, skipSelect: bool
) -> Any:
    ...


def renderSettings(*args, **kwargs) -> Any:
    ...


def renderSetup(query: bool, renderLayers: bool) -> Any:
    ...


def renderSetupFind() -> Any:
    ...


def renderSetupLegacyLayer() -> Any:
    ...


def renderSetupLocalOverride(query: bool, state: bool) -> Any:
    ...


def renderSetupPostApply() -> Any:
    ...


def renderSetupSwitchVisibleRenderLayer() -> Any:
    ...


def renderThumbnailUpdate(*args, **kwargs) -> Any:
    ...


def renderWindowEditor(*args, **kwargs) -> Any:
    ...


def renderWindowSelectContext(*args, **kwargs) -> Any:
    ...


def renderer(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    addGlobalsNode: str,
    addGlobalsTab: Tuple[str, str, str],
    namesOfAvailableRenderers: bool,
    batchRenderProcedure: str,
    showBatchRenderLogProcedure: str,
    batchRenderOptionsProcedure: str,
    batchRenderOptionsStringProcedure: str,
    cancelBatchRenderProcedure: str,
    changeIprRegionProcedure: str,
    commandRenderProcedure: str,
    exists: bool,
    globalsNodes: bool,
    globalsTabCreateProcNames: bool,
    globalsTabLabels: bool,
    globalsTabUpdateProcNames: bool,
    iprOptionsProcedure: str,
    iprOptionsMenuLabel: str,
    iprRenderProcedure: str,
    iprOptionsSubMenuProcedure: str,
    iprRenderSubMenuProcedure: str,
    isRunningIprProcedure: str,
    logoCallbackProcedure: str,
    logoImageName: str,
    materialViewRendererList: bool,
    materialViewRendererPause: bool,
    materialViewRendererSuspend: bool,
    polyPrelightProcedure: str,
    pauseIprRenderProcedure: str,
    renderProcedure: str,
    renderDiagnosticsProcedure: str,
    renderingEditorsSubMenuProcedure: str,
    refreshIprRenderProcedure: str,
    renderGlobalsProcedure: str,
    renderMenuProcedure: str,
    renderOptionsProcedure: str,
    renderRegionProcedure: str,
    renderSequenceProcedure: str,
    showBatchRenderProcedure: str,
    supportColorManagement: bool,
    stopIprRenderProcedure: str,
    showRenderLogProcedure: str,
    startIprRenderProcedure: str,
    textureBakingProcedure: str,
    rendererUIName: str,
    unregisterRenderer: bool,
) -> Any:
    ...


def reorder(*args: List[str], back: bool, front: bool, relative: int) -> Any:
    ...


def reorderContainer(
    *args: List[str], edit: bool, query: bool, back: bool, front: bool, relative: int
) -> Any:
    ...


def reorderDeformers(*args: List[Incomplete], name: str) -> Any:
    ...


def repeatLast(
    edit: bool,
    query: bool,
    addCommand: str,
    addCommandLabel: str,
    commandList: int,
    commandNameList: int,
    historyLimit: int,
    item: int,
    numberOfHistoryItems: bool,
) -> Any:
    ...


def replaceCacheFrames() -> Any:
    ...


def replaceCacheFramesOpt() -> Any:
    ...


def requires(*args: Tuple[str, str], dataType: List[str], nodeType: List[str]) -> Any:
    ...


def reroot() -> Any:
    ...


def resampleFluid(
    *args: List[str],
    edit: bool,
    query: bool,
    resampleDepth: int,
    resampleHeight: int,
    resampleWidth: int,
) -> Any:
    ...


def resetTool() -> Any:
    ...


def resolutionNode(
    arg0: str, /, name: str, parent: str, shared: bool, skipSelect: bool
) -> Any:
    ...


def resourceManager(nameFilter: str, saveAs: Tuple[str, str]) -> Any:
    ...


def retimeHelper(
    edit: bool,
    query: bool,
    deleteFrame: int,
    frame: float,
    lockBar: Tuple[int, int],
    locks: int,
    moveFrame: Tuple[int, float],
    mouseOver: bool,
) -> Any:
    ...


def retimeKeyCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    moveByFrame: int,
    name: str,
    snapOnFrame: bool,
) -> Any:
    ...


def reverseCurve(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    curveOnSurface: bool,
    frozen: bool,
    name: str,
    noChanges: bool,
    nodeState: int,
    object: bool,
    range: bool,
    replaceOriginal: bool,
) -> Any:
    ...


def reverseSurface(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    direction: int,
    frozen: bool,
    name: str,
    noChanges: bool,
    nodeState: int,
    object: bool,
    replaceOriginal: bool,
) -> Any:
    ...


def revolve(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    autoCorrectNormal: bool,
    axisChoice: int,
    axis: Tuple[float, float, float],
    axisX: float,
    axisY: float,
    axisZ: float,
    bridge: bool,
    caching: bool,
    constructionHistory: bool,
    computePivotAndAxis: int,
    degree: int,
    endSweep: float,
    frozen: bool,
    mergeItems: bool,
    name: str,
    nodeState: int,
    object: bool,
    pivot: Tuple[float, float, float],
    polygon: int,
    pivotX: float,
    pivotY: float,
    pivotZ: float,
    radius: float,
    radiusAnchor: float,
    rebuild: bool,
    range: bool,
    sections: int,
    startSweep: float,
    tolerance: float,
    useLocalPivot: bool,
    useTolerance: bool,
) -> Any:
    ...


def rigidBody(
    *args: List[str],
    edit: bool,
    query: bool,
    active: bool,
    applyForceAt: str,
    angularVelocity: bool,
    bounciness: float,
    cache: bool,
    contactCount: bool,
    collisions: bool,
    contactName: bool,
    centerOfMass: Tuple[float, float, float],
    contactPosition: bool,
    deleteCache: bool,
    dynamicFriction: float,
    damping: float,
    force: bool,
    impulse: Tuple[float, float, float],
    initialAngularVelocity: Tuple[float, float, float],
    ignore: bool,
    impulsePosition: Tuple[float, float, float],
    initialVelocity: Tuple[float, float, float],
    layer: int,
    lockCenterOfMass: bool,
    mass: float,
    name: str,
    orientation: Tuple[float, float, float],
    position: Tuple[float, float, float],
    passive: bool,
    particleCollision: bool,
    removeShape: str,
    staticFriction: float,
    spinImpulse: Tuple[float, float, float],
    standInObject: str,
    solver: str,
    tesselationFactor: int,
    velocity: bool,
) -> Any:
    ...


def rigidSolver(
    *args: List[str],
    edit: bool,
    query: bool,
    autoTolerances: bool,
    bounciness: bool,
    collide: bool,
    cacheData: bool,
    create: bool,
    collisionTolerance: float,
    contactData: bool,
    current: bool,
    dynamics: bool,
    displayConstraint: bool,
    displayCenterOfMass: bool,
    deleteCache: bool,
    displayVelocity: bool,
    friction: bool,
    interpenetrate: bool,
    interpenetrationCheck: bool,
    name: str,
    rigidBodies: bool,
    rigidBodyCount: bool,
    stepSize: float,
    showCollision: bool,
    showInterpenetration: bool,
    solverMethod: int,
    state: bool,
    statistics: bool,
    startTime: float,
    velocityVectorScale: float,
) -> Any:
    ...


def roll(arg0: str, /, absolute: bool, degree: float, relative: bool) -> Any:
    ...


def rollCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    alternateContext: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
    rollScale: float,
    toolName: str,
) -> Any:
    ...


def rotate(
    *args: List[Incomplete],
    absolute: bool,
    centerPivot: bool,
    componentSpace: bool,
    deletePriorHistory: bool,
    euler: bool,
    forceOrderXYZ: bool,
    orientAxes: Tuple[float, float, float],
    objectCenterPivot: bool,
    objectSpace: bool,
    pivot: Tuple[float, float, float],
    preserveChildPosition: bool,
    preserveGeometryPosition: bool,
    preserveUV: bool,
    relative: bool,
    reflectionAboutBBox: bool,
    reflectionAboutOrigin: bool,
    reflectionAboutX: bool,
    reflectionAboutY: bool,
    reflectionAboutZ: bool,
    reflection: bool,
    reflectionTolerance: float,
    symNegative: bool,
    translate: bool,
    worldSpace: bool,
    rotateX: bool,
    xformConstraint: str,
    constrainAlongNormal: bool,
    rotateXY: bool,
    rotateXYZ: bool,
    rotateXZ: bool,
    rotateY: bool,
    rotateYZ: bool,
    rotateZ: bool,
) -> Any:
    ...


def rotationInterpolation(*args: List[str], query: bool, convert: str) -> Any:
    ...


def roundCRCtx(*args, **kwargs) -> Any:
    ...


def roundConstantRadius(
    *args: List[Incomplete],
    edit: bool,
    query: bool,
    append: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    radius: List[float],
    radiuss: List[float],
    side: List[Tuple[str, int]],
    sidea: List[int],
    sideb: List[int],
    tolerance: float,
) -> Any:
    ...


def rowColumnLayout(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn: int,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    childArray: bool,
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    columnOffset: List[Tuple[int, str, int]],
    columnSpacing: List[Tuple[int, int]],
    columnWidth: List[Tuple[int, int]],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfColumns: int,
    numberOfChildren: bool,
    numberOfPopupMenus: bool,
    numberOfRows: int,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rowAlign: List[Tuple[int, str]],
    rowAttach: List[Tuple[int, str, int]],
    rowHeight: List[Tuple[int, int]],
    rowOffset: List[Tuple[int, str, int]],
    rowSpacing: List[Tuple[int, int]],
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def rowLayout(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn1: int,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    childArray: bool,
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    columnAlign1: str,
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    columnOffset1: int,
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach1: str,
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfColumns: int,
    numberOfChildren: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rowAttach: List[Tuple[int, str, int]],
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def runTimeCommand(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    addKeyword: List[str],
    annotation: str,
    addTag: List[str],
    command: Callable,
    commandArray: bool,
    categoryArray: bool,
    category: str,
    commandLanguage: str,
    default: bool,
    defaultCommandArray: bool,
    delete: bool,
    exists: bool,
    hotkeyCtx: str,
    image: str,
    keywords: str,
    label: str,
    longAnnotation: str,
    numberOfCommands: bool,
    numberOfDefaultCommands: bool,
    numberOfUserCommands: bool,
    plugin: str,
    save: bool,
    showInHotkeyEditor: bool,
    tags: str,
    userCommandArray: bool,
    helpUrl: str,
) -> Any:
    ...


def runup(
    cache: bool,
    fromPreviousFrame: bool,
    fromStartFrame: bool,
    maxFrame: int,
    state: bool,
) -> Any:
    ...


def safemodecheckhash() -> Any:
    ...


def sampleImage(*args, **kwargs) -> Any:
    ...


def saveAllShelves() -> Any:
    ...


def saveFluid(
    *args: List[str],
    edit: bool,
    query: bool,
    currentTime: int,
    endTime: int,
    startTime: int,
) -> Any:
    ...


def saveImage(*args, **kwargs) -> Any:
    ...


def saveInitialState(*args: List[str], saveall: bool, attribute: List[str]) -> Any:
    ...


def saveMenu() -> Any:
    ...


def savePrefObjects() -> Any:
    ...


def saveShelf() -> Any:
    ...


def saveToolSettings() -> Any:
    ...


def saveViewportSettings() -> Any:
    ...


def scale(
    *args: List[Incomplete],
    absolute: bool,
    centerPivot: bool,
    componentSpace: bool,
    deletePriorHistory: bool,
    distanceOnly: bool,
    localSpace: bool,
    orientAxes: Tuple[float, float, float],
    objectCenterPivot: bool,
    objectSpace: bool,
    pivot: Tuple[float, float, float],
    preserveChildPosition: bool,
    preserveGeometryPosition: bool,
    preserveUV: bool,
    relative: bool,
    reflectionAboutBBox: bool,
    reflectionAboutOrigin: bool,
    reflectionAboutX: bool,
    reflectionAboutY: bool,
    reflectionAboutZ: bool,
    reflection: bool,
    reflectionTolerance: float,
    symNegative: bool,
    worldSpace: bool,
    scaleX: bool,
    xformConstraint: str,
    constrainAlongNormal: bool,
    scaleXY: bool,
    scaleXYZ: bool,
    scaleXZ: bool,
    scaleY: bool,
    scaleYZ: bool,
    scaleZ: bool,
) -> Any:
    ...


def scaleComponents(
    *args: List[Incomplete],
    pivot: Tuple[float, float, float],
    rotation: Tuple[float, float, float],
) -> Any:
    ...


def scaleConstraint(
    *args: List[str],
    edit: bool,
    query: bool,
    layer: str,
    maintainOffset: bool,
    name: str,
    offset: Tuple[float, float, float],
    remove: bool,
    scaleCompensate: bool,
    skip: List[str],
    targetList: bool,
    weight: float,
    weightAliasList: bool,
) -> Any:
    ...


def scaleKey(
    *args: List[str],
    animation: str,
    autoSnap: bool,
    attribute: List[str],
    controlPoints: bool,
    float: List[Incomplete],
    floatPivot: float,
    floatScale: float,
    hierarchy: str,
    index: List[Incomplete],
    includeUpperBound: bool,
    newEndFloat: float,
    newEndTime: int,
    newStartFloat: float,
    newStartTime: int,
    shape: bool,
    scaleSpecifiedKeys: bool,
    time: List[Incomplete],
    timePivot: int,
    timeScale: float,
    valuePivot: float,
    valueScale: float,
) -> Any:
    ...


def scaleKeyCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
    scaleSpecifiedKeys: bool,
    type: str,
) -> Any:
    ...


def sceneEditor(*args, **kwargs) -> Any:
    ...


def sceneLint(*args, **kwargs) -> Any:
    ...


def sceneUIReplacement(
    clear: bool,
    deleteRemaining: bool,
    getNextFilter: Tuple[str, str],
    getNextPanel: Tuple[str, str],
    getNextScriptedPanel: Tuple[str, str],
    update: str,
) -> Any:
    ...


def scmh(
    *args: List[Incomplete],
    absolute: bool,
    ignore: List[int],
    quiet: bool,
    relative: bool,
) -> Any:
    ...


def scriptCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    animBreakdown: List[bool],
    animCurve: List[bool],
    animInTangent: List[bool],
    animKeyframe: List[bool],
    allComponents: List[bool],
    allObjects: List[bool],
    animOutTangent: List[bool],
    baseClassName: str,
    byName: List[Tuple[str, int]],
    curve: List[bool],
    camera: List[bool],
    history: bool,
    curveKnot: List[bool],
    cluster: List[bool],
    collisionModel: List[bool],
    cumulativeLists: bool,
    curveOnSurface: List[bool],
    curveParameterPoint: List[bool],
    controlVertex: List[bool],
    dynamicConstraint: List[bool],
    dimension: List[bool],
    setDoneSelectionPrompt: List[str],
    edge: List[bool],
    emitter: List[bool],
    editPoint: List[bool],
    enableRootSelection: bool,
    escToQuit: bool,
    expandSelectionList: bool,
    exitUponCompletion: bool,
    exists: bool,
    forceAddSelect: bool,
    facet: List[bool],
    finalCommandScript: Callable,
    field: List[bool],
    fluid: List[bool],
    follicle: List[bool],
    handle: List[bool],
    hull: List[bool],
    hairSystem: List[bool],
    image1: str,
    image2: str,
    image3: str,
    ikEndEffector: List[bool],
    implicitGeometry: List[bool],
    ignoreInvalidItems: bool,
    ikHandle: List[bool],
    imagePlane: List[bool],
    isoparm: List[bool],
    joint: List[bool],
    jointPivot: List[bool],
    lattice: List[bool],
    lastAutoComplete: bool,
    locator: List[bool],
    latticePoint: List[bool],
    light: List[bool],
    locatorUV: List[bool],
    meshComponents: List[bool],
    meshUVShell: List[bool],
    motionTrailPoint: List[bool],
    motionTrailTangent: List[bool],
    name: str,
    nurbsCurve: List[bool],
    nCloth: List[bool],
    nonlinear: List[bool],
    nParticle: List[bool],
    nParticleShape: List[bool],
    nRigid: List[bool],
    nurbsSurface: List[bool],
    objectComponent: bool,
    orientationLocator: List[bool],
    polymesh: List[bool],
    polymeshEdge: List[bool],
    polymeshFace: List[bool],
    polymeshFreeEdge: List[bool],
    plane: List[bool],
    particle: List[bool],
    particleShape: List[bool],
    polymeshUV: List[bool],
    polymeshVertex: List[bool],
    polymeshVtxFace: List[bool],
    queryByName: str,
    localRotationAxis: List[bool],
    rigidBody: List[bool],
    rigidConstraint: List[bool],
    rotatePivot: List[bool],
    setAutoComplete: List[bool],
    setAllowExcessCount: List[bool],
    setAutoToggleSelection: List[bool],
    sculpt: List[bool],
    subdiv: List[bool],
    surfaceEdge: List[bool],
    surfaceFace: List[bool],
    selectHandle: List[bool],
    surfaceKnot: List[bool],
    showManipulators: bool,
    subdivMeshEdge: List[bool],
    subdivMeshFace: List[bool],
    subdivMeshPoint: List[bool],
    subdivMeshUV: List[bool],
    setNoSelectionHeadsUp: List[str],
    setNoSelectionPrompt: List[str],
    scalePivot: List[bool],
    springComponent: List[bool],
    surfaceParameterPoint: List[bool],
    spring: List[bool],
    surfaceRange: List[bool],
    setSelectionCount: List[int],
    setSelectionHeadsUp: List[str],
    setSelectionPrompt: List[str],
    stroke: List[bool],
    surfaceUV: List[bool],
    title: str,
    toolCursorType: str,
    toolFinish: Callable,
    toolStart: Callable,
    totalSelectionSets: int,
    texture: List[bool],
    vertex: List[bool],
    locatorXYZ: List[bool],
) -> Any:
    ...


def scriptEditorInfo(
    edit: bool,
    query: bool,
    clearHistory: bool,
    clearHistoryFile: bool,
    historyFilename: str,
    input: str,
    suppressErrors: bool,
    suppressInfo: bool,
    suppressResults: bool,
    suppressStackWindow: bool,
    suppressWarnings: bool,
    writeHistory: bool,
) -> Any:
    ...


def scriptJob(
    attributeAdded: Tuple[str, Callable],
    attributeChange: Tuple[str, Callable],
    attributeDeleted: Tuple[str, Callable],
    allChildren: bool,
    conditionChange: Tuple[str, Callable],
    conditionFalse: Tuple[str, Callable],
    connectionChange: Tuple[str, Callable],
    conditionTrue: Tuple[str, Callable],
    compressUndo: bool,
    disregardIndex: bool,
    event: Tuple[str, Callable],
    exists: int,
    force: bool,
    idleEvent: Callable,
    kill: List[int],
    killAll: bool,
    killWithScene: bool,
    listConditions: bool,
    listEvents: bool,
    listJobs: bool,
    nodeDeleted: Tuple[str, Callable],
    nodeNameChanged: Tuple[str, Callable],
    optionVarChanged: Tuple[str, Callable],
    parent: str,
    permanent: bool,
    protected: bool,
    runOnce: bool,
    replacePrevious: bool,
    timeChange: Callable,
    uiDeleted: Tuple[str, Callable],
) -> Any:
    ...


def scriptNode(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    afterScript: str,
    beforeScript: str,
    executeAfter: bool,
    executeBefore: bool,
    ignoreReferenceEdits: bool,
    name: str,
    scriptType: int,
    sourceType: str,
) -> Any:
    ...


def scriptTable(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    afterCellChangedCmd: Callable,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    columns: int,
    cellBackgroundColorCommand: Callable,
    cellChangedCmd: Callable,
    columnFilter: Tuple[int, str],
    cellForegroundColorCommand: Callable,
    cellIndex: Tuple[int, int],
    clearRow: int,
    clearTable: bool,
    cellValue: str,
    columnWidth: List[Tuple[int, int]],
    dragCallback: Callable,
    dropCallback: Callable,
    deleteRow: int,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    editable: bool,
    excludingHeaders: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    getCellCmd: Callable,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    insertRow: int,
    label: List[Tuple[int, str]],
    manage: bool,
    multiEditEnabled: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rows: int,
    rowHeight: int,
    rowsRemovedCmd: Callable,
    rowsToBeRemovedCmd: Callable,
    selectionBehavior: int,
    statusBarMessage: str,
    selectedCells: Incomplete,
    selectionChangedCmd: Callable,
    selectedColumns: Incomplete,
    sortEnabled: bool,
    selectionMode: int,
    selectedRow: bool,
    selectedRows: Incomplete,
    useDoubleClickEdit: bool,
    underPointerColumn: bool,
    underPointerRow: bool,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def scriptedPanel(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    copy: str,
    createString: bool,
    control: bool,
    defineTemplate: str,
    docTag: str,
    editString: bool,
    exists: bool,
    init: bool,
    isUnique: bool,
    label: str,
    menuBarVisible: bool,
    menuBarRepeatLast: bool,
    needsInit: bool,
    parent: str,
    popupMenuProcedure: Callable,
    replacePanel: str,
    tearOff: bool,
    tearOffCopy: str,
    tearOffRestore: bool,
    type: str,
    unParent: bool,
    useTemplate: str,
) -> Any:
    ...


def scriptedPanelType(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    addCallback: str,
    createCallback: str,
    customView: bool,
    deleteCallback: str,
    defineTemplate: str,
    exists: bool,
    hotkeyCtxClient: str,
    initCallback: str,
    label: str,
    obsolete: bool,
    copyStateCallback: str,
    removeCallback: str,
    retainOnFileOpen: bool,
    saveStateCallback: str,
    unique: bool,
    useTemplate: str,
) -> Any:
    ...


def scrollField(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    command: str,
    changeCommand: Callable,
    clear: bool,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enterCommand: Callable,
    editable: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    font: str,
    fontPointSize: int,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    insertionPosition: int,
    insertText: str,
    keyPressCommand: Callable,
    manage: bool,
    noBackground: bool,
    numberOfLines: int,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    selection: bool,
    text: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
    wordWrap: bool,
) -> Any:
    ...


def scrollLayout(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    borderVisible: bool,
    childArray: bool,
    childResizable: bool,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    horizontalScrollBarThickness: int,
    isObscured: bool,
    manage: bool,
    minChildWidth: int,
    noBackground: bool,
    numberOfChildren: bool,
    numberOfPopupMenus: bool,
    parent: str,
    panEnabled: bool,
    popupMenuArray: bool,
    preventOverride: bool,
    resizeCommand: Callable,
    scrollAreaHeight: bool,
    scrollAreaValue: bool,
    scrollAreaWidth: bool,
    statusBarMessage: str,
    scrollByPixel: Tuple[str, int],
    scrollPage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    verticalScrollBarAlwaysVisible: bool,
    verticalScrollBarThickness: int,
    width: int,
) -> Any:
    ...


def sculpt(
    *args: List[str],
    edit: bool,
    query: bool,
    after: bool,
    afterReference: bool,
    before: bool,
    components: bool,
    selectedComponents: bool,
    dropoffDistance: float,
    dropoffType: str,
    deformerTools: bool,
    exclusive: str,
    frontOfChain: bool,
    geometry: List[str],
    geometryIndices: bool,
    groupWithLocator: bool,
    includeHiddenSelections: bool,
    insideMode: str,
    ignoreSelected: bool,
    mode: str,
    maxDisplacement: float,
    name: str,
    objectCentered: bool,
    parallel: bool,
    prune: bool,
    remove: List[bool],
    split: bool,
    sculptTool: str,
    useComponentTags: bool,
) -> Any:
    ...


def sculptMeshCacheChangeCloneSource(*args, **kwargs) -> Any:
    ...


def sculptMeshCacheCtx(*args, **kwargs) -> Any:
    ...


def sculptTarget(
    *args: List[str],
    edit: bool,
    query: bool,
    after: bool,
    afterReference: bool,
    before: bool,
    components: bool,
    selectedComponents: bool,
    deformerTools: bool,
    exclusive: str,
    frontOfChain: bool,
    geometry: List[str],
    geometryIndices: bool,
    inbetweenWeight: float,
    includeHiddenSelections: bool,
    ignoreSelected: bool,
    name: str,
    parallel: bool,
    prune: bool,
    regenerate: bool,
    remove: List[bool],
    snapshot: int,
    split: bool,
    target: int,
    useComponentTags: bool,
) -> Any:
    ...


def selLoadSettings(
    *args: List[str],
    edit: bool,
    query: bool,
    activeProxy: str,
    deferReference: bool,
    fileName: str,
    numSettings: int,
    proxyManager: str,
    proxySetFiles: str,
    proxySetTags: str,
    proxyTag: str,
    referenceNode: str,
    shortName: bool,
    unresolvedName: bool,
) -> Any:
    ...


def select(
    *args: List[str],
    allDependencyNodes: bool,
    allDagObjects: bool,
    addFirst: bool,
    containerCentric: bool,
    clear: bool,
    deselect: bool,
    hierarchy: bool,
    noExpand: bool,
    replace: bool,
    symmetry: bool,
    symmetrySide: int,
    toggle: bool,
    visible: bool,
) -> Any:
    ...


def selectContext(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def selectKey(
    *args: List[str],
    addTo: bool,
    animation: str,
    attribute: List[str],
    clear: bool,
    controlPoints: bool,
    float: List[Incomplete],
    hierarchy: str,
    index: List[Incomplete],
    inTangent: bool,
    includeUpperBound: bool,
    keyframe: bool,
    outTangent: bool,
    replace: bool,
    remove: bool,
    shape: bool,
    time: List[Incomplete],
    toggle: bool,
    unsnappedKeys: float,
) -> Any:
    ...


def selectKeyCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def selectKeyframe(
    *args: List[str],
    animation: str,
    attribute: List[str],
    controlPoints: bool,
    float: List[Incomplete],
    hierarchy: str,
    index: List[Incomplete],
    includeUpperBound: bool,
    shape: bool,
    selectionWindow: Tuple[float, float, float, float],
    time: List[Incomplete],
) -> Any:
    ...


def selectKeyframeRegionCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def selectMode(
    query: bool,
    component: bool,
    hierarchical: bool,
    leaf: bool,
    object: bool,
    preset: bool,
    root: bool,
    template: bool,
) -> Any:
    ...


def selectPref(
    query: bool,
    affectsActive: bool,
    allowHiliteSelection: bool,
    autoSelectContainer: bool,
    autoSelectOutlinerSetMembers: bool,
    autoUseDepth: bool,
    clickBoxSize: int,
    containerCentricSelection: bool,
    clickDrag: bool,
    disableComponentPopups: bool,
    expandPopupList: bool,
    ignoreSelectionPriority: bool,
    manipClickBoxSize: int,
    preSelectDeadSpace: int,
    preSelectTweakDeadSpace: int,
    preSelectHiliteSize: float,
    popupMenuSelection: bool,
    paintSelect: bool,
    preSelectBackfacing: bool,
    preSelectClosest: bool,
    paintSelectWithDepth: bool,
    paintSelectRefine: bool,
    preSelectHilite: bool,
    preSelectSize: int,
    singleBoxSelection: bool,
    selectionChildHighlightMode: int,
    straightLineDistance: bool,
    selectTypeChangeAffectsActive: bool,
    trackSelectionOrder: bool,
    useDepth: bool,
    xformNoSelect: bool,
) -> Any:
    ...


def selectPriority(
    query: bool,
    animBreakdown: int,
    animCurve: int,
    animInTangent: int,
    animKeyframe: int,
    allComponents: int,
    allObjects: int,
    animOutTangent: int,
    byName: List[Tuple[str, int]],
    curve: int,
    camera: int,
    curveKnot: int,
    cluster: int,
    collisionModel: int,
    curveOnSurface: int,
    curveParameterPoint: int,
    controlVertex: int,
    dynamicConstraint: int,
    dimension: int,
    edge: int,
    emitter: int,
    editPoint: int,
    facet: int,
    field: int,
    fluid: int,
    follicle: int,
    handle: int,
    hull: int,
    hairSystem: int,
    ikEndEffector: int,
    implicitGeometry: int,
    ikHandle: int,
    imagePlane: int,
    isoparm: int,
    joint: int,
    jointPivot: int,
    lattice: int,
    locator: int,
    latticePoint: int,
    light: int,
    locatorUV: int,
    meshUVShell: int,
    motionTrailPoint: int,
    motionTrailTangent: int,
    nurbsCurve: int,
    nCloth: int,
    nonlinear: int,
    nParticle: int,
    nParticleShape: int,
    nRigid: int,
    nurbsSurface: int,
    orientationLocator: int,
    polymesh: int,
    polymeshEdge: int,
    polymeshFace: int,
    polymeshFreeEdge: int,
    plane: int,
    particle: int,
    particleShape: int,
    polymeshUV: int,
    polymeshVertex: int,
    polymeshVtxFace: int,
    queryByName: str,
    localRotationAxis: int,
    rigidBody: int,
    rigidConstraint: int,
    rotatePivot: int,
    sculpt: int,
    subdiv: int,
    surfaceEdge: int,
    surfaceFace: int,
    selectHandle: int,
    surfaceKnot: int,
    subdivMeshEdge: int,
    subdivMeshFace: int,
    subdivMeshPoint: int,
    subdivMeshUV: int,
    scalePivot: int,
    springComponent: int,
    surfaceParameterPoint: int,
    spring: int,
    surfaceRange: int,
    stroke: int,
    texture: int,
    vertex: int,
    locatorXYZ: int,
) -> Any:
    ...


def selectType(
    query: bool,
    animBreakdown: bool,
    animCurve: bool,
    animInTangent: bool,
    animKeyframe: bool,
    allComponents: bool,
    allObjects: bool,
    animOutTangent: bool,
    byName: List[Tuple[str, int]],
    curve: bool,
    camera: bool,
    curveKnot: bool,
    cluster: bool,
    collisionModel: bool,
    curveOnSurface: bool,
    curveParameterPoint: bool,
    controlVertex: bool,
    dynamicConstraint: bool,
    dimension: bool,
    edge: bool,
    emitter: bool,
    editPoint: bool,
    facet: bool,
    field: bool,
    fluid: bool,
    follicle: bool,
    handle: bool,
    hull: bool,
    hairSystem: bool,
    ikEndEffector: bool,
    implicitGeometry: bool,
    ikHandle: bool,
    imagePlane: bool,
    isoparm: bool,
    joint: bool,
    jointPivot: bool,
    lattice: bool,
    locator: bool,
    latticePoint: bool,
    light: bool,
    locatorUV: bool,
    meshComponents: bool,
    meshUVShell: bool,
    motionTrailPoint: bool,
    motionTrailTangent: bool,
    nurbsCurve: bool,
    nCloth: bool,
    nonlinear: bool,
    nParticle: bool,
    nParticleShape: bool,
    nRigid: bool,
    nurbsSurface: bool,
    objectComponent: bool,
    orientationLocator: bool,
    polymesh: bool,
    polymeshEdge: bool,
    polymeshFace: bool,
    polymeshFreeEdge: bool,
    plane: bool,
    particle: bool,
    particleShape: bool,
    polymeshUV: bool,
    polymeshVertex: bool,
    polymeshVtxFace: bool,
    queryByName: str,
    localRotationAxis: bool,
    rigidBody: bool,
    rigidConstraint: bool,
    rotatePivot: bool,
    sculpt: bool,
    subdiv: bool,
    surfaceEdge: bool,
    surfaceFace: bool,
    selectHandle: bool,
    surfaceKnot: bool,
    subdivMeshEdge: bool,
    subdivMeshFace: bool,
    subdivMeshPoint: bool,
    subdivMeshUV: bool,
    scalePivot: bool,
    springComponent: bool,
    surfaceParameterPoint: bool,
    spring: bool,
    surfaceRange: bool,
    stroke: bool,
    surfaceUV: bool,
    texture: bool,
    vertex: bool,
    locatorXYZ: bool,
) -> Any:
    ...


def selectedNodes(dagObjects: bool) -> Any:
    ...


def selectionConnection(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    activeCharacterList: bool,
    activeList: bool,
    addTo: str,
    addScript: Callable,
    activeCacheList: bool,
    characterList: bool,
    clear: bool,
    deselect: str,
    defineTemplate: str,
    editor: str,
    exists: bool,
    filter: str,
    findObject: str,
    g: bool,
    highlightList: bool,
    identify: bool,
    keyframeList: bool,
    lock: bool,
    connectionList: bool,
    modelList: bool,
    object: str,
    parent: str,
    remove: str,
    removeScript: Callable,
    select: str,
    setList: bool,
    switch: bool,
    useTemplate: str,
    worldList: bool,
) -> Any:
    ...


def separator(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    horizontal: bool,
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    style: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def sequenceManager(
    edit: bool,
    query: bool,
    addSequencerAudio: str,
    attachSequencerAudio: str,
    currentShot: str,
    currentTime: int,
    listSequencerAudio: str,
    listShots: bool,
    modelPanel: str,
    node: str,
    writableSequencer: str,
) -> Any:
    ...


def setAttr(
    *args: List[Incomplete],
    edit: bool,
    query: bool,
    alteredValue: bool,
    clamp: bool,
    caching: bool,
    channelBox: bool,
    capacityHint: int,
    keyable: bool,
    lock: bool,
    size: int,
    type: str,
) -> Any:
    ...


def setAttrMapping(*args, **kwargs) -> Any:
    ...


def setDefaultShadingGroup(arg0: str, /, query: bool) -> Any:
    ...


def setDrivenKeyframe(
    *args: List[str],
    edit: bool,
    query: bool,
    attribute: List[str],
    currentDriver: str,
    count: bool,
    controlPoints: bool,
    driven: bool,
    driver: bool,
    driverValue: List[float],
    hierarchy: str,
    insert: bool,
    insertBlend: bool,
    inTangentType: str,
    outTangentType: str,
    shape: bool,
    value: float,
) -> Any:
    ...


def setDynStartState() -> Any:
    ...


def setDynamic(
    *args: List[str],
    setAll: bool,
    allOnWhenRun: bool,
    disableAllOnWhenRun: bool,
    setOff: bool,
    setOn: bool,
) -> Any:
    ...


def setEditCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def setFluidAttr(
    *args: List[str],
    addValue: bool,
    attribute: str,
    clear: bool,
    floatRandom: float,
    floatValue: float,
    lowerFace: bool,
    reset: bool,
    vectorRandom: Tuple[float, float, float],
    vectorValue: Tuple[float, float, float],
    xvalue: bool,
    xIndex: int,
    yvalue: bool,
    yIndex: int,
    zvalue: bool,
    zIndex: int,
) -> Any:
    ...


def setFocus() -> Any:
    ...


def setInfinity(
    *args: List[str],
    edit: bool,
    query: bool,
    attribute: List[str],
    controlPoints: bool,
    hierarchy: str,
    postInfinite: str,
    preInfinite: str,
    shape: bool,
) -> Any:
    ...


def setInputDeviceMapping(*args, **kwargs) -> Any:
    ...


def setKeyCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    breakdown: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
    preserveTangent: bool,
) -> Any:
    ...


def setKeyPath() -> Any:
    ...


def setKeyframe(
    *args: List[str],
    edit: bool,
    query: bool,
    adjustTangent: bool,
    animLayer: str,
    animated: bool,
    attribute: List[str],
    breakdown: bool,
    clip: str,
    controlPoints: bool,
    dirtyDG: bool,
    float: List[float],
    hierarchy: str,
    insert: bool,
    insertBlend: bool,
    identity: bool,
    inTangentType: str,
    useCurrentLockedWeights: bool,
    minimizeRotation: bool,
    noResolve: bool,
    outTangentType: str,
    preserveCurveShape: bool,
    respectKeyable: bool,
    shape: bool,
    time: List[int],
    value: float,
) -> Any:
    ...


def setKeyframeBlendshapeTargetWts() -> Any:
    ...


def setMenuMode() -> Any:
    ...


def setNClothStartState() -> Any:
    ...


def setNodeTypeFlag(arg0: str, /, query: bool, display: bool, threadSafe: bool) -> Any:
    ...


def setParent(
    arg0: str,
    /,
    query: bool,
    defineTemplate: str,
    menu: bool,
    topLevel: bool,
    upLevel: bool,
    useTemplate: str,
) -> Any:
    ...


def setParticleAttr(
    *args: List[str],
    attribute: str,
    floatValue: float,
    object: str,
    relative: bool,
    randomFloat: float,
    randomVector: Tuple[float, float, float],
    vectorValue: Tuple[float, float, float],
) -> Any:
    ...


def setRenderPassType(
    *args: List[Incomplete], defaultDataType: bool, numChannels: int, type: str
) -> Any:
    ...


def setStartupMessage() -> Any:
    ...


def setToolTo() -> Any:
    ...


def setUITemplate(
    arg0: str, /, query: bool, popTemplate: bool, pushTemplate: bool
) -> Any:
    ...


def setXformManip(*args, **kwargs) -> Any:
    ...


def sets(
    *args: List[str],
    edit: bool,
    query: bool,
    addElement: str,
    afterFilters: bool,
    anyMember: str,
    clear: str,
    color: int,
    copy: str,
    edges: bool,
    empty: bool,
    editPoints: bool,
    facets: bool,
    forceElement: str,
    flatten: str,
    isIntersecting: str,
    isMember: str,
    include: str,
    intersection: str,
    layer: bool,
    name: str,
    noIntermediate: bool,
    nodesOnly: bool,
    noSurfaceShader: bool,
    noWarnings: bool,
    renderable: bool,
    remove: str,
    size: bool,
    split: str,
    subtract: str,
    text: str,
    union: str,
    vertices: bool,
) -> Any:
    ...


def shadingConnection(
    *args: List[Incomplete], edit: bool, query: bool, connectionState: bool
) -> Any:
    ...


def shadingGeometryRelCtx(*args, **kwargs) -> Any:
    ...


def shadingLightRelCtx(*args, **kwargs) -> Any:
    ...


def shadingNetworkCompare(
    *args: List[str],
    query: bool,
    delete: bool,
    equivalent: bool,
    network1: bool,
    network2: bool,
    byName: bool,
    upstreamOnly: bool,
    byValue: bool,
) -> Any:
    ...


def shadingNode(*args, **kwargs) -> Any:
    ...


def shapeCompare() -> Any:
    ...


def shapeEditor(*args, **kwargs) -> Any:
    ...


def shapePanel(*args, **kwargs) -> Any:
    ...


def shelfButton(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    actionIsSubstitute: bool,
    align: str,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    command: Callable,
    doubleClickCommand: Callable,
    dragCallback: Callable,
    disabledImage: str,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableCommandRepeat: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    flat: bool,
    font: str,
    fullPathName: bool,
    flexibleWidthType: int,
    flexibleWidthValue: int,
    flipX: float,
    flipY: float,
    height: int,
    highlightImage: str,
    highlightColor: Tuple[float, float, float],
    handleNodeDropCallback: Callable,
    image: str,
    image1: str,
    image2: str,
    image3: str,
    isObscured: bool,
    imageOverlayLabel: str,
    label: str,
    labelEditingCallback: Callable,
    labelOffset: int,
    manage: bool,
    marginHeight: int,
    menuItem: List[Tuple[str, str]],
    menuItemWithOptionBox: List[Tuple[str, str, str]],
    menuItemPython: List[int],
    marginWidth: int,
    noBackground: bool,
    noDefaultPopup: bool,
    numberOfPopupMenus: bool,
    overlayLabelBackColor: Tuple[float, float, float, float],
    overlayLabelColor: Tuple[float, float, float],
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rotation: float,
    commandRepeatable: bool,
    statusBarMessage: str,
    selectionImage: str,
    scaleIcon: bool,
    style: str,
    sourceType: str,
    useAlpha: float,
    useTemplate: str,
    visibleChangeCommand: Callable,
    version: str,
    visible: bool,
    width: int,
) -> Any:
    ...


def shelfLayout(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    alignment: str,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    childArray: bool,
    cellHeight: int,
    cellWidth: int,
    cellWidthHeight: Tuple[int, int],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    horizontal: bool,
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfChildren: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    position: List[Tuple[str, int]],
    statusBarMessage: str,
    spacing: int,
    style: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    version: str,
    visible: bool,
    width: int,
) -> Any:
    ...


def shelfTabLayout(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    borderStyle: str,
    childArray: bool,
    changeCommand: Callable,
    childResizable: bool,
    closeTab: int,
    closeTabCommand: Callable,
    doubleClickCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    horizontalScrollBarThickness: int,
    image: str,
    innerMarginHeight: int,
    innerMarginWidth: int,
    isObscured: bool,
    imageVisible: bool,
    manage: bool,
    minChildWidth: int,
    moveTab: Tuple[int, int],
    noBackground: bool,
    numberOfChildren: bool,
    numberOfPopupMenus: bool,
    newTabCommand: Callable,
    parent: str,
    popupMenuArray: bool,
    postMenuCommand: Callable,
    preventOverride: bool,
    preSelectCommand: Callable,
    statusBarMessage: str,
    selectCommand: Callable,
    scrollable: bool,
    showNewTab: bool,
    selectTab: str,
    scrollableTabs: bool,
    selectTabIndex: int,
    tabsClosable: bool,
    tabIcon: List[Tuple[str, str]],
    tabIconIndex: List[Tuple[int, str]],
    tabLabel: List[Tuple[str, str]],
    tabLabelIndex: List[Tuple[int, str]],
    tabPosition: str,
    tabTooltip: List[Tuple[str, str]],
    tabTooltipIndex: List[Tuple[int, str]],
    tabsVisible: bool,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    verticalScrollBarThickness: int,
    width: int,
) -> Any:
    ...


def shot(
    *args: List[Incomplete],
    edit: bool,
    query: bool,
    audio: str,
    copy: bool,
    customAnim: bool,
    currentCamera: str,
    createCustomAnim: bool,
    clipDuration: int,
    clip: str,
    clipOpacity: float,
    clipSyncState: bool,
    clipZeroOffset: int,
    deleteCustomAnim: bool,
    determineTrack: bool,
    endTime: int,
    flag1: bool,
    flag10: bool,
    flag11: bool,
    flag12: bool,
    flag2: bool,
    flag3: bool,
    flag4: bool,
    flag5: bool,
    flag6: bool,
    flag7: bool,
    flag8: bool,
    flag9: bool,
    favorite: bool,
    hasCameraSet: bool,
    hasStereoCamera: bool,
    imagePlaneVisibility: bool,
    linkAudio: str,
    lock: bool,
    mute: bool,
    paste: bool,
    pasteInstance: bool,
    preHoldTime: int,
    postHoldTime: int,
    scale: float,
    sourceDuration: int,
    sequenceEndTime: int,
    selfmute: bool,
    shotName: str,
    sequenceDuration: int,
    sequenceStartTime: int,
    startTime: int,
    transitionInLength: int,
    transitionInType: int,
    transitionOutLength: int,
    transitionOutType: int,
    track: int,
    unlinkAudio: bool,
) -> Any:
    ...


def shotRipple(
    *args: List[Incomplete],
    edit: bool,
    query: bool,
    deleted: bool,
    endDelta: int,
    endTime: int,
    startDelta: int,
    startTime: int,
) -> Any:
    ...


def shotTrack(
    *args: List[str],
    edit: bool,
    query: bool,
    insertTrack: int,
    lock: bool,
    mute: bool,
    numTracks: int,
    removeEmptyTracks: bool,
    removeTrack: int,
    selfmute: bool,
    solo: bool,
    swapTracks: Tuple[int, int],
    title: str,
    track: int,
    unsolo: bool,
) -> Any:
    ...


def showHelp(
    arg0: str,
    /,
    query: bool,
    absolute: bool,
    docs: bool,
    helpTable: bool,
    version: bool,
) -> Any:
    ...


def showHidden(
    *args: List[str], above: bool, allObjects: bool, below: bool, lastHidden: bool
) -> Any:
    ...


def showManipCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    addAttr: str,
    history: bool,
    currentNodeName: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    incSnap: List[Tuple[int, bool]],
    incSnapRelative: List[Tuple[int, bool]],
    incSnapUI: bool,
    incSnapValue: List[Tuple[int, float]],
    iveVisible: bool,
    lockSelection: bool,
    moveActiveAttrDown: bool,
    moveActiveAttrToTop: bool,
    moveActiveAttrUp: bool,
    name: str,
    removeAttr: str,
    resetActiveAttr: bool,
    selectedAttributes: bool,
    setAttrActive: str,
    setNextAttrActive: bool,
    setPreviousAttrActive: bool,
    toolFinish: Callable,
    toggleIncSnap: bool,
    toolStart: Callable,
) -> Any:
    ...


def showMetadata(
    *args: List[str],
    query: bool,
    auto: bool,
    dataType: str,
    interpolation: bool,
    isActivated: bool,
    listAllStreams: bool,
    listMembers: bool,
    listValidMethods: bool,
    listVisibleStreams: bool,
    method: str,
    member: str,
    range: Tuple[float, float],
    rayScale: float,
    stream: str,
) -> Any:
    ...


def showSelectionInTitle() -> Any:
    ...


def showShadingGroupAttrEditor(*args, **kwargs) -> Any:
    ...


def showWindow() -> Any:
    ...


def simplify(
    *args: List[str],
    animation: str,
    attribute: List[str],
    controlPoints: bool,
    float: List[Incomplete],
    floatTolerance: float,
    hierarchy: str,
    index: List[Incomplete],
    includeUpperBound: bool,
    shape: bool,
    time: List[Incomplete],
    timeTolerance: int,
    valueTolerance: float,
) -> Any:
    ...


def singleProfileBirailSurface(
    *args: List[Incomplete],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    polygon: int,
    transformMode: int,
    tangentContinuityProfile1: bool,
) -> Any:
    ...


def skeletonEmbed(
    *args: List[str],
    query: bool,
    mergedMesh: bool,
    segmentationMethod: int,
    segmentationResolution: int,
) -> Any:
    ...


def skinBindCtx(*args, **kwargs) -> Any:
    ...


def skinCluster(
    *args: List[str],
    edit: bool,
    query: bool,
    after: bool,
    addInfluence: List[str],
    afterReference: bool,
    addToSelection: bool,
    before: bool,
    bindMethod: int,
    baseShape: List[str],
    components: bool,
    selectedComponents: bool,
    dropoffRate: float,
    deformerTools: bool,
    exclusive: str,
    forceNormalizeWeights: bool,
    frontOfChain: bool,
    geometry: List[str],
    geometryIndices: bool,
    heatmapFalloff: float,
    ignoreBindPose: bool,
    ignoreHierarchy: bool,
    includeHiddenSelections: bool,
    influence: str,
    ignoreSelected: bool,
    lockWeights: bool,
    maximumInfluences: int,
    moveJointsMode: bool,
    name: str,
    nurbsSamples: int,
    normalizeWeights: int,
    obeyMaxInfluences: bool,
    parallel: bool,
    prune: bool,
    polySmoothness: float,
    recacheBindMatrices: bool,
    removeFromSelection: bool,
    removeInfluence: List[str],
    remove: List[bool],
    removeUnusedInfluence: bool,
    selectInfluenceVerts: List[str],
    skinMethod: int,
    split: bool,
    smoothWeights: float,
    smoothWeightsMaxIterations: int,
    toSelectedBones: bool,
    toSkeletonAndTransforms: bool,
    unbind: bool,
    unbindKeepHistory: bool,
    useComponentTags: bool,
    useGeometry: bool,
    volumeBind: float,
    volumeType: int,
    weightDistribution: int,
    weightedInfluence: bool,
    weight: float,
) -> Any:
    ...


def skinPercent(
    *args: List[Incomplete],
    query: bool,
    ignoreBelow: float,
    normalize: bool,
    pruneWeights: float,
    relative: bool,
    resetToDefault: bool,
    transform: str,
    transformMoveWeights: List[str],
    transformValue: List[Tuple[str, float]],
    value: bool,
    zeroRemainingInfluences: bool,
) -> Any:
    ...


def smoothCurve(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    replaceOriginal: bool,
    smoothness: float,
) -> Any:
    ...


def smoothTangentSurface(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    direction: int,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    parameter: List[float],
    replaceOriginal: bool,
    smoothness: int,
) -> Any:
    ...


def snapKey(
    *args: List[str],
    animation: str,
    attribute: List[str],
    controlPoints: bool,
    float: List[Incomplete],
    hierarchy: str,
    index: List[Incomplete],
    includeUpperBound: bool,
    mergeDuplicate: bool,
    shape: bool,
    time: List[Incomplete],
    timeMultiple: float,
    valueMultiple: float,
) -> Any:
    ...


def snapMode(
    query: bool,
    curve: bool,
    distanceIncrement: float,
    edgeMagnet: int,
    edgeMagnetTolerance: float,
    grid: bool,
    liveFaceCenter: bool,
    livePoint: bool,
    meshCenter: bool,
    point: bool,
    pixelCenter: bool,
    pixelSnap: bool,
    tolerance: int,
    useTolerance: bool,
    uvTolerance: int,
    viewPlane: bool,
) -> Any:
    ...


def snapTogetherCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    clearSelection: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
    setOrientation: bool,
    snapPolygonFace: bool,
) -> Any:
    ...


def snapshot(
    *args: List[str],
    edit: bool,
    query: bool,
    anchorTransform: str,
    constructionHistory: bool,
    endTime: int,
    increment: int,
    motionTrail: bool,
    motionTrailName: str,
    name: str,
    removeAnchorTransform: str,
    startTime: int,
    update: str,
) -> Any:
    ...


def snapshotBeadContext(*args, **kwargs) -> Any:
    ...


def snapshotBeadCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    inTangent: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
    outTangent: bool,
) -> Any:
    ...


def snapshotModifyKeyCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def soft(
    *args: List[str],
    query: bool,
    convert: bool,
    duplicate: bool,
    duplicateHistory: bool,
    goal: float,
    hideOriginal: bool,
    name: str,
) -> Any:
    ...


def softMod(
    *args: List[str],
    edit: bool,
    query: bool,
    after: bool,
    afterReference: bool,
    before: bool,
    bindState: bool,
    curveInterpolation: List[int],
    components: bool,
    selectedComponents: bool,
    curvePoint: List[float],
    curveValue: List[float],
    deformerTools: bool,
    envelope: float,
    exclusive: str,
    falloffAroundSelection: bool,
    falloffBasedOnX: bool,
    falloffBasedOnY: bool,
    falloffBasedOnZ: bool,
    falloffCenter: Tuple[float, float, float],
    falloffMasking: bool,
    frontOfChain: bool,
    falloffMode: int,
    falloffRadius: float,
    geometry: List[str],
    geometryIndices: bool,
    includeHiddenSelections: bool,
    ignoreSelected: bool,
    name: str,
    parallel: bool,
    prune: bool,
    relative: bool,
    resetGeometry: bool,
    remove: List[bool],
    split: bool,
    useComponentTags: bool,
    weightedNode: Tuple[str, str],
) -> Any:
    ...


def softModContext(*args, **kwargs) -> Any:
    ...


def softSelect(
    *args: List[str],
    edit: bool,
    query: bool,
    compressUndo: int,
    enableFalseColor: int,
    softSelectColorCurve: str,
    softSelectCurve: str,
    softSelectDistance: float,
    softSelectEnabled: int,
    softSelectFalloff: int,
    softSelectReset: bool,
    softSelectUVDistance: float,
) -> Any:
    ...


def softSelectOptionsCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    buttonDown: bool,
    buttonUp: bool,
    colorCurve: str,
    condition: bool,
    enableFalseColor: int,
    enabled: bool,
    exists: bool,
    falloffCurve: str,
    falloffMode: int,
    image1: str,
    image2: str,
    image3: str,
    size: float,
    uvSize: float,
) -> Any:
    ...


def soloMaterial(*args, **kwargs) -> Any:
    ...


def sortCaseInsensitive() -> Any:
    ...


def sound(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    endTime: int,
    file: str,
    length: bool,
    mute: bool,
    name: str,
    offset: int,
    sourceEnd: int,
    sourceStart: int,
) -> Any:
    ...


def soundControl(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    beginScrub: bool,
    dragCallback: Callable,
    dropCallback: Callable,
    displaySound: bool,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    endScrub: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    maxTime: int,
    minTime: int,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    pressCommand: str,
    popupMenuArray: bool,
    preventOverride: bool,
    resample: bool,
    releaseCommand: str,
    repeatChunkSize: float,
    repeatOnHold: bool,
    sound: str,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
    waveform: str,
) -> Any:
    ...


def soundPopup(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def spBirailCtx(*args, **kwargs) -> Any:
    ...


def spaceLocator(
    *args: List[str],
    edit: bool,
    query: bool,
    absolute: bool,
    name: str,
    position: Tuple[float, float, float],
    relative: bool,
) -> Any:
    ...


def sphere(
    *args: List[str],
    edit: bool,
    query: bool,
    axis: Tuple[float, float, float],
    caching: bool,
    constructionHistory: bool,
    degree: int,
    endSweep: float,
    frozen: bool,
    heightRatio: float,
    name: str,
    nodeState: int,
    spans: int,
    object: bool,
    pivot: Tuple[float, float, float],
    polygon: int,
    radius: float,
    sections: int,
    startSweep: float,
    tolerance: float,
    useTolerance: bool,
) -> Any:
    ...


def spotLight(
    *args: List[str],
    edit: bool,
    query: bool,
    bottomBarnDoorAngle: float,
    barnDoors: bool,
    coneAngle: float,
    decayRate: int,
    dropOff: float,
    discRadius: float,
    exclusive: bool,
    intensity: float,
    leftBarnDoorAngle: float,
    name: str,
    penumbra: float,
    position: Tuple[float, float, float],
    rightBarnDoorAngle: float,
    rotation: Tuple[float, float, float],
    useRayTraceShadows: bool,
    shadowColor: Tuple[float, float, float],
    shadowDither: float,
    shadowSamples: int,
    softShadow: bool,
    topBarnDoorAngle: float,
) -> Any:
    ...


def spotLightPreviewPort(*args, **kwargs) -> Any:
    ...


def spreadSheetEditor(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    allAttr: bool,
    attrRegExp: str,
    control: bool,
    defineTemplate: str,
    docTag: str,
    exists: bool,
    execute: str,
    filter: str,
    fixedAttrList: Incomplete,
    forceMainConnection: str,
    highlightConnection: str,
    keyableOnly: bool,
    lockMainConnection: bool,
    longNames: bool,
    mainListConnection: str,
    niceNames: bool,
    parent: str,
    panel: str,
    precision: int,
    selectedAttr: bool,
    selectionConnection: str,
    showShapes: bool,
    stateString: bool,
    unlockMainConnection: bool,
    unParent: bool,
    updateMainConnection: bool,
    useTemplate: str,
) -> Any:
    ...


def spring(
    *args: List[str],
    edit: bool,
    query: bool,
    addSprings: bool,
    allPoints: bool,
    count: bool,
    damping: float,
    dampingPS: float,
    damp: float,
    endForceWeight: float,
    exclusive: bool,
    length: float,
    minMax: bool,
    minDistance: float,
    maxDistance: float,
    name: str,
    noDuplicate: bool,
    restLengthPS: float,
    restLength: float,
    stiffness: float,
    stiffnessPS: float,
    startForceWeight: float,
    strength: float,
    useDampingPS: bool,
    useRestLengthPS: bool,
    useStiffnessPS: bool,
    wireframe: bool,
    walkLength: int,
) -> Any:
    ...


def squareSurface(
    *args: Tuple[str, str, str, str],
    edit: bool,
    query: bool,
    caching: bool,
    curveFitCheckpoints: int,
    constructionHistory: bool,
    continuityType1: int,
    continuityType2: int,
    continuityType3: int,
    continuityType4: int,
    endPointTolerance: float,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    polygon: int,
    rebuildCurve1: bool,
    rebuildCurve2: bool,
    rebuildCurve3: bool,
    rebuildCurve4: bool,
) -> Any:
    ...


def srtContext(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def stackTrace(
    query: bool,
    dump: bool,
    parameterCount: int,
    parameterType: Tuple[int, int],
    parameterValue: Tuple[int, int],
    state: bool,
) -> Any:
    ...


def stitchSurface(
    *args: List[str],
    edit: bool,
    query: bool,
    bias: float,
    cascade: bool,
    caching: bool,
    constructionHistory: bool,
    cvIthIndex: List[int],
    cvJthIndex: List[int],
    fixBoundary: bool,
    frozen: bool,
    keepG0Continuity: bool,
    keepG1Continuity: bool,
    name: str,
    nodeState: int,
    numberOfSamples: int,
    object: bool,
    positionalContinuity: List[bool],
    replaceOriginal: bool,
    stepCount: List[int],
    tangentialContinuity: List[bool],
    tolerance: List[float],
    togglePointNormals: bool,
    togglePointPosition: bool,
    toggleTolerance: List[bool],
    parameterU: List[float],
    parameterV: List[float],
    weight0: float,
    weight1: float,
) -> Any:
    ...


def stitchSurfaceCtx(*args, **kwargs) -> Any:
    ...


def stitchSurfacePoints(
    *args: List[str],
    edit: bool,
    query: bool,
    bias: float,
    cascade: bool,
    caching: bool,
    constructionHistory: bool,
    cvIthIndex: List[int],
    cvJthIndex: List[int],
    equalWeight: bool,
    fixBoundary: bool,
    frozen: bool,
    keepG0Continuity: bool,
    keepG1Continuity: bool,
    name: str,
    nodeState: int,
    object: bool,
    positionalContinuity: List[bool],
    replaceOriginal: bool,
    stepCount: List[int],
    tangentialContinuity: List[bool],
    tolerance: List[float],
    togglePointNormals: bool,
    togglePointPosition: bool,
    toggleTolerance: List[bool],
    parameterU: List[float],
    parameterV: List[float],
) -> Any:
    ...


def stringArrayIntersector(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    allowDuplicates: bool,
    defineTemplate: str,
    exists: bool,
    intersect: Incomplete,
    reset: bool,
    useTemplate: str,
) -> Any:
    ...


def stroke(name: str, pressure: bool, seed: int) -> Any:
    ...


def subdAutoProjection(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    layout: int,
    layoutMethod: int,
    name: str,
    nodeState: int,
    optimize: int,
    planes: int,
    percentageSpace: float,
    scale: int,
    skipIntersect: bool,
    worldSpace: bool,
) -> Any:
    ...


def subdCleanTopology() -> Any:
    ...


def subdCollapse(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    level: int,
    name: str,
    nodeState: int,
    object: bool,
) -> Any:
    ...


def subdDisplayMode(*args, **kwargs) -> Any:
    ...


def subdDuplicateAndConnect() -> Any:
    ...


def subdEditUV(
    *args: List[str],
    query: bool,
    angle: float,
    pivotU: float,
    pivotV: float,
    relative: bool,
    rotation: bool,
    rotateRatio: float,
    scale: bool,
    scaleU: float,
    scaleV: float,
    uValue: float,
    uvSetName: str,
    vValue: float,
) -> Any:
    ...


def subdLayoutUV(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    flipReversed: bool,
    frozen: bool,
    layout: int,
    layoutMethod: int,
    name: str,
    nodeState: int,
    percentageSpace: float,
    rotateForBestFit: int,
    scale: int,
    separate: int,
    worldSpace: bool,
) -> Any:
    ...


def subdListComponentConversion(*args, **kwargs) -> Any:
    ...


def subdMapCut(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
) -> Any:
    ...


def subdMapSewMove(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    limitPieceSize: bool,
    name: str,
    nodeState: int,
    numberFaces: int,
    worldSpace: bool,
) -> Any:
    ...


def subdMatchTopology(*args: List[str], frontOfChain: bool) -> Any:
    ...


def subdMirror(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    xMirror: bool,
    yMirror: bool,
    zMirror: bool,
) -> Any:
    ...


def subdPlanarProjection(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    createNewMap: bool,
    frozen: bool,
    insertBeforeDeformers: bool,
    imageCenter: Tuple[float, float],
    imageCenterX: float,
    imageCenterY: float,
    imageScale: Tuple[float, float],
    imageScaleU: float,
    imageScaleV: float,
    keepImageRatio: bool,
    mapDirection: str,
    name: str,
    nodeState: int,
    projectionCenter: Tuple[float, float, float],
    projectionCenterX: float,
    projectionCenterY: float,
    projectionCenterZ: float,
    projectionHeight: float,
    projectionScale: Tuple[float, float],
    projectionWidth: float,
    rotationAngle: float,
    rotate: Tuple[float, float, float],
    rotateX: float,
    rotateY: float,
    rotateZ: float,
    smartFit: bool,
    worldSpace: bool,
) -> Any:
    ...


def subdToBlind(*args, **kwargs) -> Any:
    ...


def subdToNurbs(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    applyMatrixToResult: bool,
    addUnderTransform: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    outputType: int,
) -> Any:
    ...


def subdToPoly(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    applyMatrixToResult: bool,
    addUnderTransform: bool,
    caching: bool,
    constructionHistory: bool,
    connectShaders: bool,
    copyUVTopology: bool,
    depth: int,
    extractPointPosition: bool,
    format: int,
    frozen: bool,
    inSubdCVId: List[Tuple[int, int]],
    inSubdCVIdLeft: int,
    inSubdCVIdRight: int,
    maxPolys: int,
    name: str,
    nodeState: int,
    object: bool,
    outSubdCVId: List[Tuple[int, int]],
    outSubdCVIdLeft: int,
    outSubdCVIdRight: int,
    outv: List[int],
    preserveVertexOrdering: bool,
    sampleCount: int,
    shareUVs: bool,
    subdNormals: bool,
) -> Any:
    ...


def subdTransferUVsToCache() -> Any:
    ...


def subdiv(*args, **kwargs) -> Any:
    ...


def subdivCrease(*args, **kwargs) -> Any:
    ...


def subdivDisplaySmoothness(*args, **kwargs) -> Any:
    ...


def subgraph(*args, **kwargs) -> Any:
    ...


def substituteGeometry(
    *args: List[str],
    disableNonSkinDeformers: bool,
    newGeometryToLayer: bool,
    oldGeometryToLayer: bool,
    retainOldGeometry: bool,
    reWeightDistTolerance: float,
) -> Any:
    ...


def suitePrefs(
    edit: bool,
    query: bool,
    applyToSuite: str,
    installedAsSuite: bool,
    isCompleteSuite: bool,
) -> Any:
    ...


def superCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    attach: List[str],
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
) -> Any:
    ...


def surface(
    *args: List[str],
    degreeU: int,
    degreeV: int,
    formU: str,
    formV: str,
    knotU: List[float],
    knotV: List[float],
    name: str,
    objectSpace: bool,
    point: List[Tuple[float, float, float]],
    pointWeight: List[Tuple[float, float, float, float]],
    worldSpace: bool,
) -> Any:
    ...


def surfaceSampler(
    *args: List[str],
    camera: str,
    fileFormat: List[str],
    filename: List[str],
    filterSize: float,
    filterType: int,
    flipU: bool,
    flipV: bool,
    ignoreMirroredFaces: bool,
    ignoreTransforms: bool,
    maximumValue: List[float],
    mapHeight: List[int],
    mapMaterials: List[bool],
    mapOutput: List[str],
    maxSearchDistance: List[float],
    mapWidth: List[int],
    overscan: int,
    source: List[str],
    searchCage: List[str],
    shadows: List[bool],
    searchMethod: int,
    searchOffset: List[float],
    mapSpace: List[str],
    superSampling: int,
    sourceUVSpace: List[str],
    target: List[str],
    targetUVSpace: List[str],
    useGeometryNormals: bool,
    uvSet: List[str],
) -> Any:
    ...


def surfaceShaderList(*args: List[str], edit: bool, query: bool, remove: str) -> Any:
    ...


def swatchDisplayPort(*args, **kwargs) -> Any:
    ...


def swatchRefresh() -> Any:
    ...


def switchTable(*args, **kwargs) -> Any:
    ...


def symbolButton(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    command: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    image: str,
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def symbolCheckBox(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    disableOffImage: str,
    dragCallback: Callable,
    disableOnImage: str,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    image: str,
    innerMargin: bool,
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    offCommand: Callable,
    offImage: str,
    onCommand: Callable,
    onImage: str,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    useTemplate: str,
    value: bool,
    visibleChangeCommand: Callable,
    version: str,
    visible: bool,
    width: int,
) -> Any:
    ...


def symmetricModelling(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    about: str,
    allowPartial: bool,
    axis: str,
    preserveSeam: int,
    reset: bool,
    symmetry: int,
    seamFalloffCurve: str,
    seamTolerance: float,
    tolerance: float,
    topoSymmetry: bool,
) -> Any:
    ...


def syncSculptCache(*args, **kwargs) -> Any:
    ...


def sysFile(
    arg0: str,
    /,
    copy: str,
    delete: bool,
    makeDir: bool,
    move: str,
    removeEmptyDir: bool,
    rename: str,
) -> Any:
    ...


def tabLayout(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    borderStyle: str,
    childArray: bool,
    changeCommand: Callable,
    childResizable: bool,
    closeTab: int,
    closeTabCommand: Callable,
    doubleClickCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    horizontalScrollBarThickness: int,
    image: str,
    innerMarginHeight: int,
    innerMarginWidth: int,
    isObscured: bool,
    imageVisible: bool,
    manage: bool,
    minChildWidth: int,
    moveTab: Tuple[int, int],
    noBackground: bool,
    numberOfChildren: bool,
    numberOfPopupMenus: bool,
    newTabCommand: Callable,
    parent: str,
    popupMenuArray: bool,
    postMenuCommand: Callable,
    preventOverride: bool,
    preSelectCommand: Callable,
    statusBarMessage: str,
    selectCommand: Callable,
    scrollable: bool,
    showNewTab: bool,
    selectTab: str,
    scrollableTabs: bool,
    selectTabIndex: int,
    tabsClosable: bool,
    tabIcon: List[Tuple[str, str]],
    tabIconIndex: List[Tuple[int, str]],
    tabLabel: List[Tuple[str, str]],
    tabLabelIndex: List[Tuple[int, str]],
    tabPosition: str,
    tabTooltip: List[Tuple[str, str]],
    tabTooltipIndex: List[Tuple[int, str]],
    tabsVisible: bool,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    verticalScrollBarThickness: int,
    width: int,
) -> Any:
    ...


def tangentConstraint(
    *args: List[str],
    edit: bool,
    query: bool,
    aimVector: Tuple[float, float, float],
    name: str,
    remove: bool,
    targetList: bool,
    upVector: Tuple[float, float, float],
    weight: float,
    weightAliasList: bool,
    worldUpVector: Tuple[float, float, float],
    worldUpObject: str,
    worldUpType: str,
) -> Any:
    ...


def targetWeldCtx(*args, **kwargs) -> Any:
    ...


def tension(
    *args: List[str],
    edit: bool,
    query: bool,
    after: bool,
    afterReference: bool,
    before: bool,
    components: bool,
    selectedComponents: bool,
    deformerTools: bool,
    envelope: float,
    exclusive: str,
    frontOfChain: bool,
    geometry: List[str],
    geometryIndices: bool,
    includeHiddenSelections: bool,
    ignoreSelected: bool,
    inwardConstraint: float,
    name: str,
    outwardConstraint: float,
    parallel: bool,
    pinBorderVertices: bool,
    prune: bool,
    remove: List[bool],
    smoothingIterations: int,
    split: bool,
    smoothingStep: float,
    useComponentTags: bool,
) -> Any:
    ...


def testPa() -> Any:
    ...


def testPassContribution(
    *args: List[Incomplete], renderLayer: str, renderPass: str
) -> Any:
    ...


def texCutContext(*args, **kwargs) -> Any:
    ...


def texLatticeDeformContext(*args, **kwargs) -> Any:
    ...


def texManipContext(*args, **kwargs) -> Any:
    ...


def texMoveContext(*args, **kwargs) -> Any:
    ...


def texMoveUVShellContext(*args, **kwargs) -> Any:
    ...


def texRotateContext(*args, **kwargs) -> Any:
    ...


def texScaleContext(*args, **kwargs) -> Any:
    ...


def texSculptCacheContext(*args, **kwargs) -> Any:
    ...


def texSculptCacheSync(*args, **kwargs) -> Any:
    ...


def texSelectContext(*args, **kwargs) -> Any:
    ...


def texSelectShortestPathCtx(*args, **kwargs) -> Any:
    ...


def texSmoothContext(*args, **kwargs) -> Any:
    ...


def texSmudgeUVContext(*args, **kwargs) -> Any:
    ...


def texTweakUVContext(*args, **kwargs) -> Any:
    ...


def texWinToolCtx(*args, **kwargs) -> Any:
    ...


def text(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    align: str,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    dragCallback: Callable,
    dropCallback: Callable,
    dropRectCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    font: str,
    fullPathName: bool,
    height: int,
    hyperlink: bool,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    label: str,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    recomputeSize: bool,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
    wordWrap: bool,
) -> Any:
    ...


def textCurves(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    deprecatedFontName: bool,
    font: str,
    frozen: bool,
    name: str,
    nodeState: int,
    object: bool,
    text: str,
) -> Any:
    ...


def textField(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    alwaysInvokeEnterCommandOnReturn: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    disableButtons: bool,
    disableClearButton: bool,
    dragCallback: Callable,
    disableHistoryButton: bool,
    drawInactiveFrame: bool,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enterCommand: Callable,
    editable: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fileName: str,
    font: str,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    insertionPosition: int,
    insertText: str,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    placeholderText: str,
    popupMenuArray: bool,
    preventOverride: bool,
    receiveFocusCommand: Callable,
    statusBarMessage: str,
    searchField: bool,
    textChangedCommand: Callable,
    text: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def textFieldButtonGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    annotation: str,
    buttonCommand: Callable,
    backgroundColor: Tuple[float, float, float],
    buttonLabel: str,
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    changeCommand: Callable,
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableButton: bool,
    enableBackground: bool,
    editable: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    forceChangeCommand: bool,
    fileName: str,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    insertionPosition: int,
    insertText: str,
    label: str,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    placeholderText: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rowAttach: List[Tuple[int, str, int]],
    statusBarMessage: str,
    textChangedCommand: Callable,
    text: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def textFieldGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    changeCommand: Callable,
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    editable: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    forceChangeCommand: bool,
    fileName: str,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    insertionPosition: int,
    insertText: str,
    label: str,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    placeholderText: str,
    popupMenuArray: bool,
    preventOverride: bool,
    rowAttach: List[Tuple[int, str, int]],
    statusBarMessage: str,
    textChangedCommand: Callable,
    text: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def textManip(*args, **kwargs) -> Any:
    ...


def textScrollList(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    append: List[str],
    allowAutomaticSelection: bool,
    allItems: bool,
    allowSorting: List[bool],
    allowMultiSelection: bool,
    annotation: str,
    appendPosition: List[Tuple[int, str]],
    appendWithToolTip: List[Tuple[str, str]],
    backgroundColor: Tuple[float, float, float],
    deselectAll: bool,
    doubleClickCommand: Callable,
    dragCallback: Callable,
    deselectItem: List[str],
    deselectIndexedItem: List[int],
    deleteKeyCommand: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    font: str,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    lineFont: List[Tuple[int, str]],
    manage: bool,
    noBackground: bool,
    numberOfItems: bool,
    numberOfPopupMenus: bool,
    numberOfRows: int,
    numberOfSelectedItems: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    removeAll: bool,
    removeItem: List[str],
    removeIndexedItem: List[int],
    statusBarMessage: str,
    selectCommand: Callable,
    setCheckedState: List[Tuple[str, bool]],
    showIndexedItem: int,
    selectItem: List[str],
    selectIndexedItem: List[int],
    setUniformItemSize: bool,
    selectUniqueTagItem: List[str],
    useTemplate: str,
    uniqueTag: List[str],
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def textureDeformer(
    *args: List[str],
    edit: bool,
    query: bool,
    after: bool,
    afterReference: bool,
    before: bool,
    components: bool,
    selectedComponents: bool,
    direction: str,
    deformerTools: bool,
    envelope: float,
    exclusive: str,
    frontOfChain: bool,
    geometry: List[str],
    geometryIndices: bool,
    includeHiddenSelections: bool,
    ignoreSelected: bool,
    name: str,
    offset: float,
    parallel: bool,
    prune: bool,
    pointSpace: str,
    remove: List[bool],
    strength: float,
    split: bool,
    useComponentTags: bool,
    vectorOffset: Tuple[float, float, float],
    vectorStrength: Tuple[float, float, float],
    vectorSpace: str,
) -> Any:
    ...


def textureLassoContext(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    drawClosed: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
) -> Any:
    ...


def texturePlacementContext(*args, **kwargs) -> Any:
    ...


def textureWindow(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    activeSelectionOnTop: bool,
    axesColor: Tuple[float, float, float],
    backFacingColor: Tuple[float, float, float, float],
    changeCommand: Tuple[str, str, str, str],
    checkerColor1: Tuple[float, float, float],
    checkerColor2: Tuple[float, float, float],
    checkerColorMode: int,
    checkerDensity: int,
    checkerDrawTileLabels: bool,
    checkerGradient1: Tuple[float, float, float],
    checkerGradient2: Tuple[float, float, float],
    checkerGradientOverlay: bool,
    clearImage: bool,
    cmEnabled: bool,
    capture: str,
    captureSequenceNumber: int,
    checkerTileLabelColor: Tuple[float, float, float],
    control: bool,
    divisions: int,
    drawAxis: bool,
    displayAxes: bool,
    doubleBuffer: bool,
    displayCheckered: bool,
    displayDivisionLines: bool,
    displayDistortion: bool,
    displayGridLines: bool,
    displayImage: int,
    displayIsolateSelectHUD: bool,
    displayLabels: bool,
    displayOverlappingUVCountHUD: bool,
    displayUsedPercentageHUD: bool,
    distortionPerObject: bool,
    displayPreselection: bool,
    displayReversedUVCountHUD: bool,
    displayUVShellCountHUD: bool,
    displaySolidMap: bool,
    drawSubregions: bool,
    displayStyle: str,
    defineTemplate: str,
    distortionAlpha: float,
    displayTextureBorder: bool,
    docTag: str,
    displayUVStatisticsHUD: bool,
    displayUVPositionHUD: bool,
    exists: bool,
    exposure: float,
    filter: str,
    frameAll: bool,
    frontFacingColor: Tuple[float, float, float, float],
    forceMainConnection: str,
    forceRebake: bool,
    frameSelected: bool,
    gamma: float,
    gridLinesColor: Tuple[float, float, float],
    gridNumbersColor: Tuple[float, float, float],
    highlightConnection: str,
    imageBaseColor: Tuple[float, float, float],
    imageDisplay: bool,
    imageDim: bool,
    internalFaces: bool,
    imageNames: bool,
    imageRatio: bool,
    imageNumber: int,
    imagePixelSnap: bool,
    imageRatioValue: float,
    imageSize: bool,
    isolateSelectSetUpdated: bool,
    imageToTextureNumber: int,
    imageTileRange: Tuple[float, float, float, float],
    imageUnfiltered: bool,
    lockMainConnection: bool,
    loadImage: str,
    labelPosition: str,
    multiColorAlpha: float,
    mainListConnection: str,
    maxResolution: int,
    numberOfImages: int,
    nbImages: bool,
    numberOfTextures: int,
    numUvSets: bool,
    nextView: bool,
    parent: str,
    panel: str,
    previousView: bool,
    reset: bool,
    removeAllImages: bool,
    rendererString: str,
    refresh: bool,
    relatedFaces: bool,
    removeImage: bool,
    realSize: bool,
    size: float,
    solidMap3dView: bool,
    scaleBlue: float,
    singleBuffer: bool,
    solidMapColorSeed: int,
    subdivisionLinesColor: Tuple[float, float, float],
    scaleGreen: float,
    saveImage: bool,
    selectInternalFaces: bool,
    selectionConnection: str,
    spacing: float,
    solidMapPerShell: bool,
    scaleRed: float,
    selectRelatedFaces: bool,
    style: int,
    stateString: bool,
    setUvSet: int,
    textureBorder3dView: bool,
    textureBorderColor: Tuple[float, float, float],
    textureBorderWidth: int,
    toggleExposure: bool,
    toggleGamma: bool,
    toggle: bool,
    textureToImageNumber: int,
    tileLabels: bool,
    tileLinesColor: Tuple[float, float, float],
    textureNumber: int,
    textureNames: bool,
    useFaceGroup: bool,
    unlockMainConnection: bool,
    unParent: bool,
    updateMainConnection: bool,
    usedPercentageHUDRange: Tuple[float, float, float, float],
    useTemplate: str,
    uvSets: bool,
    viewPortImage: bool,
    viewTransformName: str,
    wireframeComponentColor: Tuple[float, float, float, float],
    writeImage: str,
    wireframeObjectColor: Tuple[float, float, float, float],
) -> Any:
    ...


def threadCount(query: bool, numberOfThreads: int) -> Any:
    ...


def threePointArcCtx(*args, **kwargs) -> Any:
    ...


def thumbnailCaptureComponent(
    query: bool,
    capture: bool,
    closeCurrentSession: bool,
    capturedFrameCount: bool,
    delete: bool,
    endFrame: int,
    fileDialogCallback: str,
    fileDialogProcessing: bool,
    isSessionOpened: bool,
    launchedFromOptionsBox: bool,
    previewPath: str,
    removeProjectThumbnail: str,
    save: str,
    startFrame: int,
    selectedFileName: bool,
) -> Any:
    ...


def timeCode(
    edit: bool,
    query: bool,
    mayaStartFrame: float,
    productionStartFrame: float,
    productionStartHour: float,
    productionStartMinute: float,
    productionStartSecond: float,
) -> Any:
    ...


def timeControl(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    animCurveNames: bool,
    animLayerFilterOptions: str,
    annotation: str,
    animLayerShowWeight: bool,
    backgroundColor: Tuple[float, float, float],
    beginScrub: bool,
    currentFrameColor: Tuple[float, float, float, float],
    dragCallback: Callable,
    dropCallback: Callable,
    displaySound: bool,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    endScrub: bool,
    exists: bool,
    forceRedraw: bool,
    foregroundColor: Tuple[float, float, float],
    fullPathName: bool,
    forceRefresh: bool,
    globalTime: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    mainListConnection: str,
    noBackground: bool,
    numberOfPopupMenus: bool,
    outsideSpacing: int,
    parent: str,
    pressCommand: Callable,
    popupMenuArray: bool,
    preventOverride: bool,
    resample: bool,
    rangeArray: bool,
    releaseCommand: Callable,
    repeatChunkSize: float,
    range: bool,
    repeatOnHold: bool,
    rangeVisible: bool,
    sound: str,
    statusBarMessage: str,
    showKeys: str,
    showKeysCombined: bool,
    snap: bool,
    tickSize: int,
    tickSpan: int,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
    waveform: str,
) -> Any:
    ...


def timeEditor(*args, **kwargs) -> Any:
    ...


def timeEditorAnimSource(*args, **kwargs) -> Any:
    ...


def timeEditorBakeClips(*args, **kwargs) -> Any:
    ...


def timeEditorClip(*args, **kwargs) -> Any:
    ...


def timeEditorClipLayer(*args, **kwargs) -> Any:
    ...


def timeEditorClipOffset(*args, **kwargs) -> Any:
    ...


def timeEditorComposition(*args, **kwargs) -> Any:
    ...


def timeEditorPanel(*args, **kwargs) -> Any:
    ...


def timeEditorTracks(*args, **kwargs) -> Any:
    ...


def timeField(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    dragCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enterCommand: Callable,
    editable: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    precision: int,
    receiveFocusCommand: Callable,
    step: int,
    statusBarMessage: str,
    useTemplate: str,
    value: int,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def timeFieldGrp(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    adjustableColumn2: int,
    adjustableColumn3: int,
    adjustableColumn4: int,
    adjustableColumn5: int,
    adjustableColumn6: int,
    adjustableColumn: int,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    columnAlign: List[Tuple[int, str]],
    columnAttach: List[Tuple[int, str, int]],
    changeCommand: Callable,
    columnAlign2: Tuple[str, str],
    columnAlign3: Tuple[str, str, str],
    columnAlign4: Tuple[str, str, str, str],
    columnAlign5: Tuple[str, str, str, str, str],
    columnAlign6: Tuple[str, str, str, str, str, str],
    columnOffset2: Tuple[int, int],
    columnOffset3: Tuple[int, int, int],
    columnOffset4: Tuple[int, int, int, int],
    columnOffset5: Tuple[int, int, int, int, int],
    columnOffset6: Tuple[int, int, int, int, int, int],
    columnAttach2: Tuple[str, str],
    columnAttach3: Tuple[str, str, str],
    columnAttach4: Tuple[str, str, str, str],
    columnAttach5: Tuple[str, str, str, str, str],
    columnAttach6: Tuple[str, str, str, str, str, str],
    columnWidth: List[Tuple[int, int]],
    columnWidth1: int,
    columnWidth2: Tuple[int, int],
    columnWidth3: Tuple[int, int, int],
    columnWidth4: Tuple[int, int, int, int],
    columnWidth5: Tuple[int, int, int, int, int],
    columnWidth6: Tuple[int, int, int, int, int, int],
    dragCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    extraLabel: str,
    enable: bool,
    enable1: bool,
    enable2: bool,
    enable3: bool,
    enable4: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    label: str,
    manage: bool,
    noBackground: bool,
    numberOfFields: int,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    precision: int,
    rowAttach: List[Tuple[int, str, int]],
    step: float,
    statusBarMessage: str,
    useTemplate: str,
    value: Tuple[float, float, float, float],
    value1: float,
    value2: float,
    value3: float,
    value4: float,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def timePort(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    globalTime: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    snap: bool,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def timeRangeInfo(time: List[Incomplete]) -> Any:
    ...


def timeSliderCustomDraw(
    arg0: int,
    /,
    edit: bool,
    query: bool,
    color: Tuple[float, float, float, float],
    clearPrimitives: bool,
    deregister: int,
    height: int,
    layer: int,
    location: int,
    priority: int,
    registerAbove: str,
    registerBelow: str,
    registerOn: Tuple[str, int],
    setPrimitives: Tuple[str, float, float],
    visible: bool,
) -> Any:
    ...


def timeWarp(
    *args: List[str],
    edit: bool,
    query: bool,
    deleteFrame: int,
    frame: List[float],
    g: bool,
    interpType: Tuple[int, str],
    moveFrame: Tuple[int, float],
) -> Any:
    ...


def timer(endTimer: bool, lapTime: bool, name: str, startTimer: bool) -> Any:
    ...


def timerX(startTime: float) -> Any:
    ...


def toggle(
    *args: List[str],
    query: bool,
    above: bool,
    below: bool,
    boundary: bool,
    boundingBox: bool,
    controlVertex: bool,
    doNotWrite: bool,
    editPoint: bool,
    extent: bool,
    facet: bool,
    geometry: bool,
    gl: bool,
    hull: bool,
    highPrecisionNurbs: bool,
    localAxis: bool,
    latticePoint: bool,
    latticeShape: bool,
    newCurve: bool,
    newPolymesh: bool,
    normal: bool,
    newSurface: bool,
    origin: bool,
    pointDisplay: bool,
    pointFacet: bool,
    point: bool,
    rotatePivot: bool,
    surfaceFace: bool,
    selectHandle: bool,
    scalePivot: bool,
    state: bool,
    template: bool,
    uvCoords: bool,
    vertex: bool,
) -> Any:
    ...


def toggleAxis(query: bool, origin: bool, view: bool) -> Any:
    ...


def toggleDisplacement() -> Any:
    ...


def toggleWindowVisibility() -> Any:
    ...


def tolerance(query: bool, angular: float, linear: float) -> Any:
    ...


def toolBar(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    area: str,
    allowedArea: List[str],
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    content: str,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    label: str,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def toolButton(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    allowMultipleTools: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    changeCommand: Callable,
    collection: str,
    doubleClickCommand: Callable,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    image1: str,
    image2: str,
    image3: str,
    isObscured: bool,
    imageOverlayLabel: str,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    offCommand: Callable,
    onCommand: Callable,
    parent: str,
    popupIndicatorVisible: bool,
    popupMenuArray: bool,
    preventOverride: bool,
    statusBarMessage: str,
    select: bool,
    style: str,
    tool: List[str],
    toolArray: bool,
    toolCount: bool,
    toolImage1: List[Tuple[str, str]],
    toolImage2: List[Tuple[str, str]],
    toolImage3: List[Tuple[str, str]],
    useTemplate: str,
    visibleChangeCommand: Callable,
    version: str,
    visible: bool,
    width: int,
) -> Any:
    ...


def toolCollection(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    collectionItemArray: bool,
    defineTemplate: str,
    exists: bool,
    gl: bool,
    numberOfCollectionItems: bool,
    parent: str,
    select: str,
    useTemplate: str,
) -> Any:
    ...


def toolDropped() -> Any:
    ...


def toolHasOptions() -> Any:
    ...


def toolPropertyWindow(
    edit: bool,
    query: bool,
    field: str,
    helpButton: str,
    icon: str,
    inMainWindow: bool,
    location: str,
    noviceMode: bool,
    resetButton: str,
    refresh: bool,
    restore: bool,
    selectCommand: str,
    showCommand: str,
) -> Any:
    ...


def torus(
    *args: List[str],
    edit: bool,
    query: bool,
    axis: Tuple[float, float, float],
    caching: bool,
    constructionHistory: bool,
    degree: int,
    endSweep: float,
    frozen: bool,
    heightRatio: float,
    minorSweep: float,
    name: str,
    nodeState: int,
    spans: int,
    object: bool,
    pivot: Tuple[float, float, float],
    polygon: int,
    radius: float,
    sections: int,
    startSweep: float,
    tolerance: float,
    useTolerance: bool,
) -> Any:
    ...


def track(
    arg0: str,
    /,
    down: float,
    left: float,
    right: float,
    upDistance01: float,
    upDistance02: float,
) -> Any:
    ...


def trackCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    alternateContext: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
    trackGeometry: bool,
    toolName: str,
    trackScale: float,
) -> Any:
    ...


def transferAttributes(
    *args: List[str],
    edit: bool,
    query: bool,
    after: bool,
    afterReference: bool,
    before: bool,
    colorBorders: int,
    components: bool,
    selectedComponents: bool,
    transferColors: int,
    deformerTools: bool,
    exclusive: str,
    frontOfChain: bool,
    flipUVs: int,
    geometry: List[str],
    geometryIndices: bool,
    includeHiddenSelections: bool,
    ignoreSelected: bool,
    matchChoice: int,
    name: str,
    transferNormals: int,
    parallel: bool,
    transferPositions: int,
    prune: bool,
    remove: List[bool],
    sourceColorSet: str,
    searchMethod: int,
    split: bool,
    sampleSpace: int,
    searchScaleX: float,
    searchScaleY: float,
    searchScaleZ: float,
    sourceUvSpace: str,
    sourceUvSet: str,
    targetColorSet: str,
    targetUvSpace: str,
    targetUvSet: str,
    useComponentTags: bool,
    transferUVs: int,
) -> Any:
    ...


def transferShadingSets(
    *args: List[str], edit: bool, query: bool, searchMethod: int, sampleSpace: int
) -> Any:
    ...


def transformCompare(*args: List[str], root: bool) -> Any:
    ...


def transformLimits(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    enableRotationX: Tuple[bool, bool],
    enableRotationY: Tuple[bool, bool],
    enableRotationZ: Tuple[bool, bool],
    enableScaleX: Tuple[bool, bool],
    enableScaleY: Tuple[bool, bool],
    enableScaleZ: Tuple[bool, bool],
    enableTranslationX: Tuple[bool, bool],
    enableTranslationY: Tuple[bool, bool],
    enableTranslationZ: Tuple[bool, bool],
    remove: bool,
    rotationX: Tuple[float, float],
    rotationY: Tuple[float, float],
    rotationZ: Tuple[float, float],
    scaleX: Tuple[float, float],
    scaleY: Tuple[float, float],
    scaleZ: Tuple[float, float],
    translationX: Tuple[float, float],
    translationY: Tuple[float, float],
    translationZ: Tuple[float, float],
) -> Any:
    ...


def translator(
    arg0: str,
    /,
    query: bool,
    fileCompression: str,
    defaultFileRule: bool,
    defaultOptions: str,
    extension: bool,
    filter: bool,
    list: bool,
    loaded: bool,
    optionsScript: bool,
    objectType: bool,
    readSupport: bool,
    writeSupport: bool,
) -> Any:
    ...


def treeLister(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    addItem: List[Tuple[str, str, Callable]],
    addFavorite: List[str],
    annotation: str,
    addVnnItem: List[Tuple[str, str, str, str]],
    backgroundColor: Tuple[float, float, float],
    clearContents: bool,
    collapsePath: List[str],
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    executeItem: str,
    enableKeyboardFocus: bool,
    enable: bool,
    expandPath: List[str],
    expandToDepth: int,
    exists: bool,
    favoritesCallback: Callable,
    favoritesList: bool,
    fullPathName: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    isObscured: bool,
    itemScript: str,
    manage: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    refreshCommand: Callable,
    removeItem: List[str],
    removeFavorite: List[str],
    resultsPathUnderCursor: bool,
    statusBarMessage: str,
    selectPath: List[str],
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    vnnString: bool,
    width: int,
) -> Any:
    ...


def treeView(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    attachButtonRight: int,
    allowDragAndDrop: bool,
    allowHiddenParents: bool,
    addItem: List[Tuple[str, str]],
    allowMultiSelection: bool,
    annotation: str,
    allowReparenting: bool,
    borderHighliteColor: Tuple[str, float, float, float],
    buttonErase: List[Tuple[str, bool]],
    backgroundColor: Tuple[float, float, float],
    borderHighlite: Tuple[str, bool],
    buttonStyle: List[Tuple[str, int, str]],
    buttonState: List[Tuple[str, int, str]],
    buttonTransparencyColor: List[Tuple[str, int, float, float, float]],
    buttonTextIcon: List[Tuple[str, int, str]],
    buttonTransparencyOverride: List[Tuple[str, int, bool]],
    buttonTooltip: List[Tuple[str, int, str]],
    buttonVisible: List[Tuple[str, int, bool]],
    children: str,
    contextMenuCommand: Callable,
    clearSelection: bool,
    dragAndDropCommand: Callable,
    itemDblClickCommand2: Callable,
    dragCallback: Callable,
    displayLabel: List[Tuple[str, str]],
    displayLabelSuffix: List[Tuple[str, str]],
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableButton: List[Tuple[str, int, int]],
    enableBackground: bool,
    expandCollapseCommand: Callable,
    expandItem: Tuple[str, bool],
    enableKeyboardFocus: bool,
    editLabelCommand: Callable,
    enable: bool,
    enableKeys: bool,
    enableLabel: Tuple[str, int],
    exists: bool,
    flatButton: int,
    fontFace: Tuple[str, int],
    font: Tuple[str, str],
    fullPathName: bool,
    height: int,
    hideButtons: bool,
    highliteColor: Tuple[str, float, float, float],
    highlite: Tuple[str, bool],
    highlightColor: Tuple[float, float, float],
    image: List[Tuple[str, int, str]],
    itemAnnotation: Tuple[str, str],
    ignoreButtonClick: List[Tuple[str, int, int]],
    itemDblClickCommand: Callable,
    itemIndex: str,
    itemExists: str,
    insertItem: List[Tuple[str, str, int]],
    isItemExpanded: str,
    isLeaf: str,
    isObscured: bool,
    itemParent: str,
    itemRenamedCommand: Callable,
    itemSelected: str,
    item: str,
    itemVisible: Tuple[str, bool],
    labelBackgroundColor: Tuple[str, float, float, float],
    manage: bool,
    numberOfButtons: int,
    noBackground: bool,
    numberOfPopupMenus: bool,
    ornament: Tuple[str, int, int, int],
    ornamentColor: Tuple[str, float, float, float],
    parent: str,
    pressCommand: List[Tuple[int, Callable]],
    popupMenuArray: bool,
    preventOverride: bool,
    removeAll: bool,
    removeItem: str,
    rightPressCommand: List[Tuple[int, Callable]],
    reverseTreeOrder: bool,
    statusBarMessage: str,
    selectCommand: Callable,
    selectionChangedCommand: Callable,
    selectionColor: Tuple[str, float, float, float],
    showItem: str,
    selectItem: Tuple[str, bool],
    select: Tuple[str, int],
    textColor: Tuple[str, float, float, float],
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
) -> Any:
    ...


def trim(
    *args: List[str],
    edit: bool,
    query: bool,
    caching: bool,
    constructionHistory: bool,
    frozen: bool,
    locatorU: List[float],
    locatorV: List[float],
    name: str,
    nodeState: int,
    object: bool,
    replaceOriginal: bool,
    shrink: bool,
    selected: int,
    tolerance: float,
) -> Any:
    ...


def trimCtx(*args, **kwargs) -> Any:
    ...


def truncateFluidCache(*args: List[str], edit: bool, query: bool) -> Any:
    ...


def truncateHairCache(*args: List[str], edit: bool, query: bool) -> Any:
    ...


def tumble(
    arg0: str,
    /,
    azimuthAngle: float,
    elevationAngle: float,
    localTumble: int,
    pivotPoint: Tuple[float, float, float],
    rotationAngles: Tuple[float, float],
) -> Any:
    ...


def tumbleCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    alternateContext: bool,
    autoOrthoConstrain: bool,
    autoSetPivot: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    localTumble: int,
    name: str,
    orthoLock: bool,
    orthoStep: float,
    objectTumble: bool,
    toolName: str,
    tumbleScale: float,
) -> Any:
    ...


def turbulence(
    *args: List[str],
    edit: bool,
    query: bool,
    attenuation: float,
    frequency: float,
    magnitude: float,
    maxDistance: float,
    name: str,
    noiseLevel: int,
    noiseRatio: float,
    phase: float,
    position: List[Tuple[float, float, float]],
    perVertex: bool,
    phaseX: float,
    phaseY: float,
    phaseZ: float,
    torusSectionRadius: float,
    volumeExclusion: bool,
    volumeOffset: Tuple[float, float, float],
    volumeShape: str,
    volumeSweep: float,
) -> Any:
    ...


def twoPointArcCtx(*args, **kwargs) -> Any:
    ...


def ubercam() -> Any:
    ...


def uiTemplate(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    defineTemplate: str,
    exists: bool,
    useTemplate: str,
) -> Any:
    ...


def unapplyOverride() -> Any:
    ...


def unassignInputDevice(*args, **kwargs) -> Any:
    ...


def undo() -> Any:
    ...


def undoInfo(
    query: bool,
    closeChunk: bool,
    chunkName: str,
    infinity: bool,
    length: int,
    openChunk: bool,
    printQueue: bool,
    printRedoQueue: bool,
    redoName: str,
    redoQueueEmpty: bool,
    state: bool,
    stateWithoutFlush: bool,
    undoName: str,
    undoQueueEmpty: bool,
) -> Any:
    ...


def unfold(
    *args: List[str],
    applyToShell: bool,
    areaWeight: float,
    globalBlend: float,
    globalMethodBlend: float,
    iterations: int,
    optimizeAxis: int,
    pinSelected: bool,
    pinUvBorder: bool,
    scale: float,
    stoppingThreshold: float,
    useScale: bool,
) -> Any:
    ...


def ungroup(
    *args: List[str], absolute: bool, parent: str, relative: bool, world: bool
) -> Any:
    ...


def uniform(
    *args: List[str],
    edit: bool,
    query: bool,
    attenuation: float,
    directionX: float,
    directionY: float,
    directionZ: float,
    magnitude: float,
    maxDistance: float,
    name: str,
    position: List[Tuple[float, float, float]],
    perVertex: bool,
    torusSectionRadius: float,
    volumeExclusion: bool,
    volumeOffset: Tuple[float, float, float],
    volumeShape: str,
    volumeSweep: float,
) -> Any:
    ...


def unknownNode(
    arg0: Incomplete,
    /,
    query: bool,
    plugin: bool,
    realClassName: bool,
    realClassTag: bool,
) -> Any:
    ...


def unknownPlugin(
    arg0: str,
    /,
    query: bool,
    dataTypes: bool,
    list: bool,
    nodeTypes: bool,
    remove: bool,
    version: bool,
) -> Any:
    ...


def unloadPlugin(
    *args: List[str], addCallback: Callable, force: bool, removeCallback: Callable
) -> Any:
    ...


def untangleUV(
    *args: List[str],
    mapBorder: str,
    maxRelaxIterations: int,
    pinBorder: bool,
    pinSelected: bool,
    pinUnselected: bool,
    relax: str,
    relaxTolerance: float,
    shapeDetail: float,
) -> Any:
    ...


def untrim(
    arg0: Incomplete,
    /,
    edit: bool,
    query: bool,
    untrimAll: bool,
    caching: bool,
    constructionHistory: bool,
    curveOnSurface: bool,
    frozen: bool,
    name: str,
    noChanges: bool,
    nodeState: int,
    object: bool,
    replaceOriginal: bool,
) -> Any:
    ...


def upAxis(*args: List[str], query: bool, axis: str, rotateView: bool) -> Any:
    ...


def userCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    history: bool,
    editCommand: Callable,
    editPrompt: str,
    exists: bool,
    finalCommand: str,
    selectionFlag: List[Tuple[int, str]],
    image1: str,
    image2: str,
    image3: str,
    name: str,
    noSelectionPrompt: List[Tuple[int, str]],
    selectionCount: List[Tuple[int, int]],
    selectionMask: List[Tuple[int, str]],
    selectionPrompt: List[str],
) -> Any:
    ...


def uvLink(
    b: bool,
    isValid: bool,
    make: bool,
    query: bool,
    queryObject: str,
    texture: str,
    uvSet: str,
) -> Any:
    ...


def uvSnapshot(
    *args: List[str],
    antiAliased: bool,
    blueColor: int,
    entireUVRange: bool,
    fileFormat: str,
    greenColor: int,
    name: str,
    overwrite: bool,
    redColor: int,
    uMin: float,
    uMax: float,
    uvSetName: str,
    vMin: float,
    vMax: float,
    xResolution: int,
    yResolution: int,
) -> Any:
    ...


def view2dToolCtx(*args, **kwargs) -> Any:
    ...


def viewCamera(arg0: Incomplete, /, move: str, sideView: bool, topView: bool) -> Any:
    ...


def viewClipPlane(
    arg0: str,
    /,
    query: bool,
    autoClipPlane: bool,
    farClipPlane: float,
    nearClipPlane: float,
    surfacesOnly: bool,
) -> Any:
    ...


def viewFit(
    *args: List[str],
    allObjects: bool,
    animate: bool,
    center: bool,
    fitFactor: float,
    noChildren: bool,
    namespace: str,
    panel: str,
) -> Any:
    ...


def viewHeadOn() -> Any:
    ...


def viewLookAt(arg0: str, /, position: Tuple[float, float, float]) -> Any:
    ...


def viewManip(*args, **kwargs) -> Any:
    ...


def viewPlace(
    arg0: Incomplete,
    /,
    animate: bool,
    eyePoint: Tuple[float, float, float],
    fieldOfView: float,
    lookAt: Tuple[float, float, float],
    ortho: bool,
    perspective: bool,
    upDirection: Tuple[float, float, float],
    viewDirection: Tuple[float, float, float],
) -> Any:
    ...


def viewSet(
    arg0: str,
    /,
    query: bool,
    animate: bool,
    back: bool,
    bottom: bool,
    front: bool,
    fitFactor: float,
    home: bool,
    keepRenderSettings: bool,
    leftSide: bool,
    namespace: str,
    nextView: bool,
    persp: bool,
    previousView: bool,
    rightSide: bool,
    side: bool,
    viewNegativeX: bool,
    viewNegativeY: bool,
    viewNegativeZ: bool,
    viewX: bool,
    viewY: bool,
    viewZ: bool,
) -> Any:
    ...


def visor(*args, **kwargs) -> Any:
    ...


def volumeAxis(
    *args: List[str],
    edit: bool,
    query: bool,
    awayFromCenter: float,
    awayFromAxis: float,
    alongAxis: float,
    aroundAxis: float,
    attenuation: float,
    directionalSpeed: float,
    detailTurbulence: float,
    directionX: float,
    directionY: float,
    directionZ: float,
    invertAttenuation: bool,
    magnitude: float,
    maxDistance: float,
    name: str,
    position: List[Tuple[float, float, float]],
    perVertex: bool,
    turbulenceFrequencyX: float,
    turbulenceFrequencyY: float,
    turbulenceFrequencyZ: float,
    turbulenceOffsetX: float,
    turbulenceOffsetY: float,
    turbulenceOffsetZ: float,
    turbulence: float,
    turbulenceSpeed: float,
    torusSectionRadius: float,
    volumeExclusion: bool,
    volumeOffset: Tuple[float, float, float],
    volumeShape: str,
    volumeSweep: float,
) -> Any:
    ...


def volumeBind(edit: bool, query: bool, influence: str, name: str) -> Any:
    ...


def vortex(
    *args: List[str],
    edit: bool,
    query: bool,
    attenuation: float,
    axisX: float,
    axisY: float,
    axisZ: float,
    magnitude: float,
    maxDistance: float,
    name: str,
    position: List[Tuple[float, float, float]],
    perVertex: bool,
    torusSectionRadius: float,
    volumeExclusion: bool,
    volumeOffset: Tuple[float, float, float],
    volumeShape: str,
    volumeSweep: float,
) -> Any:
    ...


def waitCursor(query: bool, state: bool) -> Any:
    ...


def walkCtx(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    alternateContext: bool,
    history: bool,
    exists: bool,
    image1: str,
    image2: str,
    image3: str,
    name: str,
    toolName: str,
    crouchCount: float,
    walkHeight: float,
    walkSpeed: float,
    walkSensitivity: float,
    walkToolHud: bool,
) -> Any:
    ...


def warnUserDialog(addInfo: Tuple[str, str], message: str, title: str) -> Any:
    ...


def warning(*args: List[str], noContext: bool, showLineNumber: bool) -> Any:
    ...


def webBrowser(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    annotation: str,
    backgroundColor: Tuple[float, float, float],
    back: bool,
    command: str,
    dragCallback: Callable,
    dropCallback: Callable,
    defineTemplate: str,
    docTag: str,
    enableBackground: bool,
    enableKeyboardFocus: bool,
    enable: bool,
    exists: bool,
    find: str,
    fullPathName: bool,
    forward: bool,
    height: int,
    highlightColor: Tuple[float, float, float],
    home: bool,
    isObscured: bool,
    manage: bool,
    matchCase: bool,
    matchWholeWord: bool,
    noBackground: bool,
    numberOfPopupMenus: bool,
    parent: str,
    popupMenuArray: bool,
    preventOverride: bool,
    reload: bool,
    statusBarMessage: str,
    searchForward: bool,
    stop: bool,
    urlChangedCb: str,
    openURL: str,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: int,
    wrap: bool,
) -> Any:
    ...


def webBrowserPrefs(
    arg0: str, /, edit: bool, query: bool, preference: Tuple[str, str]
) -> Any:
    ...


def weightsColor(*args, **kwargs) -> Any:
    ...


def whatsNewHighlight(
    query: bool,
    highlightColor: Tuple[float, float, float],
    highlightOn: bool,
    showStartupDialog: bool,
) -> Any:
    ...


def window(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    backgroundColor: Tuple[float, float, float],
    closeCommand: Callable,
    dockCorner: List[Tuple[str, str]],
    dockingLayout: str,
    dockStation: bool,
    defineTemplate: str,
    docTag: str,
    exists: bool,
    frontWindow: bool,
    height: int,
    iconify: bool,
    iconName: str,
    interactivePlacement: bool,
    leftEdge: int,
    menuArray: bool,
    menuBar: bool,
    menuBarResize: bool,
    menuBarVisible: bool,
    menuBarCornerWidget: Tuple[str, str],
    menuIndex: Tuple[str, int],
    mainMenuBar: bool,
    minimizeButton: bool,
    minimizeCommand: Callable,
    mainWindow: bool,
    maximizeButton: bool,
    nestedDockingEnabled: bool,
    numberOfMenus: bool,
    parent: str,
    restoreCommand: Callable,
    retain: bool,
    resizeToFitChildren: bool,
    sizeable: bool,
    state: str,
    title: str,
    titleBar: bool,
    titleBarMenu: bool,
    topEdge: int,
    toolbox: bool,
    topLeftCorner: Tuple[int, int],
    useTemplate: str,
    visible: bool,
    width: int,
    widthHeight: Tuple[int, int],
) -> Any:
    ...


def windowPref(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    enableAll: bool,
    exists: bool,
    height: int,
    loadAll: bool,
    leftEdge: int,
    maximized: bool,
    parentMain: bool,
    remove: bool,
    removeAll: bool,
    restoreMainWindowState: str,
    saveAll: bool,
    saveMainWindowState: str,
    topEdge: int,
    topLeftCorner: Tuple[int, int],
    width: int,
    widthHeight: Tuple[int, int],
) -> Any:
    ...


def wire(
    *args: List[str],
    edit: bool,
    query: bool,
    after: bool,
    afterReference: bool,
    before: bool,
    crossingEffect: float,
    components: bool,
    selectedComponents: bool,
    dropoffDistance: List[Tuple[int, float]],
    deformerTools: bool,
    envelope: float,
    exclusive: str,
    frontOfChain: bool,
    geometry: List[str],
    geometryIndices: bool,
    groupWithBase: bool,
    holder: List[Tuple[int, str]],
    includeHiddenSelections: bool,
    ignoreSelected: bool,
    localInfluence: float,
    name: str,
    parallel: bool,
    prune: bool,
    remove: List[bool],
    split: bool,
    useComponentTags: bool,
    wire: List[str],
    wireCount: int,
) -> Any:
    ...


def wireContext(*args, **kwargs) -> Any:
    ...


def workspace(
    arg0: str,
    /,
    query: bool,
    active: bool,
    baseWorkspace: str,
    create: str,
    directory: str,
    expandName: str,
    filter: bool,
    fullName: bool,
    fileRule: Tuple[str, str],
    fileRuleEntry: str,
    fileRuleList: bool,
    list: bool,
    listFullWorkspaces: bool,
    listWorkspaces: bool,
    newWorkspace: bool,
    openWorkspace: bool,
    objectType: Tuple[str, str],
    objectTypeEntry: str,
    objectTypeList: bool,
    projectPath: str,
    rootDirectory: bool,
    removeFileRuleEntry: str,
    renderType: Tuple[str, str],
    renderTypeEntry: str,
    renderTypeList: bool,
    removeVariableEntry: str,
    saveWorkspace: bool,
    shortName: bool,
    update: bool,
    updateAll: bool,
    variable: Tuple[str, str],
    variableEntry: str,
    variableList: bool,
) -> Any:
    ...


def workspaceControl(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    actLikeMayaUIElement: bool,
    closeCommand: Callable,
    close: bool,
    collapse: bool,
    checksPlugins: bool,
    deleteLater: bool,
    defineTemplate: str,
    dockToControl: Tuple[str, str],
    dockToMainWindow: Tuple[str, bool],
    dockToPanel: Tuple[str, str, bool],
    duplicatable: bool,
    exists: bool,
    floating: bool,
    height: bool,
    heightProperty: str,
    horizontal: bool,
    initCallback: str,
    initialHeight: int,
    initialWidth: int,
    label: str,
    layoutDirectionCallback: str,
    loadImmediately: bool,
    minimumHeight: int,
    minimumWidth: int,
    r: bool,
    requiredControl: List[str],
    requiredPlugin: List[str],
    restore: bool,
    resizeHeight: int,
    resizeWidth: int,
    retain: bool,
    stateString: str,
    tabPosition: Tuple[str, bool],
    tabToControl: Tuple[str, int],
    uiScript: Callable,
    useTemplate: str,
    visibleChangeCommand: Callable,
    visible: bool,
    width: bool,
    widthProperty: str,
) -> Any:
    ...


def workspaceControlState(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    defaultTopLeftCorner: Tuple[int, int],
    defaultWidthHeight: Tuple[int, int],
    exists: bool,
    height: int,
    leftEdge: int,
    maximized: bool,
    remove: bool,
    topEdge: int,
    topLeftCorner: Tuple[int, int],
    width: int,
    widthHeight: Tuple[int, int],
) -> Any:
    ...


def workspaceLayoutManager(
    edit: bool,
    query: bool,
    collapseMainWindowControls: Tuple[str, bool],
    current: bool,
    delete: str,
    i: str,
    listLayouts: bool,
    listModuleLayouts: bool,
    listUserLayouts: bool,
    modified: str,
    parentWorkspaceControl: str,
    restoreMainWindowControls: bool,
    reset: bool,
    save: bool,
    saveAs: str,
    setCurrent: str,
    setCurrentCallback: str,
    setModifiedCallback: str,
    type: str,
) -> Any:
    ...


def workspacePanel(
    arg0: str,
    /,
    edit: bool,
    query: bool,
    defineTemplate: str,
    exists: bool,
    mainWindow: bool,
    useTemplate: str,
) -> Any:
    ...


def wrinkle(
    *args: List[str],
    axis: Tuple[float, float, float],
    branchDepth: int,
    branchCount: int,
    crease: List[str],
    center: Tuple[float, float, float],
    dropoffDistance: float,
    envelope: float,
    randomness: float,
    style: str,
    thickness: float,
    uvSpace: Tuple[float, float, float, float, float],
    wrinkleCount: int,
    wrinkleIntensity: float,
) -> Any:
    ...


def wrinkleContext(*args, **kwargs) -> Any:
    ...


def writeTake(*args, **kwargs) -> Any:
    ...


def xform(
    *args: List[str],
    query: bool,
    absolute: bool,
    boundingBox: bool,
    boundingBoxInvisible: bool,
    centerPivots: bool,
    centerPivotsOnComponents: bool,
    deletePriorHistory: bool,
    euler: bool,
    matrix: Tuple[
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
    ],
    objectSpace: bool,
    preserve: bool,
    pivots: Tuple[float, float, float],
    preserveUV: bool,
    relative: bool,
    rotateAxis: Tuple[float, float, float],
    reflectionAboutBBox: bool,
    reflectionAboutOrigin: bool,
    reflectionAboutX: bool,
    reflectionAboutY: bool,
    reflectionAboutZ: bool,
    reflection: bool,
    reflectionTolerance: float,
    rotation: Tuple[float, float, float],
    rotateOrder: str,
    rotatePivot: Tuple[float, float, float],
    rotateTranslation: Tuple[float, float, float],
    scale: Tuple[float, float, float],
    shear: Tuple[float, float, float],
    scalePivot: Tuple[float, float, float],
    scaleTranslation: Tuple[float, float, float],
    translation: Tuple[float, float, float],
    worldSpaceDistance: bool,
    worldSpace: bool,
    zeroTransformPivots: bool,
) -> Any:
    ...


def xformConstraint(
    edit: bool, query: bool, live: bool, alongNormal: bool, type: str
) -> Any:
    ...


def xpmPicker(*args, **kwargs) -> Any:
    ...
