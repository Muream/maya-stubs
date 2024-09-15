from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def containerProxy(*args: str, edit: bool = ..., query: bool = ..., fromTemplate: str = ..., type: str = ...) -> bool:
    """Creates a new container with the same published interface, dynamic attributes
    and attribute values as the specified container but with fewer container
    members. This proxy container can be used as a reference proxy so that values
    can be set on container attributes without loading in the full container.
    The proxy container will contain one or more locator nodes. The first locator
    has dynamic attributes that serve as stand-ins for the original published
    attributes. The remaining locators serve as stand-ins for any dag nodes
    that have been published as parent or as child and will be placed at the
    world space location of the published parent/child nodes.
    The expected usage of container proxies is to serve as a reference proxy
    for a referenced container. For automated creation, export and setup
    of the proxy see the doExportContainerProxy.mel script which is
    invoked by the "Export Container Proxy" menu item.proxy, container
    Args:
        fromTemplate (str?): Specifies the name of a template file which will be used to create the new  
                container proxy. Stand-in attributes will be created and published for all  
                the numeric attributes on the proxy.  
                Properties: create
        type (str?): Specifies the type of container node to use for the proxy. This flag is only  
                valid in conjunction with the fromTemplate flag. When creating a proxy for an  
                existing container, the type created will always be identical to that of the source  
                container. The default value for this flag is 'container'.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

