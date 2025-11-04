import sys
import argparse
from pathlib import Path


def is_doc_valid(doc: str) -> bool:
    return "Quick help is not" not in doc


def main(cache: Path):
    import maya.standalone

    maya.standalone.initialize()

    from maya import cmds

    synopsis_cache = cache / "synopsis"
    synopsis_cache.mkdir(parents=True, exist_ok=True)

    for cmd in cmds.help("*", list=True):
        doc = cmds.help(cmd)

        if "Command Type: Command" not in doc:
            continue

        if not is_doc_valid(doc):
            try:
                getattr(cmds, cmd)()
            except Exception:
                pass
        doc = cmds.help(cmd)

        if not is_doc_valid(doc):
            continue

        synopsis = cmds.help(cmd, syntaxOnly=True).strip()

        cmd_synposis_file = synopsis_cache / f"{cmd}.txt"
        cmd_synposis_file.write_text(synopsis)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--cache",
        help="Cache Directory to output the synopsys to",
        default=".cache",
        type=Path,
    )
    args = parser.parse_args()
    main(cache=args.cache)
