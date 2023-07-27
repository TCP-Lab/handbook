"""Crawl the handbook and find status lines, then report them."""
from pathlib import Path
import os
from enum import Enum
from typing import Optional

class Status(Enum):
    DONE = "🟢"
    ONGOING = "🟠"
    DRAFT = "🔴"
    IDEA = "⚪"

KEYS = {
    "![draft](": Status.DRAFT,
    "![ongoing](": Status.ONGOING,
    "![complete](": Status.DONE,
    "![idea](": Status.IDEA
}

def get_file_status(path: Path) -> Optional[Status]:
    assert path.exists()
    if path.suffix != ".md":
        return None

    with path.open("r") as stream:
        for line in stream:
            for key, value in KEYS.items():
                if line.strip().lower().startswith(key):
                    return value
    
    return None

def is_file_draft(path: Path) -> bool:
    assert path.exists()
    if path.suffix != ".md":
        return False
    
    with path.open("r") as stream:
        for line in stream:
            if line.strip().lower().replace(" ", "").startswith("draft:true"):
                return True
    
    return False


def main(path: Path):
    path = path.expanduser().absolute()

    file_statuses = {}
    for root, _, files in os.walk(path):
        for filename in files:
            file_statuses[filename] = (
                get_file_status(Path(os.path.join(root, filename))),
                is_file_draft(Path(os.path.join(root, filename)))
            )
    
    for path, status in file_statuses.items():
        if not status[0]:
            continue
        
        prefix = f"👻" if status[1] else "  "
        print(f"{prefix} {status[0].value} - {path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("path", type = Path)

    args = parser.parse_args()

    main(args.path)
