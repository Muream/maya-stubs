import argparse
from pathlib import Path


def is_doc_valid(doc: str) -> bool:
    return "Quick help is not" not in doc


def is_cmd_valid(what_is: str, syntax: str) -> bool:
    return "No syntax information" not in syntax and what_is == "Command"


def main(cache: Path):
    import maya.standalone

    maya.standalone.initialize()

    from maya import cmds, mel

    synopsis_cache = cache / "synopsis"
    synopsis_cache.mkdir(parents=True, exist_ok=True)

    for cmd in cmds.help("*", list=True):
        doc = cmds.help(cmd)

        if not is_doc_valid(doc):
            try:
                getattr(cmds, cmd)()
                doc = cmds.help(cmd)
            except Exception:
                pass

        syntax = cmds.help(cmd, syntaxOnly=True).strip()
        what_is = mel.eval(f"whatIs {cmd}")
        if not is_cmd_valid(what_is, syntax):
            continue

        if is_doc_valid(doc):
            synopsis = syntax
        else:
            synopsis = f"{cmd}\nNo Flags."

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
