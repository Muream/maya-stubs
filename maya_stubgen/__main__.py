import site
import sys
from pathlib import Path


def ensure_venv():
    current_dir = Path().resolve()
    if not (current_dir / "pyproject.toml").exists():
        raise RuntimeError("maya_stubgen must be run from the root of the repo.")

    venv_path = current_dir / ".venv"
    if not venv_path.exists():
        raise RuntimeError(
            f"No virtual environment found at {venv_path}.\n"
            "Make sure to run `poetry install` first."
        )

    site_dir = str(venv_path / "Lib" / "site-packages")
    if site_dir not in sys.path:
        site.addsitedir(site_dir)


if __name__ == "__main__":
    ensure_venv()
    from .cli import cli

    cli()
