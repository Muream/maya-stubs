# fmt: off
from typing import *
from typing_extensions import Self
from _typeshed import Incomplete


class MAttributeParameterMapping(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def allowConnection(self: Self, *args: Any, **kwargs: Any) -> Any:
        """allowConnection() -> bool

        This method returns true if Maya is allowed to connect other shade fragments to the parameter named by this mapping.
        """
        ...
    def allowRename(self: Self, *args: Any, **kwargs: Any) -> Any:
        """allowRename() -> bool

        This method returns true if the parameter named by this mapping may be renamed in the final shading effect.
        If false, name collisions of parameters will be unresolved and results will be unpredictable.
        """
        ...
    def attributeName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """attributeName() -> string

        Get the attribute name for this mapping.
        """
        ...
    def parameterName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """parameterName() -> string

        Get the parameter name for this mapping.
        """
        ...
    def resolvedParameterName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """resolvedParameterName() -> string

        Get the resolved parameter name for this mapping. After the fragment has been joined with other
        fragments to form the final shading effect its parameters are renamed to prevent name collisions.
        This returns the name of the parameter on the final shading effect.
        This name is useful in MPxShadingNodeOverride::updateShader() for setting parameter values manually.

        If the fragment has not yet been joined with other fragments, this will return the same string as parameterName().
        """
        ...

class MAttributeParameterMappingList(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __getitem__(self: Self, key: Any) -> Any:
        """Return self[key]."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __len__(self: Self) -> Any:
        """Return len(self)."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """append(MAttributeParameterMapping) -> self

        Add a mapping to the list. The list makes a copy; ownership of the original is left with the caller.
        """
        ...
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clear() -> self

        Clear all mappings from the list.
        """
        ...
    def findByAttributeName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """findByAttributeName(attributeName) -> MAttributeParameterMapping

        Find a mapping by attribute name.
        This will return the first mapping found with a matching attribute name.
        """
        ...
    def findByParameterName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """findByParameterName(parameterName) -> MAttributeParameterMapping

        Find a mapping by parameter name.
        This will return the first mapping found with a matching parameter name.
        """
        ...

class MBlendState(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def desc(self: Self, *args: Any, **kwargs: Any) -> Any:
        """desc() -> MBlendStateDesc

        Get the blend state descriptor that was used to create the state object.
        """
        ...
    kAdd: int = ...
    kAlphaChannel: int = ...
    kBlendFactor: int = ...
    kBlueChannel: int = ...
    kBothInvSourceAlpha: int = ...
    kBothSourceAlpha: int = ...
    kDestinationAlpha: int = ...
    kDestinationColor: int = ...
    kGreenChannel: int = ...
    kInvBlendFactor: int = ...
    kInvDestinationAlpha: int = ...
    kInvDestinationColor: int = ...
    kInvSourceAlpha: int = ...
    kInvSourceColor: int = ...
    kMax: int = ...
    kMaxTargets: int = ...
    kMin: int = ...
    kNoChannels: int = ...
    kOne: int = ...
    kRGBAChannels: int = ...
    kRGBChannels: int = ...
    kRedChannel: int = ...
    kReverseSubtract: int = ...
    kSourceAlpha: int = ...
    kSourceAlphaSat: int = ...
    kSourceColor: int = ...
    kSubtract: int = ...
    kZero: int = ...
    def resourceHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """resourceHandle() -> long

        Returns a long containing a C++ 'void' pointer which points to the draw API dependent handle for a blend state.
        For OpenGL, such a handle does not exist and a NULL pointer will be returned.
        For DirectX, a pointer to a Direct3D state will be returned.
        """
        ...

class MBlendStateDesc(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    @property
    def alphaToCoverageEnable(*args: Any, **kwargs: Any) -> Any:
        """Enable alpha to coverage. Default false"""
        ...
    @alphaToCoverageEnable.setter
    def alphaToCoverageEnable(*args: Any, **kwargs: Any) -> Any:
        """Enable alpha to coverage. Default false"""
        ...
    @property
    def blendFactor(*args: Any, **kwargs: Any) -> Any:
        """Global blend factor, default (1,1,1,1)"""
        ...
    @blendFactor.setter
    def blendFactor(*args: Any, **kwargs: Any) -> Any:
        """Global blend factor, default (1,1,1,1)"""
        ...
    @property
    def independentBlendEnable(*args: Any, **kwargs: Any) -> Any:
        """Use TargetBlends[0] if false or individual blend states if true. Default false"""
        ...
    @independentBlendEnable.setter
    def independentBlendEnable(*args: Any, **kwargs: Any) -> Any:
        """Use TargetBlends[0] if false or individual blend states if true. Default false"""
        ...
    @property
    def multiSampleMask(*args: Any, **kwargs: Any) -> Any:
        """Each bit in this mask, starting at the least significant bit (LSB), controls modification of one of the samples in a multisample render target"""
        ...
    @multiSampleMask.setter
    def multiSampleMask(*args: Any, **kwargs: Any) -> Any:
        """Each bit in this mask, starting at the least significant bit (LSB), controls modification of one of the samples in a multisample render target"""
        ...
    def setDefaults(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDefaults() -> self

        Set all values for the blend state to their default values.
        """
        ...
    @property
    def targetBlends(*args: Any, **kwargs: Any) -> Any:
        """An array of 8 MTargetBlendDesc, one for each target"""
        ...
    @targetBlends.setter
    def targetBlends(*args: Any, **kwargs: Any) -> Any:
        """An array of 8 MTargetBlendDesc, one for each target"""
        ...

class MCameraOverride(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    @property
    def mCameraPath(*args: Any, **kwargs: Any) -> Any:
        """Camera path override"""
        ...
    @mCameraPath.setter
    def mCameraPath(*args: Any, **kwargs: Any) -> Any:
        """Camera path override"""
        ...
    @property
    def mFarClippingPlane(*args: Any, **kwargs: Any) -> Any:
        """Far clipping plane override"""
        ...
    @mFarClippingPlane.setter
    def mFarClippingPlane(*args: Any, **kwargs: Any) -> Any:
        """Far clipping plane override"""
        ...
    @property
    def mHiddenCameraList(*args: Any, **kwargs: Any) -> Any:
        """List of cameras that should not be made visible when rendering"""
        ...
    @mHiddenCameraList.setter
    def mHiddenCameraList(*args: Any, **kwargs: Any) -> Any:
        """List of cameras that should not be made visible when rendering"""
        ...
    @property
    def mNearClippingPlane(*args: Any, **kwargs: Any) -> Any:
        """Near clipping plane override"""
        ...
    @mNearClippingPlane.setter
    def mNearClippingPlane(*args: Any, **kwargs: Any) -> Any:
        """Near clipping plane override"""
        ...
    @property
    def mProjectionMatrix(*args: Any, **kwargs: Any) -> Any:
        """Camera projection matrix override"""
        ...
    @mProjectionMatrix.setter
    def mProjectionMatrix(*args: Any, **kwargs: Any) -> Any:
        """Camera projection matrix override"""
        ...
    @property
    def mUseFarClippingPlane(*args: Any, **kwargs: Any) -> Any:
        """Whether to use the far clipping plane override"""
        ...
    @mUseFarClippingPlane.setter
    def mUseFarClippingPlane(*args: Any, **kwargs: Any) -> Any:
        """Whether to use the far clipping plane override"""
        ...
    @property
    def mUseHiddenCameraList(*args: Any, **kwargs: Any) -> Any:
        """Whether to use hidden camera list override"""
        ...
    @mUseHiddenCameraList.setter
    def mUseHiddenCameraList(*args: Any, **kwargs: Any) -> Any:
        """Whether to use hidden camera list override"""
        ...
    @property
    def mUseNearClippingPlane(*args: Any, **kwargs: Any) -> Any:
        """Whether to use the near clipping plane override"""
        ...
    @mUseNearClippingPlane.setter
    def mUseNearClippingPlane(*args: Any, **kwargs: Any) -> Any:
        """Whether to use the near clipping plane override"""
        ...
    @property
    def mUseProjectionMatrix(*args: Any, **kwargs: Any) -> Any:
        """Whether to use the projection matrix override"""
        ...
    @mUseProjectionMatrix.setter
    def mUseProjectionMatrix(*args: Any, **kwargs: Any) -> Any:
        """Whether to use the projection matrix override"""
        ...
    @property
    def mUseViewMatrix(*args: Any, **kwargs: Any) -> Any:
        """Whether to use the view matrix override"""
        ...
    @mUseViewMatrix.setter
    def mUseViewMatrix(*args: Any, **kwargs: Any) -> Any:
        """Whether to use the view matrix override"""
        ...
    @property
    def mViewMatrix(*args: Any, **kwargs: Any) -> Any:
        """Camera view matrix override"""
        ...
    @mViewMatrix.setter
    def mViewMatrix(*args: Any, **kwargs: Any) -> Any:
        """Camera view matrix override"""
        ...

class MClearOperation(MRenderOperation):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def clearColor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clearColor() -> [float, float, float, float]

        Query the first clear color values.
        """
        ...
    def clearColor2(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clearColor2() -> [float, float, float, float]

        Query the second clear color values.
        """
        ...
    def clearDepth(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clearDepth() -> float

        Query the clear depth value.
        """
        ...
    def clearGradient(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clearGradient() -> bool

        Query if the clear should clear with a vertical color gradient.
        """
        ...
    def clearStencil(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clearStencil() -> int

        Query the stencil clear value.
        """
        ...
    def enableSRGBWrite(self: Self, *args: Any, **kwargs: Any) -> Any:
        """enableSRGBWrite() -> bool

        Return whether to enable GPU based gamma correction during pixel writes.
        """
        ...
    kClear: int = ...
    kClearAll: int = ...
    kClearColor: int = ...
    kClearDepth: int = ...
    kClearNone: int = ...
    kClearStencil: int = ...
    kHUDRender: int = ...
    kPresentTarget: int = ...
    kQuadRender: int = ...
    kSceneRender: int = ...
    kUserDefined: int = ...
    def mask(self: Self, *args: Any, **kwargs: Any) -> Any:
        """mask() -> int

        Query the clear mask.
        """
        ...
    def name(self: Self, *args: Any, **kwargs: Any) -> Any:
        """name() -> string

        Returns the name of the render operator.
        """
        ...
    def operationType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """operationType() -> int

        Returns the type of a render operator.
        """
        ...
    def overridesColors(self: Self, *args: Any, **kwargs: Any) -> Any:
        """overridesColors() -> bool

        Query whether clear colors are set by the override or come from Maya's preferences.
        """
        ...
    def setClearColor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setClearColor([float, float, float, float]) -> self

        Set the first clear color values.
        """
        ...
    def setClearColor2(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setClearColor2([float, float, float, float]) -> self

        Set the second clear color values.
        """
        ...
    def setClearDepth(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setClearDepth(float) -> self

        Set the clear depth value.
        """
        ...
    def setClearGradient(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setClearGradient(bool) -> self

        Set whether to clear with a vertical color gradient.
        """
        ...
    def setClearStencil(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setClearStencil(int) -> self

        Set the clear stencil value.
        """
        ...
    def setMask(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setMask(int) -> self

        Set the clear mask to define which channels to clear.
        """
        ...
    def setOverridesColors(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setOverridesColors(bool) -> self

        Set the enabled state to control whether the clear operation overrides Maya's color preferences.
        """
        ...
    def targetOverrideList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """targetOverrideList() -> list of MRenderTarget

        Return a list of render target which will be used as the target overrides for the operation.
        """
        ...
    def viewportRectangleOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """viewportRectangleOverride() -> MFloatPoint

        Query for a viewport rectangle override.
        """
        ...

class MColorManagementUtilities(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def getColorTransformCacheIdForInputSpace(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getColorTransformCacheIdForInputSpace(inputSpaceName) -> transformId

        Utility function to retrieve the id of a color transform
        based on the input color space name provided.

        The color transform id corresponds to a color transform that
        converts colors from the input color space specified to the scene
        rendering space

        For example, given the name of the input color space of a node,
        this function retrieves the id of the color transform to be used
        for mapping colors from input space to rendering space.  For nodes
        that have such a color space attribute, the transform id is meant
        to be written by a file translator plug-in to a renderer file
        alongside the node information. This id corresponds to a color
        transform contained in the color transform data retrieved by
        MRenderUtilities::getColorTransformData.

        * inputSpaceName (string) - Name of the color space of the node.

        Returns identifier of the color transform required to be 
        applied to the node.
        """
        ...
    def getColorTransformCacheIdForOutputTransform(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getColorTransformCacheIdForOutputTransform() -> transformId

        Utility function to retrieve the id of the color transform to be applied on the final output.

        The color transform id corresponds to a color transform that
        converts colors of the rendered image to a target color space.

        This id corresponds to a color transform contained in the color
        transform data retrieved by the MColorTransformData class.

        Returns identifier of the color transform required to be 
        applied on the rendered image
        """
        ...
    def getColorTransformData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getColorTransformData() -> (size, data)

        Obtain a reference to opaque data containing the color transform
        information needed to render the scene.

        This block of data is meant to be written by a file translator
        plug-in to a renderer file.  With the help of the SynColor SDK and
        this block of data, the external renderer can  reproduce the same
        color transformations as in Maya

        Returns the color transform data block info (bytearray).
        """
        ...
    def isColorManagementAvailable(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isColorManagementAvailable() -> Boolean

        Returns whether color management is available for the current scene.

        True if color management is enabled.
        """
        ...
    def isColorManagementEnabled(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isColorManagementEnabled() -> Boolean

        Returns whether color management is enabled for the current scene.

        True if color management is enabled.
        """
        ...

class MComponentDataIndexing(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def componentType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """componentType() -> MComponentType

        Get the component type that the vertex indices represent.
        """
        ...
    def indices(self: Self, *args: Any, **kwargs: Any) -> Any:
        """indices() -> MUintArray

        Get the array of vertex indices for the component.
        """
        ...
    kFaceVertex: int = ...
    def setComponentType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setComponentType(MComponentType) -> self

        Set the component type that the vertex indices represent.
        """
        ...

class MComponentDataIndexingList(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __getitem__(self: Self, key: Any) -> Any:
        """Return self[key]."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __len__(self: Self) -> Any:
        """Return len(self)."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """append(MComponentDataIndexing) -> bool

        Add a MComponentDataIndexing to the list. Creates and stores a copy which is owned by the list.
        """
        ...
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clear() -> self

        Clear the list.
        """
        ...
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """remove(index) -> bool

        Remove a MComponentDataIndexing from the list.
        """
        ...

class MDepthNormalizationDescription(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    @property
    def fDepthBias(*args: Any, **kwargs: Any) -> Any:
        """Bias to apply to depth value"""
        ...
    @fDepthBias.setter
    def fDepthBias(*args: Any, **kwargs: Any) -> Any:
        """Bias to apply to depth value"""
        ...
    @property
    def fDepthScale(*args: Any, **kwargs: Any) -> Any:
        """Scale to apply to depth values"""
        ...
    @fDepthScale.setter
    def fDepthScale(*args: Any, **kwargs: Any) -> Any:
        """Scale to apply to depth values"""
        ...
    @property
    def fFarClipDistance(*args: Any, **kwargs: Any) -> Any:
        """Far clip plane of a camera"""
        ...
    @fFarClipDistance.setter
    def fFarClipDistance(*args: Any, **kwargs: Any) -> Any:
        """Far clip plane of a camera"""
        ...
    @property
    def fNearClipDistance(*args: Any, **kwargs: Any) -> Any:
        """Near clip plane of a camera"""
        ...
    @fNearClipDistance.setter
    def fNearClipDistance(*args: Any, **kwargs: Any) -> Any:
        """Near clip plane of a camera"""
        ...

class MDepthStencilState(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def desc(self: Self, *args: Any, **kwargs: Any) -> Any:
        """desc() -> MDepthStencilStateDesc

        Get the depth-stencil state descriptor that was used to create the state object.
        """
        ...
    kDecrementStencil: int = ...
    kDecrementStencilSat: int = ...
    kIncrementStencil: int = ...
    kIncrementStencilSat: int = ...
    kInvertStencil: int = ...
    kKeepStencil: int = ...
    kReplaceStencil: int = ...
    kZeroStencil: int = ...
    def resourceHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """resourceHandle() -> long

        Returns a long containing a C++ 'void' pointer which points to the draw API dependent handle for a depth-stencil state.
        For OpenGL, such a handle does not exist and a NULL pointer will be returned.
        For DirectX, a pointer to a Direct3D state will be returned.
        """
        ...

class MDepthStencilStateDesc(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    @property
    def backFace(*args: Any, **kwargs: Any) -> Any:
        """Sets the stencil op for the back facing fragments"""
        ...
    @backFace.setter
    def backFace(*args: Any, **kwargs: Any) -> Any:
        """Sets the stencil op for the back facing fragments"""
        ...
    @property
    def depthEnable(*args: Any, **kwargs: Any) -> Any:
        """Enables depth buffer reads and compares, default true"""
        ...
    @depthEnable.setter
    def depthEnable(*args: Any, **kwargs: Any) -> Any:
        """Enables depth buffer reads and compares, default true"""
        ...
    @property
    def depthFunc(*args: Any, **kwargs: Any) -> Any:
        """Sets the depth buffer comparison function, default less than"""
        ...
    @depthFunc.setter
    def depthFunc(*args: Any, **kwargs: Any) -> Any:
        """Sets the depth buffer comparison function, default less than"""
        ...
    @property
    def depthWriteEnable(*args: Any, **kwargs: Any) -> Any:
        """Enables depth buffer writes, default true"""
        ...
    @depthWriteEnable.setter
    def depthWriteEnable(*args: Any, **kwargs: Any) -> Any:
        """Enables depth buffer writes, default true"""
        ...
    @property
    def frontFace(*args: Any, **kwargs: Any) -> Any:
        """Sets the stencil op for the front facing fragments"""
        ...
    @frontFace.setter
    def frontFace(*args: Any, **kwargs: Any) -> Any:
        """Sets the stencil op for the front facing fragments"""
        ...
    def setDefaults(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDefaults() -> self

        Set all values for the depth stencil state to their default values.
        """
        ...
    @property
    def stencilEnable(*args: Any, **kwargs: Any) -> Any:
        """Enables stencil buffer operation"""
        ...
    @stencilEnable.setter
    def stencilEnable(*args: Any, **kwargs: Any) -> Any:
        """Enables stencil buffer operation"""
        ...
    @property
    def stencilReadMask(*args: Any, **kwargs: Any) -> Any:
        """Sets a bitwise stencil buffer read mask, default 0xff"""
        ...
    @stencilReadMask.setter
    def stencilReadMask(*args: Any, **kwargs: Any) -> Any:
        """Sets a bitwise stencil buffer read mask, default 0xff"""
        ...
    @property
    def stencilReferenceVal(*args: Any, **kwargs: Any) -> Any:
        """Sets the stencil reference value"""
        ...
    @stencilReferenceVal.setter
    def stencilReferenceVal(*args: Any, **kwargs: Any) -> Any:
        """Sets the stencil reference value"""
        ...
    @property
    def stencilWriteMask(*args: Any, **kwargs: Any) -> Any:
        """Sets a bitwise stencil buffer write mask, default 0xff"""
        ...
    @stencilWriteMask.setter
    def stencilWriteMask(*args: Any, **kwargs: Any) -> Any:
        """Sets a bitwise stencil buffer write mask, default 0xff"""
        ...

class MDrawContext(MFrameContext):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def classificationExclusions(self: Self, *args: Any, **kwargs: Any) -> Any:
        """classificationExclusions() -> [classification strings]

        Get a list of drawdb strings for object which are excluded from display
        """
        ...
    def copyCurrentColorRenderTarget(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copyCurrentColorRenderTarget(string) -> MRenderTarget

        Get a copy of the current color render target.
        When the object is no longer needed, MRenderTargetManager::releaseRenderTarget() should be called
        to notify the target manager that the caller is done with the render target.
        """
        ...
    def copyCurrentColorRenderTargetToTexture(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copyCurrentColorRenderTargetToTexture() -> MTexture

        Get a copy of the current color render target as a texture.
        When the texture is no longer needed, MTextureManager::releaseTexture() should be called.
        """
        ...
    def copyCurrentDepthRenderTarget(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copyCurrentDepthRenderTarget(string) -> MRenderTarget

        Get a copy of the current depth render target.
        When the object is no longer needed, MRenderTargetManager::releaseRenderTarget() should be called
        to notify the target manager that the caller is done with the render target.
        """
        ...
    def copyCurrentDepthRenderTargetToTexture(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copyCurrentDepthRenderTargetToTexture() -> MTexture

        Get a copy of the current depth render target as a texture.
        When the texture is no longer needed, MTextureManager::releaseTexture() should be called.
        """
        ...
    def getBackgroundParameters(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getBackgroundParameters() -> [displayGradient, clearColorFlag, clearDepthFlag, clearStencilFlag, clearColor1, clearColor2, clearDepthValue, clearStencilValue]

        Get parameters related to how the background is cleared
        """
        ...
    def getCurrentCameraPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getCurrentCameraPath() -> MDagPath

        Get the path to the camera being used to render the current frame.
        """
        ...
    def getCurrentColorRenderTarget(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getCurrentColorRenderTarget() -> MRenderTarget

        Get current color render target.
        Calling code is responsible for invoking MRenderTargetManager::releaseRenderTarget() to release the reference to the target after use.
        """
        ...
    def getCurrentDepthRenderTarget(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getCurrentDepthRenderTarget() -> MRenderTarget

        Get current depth render target.
        Calling code is responsible for invoking MRenderTargetManager::releaseRenderTarget() to release the reference to the target after use.
        """
        ...
    def getDOFParameters(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getDOFParameters() -> [enabled, focalDistance, alpha]

        Get the parameters generated by Maya for the circle-of-confusion depth shader used
        for a pass used when computing depth of field.


        This pass is indicated by the pass semantic MPassContext::kDOFPassSemantic.
        The shader fragment used is called cocDepthSurface.
        The XML wrapper can be queried from MFragmentManager or using the 'ogs -xml maya_CocDepthSurface' command.
        """
        ...
    def getDepthRange(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getDepthRange() -> [float, float]

        Get the depth range which specifies the mapping of depth values from normalized device coordinates to window coordinates.
        The depth range values are normally 0.0 and 1.0.
        """
        ...
    def getDisplayStyle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getDisplayStyle() -> int

        The DisplayStyle enums can be use to test the bit field for the enabling of any
        of the listed display modes. For example to test for wireframe on shaded the test
        would be test against the bit for kGourandShaded or kFlatShaded as well as testing
        against the bit for kWireframe.

          MFrameContext.kGouraudShaded        Shaded display.
          MFrameContext.kWireFrame            Wire frame display.
          MFrameContext.kBoundingBox          Bounding box display.
          MFrameContext.kTextured             Textured display.
          MFrameContext.kDefaultMaterial      Default material display.
          MFrameContext.kXrayJoint            X-ray joint display.
          MFrameContext.kXray                 X-ray display.
          MFrameContext.kTwoSidedLighting     Two-sided lighting enabled.
          MFrameContext.kFlatShaded	         Flat shading display.
          MFrameContext.kShadeActiveOnly      Shade active object only.
          MFrameContext.kXrayActiveComponents X-ray active components.
          MFrameContext.kBackfaceCulling		 Backface culling enabled.
          MFrameContext.kSmoothWireframe	     Smooth wireframe enabled.
        """
        ...
    def getEnvironmentParameters(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getEnvironmentParameters() -> [bool, string]

        Get parameters for currently used environment. Note that this information is set
        per viewport and so might change between draw calls if multiple viewports are
        displayed at the same time.
        Return the destination (type and name) that the renderer is drawing to.
        """
        ...
    def getFrameStamp(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFrameStamp() -> long

        Returns the current frame stamp.
        """
        ...
    def getFrustumBox(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFrustumBox() -> MBoundingBox

        Get the bounding box of the current view frustum in world space.
        """
        ...
    def getGlobalLineWidth(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getGlobalLineWidth() -> float

        Get global line width.
        """
        ...
    def getHwFogParameters(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getHwFogParameters() -> [enabled, mode, start, end, density, color]

        Get all the hardware fog parameters.

        Hardware fog parameters include:

        - hardware fog enabled
        - hardware fog mode: Linear, Exponential, Exponential squared.
          The possible values are:
             MFrameContext::kFogLinear : Linear fog
             MFrameContext::kFogExp : Exponential fog
             MFrameContext::kFogExp2 : Exponential squared fog
        - hardware fog start: The near distance used in the linear fog.
        - hardware fog end: The far distance used in the linear fog.
        - hardware fog density: The density of the exponential fog.
        - hardware fog color: (r, g, b, a).
        """
        ...
    def getLightInformation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getLightInformation(lightNumber, lightFilter=kFilteredToLightLimit) -> [positions, direction, intensity, color, hasDirection, hasPosition]

        Return common lighting information for a given active light.
        """
        ...
    def getLightLimit(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getLightLimit() -> int

        Get the current light limit.
        """
        ...
    def getLightParameterInformation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getLightParameterInformation(lightNumber, lightFilter=kFilteredToLightLimit) -> MLightParameterInformation

        Return parameter information for a given active light.
        """
        ...
    def getLightingMode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getLightingMode() -> int

        Get the current light mode.

          MFrameContext.kNoLighting	      Use no light
          MFrameContext.kAmbientLight      Use global ambient light
          MFrameContext.kLightDefault      Use default light
          MFrameContext.kSelectedLights    Use lights which are selected
          MFrameContext.kSceneLights       Use all lights in the scene
          MFrameContext.kCustomLights      Use a custom set of lights which are not part of the scene. Currently this applies for use in the Hypershade Material Viewer panel
        """
        ...
    def getMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getMatrix(int) -> MMatrix

        Get a matrix value of a certain type.
        Note that not all types are available for querying in MFrameContext.
        Return None if matrix type not available from MFrameContext.
        For a list of matrix type, see MDrawContext.semanticToMatrixType() description.
        """
        ...
    def getPassContext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPassContext() -> MPassContext

        Access the current pass context.
        """
        ...
    def getPostEffectEnabled(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPostEffectEnabled(int) -> bool

        Returns if a given post effect is currently enabled.

          MFrameContext.kAmbientOcclusion    Screen-space ambient occlusion
          MFrameContext.kMotionBlur          2D Motion blur
          MFrameContext.kGammaCorrection     Gamma correction
          MFrameContext.kDepthOfField        Depth of field
          MFrameContext.kAntiAliasing        Hardware multi-sampling
        """
        ...
    def getRenderOverrideInformation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getRenderOverrideInformation() -> [overrideName]

        Get information about any render override
        """
        ...
    def getRenderTargetSize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getRenderTargetSize() -> [int, int]

        Get the size of the render target (output buffer) being rendered into.
        The dimensions of the target are in pixels
        """
        ...
    def getSceneBox(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getSceneBox() -> MBoundingBox

        Get a bounding box of the scene in world space.
        """
        ...
    def getStateManager(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getStateManager() -> MStateManager

        Access the GPU state manager for the current draw context.
        """
        ...
    def getTransparencyAlgorithm(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getTransparencyAlgorithm() -> int

        Get the current transparency algoritm.

          MFrameContext.kUnsorted            Unsorted transparent object drawing
          MFrameContext.kObjectSorting       Object sorting of transparent objects
          MFrameContext.kWeightedAverage     Weight average transparency
          MFrameContext.kDepthPeeling        Depth-peel transparency
        """
        ...
    def getTuple(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getTuple(int) -> MDoubleArray

        Get a tuple (vector, position or single) value of a certain type.
        Note that not all types are available for querying in MFrameContext.
        Return None if unknown tuple type.
        """
        ...
    def getViewportDimensions(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getViewportDimensions() -> [originX, originY, width, height]

        Get the viewport dimensions. The origin is the upper left corner of the viewport.
        """
        ...
    def inUserInteraction(self: Self, *args: Any, **kwargs: Any) -> Any:
        """inUserInteraction() -> bool

        Returns True during any interactive refresh, as when user is interacting with the scene
        in any way including camera changes, object or component TRS changes, etc.
        """
        ...
    k2dViewport: int = ...
    k3dViewport: int = ...
    kAmbientLight: int = ...
    kAmbientOcclusion: int = ...
    kAntiAliasing: int = ...
    kBackfaceCulling: int = ...
    kBoundingBox: int = ...
    kCustomLights: int = ...
    kDefaultMaterial: int = ...
    kDepthOfField: int = ...
    kDepthPeeling: int = ...
    kExcludeAll: int = ...
    kExcludeCVs: int = ...
    kExcludeCameras: int = ...
    kExcludeClipGhosts: int = ...
    kExcludeControllers: int = ...
    kExcludeDeformers: int = ...
    kExcludeDimensions: int = ...
    kExcludeDynamicConstraints: int = ...
    kExcludeDynamics: int = ...
    kExcludeFluids: int = ...
    kExcludeFollicles: int = ...
    kExcludeGreasePencils: int = ...
    kExcludeGrid: int = ...
    kExcludeHUD: int = ...
    kExcludeHairSystems: int = ...
    kExcludeHoldOuts: int = ...
    kExcludeHulls: int = ...
    kExcludeIkHandles: int = ...
    kExcludeImagePlane: int = ...
    kExcludeJoints: int = ...
    kExcludeLights: int = ...
    kExcludeLocators: int = ...
    kExcludeManipulators: int = ...
    kExcludeMeshes: int = ...
    kExcludeMotionTrails: int = ...
    kExcludeNCloths: int = ...
    kExcludeNParticles: int = ...
    kExcludeNRigids: int = ...
    kExcludeNone: int = ...
    kExcludeNurbsCurves: int = ...
    kExcludeNurbsSurfaces: int = ...
    kExcludeParticleInstancers: int = ...
    kExcludePivots: int = ...
    kExcludePlanes: int = ...
    kExcludePluginShapes: int = ...
    kExcludeSelectHandles: int = ...
    kExcludeStrokes: int = ...
    kExcludeSubdivSurfaces: int = ...
    kExcludeTextures: int = ...
    kFilteredIgnoreLightLimit: int = ...
    kFilteredToLightLimit: int = ...
    kFlatShaded: int = ...
    kFogExp: int = ...
    kFogExp2: int = ...
    kFogLinear: int = ...
    kGammaCorrection: int = ...
    kGouraudShaded: int = ...
    kImage: int = ...
    kLightDefault: int = ...
    kMotionBlur: int = ...
    kNoLighting: int = ...
    kObjectSorting: int = ...
    kProjectionInverseMtx: int = ...
    kProjectionMtx: int = ...
    kProjectionTranposeMtx: int = ...
    kProjectionTranspInverseMtx: int = ...
    kSceneLights: int = ...
    kSelectedLights: int = ...
    kShadeActiveOnly: int = ...
    kSmoothWireframe: int = ...
    kTextured: int = ...
    kTwoSidedLighting: int = ...
    kUnsorted: int = ...
    kViewColorTransformEnabled: int = ...
    kViewDirection: int = ...
    kViewFarClipValue: int = ...
    kViewInverseMtx: int = ...
    kViewMtx: int = ...
    kViewNearClipValue: int = ...
    kViewPosition: int = ...
    kViewProjInverseMtx: int = ...
    kViewProjMtx: int = ...
    kViewProjTranposeMtx: int = ...
    kViewProjTranspInverseMtx: int = ...
    kViewRight: int = ...
    kViewTranspInverseMtx: int = ...
    kViewTransposeMtx: int = ...
    kViewUnnormalizedFarClipValue: int = ...
    kViewUnnormlizedNearClipValue: int = ...
    kViewUp: int = ...
    kViewportPixelSize: int = ...
    kWeightedAverage: int = ...
    kWireFrame: int = ...
    kWireFrameOnShadedNone: int = ...
    kWireFrameOnShadedReduced: int = ...
    kWireframeOnShadedFull: int = ...
    kWorldInverseMtx: int = ...
    kWorldMtx: int = ...
    kWorldTranspInverseMtx: int = ...
    kWorldTransposeMtx: int = ...
    kWorldViewInverseMtx: int = ...
    kWorldViewMtx: int = ...
    kWorldViewProjInverseMtx: int = ...
    kWorldViewProjMtx: int = ...
    kWorldViewProjTranspInverseMtx: int = ...
    kWorldViewProjTransposeMtx: int = ...
    kWorldViewTranspInverseMtx: int = ...
    kWorldViewTransposeMtx: int = ...
    kXray: int = ...
    kXrayActiveComponents: int = ...
    kXrayJoint: int = ...
    def numberOfActiveLights(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numberOfActiveLights(lightFilter=kFilteredToLightLimit) -> int

        Return the number of available lights to render the scene,
        only considering lights which pass the filter option.
        """
        ...
    def objectTypeExclusions(self: Self, *args: Any, **kwargs: Any) -> Any:
        """objectTypeExclusions() -> long

        Get the object type exclusions as a bitfield.
        	The bitfield can be tested using the bits defined by class statics starting with kExclude.
        """
        ...
    def renderingDestination(self: Self, *args: Any, **kwargs: Any) -> Any:
        """renderingDestination() -> [int, destinationName]

        Return the destination (type and name) that the renderer is drawing to.

          MFrameContext.k3dViewport    Rendering to an interactive 3d viewport
          MFrameContext.k2dViewport    Rendering to an interactive 2d viewport such as the render view
          MFrameContext.kImage         Rendering to an image
        """
        ...
    def semanticToMatrixType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """semanticToMatrixType(string) -> int

        Given a semantic name return the corresponding matrix enumeration that can be used to retrieve a matrix value via the getMatrix() method.

          MFrameContext.kWorldMtx                        Object to world matrix
          MFrameContext.kWorldTransposeMtx               Object to world matrix transpose
          MFrameContext.kWorldInverseMtx                 Object to world matrix inverse
          MFrameContext.kWorldTranspInverseMtx           Object to world matrix transpose inverse (adjoint)
          MFrameContext.kViewMtx                         World to view matrix
          MFrameContext.kViewTransposeMtx                World to view matrix tranpose
          MFrameContext.kViewInverseMtx                  World to view matrix inverse
          MFrameContext.kViewTranspInverseMtx            World to view matrix transpose inverse (adjoint)
          MFrameContext.kProjectionMtx                   Projection matrix
          MFrameContext.kProjectionTranposeMtx           Projection matrix tranpose
          MFrameContext.kProjectionInverseMtx            Projection matrix inverse
          MFrameContext.kProjectionTranspInverseMtx      Projection matrix tranpose inverse (adjoint)
          MFrameContext.kViewProjMtx                     View * projection matrix
          MFrameContext.kViewProjTranposeMtx             View * projection matrix tranpose
          MFrameContext.kViewProjInverseMtx              View * projection matrix inverse
          MFrameContext.kViewProjTranspInverseMtx        View * projection matrix tranpose inverse (adjoint)
          MFrameContext.kWorldViewMtx                    World * view matrix
          MFrameContext.kWorldViewTransposeMtx           World * view matrix transpose
          MFrameContext.kWorldViewInverseMtx             World * view matrix inverse
          MFrameContext.kWorldViewTranspInverseMtx       World * view matrix transpose inverse (adjoint)
          MFrameContext.kWorldViewProjMtx                World * view * projection matrix
          MFrameContext.kWorldViewProjTransposeMtx       World * view * projection matrix transpose
          MFrameContext.kWorldViewProjInverseMtx         World * view * projection matrix inverse
          MFrameContext.kWorldViewProjTranspInverseMtx   World * view * projection matrix tranpose inverse (adjoint)
        """
        ...
    def semanticToTupleType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """semanticToTupleType(string) -> int

        Given a semantic name return the corresponding tuple enumeration that can be used to retrieve a value via the getTuple() method.

          MFrameContext.kViewPosition         View position
          MFrameContext.kViewDirection        View direction vector
          MFrameContext.kViewUp               View up vector
          MFrameContext.kViewRight            View right vector
          MFrameContext.kViewportPixelSize    Viewport size in pixels (single value)
          MFrameContext.kViewNearClipValue    Camera near clip value (single value)
          MFrameContext.kViewFarClipValue     Camera far clip value (single value)
          MFrameContext.kViewUnnormlizedNearClipValue Unnormalized camera near clip value (single value)
        	 MFrameContext.kViewUnnormalizedFarClipValue Unnormalized camera far clip value (single value)
        """
        ...
    def shadeTemplates(self: Self, *args: Any, **kwargs: Any) -> Any:
        """shadeTemplates() -> bool

        Returns the display preference indicating whether templated objects should be drawn shaded.
        """
        ...
    def userChangingViewContext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """userChangingViewContext() -> bool

        Returns True during any interactive refresh, as when user is	changing the view using view context
        tools such as tumble, dolly or track.
        """
        ...
    def viewDirectionAlongNegZ(self: Self, *args: Any, **kwargs: Any) -> Any:
        """viewDirectionAlongNegZ() -> bool

        Return whether the view direction is pointing down the -Z axis.
        """
        ...
    def wireOnShadedMode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """wireOnShadedMode() -> int

        Returns the global user display preference which indicates how wireframe should be drawn on top of objects while in shaded mode.

        Please refer to documentation on the 'Wireframe-on-shaded' option under the 'Display->View' tab in the preferences window.

        Note that 'viewport in wireframe on shaded mode' is a different option which is per viewport. This can be tested by testing if
        a shaded mode is set as well as wireframe mode. Refer to the enumerations DisplayStyle and the method getDisplayStyle().


          MFrameContext.kWireframeOnShadedFull      Draw wireframe
          MFrameContext.kWireFrameOnShadedReduced   Draw wireframe but with reduced quality
          MFrameContext.kWireFrameOnShadedNone      Do not draw wireframe
        """
        ...

class MDrawRegistry(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def deregisterComponentConverter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deregisterComponentConverter(renderItemName) -> None

        Deregister an implementation of MPxComponentConverter.
        """
        ...
    def deregisterDrawOverrideCreator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deregisterDrawOverrideCreator(drawClassification, registrantId) -> None

        Deregister an implementation of MPxDrawOverride.
        """
        ...
    def deregisterGeometryOverrideCreator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deregisterGeometryOverrideCreator(drawClassification, registrantId) -> None

        Deregister an implementation of MPxGeometryOverride.
        """
        ...
    def deregisterImagePlaneOverrideCreator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deregisterImagePlaneOverrideCreator(drawClassification, registrantId) -> None

        Deregister an implementation of MPxImagePlaneOverride.
        """
        ...
    def deregisterIndexBufferMutator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deregisterIndexBufferMutator(primitiveType) -> None

        Deregister an implementation of MPxIndexBufferMutator.
        """
        ...
    def deregisterPrimitiveGenerator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deregisterPrimitiveGenerator(primitiveType) -> None

        Deregister an implementation of MPxPrimitiveGenerator.
        """
        ...
    def deregisterShaderOverrideCreator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deregisterShaderOverrideCreator(drawClassification, registrantId) -> None

        Deregister an implementation of MPxShaderOverride.
        """
        ...
    def deregisterShadingNodeOverrideCreator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deregisterShadingNodeOverrideCreator(drawClassification, registrantId) -> None

        Deregister an implementation of MPxShadingNodeOverride.
        """
        ...
    def deregisterSubSceneOverrideCreator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deregisterSubSceneOverrideCreator(drawClassification, registrantId) -> None

        Deregister an implementation of MPxSubSceneOverride.
        """
        ...
    def deregisterSurfaceShadingNodeOverrideCreator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deregisterSurfaceShadingNodeOverrideCreator(drawClassification, registrantId) -> None

        Deregister an implementation of MPxSurfaceShadingNodeOverride.
        """
        ...
    def deregisterVertexBufferGenerator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deregisterVertexBufferGenerator(bufferName) -> None

        Deregister an implementation of MPxVertexBufferGenerator.
        """
        ...
    def deregisterVertexBufferMutator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deregisterVertexBufferMutator(bufferName) -> None

        Deregister an implementation of MPxVertexBufferMutator.
        """
        ...
    def registerComponentConverter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """registerComponentConverter(renderItemName, creator) -> None

        Register an implementation of MPxComponentConverter to use with render items that have the specified name.
        """
        ...
    def registerDrawOverrideCreator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """registerDrawOverrideCreator(drawClassification, registrantId, creator) -> None

        Register an implementation of MPxDrawOverride to use with DAG objects that have the specified, draw-specific classification string.
        """
        ...
    def registerGeometryOverrideCreator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """registerGeometryOverrideCreator(drawClassification, registrantId, creator) -> None

        Register an implementation of MPxGeometryOverride to use with nodes that have the specified, draw-specific classification string.
        """
        ...
    def registerImagePlaneOverrideCreator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """registerImagePlaneOverrideCreator(drawClassification, registrantId, creator) -> None

        Register an implementation of MPxImagePlaneOverride to use with DAG objects that have the specified, draw-specific classification string.
        """
        ...
    def registerIndexBufferMutator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """registerIndexBufferMutator(primitiveType, creator) -> None

        Register an implementation of MPxIndexBufferMutator to generate custom primitive types for shapes.
        """
        ...
    def registerPrimitiveGenerator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """registerPrimitiveGenerator(primitiveType, creator) -> None

        Register an implementation of MPxPrimitiveGenerator to generate custom primitive types for shapes.
        """
        ...
    def registerShaderOverrideCreator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """registerShaderOverrideCreator(drawClassification, registrantId, creator) -> None

        Register an implementation of MPxShaderOverride to use with nodes that have the specified, draw-specific classification string.
        """
        ...
    def registerShadingNodeOverrideCreator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """registerShadingNodeOverrideCreator(drawClassification, registrantId, creator) -> None

        Register an implementation of MPxShadingNodeOverride to use with nodes that have the specified, draw-specific classification string.
        """
        ...
    def registerSubSceneOverrideCreator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """registerSubSceneOverrideCreator(drawClassification, registrantId, creator) -> None

        Register an implementation of MPxSubSceneOverride to use with DAG objects that have the specified, draw-specific classification string.
        """
        ...
    def registerSurfaceShadingNodeOverrideCreator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """registerSurfaceShadingNodeOverrideCreator(drawClassification, registrantId, creator) -> None

        Register an implementation of MPxSurfaceShadingNodeOverride to use with surface shaders that have the specified, draw-specific classification string.
        """
        ...
    def registerVertexBufferGenerator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """registerVertexBufferGenerator(bufferName, creator) -> None

        Register an implementation of MPxVertexBufferGenerator to provide custom vertex streams for shapes.
        """
        ...
    def registerVertexBufferMutator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """registerVertexBufferMutator(bufferName, creator) -> None

        Register an implementation of MPxVertexBufferMutator to provide custom vertex streams for shapes.
        """
        ...

class MFragmentManager(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def addAutomaticShaderStageInput(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addAutomaticShaderStageInput(int, string, string, int, bool) -> bool

        Add a parameter to the list of automatic input parameters for a specified
        shader stage. If an input parameter with the same name or semantic is found
        unconnected in a fragment graph during compilation, the parameter will be
        automatically connected with a matching source, which can be either a member
        in the shader stage input structure or a registered fragment, depending on
        whether or not the parameter is a varying input.

        The method will fail if the parameter name has been registered already. A
        plug-in can add a unique prefix to the parameter name to avoid conflicts.

        - shaderStage (int) - Shader stage
        - parameterName (string) - Name of the parameter
        - semantic (string) - Semantic of the parameter
        - parameterType (int) - Type of the parameter
        - isVaryingInput (bool) - Whether or not the parameter is a varying input
        """
        ...
    def addDomainShaderInputNameMapping(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addDomainShaderInputNameMapping(string, string) -> bool

        Add a mapping between a parameter name (realParamName) and a transient
        name (domainParamName) which is used in domain shader. If realParamName
        is found in the domain shader output struct when compiling a shader fragment
        graph, it will temporarily be treated as domainParamName to connect to a
        matching source, which can be either a member in the domain shader stage input
        struct or a registered tessellation evaluation fragment, depending on whether
        or not domainParamName has been registered as a varying input.

        The method will fail if a mapping has already been added for realParamName.

        - realParamName (string) - Real name of the parameter
        - domainParamName (string) - Transient name of the parameter in domain shader
        """
        ...
    def addFragmentGraphFromBuffer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addFragmentGraphFromBuffer(buffer) -> string

        Add a new fragment graph to the manager.
        The fragment graph is defined as XML stored in a string buffer.Returns name of the registered fragment graph, or empty string on failure.

        - buffer (string) - String containing an XML description of the fragment graph.
        """
        ...
    def addFragmentGraphFromFile(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addFragmentGraphFromFile(fileName) -> string

        Add a new fragment graph to the manager.
        The fragment graph is defined as XML stored in the given file.Returns name of the registered fragment graph, or empty string on failure.

        - fileName (string) - The name of the file containing the fragment graph description.
        """
        ...
    def addFragmentPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addFragmentPath(path) -> bool

        Add a path to the list of fragment search paths used when parsing the file path for any
        methods which add fragments to the manager from files on disk.
        """
        ...
    def addShadeFragmentFromBuffer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addShadeFragmentFromBuffer(buffer, hidden) -> string

        Add a new fragment to the manager.
        The fragment is defined as XML stored in a string buffer.
        Returns name of the registered fragment, or empty string on failure.

        - buffer (string) - String containing an XML description of the fragment.
        - hidden (bool) - If True, this fragment will not appear in the list returned by fragmentList()
                          and it will not be possible to query the XML for it using getFragmentXML().
        """
        ...
    def addShadeFragmentFromFile(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addShadeFragmentFromFile(fileName, hidden) -> string

        Add a new fragment to the manager.
        The fragment is defined as XML stored in the given file.
        Returns name of the registered fragment, or empty string on failure.

        - fileName (string) - The name of the file containing the fragment description.
        - hidden (bool) - If True, this fragment will not appear in the list returned by fragmentList()
                          and it will not be possible to query the XML for it using getFragmentXML().
        """
        ...
    def findDomainShaderInputName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """findDomainShaderInputName(string) -> string

        Find the transient name which is used in domain shader.

        Returns transient name of the parameter, or empty string on failure.

        - realParamName (string) - Real name of the parameter
        """
        ...
    def fragmentList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """fragmentList() -> list of string

        Returns a list of the names of all registered fragments and fragment graphs.
        """
        ...
    def getEffectOutputDirectory(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getEffectOutputDirectory() -> string

        Get the directory to be used for effect file output.
        """
        ...
    def getFragmentXML(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFragmentXML(fragmentName) -> string
        getFragmentXML(shadingNode, includeUpstreamNodes=False, objectContext=None) -> string

        Get the XML representation of the named fragment or fragment graph.
        Return None if failed
        - fragmentName (string) - The name of the fragment to get the XML for.

        Get XML code for the fragment graph Maya would use to represent the given shading node in Viewport 2.0.
        Return None if failed
        - shadingNode (MObject) - The node to get the XML code for.
        - includeUpstreamNodes (bool) - Return the XML for the entire fragment graph rooted at the given shading node if True.
        - objectContext (MDagPath) - Optional path to an instance that is associated with the shading node to provide object context.
        """
        ...
    def getIntermediateGraphOutputDirectory(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getIntermediateGraphOutputDirectory() -> string

        Get the directory to be used for intermediate fragment graph output.
        """
        ...
    def hasFragment(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasFragment(string) -> bool

        Returns True if a fragment of the given name has been registered with the fragment manager.
        """
        ...
    kDomainShader: int = ...
    kGeometryShader: int = ...
    kHullConstantShader: int = ...
    kHullShader: int = ...
    kPixelShader: int = ...
    kVertexShader: int = ...
    def removeAutomaticShaderStageInput(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeAutomaticShaderStageInput(int, string) -> bool

        Remove a parameter from the list of automatic input parameters for a
        specified shader stage.

        The method will fail if the parameter name hasn't been registered yet. A
        plug-in should keep track of its own parameters and clean them up at an
        appropriate time.

        - shaderStage (int) - Shader stage
        - parameterName (string) - Name of the parameter
        """
        ...
    def removeDomainShaderInputNameMapping(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeDomainShaderInputNameMapping(string) -> bool

        Remove a mapping between a parameter name (realParamName) and a transient
        name (domainParamName) which is used in domain shader.

        The method will fail if a mapping hasn't been added for realParamName yet.

        - realParamName (string) - Real name of the parameter
        """
        ...
    def removeFragment(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeFragment(fragmentName) -> bool

        Remove a named fragment or fragment graph from the fragment manager. This
        can be used to remove registered fragments on plug-in unload.

        Any fragment may be removed including those defined by Maya. In this way
        users may replace default Maya fragments with custom fragments. When
        replacing an existing Maya fragment it is important to maintain the same
        fragment interface (i.e. input and output parameters) otherwise Maya's
        behavior will be undefined. Maya's behavior will also be undefined if a
        default Maya fragment is removed without replacing it.

        Returns True if the fragment was successfuly removed from the fragment manager.
        """
        ...
    def setEffectOutputDirectory(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setEffectOutputDirectory(string) -> self

        Set the path to use for dumping final effect files.
        """
        ...
    def setIntermediateGraphOutputDirectory(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setIntermediateGraphOutputDirectory(string) -> self

        Set the path to use for dumping intermediate fragment graph XML files.
        """
        ...

class MFrameContext(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def classificationExclusions(self: Self, *args: Any, **kwargs: Any) -> Any:
        """classificationExclusions() -> [classification strings]

        Get a list of drawdb strings for object which are excluded from display
        """
        ...
    def getBackgroundParameters(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getBackgroundParameters() -> [displayGradient, clearColorFlag, clearDepthFlag, clearStencilFlag, clearColor1, clearColor2, clearDepthValue, clearStencilValue]

        Get parameters related to how the background is cleared
        """
        ...
    def getCurrentCameraPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getCurrentCameraPath() -> MDagPath

        Get the path to the camera being used to render the current frame.
        """
        ...
    def getCurrentColorRenderTarget(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getCurrentColorRenderTarget() -> MRenderTarget

        Get current color render target.
        Calling code is responsible for invoking MRenderTargetManager::releaseRenderTarget() to release the reference to the target after use.
        """
        ...
    def getCurrentDepthRenderTarget(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getCurrentDepthRenderTarget() -> MRenderTarget

        Get current depth render target.
        Calling code is responsible for invoking MRenderTargetManager::releaseRenderTarget() to release the reference to the target after use.
        """
        ...
    def getDOFParameters(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getDOFParameters() -> [enabled, focalDistance, alpha]

        Get the parameters generated by Maya for the circle-of-confusion depth shader used
        for a pass used when computing depth of field.


        This pass is indicated by the pass semantic MPassContext::kDOFPassSemantic.
        The shader fragment used is called cocDepthSurface.
        The XML wrapper can be queried from MFragmentManager or using the 'ogs -xml maya_CocDepthSurface' command.
        """
        ...
    def getDisplayStyle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getDisplayStyle() -> int

        The DisplayStyle enums can be use to test the bit field for the enabling of any
        of the listed display modes. For example to test for wireframe on shaded the test
        would be test against the bit for kGourandShaded or kFlatShaded as well as testing
        against the bit for kWireframe.

          MFrameContext.kGouraudShaded        Shaded display.
          MFrameContext.kWireFrame            Wire frame display.
          MFrameContext.kBoundingBox          Bounding box display.
          MFrameContext.kTextured             Textured display.
          MFrameContext.kDefaultMaterial      Default material display.
          MFrameContext.kXrayJoint            X-ray joint display.
          MFrameContext.kXray                 X-ray display.
          MFrameContext.kTwoSidedLighting     Two-sided lighting enabled.
          MFrameContext.kFlatShaded	         Flat shading display.
          MFrameContext.kShadeActiveOnly      Shade active object only.
          MFrameContext.kXrayActiveComponents X-ray active components.
          MFrameContext.kBackfaceCulling		 Backface culling enabled.
          MFrameContext.kSmoothWireframe	     Smooth wireframe enabled.
        """
        ...
    def getEnvironmentParameters(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getEnvironmentParameters() -> [bool, string]

        Get parameters for currently used environment. Note that this information is set
        per viewport and so might change between draw calls if multiple viewports are
        displayed at the same time.
        Return the destination (type and name) that the renderer is drawing to.
        """
        ...
    def getGlobalLineWidth(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getGlobalLineWidth() -> float

        Get global line width.
        """
        ...
    def getHwFogParameters(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getHwFogParameters() -> [enabled, mode, start, end, density, color]

        Get all the hardware fog parameters.

        Hardware fog parameters include:

        - hardware fog enabled
        - hardware fog mode: Linear, Exponential, Exponential squared.
          The possible values are:
             MFrameContext::kFogLinear : Linear fog
             MFrameContext::kFogExp : Exponential fog
             MFrameContext::kFogExp2 : Exponential squared fog
        - hardware fog start: The near distance used in the linear fog.
        - hardware fog end: The far distance used in the linear fog.
        - hardware fog density: The density of the exponential fog.
        - hardware fog color: (r, g, b, a).
        """
        ...
    def getLightLimit(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getLightLimit() -> int

        Get the current light limit.
        """
        ...
    def getLightingMode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getLightingMode() -> int

        Get the current light mode.

          MFrameContext.kNoLighting	      Use no light
          MFrameContext.kAmbientLight      Use global ambient light
          MFrameContext.kLightDefault      Use default light
          MFrameContext.kSelectedLights    Use lights which are selected
          MFrameContext.kSceneLights       Use all lights in the scene
          MFrameContext.kCustomLights      Use a custom set of lights which are not part of the scene. Currently this applies for use in the Hypershade Material Viewer panel
        """
        ...
    def getMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getMatrix(int) -> MMatrix

        Get a matrix value of a certain type.
        Note that not all types are available for querying in MFrameContext.
        Return None if matrix type not available from MFrameContext.
        For a list of matrix type, see MDrawContext.semanticToMatrixType() description.
        """
        ...
    def getPostEffectEnabled(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPostEffectEnabled(int) -> bool

        Returns if a given post effect is currently enabled.

          MFrameContext.kAmbientOcclusion    Screen-space ambient occlusion
          MFrameContext.kMotionBlur          2D Motion blur
          MFrameContext.kGammaCorrection     Gamma correction
          MFrameContext.kDepthOfField        Depth of field
          MFrameContext.kAntiAliasing        Hardware multi-sampling
        """
        ...
    def getRenderOverrideInformation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getRenderOverrideInformation() -> [overrideName]

        Get information about any render override
        """
        ...
    def getTransparencyAlgorithm(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getTransparencyAlgorithm() -> int

        Get the current transparency algoritm.

          MFrameContext.kUnsorted            Unsorted transparent object drawing
          MFrameContext.kObjectSorting       Object sorting of transparent objects
          MFrameContext.kWeightedAverage     Weight average transparency
          MFrameContext.kDepthPeeling        Depth-peel transparency
        """
        ...
    def getTuple(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getTuple(int) -> MDoubleArray

        Get a tuple (vector, position or single) value of a certain type.
        Note that not all types are available for querying in MFrameContext.
        Return None if unknown tuple type.
        """
        ...
    def getViewportDimensions(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getViewportDimensions() -> [originX, originY, width, height]

        Get the viewport dimensions. The origin is the upper left corner of the viewport.
        """
        ...
    def inUserInteraction(self: Self, *args: Any, **kwargs: Any) -> Any:
        """inUserInteraction() -> bool

        Returns True during any interactive refresh, as when user is interacting with the scene
        in any way including camera changes, object or component TRS changes, etc.
        """
        ...
    k2dViewport: int = ...
    k3dViewport: int = ...
    kAmbientLight: int = ...
    kAmbientOcclusion: int = ...
    kAntiAliasing: int = ...
    kBackfaceCulling: int = ...
    kBoundingBox: int = ...
    kCustomLights: int = ...
    kDefaultMaterial: int = ...
    kDepthOfField: int = ...
    kDepthPeeling: int = ...
    kExcludeAll: int = ...
    kExcludeCVs: int = ...
    kExcludeCameras: int = ...
    kExcludeClipGhosts: int = ...
    kExcludeControllers: int = ...
    kExcludeDeformers: int = ...
    kExcludeDimensions: int = ...
    kExcludeDynamicConstraints: int = ...
    kExcludeDynamics: int = ...
    kExcludeFluids: int = ...
    kExcludeFollicles: int = ...
    kExcludeGreasePencils: int = ...
    kExcludeGrid: int = ...
    kExcludeHUD: int = ...
    kExcludeHairSystems: int = ...
    kExcludeHoldOuts: int = ...
    kExcludeHulls: int = ...
    kExcludeIkHandles: int = ...
    kExcludeImagePlane: int = ...
    kExcludeJoints: int = ...
    kExcludeLights: int = ...
    kExcludeLocators: int = ...
    kExcludeManipulators: int = ...
    kExcludeMeshes: int = ...
    kExcludeMotionTrails: int = ...
    kExcludeNCloths: int = ...
    kExcludeNParticles: int = ...
    kExcludeNRigids: int = ...
    kExcludeNone: int = ...
    kExcludeNurbsCurves: int = ...
    kExcludeNurbsSurfaces: int = ...
    kExcludeParticleInstancers: int = ...
    kExcludePivots: int = ...
    kExcludePlanes: int = ...
    kExcludePluginShapes: int = ...
    kExcludeSelectHandles: int = ...
    kExcludeStrokes: int = ...
    kExcludeSubdivSurfaces: int = ...
    kExcludeTextures: int = ...
    kFlatShaded: int = ...
    kFogExp: int = ...
    kFogExp2: int = ...
    kFogLinear: int = ...
    kGammaCorrection: int = ...
    kGouraudShaded: int = ...
    kImage: int = ...
    kLightDefault: int = ...
    kMotionBlur: int = ...
    kNoLighting: int = ...
    kObjectSorting: int = ...
    kProjectionInverseMtx: int = ...
    kProjectionMtx: int = ...
    kProjectionTranposeMtx: int = ...
    kProjectionTranspInverseMtx: int = ...
    kSceneLights: int = ...
    kSelectedLights: int = ...
    kShadeActiveOnly: int = ...
    kSmoothWireframe: int = ...
    kTextured: int = ...
    kTwoSidedLighting: int = ...
    kUnsorted: int = ...
    kViewColorTransformEnabled: int = ...
    kViewDirection: int = ...
    kViewFarClipValue: int = ...
    kViewInverseMtx: int = ...
    kViewMtx: int = ...
    kViewNearClipValue: int = ...
    kViewPosition: int = ...
    kViewProjInverseMtx: int = ...
    kViewProjMtx: int = ...
    kViewProjTranposeMtx: int = ...
    kViewProjTranspInverseMtx: int = ...
    kViewRight: int = ...
    kViewTranspInverseMtx: int = ...
    kViewTransposeMtx: int = ...
    kViewUnnormalizedFarClipValue: int = ...
    kViewUnnormlizedNearClipValue: int = ...
    kViewUp: int = ...
    kViewportPixelSize: int = ...
    kWeightedAverage: int = ...
    kWireFrame: int = ...
    kWireFrameOnShadedNone: int = ...
    kWireFrameOnShadedReduced: int = ...
    kWireframeOnShadedFull: int = ...
    kWorldInverseMtx: int = ...
    kWorldMtx: int = ...
    kWorldTranspInverseMtx: int = ...
    kWorldTransposeMtx: int = ...
    kWorldViewInverseMtx: int = ...
    kWorldViewMtx: int = ...
    kWorldViewProjInverseMtx: int = ...
    kWorldViewProjMtx: int = ...
    kWorldViewProjTranspInverseMtx: int = ...
    kWorldViewProjTransposeMtx: int = ...
    kWorldViewTranspInverseMtx: int = ...
    kWorldViewTransposeMtx: int = ...
    kXray: int = ...
    kXrayActiveComponents: int = ...
    kXrayJoint: int = ...
    def objectTypeExclusions(self: Self, *args: Any, **kwargs: Any) -> Any:
        """objectTypeExclusions() -> long

        Get the object type exclusions as a bitfield.
        	The bitfield can be tested using the bits defined by class statics starting with kExclude.
        """
        ...
    def renderingDestination(self: Self, *args: Any, **kwargs: Any) -> Any:
        """renderingDestination() -> [int, destinationName]

        Return the destination (type and name) that the renderer is drawing to.

          MFrameContext.k3dViewport    Rendering to an interactive 3d viewport
          MFrameContext.k2dViewport    Rendering to an interactive 2d viewport such as the render view
          MFrameContext.kImage         Rendering to an image
        """
        ...
    def semanticToMatrixType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """semanticToMatrixType(string) -> int

        Given a semantic name return the corresponding matrix enumeration that can be used to retrieve a matrix value via the getMatrix() method.

          MFrameContext.kWorldMtx                        Object to world matrix
          MFrameContext.kWorldTransposeMtx               Object to world matrix transpose
          MFrameContext.kWorldInverseMtx                 Object to world matrix inverse
          MFrameContext.kWorldTranspInverseMtx           Object to world matrix transpose inverse (adjoint)
          MFrameContext.kViewMtx                         World to view matrix
          MFrameContext.kViewTransposeMtx                World to view matrix tranpose
          MFrameContext.kViewInverseMtx                  World to view matrix inverse
          MFrameContext.kViewTranspInverseMtx            World to view matrix transpose inverse (adjoint)
          MFrameContext.kProjectionMtx                   Projection matrix
          MFrameContext.kProjectionTranposeMtx           Projection matrix tranpose
          MFrameContext.kProjectionInverseMtx            Projection matrix inverse
          MFrameContext.kProjectionTranspInverseMtx      Projection matrix tranpose inverse (adjoint)
          MFrameContext.kViewProjMtx                     View * projection matrix
          MFrameContext.kViewProjTranposeMtx             View * projection matrix tranpose
          MFrameContext.kViewProjInverseMtx              View * projection matrix inverse
          MFrameContext.kViewProjTranspInverseMtx        View * projection matrix tranpose inverse (adjoint)
          MFrameContext.kWorldViewMtx                    World * view matrix
          MFrameContext.kWorldViewTransposeMtx           World * view matrix transpose
          MFrameContext.kWorldViewInverseMtx             World * view matrix inverse
          MFrameContext.kWorldViewTranspInverseMtx       World * view matrix transpose inverse (adjoint)
          MFrameContext.kWorldViewProjMtx                World * view * projection matrix
          MFrameContext.kWorldViewProjTransposeMtx       World * view * projection matrix transpose
          MFrameContext.kWorldViewProjInverseMtx         World * view * projection matrix inverse
          MFrameContext.kWorldViewProjTranspInverseMtx   World * view * projection matrix tranpose inverse (adjoint)
        """
        ...
    def semanticToTupleType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """semanticToTupleType(string) -> int

        Given a semantic name return the corresponding tuple enumeration that can be used to retrieve a value via the getTuple() method.

          MFrameContext.kViewPosition         View position
          MFrameContext.kViewDirection        View direction vector
          MFrameContext.kViewUp               View up vector
          MFrameContext.kViewRight            View right vector
          MFrameContext.kViewportPixelSize    Viewport size in pixels (single value)
          MFrameContext.kViewNearClipValue    Camera near clip value (single value)
          MFrameContext.kViewFarClipValue     Camera far clip value (single value)
          MFrameContext.kViewUnnormlizedNearClipValue Unnormalized camera near clip value (single value)
        	 MFrameContext.kViewUnnormalizedFarClipValue Unnormalized camera far clip value (single value)
        """
        ...
    def shadeTemplates(self: Self, *args: Any, **kwargs: Any) -> Any:
        """shadeTemplates() -> bool

        Returns the display preference indicating whether templated objects should be drawn shaded.
        """
        ...
    def userChangingViewContext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """userChangingViewContext() -> bool

        Returns True during any interactive refresh, as when user is	changing the view using view context
        tools such as tumble, dolly or track.
        """
        ...
    def wireOnShadedMode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """wireOnShadedMode() -> int

        Returns the global user display preference which indicates how wireframe should be drawn on top of objects while in shaded mode.

        Please refer to documentation on the 'Wireframe-on-shaded' option under the 'Display->View' tab in the preferences window.

        Note that 'viewport in wireframe on shaded mode' is a different option which is per viewport. This can be tested by testing if
        a shaded mode is set as well as wireframe mode. Refer to the enumerations DisplayStyle and the method getDisplayStyle().


          MFrameContext.kWireframeOnShadedFull      Draw wireframe
          MFrameContext.kWireFrameOnShadedReduced   Draw wireframe but with reduced quality
          MFrameContext.kWireFrameOnShadedNone      Do not draw wireframe
        """
        ...

class MGeometry(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def addIndexBuffer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addIndexBuffer(MIndexBuffer) -> bool

        Buffers cannot be added to the same object twice.Adds a index buffer to this MGeometry object.
        The buffer can only be added to this object once but may be added to others.
        """
        ...
    def addVertexBuffer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addVertexBuffer(MVertexBuffer) -> bool

        Adds a vertex buffer to this MGeometry object.
        The buffer can only be added to this object once but may be added to others.
        """
        ...
    def createIndexBuffer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """createIndexBuffer(int) -> MIndexBuffer

        Creates a index buffer which is bound to this MGeometry object and cannot be used with any other.
        The buffer is automatically added to the MGeometry object so there is no need to call addIndexBuffer().
        See MGeometry.dataTypeString() for a list of valid data types.
        """
        ...
    def createVertexBuffer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """createVertexBuffer(MVertexBufferDescriptor) -> MVertexBuffer

        Creates a vertex buffer which is bound to this MGeometry object and cannot be used with any other.
        The buffer is automatically added to the MGeometry object so there is no need to call addVertexBuffer().
        """
        ...
    def dataTypeString(self: Self, *args: Any, **kwargs: Any) -> Any:
        """dataTypeString(int) -> string

        Get the string name (e.g. 'Unsigned Char') for the following data type values:

          kInvalidType     Invalid element type (default value)
          kFloat           IEEE single precision floating point
          kDouble          IEEE double precision floating point
          kChar            Signed char
          kUnsignedChar    Unsigned char
          kInt16           Signed 16-bit integer
          kUnsignedInt16   Unsigned 16-bit integer
          kInt32           Signed 32-bit integer
          kUnsignedInt32   Unsigned 32-bit integer
        """
        ...
    def deleteIndexBuffer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deleteIndexBuffer(int) -> bool

        Remove a index buffer from this object.
        If the buffer was bound to this object (see createIndexBuffer()) then it will become inactive and any attempt to call any of its methods will result in an exception.
        """
        ...
    def deleteVertexBuffer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deleteVertexBuffer(int) -> bool

        Remove a vertex buffer from this object.
        If the buffer was bound to this object (see createVertexBuffer()) then it will become inactive and any attempt to call any of its methods will result in an exception.
        """
        ...
    def drawModeString(self: Self, *args: Any, **kwargs: Any) -> Any:
        """drawModeString(int) -> string

        Get the string name (e.g. 'Wireframe, Shaded, Textured') for a combination of the following draw mode values:

          kWireframe      Draw in wireframe mode
          kShaded         Draw in shaded mode
          kTextured       Draw in textured mode
          kBoundingBox    Draw in bounding box mode
          kSelectionOnly  Draw only in selection mode

        The draw mode value kAll is a combination of the following modes: kWireframe, kShaded, kTextured, and kBoundingBox
        """
        ...
    def indexBuffer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """indexBuffer(int) -> MIndexBuffer

        Get the index buffer stored at the given index.
        """
        ...
    def indexBufferCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """indexBufferCount() -> int

        Get the number of index buffers contained in this MGeometry object.
        """
        ...
    kAdjacentLineStrip: int = ...
    kAdjacentLines: int = ...
    kAdjacentTriangleStrip: int = ...
    kAdjacentTriangles: int = ...
    kAll: int = ...
    kBitangent: int = ...
    kBoundingBox: int = ...
    kChar: int = ...
    kColor: int = ...
    kDouble: int = ...
    kFloat: int = ...
    kInt16: int = ...
    kInt32: int = ...
    kInvalidPrimitive: int = ...
    kInvalidSemantic: int = ...
    kInvalidType: int = ...
    kLineStrip: int = ...
    kLines: int = ...
    kNormal: int = ...
    kPatch: int = ...
    kPoints: int = ...
    kPosition: int = ...
    kSelectionHighlighting: int = ...
    kSelectionOnly: int = ...
    kShaded: int = ...
    kTangent: int = ...
    kTangentWithSign: int = ...
    kTexture: int = ...
    kTextured: int = ...
    kTriangleStrip: int = ...
    kTriangles: int = ...
    kUnsignedChar: int = ...
    kUnsignedInt16: int = ...
    kUnsignedInt32: int = ...
    kWireframe: int = ...
    def primitiveString(self: Self, *args: Any, **kwargs: Any) -> Any:
        """primitiveString(int) -> string

        Get the string name (e.g. 'Triangles') for the following primitive values:

          kInvalidPrimitive        Default value is not valid
          kPoints                  List of points
          kLines                   List of lines
          kLineStrip               A line strip
          kTriangles               List of triangles
          kTriangleStrip           A triangle strip
          kAdjacentTriangles       A list of triangle with adjacency
          kAdjacentTriangleStrip   A triangle strip with adjacency
          kAdjacentLines           A list of lines with adjacency
          kAdjacentLineStrip       A line strip with adjacency
          kPatch                   A patch
        """
        ...
    def semanticString(self: Self, *args: Any, **kwargs: Any) -> Any:
        """semanticString(int) -> string

        Get the string name (e.g. 'Color') for the following semantic values:

          kInvalidSemantic    Invalid data type (default value)
          kPosition           Position vector
          kNormal             Normal vector
          kTexture            Texture coordinate tuple
          kColor              Color tuple
          kTangent            Tangent vector
          kBitangent          Bi-normal vector
          kTangentWithSign    Tangent vector with winding order sign
        """
        ...
    def vertexBuffer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """vertexBuffer(int) -> MVertexBuffer

        Get the vertex buffer stored at the given index.
        """
        ...
    def vertexBufferCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """vertexBufferCount() -> int

        Get the number of vertex buffers contained in this MGeometry object.
        """
        ...

class MGeometryExtractor(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    kPolyGeom_BaseMesh: int = ...
    kPolyGeom_Normal: int = ...
    kPolyGeom_NotSharing: int = ...
    def minimumBufferSize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """minimumBufferSize(primitiveCount, primitive, primitiveStride=0) -> int

        Get the minimum buffer size required by populateIndexBuffer().

        * primitiveCount (int) - The number of primitives.
        * primitive (int) - The primitive type. See MGeometry.primitiveString() for list of primitive types.
        * primitiveStride (int) - The number of control points in a patch when the type is kPatch.
        """
        ...
    def populateIndexBuffer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """populateIndexBuffer(data, primitiveCount, indexDesc) -> self

        Fill a buffer with geometry indexing data.
        This method will use the information provided in the MIndexBufferDescriptor argument to populate the buffer with the desired indexing data.  The descriptor will describe the surface index type, the primitive type, and the data type.  The populateIndexBuffer method will generate a buffer that matches the request.
        The length of the buffer should be at least the as big as the value returned by minimumBufferSize().

        * data (buffer) - The buffer you want filled.
        * primitiveCount (int) - The number of primitives you expect to be filled in the buffer.
        * indexDesc (MIndexBufferDescriptor) - The description of the buffer you are requesting.
        """
        ...
    def populateVertexBuffer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """populateVertexBuffer(data, vertexCount, bufferDesc) -> self

        Fill a buffer with vertex data.
        This method will use the information provided in the MVertexBufferDescriptor argument to populate the buffer with the desired vertex data.  The descriptor will describe the buffer's name, semantic, and data type.
        The populateVertexBuffer method will supply a buffer that matches the request.  The length of the buffer should be at least (vertexCount * bufferDesc.stride()).
        Values for normals, tangents and bitangents are all normalized.

        * data (buffer) - The buffer you want filled.
        * vertexCount (int) - The vertex count you expect to be filled in the buffer.
        * bufferDesc (MVertexBufferDescriptor) - The description of the buffer you are requesting.
        """
        ...
    def primitiveCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """primitiveCount(indexDesc) -> int

        Returns the number of primitives (triangles, lines, points, etc.) that will be produced for the given indexing requirements.
        Call this method before calling populateIndexBuffer to determine the minimum size the buffer passed into populateIndexBuffer needs to be.

        * indexDesc (MIndexBufferDescriptor) - The description of the index buffer you request the count for.
        """
        ...
    def vertexCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """vertexCount() -> int

        Returns the number of vertices that will be produced for the vertex requirement.
        Call this method before calling populateVertexBuffer to determine the minimum size the buffer passed into populateVertexBuffer needs to be.
        """
        ...

class MGeometryIndexMapping(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def component(self: Self, *args: Any, **kwargs: Any) -> Any:
        """component(int) -> MObject

        Get the component of a geometry.
        """
        ...
    def dagPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """dagPath(int) -> MDagPath

        Get the MDagPath of a geometry.
        """
        ...
    def geometryCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """geometryCount() -> int

        Get the number of geometry described by the mapping.
        """
        ...
    def indexLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """indexLength(int) -> int

        Get the index length of a geometry.
        The index length represents the length of the geometry index data in the index buffer of the consolidated render item.
        """
        ...
    def indexStart(self: Self, *args: Any, **kwargs: Any) -> Any:
        """indexStart(int) -> int

        Get the index start of a geometry.
        The index start represents the offset of the geometry index data in the index buffer of the consolidated render item.
        """
        ...

class MGeometryRequirements(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def addIndexingRequirement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addIndexingRequirement(MIndexBufferDescriptor) -> self

        Add a new indexing requirement to the list of indexing requirements.
        """
        ...
    def addVertexRequirement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addVertexRequirement(MVertexBufferDescriptor) -> self

        Add a new vertex requirement to the list of vertex requirements.
        """
        ...
    def indexingRequirements(self: Self, *args: Any, **kwargs: Any) -> Any:
        """indexingRequirements() -> MIndexBufferDescriptorList

        Get a list of descriptors that specify the geometry indexing requirements of an object.
        """
        ...
    def vertexRequirements(self: Self, *args: Any, **kwargs: Any) -> Any:
        """vertexRequirements() -> MVertexBufferDescriptorList

        Get a list of descriptors that specify the vertex geometry requirements of this object.
        """
        ...

class MGeometryUtilities(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def acquireReferenceGeometry(self: Self, *args: Any, **kwargs: Any) -> Any:
        """acquireReferenceGeometry(shape, requirements) -> MGeometry

        Acquire reference geometry with required buffers.

        The user is responsible for releasing the geometry when it is no longer needed, by calling MGeometryUtilities::releaseReferenceGeometry().


        * shape (int) - The shape of the requested geometry.
        * requirements (MGeometryRequirements) - The list of required index and vertex buffers.

        Valid geometry shapes:
          kDefaultSphere   Sphere with radius 1, centered at 0,0,0.
          kDefaultPlane    Plane with width and height of 1, centered at 0,0,0. Assuming Y-Up orientation: width = x-axis, and height = y-axis.
          kDefaultCube     Cube with width, height and depth of 1, centered at 0,0,0.
        """
        ...
    def displayStatus(self: Self, *args: Any, **kwargs: Any) -> Any:
        """displayStatus(path) -> DisplayStatus

        Returns the display status of the given DAG path. Note that the last selected object will have status kLead
        instead of kActive and if only one object is selected the status will be kLead.

        * path (MDagPath) - The DAG path to get.
        """
        ...
    kActive: int = ...
    kActiveAffected: int = ...
    kActiveComponent: int = ...
    kActiveTemplate: int = ...
    kDefaultCube: int = ...
    kDefaultPlane: int = ...
    kDefaultSphere: int = ...
    kDormant: int = ...
    kHilite: int = ...
    kIntermediateObject: int = ...
    kInvisible: int = ...
    kLead: int = ...
    kLive: int = ...
    kNoStatus: int = ...
    kTemplate: int = ...
    def releaseReferenceGeometry(self: Self, *args: Any, **kwargs: Any) -> Any:
        """releaseReferenceGeometry(geometry) -> None

        Release a generated reference geometry.

        * geometry (MGeometry) - The geometry to delete.
        """
        ...
    def wireframeColor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """wireframeColor(path) -> MColor

        Returns the wireframe color used in Viewport 2.0 for the given DAG path.

        * path (MDagPath) - The DAG path to get wireframe color.
        """
        ...

class MHUDRender(MRenderOperation):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def addUIDrawables(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addUIDrawables(drawManager2D, frameContext) -> self

        Provides access to the 2D version of MUIDrawManager, which can be used to queue up operations to draw simple UI shapes like lines, circles, text, etc.

        This method will only be called when hasUIDrawables() is overridden to return true.

        * drawManager2D (MUIDrawManager) - A UI draw manager which can be used to draw simple 2D geometry, including text. When passing coordinates to the draw manager's methods, only X and Y have meaning. The origin (0, 0) is in the lower-left corner of the view.
        * frameContext (MFrameContext) - Frame level context information.
        """
        ...
    def enableSRGBWrite(self: Self, *args: Any, **kwargs: Any) -> Any:
        """enableSRGBWrite() -> bool

        Return whether to enable GPU based gamma correction during pixel writes.
        """
        ...
    def hasUIDrawables(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasUIDrawables() -> bool

        Query whether addUIDrawables() should be called or not.
        """
        ...
    kClear: int = ...
    kHUDRender: int = ...
    kPresentTarget: int = ...
    kQuadRender: int = ...
    kSceneRender: int = ...
    kUserDefined: int = ...
    def name(self: Self, *args: Any, **kwargs: Any) -> Any:
        """name() -> string

        Returns the unique name for a hud render operation.
        Note that all HUD operations share the same name since they need not be distinguished from one another.
        """
        ...
    def operationType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """operationType() -> int

        Returns the type of a render operator.
        """
        ...
    def targetOverrideList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """targetOverrideList() -> list of MRenderTarget

        Return a list of render target which will be used as the target overrides for the operation.
        """
        ...
    def viewportRectangleOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """viewportRectangleOverride() -> MFloatPoint

        Query for a viewport rectangle override.
        """
        ...

class MIndexBuffer(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def acquire(self: Self, *args: Any, **kwargs: Any) -> Any:
        """acquire(size, writeOnly) -> long

        Get a pointer to memory for the buffer.

        * size (int) - The size of the buffer to acquire.
        * writeOnly (bool) - Specified if the returned memory should be uninitialized or filled with actual buffer content.
                             When the current buffer content is not needed, it is preferable to set the writeOnly flag to true for better performance.
        """
        ...
    def commit(self: Self, *args: Any, **kwargs: Any) -> Any:
        """commit(long) -> self

        Commit the data stored in the memory given by acquire() to the buffer.
        If this method is not called, the acquired buffer will not be used in drawing.
        The pointer must be the same pointer returned from acquire().
        """
        ...
    def dataType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """dataType() -> int

        Get the data type of the buffer.
        See MGeometry.dataTypeString() for a list of valid data types.
        """
        ...
    def hasCustomResourceHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasCustomResourceHandle() -> bool

        Returns true if this index buffer is using a custom resource handle set
        by the plugin using MIndexBuffer.setResourceHandle(long, int).
        """
        ...
    def lockResourceHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """lockResourceHandle() -> self

        Lock the resource handle. The pointer returned from resourceHandle() is
        guaranteed to exist between lockResourceHandle() and unlockResourceHandle().

        MIndexBuffer may store data in system memory, GPU memory or both. Direct
        access to the GPU representation of the data is possible through the
        buffer's resourceHandle(). If the GPU representation of the data is to be
        directly modified using an external graphics or compute API, then
        lockResourceHandle() must be called on the MIndexBuffer once, before any
        modifications to the buffer are made.

        While a resource handle is locked, any external modifications to the GPU
        buffer will be recognized by Maya.

        While a resource handle is locked, consolidated world will take longer to
        consolidate the corresponding object. After unlocking a resource handle,
        consolidated world will take longer to consolidate the corresponding object
        one more time, the first time the unlocked resource handle is consolidated.

        Calling lockResourceHandle() and unlockResourceHandle() on a custom resource
        handle has no effect.

        Reallocating or deleting the GPU representation of the data between
        lockResourceHandle() and unlockResourceHandle() will result in undefined
        behavior. acquire(), commit() and update() may reallocate the GPU representation.
        unload() may delete the GPU representation.

        map() and unmap() will work if they are called between lockResourceHandle()
        and unlockResourceHandle(). They operate on the GPU representation.
        """
        ...
    def map(self: Self, *args: Any, **kwargs: Any) -> Any:
        """map() -> long

        Get a read-only pointer to the existing content of the buffer.
        Writing new content in this memory block is not supported and can lead to unexpected behavior.
        """
        ...
    def resourceHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """resourceHandle() -> long

        Returns a long containing a C++ 'float' pointer which points to the graphics device dependent handle to the vertex indexing data.
        """
        ...
    def setResourceHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setResourceHandle(long, int) -> selfset the graphics-device-dependent hardware buffer resource handle."""
        ...
    def size(self: Self, *args: Any, **kwargs: Any) -> Any:
        """size() -> int

        Get the size of the buffer in units of dataType(). Returns 0 if unallocated.
        """
        ...
    def unload(self: Self, *args: Any, **kwargs: Any) -> Any:
        """unload() -> self

        If the buffer is resident in GPU memory, calling this method will move it to system memory and free the GPU memory.
        """
        ...
    def unlockResourceHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """unlockResourceHandle() -> self

        Unlock the resource handle. The pointer returned from resourceHandle is not
        guaranteed to exist any more.
        See lockResourceHandle() for more details.
        """
        ...
    def unmap(self: Self, *args: Any, **kwargs: Any) -> Any:
        """unmap() -> self

        Release the data exposed by map(). If this method is not called, the buffer will not be recycled.
        """
        ...
    def update(self: Self, *args: Any, **kwargs: Any) -> Any:
        """update(buffer, destOffset, numIndices, truncateIfSmaller) -> self

        Set a portion (or all) of the contents of the MIndexBuffer using the data in the provided software buffer.
        The internal hardware buffer will be allocated or reallocated to fit if required, according to the vertex size from the descriptor.

        * buffer (long) - The input data buffer, starting with the first vertex to copy.
        * destOffset (int) - The offset (in indices) from the beginning of the buffer to start writing to.
        * numIndices (int) - The number of indices to copy.
        * truncateIfSmaller (bool) - If true and offset+numVerts is less than the pre-existing size of the buffer,
                                     then the buffer contents will be truncated to the new size. Truncating the buffer size
                                     will not cause a reallocation and will not lose data before the destOffset.
        """
        ...

class MIndexBufferDescriptor(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    @property
    def component(*args: Any, **kwargs: Any) -> Any:
        """The component associated with the index buffer."""
        ...
    @component.setter
    def component(*args: Any, **kwargs: Any) -> Any:
        """The component associated with the index buffer."""
        ...
    @property
    def dataType(*args: Any, **kwargs: Any) -> Any:
        """The type of data expected to be in the index buffer.
        See MGeometry.dataTypeString() for a list of valid data types.
        """
        ...
    @dataType.setter
    def dataType(*args: Any, **kwargs: Any) -> Any:
        """The type of data expected to be in the index buffer.
        See MGeometry.dataTypeString() for a list of valid data types.
        """
        ...
    @property
    def indexType(*args: Any, **kwargs: Any) -> Any:
        """The indexing type describing what the buffer is used for:
          kVertexPoint
          kEdgeLine
          kTriangleEdge
          kTriangle
          kFaceCenter
          kEditPoint
          kControlVertex
          kHullEdgeLine
          kHullTriangle
          kHullFaceCenter
          kHullEdgeCenter
          kHullUV
          kSubDivEdge
          kTangent
          kCustom
        """
        ...
    @indexType.setter
    def indexType(*args: Any, **kwargs: Any) -> Any:
        """The indexing type describing what the buffer is used for:
          kVertexPoint
          kEdgeLine
          kTriangleEdge
          kTriangle
          kFaceCenter
          kEditPoint
          kControlVertex
          kHullEdgeLine
          kHullTriangle
          kHullFaceCenter
          kHullEdgeCenter
          kHullUV
          kSubDivEdge
          kTangent
          kCustom
        """
        ...
    kControlVertex: int = ...
    kCustom: int = ...
    kEdgeLine: int = ...
    kEditPoint: int = ...
    kFaceCenter: int = ...
    kHullEdgeCenter: int = ...
    kHullEdgeLine: int = ...
    kHullFaceCenter: int = ...
    kHullTriangle: int = ...
    kHullUV: int = ...
    kSubDivEdge: int = ...
    kTangent: int = ...
    kTriangle: int = ...
    kTriangleEdge: int = ...
    kVertexPoint: int = ...
    @property
    def name(*args: Any, **kwargs: Any) -> Any:
        """The name used to describe the type when 'indexType' is set to kCustom."""
        ...
    @name.setter
    def name(*args: Any, **kwargs: Any) -> Any:
        """The name used to describe the type when 'indexType' is set to kCustom."""
        ...
    @property
    def primitive(*args: Any, **kwargs: Any) -> Any:
        """The primitive describing the input layout for each drawable.
        See MGeometry.primitiveString() for a list of valid primitive types.
        """
        ...
    @primitive.setter
    def primitive(*args: Any, **kwargs: Any) -> Any:
        """The primitive describing the input layout for each drawable.
        See MGeometry.primitiveString() for a list of valid primitive types.
        """
        ...
    @property
    def primitiveStride(*args: Any, **kwargs: Any) -> Any:
        """The number of control points used for patch primitives.
        Only meaningful when 'primitive' is set to kPatch.
        """
        ...
    @primitiveStride.setter
    def primitiveStride(*args: Any, **kwargs: Any) -> Any:
        """The number of control points used for patch primitives.
        Only meaningful when 'primitive' is set to kPatch.
        """
        ...

class MIndexBufferDescriptorList(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __getitem__(self: Self, key: Any) -> Any:
        """Return self[key]."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __len__(self: Self) -> Any:
        """Return len(self)."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """append(MIndexBufferDescriptor) -> bool

        Add a descriptor to the list. Creates and stores a copy which is owned by the list.
        """
        ...
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clear() -> self

        Clear the list.
        """
        ...
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """remove(index) -> bool

        Remove a descriptor from the list and delete it.
        """
        ...

class MInitContext(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    @property
    def dagPath(*args: Any, **kwargs: Any) -> Any:
        """A path to the instance of the Maya DAG object for which the shader is being initialized"""
        ...
    @dagPath.setter
    def dagPath(*args: Any, **kwargs: Any) -> Any:
        """A path to the instance of the Maya DAG object for which the shader is being initialized"""
        ...
    @property
    def shader(*args: Any, **kwargs: Any) -> Any:
        """The Maya shading node this override is used for"""
        ...
    @shader.setter
    def shader(*args: Any, **kwargs: Any) -> Any:
        """The Maya shading node this override is used for"""
        ...

class MInitFeedback(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    @property
    def customData(*args: Any, **kwargs: Any) -> Any:
        """Optional user data to be associated with the render item for the shader assignment"""
        ...
    @customData.setter
    def customData(*args: Any, **kwargs: Any) -> Any:
        """Optional user data to be associated with the render item for the shader assignment"""
        ...

class MIntersection(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    @property
    def barycentricCoordinates(*args: Any, **kwargs: Any) -> Any:
        """Get the barycentric coordinates (a, b). Only valid for triangles.
        Follows Tomas Moller & Ben Trumbore, jgt 97 "Fast minimum storage ray/triangle intersection" which means that a point, T(a,b), on a triangle is given by: 
           T(a,b) = (1-a-b)V0 + aV1 + bV2
        where V0, V1, and V2 are the triangle vertices.
        """
        ...
    @barycentricCoordinates.setter
    def barycentricCoordinates(*args: Any, **kwargs: Any) -> Any:
        """Get the barycentric coordinates (a, b). Only valid for triangles.
        Follows Tomas Moller & Ben Trumbore, jgt 97 "Fast minimum storage ray/triangle intersection" which means that a point, T(a,b), on a triangle is given by: 
           T(a,b) = (1-a-b)V0 + aV1 + bV2
        where V0, V1, and V2 are the triangle vertices.
        """
        ...
    @property
    def edgeInterpolantValue(*args: Any, **kwargs: Any) -> Any:
        """The edge interpolant value. Only valid for edges.
        It corresponds to the intersection position on the edge, from 0 to 1 starting at V0 going to V1.
        """
        ...
    @edgeInterpolantValue.setter
    def edgeInterpolantValue(*args: Any, **kwargs: Any) -> Any:
        """The edge interpolant value. Only valid for edges.
        It corresponds to the intersection position on the edge, from 0 to 1 starting at V0 going to V1.
        """
        ...
    @property
    def index(*args: Any, **kwargs: Any) -> Any:
        """The index of the hit vertex, edge or triangle.
        It is the position in the index buffer of the render item geometry when provided, and the position in the vertex buffer if not.
        """
        ...
    @index.setter
    def index(*args: Any, **kwargs: Any) -> Any:
        """The index of the hit vertex, edge or triangle.
        It is the position in the index buffer of the render item geometry when provided, and the position in the vertex buffer if not.
        """
        ...
    @property
    def instanceID(*args: Any, **kwargs: Any) -> Any:
        """The draw instance ID of the render item. Only valid for instanced render items."""
        ...
    @instanceID.setter
    def instanceID(*args: Any, **kwargs: Any) -> Any:
        """The draw instance ID of the render item. Only valid for instanced render items."""
        ...
    @property
    def intersectionPoint(*args: Any, **kwargs: Any) -> Any:
        """The intersection point."""
        ...
    @intersectionPoint.setter
    def intersectionPoint(*args: Any, **kwargs: Any) -> Any:
        """The intersection point."""
        ...
    @property
    def selectionLevel(*args: Any, **kwargs: Any) -> Any:
        """The selection level of the intersection.
        See MSelectionContext::selectionLevel for list of valid level values.
        """
        ...
    @selectionLevel.setter
    def selectionLevel(*args: Any, **kwargs: Any) -> Any:
        """The selection level of the intersection.
        See MSelectionContext::selectionLevel for list of valid level values.
        """
        ...

class MLightParameterInformation(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def arrayParameterCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """arrayParameterCount(string) -> int

        Return the array size of a parameter. If the parameter is not an array then a value of 0 is returned.
        """
        ...
    def getParameter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getParameter(int) -> MIntArraygetParameter(int) -> MFloatArraygetParameter(int) -> MMatrixgetParameter(int) -> MSamplerStateDescgetParameter(int) -> MTexturegetParameter(string) -> MIntArraygetParameter(string) -> MFloatArraygetParameter(string) -> MMatrixgetParameter(string) -> MSamplerStateDescgetParameter(string) -> MTexture

        Get parameter value by name or by semantic.
        If more than one parameter matches the semantic, the value of the first matching parameter found will be returned.
        """
        ...
    def getParameterTextureHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getParameterTextureHandle(int) -> longgetParameterTextureHandle(string) -> long

        Get a resource handle for a texture parameter by name or by semantic.
        Returns a long containing a C++ 'void' pointer which points to the resource handle.
        """
        ...
    kBoolean: int = ...
    kColor: int = ...
    kCosConeAngle: int = ...
    kDecayRate: int = ...
    kDepthRange: int = ...
    kDropoff: int = ...
    kEmitsDiffuse: int = ...
    kEmitsSpecular: int = ...
    kFloat: int = ...
    kFloat2: int = ...
    kFloat3: int = ...
    kFloat4: int = ...
    kFloat4x4Col: int = ...
    kFloat4x4Row: int = ...
    kGlobalShadowOn: int = ...
    kInteger: int = ...
    kIntensity: int = ...
    kInvalid: int = ...
    kIrradianceIn: int = ...
    kLightEnabled: int = ...
    kNoSemantic: int = ...
    kSampler: int = ...
    kShadowBias: int = ...
    kShadowColor: int = ...
    kShadowDirty: int = ...
    kShadowMap: int = ...
    kShadowMapSize: int = ...
    kShadowOn: int = ...
    kShadowSamp: int = ...
    kShadowViewProj: int = ...
    kStartShadowParameters: int = ...
    kTexture2: int = ...
    kTextureCube: int = ...
    kWorldDirection: int = ...
    kWorldPosition: int = ...
    def lightPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """lightPath() -> MDagPath

        Returns the DagPath to the scene light. Will return an unitialized DagPath for default lights.
        """
        ...
    def lightType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """lightType() -> string

        Get the classification of the light node.
        """
        ...
    def parameterList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """parameterList() -> list of string

        Get the names of all light parameters that are accessible.
        """
        ...
    def parameterNames(self: Self, *args: Any, **kwargs: Any) -> Any:
        """parameterNames(int) -> list of string

        Get the name of all parameters on the light which are tagged with the stock semantic.
        """
        ...
    def parameterSemantic(self: Self, *args: Any, **kwargs: Any) -> Any:
        """parameterSemantic(string) -> int

        Get the stock semantic for a named parameter:
          MDrawContext.kNoSemantic       No semantic
          MDrawContext.kLightEnabled     Light is enabled
          MDrawContext.kWorldPosition    World space position
          MDrawContext.kWorldDirection   World space direction
          MDrawContext.kIntensity        Intensity
          MDrawContext.kColor            Color
          MDrawContext.kEmitsDiffuse     Emits diffuse lighting
          MDrawContext.kEmitsSpecular    Emits specular lighting
          MDrawContext.kDecayRate        Decay rate
          MDrawContext.kDropoff          Dropoff
          MDrawContext.kCosConeAngle     Cosine of the cone angle
          MDrawContext.kIrradianceIn     Incoming irradiance
          MDrawContext.kShadowMap        Shadow map
          MDrawContext.kShadowSamp       Shadow map sampler
          MDrawContext.kShadowBias       Shadow map bias
          MDrawContext.kShadowMapSize    Shadow map size
          MDrawContext.kShadowViewProj   Shadow map view projection matrix
          MDrawContext.kShadowColor      Shadow color
          MDrawContext.kGlobalShadowOn   Global toggle for whether shadows are enabled or not
          MDrawContext.kShadowOn         Local toggle per light for whether shadows are enabled or not
          MDrawContext.kShadowDirty      Indicates if the contents of the shadow map are out-of-date or uninitialized
        """
        ...
    def parameterType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """parameterType(string) -> int

        Get the type of the named parameter, returns kInvalid if parameter is not found.

          MDrawContext.kInvalid        Invalid element type (default value)
          MDrawContext.kBoolean        Boolean
          MDrawContext.kInteger        Signed 32-bit integer
          MDrawContext.kFloat          IEEE single precision floating point
          MDrawContext.kFloat2         IEEE single precision floating point (x2)
          MDrawContext.kFloat3         IEEE single precision floating point (x3)
          MDrawContext.kFloat4         IEEE single precision floating point (x4)
          MDrawContext.kFloat4x4Row    IEEE single precision floating point row-major matrix (4x4)
          MDrawContext.kFloat4x4Col    IEEE single precision floating point column-major matrix (4x4)
          MDrawContext.kTexture2       2D texture
          MDrawContext.kSampler        Sampler
        """
        ...

class MPassContext(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def hasShaderOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasShaderOverride() -> bool

        Return if there is a shader instance override set for the current pass.
        """
        ...
    kBeginRenderSemantic: str = ...
    kBeginSceneRenderSemantic: str = ...
    kColorPassSemantic: str = ...
    kCullBackSemantic: str = ...
    kCullFrontSemantic: str = ...
    kDOFPassSemantic: str = ...
    kDepthPassSemantic: str = ...
    kEndRenderSemantic: str = ...
    kEndSceneRenderSemantic: str = ...
    kMaterialOverrideSemantic: str = ...
    kMotionVectorPassSemantic: str = ...
    kNonPEPatternPassSemantic: str = ...
    kNormalDepthPassSemantic: str = ...
    kOpaqueGeometrySemantic: str = ...
    kOpaqueUISemantic: str = ...
    kPEPatternPassSemantic: str = ...
    kPostUIGeometrySemantic: str = ...
    kPreUIGeometrySemantic: str = ...
    kSelectionPassSemantic: str = ...
    kShadowPassSemantic: str = ...
    kTransparentGeometrySemantic: str = ...
    kTransparentPeelAndAvgSemantic: str = ...
    kTransparentPeelSemantic: str = ...
    kTransparentUISemantic: str = ...
    kTransparentWeightedAvgSemantic: str = ...
    kUIGeometrySemantic: str = ...
    kUserPassSemantic: str = ...
    kXrayUISemantic: str = ...
    def passIdentifier(self: Self, *args: Any, **kwargs: Any) -> Any:
        """passIdentifier() -> string

        Return the identifier for the pass context.
        """
        ...
    def passSemantics(self: Self, *args: Any, **kwargs: Any) -> Any:
        """passSemantics() -> list of string

        Return an array of semantics for the pass context.
        """
        ...
    def shaderOverrideInstance(self: Self, *args: Any, **kwargs: Any) -> Any:
        """shaderOverrideInstance() -> MShaderInstance

        Return the shader instance override set for the current pass.

        When the returned new shader instance is no longer needed, MShaderManager::releaseShader() should be called to notify the shader manager that the caller is done with the shader.
        """
        ...

class MPresentTarget(MRenderOperation):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def enableSRGBWrite(self: Self, *args: Any, **kwargs: Any) -> Any:
        """enableSRGBWrite() -> bool

        Return whether to enable GPU based gamma correction during pixel writes.
        """
        ...
    kCenterBuffer: int = ...
    kClear: int = ...
    kHUDRender: int = ...
    kLeftBuffer: int = ...
    kPresentTarget: int = ...
    kQuadRender: int = ...
    kRightBuffer: int = ...
    kSceneRender: int = ...
    kUserDefined: int = ...
    def name(self: Self, *args: Any, **kwargs: Any) -> Any:
        """name() -> string

        Returns the name of the render operator.
        """
        ...
    def operationType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """operationType() -> int

        Returns the type of a render operator.
        """
        ...
    def presentDepth(self: Self, *args: Any, **kwargs: Any) -> Any:
        """presentDepth() -> bool

        Query whether the present operation will display depth values.
        """
        ...
    def setPresentDepth(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPresentDepth(bool) -> self

        Set whether the operation will present depth values.
        """
        ...
    def setTargetBackBuffer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setTargetBackBuffer(int) -> self

        Set the desired back-buffer to use on the output target.
        see MPresentTarget.targetBackBuffer() description for the list of available back-buffers.
        """
        ...
    def targetBackBuffer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """targetBackBuffer() -> int

        Query the desired back-buffer to use on the output target.

          MPresentTarget.kCenterBuffer   Default or 'center' buffer
          MPresentTarget.kLeftBuffer     Left back-buffer
          MPresentTarget.kRightBuffer    Right back-buffer
        """
        ...
    def targetOverrideList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """targetOverrideList() -> list of MRenderTarget

        Return a list of render target which will be used as the target overrides for the operation.
        """
        ...
    def viewportRectangleOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """viewportRectangleOverride() -> MFloatPoint

        Query for a viewport rectangle override.
        """
        ...

class MPxComponentConverter(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def addIntersection(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addIntersection(intersection) -> self

        Maya calls this function for every selection hit on the render item.
        The intersection gives information on the component that was hit.

        * intersection (MIntersection) - The selection intersection.
        """
        ...
    def component(self: Self, *args: Any, **kwargs: Any) -> Any:
        """component() -> MObject

        Once all of the geometry hits have been passed to the converter through calls to addIntersection(), Maya will call this method to retrieve the components corresponding to those hits.

        Returns the component selection.
        """
        ...
    def initialize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """initialize(renderItem) -> self

        Maya calls this function to allow the converter to initialize itself for the selection on the given render item.

        * renderItem (MRenderItem) - The render item.
        """
        ...
    def selectionMask(self: Self, *args: Any, **kwargs: Any) -> Any:
        """selectionMask() -> MSelectionMask

        Maya calls this function to allow the converter to specify the type of components it can handle..

        Returns the selection mask.
        """
        ...

class MPxDrawOverride(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def addUIDrawables(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addUIDrawables(objPath, drawManager, frameContext, data) -> self

        Provides access to the MUIDrawManager, which can be used to queue up operations to draw simple UI shapes like lines, circles, text, etc.

        This method will only be called when hasUIDrawables() is overridden to return True.
        It is called after prepareForDraw() and carries the same restrictions on the sorts of operations it can perform.

        * objPath (MDagPath) - The path to the object being drawn.
        * drawManager (MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry including text.
        * frameContext (MFrameContext) - Frame level context information.
        * data (MUserData) - Data cached by prepareForDraw().
        """
        ...
    def boundingBox(self: Self, *args: Any, **kwargs: Any) -> Any:
        """boundingBox(objPath, cameraPath) -> MBoundingBox

        Called by Maya whenever the bounding box of the drawable object is needed.
        This method should return the object space bounding box for the object to be drawn.

        Note that this method will not be called if the isBounded() method returns a value of False.

        * objPath (MDagPath) - The path to the object being drawn
        * cameraPath (MDagPath) - The path to the camera that is being used to draw

        Returns The object space bounding box of object drawn in the draw callback
        """
        ...
    def disableInternalBoundingBoxDraw(self: Self, *args: Any, **kwargs: Any) -> Any:
        """disableInternalBoundingBoxDraw() -> bool

        Returns True to disable bounding box drawing. The default value is False.

        Indicates whether to disable the automatic drawing of bounding boxes when the display mode has been set to bounding box display.


        Note that bounding box drawing is also disabled if the isBounded() method has been set to False.
        As noted the boundingBox() method is never called under this condition.
        As such with no bounding box information provided it is not possible to automatically draw due to insufficient information provided.
        """
        ...
    def excludedFromPostEffects(self: Self, *args: Any, **kwargs: Any) -> Any:
        """excludedFromPostEffects() -> bool

        Returns False to indicate inclusion in post effects. The default value is true.

        Indicates whether or not the draw code should be called for any additional passes required to perform post effects.


        Note that the appropriate pass identifier and pass semantic can be queried at draw time via the MPassContext data structure.
        Also note that if the pass requires a shader override that it can be obtained from the MDrawContext data structure provided at draw time.
        """
        ...
    def handleTraceMessage(self: Self, *args: Any, **kwargs: Any) -> Any:
        """handleTraceMessage(message) -> self

        When debug tracing is enabled via MPxDrawOverride::traceCallSequence(),
        this method will be called for each trace message.

        The default implementation will print the message
        to stderr.

        * message - A string which will provide feedback on either an
        internal or plug-in call location. To help distinguish which
        draw override a message is associated with, the full path
        name for the DAG object (associated with the draw override) may
        be included as part of the string.
        """
        ...
    def hasUIDrawables(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasUIDrawables() -> bool

        Query whether 'addUIDrawables()' will be called or not.

        In order for any override for the addUIDrawables() method to be called this method must also be overridden to return True.

        This method should not be overridden if addUIDrawables() has not also been overridden as there may be associated wasted overhead.
        """
        ...
    def isBounded(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isBounded(objPath, cameraPath) -> bool

        Returns True if object is bounded.

        Called by Maya to determine if the drawable object is bounded or not. If the object is not bounded then it will never
        be culled by the current camera frustum used for drawing.

        The default implementation will always return True.
        This method can be overridden in derived classes to customize the behaviour.

        Note that if this method returns False then the boundingBox() method will not be called as no bounds are required in this case.

        * objPath (MDagPath) - The path to the object whose transform is needed.
        * cameraPath (MDagPath) - The path to the camera that is being used to draw.
        """
        ...
    def isTransparent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isTransparent() -> bool

        Returns True to indicate inclusion in transparency passes. The default value is false.

        Indicates whether or not the draw method should be called for each transparency pass(front-culling and back-culling).
        """
        ...
    def pointSnappingActive(self: Self, *args: Any, **kwargs: Any) -> Any:
        """pointSnappingActive() -> bool

        This utility function can be called by a draw override to query whether Viewport 2.0 selection has been launched to find points for snapping. If so, in order for the associated DAG object to participate,

        - The MPxSurfaceShape::getComponentSelectionMask() method must be overridden to include MSelectionMask::kSelectPointsForGravity.

        - During the pre-filtering phase, updateSelectionGranularity() must be overridden to set the selection level to MSelectionContext::kComponent.

        - During the hit test phase, wantUserSelection() must be overridden to return true, userSelect() must be overridden to return points for snapping.

        The method returns true if snapping to points is active.
        """
        ...
    def prepareForDraw(self: Self, *args: Any, **kwargs: Any) -> Any:
        """prepareForDraw(objPath, cameraPath, frameContext, oldData) -> MUserData

        Called by Maya each time the object needs to be drawn. Any data needed from the Maya dependency graph must be retrieved and cached in this stage. It is invalid to pull data from the Maya dependency graph in the draw callback method and Maya may become unstable if that is attempted.

        Implementors may allow Maya to handle the data caching by returning a pointer to the data from this method. The pointer must be to a class derived from MUserData. This same pointer will be passed to the draw callback. On subsequent draws, the pointer will also be passed back into this method so that the data may be modified and reused instead of reallocated. If a different pointer is returned Maya will delete the old data. If the cache should not be maintained between draws, set the delete after use flag on the user data. In all cases, the lifetime and ownership of the user data is handled by Maya and the user should not try to delete the data themselves. Data caching occurs per-instance of the associated DAG object. The lifetime of the user data can be longer than the associated node, instance or draw override. Due to internal caching, the user data can be deleted after an arbitrary long time. One should therefore be careful to not access stale objects from the user data destructor. If it is not desirable to allow Maya to handle data caching, simply return NULL in this method and ignore the user data parameter in the draw callback method.

        * objPath (MDagPath) - The path to the object being drawn
        * cameraPath (MDagPath) - The path to the camera that is being used to draw
        * frameContext (MFrameContext) - Frame level context information
        * oldData (MUserData) - Data cached by the previous draw of the instance

        Returns the data to be passed to the draw callback method
        """
        ...
    def refineSelectionPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """refineSelectionPath(selectInfo, hitItem, path, components, objectMask) -> bool

        This method is called during the hit test phase of the viewport 2.0 selection and is used to override the selected path, the selected components or simply reject the selection.
        Should return True if the selection candidate is acceptable.

        One can decide to change the selected path (ie: select the bottom-most transform instead of the proposed path).
        One can decide to remove or add component to the proposed selected list.
        One can decide to change the selection mask of the object (ie: override the selection mask returned by a component converter).
        One can decide that the proposed selection (path or component) is not acceptable and discard it (ie: return False).

        The default implementation makes no changes to 'path', 'components' or 'objectMask' and returns True (i.e. the selection is accepted).

        * selectInfo (MSelectionInfo) - The selection info
        * hitItem (MRenderItem) - The render item hit
        * path [IN/OUT] (MDagPath) - The selected path
        * components [IN/OUT] (MObject) - The selected components
        * objectMask [IN/OUT] (MSelectionMask) - The object selection mask
        """
        ...
    def supportedDrawAPIs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """supportedDrawAPIs() -> DrawAPI

        Returns the draw API supported by this override.
        """
        ...
    def traceCallSequence(self: Self, *args: Any, **kwargs: Any) -> Any:
        """traceCallSequence() -> bool

        This method allows a way for a plug-in to examine
        the basic call sequence for a draw override.

        The default implementation returns false meaning no
        tracing will occur.
        """
        ...
    def transform(self: Self, *args: Any, **kwargs: Any) -> Any:
        """transform(objPath, cameraPath) -> MMatrix

        Returns The world space transformation matrix.

        Called by Maya whenever the world space transform is needed for the object to be drawn by the draw callback.
        The default implementation simply returns the transformation defined by the parent transform nodes in Maya.
        Override to get custom behaviour.

        * objPath (MDagPath) - The path to the object whose transform is needed.
        * cameraPath (MDagPath) - The path to the camera that is being used to draw.
        """
        ...
    def updateSelectionGranularity(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateSelectionGranularity(path, selectionContext) -> self

        This is method is called during the pre-filtering phase of the viewport 2.0 selection and is used to setup the selection context of the given DAG object.

        This is useful to specify the selection level, which defines what can be selected on the object :
          MSelectionContext.kNone        Nothing can be selected
          MSelectionContext.kObject      Object can be selected as a whole
          MSelectionContext.kComponent   Parts of the object - such as vertex, edge or face - are selectable
        This is used to discard objects that are not selectable given the current selection mode (see MGlobal.selectionMode()).

        The default implementation leaves the selection level set at its default value, which is kObject.

         path (MDagPath) - The path to the instance to update the selection context for
         selectionContext [OUT] (MSelectionContext) - The selection context
        """
        ...
    def userSelect(self: Self, *args: Any, **kwargs: Any) -> Any:
        """userSelect(selectInfo, drawContext, objPath, data, selectionList, worldSpaceHitPts) -> bool

        This method is called during the hit test phase of Viewport 2.0 selection if wantUserSelection() returns true, in order to override the default hit test implementation for the associated DAG object. 

        The selection info encapsulates the selection states such as the selection region. The draw context along with the user data cached by prepareForDraw() provides information the same as that being passed to the draw callback, thus makes it possible for a draw override to match its custom hit test with its custom drawing (a.k.a. WYSIWYG selection). 

        If the object is hit, the implementation should add the DAG path and if appropriate its component to selectionList. It is the responsibility of the implementation to add world-space coordinate of the intersection between the selected item and selection ray to worldSpaceHitPts. 

        A custom hit test implementation can choose GPU-based approaches such as OpenGL selection mode, occlusion query etc., or CPU-based approaches which perform hit test for custom geometries. Note that a custom hit test implementation is an object-level override, thus the default hit test implementation can still work for other objects in the scene. 

        After a scene traversal in the hit test phase, Maya records a list of selected items and hit points. During the selection interpretation phase, the hit points will be sorted for certain cases such as single selection; only the winning hit point(s) will have the corresponding selected item(s) to call the refineSelectionPath() method for final selection result that is used to adjust the global active selection list. Thus, for these cases, Maya can only guarantee correct behavior if the implementation returns a valid hit point. 

        For cases such as marquee selection over multiple components, where hit points don't matter, instead of creating one component object for each selected component element, the implementation should create one component object for all selected component elements, to avoid any unnecessary performance overhead due to the frequency of calling refineSelectionPath(). 

        For cases such as point snapping, where multiple hit points are required, each hit point should be stored with the same array index as its selected item (typically a vertex component object), in order for Maya to associate each pair of selected item and hit point. 

        This method should return true if at least one object was hit. The default value is false. 

        * selectInfo [IN] (MSelectionInfo) - The selection info
        * context [IN] (MDrawContext) - The draw context
        * objPath [IN] (MDagPath) - The path to the associated DAG object
        * data [IN] (MUserData) - The data cached by prepareForDraw()
        * selectionList [OUT] (MSelectionList) - List of items selected by this method
        * worldSpaceHitPts [OUT] (MPointArray) - List of hit points
        """
        ...
    def wantUserSelection(self: Self, *args: Any, **kwargs: Any) -> Any:
        """wantUserSelection() -> bool

        This method is called during the hit test phase of Viewport 2.0 selection and is used to indicate whether or not the userSelect() method should be called to override the default hit test implementation for the associated DAG object. 

        This method returns false by default. In this case the draw callback method is invoked for the selection pass, with a special shader that encodes each entity with a different plain color, then the draw buffer is scanned and each color found inside the selection region is transformed into hit info that will be used by the later selection interpretation phase, including selected item and world-space hit point. 

        If a custom hit test implementation is required, this method must be overridden to return true in order for userSelect() to be called.
        """
        ...

class MPxGeometryOverride(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def addUIDrawables(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addUIDrawables(path, drawManager, frameContext) -> self

        For each instance of the object, besides the render items updated in updateRenderItems() there is also a render item list for rendering simple UI elements.
        This stage gives the plugin access to MUIDrawManager which aids in drawing simple geometry like line, circle, rectangle, text, etc.

        Overriding this methods is not always necessary, but if you want to override it, please also override 'hasUIDrawables()' to make it return True or the overridden method will not be called.

        If you are not going to override this function, please don't make 'hasUIDrawables()' return True or there may be some wasted performance overhead.

        Implementation of this method here is empty.

        * path (MDagPath) - The path to the instance to update auxiliary items for.
        * drawManager (MUIDrawManager) - The draw manager used to draw simple geometry.
        * frameContext (MFrameContext) - Frame level context information.
        """
        ...
    def cleanUp(self: Self, *args: Any, **kwargs: Any) -> Any:
        """cleanUp() -> self

        Called after all other stages are completed. Clean up any cached data stored from the updateDG() phase.
        """
        ...
    def configCache(self: Self, *args: Any, **kwargs: Any) -> Any:
        """configCache(evalNode, schema) -> None

        Defines the node's behavior when participating in Cached Playback.

        This method will be called at EM partitioning time, after rules evaluation.

        * evalNode (MEvaluationNode)  - This node's evaluation node, contains animated plug information
        * schema (MCacheSchema)       - Specification about what attributes to cache
        """
        ...
    def getFrameContext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFrameContext() -> MFrameContext

        Return a frame context. The context is not available if called before setup or after cleanup.
        The context should never be deleted by the plug-in as it is owned by the geometry override.
        """
        ...
    def handleTraceMessage(self: Self, *args: Any, **kwargs: Any) -> Any:
        """handleTraceMessage(message) -> self

        When debug tracing is enabled via MPxGeometryOverride::traceCallSequence(),
        this method will be called for each trace message.

        The default implementation will print the message
        to stderr.

        * message - A string which will provide feedback on either an
        internal or plug-in call location. To help distinguish which
        geometry override a message is associated with, the full path
        name for the DAG object (associated with the geometry override) may
        be included as part of the string.
        """
        ...
    def hasUIDrawables(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasUIDrawables() -> bool

        Query whether 'addUIDrawables()' will be called or not.

        In order for any override for the addUIDrawables() method to be called this method must also be overridden to return True.

        This method should not be overridden if addUIDrawables() has not also been overridden as there may be associated wasted overhead.
        """
        ...
    def isIndexingDirty(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isIndexingDirty(item) -> bool

        Returns True if the index buffer needs to be updated.

        This method is called for each render item on the assocated DAG object whenever the object changes. This method is passed a render item. This method should return True if the indexing for the render item has changed since the last frame. Note that returning False from isIndexingDirty may NOT prevent populate geometry from requiring that an index buffer is updated.

        * item (MRenderItem) - The render item in question.
        """
        ...
    def isStreamDirty(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isStreamDirty(desc) -> bool

        Returns True if the vertex buffer needs to be updated.

        This method is called for each geometry stream on the assocated DAG object whenever the object changes. This method is passed a vertex buffer descriptor representing one stream on the object to be updated. This method should return True if it is safe to reuse the existing buffer rather than filling a new buffer with data. Note that returning False from isStreamDirty may NOT prevent populateGeometry from requiring that a stream be updated.

        * desc (MVertexBufferDescriptor) - The description of the vertex buffer.
        """
        ...
    def pointSnappingActive(self: Self, *args: Any, **kwargs: Any) -> Any:
        """pointSnappingActive() -> bool

        Returns True if selection has been launched to find snap points.
        To participate, you need to have at least one render item with point geometry
        and MSelectionMask.kSelectPointsForGravity set in MRenderItem.selectableMask().
        - The granularity must be set to MSelectionContext.kComponent in updateSelectionGranularity()
        - A component converter is not necessary in this scenario.
        - refineSelectionPath() will not be called. All points present in the render item will be
        considered suitable locations for snapping.
        """
        ...
    def populateGeometry(self: Self, *args: Any, **kwargs: Any) -> Any:
        """populateGeometry(requirements, renderItems, data) -> self

        Implementations of this method should create and populate vertex and index buffers on the MGeometry instance 'data' in order to fulfill all of the geometry requirements defined by the 'requirements' parameter. Failure to do so will result in the object either drawing incorrectly or not drawing at all. See the documentation of MGeometryRequirements and MGeometry for more details on the usage of these classes. The geometry requirements will ask for index buffers on demand. Implementations can force the geometry requirements to update index buffers by calling MRenderer.setGeometryDrawDirty() with topologyChanged setting to True.

        * requirements (MGeometryRequirements) - The requirements that need to be satisfied.
        * renderItems (MRenderItemList) - The list of render items that need to be updated.
        * data [OUT] (MGeometry) - The container for the geometry data
        """
        ...
    def refineSelectionPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """refineSelectionPath(selectInfo, hitItem, path, components, objectMask) -> bool

        This method is called during the hit test phase of the viewport 2.0 selection and is used to override the selected path, the selected components or simply reject the selection.
        Should return True if the selection candidate is acceptable.

        One can decide to change the selected path (ie: select the bottom-most transform instead of the proposed path).
        One can decide to remove or add component to the proposed selected list.
        One can decide to change the selection mask of the object (ie: override the selection mask returned by a component converter).
        One can decide that the proposed selection (path or component) is not acceptable and discard it (ie: return False).

        The default implementation makes no changes to 'path', 'components' or 'objectMask' and returns True (i.e. the selection is accepted).

        * selectInfo (MSelectionInfo) - The selection info
        * hitItem (MRenderItem) - The render item hit
        * path [IN/OUT] (MDagPath) - The selected path
        * components [IN/OUT] (MObject) - The selected components
        * objectMask [IN/OUT] (MSelectionMask) - The object selection mask
        """
        ...
    def requiresGeometryUpdate(self: Self, *args: Any, **kwargs: Any) -> Any:
        """requiresGeometryUpdate() -> bool

        This method is called one during each draw - preparation phase. If this method returns true then all of the other MPxGeometryOverride methods will be called for the associated DAG object this draw preparation phase.If this method returns false then all of the other MPxGeometryOverride methods may be called.This code has to be thread safe, non - blocking and work only on data owned by the associated DAG object.
        """
        ...
    def requiresUpdateRenderItems(self: Self, *args: Any, **kwargs: Any) -> Any:
        """requiresUpdateRenderItems(path) -> bool

        This method is called for each instance of the associated DAG object whenever the object changes.If, during a single draw - preparation phase this method returns false for all DAG instances of this MPxGeometryOverride then updateRenderItems() will not be called for the draw - preparation phase.

        * path (MDagPath) - The path to the instance to update render items for
        """
        ...
    def supportedDrawAPIs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """supportedDrawAPIs() -> DrawAPI

        Returns the draw API supported by this override.
        """
        ...
    def supportsEvaluationManagerParallelUpdate(self: Self, *args: Any, **kwargs: Any) -> Any:
        """supportsEvaluationManagerParallelUpdate() -> bool

        This method is called for each MPxGeometryOverride in the scene to determine if the MPxGeometryOverride is eligible for Evaluation Manager Parallel Update.
        """
        ...
    def supportsVP2CustomCaching(self: Self, *args: Any, **kwargs: Any) -> Any:
        """supportsVP2CustomCaching() -> bool

        This method is called for each MPxGeometryOverride in the scene to determine if the MPxGeometryOverride is eligible for VP2 Evaluation Caching.
        """
        ...
    def traceCallSequence(self: Self, *args: Any, **kwargs: Any) -> Any:
        """traceCallSequence() -> bool

        This method allows a way for a plug-in to examine
        the basic call sequence for a geometry override.

        The default implementation returns false meaning no
        tracing will occur.
        """
        ...
    def updateDG(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateDG() -> self

        Perform any work required to translate the geometry data that needs to get information from the dependency graph.  This should be the only place that dependency graph evaluation occurs. Any data retrieved should be cached for later stages.
        """
        ...
    def updateRenderItems(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateRenderItems(path, list) -> self

        This method is called for each instance of the associated DAG object whenever the object changes. The method is passed the path to the instance and the current list of render items associated with that instance. By default the list will contain one render item for each shader assigned to the instance. Implementations of this method method may add, remove or modify items in the list. Note that removal of items created by Maya for assigned shaders is not allowed and will fail. As an alternative this method can disable those items so that they do not draw.

        * path (MDagPath) - The path to the instance to update render items for
        * list [IN/OUT] (MRenderItemList) - The current render item list, items may be modified, added or removed.
        """
        ...
    def updateSelectionGranularity(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateSelectionGranularity(path, selectionContext) -> self

        This is method is called during the pre-filtering phase of the viewport 2.0 selection and is used to setup the selection context of the given DAG object.

        This is useful to specify the selection level, which defines what can be selected on the object :
          MSelectionContext.kNone        Nothing can be selected
          MSelectionContext.kObject      Object can be selected as a whole
          MSelectionContext.kComponent   Parts of the object - such as vertex, edge or face - are selectable
        This is used to discard objects that are not selectable given the current selection mode (see MGlobal.selectionMode()).

        The default implementation leaves the selection level set at its default value, which is kObject.

         path (MDagPath) - The path to the instance to update the selection context for
         selectionContext [OUT] (MSelectionContext) - The selection context
        """
        ...

class MPxImagePlaneOverride(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def supportedDrawAPIs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """supportedDrawAPIs() -> DrawAPI

        Returns the draw API supported by this override.
        """
        ...

class MPxIndexBufferMutator(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def mutateIndexing(self: Self, *args: Any, **kwargs: Any) -> Any:
        """mutateIndexing(sourceIndexBuffers, vertexBuffers, indexBuffer) -> (int, int)

        This method gets called to allow the generator to mutate the data for a custom index stream using information stored in the vertex buffers.

        * sourceIndexBuffers (MComponentDataIndexingList) - Current values for the index buffers.
        * vertexBuffers (MVertexBufferArray) - All vertex buffers generated for this primitive.
        * indexBuffer [OUT] (MIndexBuffer) - The index buffer to fill.

        Returns the type of primitive of the generated indexing and the stride of the generated indexing, only valid when the returned primitive type is kPatch
        See MGeometry.primitiveString() description for a list of valid primitive types.
        """
        ...

class MPxPrimitiveGenerator(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def computeIndexCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """computeIndexCount(object, component) -> int

        This function is called to allow the primitive generator to provide the number of vertices it will use.

        * object (MObject) - The object being evaluated.
        * component (MObject) - The components to use.
        """
        ...
    def generateIndexing(self: Self, *args: Any, **kwargs: Any) -> Any:
        """generateIndexing(object, component, sourceIndexing, targetIndexing, indexBuffer) -> (int, int)

        This method gets called to allow the generator to fill in the data for a custom index stream.

        * object (MObject) - The object being evaluated.
        * component (MObject) - The components to use when building the index buffer. 
        * sourceIndexing (MComponentDataIndexingList) - Vertex index mapping in the declared MComponentDataIndexing::MComponentType space.
        * targetIndexing (MComponentDataIndexingList) - Vertex index mapping from targetIndexing.getComponentType() space to vertex buffer space.
        * indexBuffer [OUT] (MIndexBuffer) - The index buffer to fill.

        Returns the type of primitive of the generated indexing and the stride of the generated indexing, only valid when the returned primitive type is kPatch
        See MGeometry.primitiveString() description for a list of valid primitive types.
        """
        ...

class MPxShaderOverride(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def activateKey(self: Self, *args: Any, **kwargs: Any) -> Any:
        """activateKey(context, key) -> self

        This is the activateKey callback.

        This method is called during the draw phase before invoking any draw() callback that are sharing a common shader key.

        The default implementation is empty.
        """
        ...
    def addGeometryRequirement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addGeometryRequirement(MVertexBufferDescriptor) -> self

        During the initialization phase the geometry requirements for the shading effect can be updated. The update is
        accomplished by calling this method once for each new data stream that needs to be added to the list of requirements.

        If the geometry has multiple fields of the same type associated with it (e.g. multiple UV sets) the 'name' attribute
        of the vertex descriptor can be used to select the desired one. If that member is empty or does not match any of the
        fields then the default field of that type will be used.
        """
        ...
    def addGeometryRequirements(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addGeometryRequirements(MVertexBufferDescriptorList) -> self


        During the initialization phase the geometry requirements for the shading effect can be updated. The update is
        accomplished by calling this method with a list containing descriptions of all data streams that are required by the shader.

        If the geometry has multiple fields of the same type associated with it (e.g. multiple UV sets) the 'name' attribute
        of the vertex descriptor can be used to select the desired one. If that member is empty or does not match any of the
        fields then the default field of that type will be used.

        This method will attempt to add as many requirements as possible from the list, skipping invalid ones.
        If kInvalidParameter is returned it means at least one requirement failed to be added.
        """
        ...
    def addIndexingRequirement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addIndexingRequirement(MIndexBufferDescriptor) -> self

        During the initialization phase the indexing requirements for the shading effect can be updated. The update is accomplished by
        calling this method once for each new index stream required by the shader.

        A shader override can specify the type of primitive it supports.  If the shader relies on a special primitive type like kPatch
        it should use this method to indicate that requirement to the system.  Not all fields on the MIndexBufferDescriptor need to be
        filled in when using this method.  Only the name(), primitive(), and primitiveStride() values are important for a shader to report
        as requirements.

        The primitive type must be specified if the shader requires a primitive type different then a standard point, line, or triangle list
        or strip. The primitiveStride must be specified if using the kPatch primitive type. Valid values range from 1 - 32.
        The name can be specified to trigger a custom MPxPrimitiveGenerator plugin to be used to produce the desired primitive tessellation.
        When requesting custom primitives you should register an MPxPrimitiveGenerator that knows how to produce the custom primitive needed
        by the shader.
        """
        ...
    def addShaderSignature(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addShaderSignature(signature, signatureSize) -> selfaddShaderSignature(MShaderInstance) -> self

        During the initialization phase, the "signature" for the shader may be set. Certain Draw APIs (like DirectX 11) require a
        signature to allow a shading effect to be properly activated. The signature will be used if the override uses
        MPxShaderOverride.drawGeometry() in the draw phase in order to perform drawing. If drawing is done manually, adding a shader
        signature is not necessary.
        """
        ...
    def boundingBoxExtraScale(self: Self, *args: Any, **kwargs: Any) -> Any:
        """boundingBoxExtraScale() -> float

        Returns the Extra scale factor.

        Override this method to supply an extra scale factor to be applied to the object space bounding box of any objects
        which use the shader associated with this override. This is to allow the shader to indicate that the bounding box should
        be bigger than just the base geometry; normally due to shading effects like displacement. Note that the value returned
        here will only be used to put a lower bound on the extra scale applied to the bounding box. It may be made larger due to
        the demands of other shaders associated with the object.

        This method will be called any time a change occurs which may affect the bounding box of associated objects. It is acceptable
        to access the Maya dependency graph within calls to this method as it will never be called during draw.

        The default implementation returns the unit scale factor (1.0).
        """
        ...
    def draw(self: Self, *args: Any, **kwargs: Any) -> Any:
        """draw(context, renderItemList) -> bool

        This is the draw callback, the method is called during the draw phase.

        The expected implementation of this method is to do shader setup and then call drawGeometry() to allow Maya to handle the actual geometry drawing. It is however possible to do all shader setup and geometry draw here directly by accessing the hardware resource handles for geometry and index buffers through the geometry associated with each render item in the render item list.

        No dependency graph evaluation should occur during this phase. If data from Maya is needed here it must be cached on this object (or elsewhere) during the update phase.

        This method should return True on successful draw. If False is returned, Maya will attempt to draw using the default internal draw mechanism.

        Information about the current GPU state may be accessed through the MDrawContext object passed to this method. The MRenderItemList object contains one render item for each object that is meant to be drawn by this method.

        * context [IN/OUT] (MDrawContext) - The current draw context
        * renderItemList (MRenderItemList) - The list of renderable items to draw

        Returns True if draw was successful, False otherwise.
        """
        ...
    def drawGeometry(self: Self, *args: Any, **kwargs: Any) -> Any:
        """drawGeometry(MDrawContext) -> self

        This method may be called from draw() and will cause Maya to immediately draw the current geometry using the current state of the draw API.
        """
        ...
    def endUpdate(self: Self, *args: Any, **kwargs: Any) -> Any:
        """endUpdate() -> self

        This is the final part of the update phase.

        This method is called by Maya to allow the plugin to clean up any data or state from the previous update stages.
        No dependency graph evaluation, nor graphics device access should be performed during this phase.
        """
        ...
    def handlesConsolidatedGeometry(self: Self, *args: Any, **kwargs: Any) -> Any:
        """handlesConsolidatedGeometry() -> bool

        Returns True if the shader instance should disable the consolidation
        for the geometry it is applied to.

        Override this method if the shader instance should disable the consolidation
        for the geometry it is applied to.This is to prevent inconsistency between consolidated and non-consolidated geometry,
        particularly useful for shading effects that compute displacement based on
        the World position.

        The default implementation returns true indicating that the shader instance
        should not be disable the consolidation of the geometry.
        """
        ...
    def handlesDraw(self: Self, *args: Any, **kwargs: Any) -> Any:
        """handlesDraw(context) -> bool

        Returns True if shader handles drawing.

        This method indicates whether the shader will handle the drawing based on the context passed in.

        The default implementation will check the pass context. If the pass semantic is specified to be a color pass
        and the pass has no shader override (MPassContext.hasShaderOverride() returns False) then this method will return True.
        """
        ...
    def initialize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """initialize(shader) -> string
        initialize(initContext, initFeedback) -> string

        Initialization occurs when Maya determines that the hardware shader needs to be rebuilt. Any initialization
        work may be performed here. Also, this is the only time that calls to addGeometryRequirement() may occur.

        Note: There are two versions of the initialize method. Derived classes should override exactly one of them.

        The default implementation returns a constant string.
        """
        ...
    def initialize2(self: Self, *args: Any, **kwargs: Any) -> Any:
        """initialize2(initContext) -> string, userData

        Initialization occurs when Maya determines that the hardware shader needs to be rebuilt. Any initialization
        work may be performed here. Also, this is the only time that calls to addGeometryRequirement() may occur.

        The default implementation returns a string and None MUserData
        """
        ...
    def isTransparent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isTransparent() -> bool

        Returns True if semi-transparent drawing should occur.

        During the update phase the override will be called to return whether it will be drawing with semi-transparency.

        This call occurs after updateDevice() which allows for any device evaluation to occur to determine the transparency state.

        The default return value is False.
        """
        ...
    def nonTexturedShaderInstance(self: Self, *args: Any, **kwargs: Any) -> Any:
        """nonTexturedShaderInstance() -> MShaderInstancenonTexturedShaderInstance() -> (MShaderInstance, bool)

        Returns an override shader instance to be used when drawing in non-textured
        mode. If None is returned an internally defined non-modifiable shader
        instance is used.

        A second optional boolean value 'monitorNode' can be returned as well which will indicate
        that the associated shader node requires monitoring to call back to the override
        during the update phase.

        Note that if transparency is required at initialization time then
        the method setIsTransparent() should be called
        within this method.

        The default implementation returns None indicating that no shader instance will be used.
        """
        ...
    def overridesDrawState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """overridesDrawState() -> bool

        Returns True if the override overrides the draw state.

        During the draw phase this method will be called to determine whether the override will override the draw state when drawing.

        This call occurs after updateDevice() which allows for any device evaluation to occur to determine if the override will
        override the draw state.

        The Viewport 2.0 renderer will skip setting the draw state for plugins that will override the draw state when drawing.
        Note that the MPxShaderOverride.terminateKey() should still return the draw state to the value it had when activateKey was called.

        The default return value is False.
        """
        ...
    def overridesNonMaterialItems(self: Self, *args: Any, **kwargs: Any) -> Any:
        """overridesNonMaterialItems() -> bool

        Returns True if the shader instance should also be used to render non material items.

        Override this method if the shader instance should also be used to render
        non material items such as the wireframe and the selected edges/vertices components.
        This is particularly useful for shading effects that compute displacement for
        which the object geometry will not match the rendered material, making selection
        difficult.

        The default implementation returns False indicating that the shader instance
        should not be used for non material items.
        """
        ...
    def rebuildAlways(self: Self, *args: Any, **kwargs: Any) -> Any:
        """rebuildAlways() -> bool

        Returns True if the shader and geometry should be rebuilt on every update.

        If this method returns True, it will force shader and geometry data to be rebuilt on any change to the shader.
        This may be necessary for shaders that request specific named data sets like UVs or CPVs.
        Any change to the required data set means that geometry needs to be rebuilt.

        The default return value is False.
        """
        ...
    def setGeometryRequirements(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setGeometryRequirements(MShaderInstance) -> self


        During the initialization phase the geometry requirements for the shading effect can be updated. The update can be
        accomplished by calling this method with a shader instance (MShaderInstance). The geometry requirements are copied
        from the MShaderInstance and used as the current shading effect requirements. If there are any requirements already
        specified for the shading effect, they will be replaced.

        This method should not be used in conjunction with addGeometryRequirement() and addGeometryRequirements() methods.
        The reason is that when rendering the vertex format used must exactly match the one used for the shader instance.
        If any additional requirements are added, the geometry may not draw properly.

        The corresponding addShaderSignature() method, which takes an MShaderInstance as an input argument, should also be
        called during initialization if the utility method drawGeometry() is used by the plug-in.
        """
        ...
    def shaderInstance(self: Self, *args: Any, **kwargs: Any) -> Any:
        """shaderInstance() -> MShaderInstance

        Returns the Shader instance.

        Override this method if a shader instance (MShaderInstance) is to be used for drawing.

        The default implementation returns None indicating that no shader instance will be used.
        """
        ...
    def supportedDrawAPIs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """supportedDrawAPIs() -> DrawAPI

        Returns The draw API supported by this override.

        Returns the draw API supported by this override. The returned value may be formed as the bitwise 'or'
        of render drawAPI elements to indicate that the override supports multiple draw APIs. See MRenderer.drawAPI().
        This method returns 'MRender.kOpenGL' by default.
        """
        ...
    def supportsAdvancedTransparency(self: Self, *args: Any, **kwargs: Any) -> Any:
        """supportsAdvancedTransparency() -> bool

        Returns True if advanced tranparency algorithm is supported.

        During the update phase the override will be called to return whether it supports advanced transparency algorithms
        (such as depth peeling).
        """
        ...
    def terminateKey(self: Self, *args: Any, **kwargs: Any) -> Any:
        """terminateKey(context, key) -> self

        This is the terminateKey callback.

        This method is called during the draw phase after invoking draw() callbacks that are sharing a common shader key.

        The default implementation is empty.
        """
        ...
    def updateDG(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateDG(object) -> self

        This is the first part of the update phase.

        Perform any work required to update the shading effect which is related to evaluating the dependency graph.
        This should be the only place that dependency graph evaluation occurs. Data retrieved from Maya may be cached
        on the override for use in later stages.
        """
        ...
    def updateDevice(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateDevice() -> self

        This is the second part of the update phase.

        Perform any work required to update the shading effect which is related to accessing the underlying graphics
        device. This is the only place that the graphics device may be safely accessed other than at draw time.
        """
        ...

class MPxShadingNodeOverride(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def allowConnections(self: Self, *args: Any, **kwargs: Any) -> Any:
        """allowConnections() -> bool

        Returns True if connections should be allowed to parameters of the fragment that do not have custom mappings that
        specifically prevent connections.

        An override may prevent Maya from connecting fragments to specific parameters of the fragment for this
        override by providing custom attribute parameter mappings. It is also possible to prevent connections to all
        parameters on the fragment by overriding this method to return False.
        In that case, the fragment for this override will become a final fragment, and nothing will be connected to it.
        This is equivalent to creating an attribute parameter mapping for every parameter on the fragment and setting
        the allowConnection flag on each mapping to False.

        This method is called once only, just after creation of the override.
        """
        ...
    def fragmentName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """fragmentName() -> string

        Override this method to return the name of the fragment or fragment graph to use for rendering the shading node associated with this override. This fragment will be automatically connected to the other fragments for the other nodes in the shading network to produce a complete shading effect.

        A fragment with the returned name must already exist in the fragment manager for rendering to succeed. If the fragment does not exist, the associated node will not contribute to shading.

        The parameter values for the fragment will be automatically populated from the attribute values on the node wherever the name and type of a parameter on the fragment match the name and type of an attribute on the node.

        The fragment will only be connected to the other fragments in the graph if the output parameter of the fragment has the same name as the output attribute of the node that is connected to the rest of the shading network. To support multiple output attributes of a node, the fragment should return a "struct" type parameter. The names of the members of the struct should match the names of the output attributes for which support is desired. The fragment must compute all output attributes on every execution.

        Returns the name of the fragment to use
        """
        ...
    def getCustomMappings(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getCustomMappings(mappings) -> self

        Maya will automatically match parameters on the shade fragment specified by this override with attributes on the
        associated Maya node as long as the names and types match. In order to specify custom attribute parameter mappings,
        override this method.

        This method will be called before Maya performs its automatic matching so it can be used to prevent that process by
        defining mappings for parameters that would normally be mapped automatically.
        Such mappings will take precedence over automatic mappings.

        It is an error to provide more than one mapping per fragment parameter.
        Only the first such mapping will be used.

        The same attribute may be used for multiple parameters.

        By default, this method defines no custom mappings.

        * mappings [OUT] (MAttributeParameterMappingList) - An attribute parameter mapping list; fill with any desired custom mappings.
        """
        ...
    def outputForConnection(self: Self, *args: Any, **kwargs: Any) -> Any:
        """outputForConnection(sourcePlug, destinationPlug) -> string

        Returns the name of an output parameter on the fragment for the override.

        When Maya attempts to connect the fragment for this override to the fragment for another node in the shading network,
        it will call this method to get the name of the output on the fragment to use for the connection.
        By default, this will simply return the name of the output attribute on the node for the override that is driving the connection.
        Override this method to specify that a different output of the fragment should be used instead.
        This method may also be overridden to get information about how and where the fragment is being connected.

        If the output of the fragment is of "struct" type, this method should return the name of one of the members of the struct.

        This method is called after getCustomMappings().

        If the name returned does not match the name of any output parameter (or struct member in the case of struct output) on the
        fragment for this override then the fragment will not be connected to the overall shading effect.

        * sourcePlug (MPlug) - The plug on the node for this override which is the source of the connection.
                               By default the name of the attribute for this plug is returned.
        * destinationPlug (MPlug) - The plug on the node which is the destination of the connection.
        """
        ...
    def supportedDrawAPIs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """supportedDrawAPIs() -> DrawAPI

        Returns the draw API supported by this override.
        """
        ...
    def updateDG(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateDG() -> self

        This method is called every time Maya needs to update the parameter values on the final shading effect of which the fragment
        produced by this override is a part. In this method implementations should query and cache any values needed for setting
        parameters on the final shading effect in updateShader().
        """
        ...
    def updateShader(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateShader(shader, mappings) -> self

        This method is called every time Maya needs to update the parameter values on the final shading effect of which the fragment
        produced by this override is a part. Implementations may use the information from the mappings list to set parameter values on
        the shader. The list contains all parameter mappings for the override, both automatic and custom. Although it is possible to set
        the value for any parameter on the shader it is an error to do so for parameters which are not defined by the fragment for this
        override and doing so may result in unpredictable behaviour.

        The default implementation does nothing. Note that values for parameters with valid attribute parameter mappings will be set
        automatically. This method need only be overridden if custom behaviour is required.

        For performance, consider caching the resolved parameter names of parameters needing update the first time this method is called.
        This will avoid searching the mappings list and then retrieving the resolved name from the mapping on each update. Resolved names
        are guaranteed to remain constant until the next time fragmentName() is called. Const pointers to individual mappings may also be
        cached in this way and are valid for the same duration.
        Do not attempt to cache mappings created in the getCustomMappings() method.

        It is an error to attempt to access the Maya dependency graph from within updateShader().
        Any attempt to do so will result in instability. Required data should be retrieved and cached in updateDG().

        * shader (MShaderInstance) - The shader instance.
        * mappings (MAttributeParameterMappingList) - The attribute parameter mappings for this override.
        """
        ...
    def valueChangeRequiresFragmentRebuild(self: Self, *args: Any, **kwargs: Any) -> Any:
        """valueChangeRequiresFragmentRebuild(plug) -> bool

        Returns True if a change in attribute values should cause a rebuild of the complete shading effect.

        This method will be called by Maya when it detects changes in the attribute values of nodes in the shading network.
        If this method returns True, Maya will assume that the change means that a new configuration of the total fragment graph
        is necessary and it will trigger a rebuild of the complete shading effect. This will cause fragmentName() to be invoked
        again at which point a different fragment name could be returned.

        For example, if a texture node has multiple modes, each implemented with a different fragment, then a change to the active
        mode would require the shading effect to be rebuilt in order to switch which fragment is used.

        The plug parameter passed in is Maya's best attempt at informing the implementation of what changed. However due to the
        nature of the change management system a single source plug cannot always be determined in which case the plug may be NULL.

        The default implementation returns False.

        * plug (MPlug) - The plug that changed, may be None.
        """
        ...

class MPxSubSceneOverride(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def addInstanceTransform(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addInstanceTransform(renderItem, transform) -> int

        Returns The instance ID for the new instance. This ID can be used to change the matrix or remove it. A return value of 0 indicates an error (render item does not support instancing or invalid state). 0 is never a valid instance ID.

        Add an additional instance for a render item.  Will convert the MRenderItem to instanced rendering if not already done. The render item should already have it's other properties set (including shader and geometry).  A render item converted to instanced rendering will ignore its typical matrix from setMatrix().

        * renderItem (MRenderItem) - The render item to add a new instance to.
        * transform (MMatrix) - The transformation matrix of the new instance.
        """
        ...
    def addUIDrawables(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addUIDrawables(drawManager, frameContext) -> int

        Provides access to a MUIDrawManager, which can be used to queue upoperations to draw simple UI shapes like lines, circles, text, etc.If you override this method you must also override hasUIDrawables()to return true, otherwise this method will not be called.If you are not going to override this function, please don't make 'hasUIDrawables()' return trueor there may be some wasted performance overhead.By default the drawables will persist until either the DAG object associated with the overrideis destroyed or the override is deregistered.If you don't want them to be redrawn on each refresh,override areUIDrawablesDirty() to return false.That will cause the drawables to be destroyedon next refresh and this method called again to replace them.

        drawManager The UI draw manager, it can be used to draw some simple geometry including text
        frameContext Frame level context information
        """
        ...
    def areUIDrawablesDirty(self: Self, *args: Any, **kwargs: Any) -> Any:
        """areUIDrawablesDirty() -> bool

        Determines whether addUIDrawables() should be called on the next refresh.

        Return	True if addUIDrawables() should be called on the next refresh, false if not.The default is true.

        If you've overridden addUIDrawables() then at the start of each refresh Maya willdestroy the drawables added in the previous refresh and call addUIDrawables() again.If you override this method to return false then Maya will preserve the UI drawablesfrom the previous refresh until either the DAG object associated with the override isdestroyed, or the override is deregistered.
        """
        ...
    def furtherUpdateRequired(self: Self, *args: Any, **kwargs: Any) -> Any:
        """furtherUpdateRequired(frameContext) -> bool

        Returns True if further update is required. The default value return is False.

        This method is called by Maya following update() to allow the override to indicate whether further processing is required.

        If so, then requiresUpdate() and update() will be called again at a later time. In general this will occur when no active processing is occuring (when "idle").

        It is the responsibility of the plug-in to ensure that this method does not continuously request further updates as it may block the execution of other idle time events.

        * frameContext (MFrameContext) - Context information for the current frame.
        """
        ...
    def getInstancedSelectionPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getInstancedSelectionPath(renderItem, intersection, dagPath) -> bool

        Returns True if a dag path was found for the instantiable render item.

        This method is called by Maya following selection to allow specifying the selection path for a single instantiable render item. It is identical to getSelectionPath() but includes MIntersection information to properly distinguish between instances when the viewport is in GPU acceleration mode.

        In GPU acceleration mode, the renderItem will be the one of the master instance and the value of intersection.instanceID() will match the value returned by addInstanceTransform(). In regular non GPU accelerated mode, the renderItem will be the one directly associated with the instance. If intersection.instanceID() is equal to -1, then the geometry was not GPU accelerated.

        * renderItem (MRenderItem) - Render item found inside the selection frustum, or master item in GPU accelerated mode.
        * intersection (MIntersection) - Extra information to help find out how the render item got selected.
        * dagPath [OUT] (MDagPath) - the MDagPath associated with the provided render item.
        """
        ...
    def getSelectionPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getSelectionPath(renderItem, dagPath) -> bool

        Returns True if a dag path was found for the render item.

        This method is called by Maya following selection to allow specifying the selection path for a single render item. It will be called once for each MRenderItem submitted in MPxSubSceneOverride.update() that intersects the selection frustum. If none of the MRenderItem intersects, then this callback will remain silent.

        When selection filtering is active, or in case of single click selection it is possible that the item will not be in the final selection list.

        The default implementation will return the first path to the associated DAG object. Specialization is required to provide support for multiple instances of the DAG object.

        Note: If your SubScene override plugin supports instancing, then you should overload getInstancedSelectionPath() instead to get all the necessary information to be able to return a proper path.

        * renderItem (MRenderItem) - Render item found inside the selection frustum.
        * dagPath [OUT] (MDagPath) - the MDagPath associated with the provided render item.
        """
        ...
    def hasUIDrawables(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasUIDrawables() -> bool

        Return Whether addUIDrawables() will be called or not.

        In order for any override for the addUIDrawables() method to be calledthis method must also be overridden to return true.This method should not be overridden if addUIDrawables() has not alsobeen overridden as there may be associated wasted overhead.
        """
        ...
    def pointSnappingActive(self: Self, *args: Any, **kwargs: Any) -> Any:
        """pointSnappingActive() -> bool

        Returns True if selection has been launched to find snap points.
        To participate, you need to have at least one render item with point geometry
        and MSelectionMask.kSelectPointsForGravity set in MRenderItem.selectableMask().
        - The granularity must be set to MSelectionContext.kComponent in updateSelectionGranularity()
        - A component converter is not necessary in this scenario.
        - getSelectionPath() will not be called. All points present in the render item will be
        considered suitable locations for snapping.
        """
        ...
    def removeAllInstances(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeAllInstances(renderItem) -> self

        Remove all instances for a render item. This render item will remain set up for instancing and will render nothing until new instances are added.

        * renderItem (MRenderItem) - The render item to operate on.
        """
        ...
    def removeExtraInstanceData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeExtraInstanceData(renderItem, parameterName) -> self

        Remove an entire extra instance data stream from the instanced render item.

        * renderItem (MRenderItem) - The render item to operate on.
        * parameterName (string) - The name of the parameter associated with the extra instance data stream.
        """
        ...
    def removeInstance(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeInstance(renderItem, instanceId) -> self

        Remove one instance of a render item.

        * renderItem (MRenderItem) - The render item to operate on.
        * instanceId (int) - The instance ID of the instance to remove. This must be a value returned by addInstanceTransform.
        """
        ...
    def requiresUpdate(self: Self, *args: Any, **kwargs: Any) -> Any:
        """requiresUpdate(container, frameContext) -> bool

        On each frame Maya will give each instantiated MPxSubSceneOverride object a chance to update its set of render items. Before beginning the update process for a specific override, Maya will first call this method to give the override a chance to indicate whether or not an update is necessary. If this method returns False, MPxSubSceneOverride.update() will not be called.

        The set of render items for this override must not be modified in this method.

        * container (MSubSceneContainer) - The container for this override
        * frameContext (MFrameContext) - Context information for the current frame

        Returns True if Maya should trigger the update process for this override
        """
        ...
    def setAllowTransparentInstances(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setAllowTransparentInstances(renderItem, transform) -> int

        Instancing is disabled automatically by default when the shader is transparent.This achieves the best appearance because Maya can sort individual instances.

        In some cases, performance is more important than appearance.e.g.particlesThis method allows to override the default behavior.

        renderItem The render item to operate on.
        allow Whether to allow instancing with transparent shader.
        """
        ...
    def setExtraInstanceData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setExtraInstanceData(renderItem, parameterName, data, instanceId=None) -> self

        Adds an extra stream of instanced data to an instanced render item. Once a render item has been instanced, additional per-instance data may be bound to a parameter on the shader for that item. Supported shader parameter types for instanced data include: float, float2, float3 and float4. Once a stream of instanced data is specified for a shader parameter, the original value of that parameter will be ignored in favor of the per-instance data specified in this method.

        If the render item has not been set up for instancing or if an invalid parameter was specified this method will fail. The size of the data array must be x*numberOfInstances where x is the size of the channel (1-4). If the size is wrong, the method will fail.

        More than one stream of extra instance data may be specified for an instanced render item. The number of streams will be limited by the number of texture co-ordinate channels available from the underlying graphics system (and note that the instanced matrix occupies four streams). If too many streams are used then a red error shader will be displayed instead of the expected shader.

        * renderItem (MRenderItem) - The render item to operate on.
        * parameterName (string) - The name of the parameter on the shader to fill with the instanced data.
        * data (MFloatArray) - The instanced data stream.
        * instanceId (int) - The instance ID of the instance to set the data for.
        """
        ...
    def setGeometryForRenderItem(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setGeometryForRenderItem(renderItem, vertexBuffers, indexBuffer=None, objectBox=None) -> self

        Call this method to provide the geometry for a render item. Although the render item will add a reference to each buffer, ultimate ownership of the geometric data remains with the caller. This method may only be called on render items which have been generated by this override and it may only be called during update(). Buffers may be shared among multiple render items. This method will replace any geometry currently associated with the render item with the newly provided geometry.

        The bounding box parameter to this method is optional. If None, Maya will attempt to calculate the box automatically. Note that this may require a read-back of vertex data from the graphics card which can be a very slow operation. It is better to supply a correct bounding box whenever possible.

        It is the responsibility of the caller to ensure that the buffers provided fulfill the geometry requirements of the shader for the render item. If the requirements are not met, the render item will not draw. If there is no shader assigned to the render item, this method will fail.

        When a geometry is completely defined by its vertex buffers, like when drawing all points in a MGeometry.kPoints render item, it is possible to provide an empty MIndexBuffer or None for the indexBuffer parameter. The geometry will then be drawn using a non-indexed draw call like glDrawArrays() or ID3D11DeviceContext::Draw().

        * renderItem (MRenderItem) - The render item to provide geometry for.
        * vertexBuffers (MVertexBufferArray) - The vertex buffers for the geometry.
        * indexBuffer (MIndexBuffer) - The index buffer for the geometry, may be None.
        * objectBox (MBoundingBox) - Object-space bounding box, may be None.
        """
        ...
    def setInstanceTransformArray(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setInstanceTransformArray(renderItem, matrixArray) -> self

        Sets the entire instance array for a render item.  Will convert the MRenderItem to instanced rendering if not already done.  Any pre-existing instances will be removed. The render item should already have it's other properties set (including shader and geometry). A render item converted to instanced rendering will ignore its typical matrix from setMatrix().
        This function is provided as a simpler alternative to addInstanceTransform() for when the ability to update or remove individual instances is not required. However additional instances may still be added via addInstanceTransform() and those may be individually updated or removed.

        * renderItem (MRenderItem) - The render item to set the instance matrix array for.
        * matrixArray (MMatrixArray) - The transformation matrix array for all the instances.
        """
        ...
    def supportedDrawAPIs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """supportedDrawAPIs() -> DrawAPI

        Returns the draw API supported by this override.
        """
        ...
    def update(self: Self, *args: Any, **kwargs: Any) -> Any:
        """update(container, frameContext) -> self

        This method is called by Maya on each frame as long as the implementation of MPxSubSceneOverride.requiresUpdate() returns True. In this method, the MSubSceneContainer should be populated with the render items that are required to draw the associated DAG object. The render items will remain in the container until they are explicitly removed or the associated object is deleted. Render items in the container may also be modified at this time. 

        All render items in the container upon completion of this method will be processed for drawing. Any such items which pass all filtering tests for the active viewport will draw. At a minimum, render items must be enabled, have a valid shader and valid geometry in order to draw in Viewport 2.0. 

        It is the responsibility of this method	to call MRenderer.setLightsAndShadowsDirty() to trigger recomputation of any shadow maps in the scene (if required). 

        * container (MSubSceneContainer) - The container for this override
        * frameContext (MFrameContext) - Context information for the current frame
        """
        ...
    def updateInstanceTransform(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateInstanceTransform(renderItem, instanceId, transform) -> self

        Update the instance transform matrix for one instance of a render item.

        * renderItem (MRenderItem) - The render item to operate on.
        * instanceId (int) - The instance ID of the instance to update. This must be a value returned by addInstanceTransform.
        * transform (MMatrix) - The new transformation matrix for the instance.
        """
        ...
    def updateSelectionGranularity(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateSelectionGranularity(path, selectionContext) -> self

        This method is called during the pre-filtering phase of the viewport 2.0 selection and is used to allow derived classes to modify the selection context of the given DAG object.

        This is useful to specify the selection level, which defines what can be selected on the object :
          MSelectionContext.kNone        Nothing can be selected
          MSelectionContext.kObject      Object can be selected as a whole
          MSelectionContext.kComponent   Parts of the object - such as vertex, edge or face - are selectable
        This is used to discard objects that are not selectable given the current selection mode (see MGlobal.selectionMode()).

        Implementation of this method here is empty, and default selection level is set to kObject.

         path (MDagPath) - The path to the instance to update the selection context for
         selectionContext [OUT] (MSelectionContext) - The selection context
        """
        ...

class MPxSurfaceShadingNodeOverride(MPxShadingNodeOverride):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def allowConnections(self: Self, *args: Any, **kwargs: Any) -> Any:
        """allowConnections() -> bool

        Returns True if connections should be allowed to parameters of the fragment that do not have custom mappings that
        specifically prevent connections.

        An override may prevent Maya from connecting fragments to specific parameters of the fragment for this
        override by providing custom attribute parameter mappings. It is also possible to prevent connections to all
        parameters on the fragment by overriding this method to return False.
        In that case, the fragment for this override will become a final fragment, and nothing will be connected to it.
        This is equivalent to creating an attribute parameter mapping for every parameter on the fragment and setting
        the allowConnection flag on each mapping to False.

        This method is called once only, just after creation of the override.
        """
        ...
    def bumpAttribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """bumpAttribute() -> string

        Returns the name of the attribute that accepts bump connections from bump nodes.

        This method is called after getCustomMappings() to allow the plugin to provide surface-shader specific information.
        If required, the override may return the name of the attribute on the node that accepts connections from bump nodes for
        doing bump or normal mapping (often this is "normalCamera"). A special mapping will be created linking this attribute
        to the parameter named "Nw" (world space normal) on the fragment. The special mapping will ensure that the extra fragments
        needed for bump mapping are set up correctly. If there is no "Nw" parameter on the fragment the mapping will not be created
        and bump mapping will not work for the associated shader.

        The default implementation returns the empty string (no bump).
        """
        ...
    def fragmentName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """fragmentName() -> string

        Override this method to return the name of the fragment or fragment graph to use for rendering the shading node associated with this override. This fragment will be automatically connected to the other fragments for the other nodes in the shading network to produce a complete shading effect.

        A fragment with the returned name must already exist in the fragment manager for rendering to succeed. If the fragment does not exist, the associated node will not contribute to shading.

        The parameter values for the fragment will be automatically populated from the attribute values on the node wherever the name and type of a parameter on the fragment match the name and type of an attribute on the node.

        The fragment will only be connected to the other fragments in the graph if the output parameter of the fragment has the same name as the output attribute of the node that is connected to the rest of the shading network. To support multiple output attributes of a node, the fragment should return a "struct" type parameter. The names of the members of the struct should match the names of the output attributes for which support is desired. The fragment must compute all output attributes on every execution.

        Returns the name of the fragment to use
        """
        ...
    def getCustomMappings(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getCustomMappings(mappings) -> self

        Maya will automatically match parameters on the shade fragment specified by this override with attributes on the
        associated Maya node as long as the names and types match. In order to specify custom attribute parameter mappings,
        override this method.

        This method will be called before Maya performs its automatic matching so it can be used to prevent that process by
        defining mappings for parameters that would normally be mapped automatically.
        Such mappings will take precedence over automatic mappings.

        It is an error to provide more than one mapping per fragment parameter.
        Only the first such mapping will be used.

        The same attribute may be used for multiple parameters.

        By default, this method defines no custom mappings.

        * mappings [OUT] (MAttributeParameterMappingList) - An attribute parameter mapping list; fill with any desired custom mappings.
        """
        ...
    def outputForConnection(self: Self, *args: Any, **kwargs: Any) -> Any:
        """outputForConnection(sourcePlug, destinationPlug) -> string

        Returns the name of an output parameter on the fragment for the override.

        When Maya attempts to connect the fragment for this override to the fragment for another node in the shading network,
        it will call this method to get the name of the output on the fragment to use for the connection.
        By default, this will simply return the name of the output attribute on the node for the override that is driving the connection.
        Override this method to specify that a different output of the fragment should be used instead.
        This method may also be overridden to get information about how and where the fragment is being connected.

        If the output of the fragment is of "struct" type, this method should return the name of one of the members of the struct.

        This method is called after getCustomMappings().

        If the name returned does not match the name of any output parameter (or struct member in the case of struct output) on the
        fragment for this override then the fragment will not be connected to the overall shading effect.

        * sourcePlug (MPlug) - The plug on the node for this override which is the source of the connection.
                               By default the name of the attribute for this plug is returned.
        * destinationPlug (MPlug) - The plug on the node which is the destination of the connection.
        """
        ...
    def primaryColorParameter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """primaryColorParameter() -> string

        Returns the name of the fragment parameter to use as the primary color.

        This method is called just after getCustomMappings() to allow the plugin to provide extra surface shader-specific
        information. If required, the override may return the name of a 3-float parameter on the fragment that should be marked
        as the primary color. If the viewport is set to hide textures (shaded mode) then the specified parameter will be set
        using the "default color" value from the texture which is connected to the associated attribute on the Maya node.

        The default implementation returns the empty string (no primary color).

        The name must correspond to a parameter on the fragment that is mapped to an attribute on the node either automatically
        or through custom attribute parameter mappings.
        """
        ...
    def supportedDrawAPIs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """supportedDrawAPIs() -> DrawAPI

        Returns the draw API supported by this override.
        """
        ...
    def transparencyParameter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """transparencyParameter() -> string

        Returns the name of the fragment parameter that should drive transparency.

        This method is called just after getCustomMappings() to allow the plugin to provide extra surface shader-specific
        information. If required, the override may return the name of a single float or 3-float parameter on the fragment that
        should be marked as the parameter that drives the transparency of the surface shader. The values of this parameter will
        be watched so that scene objects using this shader will be correctly marked and sorted for transparent drawing.

        The default implementation returns the empty string (no transparency).

        The name must correspond to a parameter on the fragment that is mapped to an attribute on the node either automatically
        or through custom attribute parameter mappings.
        """
        ...
    def updateDG(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateDG() -> self

        This method is called every time Maya needs to update the parameter values on the final shading effect of which the fragment
        produced by this override is a part. In this method implementations should query and cache any values needed for setting
        parameters on the final shading effect in updateShader().
        """
        ...
    def updateShader(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateShader(shader, mappings) -> self

        This method is called every time Maya needs to update the parameter values on the final shading effect of which the fragment
        produced by this override is a part. Implementations may use the information from the mappings list to set parameter values on
        the shader. The list contains all parameter mappings for the override, both automatic and custom. Although it is possible to set
        the value for any parameter on the shader it is an error to do so for parameters which are not defined by the fragment for this
        override and doing so may result in unpredictable behaviour.

        The default implementation does nothing. Note that values for parameters with valid attribute parameter mappings will be set
        automatically. This method need only be overridden if custom behaviour is required.

        For performance, consider caching the resolved parameter names of parameters needing update the first time this method is called.
        This will avoid searching the mappings list and then retrieving the resolved name from the mapping on each update. Resolved names
        are guaranteed to remain constant until the next time fragmentName() is called. Const pointers to individual mappings may also be
        cached in this way and are valid for the same duration.
        Do not attempt to cache mappings created in the getCustomMappings() method.

        It is an error to attempt to access the Maya dependency graph from within updateShader().
        Any attempt to do so will result in instability. Required data should be retrieved and cached in updateDG().

        * shader (MShaderInstance) - The shader instance.
        * mappings (MAttributeParameterMappingList) - The attribute parameter mappings for this override.
        """
        ...
    def valueChangeRequiresFragmentRebuild(self: Self, *args: Any, **kwargs: Any) -> Any:
        """valueChangeRequiresFragmentRebuild(plug) -> bool

        Returns True if a change in attribute values should cause a rebuild of the complete shading effect.

        This method will be called by Maya when it detects changes in the attribute values of nodes in the shading network.
        If this method returns True, Maya will assume that the change means that a new configuration of the total fragment graph
        is necessary and it will trigger a rebuild of the complete shading effect. This will cause fragmentName() to be invoked
        again at which point a different fragment name could be returned.

        For example, if a texture node has multiple modes, each implemented with a different fragment, then a change to the active
        mode would require the shading effect to be rebuilt in order to switch which fragment is used.

        The plug parameter passed in is Maya's best attempt at informing the implementation of what changed. However due to the
        nature of the change management system a single source plug cannot always be determined in which case the plug may be NULL.

        The default implementation returns False.

        * plug (MPlug) - The plug that changed, may be None.
        """
        ...

class MPxVertexBufferGenerator(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def createVertexStream(self: Self, *args: Any, **kwargs: Any) -> Any:
        """createVertexStream(object, vertexBuffer, targetIndexing, sharedIndexing, sourceStreams) -> self

        This method gets called to allow the generator to fill in the data for a custom vertex stream. Use the requirements in the vertexBuffer to get the description of the stream. Use vertexBuffer.acquire() and vertexBuffer.commit() to fill the buffer. 

        * object (MObject) - The dag object being evaluated.
        * vertexBuffer [IN/OUT] (MVertexBuffer) - The vertex buffer to fill.
        * targetIndexing (MComponentDataIndexing) - Vertex index mapping from targetIndexing.getComponentType() space to vertex buffer space.
        * sharedIndexing (MComponentDataIndexing) - Vertex index mapping in the declared MComponentDataIndexing::MComponentType space.
        * sourceStreams (MVertexBufferArray) - Array of Vertex Buffers that can be used to create the new stream.
        """
        ...
    def getSourceIndexing(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getSourceIndexing(object, sourceIndexing) -> self

        This function is called to allow the vertex buffer generator to provide its vertex indexing information as well as the space the vertices are in.  The indexing and the component type are stored in the  sourceIndexing argument.  This indexing information is to allow the system to identify any potential  vertex sharing that is common across all vertex requirements. 

        * object (MObject) - The object being evaluated.
        * sourceIndexing [OUT] (MComponentDataIndexing) - Vertex index mapping in the declared MComponentDataIndexing::MComponentType space.
        """
        ...
    def getSourceStreams(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getSourceStreams(object, sourceStreams) -> self

        This function is called to allow the vertex buffer generator to provide the list of stream names that it requires. The names will be used to fill the array of vertex buffers that will be passed to createVertexStream. 

        * object (MObject) - The dag object being evaluated.
        * sourceStreams [OUT] (list of strings) - Array of strings.
        """
        ...

class MPxVertexBufferMutator(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def modifyVertexStream(self: Self, *args: Any, **kwargs: Any) -> Any:
        """modifyVertexStream(object, vertexBuffer, targetIndexing) -> self

        This method gets called to allow the mutator to alter the data for a custom vertex stream.
        Use the requirements in the vertexBuffer to get the description of the stream.
        Use vertexBuffer.aquire() and vertexBuffer.commit() to fill the buffer.

        * object (MObject) - The object being evaluated.
        * vertexBuffer [IN/OUT] (MVertexBuffer) - The vertex buffer to alter.
        * targetIndexing (MComponentDataIndexing) - Vertex index mapping from targetIndexing.getComponentType() space to vertex buffer space.
        """
        ...

class MQuadRender(MRenderOperation):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def blendStateOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """blendStateOverride() -> MBlendState

        Query if a blend state override is performed by this quad operation.
        """
        ...
    def clearOperation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clearOperation() -> MClearOperation

        Get the scene clear operation.
        """
        ...
    def depthStencilStateOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """depthStencilStateOverride() -> MDepthStencilState

        Query if a depth-stencil state override is performed by this quad operation.
        """
        ...
    def enableSRGBWrite(self: Self, *args: Any, **kwargs: Any) -> Any:
        """enableSRGBWrite() -> bool

        Return whether to enable GPU based gamma correction during pixel writes.
        """
        ...
    kClear: int = ...
    kHUDRender: int = ...
    kPresentTarget: int = ...
    kQuadRender: int = ...
    kSceneRender: int = ...
    kUserDefined: int = ...
    @property
    def mClearOperation(*args: Any, **kwargs: Any) -> Any:
        """Clear operation"""
        ...
    @mClearOperation.setter
    def mClearOperation(*args: Any, **kwargs: Any) -> Any:
        """Clear operation"""
        ...
    def name(self: Self, *args: Any, **kwargs: Any) -> Any:
        """name() -> string

        Returns the name of the render operator.
        """
        ...
    def operationType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """operationType() -> int

        Returns the type of a render operator.
        """
        ...
    def rasterizerStateOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """rasterizerStateOverride() -> MRasterizerState

        Query if a rasterizer state override is performed by this quad operation.
        """
        ...
    def shader(self: Self, *args: Any, **kwargs: Any) -> Any:
        """shader() -> MShaderInstance

        Get the shader to use when rendering a quad.
        """
        ...
    def targetOverrideList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """targetOverrideList() -> list of MRenderTarget

        Return a list of render target which will be used as the target overrides for the operation.
        """
        ...
    def viewportRectangleOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """viewportRectangleOverride() -> MFloatPoint

        Query for a viewport rectangle override.
        """
        ...

class MRasterizerState(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def desc(self: Self, *args: Any, **kwargs: Any) -> Any:
        """desc() -> MRasterizerStateDesc

        Get the rasterizer state descriptor that was used to create the state object.
        """
        ...
    kCullBack: int = ...
    kCullFront: int = ...
    kCullNone: int = ...
    kFillSolid: int = ...
    kFillWireFrame: int = ...
    def resourceHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """resourceHandle() -> long

        Returns a long containing a C++ 'void' pointer which points to the draw API dependent handle for a rasterizer state.
        For OpenGL, such a handle does not exist and a NULL pointer will be returned.
        For DirectX, a pointer to a Direct3D state will be returned.
        """
        ...

class MRasterizerStateDesc(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    @property
    def antialiasedLineEnable(*args: Any, **kwargs: Any) -> Any:
        """Enables HW anti-aliased lines, auto disabled by multi-sample AA, default false"""
        ...
    @antialiasedLineEnable.setter
    def antialiasedLineEnable(*args: Any, **kwargs: Any) -> Any:
        """Enables HW anti-aliased lines, auto disabled by multi-sample AA, default false"""
        ...
    @property
    def cullMode(*args: Any, **kwargs: Any) -> Any:
        """Select the face culling mode, default kCullNone"""
        ...
    @cullMode.setter
    def cullMode(*args: Any, **kwargs: Any) -> Any:
        """Select the face culling mode, default kCullNone"""
        ...
    @property
    def depthBias(*args: Any, **kwargs: Any) -> Any:
        """DepthBias adds the given bias value to the rasterizer z value prior to depth testing"""
        ...
    @depthBias.setter
    def depthBias(*args: Any, **kwargs: Any) -> Any:
        """DepthBias adds the given bias value to the rasterizer z value prior to depth testing"""
        ...
    @property
    def depthBiasClamp(*args: Any, **kwargs: Any) -> Any:
        """Maximum value scaled depth bias can attain, default 0"""
        ...
    @depthBiasClamp.setter
    def depthBiasClamp(*args: Any, **kwargs: Any) -> Any:
        """Maximum value scaled depth bias can attain, default 0"""
        ...
    @property
    def depthBiasIsFloat(*args: Any, **kwargs: Any) -> Any:
        """Indicates that DepthBias is a float value, default false"""
        ...
    @depthBiasIsFloat.setter
    def depthBiasIsFloat(*args: Any, **kwargs: Any) -> Any:
        """Indicates that DepthBias is a float value, default false"""
        ...
    @property
    def depthClipEnable(*args: Any, **kwargs: Any) -> Any:
        """Enables HW automatic depth clipping, default true"""
        ...
    @depthClipEnable.setter
    def depthClipEnable(*args: Any, **kwargs: Any) -> Any:
        """Enables HW automatic depth clipping, default true"""
        ...
    @property
    def fillMode(*args: Any, **kwargs: Any) -> Any:
        """Select the primitive fill mode, default kFillSolid"""
        ...
    @fillMode.setter
    def fillMode(*args: Any, **kwargs: Any) -> Any:
        """Select the primitive fill mode, default kFillSolid"""
        ...
    @property
    def frontCounterClockwise(*args: Any, **kwargs: Any) -> Any:
        """Select whether CW or CCW winding is used for "_CSTRfront" face, default false"""
        ...
    @frontCounterClockwise.setter
    def frontCounterClockwise(*args: Any, **kwargs: Any) -> Any:
        """Select whether CW or CCW winding is used for "_CSTRfront" face, default false"""
        ...
    @property
    def multiSampleEnable(*args: Any, **kwargs: Any) -> Any:
        """Enables HW full screen multi-sample anti-aliasing, default false"""
        ...
    @multiSampleEnable.setter
    def multiSampleEnable(*args: Any, **kwargs: Any) -> Any:
        """Enables HW full screen multi-sample anti-aliasing, default false"""
        ...
    @property
    def scissorEnable(*args: Any, **kwargs: Any) -> Any:
        """Enables HW scissor clip rectangle, default false"""
        ...
    @scissorEnable.setter
    def scissorEnable(*args: Any, **kwargs: Any) -> Any:
        """Enables HW scissor clip rectangle, default false"""
        ...
    def setDefaults(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDefaults() -> self

        Set all values for the rasterizer state to their default values.
        """
        ...
    @property
    def slopeScaledDepthBias(*args: Any, **kwargs: Any) -> Any:
        """Slope scaled depth bias value, default 0"""
        ...
    @slopeScaledDepthBias.setter
    def slopeScaledDepthBias(*args: Any, **kwargs: Any) -> Any:
        """Slope scaled depth bias value, default 0"""
        ...

class MRenderItem(object):
    DecorationItem: int = ...
    DrawOnlyWhenDefaultMaterialActive: int = ...
    IgnoreDefaultMaterialMode: int = ...
    InternalItem: int = ...
    InternalMaterialItem: int = ...
    InternalTexturedMaterialItem: int = ...
    InternalUnsupportedMaterialItem: int = ...
    MaterialSceneItem: int = ...
    NonMaterialSceneItem: int = ...
    OverrideNonMaterialItem: int = ...
    SkipWhenDefaultMaterialActive: int = ...
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def allowIsolateSelectCopy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """allowIsolateSelectCopy() -> bool

        Returns whether or not the render item allows its copies to be created forthe drawing of isolate selected components.

        See setAllowIsolateSelectCopy() for more information.
        """
        ...
    def associateWithIndexBuffer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """associateWithIndexBuffer(MIndexBuffer) -> bool

        Use to indicate that a particular index buffer should be used with this render item.
        This method must be called from MPxGeometryOverride in order to link index buffers generated in
        the MGeometry class with specific render items.
        Without an index buffer, a render item cannot draw.
        """
        ...
    def availableShaderParameters(self: Self, *args: Any, **kwargs: Any) -> Any:
        """availableShaderParameters() -> list of string

        Returns the list of available shader parameters.
        This is useful for OverrideNonMaterialItem to retrieve default parameters.
        """
        ...
    def boundingBox(self: Self, *args: Any, **kwargs: Any) -> Any:
        """boundingBox(space=kObject) -> MBoundingBox

        Returns the bounding box for the geometry data of the render item.
        Returns None if the render item is unbounded or does not have a valid associated geometry.

        * space (Space) - The requested space of the bounding box.
        """
        ...
    def castsShadows(self: Self, *args: Any, **kwargs: Any) -> Any:
        """castsShadows() -> bool

        Get the castsShadows state of the render item.
        """
        ...
    def component(self: Self, *args: Any, **kwargs: Any) -> Any:
        """component() -> MObject

        Get the optional component for the render item if the render item representsthe drawing of a component as a result of per - face shader assignment, componentselection highlighting etc.

        If the render item doesn't represent the drawing of a component, then a nullMObject will be returned. Use the isNull() method of the MObject to check.
        """
        ...
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """create(name, type, primitive) -> MRenderItem
        create(item) -> MRenderItem

        Static MRenderItem creation utility.

        Create new render item:
        * name (string) - The name of the render item (should be non-empty).
        * type (int) - The type of the render item.
        * primitive (int) - The primitive type of the render item.

        See MRenderItem.type() for a list of valid render item types.
        Internal types are not allowed and will result no item being created.
        See MGeometry.primitiveString() for a list of valid primitive types.

        Create new render item and copy all parameters from the incoming MRenderItem:
        * item (MRenderItem) - The item to copy.
        """
        ...
    def customData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """customData() -> MUserData

        Retrieve custom data from the render item, returns None if no such data has ever been set on the render item.

            DEPRECATED in 2022, use getCustomData instead.
        """
        ...
    def depthPriority(self: Self, *args: Any, **kwargs: Any) -> Any:
        """depthPriority() -> int

        Get the depth priority of the render item.
        The higher the depth priority the closer it will be drawn to the camera.
        """
        ...
    def destroy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """destroy(item) -> None

        Static MRenderItem destruction utility.
        Destroys the internal data structures associated with this MRenderItem.
        Any attempt to use the MRenderItem after this will result in an exception.
        """
        ...
    def drawMode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """drawMode() -> int

        Get the draw mode for the render item.
        See MGeometry.drawModeString() for a list of valid draw modes.
        """
        ...
    def enable(self: Self, *args: Any, **kwargs: Any) -> Any:
        """enable(bool) -> self

        Enable or disable the render item for rendering.
        """
        ...
    def excludedFromPostEffects(self: Self, *args: Any, **kwargs: Any) -> Any:
        """excludedFromPostEffects() -> bool

        Get whether this item is excluded from post-effects like SSAO and depth-of-field.
        """
        ...
    def geometry(self: Self, *args: Any, **kwargs: Any) -> Any:
        """geometry() -> MGeometry

        Access full geometry data for the render item.
        Returns None if geometry has not been generated yet.
        """
        ...
    def getCustomData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getCustomData() -> MUserData

        Retrieve custom data from the render item, returns None if no such data has ever been set on the render item.
        """
        ...
    def getDefaultMaterialHandling(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getDefaultMaterialHandling() -> MRenderItem.DefaultMaterialFiltering

        Returns whether or not this render item will draw when default material mode is active.
        """
        ...
    def getShader(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getShader() -> MShaderInstance

        Get the shader used by this render item.
        The return value may be None if no shader is set on the render item.
        """
        ...
    def getShaderParameters(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getShaderParameters(name) -> bool / int / float / tuple of floats

        Get the value of a shader parameter.
        This is useful for OverrideNonMaterialItem to retrieve default parameters.
        Use availableShaderParameters() to get the list of available parameters.
        """
        ...
    def isCompatibleWithMayaInstancer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isCompatibleWithMayaInstancer() -> bool

        Returns whether or not this render item can be used as an instance object with Maya Instancer node.
        """
        ...
    def isConsolidated(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isConsolidated() -> bool

        Get the consolidated state of the render item.
        """
        ...
    def isEnabled(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isEnabled() -> bool

        Get the enable state of the render item.
        """
        ...
    def isIsolateSelectCopy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isIsolateSelectCopy() -> bool

        Returns whether or not the render item is a copy created to represent thedrawing of an isolate selected component.

        See setAllowIsolateSelectCopy() for more information.
        """
        ...
    def isShaderFromNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isShaderFromNode() -> bool

        Return True if the shader instance was set by evaluating the shading network of
        a surface shader node (either standard or custom) in the scene via setShaderFromNode().
        """
        ...
    def name(self: Self, *args: Any, **kwargs: Any) -> Any:
        """name() -> string

        Get the name of the render item.
        """
        ...
    def objectTypeExclusionFlag(self: Self, *args: Any, **kwargs: Any) -> Any:
        """objectTypeExclusionFlag() -> long

        Query the bit flag which is used in display filtering based on object types.
        See setObjectTypeExclusionFlag() for details.
        """
        ...
    def primitive(self: Self, *args: Any, **kwargs: Any) -> Any:
        """primitive() -> int

        Get the primitive type drawn by the render item.
        See MGeometry.primitiveString() for a list of valid primitive types.
        """
        ...
    def primitiveAndStride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """primitiveAndStride() -> [int, int]

        Get the primitive type drawn by the render item, as well as its stride.
        See MGeometry.primitiveString() for a list of valid primitive types.
        """
        ...
    def receivesShadows(self: Self, *args: Any, **kwargs: Any) -> Any:
        """receivesShadows() -> bool

        Get the receivesShadows state of the render item.
        """
        ...
    def requiredVertexBuffers(self: Self, *args: Any, **kwargs: Any) -> Any:
        """requiredVertexBuffers() -> MVertexBufferDescriptorList

        Get a list of vertex buffer descriptors that describe the buffers required to draw the given render item.
        These are determined by the shader that will be used to draw the render item and so this method will return
        a non-empty list as long as there is a shader assigned to the render item.
        """
        ...
    sActiveLineDepthPriority: int = ...
    sActivePointDepthPriority: int = ...
    sActiveWireDepthPriority: int = ...
    sDormantFilledDepthPriority: int = ...
    sDormantPointDepthPriority: int = ...
    sDormantWireDepthPriority: int = ...
    sHiliteWireDepthPriority: int = ...
    sSelectionDepthPriority: int = ...
    def selectionMask(self: Self, *args: Any, **kwargs: Any) -> Any:
        """selectionMask() -> MSelectionMask

        Get the render item selection mask.
        """
        ...
    def setAllowIsolateSelectCopy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setAllowIsolateSelectCopy(bool) -> self

        When a 3D model view activates Isolate Select for components, Viewport 2.0will create and maintain necessary render items to represent the drawingof the isolate selected components specifically for that view. These renderitems are copies of their original items and thus have the same propertiesincluding name, type, primitive type, draw mode etc., but their shadingcomponents are filtered from the view selected set of that view.

        By default, a custom render item doesn't allow its copies to be created forthe drawing of isolate selected components; plug-ins should call the methodto allow this. When this is allowed and multiple views have view selectedsets, the render item can have multiple copies and each copy represents thedrawing in only one view.

        Viewport 2.0 is responsible to update these copies for any changes appliedto the original item and the view selected set. It is the duty of the plug-into retrieve the isolate selected components by calling the shadingComponent()method and populate the geometric buffers appropriately.

        The lifetime of the copies is managed by Viewport 2.0, thus it is not safefor plug-ins to cache their pointers.
        """
        ...
    def setBoundingBox(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setBoundingBox(bounds) -> self

        Sets the bounding box for the render item.


        * bounds (MBoundingBox) - The new bounding box.
        """
        ...
    def setCastsShadows(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setCastsShadows(bool) -> self

        Set the castsShadows state of the render item.
        """
        ...
    def setCompatibleWithMayaInstancer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setCompatibleWithMayaInstancer(bool) -> self

        Set whether or not this render item can be used as an instance object with Maya Instancer node.
        """
        ...
    def setCustomData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setCustomData(MUserData) -> self

        Associate custom user data with this render item.
        If deleteAfterUse() is true on the data, then the data object will automatically be deleted when the render item is deleted.
        Otherwise, the lifetime of the user data object is the responsibility of the caller.
        """
        ...
    def setDefaultMaterialHandling(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDefaultMaterialHandling(MRenderItem.DefaultMaterialFiltering) -> self

        Set whether or not this object should be drawn when default material mode is active.
        Set this to DrawOnlyWhenDefaultMaterialActive on render items dedicated to rendering a default material and set it to SkipWhenDefaultMaterialActive on regular shader items that should not draw in that mode.
        If a render item is to be drawn regardless of the mode, leave it at IgnoreDefaultMaterialMode.
        """
        ...
    def setDepthPriority(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDepthPriority(int) -> self

        Set the depth priority of the render item.
        The higher the depth priority the closer it will be drawn to the camera.
        """
        ...
    def setDrawMode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDrawMode(int) -> self

        Set the draw mode for the render item.
        If the draw mode is all, the render item will be drawn regardless of the viewport draw mode.
        Otherwise the render item will only be drawn when the viewport is set to draw objects in the specified mode.
        See MGeometry.drawModeString() for a list of valid draw modes.
        """
        ...
    def setExcludedFromPostEffects(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setExcludedFromPostEffects(bool) -> self

        Set whether this item should be excluded from post-effects like SSAO and depth-of-field.
        Render items default to being excluded from post-effects.
        """
        ...
    def setMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setMatrix(MMatrix) -> bool

        Override the object to world transformation matrix to use when drawing this render item.
        If unset, the render item will draw using the transformation matrix of the associated Maya DAG node.
        Pass None to this method to remove the override
        """
        ...
    def setObjectTypeExclusionFlag(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setObjectTypeExclusionFlag(long) -> self

        Set a bit flag for use in display filtering based on object types. The
        valid bit flags are defined in MFrameContext with names starting with
        "kExclude", except the following ones:

         - MFrameContext.kExcludeGrid
         - MFrameContext.kExcludeHoldOuts
         - MFrameContext.kExcludePluginShapes
         - MFrameContext.kExcludeHUD
         - MFrameContext.kExcludeAll

        When a render item is assigned with a bit flag that has been excluded by
        the current view, the render item will be excluded from display. The
        default value is MFrameContext.kExcludeNone, meaning the info is not to be
        considered when determining whether the render item should be excluded.

        This method only affects items explicitly created by the plug-in.

         * val (long) - A "kExclude" bit flag defined in MFrameContext
        """
        ...
    def setPrimitive(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPrimitive(int, int) -> self

        Set the primitive type of the render item. If it is kPatch, stride will be required to specify the number of control points per patch and the valid values are [1, 32]; otherwise stride won't be used.

        If this item is consolidated, invoking this method may cause this item to be reconsolidated.

        This method only affects items explicitly created by the plug-in.
        """
        ...
    def setReceivesShadows(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setReceivesShadows(bool) -> self

        Set the receivesShadows state of the render item.
        """
        ...
    def setSelectionMask(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setSelectionMask(mask) -> selfsetSelectionMask(type) -> self

        Set the render item selection mask.

        * mask (MSelectionMask) - The selection mask.
        * type (int) - The selection type (see MSelectionMask.addMask() for a list of values).
        """
        ...
    def setShader(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setShader(shader, customStreamName=None) -> bool

        Set shader to use when drawing this render item.
        If no shader is ever set the render item will not draw.
        The render item makes a copy of the instance so it is safe to delete the instance after
        assignment without affecting any render items the instance was assigned to.

        * shader (MShaderInstance) - The shader to use when drawing this item.
        * customStreamName (string) - If specified, shader will generate geometry requirements with the given name.
        """
        ...
    def setShaderFromNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setShaderFromNode(shaderNode, shapePath, linkLostCb=None, linkLostUserData=None, nonTextured=False) -> self

        Set shader to use when drawing this render item. If no shader is ever set this render item will not draw. This method sets the shader instance to a render item by evaluating the shading network of a surface shader node (either standard or custom) in the scene.

        This method only affects items explicitly created by the plug-in.

        If the surface shader node is None or supported by neither Maya nor the plug-in, this method will clear the shader assignment on the render item, which will thus not be drawn.

        The shape path is used as the object context for shading network evaluation to ensure that the shader instance fits its requirements. If the shape path is invalid (e.g. an empty path), a shader instance to fit basic requirements is created but will not include any geometry-dependent requirements.

        The linkLostCb will be invoked whenever the link to the surface shader node is lost. The link can be lost in a number of ways, e.g. shader nodes are deleted or shading network connections are modified. However, the linkLostCb won't be invoked for a change to shading group level connection; if needed, it is the DG node's responsibility to monitor any changes to shading group level connection by MPxNode::connectionMade and MPxNode::connectionBroken.

        There is no guarantee that the surface shader node is still valid after the link is lost. The linkLostCb should check the validity and assign the render item with a shader instance appropriately.

        After the shader instance is set, its parameter values can be automatically updated by Viewport 2.0 whenever the related shading attributes changed, therefore access to the shader instance is not provided in order to avoid unexpected behavior.

         * shaderNode (MObject) - The surface shader node.
         * shapePath (MDagPath) - The DAG path of a shape to be used as the object context for shading network evaluation.
         * linkLostCb (callable) - Function to be invoked whenever the link to the surface shader node is lost.
         * linkLostUserData (MUserData) - User supplied data to be passed into the link lost callback.
         * nonTextured (bool) - Whether or not a non-textured effect instance is needed. The default value is false.
        """
        ...
    def setTreatAsTransparent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setTreatAsTransparent(bool) -> self

        Set whether or not this object should be treated as a transparent item.Set this to true if the object has vertex colors with alpha or other inputsthat make it important to treat this object as if it were transparent.
        """
        ...
    def setWantConsolidation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setWantConsolidation(bool) -> self

        Set whether or not this render item wants to participate in consolidation.

        This method only affects items explicitly created by the plug-in. The value is true by default, unless the item is added to an MSubSceneContainer. When it is true, the geometry of compatible render items will be consolidated into a single render item, to provide better performance.

        Render items that are already instanced cannot be consolidated.

        For render items added to an MSubSceneContainer, if wantConsolidation is set to true, this will prevent them from being instanced until wantConsolidation is set to false.
        """
        ...
    def setWantSubSceneConsolidation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setWantSubSceneConsolidation(bool) -> self

        Sets whether or not this render item is eligible for consolidation in sub scene overrides.

        Render items that are already instanced cannot be consolidated. Setting a render item to
        want sub scene consolidation will prevent the render item from being instanced.
        """
        ...
    def shadingComponent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """shadingComponent() -> MObject

        Get the optional shading component for the render item. It is different fromthe component() method only when a view selected filter is applied.

        Therefore, a typical use of this method is to query the isolate selectedcomponent on a render item created by Viewport 2.0 when a 3D model viewactivates Isolate Select for components. See setAllowIsolateSelectCopy()for more information.

        If the render item doesn't represent the drawing of a shading component,then a null MObject will be returned. Use the isNull() method of the MObjectto check.
        """
        ...
    def sourceDagPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """sourceDagPath() -> MDagPath

        Retrieve the MDagPath for the instance of the object that generated this render item.

         If there are many object instances contributing due to consolidation then only one dag path out of all the objects is returned.

        The method sourceIndexMapping() should be used if the item is consolidatedto access the corresponding dag paths for the objects making up this item.
        """
        ...
    def sourceIndexMapping(self: Self, *args: Any, **kwargs: Any) -> Any:
        """sourceIndexMapping() -> MGeometryIndexMapping

        Get the geometry index mapping of the objects contained by this consolidated render item.
        Multiple geometries can be concatenated to improve rendering performance.
        You can access the index mapping of the geometries in order to render them separately.
        The index mapping gives you the name, and index start and length of each geometry.
        """
        ...
    def type(self: Self, *args: Any, **kwargs: Any) -> Any:
        """type() -> int

        Get the type of the render item.

          MRenderItem.MaterialSceneItem
             A render item which represents an object in the scene that should interact with the rest of the scene and viewport settings (e.g. a shaded piece of geometry which should be considered in processes like shadow computation, viewport effects, etc.). Inclusion in such processes can also still be controlled through the appropriate methods provided by this class.
          MRenderItem.NonMaterialSceneItem
             A render item which represents an object in the scene that should not interact with the rest of the scene and viewport settings, but that is also not part of the viewport UI (e.g. a curve or a bounding box which should not be hidden when 'Viewport UI' is hidden but which should also not participate in processes like shadow computation, viewport effects, etc.).
          MRenderItem.DecorationItem
             A render item which should be considered to be part of the viewport UI (e.g. selection wireframe, components, etc.).
          MRenderItem.InternalItem
             A render item which was created by Maya for internal purposes (e.g. A render item created as the result of a shader being assigned to a DAG node).
          MRenderItem.InternalMaterialItem
        		An internally created MaterialSceneItem for non-textured mode display.
          MRenderItem.InternalTexturedMaterialItem
             An internally created MaterialSceneItem for textured mode display.
          MRenderItem.InternalUnsupportedMaterialItem
             An internally created MaterialSceneItem for showing an unsupported material
        """
        ...
    def wantConsolidation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """wantConsolidation() -> bool

        Return whether or not this render item wants to participate in consolidation.
        """
        ...
    def wantSubSceneConsolidation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """wantSubSceneConsolidation() -> bool

        Returns True if this render item is eligible for consolidation in sub scene overrides.
        """
        ...

class MRenderItemList(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __getitem__(self: Self, key: Any) -> Any:
        """Return self[key]."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __len__(self: Self) -> Any:
        """Return len(self)."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """append(MVertexBufferDescriptor) -> bool

        Add the item to the list. The list assumes ownership of the item.
        """
        ...
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clear() -> self

        Clear the list.
        """
        ...
    def indexOf(self: Self, *args: Any, **kwargs: Any) -> Any:
        """indexOf(name) -> int
        indexOf(name, type) -> int
        indexOf(name, primitive, mode) -> int

        Find the index of the first render item in the list matching the given search parameters.

        * name (string) - The name of the render item.
        * type (int) - The type of the render item.
        * primitive (int) - The primitive type of the render item.
        * mode (int) - The draw mode of the render item.

        See MRenderItem.type() for a list of valid render item types.
        See MGeometry.primitiveString() for a list of valid primitive types.
        See MGeometry.drawModeString() for a list of valid draw modes.
        """
        ...
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """remove(index) -> bool

        Remove the item at the specified index. Item is deleted.
        """
        ...

class MRenderOperation(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def enableSRGBWrite(self: Self, *args: Any, **kwargs: Any) -> Any:
        """enableSRGBWrite() -> bool

        Return whether to enable GPU based gamma correction during pixel writes.
        """
        ...
    kClear: int = ...
    kHUDRender: int = ...
    kPresentTarget: int = ...
    kQuadRender: int = ...
    kSceneRender: int = ...
    kUserDefined: int = ...
    def name(self: Self, *args: Any, **kwargs: Any) -> Any:
        """name() -> string

        Returns the name of the render operator.
        """
        ...
    def operationType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """operationType() -> int

        Returns the type of a render operator.
        """
        ...
    def targetOverrideList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """targetOverrideList() -> list of MRenderTarget

        Return a list of render target which will be used as the target overrides for the operation.
        """
        ...
    def viewportRectangleOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """viewportRectangleOverride() -> MFloatPoint

        Query for a viewport rectangle override.
        """
        ...

class MRenderOverride(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def cleanup(self: Self, *args: Any, **kwargs: Any) -> Any:
        """cleanup() -> self

        Perform any cleanup required following the execution of render operations.
        """
        ...
    def getFrameContext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFrameContext() -> MFrameContext

        Return a frame context. The context is not available if called before setup() or after cleanup().
        The context should never be deleted by the plug-in as it is owned by the render override.
        """
        ...
    def name(self: Self, *args: Any, **kwargs: Any) -> Any:
        """name() -> string

        Returns the name of the override.
        """
        ...
    def nextRenderOperation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """nextRenderOperation() -> bool

        Iterate to the next operation. If there are no more operations then this method should return false.
        """
        ...
    def renderOperation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """renderOperation() -> MRenderOperation

        Return the current operation being iterated over.
        """
        ...
    def select(self: Self, *args: Any, **kwargs: Any) -> Any:
        """select(frameContext, selectInfo, useDepth, selectionList, worldSpaceHitPts) -> bool

        The method is called by Maya to override the default Viewport 2.0 selection. It returns false by default, meaning the default selection will be used. If an implementation returns true, selectionList and worldSpaceHitPts will be used to override the default selection.

        A complete implementation requires hit testing and selection interpretation. If an object is hit, the implementation should add its DAG path (and also its component when appropriate) to selectionList and add the world-space hit point between the selected item and selection ray to worldSpaceHitPts. The number of elements in selectionList and worldSpaceHitPts must be the same in any case, a selected item (typically a vertex component) and a hit point at the same array index will be associated.

        If the method is triggered for point snapping, the implementation needs to sort the hit points and return the one nearest to the cursor. The state of point snapping can be queried from selectInfo.

        When an implementation returns true to override the default behavior, the object-level selection override methods won't be triggered any more:

        * MPxGeometryOverride::refineSelectionPath * MPxSubSceneOverride::getInstancedSelectionPath * MPxDrawOverride::userSelect * MPxDrawOverride::refineSelectionPath 

        * frameContext [IN] (MFrameContext) - The frame-level context information
        * selectInfo [IN] (MSelectionInfo) - The selection info
        * useDepth [IN] (bool) - Whether only the objects nearest to camera can be selected
        * selectionList [OUT] (MSelectionList) - List of items selected by this method
        * worldSpaceHitPts [OUT] (MPointArray) - List of hit points
        """
        ...
    def setup(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setup(destination) -> self

        Perform any setup required before render operations are to be executed.
        """
        ...
    def startOperationIterator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """startOperationIterator() -> bool

        Query if there are any operations to iterate over.
        """
        ...
    def supportedDrawAPIs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """supportedDrawAPIs() -> int

        Returns the draw APIs supported by this override.
        See MRenderer.drawAPI() description for the list of draw APIs.
        """
        ...
    def uiName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """uiName() -> string

        Returns the user interface name for the override.
        """
        ...

class MRenderParameters(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def getParameter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getParameter(parameterName, bool) -> self
        getParameter(parameterName, int) -> self
        getParameter(parameterName, float) -> self
        getParameter(parameterName, list of float) -> self
        getParameter(parameterName, MFloatVector) -> self
        getParameter(parameterName, MMatrix) -> self
        getParameter(parameterName, MFloatMatrix) -> self
        getParameter(parameterName, MTextureAssignment) -> self
        getParameter(parameterName, MRenderTargetAssignment) -> self
        getParameter(parameterName, MSamplerStateDesc) -> self

        Get the value of the named parameter.
        """
        ...
    def isArrayParameter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isArrayParameter(string) -> bool

        Determine whether the named parameter is an array.
        """
        ...
    def parameterList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """parameterList() -> list of string

        Get the names of all parameters that are settable on this shader instance.
        """
        ...
    def parameterType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """parameterType(string) -> int

        Get the type of the named parameter, returns kInvalid if parameter is not found.
        """
        ...
    def semantic(self: Self, *args: Any, **kwargs: Any) -> Any:
        """semantic(string) -> string

        Return the semantic for a named parameter.
        """
        ...
    def setArrayParameter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setArrayParameter(parameterName, sequence of bool, int) -> self
        setArrayParameter(parameterName, sequence of int, int) -> self
        setArrayParameter(parameterName, sequence of float, int) -> self
        setArrayParameter(parameterName, sequence of MMatrix, int) -> self

        Set the value of a named array parameter.
        """
        ...
    def setParameter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setParameter(parameterName, bool) -> self
        setParameter(parameterName, int) -> self
        setParameter(parameterName, float) -> self
        setParameter(parameterName, list of float) -> self
        setParameter(parameterName, MFloatVector) -> self
        setParameter(parameterName, MMatrix) -> self
        setParameter(parameterName, MFloatMatrix) -> self
        setParameter(parameterName, MTextureAssignment) -> self
        setParameter(parameterName, MRenderTargetAssignment) -> self
        setParameter(parameterName, MSamplerState) -> self

        Set the value of the named parameter.
        """
        ...

class MRenderProfile(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def addRenderer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addRenderer(renderer) -> selfaddRenderer(name, version) -> self

        Add an internal renderer to this profile:
        * renderer (int) - One of Maya's internal renderers:
          kMayaSoftware,
          kMayaOpenGL,
          kMayaD3D

        Or add a custom renderer to this profile:
        * name (string) - The name of the renderer,
        * version (float) = The version of the renderer or rendering API.
        The name and version specified must correspond to a renderer registered with Maya. Currently, only Maya's internal renderers (just named after the APIs they use: 'OpenGL', 'D3D', or 'Software') are supported. When registering support for Maya's internal renderers, it's simpler to use the other version of this method.
        """
        ...
    def hasRenderer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasRenderer(renderer) -> boolhasRenderer(name, version) -> bool

        Check if a Maya renderer is listed in this profile:
        * renderer (int) - One of Maya's internal renderers, see addRenderer().

        Or check if a custom renderer is in this render profile:
        * name (string) - The name of the renderer,
        * version (float) = The version of the renderer or rendering API.
        see addRenderer()
        """
        ...
    kMayaD3D: int = ...
    kMayaOpenGL: int = ...
    kMayaSoftware: int = ...
    def numberOfRenderers(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numberOfRenderers() -> int

        Return the number of renderers in this profile.
        """
        ...

class MRenderTarget(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def freeRawData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """freeRawData(long) -> None
        Deallocate system memory - retrieved from rawData().
        """
        ...
    def rawData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """rawData() -> [long, rowPitch, slicePitch]

        Get a copy of the raw data mapped to the target.
        The caller must deallocate the system memory (using freeRawData()) as the target itself does not keep any references to it.

        * rowPitch [OUT] (int) - The row pitch of the data. It represents the number of bytes of one line of the target data.
        * slicePitch [OUT] (int) - The slice pitch of the data. It represents the number of bytes of the whole target data.
        """
        ...
    def resourceHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """resourceHandle() -> long

        Returns a long containing a C++ 'void' pointer which points to the draw API dependent handle for a render target.
        For OpenGL, a pointer to an OpenGL texture identifier is returned.
        For DirectX, a reference to a Direct3D "view" of a target is returned.
        """
        ...
    def targetDescription(self: Self, *args: Any, **kwargs: Any) -> Any:
        """targetDescription() -> MRenderTargetDescription

        Get target description.
        """
        ...
    def updateDescription(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateDescription(MRenderTargetDescription) -> self

        Change the description of a render target.
        """
        ...

class MRenderTargetAssignment(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    @property
    def target(*args: Any, **kwargs: Any) -> Any:
        """The render target"""
        ...
    @target.setter
    def target(*args: Any, **kwargs: Any) -> Any:
        """The render target"""
        ...

class MRenderTargetDescription(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def allowsUnorderedAccess(self: Self, *args: Any, **kwargs: Any) -> Any:
        """allowsUnorderedAccess() -> bool

        Query whether unordered access is supported.
        """
        ...
    def arraySliceCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """arraySliceCount() -> int

        Query the number of array slices defined by the description.
        """
        ...
    def compatibleWithDescription(self: Self, *args: Any, **kwargs: Any) -> Any:
        """compatibleWithDescription(MRenderTargetDescription) -> bool

        Determine if another target with a given description is 'compatible' with a target using this description.
        """
        ...
    def height(self: Self, *args: Any, **kwargs: Any) -> Any:
        """height() -> int

        Query the height of a 2D render target slice.
        """
        ...
    def isCubeMap(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isCubeMap() -> bool

        Query whether this is a cube map target.
        """
        ...
    def multiSampleCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """multiSampleCount() -> int

        Query the multi-sample count defined by the description.
        """
        ...
    def name(self: Self, *args: Any, **kwargs: Any) -> Any:
        """name() -> string

        Query the name identifier for the target description.
        """
        ...
    def rasterFormat(self: Self, *args: Any, **kwargs: Any) -> Any:
        """rasterFormat() -> int

        Query the raster format defined by the description.
        """
        ...
    def setAllowsUnorderedAccess(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setAllowsUnorderedAccess(bool) -> self

        Set the flag for unordered data access for the target.
        """
        ...
    def setArraySliceCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setArraySliceCount(int) -> self

        Set array slice count of the target.
        """
        ...
    def setHeight(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setHeight(int) -> self

        Set height of the target.
        """
        ...
    def setIsCubeMap(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setIsCubeMap(bool) -> self

        Set cube map flag for the target.
        """
        ...
    def setMultiSampleCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setMultiSampleCount(int) -> self

        Set multisample count of the target.
        """
        ...
    def setName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setName(string) -> self

        Set name of the target.
        """
        ...
    def setRasterFormat(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setRasterFormat(int) -> self

        Set the raster format of the target.
        """
        ...
    def setWidth(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setWidth(int) -> self

        Set width of the target.
        """
        ...
    def width(self: Self, *args: Any, **kwargs: Any) -> Any:
        """width() -> int

        Query the width of a 2D render target slice.
        """
        ...

class MRenderTargetManager(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def acquireRenderTarget(self: Self, *args: Any, **kwargs: Any) -> Any:
        """acquireRenderTarget(MRenderTargetDescription) -> MRenderTarget
        Acquire an instance of a render target.
        When the object is no longer needed, releaseRenderTarget() should be called
        to notify the target manager that the caller is done with the render target.
        """
        ...
    def acquireRenderTargetFromScreen(self: Self, *args: Any, **kwargs: Any) -> Any:
        """acquireRenderTargetFromScreen(string) -> MRenderTarget
        Acquire an instance of a render target with the same characteristics as the current on-screen target.
        When the object is no longer needed, releaseRenderTarget() should be called
        to notify the target manager that the caller is done with the render target.
        """
        ...
    def formatSupportsSRGBWrite(self: Self, *args: Any, **kwargs: Any) -> Any:
        """formatSupportsSRGBWrite(int) -> bool
        This method will perform a check to determine whether gamma correction can be performed
        by the GPU when writing pixels to a render target of a given format.
        """
        ...
    def releaseRenderTarget(self: Self, *args: Any, **kwargs: Any) -> Any:
        """releaseRenderTarget(MRenderTarget) -> self
        Deletes the MRenderTarget and releases the reference to the underlying target which is held by the MRenderTarget object.
        """
        ...

class MRenderUtilities(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def acquireSwatchDrawContext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """acquireSwatchDrawContext() -> MDrawContext
        acquireSwatchDrawContext(colorTarget) -> MDrawContext
        acquireSwatchDrawContext(colorTarget, depthTarget) -> MDrawContext

        Acquire a draw context fit for rendering a swatch.
        The caller is responsible for releasing the draw context when it is no longer needed, by calling MRenderUtilities::releaseDrawContext().

        * colorTarget (MRenderTarget) -  The color target for swatch drawing.
        * depthTarget (MRenderTarget) -  The depth target for swatch drawing.
        If targets are not provided, the caller is responsible for properly setting up render targets.
        Specifying targets also insures that the proper GL context is made active when using GL devices.
        """
        ...
    def acquireUVTextureDrawContext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """acquireUVTextureDrawContext() -> MDrawContext
        acquireUVTextureDrawContext(colorTarget) -> MDrawContext
        acquireUVTextureDrawContext(colorTarget, depthTarget) -> MDrawContext

        Acquire a draw context fit for rendering a texture for the UV editor.
        The caller is responsible for releasing the draw context when it is no longer needed, by calling MRenderUtilities::releaseDrawContext().

        * colorTarget (MRenderTarget) -  The color target for UV texture drawing.
        * depthTarget (MRenderTarget) -  The depth target for UV texture drawing.
        If targets are not provided, the caller is responsible for properly setting up render targets.
        Specifying targets also insures that the proper GL context is made active when using GL devices.
        """
        ...
    def blitTargetToGL(self: Self, *args: Any, **kwargs: Any) -> Any:
        """blitTargetToGL(target, region, unfiltered) -> None

        Blit the data from a target to current GL context.

        * target (MRenderTarget) - The source target to get the data from.
        * region (float[2][2]) - Rectangular region to be rendered - [ [x1, y1], [x2, y2] ].
        * unfiltered (bool) - Render with hardware filtering or sharply defined pixels.
        """
        ...
    def blitTargetToImage(self: Self, *args: Any, **kwargs: Any) -> Any:
        """blitTargetToImage(target, image) -> None

        Copy the data from a target to an image.

        * target (MRenderTarget) - The source target to get the data from.
        * image (MImage) - The destination image to copy the data to.
        """
        ...
    def drawSimpleMesh(self: Self, *args: Any, **kwargs: Any) -> Any:
        """drawSimpleMesh(context, vertexBuffer, indexBuffer, primitiveType, start, count) -> None

        Render a simple mesh.

        * context (MDrawContext) - The draw context to use for render.
        * vertexBuffer (MVertexBuffer) - The vertex buffer for the mesh.
        * indexBuffer (MIndexBuffer) - The index buffer for the mesh.
        * primitiveType (int) - The primitive type of the mesh. See MGeometry.primitiveString()
        * start (int) - The location of the first index read from the index buffer.
        * count (int) - The number of indices to draw.
        """
        ...
    kAmbientLight: int = ...
    kDefaultLights: int = ...
    kOrthogonalCameraCloseUp: int = ...
    kOrthogonalCameraWithMargin: int = ...
    kPerspectiveCamera: int = ...
    kSwatchLight: int = ...
    def releaseDrawContext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """releaseDrawContext(context) -> None
        releaseDrawContext(context, releaseTargets) -> None

        Release a draw context.

        * context (MDrawContext) - The draw context to release.
        * releaseTargets (bool) - Removes the current draw targets from the device, defaults to true.
        If releaseTargets is requested, the device will have NULL targets on function exit.
        """
        ...
    def renderMaterialViewerGeometry(self: Self, *args: Any, **kwargs: Any) -> Any:
        """renderMaterialViewerGeometry(shape, shaderNode, image, cameraMode=kPerspectiveCamera, lightRig=kDefaultLights) -> None

        Do an off-screen render replicating the results shown by the Material Viewer window of Hypershade..

        * shape (str) Shape to render. Valid values include "meshSphere", "meshPlane", "meshShaderball", "meshTeapot", and "meshCloth".
        * shaderNode (MObject) The shader node to use on the geometry.
        * image (MImage) The image where the result should be stored.
        * cameraMode (int) The camera to use for rendering. Defaults to MRenderUtilities.kPerspectiveCamera.
        * lightRig (int) The light rig to use for rendering. Defaults to MRenderUtilities.kDefaultLights.
        """
        ...
    def swatchBackgroundColor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """swatchBackgroundColor() -> MColor

        Returns the default background color for the hardware rendered swatch.
        """
        ...

class MRenderer(object):
    def GPUDeviceHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """GPUDeviceHandle() -> long

        Returns a long containing a C++ 'void' pointer which points to the GPU "device".In the case that the drawing API is OpenGL then the "device" is a handle to an OpenGL context.
        In the case that the drawing API is DirectX then the "device" is a pointer to a DirectX device.
        """
        ...
    def GPUmaximumPrimitiveCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """GPUmaximumPrimitiveCount() -> int

        Returns the maximum number of primitives that can be drawn per draw call by the GPU device.
        0 if device has not been initialized.
        """
        ...
    def GPUmaximumVertexBufferSize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """GPUmaximumVertexBufferSize() -> int

        Returns the maximum number of vertices allowed in a vertex buffer by the GPU device.
        0 if device has not been initialized.
        """
        ...
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def activeRenderOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """activeRenderOverride() -> string

        Returns the name of the active override.
        """
        ...
    def copyTargetToScreen(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copyTargetToScreen(MRenderTarget) -> bool

        Copy a render target to the screen.
        If the target's dimensions are not the same as the active viewport it will be scaled up or down as necessary to fill the entire viewport.
        """
        ...
    def deregisterOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deregisterOverride(MRenderOverride) -> None

        Deregister an existing render override on the renderer.
        The renderer will remove this override from it's list of registered overrides.
        """
        ...
    def disableChangeManagementUntilNextRefresh(self: Self, *args: Any, **kwargs: Any) -> Any:
        """disableChangeManagementUntilNextRefresh() -> None

        Calling this method will cause Viewport 2.0 to stop processing all changes to the Maya scene until the next viewport refresh.
        """
        ...
    def drawAPI(self: Self, *args: Any, **kwargs: Any) -> Any:
        """drawAPI() -> int

        Returns the current drawing API. Returns 'kNone' if the renderer is not initialized.

          MRenderer.kNone          Uninitialized device
          MRenderer.kOpenGL        OpenGL
          MRenderer.kDirectX11     Direct X 11
          MRenderer.kAllDevices    All : OpenGL and Direct X 11
        """
        ...
    def drawAPIIsOpenGL(self: Self, *args: Any, **kwargs: Any) -> Any:
        """drawAPIIsOpenGL() -> bool

        Returns whether the current drawing API is OpenGL or not
        """
        ...
    def drawAPIVersion(self: Self, *args: Any, **kwargs: Any) -> Any:
        """drawAPIVersion() -> int

        Returns the version of drawing API.
        """
        ...
    def findRenderOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """findRenderOverride(string) -> MRenderOverride

        Returns a reference to an existing render override registered with the renderer.
        """
        ...
    def getFragmentManager(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFragmentManager() -> MFragmentManager

        Returns the fragment manager or None if the renderer is not initialized properly.
        """
        ...
    def getRenderTargetManager(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getRenderTargetManager() -> MRenderTargetManager

        Returns the render target manager or None if the renderer is not initialized properly.
        """
        ...
    def getShaderManager(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getShaderManager() -> MShaderManager

        Returns the shader manager or None if the renderer is not initialized properly.
        """
        ...
    def getTextureManager(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getTextureManager() -> MTextureManager

        Returns the texture manager or None if the renderer is not initialized properly.
        """
        ...
    kA8: int = ...
    kA8B8G8R8: int = ...
    kAllDevices: int = ...
    kB5G5R5A1: int = ...
    kB5G6R5: int = ...
    kB8G8R8A8: int = ...
    kB8G8R8X8: int = ...
    kBC6H_SF16: int = ...
    kBC6H_UF16: int = ...
    kBC7_UNORM: int = ...
    kBC7_UNORM_SRGB: int = ...
    kD24S8: int = ...
    kD24X8: int = ...
    kD32_FLOAT: int = ...
    kDXT1_UNORM: int = ...
    kDXT1_UNORM_SRGB: int = ...
    kDXT2_UNORM: int = ...
    kDXT2_UNORM_PREALPHA: int = ...
    kDXT2_UNORM_SRGB: int = ...
    kDXT3_UNORM: int = ...
    kDXT3_UNORM_PREALPHA: int = ...
    kDXT3_UNORM_SRGB: int = ...
    kDXT4_SNORM: int = ...
    kDXT4_UNORM: int = ...
    kDXT5_SNORM: int = ...
    kDXT5_UNORM: int = ...
    kDirectX11: int = ...
    kL16: int = ...
    kL8: int = ...
    kNone: int = ...
    kNumberOfRasterFormats: int = ...
    kOpenGL: int = ...
    kOpenGLCoreProfile: int = ...
    kR10G10B10A2_UINT: int = ...
    kR10G10B10A2_UNORM: int = ...
    kR16G16B16A16_FLOAT: int = ...
    kR16G16B16A16_SINT: int = ...
    kR16G16B16A16_SNORM: int = ...
    kR16G16B16A16_UINT: int = ...
    kR16G16B16A16_UNORM: int = ...
    kR16G16_FLOAT: int = ...
    kR16G16_SINT: int = ...
    kR16G16_SNORM: int = ...
    kR16G16_UINT: int = ...
    kR16G16_UNORM: int = ...
    kR16_FLOAT: int = ...
    kR16_SINT: int = ...
    kR16_SNORM: int = ...
    kR16_UINT: int = ...
    kR16_UNORM: int = ...
    kR1_UNORM: int = ...
    kR24G8: int = ...
    kR24X8: int = ...
    kR32G32B32A32_FLOAT: int = ...
    kR32G32B32A32_SINT: int = ...
    kR32G32B32A32_UINT: int = ...
    kR32G32B32_FLOAT: int = ...
    kR32G32B32_SINT: int = ...
    kR32G32B32_UINT: int = ...
    kR32G32_FLOAT: int = ...
    kR32G32_SINT: int = ...
    kR32G32_UINT: int = ...
    kR32_FLOAT: int = ...
    kR32_SINT: int = ...
    kR32_UINT: int = ...
    kR8G8B8A8_SINT: int = ...
    kR8G8B8A8_SNORM: int = ...
    kR8G8B8A8_UINT: int = ...
    kR8G8B8A8_UNORM: int = ...
    kR8G8B8X8: int = ...
    kR8G8_SINT: int = ...
    kR8G8_SNORM: int = ...
    kR8G8_UINT: int = ...
    kR8G8_UNORM: int = ...
    kR8_SINT: int = ...
    kR8_SNORM: int = ...
    kR8_UINT: int = ...
    kR8_UNORM: int = ...
    kR9G9B9E5_FLOAT: int = ...
    def needEvaluateAllLights(self: Self, *args: Any, **kwargs: Any) -> Any:
        """needEvaluateAllLights() -> None

        Notify the Viewport 2.0 renderer that it should evaluate all lights marked dirty, regardless of the light limit.For example, if there are 8 lights accessible because of the Viewport 2.0 light limit option, Only the first 8 non-ambient lights created will be evaluated.Call this method to instruct Viewport 2.0 to evaluate all dirty lights regardless of the light limit option.

        Note that this method does NOT perform any DG evaluation when it is called.The actual evaluation does not occur until the next viewport refresh. This method is threadsafe. The viewport refresh will occur asynchronously.Multiple calls to this method will get merged.

        Call this method may decrease performance in Viewport 2.0 during the next viewport refresh.Once this method is called, all unused lights that are marked dirty will be evaluated in the next viewport refresh.

        An example application of this method is to obtain light information while ignoring the light limit.If this method is not called, information on unused lights cannot be obtained via MDrawContext, even if LightFilter is set to kFilteredToLightLimit.This is because unused lights are not evaluated automatically by Viewport 2.0 by default.
        """
        ...
    def outputTargetSize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """outputTargetSize() -> [int, int]

        Get target size in format [width, height].
        """
        ...
    def registerOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """registerOverride(MRenderOverride) -> None

        Register the override as being usable by the renderer.
        If the override is already registered it will not be registered again.
        """
        ...
    def render(self: Self, *args: Any, **kwargs: Any) -> Any:
        """render(sourceName, targetList) -> bool

        Render images from a panel to render targets.
        return True if render operation was successful.
        * sourceName (string) - The name of the source view want to render. 
        * targetList (PyListObject:MRenderTarget) - Render target list want to render into.
        """
        ...
    def renderOverrideCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """renderOverrideCount() -> int

        Returns the number of registered render overrides.
        """
        ...
    def renderOverrideName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """renderOverrideName() -> string

        Get the current render override name used for batch rendering.
        If there is no override then an empty string will be returned.
        """
        ...
    def setGeometryDrawDirty(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setGeometryDrawDirty(object, topologyChanged=True) -> None

        Notify the Viewport 2.0 renderer that the geometry (size, shape, etc.) of object has changed, causing the object to be updated in the viewport.

        * object (MObject) - DAG object which has been modified.
        * topologyChanged (bool) - has the object topology changed
        """
        ...
    def setLightRequiresShadows(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setLightRequiresShadows(object, flag) -> bool

        This method allows for plug-in writers to indicate that the shadow map contents for a given light are required, regardless of the light limit.
        Returns True if the method added or removed the request successfully.

        * object (MObject) - Light to request shadow update for
        * flag (bool) - Indicate if an update is requested. When set to true a request is added, and when set false any existing request is removed.
        """
        ...
    def setLightsAndShadowsDirty(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setLightsAndShadowsDirty() -> None

        Notify the Viewport 2.0 renderer that something has changed which requires re-evaluation of lighting and shadows.
        """
        ...
    def setRenderOverrideName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setRenderOverrideName(string) -> bool

        Set the name of a render override (MRenderOverride) for batch rendering.
        """
        ...

class MSamplerState(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def desc(self: Self, *args: Any, **kwargs: Any) -> Any:
        """desc() -> MSamplerStateDesc

        Get the sampler state descriptor that was used to create the state object.
        """
        ...
    kAnisotropic: int = ...
    kMinLinear_MagMipPoint: int = ...
    kMinLinear_MagPoint_MipLinear: int = ...
    kMinMagLinear_MipPoint: int = ...
    kMinMagMipLinear: int = ...
    kMinMagMipPoint: int = ...
    kMinMagPoint_MipLinear: int = ...
    kMinPoint_MagLinear_MipPoint: int = ...
    kMinPoint_MagMipLinear: int = ...
    kTexBorder: int = ...
    kTexClamp: int = ...
    kTexMirror: int = ...
    kTexWrap: int = ...
    def resourceHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """resourceHandle() -> long

        Returns a long containing a C++ 'void' pointer which points to the draw API dependent handle for a sampler state.
        For OpenGL, such a handle does not exist and a NULL pointer will be returned.
        For DirectX, a pointer to a Direct3D state will be returned.
        """
        ...

class MSamplerStateDesc(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    @property
    def addressU(*args: Any, **kwargs: Any) -> Any:
        """Select the u coordinate addressing mode, default kTexWrap"""
        ...
    @addressU.setter
    def addressU(*args: Any, **kwargs: Any) -> Any:
        """Select the u coordinate addressing mode, default kTexWrap"""
        ...
    @property
    def addressV(*args: Any, **kwargs: Any) -> Any:
        """Select the v coordinate addressing mode, default kTexWrap"""
        ...
    @addressV.setter
    def addressV(*args: Any, **kwargs: Any) -> Any:
        """Select the v coordinate addressing mode, default kTexWrap"""
        ...
    @property
    def addressW(*args: Any, **kwargs: Any) -> Any:
        """Select the w coordinate addressing mode, default kTexWrap"""
        ...
    @addressW.setter
    def addressW(*args: Any, **kwargs: Any) -> Any:
        """Select the w coordinate addressing mode, default kTexWrap"""
        ...
    @property
    def borderColor(*args: Any, **kwargs: Any) -> Any:
        """Set border color used for accesses beyond texture 0..1, default(0,0,0,0)"""
        ...
    @borderColor.setter
    def borderColor(*args: Any, **kwargs: Any) -> Any:
        """Set border color used for accesses beyond texture 0..1, default(0,0,0,0)"""
        ...
    @property
    def comparisonFn(*args: Any, **kwargs: Any) -> Any:
        """Selects the filter comparison function, default kCompareAlways"""
        ...
    @comparisonFn.setter
    def comparisonFn(*args: Any, **kwargs: Any) -> Any:
        """Selects the filter comparison function, default kCompareAlways"""
        ...
    @property
    def coordCount(*args: Any, **kwargs: Any) -> Any:
        """Set the number of texture coordinates, default 2"""
        ...
    @coordCount.setter
    def coordCount(*args: Any, **kwargs: Any) -> Any:
        """Set the number of texture coordinates, default 2"""
        ...
    @property
    def elementIndex(*args: Any, **kwargs: Any) -> Any:
        """When using texture arrays, selects array element, default 0"""
        ...
    @elementIndex.setter
    def elementIndex(*args: Any, **kwargs: Any) -> Any:
        """When using texture arrays, selects array element, default 0"""
        ...
    @property
    def filter(*args: Any, **kwargs: Any) -> Any:
        """Selects how to filter a texture sample, default kMinMagMipPoint"""
        ...
    @filter.setter
    def filter(*args: Any, **kwargs: Any) -> Any:
        """Selects how to filter a texture sample, default kMinMagMipPoint"""
        ...
    @property
    def maxAnisotropy(*args: Any, **kwargs: Any) -> Any:
        """Set the maximum anisotropy permitted for anisotropic filters. The range is 1..16, default 1"""
        ...
    @maxAnisotropy.setter
    def maxAnisotropy(*args: Any, **kwargs: Any) -> Any:
        """Set the maximum anisotropy permitted for anisotropic filters. The range is 1..16, default 1"""
        ...
    @property
    def maxLOD(*args: Any, **kwargs: Any) -> Any:
        """Set maximum mip LOD level accessed, default 16"""
        ...
    @maxLOD.setter
    def maxLOD(*args: Any, **kwargs: Any) -> Any:
        """Set maximum mip LOD level accessed, default 16"""
        ...
    @property
    def minLOD(*args: Any, **kwargs: Any) -> Any:
        """Set minimum mip LOD level accessed, default 0"""
        ...
    @minLOD.setter
    def minLOD(*args: Any, **kwargs: Any) -> Any:
        """Set minimum mip LOD level accessed, default 0"""
        ...
    @property
    def mipLODBias(*args: Any, **kwargs: Any) -> Any:
        """Set a float bias to be added to the computed mip LOD level, default 0"""
        ...
    @mipLODBias.setter
    def mipLODBias(*args: Any, **kwargs: Any) -> Any:
        """Set a float bias to be added to the computed mip LOD level, default 0"""
        ...
    def setDefaults(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDefaults() -> self

        Set all values for the target blend state to their default values.
        """
        ...

class MSceneRender(MRenderOperation):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def addPostUIDrawables(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addPostUIDrawables(drawManager, frameContext) -> self

        Provides access to the MUIDrawManager, which can be used to queue up operations to draw simple UI shapes like lines, circles, text, etc.

        This method will only be called when hasUIDrawables() is overridden to return true and kRenderPostSceneUIItems is set in the MSceneFilterOption mask returned by renderFilterOverride().

        UI drawables added in this method will be rendered after the scene render.

        * drawManager (MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry including text.
        * frameContext (MFrameContext) - Frame level context information
        """
        ...
    def addPreUIDrawables(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addPreUIDrawables(drawManager, frameContext) -> self

        Provides access to the MUIDrawManager, which can be used to queue up operations to draw simple UI shapes like lines, circles, text, etc.

        This method will only be called when hasUIDrawables() is overridden to return true and kRenderPreSceneUIItems is set in the MSceneFilterOption mask returned by renderFilterOverride().

        UI drawables added in this method will be rendered before the scene render.

        * drawManager (MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry including text.
        * frameContext (MFrameContext) - Frame level context information
        """
        ...
    def cameraOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """cameraOverride() -> MCameraOverride

        Query for a camera override.
        """
        ...
    def clearOperation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clearOperation() -> MClearOperation

        Get the scene clear operation.
        """
        ...
    def cullingOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """cullingOverride() -> int

        Query for a face culling override.

          MSceneRender.kNoCullingOverride    No culling override
          MSceneRender.kCullNone             Don't perform culling
          MSceneRender.kCullBackFaces        Cull back faces
          MSceneRender.kCullFrontFaces       Cull front faces
        """
        ...
    def displayModeOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """displayModeOverride() -> int

        Query for any display mode override.

          MSceneRender.kNoDisplayModeOverride  No display mode override
          MSceneRender.kWireFrame              Display wireframe
          MSceneRender.kShade                  Display shaded textured
          MSceneRender.kFlatShaded             Display flat shaded
          MSceneRender.kShadeActiveOnly        Shade active objects. Only applicable if kShade or kFlatShaded is enabled.
          MSceneRender.kBoundingBox            Display bounding boxes
          MSceneRender.kDefaultMaterial        Use default material. Only applicable if kShade or kFlatShaded is enabled.
          MSceneRender.kTextured               Display textured. Only applicable if kShade or kFlatShaded is enabled.
        """
        ...
    def enableSRGBWrite(self: Self, *args: Any, **kwargs: Any) -> Any:
        """enableSRGBWrite() -> bool

        Return whether to enable GPU based gamma correction during pixel writes.
        """
        ...
    def fragmentName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """fragmentName() -> String

        Query the name of the fragment used to render the scene.
        """
        ...
    def getObjectTypeExclusions(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getObjectTypeExclusions() -> long

        Query for any object type exclusions.

          MFrameContext.kExcludeNone                 Exclude no object types
          MFrameContext.kExcludeNurbsCurves          Exclude NURBS curves
          MFrameContext.kExcludeNurbsSurfaces        Exclude NURBS surface
          MFrameContext.kExcludeMeshes               Exclude polygonal meshes
          MFrameContext.kExcludePlanes               Exclude planes
          MFrameContext.kExcludeLights               Exclude lights
          MFrameContext.kExcludeCameras              Exclude camera
          MFrameContext.kExcludeJoints               Exclude joints
          MFrameContext.kExcludeIkHandles            Exclude IK handles
          MFrameContext.kExcludeDeformers            Exclude all deformations
          MFrameContext.kExcludeDynamics             Exclude all dynamics objects (emiters, cloth)
          MFrameContext.kExcludeParticleInstancers   Exclude all Particle Instancers
          MFrameContext.kExcludeLocators             Exclude locators
          MFrameContext.kExcludeDimensions           Exclude all measurement objects
          MFrameContext.kExcludeSelectHandles        Exclude selection handles
          MFrameContext.kExcludePivots               Exclude pivots
          MFrameContext.kExcludeTextures             Exclude texure placement objects
          MFrameContext.kExcludeGrid                 Exclude grid drawing
          MFrameContext.kExcludeCVs                  Exclude NURBS control vertices
          MFrameContext.kExcludeHulls                Exclude NURBS hulls
          MFrameContext.kExcludeStrokes              Exclude PaintFX strokes
          MFrameContext.kExcludeSubdivSurfaces       Exclude subdivision surfaces
          MFrameContext.kExcludeFluids               Exclude fluid objects
          MFrameContext.kExcludeFollicles            Exclude hair follicles
          MFrameContext.kExcludeHairSystems          Exclude hair system
          MFrameContext.kExcludeImagePlane           Exclude image planes
          MFrameContext.kExcludeNCloths              Exclude N-cloth objects
          MFrameContext.kExcludeNRigids              Exclude rigid-body objects
          MFrameContext.kExcludeDynamicConstraints   Exclude rigid-body constraints
          MFrameContext.kExcludeManipulators         Exclude manipulators
          MFrameContext.kExcludeNParticles           Exclude N-particle objects
          MFrameContext.kExcludeMotionTrails         Exclude motion trails
          MFrameContext.kExcludeHoldOuts				Exclude Hold-Outs
          MFrameContext.kExcludePluginShapes			Exclude plug-in shapes
          MFrameContext.kExcludeHUD				    Exclude HUD
          MFrameContext.kExcludeClipGhosts			Exclude animation clip ghosts
          MFrameContext.kExcludeGreasePencils		Exclude grease-pencil draw
          MFrameContext.kExcludeControllers			Exclude controllers objects
          MFrameContext.kExcludeAll                  Exclude all listed object types
        """
        ...
    def getParameters(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getParameters() -> MRenderParameters

        Method to return the operation's parameter set.
        """
        ...
    def hasUIDrawables(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasUIDrawables() -> bool

        Query whether addUIDrawables() should be called or not.
        """
        ...
    kAmbientLight: int = ...
    kBoundingBox: int = ...
    kClear: int = ...
    kCullBackFaces: int = ...
    kCullFrontFaces: int = ...
    kCullNone: int = ...
    kDefaultMaterial: int = ...
    kExcludeAll: int = ...
    kExcludeCVs: int = ...
    kExcludeCameras: int = ...
    kExcludeDeformers: int = ...
    kExcludeDimensions: int = ...
    kExcludeDynamicConstraints: int = ...
    kExcludeDynamics: int = ...
    kExcludeFluids: int = ...
    kExcludeFollicles: int = ...
    kExcludeGrid: int = ...
    kExcludeHairSystems: int = ...
    kExcludeHoldOuts: int = ...
    kExcludeHulls: int = ...
    kExcludeIkHandles: int = ...
    kExcludeImagePlane: int = ...
    kExcludeJoints: int = ...
    kExcludeLights: int = ...
    kExcludeLocators: int = ...
    kExcludeManipulators: int = ...
    kExcludeMeshes: int = ...
    kExcludeMotionTrails: int = ...
    kExcludeNCloths: int = ...
    kExcludeNParticles: int = ...
    kExcludeNRigids: int = ...
    kExcludeNone: int = ...
    kExcludeNurbsCurves: int = ...
    kExcludeNurbsSurfaces: int = ...
    kExcludeParticleInstancers: int = ...
    kExcludePivots: int = ...
    kExcludePlanes: int = ...
    kExcludeSelectHandles: int = ...
    kExcludeStrokes: int = ...
    kExcludeSubdivSurfaces: int = ...
    kExcludeTextures: int = ...
    kFlatShaded: int = ...
    kHUDRender: int = ...
    kLightDefault: int = ...
    kNoCullingOverride: int = ...
    kNoDisplayModeOverride: int = ...
    kNoLight: int = ...
    kNoLightingModeOverride: int = ...
    kNoSceneFilterOverride: int = ...
    kPostEffectDisableAll: int = ...
    kPostEffectDisableDOF: int = ...
    kPostEffectDisableMotionBlur: int = ...
    kPostEffectDisableNone: int = ...
    kPostEffectDisableSSAO: int = ...
    kPresentTarget: int = ...
    kQuadRender: int = ...
    kRenderAllItems: int = ...
    kRenderNonShadedItems: int = ...
    kRenderOpaqueShadedItems: int = ...
    kRenderPostSceneUIItems: int = ...
    kRenderPreSceneUIItems: int = ...
    kRenderShadedItems: int = ...
    kRenderTransparentShadedItems: int = ...
    kRenderUIItems: int = ...
    kSceneLights: int = ...
    kSceneRender: int = ...
    kSelectedLights: int = ...
    kShadeActiveOnly: int = ...
    kShaded: int = ...
    kTextured: int = ...
    kUserDefined: int = ...
    kWireFrame: int = ...
    def lightModeOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """lightModeOverride() -> int

        Query for any lighting mode override.

          MSceneRender.kNoLightingModeOverride  No lighting mode override
          MSceneRender.kNoLight                 Use no light
          MSceneRender.kAmbientLight            Use global ambient light
          MSceneRender.kLightDefault            Use default light
          MSceneRender.kSelectedLights          Use lights which are selected
          MSceneRender.kSceneLights             Use all lights in the scene
        """
        ...
    @property
    def mClearOperation(*args: Any, **kwargs: Any) -> Any:
        """Default clear operation object."""
        ...
    @mClearOperation.setter
    def mClearOperation(*args: Any, **kwargs: Any) -> Any:
        """Default clear operation object."""
        ...
    def name(self: Self, *args: Any, **kwargs: Any) -> Any:
        """name() -> string

        Returns the name of the render operator.
        """
        ...
    def objectSetOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """objectSetOverride() -> MSelectionList

        Query for override for the set of objects to view.

        Visibility takes into account the current states of each object, any displayfilters, and camera frustum culling.

        Note that the override only applies to rendering but not selection.

        By default NULL is returned which indicates that no override is present.
        """
        ...
    def objectTypeExclusions(self: Self, *args: Any, **kwargs: Any) -> Any:
        """objectTypeExclusions() -> int

        Query for any object type exclusions.
        Refer to the MObjectTypeExclusions enumeration on MSceneRender for possible values

        This method is deprecated. Use getObjectTypeExclusions instead.
        """
        ...
    def operationType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """operationType() -> int

        Returns the type of a render operator.
        """
        ...
    def postEffectsOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """postEffectsOverride() -> int

        Query for post effects override.

          MSceneRender.kPostEffectDisableNone        Use current render settings options
          MSceneRender.kPostEffectDisableSSAO        Disable SSAO post effect
          MSceneRender.kPostEffectDisableMotionBlur  Disable motion blur post effect
          MSceneRender.kPostEffectDisableDOF         Disable depth-of-field post effect
          MSceneRender.kPostEffectDisableAll         Disable all post effects
        """
        ...
    def postRender(self: Self, *args: Any, **kwargs: Any) -> Any:
        """postRender() -> self

        Method to allow for the operation to clean up itself after being executed.

        By default this method performs no action
        """
        ...
    def postSceneRender(self: Self, *args: Any, **kwargs: Any) -> Any:
        """postSceneRender(context) -> self

        Method to allow for the operation to update itself after a scene rendering ends.

        This method will be called after computing shadow maps, and after a color pass.

        * context (MDrawContext) - Draw context after rendering has completed

        By default this method performs no action
        """
        ...
    def preRender(self: Self, *args: Any, **kwargs: Any) -> Any:
        """preRender() -> self

        Method to allow for the operation to update itself before being executed. In general this would be used to update any operation parameters.


        No context information is available at this point.

        By default this method performs no action
        """
        ...
    def preSceneRender(self: Self, *args: Any, **kwargs: Any) -> Any:
        """preSceneRender(context) -> self

        Method to allow for the operation to update itself before a scene rendering begins.

        This method will be called before computing shadow maps, and before a color pass.

        * context (MDrawContext) - Draw context before rendering begins

        By default this method performs no action
        """
        ...
    def renderFilterOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """renderFilterOverride() -> int

        Query which elements of a scene render will be drawn based on semantic meaning.

          MSceneRender.kNoSceneFilterOverride
          MSceneRender.kRenderPreSceneUIItems		  Render UI items before scene render like grid or user added pre-scene UI items
          MSceneRender.kRenderOpaqueShadedItems		  Render only opaque shaded objects but not their wireframe or components
          MSceneRender.kRenderTransparentShadedItems	  Render only transparent shaded objects but not their wireframe or components
          MSceneRender.kRenderShadedItems			  Render only shaded (opaque and transparent) objects but not their wireframe or components
          MSceneRender.kRenderPostSceneUIItems		  Render UI items after scene render like wireframe and components for surfaces as well as non-surface objects.
          MSceneRender.kRenderUIItems				  kRenderPreSceneUIItems | kRenderPostSceneUIItems
          MSceneRender.kRenderAllItems				  Render all items.
        """
        ...
    def shaderOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """shaderOverride() -> MShaderInstance

        Query for a scene level shader override.
        """
        ...
    def shadowEnableOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """shadowEnableOverride() -> bool/None

        Query for shadow display override.
        By default a None value is returned indicating that no override is specified.
        """
        ...
    def targetOverrideList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """targetOverrideList() -> list of MRenderTarget

        Return a list of render target which will be used as the target overrides for the operation.
        """
        ...
    def viewportRectangleOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """viewportRectangleOverride() -> MFloatPoint

        Query for a viewport rectangle override.
        """
        ...

class MSelectionContext(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    kComponent: int = ...
    kEdge: int = ...
    kFace: int = ...
    kNone: int = ...
    kObject: int = ...
    kVertex: int = ...
    @property
    def selectionLevel(*args: Any, **kwargs: Any) -> Any:
        """The selection level used to pick items.
          kNone        No selection available.
          kObject      Object level.
                       Objects are selected as a whole. Components are not directly accessible.
          kComponent   Component level.
                       Components such as vertices, edges and faces are selectable. Selection
                       level of each individual MIntersection object is determined by primitive
                       type of the render item.
          kFace        Face level.
          kEdge        Edge level.
          kVertex      Vertex level.
        """
        ...
    @selectionLevel.setter
    def selectionLevel(*args: Any, **kwargs: Any) -> Any:
        """The selection level used to pick items.
          kNone        No selection available.
          kObject      Object level.
                       Objects are selected as a whole. Components are not directly accessible.
          kComponent   Component level.
                       Components such as vertices, edges and faces are selectable. Selection
                       level of each individual MIntersection object is determined by primitive
                       type of the render item.
          kFace        Face level.
          kEdge        Edge level.
          kVertex      Vertex level.
        """
        ...

class MSelectionInfo(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    @property
    def alignmentMatrix(*args: Any, **kwargs: Any) -> Any:
        """The alignment matrix.
        This is used to find ray object intersection.
        """
        ...
    @alignmentMatrix.setter
    def alignmentMatrix(*args: Any, **kwargs: Any) -> Any:
        """The alignment matrix.
        This is used to find ray object intersection.
        """
        ...
    @property
    def cursorPoint(*args: Any, **kwargs: Any) -> Any:
        """The cursor point (x, y) relative to the lower left corner of the viewport."""
        ...
    @cursorPoint.setter
    def cursorPoint(*args: Any, **kwargs: Any) -> Any:
        """The cursor point (x, y) relative to the lower left corner of the viewport."""
        ...
    @property
    def isRay(*args: Any, **kwargs: Any) -> Any:
        """Whether or not there is a selection ray.
        This is used to find ray object intersection
        """
        ...
    @isRay.setter
    def isRay(*args: Any, **kwargs: Any) -> Any:
        """Whether or not there is a selection ray.
        This is used to find ray object intersection
        """
        ...
    @property
    def isSingleSelection(*args: Any, **kwargs: Any) -> Any:
        """Whether or not we want to select a single shape or component."""
        ...
    @isSingleSelection.setter
    def isSingleSelection(*args: Any, **kwargs: Any) -> Any:
        """Whether or not we want to select a single shape or component."""
        ...
    @property
    def localRay(*args: Any, **kwargs: Any) -> Any:
        """The selection ray (starting point and direction).
        This is used to find ray object intersection
        """
        ...
    @localRay.setter
    def localRay(*args: Any, **kwargs: Any) -> Any:
        """The selection ray (starting point and direction).
        This is used to find ray object intersection
        """
        ...
    @property
    def pointSnapping(*args: Any, **kwargs: Any) -> Any:
        """Whether or not selection is launched to find snap points."""
        ...
    @pointSnapping.setter
    def pointSnapping(*args: Any, **kwargs: Any) -> Any:
        """Whether or not selection is launched to find snap points."""
        ...
    @property
    def selectClosest(*args: Any, **kwargs: Any) -> Any:
        """Whether or not we want to select the closest shape or component."""
        ...
    @selectClosest.setter
    def selectClosest(*args: Any, **kwargs: Any) -> Any:
        """Whether or not we want to select the closest shape or component."""
        ...
    def selectForHilite(self: Self, *args: Any, **kwargs: Any) -> Any:
        """selectForHilite(mask) -> bool

        Given the selection mask, determines if this shape can be selected for the hilite list.

        * mask (MSelectionMask) - The mask to test.
        """
        ...
    @property
    def selectOnHilitedOnly(*args: Any, **kwargs: Any) -> Any:
        """Whether or not the components can only be selected if the shape is hilited."""
        ...
    @selectOnHilitedOnly.setter
    def selectOnHilitedOnly(*args: Any, **kwargs: Any) -> Any:
        """Whether or not the components can only be selected if the shape is hilited."""
        ...
    @property
    def selectRect(*args: Any, **kwargs: Any) -> Any:
        """The current selection rectangle dimensions (x, y, width, height)."""
        ...
    @selectRect.setter
    def selectRect(*args: Any, **kwargs: Any) -> Any:
        """The current selection rectangle dimensions (x, y, width, height)."""
        ...
    def selectable(self: Self, *args: Any, **kwargs: Any) -> Any:
        """selectable(mask) -> bool

        Given the selection mask, determines if the shape is selectable.

        * mask (MSelectionMask) - The mask to test.
        """
        ...
    def selectableComponent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """selectableComponent(displayed, mask) -> bool

        Given the selection mask, determines if the component is selectable.

        * displayed (bool) - Is the component displayed.
        * mask (MSelectionMask) - The mask to test.
        """
        ...

class MShaderCompileMacro(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    @property
    def definition(*args: Any, **kwargs: Any) -> Any:
        """Macro definition"""
        ...
    @definition.setter
    def definition(*args: Any, **kwargs: Any) -> Any:
        """Macro definition"""
        ...
    @property
    def name(*args: Any, **kwargs: Any) -> Any:
        """Name of the macro"""
        ...
    @name.setter
    def name(*args: Any, **kwargs: Any) -> Any:
        """Name of the macro"""
        ...

class MShaderInstance(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def activatePass(self: Self, *args: Any, **kwargs: Any) -> Any:
        """activatePass(MDrawContext, int) -> self
        Activates the given pass of the shader.
        Must be called between calls to bind() and unbind().
        """
        ...
    def addInputFragment(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addInputFragment(fragmentName, outputName, inputName, promotedInputName=None) -> self

        Connect a fragment that has been registered with the fragment manager to an input on the existing MShaderInstance.
        Use this method to add shader instructions to an existing MShaderInstance.
        The code defined in the fragment will be compiled and executed on the GPU to compute the value for the input parameter.

        * fragmentName (string) - The name of a fragment that has been registered with the MFragmentManager.
        * outputName (string) - The name of the output on the registered fragment to connect to.
        * inputName (string) - The name of the input parameter on the MShaderInstance to connect to.* promotedInputName (string) - The name of the input parameter on the new fragment that will be promoted to replace the input parameter being connected to.
        """
        ...
    def addInputFragmentForMultiParams(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addInputFragmentForMultiParams(fragmentName, uniqueName, outputNames, inputNames, invalidParameterIndices=None, fragmentUsage=MShaderInstance.kPixelShader) -> self

        Connect a named fragment that has been registered with the MFragmentManager 
        to this MShaderInstance. The code defined in the fragment will be included 
        in the new shader and executed on GPU to compute values for input parameters 
        specified by inputNames. 

        To connect with fragments, this MShaderInstance needs to be created from a 
        shader fragment or fragment graph as well. Thus, a shader instance created 
        from a file-based effect cannot connect with any fragments. 

        After the fragment is connected, all input parameters with the same name in 
        the new fragment graph are mapped to a single parameter in the shader by 
        default. If uniqueness is required for input parameters on the fragment, 
        uniqueName can be used to prefix names of the input parameters. 

        This method is particularly useful when plugin needs to make multiple 
        connections from the input fragment to this MShaderInstance. It can be used 
        to make a single connection, but addInputFragment() is more convenient in 
        this case. The numbers of the output and input parameters must match. An 
        output and an input parameter with the same index in the two string arrays 
        will be connected. To specify fan-out connections, the same output name can 
        be repeated in outputNames as need. Fan-in connections are not allowed. 

        If the numbers of the output and input parameters don't match, or a 
        parameter (either output or input) doesn't exist, or their types don't 
        match, the relevant parameters will not be connected and the method will 
        return MStatus::kInvalidParameter. In this case, the fragment may still be 
        connected partially to this MShaderInstance through other connectable 
        parameter pairs, and plugin can use invalidParameterIndices to query 
        indices of those invalid parameters in outputNames and inputNames. 

        * fragmentName (string) - Name of the input fragment.
        * uniqueName (string) - A unique name to prefix names of input parameters on the input fragment.
        * outputNames (list of strings) - Names of the output parameters on the input fragment to connect from.
        * inputNames (list of strings) - Names of the input parameters on the MShaderInstance to connect to.
        * invalidParameterIndices (list of ints) - Optional list to query indices of invalid parameters.
        * fragmentUsage (int) - Not implemented.
        """
        ...
    def addOutputFragment(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addOutputFragment(fragmentName, inputName) -> self

        Connect a fragment that has been registered with the fragment manager to an output on the existing MShaderInstance.
        The code defined in the fragment will be compiled and executed on the GPU to modify the value returned by the original shader.
        For example, use this method to add additional alpha or conditionals to the output color.

        * fragmentName (string) - The name of a fragment that has been registered with the MFragmentManager.
        * inputName (string) - The name of the input parameter on the fragment to connect the shaders output to.
        """
        ...
    def annotation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """annotation(parameterName, annotationName) -> int / float / string

        Returns the value of a named parameter annotation.

         * parameterName (string) - The name of the parameter.
         * annotationName (string) - The name of the annotation.
        """
        ...
    def bind(self: Self, *args: Any, **kwargs: Any) -> Any:
        """bind(MDrawContext) -> self
        Binds the shader instance to the draw context, so that it is the active shader.
        """
        ...
    def clone(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clone() -> MShaderInstance

        Clone the shader. This will return a new MShaderInstance object which is identical to the existing shader.
        """
        ...
    def createShaderInstanceWithColorManagementFragment(self: Self, *args: Any, **kwargs: Any) -> Any:
        """createShaderInstanceWithColorManagementFragment(inputColorSpace) -> MShaderInstance

        Return a new shader instance with Color Management fragment added, which is based on the callee.
        The callee shader instance is the one used for rendering a render item with image(a MPxNode with image, etc.)
        The new shader is completely independent of the original shader. 
        Setting parameter values on either shader after calling this function will have no effect on the other.
        The function won't keep a copy of input parameter.


        When the returned new shader instance is no longer needed, MShaderManager.releaseShader() 
        should be called to notify the shader manager that the caller is done with the shader.

         * inputColorSpace (string) - The color space the current image is in
        """
        ...
    def getArraySize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getArraySize(string) -> int

        Return the size of an array if it is an array. Returns 0 if it is not an array
        """
        ...
    def getPassCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPassCount(MDrawContext) -> int
        Returns the number of draw passes defined by the shader.
        None if the shader instance or draw context was invalid.
        """
        ...
    def isArrayParameter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isArrayParameter(string) -> bool

        Determine whether the named parameter is an array.
        """
        ...
    def isTransparent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isTransparent() -> bool

        Return whether the shader will render with transparency.
        """
        ...
    def isVaryingParameter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isVaryingParameter(string) -> bool

        Return the true if a named parameter's values vary per vertex.
        """
        ...
    kAnisotropyShader: int = ...
    kAnisotropyShader2: int = ...
    kBoolean: int = ...
    kDisplacementPosShader: int = ...
    kFloat: int = ...
    kFloat2: int = ...
    kFloat3: int = ...
    kFloat4: int = ...
    kFloat4x4Col: int = ...
    kFloat4x4Row: int = ...
    kGeometryShader: int = ...
    kGlossShader: int = ...
    kGlossShader2: int = ...
    kInteger: int = ...
    kInvalid: int = ...
    kNormalShader: int = ...
    kNormalShader2: int = ...
    kPixelShader: int = ...
    kReflectanceShader: int = ...
    kReflectanceShader2: int = ...
    kRotationAngleShader: int = ...
    kRotationAngleShader2: int = ...
    kRoughnessShader: int = ...
    kRoughnessShader2: int = ...
    kSampler: int = ...
    kTexture1: int = ...
    kTexture2: int = ...
    kTexture3: int = ...
    kTextureCube: int = ...
    kVertexShader: int = ...
    def parameterDefaultValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """parameterDefaultValue(parameterName) -> bool / int / float / tuple of float

        Returns the default value of named parameter, None if no default value.
        """
        ...
    def parameterList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """parameterList() -> list of string

        Get the names of all parameters that are settable on this shader instance.
        """
        ...
    def parameterSemantic(self: Self, *args: Any, **kwargs: Any) -> Any:
        """parameterSemantic(parameterName) -> string

        Returns the semantic associated to a named parameter.
        """
        ...
    def parameterType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """parameterType(string) -> int

        Get the type of the named parameter, returns kInvalid if parameter is not found.
        """
        ...
    def passAnnotation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """passAnnotation(pass, annotationName) -> int / float / string

        Returns the value of the current technique's pass annotation.

         * pass (int) - The index of the pass.
         * annotationName (string) - The name of the pass annotation.
        """
        ...
    def postDrawCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """postDrawCallback() -> function/None

        Returns the post-draw callback function set for the this shader instance.
        Returns None if the callback function is not set or is not a python function.
        """
        ...
    def preDrawCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """preDrawCallback() -> function/None

        Returns the pre-draw callback function set for the this shader instance.
        Returns None if the callback function is not set or is not a python function.
        """
        ...
    def renameParameter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """renameParameter(parameterName, string) -> self

        Rename a named parameter.
        """
        ...
    def requiredVertexBuffers(self: Self, *args: Any, **kwargs: Any) -> Any:
        """requiredVertexBuffers(MVertexBufferDescriptorList) -> self
        Get the vertex buffer descriptors that describe the buffers required
        by a given shader instance.
        """
        ...
    def resourceName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """resourceName(parameterName) -> string

        Returns the resource name of a named texture parameter.
        The resource name of a texture parameter can be specified in the effect file using the 'ResourceName' annotation.
        It allows users to define a default texture using an external file.
        If no resource was defined for a texture, this function returns an empty string.
        """
        ...
    def semantic(self: Self, *args: Any, **kwargs: Any) -> Any:
        """semantic(string) -> string

        Return the semantic for a named parameter.
        """
        ...
    def setArrayParameter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setArrayParameter(parameterName, sequence of bool, int) -> self
        setArrayParameter(parameterName, sequence of int, int) -> self
        setArrayParameter(parameterName, sequence of float, int) -> self
        setArrayParameter(parameterName, sequence of MMatrix, int) -> self

        Set the value of a named array parameter.
        """
        ...
    def setAsVarying(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setAsVarying(parameterName, bool) -> self

        Set whether the named parameter's values will vary per vertex.
        """
        ...
    def setIsTransparent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setIsTransparent(bool) -> self

        Set whether the shader will render with transparency.
        """
        ...
    def setParameter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setParameter(parameterName, bool) -> self
        setParameter(parameterName, int) -> self
        setParameter(parameterName, float) -> self
        setParameter(parameterName, list of float) -> self
        setParameter(parameterName, MFloatVector) -> self
        setParameter(parameterName, MMatrix) -> self
        setParameter(parameterName, MFloatMatrix) -> self
        setParameter(parameterName, MTexture) -> self
        setParameter(parameterName, MRenderTarget) -> self
        setParameter(parameterName, MSamplerState) -> self

        Set the value of the named parameter.
        """
        ...
    def setSemantic(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setSemantic(parameterName, string) -> self

        Set the semantic of a named parameter.
        """
        ...
    def techniqueAnnotation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """techniqueAnnotation(annotationName) -> int / float / string

        Returns the value of the current technique annotation.

         * annotationName (string) - The name of the technique annotation.
        """
        ...
    def techniqueNames(self: Self, *args: Any, **kwargs: Any) -> Any:
        """techniqueNames() -> list of strings

        Returns a list of the technique names for the effect.
        """
        ...
    def uiName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """uiName(parameterName) -> string

        Returns the UI name associated with a named parameter.
        The UI name can be specified in shader using the 'UIName' annotation.
        The UI name can be used to specify the name that will be displayed in the Attribute Editor.
        """
        ...
    def uiWidget(self: Self, *args: Any, **kwargs: Any) -> Any:
        """uiWidget(parameterName) -> string

        Returns the UI widget type associated with a named parameter.
        The UI widget type can be specified in shader using the 'UIWidget' annotation.The UI widget can be used to specify which widget should be used to control the parameter in the Attribute Editor.
        """
        ...
    def unbind(self: Self, *args: Any, **kwargs: Any) -> Any:
        """unbind(MDrawContext) -> self
        Unbinds the shader instance from the draw context.
        """
        ...
    def updateParameters(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateParameters(MDrawContext) -> self
        Updates the bound shader instance with the current parameter data.
        """
        ...
    def writeEffectSourceToFile(self: Self, *args: Any, **kwargs: Any) -> Any:
        """writeEffectSourceToFile(filePath) -> self
        Write the source of the final OGSFX/HLSL/CgFX effect to a specified file. Use
        this for debugging to see how fragments are turned into the final effect for
        the current drawing API.

        Note that the effect will not be written if the effect is not generated from
        shader fragments or any of the shader fragments is marked as hidden.
        """
        ...

class MShaderManager(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def addShaderIncludePath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addShaderIncludePath(string) -> self

        Add a path to the list of paths used for searching for shader include files.
        """
        ...
    def addShaderPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addShaderPath(string) -> self

        Add a path to the list of shader search paths.
        """
        ...
    def clearEffectCache(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clearEffectCache() -> self
        Clear the effect cache.
        This will allow all relevant effects to be updated when the implementation of a shader fragment or fragment graph has been modified.
        """
        ...
    def getEffectsBufferShader(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getEffectsBufferShader(buffer, size, techniqueName, macros=None, useEffectCache=True, preCb=None, postCb=None) -> MShaderInstance

        Get a new instance of a shader generated from a block of memory containing device-specific source code (as char*).

        * buffer (const void*) - A pointer to the block of memory from which to load the effect.
        * size (unsigned int) - The size of the effect to load in bytes.
        * techniqueName (string) - The name of a technique in the effect. If an empty string is specified then the first technique in the effect will be used.
        * macros (sequence of MShaderCompileMacro) - Sequence of shader macros. The default value is None, meaning that no macros are specified.
        * useEffectCache (bool) - Use the internal effect cache to prevent reloading the effect every time it is requested. The default value is True.
        * preCb (function) - A function, or other Python callable, to be called before render items are drawn with this shader.
        * postCb (function) - A function, or other Python callable, to be called after render items are drawn with this shader.
              see MShaderManager.getEffectsFileShader() for details on the preCb and postCb functions
        """
        ...
    def getEffectsFileShader(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getEffectsFileShader(effecsFileName, techniqueName, macros=None, useEffectCache=True, preCb=None, postCb=None) -> MShaderInstance

        Get a new instance of a shader generated from an effects file stored on disk.

        * effectsFileName (string) - The effects file.
        * techniqueName (string) - The name of a technique in the effects file. If an empty string is specified then the first technique in the effects file will be used.
        * macros (sequence of MShaderCompileMacro) - Sequence of shader macros. The default value is None, meaning that no macros are specified.
        * useEffectCache (bool) - Use the internal effect cache to prevent reloading the effect file every time it is requested. The default value is True.
        * preCb (function) - A function, or other Python callable, to be called before render items are drawn with this shader.
                  def preCb(MDrawContext, MRenderItemList, MShaderInstance)
        * postCb (function) - A function, or other Python callable, to be called after render items are drawn with this shader.
                  def postCb(MDrawContext, MRenderItemList, MShaderInstance)
        """
        ...
    def getEffectsTechniques(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getEffectsTechniques(effecsFileName, macros=None, useEffectCache=True) -> tuple of strings

        Analyzes a given effect file to extract the names of the techniques that are defined.

        * effectsFileName (string) - The effects file.
        * macros (sequence of MShaderCompileMacro) - Sequence of shader macros. The default value is None, meaning that no macros are specified.
        * useEffectCache (bool) - Use the internal effect cache to prevent reloading the effect every time it is requested. The default value is True.
        """
        ...
    def getFragmentShader(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFragmentShader(fragmentName, structOutputName, decorateFragment, preCb=None, postCb=None) -> MShaderInstance

        Get a new instance of a shader generated from a named shader fragment or fragment graph.

        * fragmentName (string) - The name of the fragment to generate a shader from.
        * structOutputName (string) - If the output of the fragment is a struct, use this parameter to specify which member of the struct to use.
        								 This parameter is ignored if the output of the fragment is not a struct.
        * decorateFragment (bool) - If True, Maya state fragments will be added.
        * preCb (function) - A function, or other Python callable, to be called before render items are drawn with this shader.
        * postCb (function) - A function, or other Python callable, to be called after render items are drawn with this shader.
              see MShaderManager.getEffectsFileShader() for details on the preCb and postCb functions
        """
        ...
    def getLastError(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getLastError() -> string

        Get the description of the last error encountered by the shader manager regarding an effect.
        This includes fragment and effect loading, technique query, and shader binding.
        """
        ...
    def getLastErrorSource(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getLastErrorSource(displayLineNumber=False, filterSource=False, numSurroundingLines=2) -> string

        Get the source of the shader that generated the last error. See getLastError().
         * displayLineNumber (bool) - If True, add the number line at the beginning of each line. The default is False.
         * filterSource (bool) - If True, only display the lines surrounding the error(s). The default is False.
         * numSurroundingLines (int) - The number of leading and trailing lines to display around filtered source. The default is 2.
        """
        ...
    def getShaderFromNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getShaderFromNode(shaderNode, shapePath, linkLostCb=None, linkLostUserData=None, preCb=None, postCb=None, nonTextured=False) -> MShaderInstance

        Get the shader instance by evaluating the shading network of a surface shader node (either standard or custom) in the scene.

        If the surface shader node is NULL or supported by neither Maya nor the plug-in, this method will return NULL.

        The shape path is used as the object context for shading network evaluation to ensure that the shader instance fits its requirements. If the shape path is invalid (e.g. an empty path), a shader instance to fit basic requirements is created but will not include any geometry-dependent requirements.

        The linkLostCb will be invoked whenever the link to the surface shader node is lost. The link can be lost in a number of ways, e.g. shader nodes are deleted or shading network connections are modified. However, the linkLostCb will not be invoked for changes to a shading group; if needed, it is the plug-in's responsibility to monitor any changes to the shading group (via MNodeMessage and/or MPxNode::connectionMade/connectionBroken).

        After the shader instance is created, its parameter values can be automatically updated by Viewport 2.0 whenever the related shading attributes are changed, thus no attempt should be made to override parameter values of the shader instance manually.

        * shaderNode (MObject) - The surface shader node.
        * shapePath (MDagPath) - The DAG path of a shape to be used as the object context for shading network evaluation.
        * linkLostCb (function) - A function, or other Python callable, to be called when this shader instance is no longer connected to the node it was translated for.
                  def linkLostCb(MShaderInstance, MUserData)
        * linkLostUserData (MUserData) - User supplied data to be passed into the link lost callback.
               This data will not be deleted internally and the lifetime must be managed by the caller.
               The link lost callback will only be called once so it is safe to delete this data anytime after the callback has been triggered.
        * preCb (function) - A function, or other Python callable, to be called before render items are drawn with this shader.
        * postCb (function) - A function, or other Python callable, to be called after render items are drawn with this shader.
              see MShaderManager.getEffectsFileShader() for details on the preCb and postCb functions.
        * nonTextured (bool) - Whether or not a non-textured effect instance is needed. The default value is false.
        """
        ...
    def getStockShader(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getStockShader(shaderId, preCb=None, postCb=None) -> MShaderInstance

        Get a new instance of a stock shader.

        * shaderId (int) - The Id of stock shader.
        * preCb (function) - A function, or other Python callable, to be called before render items are drawn with this shader.
        * postCb (function) - A function, or other Python callable, to be called after render items are drawn with this shader.
              see MShaderManager.getEffectsFileShader() for details on the preCb and postCb functions

        List of available stock shader:
          k3dSolidShader                  An instance of a solid color shader for 3d rendering
          k3dBlinnShader                  An instance of a Blinn shader for 3d rendering
          k3dDefaultMaterialShader        An instance of a stock "default material" shader for 3d rendering
          k3dSolidTextureShader           An instance of a stock solid texture shader for 3d rendering
          k3dCPVFatPointShader            An instance of a stock color per vertex fat point shader for 3d rendering
          k3dColorLookupFatPointShader    An instance of a stock fat point shader using a 1D color texture lookup.
          k3dShadowerShader               An instance of a stock shader which can be used when rendering shadow maps
          k3dFatPointShader               An instance of a stock fat point shader for 3d rendering
          k3dThickLineShader              An instance of a stock thick line shader for 3d rendering
          k3dCPVThickLineShader           An instance of a color per vertex stock thick line shader for 3d rendering
          k3dDashLineShader               An instance of a stock dash line shader for 3d rendering
          k3dCPVDashLineShader            An instance of a color per vertex stock dash line shader for 3d rendering
          k3dStippleShader                An instance of a stipple shader for drawing 3d filled triangles
          k3dThickDashLineShader          An instance of a stock thick dash line shader for 3d rendering.
          k3dCPVThickDashLineShader       An instance of a color per vertex stock thick dash line shader for 3d rendering.
          k3dDepthShader                  An instance of a stock shader that can be used for 3d rendering of depth
          k3dCPVSolidShader               An instance of a stock solid color per vertex shader for 3d rendering
          k3dIntegerNumericShader         An instance of a stock shader for drawing single integer values per vertex for 3d rendering.
          k3dFloatNumericShader           An instance of a stock shader for drawing single float values values per vertex for 3d rendering.
          k3dFloat2NumericShader          An instance of a stock shader for drawing 2 float values per vertex for 3d rendering.
          k3dFloat3NumericShader          An instance of a stock shader for drawing 3 float values per vertex for 3d rendering.
          k3dPointVectorShader            An instance of a stock shader that can be used for 3d rendering of lines based on a point and a vector stream
        """
        ...
    def isSupportedShaderSemantic(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isSupportedShaderSemantic(string) -> bool
        Return if a given string is a supported shader semantic.
        """
        ...
    k3dBlinnShader: int = ...
    k3dCPVDashLineShader: int = ...
    k3dCPVFatPointShader: int = ...
    k3dCPVShader: int = ...
    k3dCPVSolidShader: int = ...
    k3dCPVThickDashLineShader: int = ...
    k3dCPVThickLineShader: int = ...
    k3dColorLookupFatPointShader: int = ...
    k3dColorOpacityLookupFatPointShader: int = ...
    k3dDashLineShader: int = ...
    k3dDefaultMaterialShader: int = ...
    k3dDepthShader: int = ...
    k3dFatPointShader: int = ...
    k3dFloat2NumericShader: int = ...
    k3dFloat3NumericShader: int = ...
    k3dFloatNumericShader: int = ...
    k3dIntegerNumericShader: int = ...
    k3dIsotropicStandardSurfaceShader: int = ...
    k3dOpacityLookupFatPointShader: int = ...
    k3dPointLightShadowerShader: int = ...
    k3dPointVectorShader: int = ...
    k3dShadowerShader: int = ...
    k3dSolidShader: int = ...
    k3dSolidTextureShader: int = ...
    k3dStandardSurfaceShader: int = ...
    k3dStippleShader: int = ...
    k3dThickDashLineShader: int = ...
    k3dThickLineShader: int = ...
    def releaseShader(self: Self, *args: Any, **kwargs: Any) -> Any:
        """releaseShader(MShaderInstance) -> None
        Deletes the MShaderInstance and releases its reference to the underlying shader which is held by the MShaderInstance object.
        """
        ...
    def removeEffectFromCache(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeEffectFromCache(effecsFileName, techniqueName, macros=None) -> self
        Remove an effect from the cache.
        This is particulary useful when calling the getEffectsTechniques() and/or getEffectsFileShader() with the flag useEffectCache set to True for maximum performance, and will allow reloading the effect from the disk when the shader file has been modified.
        * effectsFileName (string) - The effects file.
        * techniqueName (string) - The name of a technique in the effects file. If an empty string is specified then the first technique in the effects file will be used.
        * macros (sequence of MShaderCompileMacro) - Sequence of shader macros. The default value is None, meaning that no macros are specified.
        """
        ...
    def shaderIncludePaths(self: Self, *args: Any, **kwargs: Any) -> Any:
        """shaderIncludePaths() -> list of strings

        Query the list of search paths user for searching for shader include files.
        """
        ...
    def shaderPaths(self: Self, *args: Any, **kwargs: Any) -> Any:
        """shaderPaths() -> list of strings

        Query the list of shader search paths.
        """
        ...

class MStateManager(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def acquireBlendState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """acquireBlendState(MBlendStateDesc) -> MBlendState

        Acquires an immutable unique blend state matching the blend state descriptor.
        """
        ...
    def acquireDepthStencilState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """acquireDepthStencilState(MDepthStencilStateDesc) -> MDepthStencilState

        Acquires an immutable unique depth-stencil state matching the blend state descriptor.
        """
        ...
    def acquireRasterizerState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """acquireRasterizerState(MRasterizerStateDesc) -> MRasterizerState

        Acquires an immutable unique rasterizer state matching the rasterizer state descriptor.
        """
        ...
    def acquireSamplerState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """acquireSamplerState(MSamplerStateDesc) -> MSamplerState

        Acquires an immutable unique sampler state matching the blend state descriptor.
        """
        ...
    def getBlendState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getBlendState() -> MBlendState

        Gets the current active blend state from the device.
        """
        ...
    def getDepthStencilState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getDepthStencilState() -> MDepthStencilState

        Gets the current depth-stencil blend state from the device.
        """
        ...
    def getMaxSamplerCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getMaxSamplerCount() -> int

        Get the maximum number of simulataneous texture coordinate interpolation channels.
        """
        ...
    def getRasterizerState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getRasterizerState() -> MRasterizerState

        Gets the current active rasterizer state from the device.
        """
        ...
    def getSamplerState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getSamplerState(shader, samplerIndex) -> MSamplerState

        Gets the current active sampler state from the device.
        * shader (ShaderType) - The shader this sampler will apply to.
        * samplerIndex (int) - The index of the sampler to set with the given shader state.
        """
        ...
    kCompareAlways: int = ...
    kCompareEqual: int = ...
    kCompareGreater: int = ...
    kCompareGreaterEqual: int = ...
    kCompareLess: int = ...
    kCompareLessEqual: int = ...
    kCompareNever: int = ...
    kCompareNotEqual: int = ...
    kDomainShader: int = ...
    kGeometryShader: int = ...
    kHullShader: int = ...
    kNoShader: int = ...
    kPixelShader: int = ...
    kVertexShader: int = ...
    def releaseBlendState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """releaseBlendState(MBlendState) -> None

        Deletes the MBlendState and releases the reference to the underlying state object which is held by the MBlendState object.
        """
        ...
    def releaseDepthStencilState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """releaseDepthStencilState(MDepthStencilState) -> None

        Deletes the MDepthStencilState and releases the reference to the underlying state object which is held by the MDepthStencilState object.
        """
        ...
    def releaseRasterizerState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """releaseRasterizerState(MRasterizerState) -> None

        Deletes the MRasterizerState and releases the reference to the underlying state object which is held by the MRasterizerState object.
        """
        ...
    def releaseSamplerState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """releaseSamplerState(MSamplerState) -> None

        Deletes the MSamplerState and releases the reference to the underlying state object which is held by the MSamplerState object.
        """
        ...
    def setBlendState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setBlendState(MBlendState) -> self

        Sets the active blend state on the device.
        """
        ...
    def setDepthStencilState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDepthStencilState(MDepthStencilState) -> self

        Sets the active depth-stencil state on the device.
        """
        ...
    def setRasterizerState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setRasterizerState(MRasterizerState) -> self

        Sets the active rasterizer state on the device.
        """
        ...
    def setSamplerState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setSamplerState(shader, samplerIndex, samplerState) -> self

        Sets the active sampler state for any of the texture samplers on the device.
        * shader (ShaderType) - The shader this sampler will apply to, e.g. kPixelShader.
        * samplerIndex (int) - The index of the sampler to set with the given shader state.
        * samplerState (MSamplerState) - The sampler state container object that was previously acquired.
        """
        ...

class MStencilOpDesc(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def setDefaults(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDefaults() -> self

        Set all values for the stencil operation state to their default values.
        """
        ...
    @property
    def stencilDepthFailOp(*args: Any, **kwargs: Any) -> Any:
        """Stencil op to use when the fragment passes the depth test, default kKeepStencil"""
        ...
    @stencilDepthFailOp.setter
    def stencilDepthFailOp(*args: Any, **kwargs: Any) -> Any:
        """Stencil op to use when the fragment passes the depth test, default kKeepStencil"""
        ...
    @property
    def stencilFailOp(*args: Any, **kwargs: Any) -> Any:
        """Stencil op to use when the fragment fails the stencil test, default kKeepStencil"""
        ...
    @stencilFailOp.setter
    def stencilFailOp(*args: Any, **kwargs: Any) -> Any:
        """Stencil op to use when the fragment fails the stencil test, default kKeepStencil"""
        ...
    @property
    def stencilFunc(*args: Any, **kwargs: Any) -> Any:
        """Sets the stencil buffer comparison function, default kCompareAlways"""
        ...
    @stencilFunc.setter
    def stencilFunc(*args: Any, **kwargs: Any) -> Any:
        """Sets the stencil buffer comparison function, default kCompareAlways"""
        ...
    @property
    def stencilPassOp(*args: Any, **kwargs: Any) -> Any:
        """Stencil op to use when the fragment passes the stencil test, default kKeepStencil"""
        ...
    @stencilPassOp.setter
    def stencilPassOp(*args: Any, **kwargs: Any) -> Any:
        """Stencil op to use when the fragment passes the stencil test, default kKeepStencil"""
        ...

class MSubSceneContainer(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __len__(self: Self) -> Any:
        """Return len(self)."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def add(self: Self, *args: Any, **kwargs: Any) -> Any:
        """add(item) -> bool

        Add a render item to the set of render items that will be used to draw the DAG object associated with the override that owns this container. Each item in the container must have a unique name and the same render item may not be used in the container more than once. When Viewport 2.0 draws the associated DAG object, it will process all render items in this container.
        Any items that have valid geometry and a valid shader will be drawn as long as they pass all filtering tests for the active viewport.

        On successful add, Maya assumes ownership of the render item and the caller should not call MRenderItem.destroy() on the item. Callers are free to hold the render item for easy access. Note that any MRenderItem objects added to MSubSceneContainer become invalid after the render item is removed from the container. Attempts to use such object will result in instability. Further note that it is invalid to modify any render item owned by this container outside of MPxSubSceneOverride.update().
        Attempts to do so will result in unpredictable behavior.

        * item (MRenderItem) - The item to add.
        """
        ...
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clear() -> self

        Remove all render items from this container. After calling, any render items owned by this container will be invalid.
        """
        ...
    def count(self: Self, *args: Any, **kwargs: Any) -> Any:
        """count() -> int

        Get the number of render items in the container.
        """
        ...
    def find(self: Self, *args: Any, **kwargs: Any) -> Any:
        """find(name) -> MRenderItem

        Get a render item by name from the container. The ownership of the render item remains with the container and callers should not call MRenderItem.destroy() on it. The render items may be cached and will remain valid until removed from the container.

        * name (string) - The name of the render item to retrieve.
        """
        ...
    def getIterator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getIterator() -> MSubSceneContainerIterator

        Get an iterator for the container.
        Caller is responsible for deleting the iterator when it is no longer needed.
        """
        ...
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """remove(name) -> bool

        Remove a render item by name from the set of render items used to draw the object associated with the override that owns this container. Note that on successful removal any render item that was removed become invalid and any attempts to use such items will result in instability.

        * name (string) - The name of the render item to remove.
        """
        ...

class MSubSceneContainerIterator(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def destroy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """destroy() -> self

        Call this method to delete the iterator. After calling, the iterator will be invalid.
        Users of MSubSceneContainer iterators are responsible for deleting the iterators after use.
        """
        ...
    def next(self: Self, *args: Any, **kwargs: Any) -> Any:
        """next() -> MRenderItem

        Advance the iterator to the next render item in the associated MSubSceneContainer and return it.

        Returns the next render item in the container or None if no more items.
        """
        ...
    def reset(self: Self, *args: Any, **kwargs: Any) -> Any:
        """reset() -> self

        Reset the iterator to the beginning of the associated MSubSceneContainer.
        The next call to the next() method will return the first render item in the container.
        """
        ...

class MSwatchRenderBase(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def cancelCurrentSwatchRender(self: Self, *args: Any, **kwargs: Any) -> Any:
        """cancelCurrentSwatchRender() -> None

        The method cancels the swatch which is being rendered in parallel, and push the swatch render item back to the render queue after. 

        The render plugins should make sure that MSwatchRenderBase.cancelParallelRendering() is implemented acoordingly.
        """
        ...
    def cancelParallelRendering(self: Self, *args: Any, **kwargs: Any) -> Any:
        """cancelParallelRendering() -> self

        Method to cancel the parallel rendering.
        The derived classes should provide the implementation accordingly if required.
        """
        ...
    def doIteration(self: Self, *args: Any, **kwargs: Any) -> Any:
        """doIteration() -> bool

        Method called from the MSwatchRenderRegister for generation of swatch image. The doIteration function is called repeatedly (during idle events) until it returns true. Using this swatch image can be generated in stages.

        This method should be overridden in derived classes which can compute the swatches in several steps.

        Returns False as long as the swatch computation is not completed.
        """
        ...
    def finishParallelRender(self: Self, *args: Any, **kwargs: Any) -> Any:
        """finishParallelRender() -> self

        Method to update the swatch image when the parallel rendering is finished.
        If swatch is rendered parallel, this method must be called after parallel rendering finished.
        """
        ...
    def image(self: Self, *args: Any, **kwargs: Any) -> Any:
        """image() -> MImage

        This method returns the render swatch as an image.
        """
        ...
    def node(self: Self, *args: Any, **kwargs: Any) -> Any:
        """node() -> MObject

        This method returns the node that is used to compute the swatch.
        """
        ...
    def renderParallel(self: Self, *args: Any, **kwargs: Any) -> Any:
        """renderParallel() -> bool

        Method indicates if the swatch is rendered parallel.
        Default is False.
        """
        ...
    @property
    def renderQuality(*args: Any, **kwargs: Any) -> Any:
        """The quality in which the swatch will be rendered (the larger the number is set, the better quality is applied)."""
        ...
    @renderQuality.setter
    def renderQuality(*args: Any, **kwargs: Any) -> Any:
        """The quality in which the swatch will be rendered (the larger the number is set, the better quality is applied)."""
        ...
    def resolution(self: Self, *args: Any, **kwargs: Any) -> Any:
        """resolution() -> int

        This method returns the expected resolution of the swatch.
        """
        ...
    def swatchNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """swatchNode() -> MObject

        This method returns the node for which the swatch is required to be generated.
        """
        ...

class MTargetBlendDesc(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    @property
    def alphaBlendOperation(*args: Any, **kwargs: Any) -> Any:
        """The blend operation for alpha, default is add"""
        ...
    @alphaBlendOperation.setter
    def alphaBlendOperation(*args: Any, **kwargs: Any) -> Any:
        """The blend operation for alpha, default is add"""
        ...
    @property
    def alphaDestinationBlend(*args: Any, **kwargs: Any) -> Any:
        """The blend factor for the destination alpha, default is zero"""
        ...
    @alphaDestinationBlend.setter
    def alphaDestinationBlend(*args: Any, **kwargs: Any) -> Any:
        """The blend factor for the destination alpha, default is zero"""
        ...
    @property
    def alphaSourceBlend(*args: Any, **kwargs: Any) -> Any:
        """The blend factor for the source alpha, default is one"""
        ...
    @alphaSourceBlend.setter
    def alphaSourceBlend(*args: Any, **kwargs: Any) -> Any:
        """The blend factor for the source alpha, default is one"""
        ...
    @property
    def blendEnable(*args: Any, **kwargs: Any) -> Any:
        """Enable blending on this target, default is False"""
        ...
    @blendEnable.setter
    def blendEnable(*args: Any, **kwargs: Any) -> Any:
        """Enable blending on this target, default is False"""
        ...
    @property
    def blendOperation(*args: Any, **kwargs: Any) -> Any:
        """The blend operation, default is add"""
        ...
    @blendOperation.setter
    def blendOperation(*args: Any, **kwargs: Any) -> Any:
        """The blend operation, default is add"""
        ...
    @property
    def destinationBlend(*args: Any, **kwargs: Any) -> Any:
        """The blend factor for the destination color, default is zero"""
        ...
    @destinationBlend.setter
    def destinationBlend(*args: Any, **kwargs: Any) -> Any:
        """The blend factor for the destination color, default is zero"""
        ...
    def setDefaults(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDefaults() -> self

        Set all values for the target blend state to their default values.
        """
        ...
    @property
    def sourceBlend(*args: Any, **kwargs: Any) -> Any:
        """The blend factor for the source color, default is one"""
        ...
    @sourceBlend.setter
    def sourceBlend(*args: Any, **kwargs: Any) -> Any:
        """The blend factor for the source color, default is one"""
        ...
    @property
    def targetWriteMask(*args: Any, **kwargs: Any) -> Any:
        """Indicates what color components(red, green, blue, alpha) are writable, the default is RGBA"""
        ...
    @targetWriteMask.setter
    def targetWriteMask(*args: Any, **kwargs: Any) -> Any:
        """Indicates what color components(red, green, blue, alpha) are writable, the default is RGBA"""
        ...

class MTexture(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def bytesPerPixel(self: Self, *args: Any, **kwargs: Any) -> Any:
        """bytesPerPixel() -> int

        Get the number of bytes per pixel in the texture.
        """
        ...
    def freeRawData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """freeRawData(long) -> None
        Deallocate system memory - retrieved from rawData().
        """
        ...
    def hasAlpha(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasAlpha() -> bool

        Get whether the texture has an alpha channel.
        """
        ...
    def hasTransparentAlpha(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasTransparentAlpha() -> bool

        Get whether the texture has semi-transparent texels.
        """
        ...
    def hasZeroAlpha(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasZeroAlpha() -> bool

        Get whether the texture has any texels with an alpha value of 0.0.
        """
        ...
    def name(self: Self, *args: Any, **kwargs: Any) -> Any:
        """name() -> string

        Get the name of the texture.
        """
        ...
    def rawData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """rawData() -> (long, rowPitch, slicePitch)

        Returns a long containing a C++ 'void' pointer which points to the raw data mapped to the texture.
        The caller must deallocate the system memory (using freeRawData()) as the texture itself does not keep any references to it.

        * rowPitch [OUT] (int) - The row pitch of the data. It represents the number of bytes of one line of the texture data.
        * slicePitch [OUT] (int) - The slice pitch of the data. It represents the number of bytes of the whole texture data.
        """
        ...
    def resourceHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """resourceHandle() -> long

        Returns a long containing a C++ 'void' pointer which points to the texture.
        """
        ...
    def setHasAlpha(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setHasAlpha(bool) -> self

        Specify that the texture has an alpha channel.
        """
        ...
    def setHasTransparentAlpha(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setHasTransparentAlpha(bool) -> self

        Specify that the texture has texels with an alpha value greater than or equal to 0.0 and less than 1.0.
        """
        ...
    def setHasZeroAlpha(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setHasZeroAlpha(bool) -> self

        Specify that the texture has texels with an alpha value of 0.0.
        """
        ...
    def textureDescription(self: Self, *args: Any, **kwargs: Any) -> Any:
        """textureDescription() -> MTextureDescription

        Get texture description.
        """
        ...
    def update(self: Self, *args: Any, **kwargs: Any) -> Any:
        """update(pixelData, generateMipMaps, rowPitch=0, region=None) -> self
        update(image, generateMipMaps) -> selfupdate(textureNode) -> self

        Update the contents of an image with new data.

        From pixel data:
        * pixelData (void*) - Data to update the texture with.
        * generateMipMaps (bool) - Indicate if mip-maps levels for the texture be rebuilt.
        * rowPitch (int) The row pitch of the incoming data.
        * region (MTextureUpdateRegion) - Texture sub-region to update. If a None is passed in then the input data is assumed to be updating the entire texture.
        From an image:
        * image (MImage) - Image containing data to update the texture with.
        * generateMipMaps (bool) - Indicate if mip-maps levels for the texture be rebuilt.
        From a texture node:
        * textureNode (MObject) - File texture node
        """
        ...

class MTextureAssignment(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    @property
    def texture(*args: Any, **kwargs: Any) -> Any:
        """The texture"""
        ...
    @texture.setter
    def texture(*args: Any, **kwargs: Any) -> Any:
        """The texture"""
        ...

class MTextureDescription(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    @property
    def fArraySlices(*args: Any, **kwargs: Any) -> Any:
        """Number of array slices. e.g. 6 would be required for a cube-map"""
        ...
    @fArraySlices.setter
    def fArraySlices(*args: Any, **kwargs: Any) -> Any:
        """Number of array slices. e.g. 6 would be required for a cube-map"""
        ...
    @property
    def fBytesPerRow(*args: Any, **kwargs: Any) -> Any:
        """Number of bytes in a row of pixels"""
        ...
    @fBytesPerRow.setter
    def fBytesPerRow(*args: Any, **kwargs: Any) -> Any:
        """Number of bytes in a row of pixels"""
        ...
    @property
    def fBytesPerSlice(*args: Any, **kwargs: Any) -> Any:
        """Number of bytes in a slice (if an array)"""
        ...
    @fBytesPerSlice.setter
    def fBytesPerSlice(*args: Any, **kwargs: Any) -> Any:
        """Number of bytes in a slice (if an array)"""
        ...
    @property
    def fDepth(*args: Any, **kwargs: Any) -> Any:
        """Depth in pixels. A 2D texture has depth of 1."""
        ...
    @fDepth.setter
    def fDepth(*args: Any, **kwargs: Any) -> Any:
        """Depth in pixels. A 2D texture has depth of 1."""
        ...
    @property
    def fEnvMapType(*args: Any, **kwargs: Any) -> Any:
        """Type of environment mapping"""
        ...
    @fEnvMapType.setter
    def fEnvMapType(*args: Any, **kwargs: Any) -> Any:
        """Type of environment mapping"""
        ...
    @property
    def fFormat(*args: Any, **kwargs: Any) -> Any:
        """Pixel / raster format"""
        ...
    @fFormat.setter
    def fFormat(*args: Any, **kwargs: Any) -> Any:
        """Pixel / raster format"""
        ...
    @property
    def fHeight(*args: Any, **kwargs: Any) -> Any:
        """Height in pixels"""
        ...
    @fHeight.setter
    def fHeight(*args: Any, **kwargs: Any) -> Any:
        """Height in pixels"""
        ...
    @property
    def fMipmaps(*args: Any, **kwargs: Any) -> Any:
        """Number of mipmap levels. 0 means the entire mipmap chain."""
        ...
    @fMipmaps.setter
    def fMipmaps(*args: Any, **kwargs: Any) -> Any:
        """Number of mipmap levels. 0 means the entire mipmap chain."""
        ...
    @property
    def fTextureType(*args: Any, **kwargs: Any) -> Any:
        """Type of texture"""
        ...
    @fTextureType.setter
    def fTextureType(*args: Any, **kwargs: Any) -> Any:
        """Type of texture"""
        ...
    @property
    def fWidth(*args: Any, **kwargs: Any) -> Any:
        """Width in pixels"""
        ...
    @fWidth.setter
    def fWidth(*args: Any, **kwargs: Any) -> Any:
        """Width in pixels"""
        ...
    kCubeMap: int = ...
    kDepthTexture: int = ...
    kEnvCrossHoriz: int = ...
    kEnvCrossVert: int = ...
    kEnvCubemap: int = ...
    kEnvHemiSphere: int = ...
    kEnvLatLong: int = ...
    kEnvNone: int = ...
    kEnvSphere: int = ...
    kImage1D: int = ...
    kImage1DArray: int = ...
    kImage2D: int = ...
    kImage2DArray: int = ...
    kNumberOfEnvMapTypes: int = ...
    kNumberOfTextureTypes: int = ...
    kVolumeTexture: int = ...
    def setToDefault2DTexture(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setToDefault2DTexture() -> self

        Utility to set texture description to describe a 0 size 2-dimensional texture.
        """
        ...

class MTextureManager(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def acquireDepthTexture(self: Self, *args: Any, **kwargs: Any) -> Any:
        """acquireDepthTexture(textureName, image, generateMipMaps=True, normalizationDesc=None) -> MTexture
        acquireDepthTexture(textureName, pixelData, width, height, generateMipMaps=True, normalizationDesc=None) -> MTexture

        Ask the renderer to acquire a hardware texture.

        Acquire a hardware texture from an MImage's depth buffer:
        * textureName (string) - Name of the texture to create
        * image (MImage) - Contains block of system memory data containing depth map information
        * generateMipMaps (bool) - Generate the mipmap levels
        * normalizationDesc (MDepthNormalizationDescription) - Optional information to perform normalization on the depth values. Default value is None

        Acquire a hardware texture from an array of depth values:
        * textureName (string) - Name of the texture to create
        * pixelData (float*) - Contains block of system memory data containing depth information
        * width (unsigned int) - Width of the texture
        * height (unsigned int) - Height of the texture
        * generateMipMaps (bool) - Generate the mipmap levels
        * normalizationDesc (MDepthNormalizationDescription) - Optional information to perform normalization on the depth values. Default value is None
        """
        ...
    def acquireTexture(self: Self, *args: Any, **kwargs: Any) -> Any:
        """(Deprecated) acquireTexture(filePath, mipmapLevels=0, layerName="", alphaChannelIdx=-1) -> MTexture
        acquireTexture(filePath, contextNodeFullName, mipmapLevels=0, layerName="", alphaChannelIdx=-1) -> MTexture
        acquireTexture(textureName, plug, width, height, generateMipMaps=True) -> MTexture
        acquireTexture(textureName, textureDesc, pixelData, generateMipMaps=True) -> MTexture
        acquireTexture(fileNode, allowBackgroundLoad=False) -> MTexture

        Ask the renderer to acquire a hardware texture.

        Acquire a hardware texture from an image file:
        * filePath (string) - Image file name
        * contextNodeFullName (string) Full name of the texture owner Node to be provided as a context to the Maya resolver* mipmapLevels (int) - Mipmap generation levels
        * layerName (string) - The name of the layer to load, this is only relevant for PSD files, otherwise it will have no effect
        * alphaChannelIdx (int) - The index of the alpha channel to load, this is only relevant for PSD files, otherwise it will have no effect

        If a plug to a file texture node is provided then the name, width, height and
        generateMipMaps parameters will be ignored as this information will be
        based on the image on disk associated with texture node. If uv tiling is
        enabled, currently only the first tile will be returned.
        Otherwise, an attempt to bake a texture will be made using the Maya's software
        renderer convert-to-solid-texture functionality.
        * textureName (string) - Name of the texture to create
        * plug (MPlug) - Plug which is attached with a texture
        * width (int) - Width of the texture
        * height (int) - Height of the texture
        * generateMipMaps (bool) - Generate the mipmap levels

        Acquire a hardware texture by providing a texture description and a block of system memory data which matches the texture description:
        * textureName (string) - Name of the texture to create
        * textureDesc (MTextureDescription) - Description of the texture
        * pixelData (void*) - Block of system memory data which matches the texture description
        * generateMipMaps (bool) - Generate the mipmap levels
        Acquire the texture associated with a given texture node. Currently only file texture nodes are supported.
        If uv tiling is enabled, currently only the first tile will be returned.
        * textureNode (MObject) - Node to acquire texture from
        * allowBackgroundLoad (bool) - Allow for background texture loading. The default value is false.
        """
        ...
    def acquireTiledTexture(self: Self, *args: Any, **kwargs: Any) -> Any:
        """acquireTiledTexture(textureName, tilePaths, tilePositions, undefinedColor, width, height) -> [MTexture, failedTilePaths, uvScaleOffset]

        Ask the renderer to acquire a tiled hardware texture.

        * textureName (string) - Name to give to the texture
        * tilePaths (list of strings) - Set of path names to UV tiles
        * tilePositions (MFloatArray) - Set of lower left coordinates for each UV tile
        * undefinedColor (MColor) - Color to fill tile region with if the image for a given UV tile cannot be acquired
        * maxWidth (unsigned int) - Maximum width of the output texture. The value is clamped to a minimum of 256
        * maxHeight (unsigned int) - Maximum height of the output texture. The value is clamped to a minimum of 256
        * failedTilePaths [OUT] (list of strings) - List of files which were not written to the output texture
        * uvScaleOffset [OUT] (MFloatArray) - Transform to map to the uv range of the output texture
        """
        ...
    def addImagePath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addImagePath(string) -> self

        Adds an additional search path for looking up images on disk.
        """
        ...
    def imagePaths(self: Self, *args: Any, **kwargs: Any) -> Any:
        """imagePaths() -> list of strings

        Get the current set of image search paths.
        """
        ...
    def releaseTexture(self: Self, *args: Any, **kwargs: Any) -> Any:
        """releaseTexture(MTexture) -> self

        Deletes the MTexture and releases the reference to the underlying texture which is held by the MTexture object.
        """
        ...
    def saveTexture(self: Self, *args: Any, **kwargs: Any) -> Any:
        """saveTexture(MTexture, string) -> self

        Ask the renderer to save a hardware texture to disk.
        """
        ...

class MTextureUpdateRegion(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    @property
    def fXRangeMax(*args: Any, **kwargs: Any) -> Any:
        """X max value"""
        ...
    @fXRangeMax.setter
    def fXRangeMax(*args: Any, **kwargs: Any) -> Any:
        """X max value"""
        ...
    @property
    def fXRangeMin(*args: Any, **kwargs: Any) -> Any:
        """X min value"""
        ...
    @fXRangeMin.setter
    def fXRangeMin(*args: Any, **kwargs: Any) -> Any:
        """X min value"""
        ...
    @property
    def fYRangeMax(*args: Any, **kwargs: Any) -> Any:
        """Y max value"""
        ...
    @fYRangeMax.setter
    def fYRangeMax(*args: Any, **kwargs: Any) -> Any:
        """Y max value"""
        ...
    @property
    def fYRangeMin(*args: Any, **kwargs: Any) -> Any:
        """Y min value"""
        ...
    @fYRangeMin.setter
    def fYRangeMin(*args: Any, **kwargs: Any) -> Any:
        """Y min value"""
        ...
    @property
    def fZRangeMax(*args: Any, **kwargs: Any) -> Any:
        """Z max value"""
        ...
    @fZRangeMax.setter
    def fZRangeMax(*args: Any, **kwargs: Any) -> Any:
        """Z max value"""
        ...
    @property
    def fZRangeMin(*args: Any, **kwargs: Any) -> Any:
        """Z min value"""
        ...
    @fZRangeMin.setter
    def fZRangeMin(*args: Any, **kwargs: Any) -> Any:
        """Z min value"""
        ...

class MUIDrawManager(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def arc(self: Self, *args: Any, **kwargs: Any) -> Any:
        """arc(center, start, end, normal, radius, numSubdivisions, filled) -> selfarc(center, start, end, normal, radius, filled=False) -> self

        Draw an arc. The arc is within the plane determined by a normal vector.
        The arc sweeps in CCW from the vector that is the projection of the given start vector onto the arc plane,
        and ends at the vector that is the projection of the given end vector onto the arc plane.

        * center (MPoint) - Center of the arc.
        * start (MVector) - Start vector, its projection onto the arc plane is the start of the arc.
        * end (MVector) - End vector, its projection onto the arc plane is the end of the arc.
        * normal (MVector) - Normal vector of the arc plane.
        * radius (float) - Radius of the arc.
        * subdivisions (int) - Number of subdivisions of the arc.
        * filled (bool) - If true the arc will be filled otherwise it will just be drawn as an outline.
        """
        ...
    def arc2d(self: Self, *args: Any, **kwargs: Any) -> Any:
        """arc2d(center, start, end, radius, numSubdivisions, filled) -> selfarc2d(center, start, end, radius, filled=False) -> self

        Draw a 2D arc on the screen. The arc is always facing the camera.
        The arc sweeps in CCW from the start vector and ends at the end vector.

        * center (MPoint) - Center of the arc, only x-y components(in pixels) are used.
        * start (MVector) - Start vector, only x-y components are used.
        * end (MVector) - End vector, only x-y components are used.
        * radius (float) - Radius(in pixels) of the arc.
        * subdivisions (int) - Number of subdivisions of the arc.
        * filled (bool) - If true the arc will be filled otherwise it will just be drawn as an outline.
        """
        ...
    def beginDrawInXray(self: Self, *args: Any, **kwargs: Any) -> Any:
        """beginDrawInXray() -> self

        The drawables to be drawn between calls to beginDrawInXray() and endDrawInXray() will display
        on the top of other geometries in the scene, as the depth test is disabled for these drawables.
        These methods can be used to drawing objects such as locators.
        Note only the drawables meet following conditions would be affected by these two APIs.
          1. Created by method MUIDrawManager::mesh();
          2. The first input parameter in MUIDrawManager::mesh() must be one of kTriangles, kLines and kPoints.
        Any other drawables to be drawn between calls to beginDrawInXray() and endDrawInXray() would display as normal.
        If several meshes are drawn between these two APIs, occlusion order is decided by their specification order.
        """
        ...
    def beginDrawable(self: Self, *args: Any, **kwargs: Any) -> Any:
        """beginDrawable(selectability = kAutomatic, selectionName = 0) -> self

        Resets all draw state, such as color and line style, to defaults and indicates the start of a sequence of drawing operations.
        All drawing operations must take place between calls to beginDrawable() and endDrawable().

        The behavior when calling with no (default) parameters depends on the context:
         - In MPxManipulatorNode.drawUI() context, the geometries will be marked as unselectable.
         - In any other context, like MPxDrawOverride.addUIDrawables(), the geometries will be marked as selectable and can be used for shape selection.Provide parameters (kSelectable, selectionName) with manipulators to specify they are selectable and their selection handle names.
        Provide kNonSelectable as selectability to specify locators are not selectable.


        * selectability (int) - Selectability of the handle to be drawn.
          kNonSelectable  Geometries cannot be used for selection
          kSelectable     Use geometries for selection
          kAutomatic      Use geometries for selection when not in manipulator context
        * selectionName (int) - Selection name for manipulators, usually derived from MPxManipulatorNode.glFirstHandle().
        """
        ...
    def box(self: Self, *args: Any, **kwargs: Any) -> Any:
        """box(center, up, right, scaleX=1.0, scaleY=1.0, scaleZ=1.0, filled=False) -> self

        Draw a box.

        * center (MPoint) - Center position for the box.
        * up (MVector) - The top of the box will be facing this direction.
        * right (MVector) - The side of the box will be facing this direction.
        * scaleX (float) - X size of the box.
        * scaleY (float) - Y size of the box.
        * scaleZ (float) - Z size of the box.
        * filled (bool) - If true the box will be filled otherwise it will just be drawn as an outline.
        """
        ...
    def capsule(self: Self, *args: Any, **kwargs: Any) -> Any:
        """capsule(center, up,radius, height, subdivisionsAxis, subdivisionsHeight, filled=False) -> self

        Draw a capsule.

        * center (MPoint) - Center position for the capsule.
        * up (MVector) - Direction of the Up vector.
        * radius (float) - Radius of the capsule.
        * height (float) - Height of the capsule.
        * subdivisionsAxis (int) - Subdivisions along the main axis.
        * subdivisionsHeight (int) - Subdivisions along height.
        * filled (bool) - If true the capsule will be filled otherwise it will just be drawn as an outline.
        """
        ...
    def circle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """circle(center, normal, radius, numSubdivision, filled) -> selfcircle(center, normal, radius, filled=False) -> self

        Draw a circle.
        The circle is drawn within the plane determined by a normal vector.

        * center (MPoint) - Center of the circle.
        * normal (MVector) - Normal vector of the circle plane.
        * radius (float) - Radius of the circle.
        * numSubdivision (int) - Number of Subdivisions for the circle.
        * filled (bool) - If true the circle will be filled otherwise it will just be drawn as an outline.
        """
        ...
    def circle2d(self: Self, *args: Any, **kwargs: Any) -> Any:
        """circle2d(center, radius, numSubdivision, filled) -> selfcircle2d(center, radius, filled=False) -> self

        Draw a 2D circle on the screen.
        The circle is always facing the camera.

        * center (MPoint) - Center of the circle, only x-y components(in pixels) are used.
        * radius (float) - Radius(in pixels) of the circle.
        * numSubdivision (int) - Number of Subdivisions for the circle.
        * filled (bool) - If true the circle will be filled otherwise it will just be drawn as an outline.
        """
        ...
    def cone(self: Self, *args: Any, **kwargs: Any) -> Any:
        """cone(base, direction, radius, height, subdivisionsCap, filled) -> selfcone(base, direction, radius, height, filled=False) -> self

        Draw a cone.

        * base (MPoint) - Base position for the cone.
        * direction (MVector) - The cone's tip will point in this direction.
        * radius (float) - Radius of the cone.
        * height (float) - Height of the cone.
        * subdivisionsCap (int) - Number of subdivisions of the cap.
        * filled (bool) - If true the cone will be filled otherwise it will just be drawn as an outline.
        """
        ...
    def cylinder(self: Self, *args: Any, **kwargs: Any) -> Any:
        """cylinder(center, up, radius, height, subdivisionsAxis, filled=False) -> self

        Draw a cylinder.

        * center (MPoint) - Center position for the cylinder.
        * up (MVector) - Direction of the Up vector.
        * radius (float) - Radius of the cylinder.
        * height (float) - Height of the cylinder.
        * subdivisionsAxis (int) - Number of subdivisions along the main axis.
        * filled (bool) - If true the cylinder will be filled otherwise it will just be drawn as an outline.
        """
        ...
    def depthPriority(self: Self, *args: Any, **kwargs: Any) -> Any:
        """depthPriority() -> int

        Get the current depth priority value for primitive drawing.

        If the method failed to execute a value of 0 will be returned.
        """
        ...
    def endDrawInXray(self: Self, *args: Any, **kwargs: Any) -> Any:
        """endDrawInXray() -> self

        Pair with beginDrawInXray().
        """
        ...
    def endDrawable(self: Self, *args: Any, **kwargs: Any) -> Any:
        """endDrawable() -> self

        Indicates the end of a sequence of drawing operations.
        All internal drawing state, such as color and line style, are reset to defaults.
        """
        ...
    def getFontList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFontList() -> list of strings

        Get the names of all font faces that are available on current system.
        The names can then be used for MUIDrawManager::setFontName().
        """
        ...
    def getIconNames(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getIconNames() -> list of strings

        Get list of icon names. The names can be used
        for drawing icons using the MUIDrawManager::icon() method.
        """
        ...
    def icon(self: Self, *args: Any, **kwargs: Any) -> Any:
        """icon(position, name, scale)) -> self

        Draw an icon at a given 3d position.

        * position (MPoint) - 3d location of the icon..
        * name (MString) - The name of an icon. The list
         of available icon names can be found using the
        MUIDrawManager::getIconNames() method.
        * scale (float) - Uniform scaling factor for the icon.
        """
        ...
    kAutomatic: int = ...
    kCenter: int = ...
    kClosedLine: int = ...
    kDashed: int = ...
    kDefaultFontSize: int = ...
    kDotted: int = ...
    kFlat: int = ...
    kInclineItalic: int = ...
    kInclineNormal: int = ...
    kInclineOblique: int = ...
    kLeft: int = ...
    kLineNone: int = ...
    kLineOverline: int = ...
    kLineStrikeoutLine: int = ...
    kLineStrip: int = ...
    kLineUnderline: int = ...
    kLines: int = ...
    kNonSelectable: int = ...
    kPoints: int = ...
    kRight: int = ...
    kSelectable: int = ...
    kShaded: int = ...
    kShortDashed: int = ...
    kShortDotted: int = ...
    kSmallFontSize: int = ...
    kSolid: int = ...
    kStippled: int = ...
    kStretchCondensed: int = ...
    kStretchExpanded: int = ...
    kStretchExtraCondensed: int = ...
    kStretchExtraExpanded: int = ...
    kStretchSemiCondensed: int = ...
    kStretchSemiExpanded: int = ...
    kStretchUltraCondensed: int = ...
    kStretchUltraExpanded: int = ...
    kStretchUnstretched: int = ...
    kTriStrip: int = ...
    kTriangles: int = ...
    kWeightBlack: int = ...
    kWeightBold: int = ...
    kWeightDemiBold: int = ...
    kWeightLight: int = ...
    kWeightNormal: int = ...
    def line(self: Self, *args: Any, **kwargs: Any) -> Any:
        """line(startPoint, endPoint) -> self

        Draw a straight line between two points.

        * startPoint (MPoint) - The start point of the line.
        * endPoint (MPoint) - The end point of the line.
        """
        ...
    def line2d(self: Self, *args: Any, **kwargs: Any) -> Any:
        """line2d(startPoint, endPoint) -> self

        Draw a straight line between two points.

        * startPoint (MPoint) - The start point of the line, only x-y components(in pixels) are used.
        * endPoint (MPoint) - The end point of the line, only x-y components(in pixels) are used.
        """
        ...
    def lineList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """lineList(points, draw2D) -> self

        Draw a series of line segments in 3D or 2D.

        * points (MPointArray) - Array of point positions. Pairs of points are interpreted as line segments.
        If an odd number of points is specified then the last point will not be drawn, as it
        does not form a line segment.
        * draw2D (bool) Draw in 2D or 3D.
        """
        ...
    def lineStrip(self: Self, *args: Any, **kwargs: Any) -> Any:
        """lineStrip(points, draw2D) -> self

        Draw a series of connected line segments in 3D or 2D

        * points (MPointArray) - Array of point positions. Each point in the array is connected
        to form a line strip.
        * draw2D (bool) Draw in 2D or 3D.
        """
        ...
    def mesh(self: Self, *args: Any, **kwargs: Any) -> Any:
        """mesh(mode, position, normal=None, color=None, index=None, texcoord=None) -> self

        Draw custom geometric shapes from an array of vertices.

        If the optional normal or color arrays are provided they must contain a single value per element
        of the positions array (i.e. all three arrays must be the same length).

        The optional index array specifies the order in which the vertex positions (and their corresponding normals
        and colors) should be drawn. Vertices can be reused by having their indices appear multiple times, so the index
        array may be longer (or shorter) than the other three arrays.

        If the index array is not provided then the vertices will be drawn in the order in which they appear in the positions array.

        * mode (int) - Primitive mode
          kPoints       Point list
          kLines        Line list
          kLineStrip    Line strip
          kClosedLine   Closed line
          kTriangles    Triangle list
          kTriStrip     Triangle strip
        * position (MPointArray) - List of the vertex positions.
        * normal (MVectorArray) - List of the vertex normals.
        * color (MColorArray) - List of the vertex colors.
        * index (MUintArray) - List of the vertex indices.
        * texcoord (MPointArray) - List of the vertex texture coordinates.
        """
        ...
    def mesh2d(self: Self, *args: Any, **kwargs: Any) -> Any:
        """mesh2d(mode, position, color=None, index=None, texcoord=None) -> self

        Draw custom 2d geometric shapes from an array of vertices.

        If the optional color arrays are provided they must contain a single value per element of the positions
        array (i.e. both arrays must be the same length).

        The optional index array specifies the order in which the vertex positions (and their corresponding colors)
        should be drawn. Vertices can be reused by having their indices appear multiple times, so the index array may
        be longer (or shorter) than the other two arrays.

        If the index array is not provided then the vertices will be drawn in the order in which they appear in the positions array.

        * mode (int) - Primitive mode
          kPoints       Point list
          kLines        Line list
          kLineStrip    Line strip
          kClosedLine   Closed line
          kTriangles    Triangle list
          kTriStrip     Triangle strip
        * position (MPointArray) - List of the vertex positions, only x-y components of the point are used.
        * color (MColorArray) - List of the vertex colors.
        * index (MUintArray) - List of the vertex indices.
        * texcoord (MPointArray) - List of the vertex texture coordinates.
        """
        ...
    def point(self: Self, *args: Any, **kwargs: Any) -> Any:
        """point(point) -> self

        Draw a point.

        * point (MPoint) - Position of the point.
        """
        ...
    def point2d(self: Self, *args: Any, **kwargs: Any) -> Any:
        """point2d(point) -> self

        Draw a point.

        * point (MPoint) - Position of the point, only x-y components(in pixels) are used.
        """
        ...
    def points(self: Self, *args: Any, **kwargs: Any) -> Any:
        """points(points, draw2D) -> self

        Draw a series of points in 3D or 2D.

        * points (MPointArray) - Array of point positions.
        * draw2D (bool) Draw in 2D or 3D.
        """
        ...
    def rect(self: Self, *args: Any, **kwargs: Any) -> Any:
        """rect(center, up, normal, scaleX, scaleY, filled=False) -> self

        Draw a rectangle.
        The rectangle is within the plane determined by a normal vector, and a up vector is given to determine the X-Y direction.

        * center (MPoint) - Center of the rectangle.
        * up (MVector) - Up vector of the rectangle.
        * normal (MVector) - Normal vector of the rectangle plane.
        * scaleX (float) - Scale factor in X-direction.
        * scaleY (float) - Scale factor in Y-direction.
        * filled (bool) - If true the rectangle will be filled otherwise it will just be drawn as an outline.
        """
        ...
    def rect2d(self: Self, *args: Any, **kwargs: Any) -> Any:
        """rect2d(center, up, scaleX, scaleY, filled=False) -> self

        Draw a 2D rectangle on the screen.
        The rectangle is always facing the camera, and a up vector is given to determine the X-Y direction

        * center (MPoint) - Center of the rectangle, only x-y components(in pixels) are used.
        * up (MVector) - Up vector of the rectangle, only x-y components are used.
        * scaleX (float) - Scale factor in X-direction.
        * scaleY (float) - Scale factor in Y-direction.
        * filled (bool) - If true the rectangle will be filled otherwise it will just be drawn as an outline.
        """
        ...
    def setColor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setColor(color) -> self

        Set the draw color. This will remain in effect until the next call to setColor(), setColorIndex() or endDrawable().

        For text this color will be used as the foreground color. Background color can be specified directly in the call to text().


        Default: (0.7, 0.7, 0.7, 1)
        """
        ...
    def setColorIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setColorIndex(index) -> self

        Set the color index for the later primitive and text drawing.
        For default, it will use (0.7, 0.7, 0.7, 1) as default color.

        * index (int) - Color index
        """
        ...
    def setDepthPriority(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDepthPriority(priority) -> self

        Set the depth priority for primitive drawing.

        The MRenderItem class lists some sample internal priorities which may be used.

        * priority (int) - Depth priority.
        """
        ...
    def setFontIncline(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setFontIncline(fontIncline) -> self

        Set the incline of font to be used when drawing text.

        * fontIncline (int) - The font incline to use.
        """
        ...
    def setFontLine(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setFontLine(fontLine) -> self

        Set the line of font to be used when drawing text.

        * fontLine (int) - The font line to use.
        """
        ...
    def setFontName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setFontName(faceName) -> self

        Set the face name of font to be used when drawing text.

        * faceName (string) - The font face name(case-insensitive) to use, All system font faces are supported. "helvetica" is the default for invalid input.
        """
        ...
    def setFontSize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setFontSize(fontSize) -> self

        Set the size of font to be used when drawing text.

        * fontSize (int) - The font height(in pixel) to use.
        """
        ...
    def setFontStretch(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setFontStretch(fontStretch) -> self

        Set the stretch of font to be used when drawing text.

        * fontStretch (int) - The font stretch to use.
        """
        ...
    def setFontWeight(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setFontWeight(fontWeight) -> self

        Set the weight of font to be used when drawing text.

        * weight (int) - The font weight to use.
        """
        ...
    def setLineStyle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setLineStyle(style) -> self
        setLineStyle(factor, pattern) -> self

        Set the line style for the primitive drawing (line, rect, box...)

        * style (int) - Line style type.
          kSolid         Solid line
          kShortDotted   Short Dotted line
          kShortDashed   Short dashed line
          kDashed        Dashed line
          kDashed        Dotted line

        Or set the dashed line pattern for the primitive drawing (line, rect, box...)

        * factor (int) - a multiplier for each bit in the line stipple pattern.
        * pattern (int) - a bit pattern indicating which fragments of a line will be drawn
        """
        ...
    def setLineWidth(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setLineWidth(value) -> self

        Set the line width for the primitive drawing (line, rect, box...)

        * value (float) - Line width in pixels.
        """
        ...
    def setPaintStyle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPaintStyle(style) -> self

        Set the paint style for filled primitive drawing.

        * style (int) - Paint style type.
          kFlat      Solid
          kStippled  Stippled
          kShaded    Shaded with lighting
        """
        ...
    def setPointSize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPointSize(value) -> self

        Set the point size for the point drawing.

        * value (float) - Point size in pixels.
        """
        ...
    def setTexture(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setTexture(texture) -> self

        Set the active texture to apply when drawing a mesh.
        This will remain in effect until the next call to setTexture().

        * texture (MTexture) - The texture which will affect the later drawing.
        """
        ...
    def setTextureMask(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setTextureMask(mask) -> self

        Set the channel mask to used when applying a texture to a mesh.
        This will remain in effect until the next call to setTextureMask().

        Fails when mask is not supported.

        * mask (int) - The channel mask which will affect the later drawing.
                Currently, only MBlendState.kRGBAChannels, MBlendState.kRGBChannels and MBlendState.kAlphaChannel are supported.
        """
        ...
    def setTextureSampler(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setTextureSampler(filter, address) -> self

        Set the filter and address mode used when applying a texture to a mesh.
        This will remain in effect until the next call to setTextureSampler().

        Fails when filter and address combination is not supported.

        * filter (int) - The filter which will affect the later drawing.
                Currently, only MSamplerState.kMinMagMipPoint and MSamplerState.kMinMagMipLinear are supported.
        * address (int) - The canonical range which will affect the later drawing.
                Currently, only MSamplerState.kTexWrap and MSamplerState.kTexClamp are supported.
        """
        ...
    def sphere(self: Self, *args: Any, **kwargs: Any) -> Any:
        """sphere(center, radius, subdivisionsAxis, subdivisionsHeight, filled=False) -> selfsphere(center, radius, filled=False) -> self

        Draw a sphere.

        * center (MPoint) - Center of the sphere.
        * radius (float) - Radius of the sphere.
        * subdivisionsAxis (int) - Number of subdivisions along main axis.
        * subdivisionsHeight (int) - Number of subdivisions along height.
        * filled (bool) - If true the sphere will be filled otherwise it will just be drawn as a wireframe.
        """
        ...
    def text(self: Self, *args: Any, **kwargs: Any) -> Any:
        """text(position, text, alignment=kLeft, backgroundSize=None, backgroundColor=None, dynamic=False) -> self

        Draw a screen facing and horizontal aligned text in viewport 2.0.
        It has a fixed size in screen space.

        * position (MPoint) - Position of the text to be drawn, it is 3d object space.
        * text (string) - Content of the text string.
        * alignment (TextAlignment) - Alignment of the text.
                 - "kLeft", background box's left bottom will be located at "position".         In width direction, text area will be aligned to the left side of background.
                 In height direction, text are will be aligned in the middle of background.
                 - "kCenter", background box' center bottom will be located at "position".         Text area's center and background box's center will be the same point.
                 - "kRight", background box's right bottom will be located at "position".         In width direction, text area will be aligned to the right side of background.
                 In height direction, text are will be aligned in the middle of background.
        * backgroundSize ([int, int]) - The background box size of the text.
                 Default is None, in this case there will be no background, just shows the text.
                 If it is specified with smaller size than text, the text will be clipped.
                 It is a int array with size 2, like "backgroundSize = [ width, height ]"
                 Size unit is the screen pixel.
        * backgroundColor (MColor) - The color of the background, it can be transparent.
                 If None is passed, background will be fully transparent.
        * dynamic (bool) - This is mostly used for performance.
                 If the text draw is not changed frequently, we can leave it as default value false.
        			If the text draw is changing very often like it is showing some dynamic numbers,
                 in this case making dynamic true will give better performance.
        """
        ...
    def text2d(self: Self, *args: Any, **kwargs: Any) -> Any:
        """text2d(position, text, alignment=kLeft, backgroundSize=None, backgroundColor=None, dynamic=False) -> self

        Draw a text on the screen.

        * position (MPoint) - Position of the text to be drawn, it is in screen space, only x-y components are used.
        * text Content of the text string.
        * alignment (TextAlignment) - Alignment of the text.
                 - "kLeft", background box's left bottom will be located at "position".         In width direction, text area will be aligned to the left side of background.
                 In height direction, text are will be aligned in the middle of background.
                 - "kCenter", background box' center bottom will be located at "position".         Text area's center and background box's center will be the same point.
                 - "kRight", background box's right bottom will be located at "position".         In width direction, text area will be aligned to the right side of background.
                 In height direction, text are will be aligned in the middle of background.
        * backgroundSize ([int, int]) - The background box size of the text.
                 Default is None, in this case there will be no background, just shows the text.
                 If it is specified with smaller size than text, the text will be clipped.
                 It is a int array with size 2, like "backgroundSize = [ width, height ]"
                 Size unit is the screen pixel.
        * backgroundColor (MColor) - The color of the background, it can be transparent.
                 If None is passed, background will be fully transparent.
        * dynamic (bool) - This is mostly used for performance.
                 If the text draw is not changed frequently, we can leave it as default value false.
        			If the text draw is changing very often like it is showing some dynamic numbers,
                 in this case making dynamic true will give better performance.
        """
        ...

class MUniformParameter(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def asBool(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asBool(context) -> bool

        Get the value of this uniform parameter as a boolean value.
        Because some parameters can be shape-dependent, the method requires access to the current context being rendered.

        * context (MDrawContext) - Draw context being used for render.
        """
        ...
    def asFloat(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asFloat(context) -> float

        Get the value of this uniform parameter as a float.
        Because some parameters can be shape-dependent, the method requires access to the current context being rendered.

        * context (MDrawContext) - Draw context being used for render.
        """
        ...
    def asFloatArray(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asFloatArray(context) -> tuple of floats

        Get the value of this uniform parameter as one or more floating point values.
        Because some parameters can be shape-dependent, the method requires access to the current context being rendered.

        * context (MDrawContext) - Draw context being used for render.
        """
        ...
    def asInt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asInt(context) -> int

        Get the value of this uniform parameter as an integer.
        Because some parameters can be shape-dependent, the method requires access to the current context being rendered.

        * context (MDrawContext) - Draw context being used for render.
        """
        ...
    def asString(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asString(context) -> string

        Get the value of this uniform parameter as a string.
        Because some parameters can be shape-dependent, the method requires access to the current context being rendered.

        * context (MDrawContext) - Draw context being used for render.
        """
        ...
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy data from source parameter.

        * source (MUniformParameter) - The source parameter to copy from
        """
        ...
    @property
    def enumFieldNames(*args: Any, **kwargs: Any) -> Any:
        """The field names of an enum attribute."""
        ...
    @enumFieldNames.setter
    def enumFieldNames(*args: Any, **kwargs: Any) -> Any:
        """The field names of an enum attribute."""
        ...
    def hasChanged(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasChanged(context) -> bool

        Has the value of this parameter changed since the last time it was accessed?
        This allows your shader to minimise state changes by only updating modified parameters.

        * context (MDrawContext) - Draw context being used for render.
        """
        ...
    def isATexture(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isATexture() -> bool

        Returns True if this parameter represents a texture, False otherwise.
        """
        ...
    kSemanticBackgroundColor: int = ...
    kSemanticBump: int = ...
    kSemanticBumpTexture: int = ...
    kSemanticColor: int = ...
    kSemanticColorTexture: int = ...
    kSemanticEnvironment: int = ...
    kSemanticFarClipPlane: int = ...
    kSemanticFrameNumber: int = ...
    kSemanticHWSEdgeLevel: int = ...
    kSemanticHWSFaceLevel: int = ...
    kSemanticHWSFrontCCW: int = ...
    kSemanticHWSHighlighting: int = ...
    kSemanticHWSInstancedDraw: int = ...
    kSemanticHWSObjectLevel: int = ...
    kSemanticHWSOccluder: int = ...
    kSemanticHWSPrimitiveBase: int = ...
    kSemanticHWSPrimitiveCountPerInstance: int = ...
    kSemanticHWSVertexLevel: int = ...
    kSemanticLocalViewer: int = ...
    kSemanticNearClipPlane: int = ...
    kSemanticNormal: int = ...
    kSemanticNormalTexture: int = ...
    kSemanticNormalizationTexture: int = ...
    kSemanticObjectDir: int = ...
    kSemanticObjectPos: int = ...
    kSemanticOpaqueDepthTexture: int = ...
    kSemanticProjectionDir: int = ...
    kSemanticProjectionInverseMatrix: int = ...
    kSemanticProjectionInverseTransposeMatrix: int = ...
    kSemanticProjectionMatrix: int = ...
    kSemanticProjectionPos: int = ...
    kSemanticProjectionTransposeMatrix: int = ...
    kSemanticTime: int = ...
    kSemanticTranspDepthTexture: int = ...
    kSemanticUnknown: int = ...
    kSemanticViewDir: int = ...
    kSemanticViewInverseMatrix: int = ...
    kSemanticViewInverseTransposeMatrix: int = ...
    kSemanticViewMatrix: int = ...
    kSemanticViewPos: int = ...
    kSemanticViewProjectionInverseMatrix: int = ...
    kSemanticViewProjectionInverseTransposeMatrix: int = ...
    kSemanticViewProjectionMatrix: int = ...
    kSemanticViewProjectionTransposeMatrix: int = ...
    kSemanticViewTransposeMatrix: int = ...
    kSemanticViewportPixelSize: int = ...
    kSemanticWorldDir: int = ...
    kSemanticWorldInverseMatrix: int = ...
    kSemanticWorldInverseTransposeMatrix: int = ...
    kSemanticWorldMatrix: int = ...
    kSemanticWorldPos: int = ...
    kSemanticWorldTransposeMatrix: int = ...
    kSemanticWorldViewInverseMatrix: int = ...
    kSemanticWorldViewInverseTransposeMatrix: int = ...
    kSemanticWorldViewMatrix: int = ...
    kSemanticWorldViewProjectionInverseMatrix: int = ...
    kSemanticWorldViewProjectionInverseTransposeMatrix: int = ...
    kSemanticWorldViewProjectionMatrix: int = ...
    kSemanticWorldViewProjectionTransposeMatrix: int = ...
    kSemanticWorldViewTransposeMatrix: int = ...
    kType1DTexture: int = ...
    kType2DTexture: int = ...
    kType3DTexture: int = ...
    kTypeBool: int = ...
    kTypeCubeTexture: int = ...
    kTypeEnum: int = ...
    kTypeEnvTexture: int = ...
    kTypeFloat: int = ...
    kTypeInt: int = ...
    kTypeString: int = ...
    kTypeUnknown: int = ...
    @property
    def keyable(*args: Any, **kwargs: Any) -> Any:
        """The keyable state of this parameter"""
        ...
    @keyable.setter
    def keyable(*args: Any, **kwargs: Any) -> Any:
        """The keyable state of this parameter"""
        ...
    def name(self: Self, *args: Any, **kwargs: Any) -> Any:
        """name() -> string

        Get the name of this parameter.
        """
        ...
    def numColumns(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numColumns() -> int

        Get the number of columns in this parameter.
        """
        ...
    def numElements(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numElements() -> int

        Get the number of elements in this parameter (including rows and columns).
        """
        ...
    def numRows(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numRows() -> int

        Get the number of rows in this parameter.
        """
        ...
    def plug(self: Self, *args: Any, **kwargs: Any) -> Any:
        """plug() -> MPlug

        Get the plug managed by this parameter.
        """
        ...
    @property
    def rangeMax(*args: Any, **kwargs: Any) -> Any:
        """The hard range upper bound for a numeric uniform parameter."""
        ...
    @rangeMax.setter
    def rangeMax(*args: Any, **kwargs: Any) -> Any:
        """The hard range upper bound for a numeric uniform parameter."""
        ...
    @property
    def rangeMin(*args: Any, **kwargs: Any) -> Any:
        """The hard range lower bound for a numeric uniform parameter."""
        ...
    @rangeMin.setter
    def rangeMin(*args: Any, **kwargs: Any) -> Any:
        """The hard range lower bound for a numeric uniform parameter."""
        ...
    def semantic(self: Self, *args: Any, **kwargs: Any) -> Any:
        """semantic() -> int

        Get the semantic of this parameter.

        The list of available semantic values can be obtained with the following commands:
          print filter(lambda k: k.startswith('kSemantic'), dir(maya.api.OpenMayaRender.MUniformParameter))
        """
        ...
    def setBool(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setBool(value) -> self

        Set the value of this uniform parameter as a boolean value.
        Note that it is not possible to set shape-dependent parameters.

        * value (bool) - the new value for this parameter.
        """
        ...
    def setDirty(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDirty() -> self

        Mark the data for this parameter as dirty. This will force the parameter to report that it has been changed the next time it is accessed. This allows external events (e.g. device lost, texture management, etc) to force a shader to re-set parameters tied to externally managed resources.
        """
        ...
    def setFloat(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setFloat(value) -> self

        Set the value of this uniform parameter as a float.
        Note that it is not possible to set shape-dependent parameters.

        * value (float) - the new float value for this parameter.
        """
        ...
    def setFloatArray(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setFloatArray(value) -> self

        Set the value of this uniform parameter as one or more floating point values.
        Note that it is not possible to set shape-specific parameters.

        * value (tuple of floats) - a tuple of floats holding the new floating point value(s) for this parameter.
        """
        ...
    def setInt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setInt(value) -> self

        Set the value of this uniform parameter as an integer value.
        Note that it is not possible to set shape-dependent parameters.

        * value (int) - the new value for this parameter.
        """
        ...
    def setString(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setString(value) -> self

        Set the value of this uniform parameter as a string.
        Note that it is not possible to set shape-dependent parameters.

         * value (string) - the new string value for this parameter.
        """
        ...
    @property
    def softRangeMax(*args: Any, **kwargs: Any) -> Any:
        """The soft range upper bound for a numeric uniform parameter."""
        ...
    @softRangeMax.setter
    def softRangeMax(*args: Any, **kwargs: Any) -> Any:
        """The soft range upper bound for a numeric uniform parameter."""
        ...
    @property
    def softRangeMin(*args: Any, **kwargs: Any) -> Any:
        """The soft range lower bound for a numeric uniform parameter."""
        ...
    @softRangeMin.setter
    def softRangeMin(*args: Any, **kwargs: Any) -> Any:
        """The soft range lower bound for a numeric uniform parameter."""
        ...
    def source(self: Self, *args: Any, **kwargs: Any) -> Any:
        """source() -> MPlug

        Get the source plug connected to this parameter. Other than textures, this will typically be an invalid plug.
        """
        ...
    def type(self: Self, *args: Any, **kwargs: Any) -> Any:
        """type() -> int

        Get the type of this parameter.

        Available values:
          kTypeUnknown,
          kTypeBool,
          kTypeInt,
          kTypeFloat,
          kType1DTexture,
          kType2DTexture,
          kType3DTexture,
          kTypeCubeTexture,
          kTypeEnvTexture,
          kTypeString,
          kTypeEnum
        """
        ...
    @property
    def uiHidden(*args: Any, **kwargs: Any) -> Any:
        """The hidden state of this parameter"""
        ...
    @uiHidden.setter
    def uiHidden(*args: Any, **kwargs: Any) -> Any:
        """The hidden state of this parameter"""
        ...
    @property
    def uiNiceName(*args: Any, **kwargs: Any) -> Any:
        """The UI Nice Name for the attribute."""
        ...
    @uiNiceName.setter
    def uiNiceName(*args: Any, **kwargs: Any) -> Any:
        """The UI Nice Name for the attribute."""
        ...
    def userData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """userData() -> int

        Get the user data for this parameter. User data can be used to store plugin specific information that you want to associate with this parameter. Typically this will be used to store a handle to the effect parameter.
        """
        ...

class MUniformParameterList(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __getitem__(self: Self, key: Any) -> Any:
        """Return self[key]."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __len__(self: Self) -> Any:
        """Return len(self)."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """append(element) -> bool

        Append a new parameter to this end of this list.

        * element (MUniformParameter) - The new parameter to append
        """
        ...
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy data from source list.

        * source (MUniformParameterList) - The source list to copy from
        """
        ...
    def setElement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setElement(n, element) -> bool

        Set the nth parameter in this list.

        * n (int) - The index of the element to set
        * element (MUniformParameter) - The value to set
        """
        ...
    def setLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setLength(length) -> bool

        Set the number of parameters in this list. If this is greater than the current number of parameters in the list, the caller is responsible for setting the new parameters to valid values using setElement.

        * length (int) - The number of parameters in this list.
        """
        ...

class MUserRenderOperation(MRenderOperation):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def addUIDrawables(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addUIDrawables(drawManager, frameContext) -> self

        Provides access to the MUIDrawManager, which can be used to queue up operations to draw simple UI shapes like lines, circles, text, etc.

        This method will only be called when hasUIDrawables() is overridden to return true.

        * drawManager (MUIDrawManager) - The UI draw manager, it can be used to draw some simple geometry including text.
        * frameContext (MFrameContext) - Frame level context information
        """
        ...
    def cameraOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """cameraOverride() -> MCameraOverride

        Query for a camera override.
        """
        ...
    def enableSRGBWrite(self: Self, *args: Any, **kwargs: Any) -> Any:
        """enableSRGBWrite() -> bool

        Return whether to enable GPU based gamma correction during pixel writes.
        """
        ...
    def hasUIDrawables(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasUIDrawables() -> bool

        Query whether addUIDrawables() should be called or not.
        """
        ...
    kClear: int = ...
    kHUDRender: int = ...
    kPresentTarget: int = ...
    kQuadRender: int = ...
    kSceneRender: int = ...
    kUserDefined: int = ...
    def name(self: Self, *args: Any, **kwargs: Any) -> Any:
        """name() -> string

        Returns the name of the render operator.
        """
        ...
    def operationType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """operationType() -> int

        Returns the type of a render operator.
        """
        ...
    def requiresLightData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """requiresLightData() -> bool

        Indicates whether light data from the renderer is required for this user operation.
        """
        ...
    def targetOverrideList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """targetOverrideList() -> list of MRenderTarget

        Return a list of render target which will be used as the target overrides for the operation.
        """
        ...
    def viewportRectangleOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """viewportRectangleOverride() -> MFloatPoint

        Query for a viewport rectangle override.
        """
        ...

class MVaryingParameter(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def addElement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addElement(child) -> self

        Add a child element to this parameter.
        This operation is only valid for parameters of type kStructure.

        * child (MVaryingParameter) - the parameter to add to the structure.
        """
        ...
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy data from source parameter.

        * source (MVaryingParameter) - The source parameter to copy from
        """
        ...
    def destinationSetName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """destinationSetName() -> string

        Get the destination Set of this parameter.
        """
        ...
    def dimension(self: Self, *args: Any, **kwargs: Any) -> Any:
        """dimension() -> int

        Get the dimension of this parameter.
        """
        ...
    def elementSize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """elementSize() -> int

        Get the size in bytes of one element of this parameter.
        """
        ...
    def getElement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getElement(index) -> MVaryingParameter

        Get an element within a structure.
        This operation is only valid for parameters of type kStructure.

        * index (int) - The index of the structure element to return.
        """
        ...
    kBinormal: int = ...
    kChar: int = ...
    kColor: int = ...
    kDouble: int = ...
    kFloat: int = ...
    kInt16: int = ...
    kInt32: int = ...
    kInvalidParameter: int = ...
    kNoSemantic: int = ...
    kNormal: int = ...
    kPosition: int = ...
    kStructure: int = ...
    kTangent: int = ...
    kTexCoord: int = ...
    kUnsignedChar: int = ...
    kUnsignedInt16: int = ...
    kUnsignedInt32: int = ...
    kWeight: int = ...
    def maximumStride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """maximumStride() -> int

        Get the maximum stride of this parameter in bytes.
        For parameter that accept a range of element counts, this corresponds to the maximum number of elements the parameter supports.
        """
        ...
    def name(self: Self, *args: Any, **kwargs: Any) -> Any:
        """name() -> string

        Get the name of this parameter.
        """
        ...
    def numElements(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numElements() -> int

        Get the number of elements in this structure.
        This operation is only valid for parameters of type kStructure.
        """
        ...
    def removeElements(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeElements() -> self

        Remove all child elements from a structure.
        This operation is only valid for parameters of type kStructure.
        """
        ...
    def semantic(self: Self, *args: Any, **kwargs: Any) -> Any:
        """semantic() -> int

        Get the semantic of this parameter.

        Available values:
          kNoSemantic,
          kPosition,
          kNormal,
          kTexCoord,
          kColor,
          kWeight,
          kTangent,
          kBinormal
        """
        ...
    def semanticName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """semanticName() -> string

        Get the semantic name assigned to this parameter.
        The semanticName is used to identify a custom vertex stream request in order to fill the stream with the appropriate data requested by a shader override.
        """
        ...
    def setSource(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setSource(semantic, name) -> self

        While the source of geometry parameters is usually configured by the artist through Maya's user interface, this method allows you to programatically set the source of a geometry parameter, including both the data type (e.g. position, normal, etc) and an optional set name (e.g. UV set 'map1'). This is useful for implementing custom default values or shader operations.

        * type (int) - the type of data to populate this parameter with (see semantic())
        * name (string) - the specific data set to use for parameter types which support data sets, such as UV and color.
        """
        ...
    def sourceSemantic(self: Self, *args: Any, **kwargs: Any) -> Any:
        """sourceSemantic() -> int

        Get the type of data (e.g. position, normal, uv) currently populating this parameter.
        This method will only return a useful value when called on leaf-level parameters (e.g. structures do not have sources, only the elements of a structure have sources).
        See semantic() for the list of values.
        """
        ...
    def sourceSetName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """sourceSetName() -> string

        If the current data type supports data sets (e.g. uv sets, color sets), get the name of the data set populating this parameter. This method will only return a useful value when called on leaf-level parameters (e.g. structures do not have sources, only the elements of a structure have sources).
        """
        ...
    def type(self: Self, *args: Any, **kwargs: Any) -> Any:
        """type() -> int

        Get the type of this parameter.

        Available values:
          kInvalidParameter,
          kStructure,
          kFloat,
          kDouble,
          kChar,
          kUnsignedChar,
          kInt16,
          kUnsignedInt16,
          kInt32,
          kUnsignedInt32
        """
        ...
    def updateId(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateId() -> int

        Get the update id.
        The update id is increased every time the parameter sources or sourceSet are changed. A plugin can compare the update id value between subsequent calls to this function to know if the source has changed since the last call.
        """
        ...

class MVaryingParameterList(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __getitem__(self: Self, key: Any) -> Any:
        """Return self[key]."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __len__(self: Self) -> Any:
        """Return len(self)."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """append(element) -> bool

        Append a new parameter to this end of this list.

        * element (MVaryingParameter) - The new parameter to append
        """
        ...
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy data from source list.

        * source (MVaryingParameterList) - The source list to copy from
        """
        ...
    def setElement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setElement(n, element) -> bool

        Set the nth parameter in this list.

        * n (int) - The index of the element to set
        * element (MVaryingParameter) - The value to set
        """
        ...
    def setLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setLength(length) -> bool

        Set the number of parameters in this list. If this is greater than the current number of parameters in the list, the caller is responsible for setting the new parameters to valid values using setElement.

        * length (int) - The number of parameters in this list.
        """
        ...

class MVertexBuffer(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def acquire(self: Self, *args: Any, **kwargs: Any) -> Any:
        """acquire(size, writeOnly) -> long

        Get a pointer to memory for the buffer.

        * size (int) - The size of the buffer to acquire.
        * writeOnly (bool) - Specified if the returned memory should be uninitialized or filled with actual buffer content.
                             When the current buffer content is not needed, it is preferable to set the writeOnly flag to true for better performance.
        """
        ...
    def commit(self: Self, *args: Any, **kwargs: Any) -> Any:
        """commit(long) -> self

        Commit the data stored in the memory given by acquire() to the buffer.
        If this method is not called, the acquired buffer will not be used in drawing.
        The pointer must be the same pointer returned from acquire().
        """
        ...
    def descriptor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """descriptor() -> MVertexBufferDescriptor

        Get the the buffer descriptor.
        """
        ...
    def hasCustomResourceHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasCustomResourceHandle() -> bool

        Returns true if this vertex buffer is using a custom resource handle set
        by the plugin using MVertexBuffer.setResourceHandle(long, int).
        """
        ...
    def lockResourceHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """lockResourceHandle() -> self

        Lock the resource handle. The pointer returned from resourceHandle() is
        guaranteed to exist between lockResourceHandle() and unlockResourceHandle().

        MVertexBuffer may store data in system memory, GPU memory or both. Direct
        access to the GPU representation of the data is possible through the
        buffer's resourceHandle(). If the GPU representation of the data is to be
        directly modified using an external graphics or compute API, then
        lockResourceHandle() must be called on the MVertexBuffer once, before any
        modifications to the buffer are made.

        While a resource handle is locked, any external modifications to the GPU
        buffer will be recognized by Maya.

        While a resource handle is locked, consolidated world will take longer to
        consolidate the corresponding object. After unlocking a resource handle,
        consolidated world will take longer to consolidate the corresponding object
        one more time, the first time the unlocked resource handle is consolidated.

        Calling lockResourceHandle() and unlockResourceHandle() on a custom resource
        handle has no effect.

        Reallocating or deleting the GPU representation of the data between
        lockResourceHandle() and unlockResourceHandle() will result in undefined
        behavior. acquire(), commit() and update() may reallocate the GPU representation.
        unload() may delete the GPU representation.

        map() and unmap() will work if they are called between lockResourceHandle()
        and unlockResourceHandle(). They operate on the GPU representation.
        """
        ...
    def map(self: Self, *args: Any, **kwargs: Any) -> Any:
        """map() -> long

        Get a read-only pointer to the existing content of the buffer.
        Writing new content in this memory block is not supported and can lead to unexpected behavior.
        """
        ...
    def resourceHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """resourceHandle() -> long

        Returns a long containing a C++ 'float' pointer which points to the graphics device dependent handle to the vertex buffer.
        """
        ...
    def setResourceHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setResourceHandle(long, int) -> self

        Set the graphics-device-dependent hardware buffer resource handle.
        """
        ...
    def unload(self: Self, *args: Any, **kwargs: Any) -> Any:
        """unload() -> self

        If the buffer is resident in GPU memory, calling this method will move it to system memory and free the GPU memory.
        """
        ...
    def unlockResourceHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """unlockResourceHandle() -> self

        Unlock the resource handle. The pointer returned from resourceHandle is not
        guaranteed to exist any more.
        See lockResourceHandle() for more details.
        """
        ...
    def unmap(self: Self, *args: Any, **kwargs: Any) -> Any:
        """unmap() -> self

        Release the data exposed by map(). If this method is not called, the buffer will not be recycled.
        """
        ...
    def update(self: Self, *args: Any, **kwargs: Any) -> Any:
        """update(buffer, destOffset, numVerts, truncateIfSmaller) -> self

        Set a portion (or all) of the contents of the MVertexBuffer using the data in the provided software buffer.
        The internal hardware buffer will be allocated or reallocated to fit if required, according to the vertex size from the descriptor.

        * buffer (long) - The input data buffer, starting with the first vertex to copy.
        * destOffset (int) - The offset (in vertices) from the beginning of the buffer to start writing to.
        * numVerts (int) - The number of vertices to copy.
        * truncateIfSmaller (bool) - If true and offset+numVerts is less than the pre-existing size of the buffer,
                                     then the buffer contents will be truncated to the new size. Truncating the buffer size
                                     will not cause a reallocation and will not lose data before the destOffset.
        """
        ...
    def vertexCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """vertexCount() -> int

        Get the size of the vertex buffer.
        """
        ...

class MVertexBufferArray(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __getitem__(self: Self, key: Any) -> Any:
        """Return self[key]."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __len__(self: Self) -> Any:
        """Return len(self)."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """append(MVertexBuffer, name) -> self

        Add a new vertex buffer to the list.
        """
        ...
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clear() -> self

        Clear the array.
        """
        ...
    def getBuffer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getBuffer(string) -> MVertexBuffer

        Get vertex buffer by name.
        """
        ...
    def getName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getName(int) -> string

        Get the name of the buffer at desired index.
        """
        ...

class MVertexBufferDescriptor(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    @property
    def dataType(*args: Any, **kwargs: Any) -> Any:
        """The data type of the buffer.
        See MGeometry.dataTypeString() for a list of valid data types.
        """
        ...
    @dataType.setter
    def dataType(*args: Any, **kwargs: Any) -> Any:
        """The data type of the buffer.
        See MGeometry.dataTypeString() for a list of valid data types.
        """
        ...
    @property
    def dataTypeSize(*args: Any, **kwargs: Any) -> Any:
        """The size in bytes of the data type of the buffer."""
        ...
    @dataTypeSize.setter
    def dataTypeSize(*args: Any, **kwargs: Any) -> Any:
        """The size in bytes of the data type of the buffer."""
        ...
    @property
    def dimension(*args: Any, **kwargs: Any) -> Any:
        """The dimension of the buffer."""
        ...
    @dimension.setter
    def dimension(*args: Any, **kwargs: Any) -> Any:
        """The dimension of the buffer."""
        ...
    @property
    def name(*args: Any, **kwargs: Any) -> Any:
        """The name of the buffer.
        The buffer name is used to determine which render item this buffer belongs to.
        This name is typically set by the evaluator of the geometry.
        """
        ...
    @name.setter
    def name(*args: Any, **kwargs: Any) -> Any:
        """The name of the buffer.
        The buffer name is used to determine which render item this buffer belongs to.
        This name is typically set by the evaluator of the geometry.
        """
        ...
    @property
    def offset(*args: Any, **kwargs: Any) -> Any:
        """The offset of the vertex element in an interleaved vertex buffer.
        The value is currently only valid in the context of MPxShaderOverride.draw(), and only supported when using custom client buffers via resourceHandle(long).
        """
        ...
    @offset.setter
    def offset(*args: Any, **kwargs: Any) -> Any:
        """The offset of the vertex element in an interleaved vertex buffer.
        The value is currently only valid in the context of MPxShaderOverride.draw(), and only supported when using custom client buffers via resourceHandle(long).
        """
        ...
    @property
    def semantic(*args: Any, **kwargs: Any) -> Any:
        """The semantic of the buffer.
        See MGeometry.semanticString() for a list of valid semantic types.
        """
        ...
    @semantic.setter
    def semantic(*args: Any, **kwargs: Any) -> Any:
        """The semantic of the buffer.
        See MGeometry.semanticString() for a list of valid semantic types.
        """
        ...
    @property
    def semanticName(*args: Any, **kwargs: Any) -> Any:
        """The semantic name of the buffer.
        The semanticName is used to identify a custom vertex stream request in order to fill
        the stream with the appropriate data requested by a shader override.
        """
        ...
    @semanticName.setter
    def semanticName(*args: Any, **kwargs: Any) -> Any:
        """The semantic name of the buffer.
        The semanticName is used to identify a custom vertex stream request in order to fill
        the stream with the appropriate data requested by a shader override.
        """
        ...
    @property
    def stride(*args: Any, **kwargs: Any) -> Any:
        """The number of points per primitive."""
        ...
    @stride.setter
    def stride(*args: Any, **kwargs: Any) -> Any:
        """The number of points per primitive."""
        ...

class MVertexBufferDescriptorList(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
        ...
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
        ...
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
        ...
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
        ...
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
        ...
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
        ...
    def __getitem__(self: Self, key: Any) -> Any:
        """Return self[key]."""
        ...
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
        ...
    def __hash__(self: Self) -> Any:
        """Return hash(self)."""
        ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        ...
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
        ...
    def __len__(self: Self) -> Any:
        """Return len(self)."""
        ...
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
        ...
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
        ...
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
        ...
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
        ...
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
        ...
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
        ...
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
        ...
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
        ...
    def __str__(self: Self) -> Any:
        """Return str(self)."""
        ...
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        ...
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """append(MVertexBufferDescriptor) -> bool

        Add a descriptor to the list. Creates and stores a copy which is owned by the list.
        """
        ...
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clear() -> self

        Clear the list.
        """
        ...
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """remove(index) -> bool

        Remove a descriptor from the list and delete it.
        """
        ...

__builtins__: dict
__cached__: str
__doc__: NoneType
__file__: str
__loader__: SourceFileLoader
__name__: str
__package__: str
__spec__: ModuleSpec
key: str
ourdict: dict
py2dict: dict
val: str