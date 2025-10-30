from pathlib import Path
import subprocess
import site
from datetime import datetime


def find_maya_installation() -> Path | None:
    """Try to find a Maya installation automatically.

    Searches for Maya versions from current year + 2 down to 2023 in platform-specific default locations.
    Returns the path to the first found installation, or None if none found.
    """
    import sys

    current_year = datetime.now().year
    # Try versions from current year + 2 down to 2023 (newest first)
    for year in range(current_year + 2, 2022, -1):
        if sys.platform == "win32":
            # Windows default installation path
            maya_dir = Path(f"C:/Program Files/Autodesk/Maya{year}")
            mayapy_path = maya_dir / "bin" / "mayapy.exe"
        elif sys.platform == "darwin":
            # macOS default installation path
            maya_dir = Path(f"/Applications/Autodesk/maya{year}")
            mayapy_path = maya_dir / "Maya.app" / "Contents" / "bin" / "mayapy"
        else:
            # Linux default installation path
            maya_dir = Path(f"/usr/autodesk/maya{year}")
            mayapy_path = maya_dir / "bin" / "mayapy"

        if mayapy_path.exists():
            return maya_dir

    return None


def ensure_maya() -> bool:
    """Checks that maya modules are available, or attempts to rerun the command in a mayapy subprocess

    Returns whether or not the process is already running within maya.
    """
    try:
        import maya  # pyright: ignore[reportUnusedImport]

        return True
    except ImportError as e:
        import os
        import sys

        if os.path.basename(sys.executable).startswith("mayapy"):
            # prevent recursion
            raise RuntimeError("running with mayapy, but couldn't import maya") from e

    maya_install_dir_str = os.environ.get("MAYA_LOCATION")

    if maya_install_dir_str is None:
        # Try to find Maya automatically
        maya_install_dir = find_maya_installation()
        if maya_install_dir is None:
            raise RuntimeError(
                "Could not find mayapy. The environment variable `MAYA_LOCATION` is not defined "
                + "and no Maya installation was found in default locations.\n"
                + "Please set `MAYA_LOCATION` to the root of the maya install folder.\n"
                + "Examples:\n"
                + "  Windows: `C:/Program Files/Autodesk/Maya2026`\n"
                + "  macOS: `/Applications/Autodesk/maya2026`\n"
                + "  Linux: `/usr/autodesk/maya2026`"
            )
        print(f"Found Maya installation at: {maya_install_dir}")
    else:
        maya_install_dir = Path(maya_install_dir_str)
        if not maya_install_dir.exists():
            raise RuntimeError(
                "Could not find mayapy, "
                + f"The `MAYA_LOCATION` path does not exist: `{maya_install_dir}`"
            )

    if sys.platform == "win32":
        mayapy_path = maya_install_dir / "bin" / "mayapy.exe"
    elif sys.platform == "darwin":
        mayapy_path = maya_install_dir / "Maya.app" / "Contents" / "bin" / "mayapy"
    else:
        mayapy_path = maya_install_dir / "bin" / "mayapy"

    if not mayapy_path.exists():
        raise RuntimeError(f"Could not find mayapy, file does not exist: {mayapy_path}")

    subprocess.run(
        [mayapy_path, "-m", "maya_stubgen.__main__", *sys.argv[1:]],
        env={
            **os.environ,
            "PYTHONPATH": os.getcwd(),
            "MAYASTUB_VENV": os.pathsep.join(site.getsitepackages()),
        },
    )

    #
    return False


def main() -> None:
    if ensure_maya():
        from .cli import cli

        cli()


if __name__ == "__main__":
    main()
