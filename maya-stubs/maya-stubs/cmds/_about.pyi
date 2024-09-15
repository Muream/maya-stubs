from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def about(*, apiVersion: bool = ..., application: bool = ..., arm64: bool = ..., batch: bool = ..., buildDirectory: bool = ..., buildVariant: bool = ..., codeset: bool = ..., compositingManager: bool = ..., connected: bool = ..., creativeVersion: bool = ..., ctime: bool = ..., currentDate: bool = ..., currentTime: bool = ..., customVersion: bool = ..., customVersionClient: bool = ..., customVersionMajor: bool = ..., customVersionMinor: bool = ..., customVersionString: bool = ..., cutIdentifier: bool = ..., date: bool = ..., environmentFile: bool = ..., evalVersion: bool = ..., file: bool = ..., fontInfo: bool = ..., helpDataDirectory: bool = ..., installedVersion: bool = ..., ioVersion: bool = ..., irix: bool = ..., is64: bool = ..., languageResources: bool = ..., linux: bool = ..., linux64: bool = ..., liveUpdate: bool = ..., localizedResourceLocation: bool = ..., ltVersion: bool = ..., macOS: bool = ..., macOSASi: bool = ..., macOSppc: bool = ..., macOSx86: bool = ..., majorVersion: bool = ..., minorVersion: bool = ..., ntOS: bool = ..., operatingSystem: bool = ..., operatingSystemVersion: bool = ..., patchVersion: bool = ..., preferences: bool = ..., product: bool = ..., qtVersion: bool = ..., tablet: bool = ..., tabletMode: bool = ..., uiLanguage: bool = ..., uiLanguageForStartup: bool = ..., uiLanguageIsLocalized: bool = ..., uiLocaleLanguage: bool = ..., version: bool = ..., win64: bool = ..., windowManager: bool = ..., windows: bool = ...) -> str:
    """This command displays version information about the application if it is
    executed without flags.  If one of the above flags is specified
    then the specified version information is returned.
    Args:
        apiVersion (bool?): Returns the api version.  
                Properties: create
        application (bool?): Returns the application name string.  
                Properties: create
        arm64 (bool?): Returns true if the CPU is arm64 based.  
                Properties: create
        batch (bool?): Returns true if application is in batch mode.  
                Properties: create
        buildDirectory (bool?): Returns the build directory string.  
                Properties: create
        buildVariant (bool?): Returns the build variant string.  
                Properties: create
        codeset (bool?): Returns a string identifying the codeset (codepage) of the  
                locale that Maya is running in.  
                Example return values include "UTF-8", "ISO-8859. 1", "1252".  
                Note that the codeset values and naming conventions  
                are highly platform dependent.  They may differ in format  
                even if they have the same meaning (e.g. "utf8" vs. "UTF-8").  
                Properties: create
        compositingManager (bool?): On Linux, returns true if there is a compositing manager running; on  
                all other platforms, it always returns true.  
                Properties: create
        connected (bool?): Return whether the user is connected or not to the Internet.  
                Properties: create
        creativeVersion (bool?): Returns true if this is the Maya Creative version of the application.  
                Properties: create
        ctime (bool?): Returns the current time in the format Wed Jan 02 02. 03. 55 1980  
                Properties: create
        currentDate (bool?): Returns the current date in the format yyyy/mm/dd, e.g. 2003/05/04.  
                Properties: create
        currentTime (bool?): Returns the current time in the format hh:mm:ss, e.g. 14. 27. 53.  
                Properties: create
        customVersion (bool?): Returns true if this is a custom version of Maya.  
                Properties: create
        customVersionClient (bool?): Returns the custom client version string for Maya  
                or an empty string if this is not a custom version.  
                Properties: create
        customVersionMajor (bool?): Returns the custom major version of Maya  
                or 0 if this is not a custom version.  
                Properties: create
        customVersionMinor (bool?): Returns the custom minor version of Maya  
                or 0 if this is not a custom version.  
                Properties: create
        customVersionString (bool?): Returns the custom version string for Maya  
                or an empty string if this is not a custom version.  
                Properties: create
        cutIdentifier (bool?): Returns the cut string.  
                Properties: create
        date (bool?): Returns the build date string.  
                Properties: create
        environmentFile (bool?): Returns the location of the application defaults file.  
                Properties: create
        evalVersion (bool?): This flag is now deprecated. Always returns false, as the eval version is no longer supported.  
                Properties: create
        file (bool?): Returns the file version string.  
                Properties: create
        fontInfo (bool?): Returns a string of the specifications of the  
                fonts requested, and the specifications of the  
                fonts that are actually being used.  
                Properties: create
        helpDataDirectory (bool?): Returns the help data directory.  
                Properties: create
        installedVersion (bool?): Returns the product version string.  
                Properties: create
        ioVersion (bool?): Returns true if this is the Maya IO version of the application.  
                Properties: create
        irix (bool?): Returns true if the operating system is Irix.  
                Always false with support for Irix removed.  
                Properties: create
        is64 (bool?): Returns true if the application is 64 bit.  
                Properties: create
        languageResources (bool?): Returns a string array of the currently installed language resources.  
                Each string entry consists of three elements delimited with a colon (':').  
                The first token is the locale code (ISO 639. 1 language code followed by ISO 3166. 1 country code).  The second token is the language name in English.  
                This third token is the alpha-3 code (ISO 639. 2).  For example English is  
                represented as "en_US:English:enu".  
                Properties: create
        linux (bool?): Returns true if the operating system is Linux.  
                Properties: create
        linux64 (bool?): Returns true if the operating system is Linux 64 bit.  
                Properties: create
        liveUpdate (bool?): This flag is deprecated(2019) and may be removed in future releases of Maya.  
                Returns Autodesk formatted product information.  
                Properties: create
        localizedResourceLocation (bool?): Returns the path to the top level of the localized resource  
                directory, if we are running in an alternate language.  
                Returns an empty string if we are running in the default  
                language.  
                Properties: create
        ltVersion (bool?): Deprecated.  
                Returns true if this is the Maya LT version of the application.  
                Properties: create
        macOS (bool?): Returns true if the operating system is Macintosh.  
                Properties: create
        macOSASi (bool?): Returns true if the operating system is an Apple Silicon Mac.  
                Properties: create
        macOSppc (bool?): Returns true if the operating system is a PowerPC Macintosh.  
                Properties: create
        macOSx86 (bool?): Returns true if the operating system is an Intel Macintosh.  
                Properties: create
        majorVersion (bool?): Returns the major version of Maya.  
                Properties: create
        minorVersion (bool?): Returns the minor version of Maya.  
                Properties: create
        ntOS (bool?): Returns true if the operating system is Windows.  
                Properties: create
        operatingSystem (bool?): Returns the operating system type. Valid return types are  
                "nt", "win64", "mac", "linux" and "linux64"  
                Properties: create
        operatingSystemVersion (bool?): Returns the operating system version.  
                on Linux this returns the equivalent of uname -srvm  
                Properties: create
        patchVersion (bool?): Returns the patch version of Maya.  
                Properties: create
        preferences (bool?): Returns the location of the preferences directory.  
                Properties: create
        product (bool?): Returns the license product name.  
                Properties: create
        qtVersion (bool?): Returns Qt version string.  
                Properties: create
        tablet (bool?): Windows only.  Returns true if the PC is a Tablet PC.  
                Properties: create
        tabletMode (bool?): Windows 8 (and above) only.  If your device is a Tablet PC, then the convertible  
                mode the device is currently running in.  Returns  either: tablet or laptop (keyboard attached).  
                See the tablet flag.  
                Properties: create
        uiLanguage (bool?): Returns the language that Maya's running in.  Example return  
                values include "en_US" for English and "ja_JP" for Japanese.  
                Properties: create
        uiLanguageForStartup (bool?): Returns the language that is used for Maya's next start up.  
                This is read from config file and is rewritten after setting  
                ui language in preference.  
                Properties: create
        uiLanguageIsLocalized (bool?): Returns true if we are running in an alternate  
                language, not the default (English).  
                Properties: create
        uiLocaleLanguage (bool?): Returns the language locale of the OS. English is default.  
                Properties: create
        version (bool?): Returns the version string.  
                Properties: create
        win64 (bool?): Returns true if the operating system is Windows x64 based.  
                Properties: create
        windowManager (bool?): Returns the name of the Window Manager that is  
                assumed to be running.  
                Properties: create
        windows (bool?): Returns true if the operating system is Windows based.  
                Properties: create

    Returns:
        str: The application's version information.

    Example:
    """

