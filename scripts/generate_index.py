from pathlib import Path
from copy import copy
import sys

from yaml import load, Loader

class PageGobbler:
    def __init__(self) -> None:
        self.raw_yaml = []
        self.gobbling = False
        self.data = None

    def gobble(self, line: str) -> None:
        if line.startswith("---") and not self.gobbling:
            self.gobbling = True
            return
        
        if line.startswith("---") and self.gobbling:
            self.gobbling = False
            self.flush()
            return
        
        if self.gobbling:
            self.raw_yaml.append(line)
    
    def flush(self) -> None:
        yaml = "\n".join(self.raw_yaml)

        self.data = load(yaml, Loader)

def main(file_to_update: Path, target_dir: Path, dry_run: bool) -> None:

    if not target_dir.exists():
        # I don't raise anything as this error is "handled"
        print(f"Error: Target directory '{target_dir}' does not exist.")
        sys.exit(1)

    index_intro = []
    if file_to_update.exists():
        with file_to_update.open("r") as stream:
            for line in stream:
                # TODO: It would be nice to add some heuristic to this, so that
                # the title could be something different than this string.
                # Maybe detect the starting # + the word 'index'?
                if line.startswith("## The Index"):
                    break
                index_intro.append(line)
    
    # Walk in the dirs to regen the index
    index_line_template = "- [{title}](/{file_path}): {description}"
    index_lines = ["## The Index"]

    paths = list(target_dir.rglob("*.md"))

    if not paths:
        print("Found to matching files to index. Returning with error.")
        sys.exit(1)

    for path in paths:
        if path.name.lower() == "_index.md":
            continue
        gobbler = PageGobbler()
        with path.open("r") as stream:
            for line in stream:
                gobbler.gobble(line)
        line = copy(index_line_template)
        line = line.format(
            title = gobbler.data.get("title"),
            file_path = path,
            description = gobbler.data.get("desc", "No description provided")
        )
        index_lines.append(line)
    
    index_intro[-1] = index_intro[-1].strip()
    new_file_lines = ["".join(index_intro)]
    new_file_lines.extend(index_lines)

    if dry_run:
        print("\n".join(new_file_lines))
        return
    
    with file_to_update.open("w+") as stream:
        stream.writelines([f"{x}\n" for x in new_file_lines])



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(

    )

    parser.add_argument("index_file", type=Path, help="The file to update")
    parser.add_argument("folder", type=Path, help="The handbook path")
    parser.add_argument("-d", "--dry-run", action="store_true", help="Do not touch any files, just print out the new readme.")

    args = parser.parse_args()

    main(args.index_file, args.folder, args.dry_run)
