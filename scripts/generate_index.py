from pathlib import Path
from copy import copy

class PageGobbler:
    def __init__(self) -> None:
        self.title = None
        self.description = None
        self.gobbled_lines = 0

    def gobble(self, line: str) -> None:
        self.gobbled_lines += 1

        if line.startswith("> ") and self.gobbled_lines == 2:
            self.description = line.lstrip(">").strip()

        if line.startswith("# ") and self.gobbled_lines == 1:
            self.title = line.lstrip("#").strip()
            return
        

def main(file_to_update: Path, handbook_dir: Path, dry_run: bool) -> None:
    
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

    for path in handbook_dir.rglob("*.md"):
        if path.name.lower() == "readme.md":
            continue
        gobbler = PageGobbler()
        with path.open("r") as stream:
            for line in stream:
                gobbler.gobble(line)
        line = copy(index_line_template)
        line = line.format(
            title = gobbler.title,
            file_path = path,
            description = gobbler.description
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
