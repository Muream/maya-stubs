from pathlib import Path
import subprocess
import site


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

    maya_install_dir = os.environ.get("MAYA_LOCATION")
    if maya_install_dir is None:
        raise RuntimeError(
            "Could not find mayapy, "
            "the environment variable `MAYA_LOCATION` is not defined. "
            "It should be set to the root of the maya install folder. "
            "Eg: `C:/Program Files/Autodesk/Maya2025`"
        )

    maya_install_dir = Path(maya_install_dir)
    if not maya_install_dir.exists():
        raise RuntimeError(
            "Could not find mayapy, "
            f"The `MAYA_LOCATION` path does not exist: `{maya_install_dir}`"
        )

    if sys.platform == "win32":
        mayapy_path = maya_install_dir / "bin" / "mayapy.exe"
    else:
        mayapy_path = maya_install_dir / "bin" / "mayapy"

    if not mayapy_path.exists():
        raise RuntimeError(f"Could not find mayapy, file does not exist: {mayapy_path}")

    subprocess.run(
        [mayapy_path, "-m", "maya_stubgen.__main__", *sys.argv[1:]],
        env={
            **os.environ,
            "PYTHONPATH": os.getcwd(),
            "MAYASTUB_VENV": ":".join(site.getsitepackages()),
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
