from pathlib import Path
from copy import copy
import sys

from yaml import load, Loader

import logging

logging.basicConfig(format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
log = logging.getLogger("indexer")

log.setLevel(logging.INFO)

class Abort(Exception):
    """Abort execution with user-friendly message.
    
    Like a panic, but less stressful.
    """
    pass

class PageGobbler:
    """Eat up a page line-by-line, extracting the YAML header and parse it to a dict."""
    def __init__(self) -> None:
        self.raw_yaml = []
        self.gobbling = False
        self.data = None

    def gobble(self, line: str) -> None:
        """Eat up a line.
        
        Args:
            line (str): The string to eat. 
        """
        if line.startswith("---") and not self.gobbling:
            # This is the start of a yaml block
            self.gobbling = True
            return
        
        if line.startswith("---") and self.gobbling:
            # We hit the end of the yaml block we were eating
            self.gobbling = False
            self.flush()
            return
        
        if self.gobbling:
            # This is a line in a yaml block. Store it for parsing later.
            self.raw_yaml.append(line)
    
    def flush(self) -> None:
        """Flush the internal cache of the gobbler, parsing the extracted yaml"""
        yaml = "\n".join(self.raw_yaml)
        self.raw_yaml = []
        self.data = load(yaml, Loader)

def main(file_to_update: Path, target_dir: Path, dry_run: bool) -> None:
    """Run the script, updating the _index.md file specified

    Args:
        file_to_update (Path): The index file to update.
        target_dir (Path): The directory to walk to find the files to index.
        dry_run (bool): If true, does not overwrite the target file, but prints
            the new rendering of the file and quits. Useful to debug.

    Raises:
        Abort: If the target directory does not exist.
        Abort: If there are no files to index.
    """

    if not target_dir.exists():
        raise Abort(f"Target directory '{target_dir}' does not exist.")

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
        raise Abort("Found to matching files to index. Returning with error.")

    for path in paths:
        if path.name.lower() == "_index.md":
            log.debug(f"Skipped an index file {path}")
            continue

        # Gobble this content file.
        log.info(F"Gobbling {path}...")
        gobbler = PageGobbler()
        with path.open("r") as stream:
            for line in stream:
                gobbler.gobble(line)
        
        if gobbler.data is None:
            log.warn("File was gobbled, but the yaml parsing failed. Perhaps there is no yaml block? Skipping.")
            continue

        if gobbler.data.get("draft", False):
            # This page is a draft. Do not include it.
            log.debug(f"Skipped {path} as it is marked as a draft.")
            continue
        
        log.debug(f"Indexing {path}...")
        line = copy(index_line_template)
        line = line.format(
            title = gobbler.data.get("title"),
            file_path = path,
            description = gobbler.data.get("desc", "No description provided.")
        )
        index_lines.append(line)
    
    # Get rid of the `## The Index` string
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
        prog="Handbook Index Regenerator",
        description="Script to regenerate the _index.md files in the Handbook"
    )

    parser.add_argument("index_file", type=Path, help="The file to update")
    parser.add_argument("folder", type=Path, help="The handbook path")
    parser.add_argument("-d", "--dry-run", action="store_true", help="Do not touch any files, just print out the new readme.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase verbosity.")

    args = parser.parse_args()

    try:
        if args.verbose:
            log.setLevel(logging.DEBUG)

        main(args.index_file, args.folder, args.dry_run)
    except Abort as e:
        log.error("Abort! > " + str(e))
        sys.exit(1)
