from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def license(*, borrow: bool = ..., info: bool = ..., isBorrowed: bool = ..., isExported: bool = ..., isTrial: bool = ..., licenseMethod: bool = ..., productChoice: bool = ..., r: bool = ..., showBorrowInfo: bool = ..., showProductInfoDialog: bool = ..., status: bool = ..., usage: bool = ...) -> str:
    """This command displays version information about the application if it is
    executed without flags.  If one of the above flags is specified
    then the specified version information is returned.
    Args:
        borrow (bool?): This flag is obsolete and no longer supported.  
                Properties: create
        info (bool?): This flag is obsolete and no longer supported.  
                Properties: create
        isBorrowed (bool?): This flag is obsolete and no longer supported.  
                Properties: create
        isExported (bool?): This flag is obsolete and no longer supported.  
                Properties: create
        isTrial (bool?): This flag is obsolete and no longer supported.  
                Properties: create
        licenseMethod (bool?): This flag is obsolete and no longer supported.  
                Properties: create
        productChoice (bool?): This flag is obsolete and no longer supported.  
                Properties: create
        r (bool?): This flag is obsolete and no longer supported.  
                Properties: create
        showBorrowInfo (bool?): This flag is obsolete and no longer supported.  
                Properties: create
        showProductInfoDialog (bool?): Show the Product Information Dialog  
                Properties: create
        status (bool?): This flag is obsolete and no longer supported.  
                Properties: create
        usage (bool?): This flag is obsolete and no longer supported.  
                Properties: create

    Returns:
        str: The application's license information.

    Example:
    """

