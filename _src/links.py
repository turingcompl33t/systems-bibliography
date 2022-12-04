"""
Link "further reading" with existing paper summaries.
"""

import argparse
import logging
import os
import sys
from pathlib import Path
from typing import Dict, List

# Script exit codes
EXIT_SUCCESS = 0
EXIT_FAILURE = 1

# All content directory names
DIR_NAMES = [
    "cloud-computing",
    "database-systems",
    "mlsys",
    "programming-languages",
    "storage-systems",
]

# Blacklisted filenames for index construction
BLACKLIST = ["README.md", "config.json"]

# -----------------------------------------------------------------------------
# Argument Parsing
# -----------------------------------------------------------------------------


def parse_arguments():
    """
    Parse commandline arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path", type=str, help="The path to the directory for which links are written."
    )
    parser.add_argument(
        "source",
        nargs="+",
        help="One or more source directories for link content (* = all directories.)",
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output.")
    args = parser.parse_args()

    # The repository root
    root_path = Path(args.path).parent.resolve().as_posix()

    # Limit sources to expected paths (allows for globbing with *)
    maximal = [os.path.join(root_path, dirname) for dirname in DIR_NAMES]
    sources = [os.path.abspath(path) for path in args.source]
    sources = [s for s in set(sources).intersection(set(maximal))]
    return os.path.abspath(args.path), sources, args.verbose


# -----------------------------------------------------------------------------
# Index Construction
# -----------------------------------------------------------------------------


def parse_title(path: str) -> str:
    """
    Parse the title for a Markdown file.
    :param path The path to the file
    :return The title
    """
    assert os.path.isfile(path), "Broken precondition."
    with open(path, "r") as f:
        first_line = f.readline()
        return first_line.strip("##").strip().lower()


def build_index_for(directory: str) -> Dict[str, str]:
    """
    Build an index for an individual directory.
    :param directory The path to the directory.
    :return The index
    """
    logging.info(f"Building index for {directory}...")

    index = {}
    for item in os.listdir(directory):
        if item in BLACKLIST:
            continue

        path = os.path.join(directory, item)
        if os.path.isfile(path):
            index[parse_title(path)] = path
        elif os.path.isdir(path):
            index = {**index, **build_index_for(path)}

    return index


def build_index(directories: List[str]) -> Dict[str, str]:
    """
    Build an index of {title -> path} from collection of directories.
    :param directories The collection of directories
    :return The index
    """
    index = {}
    for directory in directories:
        index = {**index, **build_index_for(directory)}
    return index


# -----------------------------------------------------------------------------
# Link Construction
# -----------------------------------------------------------------------------


def parse_title_from_link(text: str) -> str:
    """
    Parse paper title (with year) from raw text.
    :param text The raw text
    :return The parsed title
    """
    return text.strip("\n").strip("-").strip()


def rewrite(text: str, link: str, path: str) -> str:
    """
    Rewrite a title to a link.
    :param text The raw text
    :param link The link content
    :param path The path to the file in which content appears
    :return The link
    """
    # Resolve the link target
    link_target = os.path.relpath(link, Path(path).parent.resolve().as_posix())
    # Rewrite the link
    rewritten = f"- [{parse_title_from_link(text)}]({link_target})\n"

    # f-string expression cannot include backslash
    stripped_text = text.strip("\n")
    stripped_rewritten = rewritten.strip("\n")

    logging.info(f"Rewriting link from {stripped_text} to {stripped_rewritten}")
    return rewritten


def write_links_for(path: str, index: Dict[str, str]):
    """
    Write links for a single file.
    :param path The path to the target file
    :param index The index
    """
    assert os.path.isfile(path), "Broken precondition."
    logging.info(f"Writing links for {path}.")

    # Read all content
    with open(path, "r") as f:
        lines = f.readlines()

    # Isolate just the lines that contain 'links'
    try:
        begin = lines.index("### Further Reading\n")
    except ValueError as e:
        logging.warning(f"Failed to find 'Further Reading' in {path}, skipping.")
        return

    # Begin constructing the new file
    new_content = lines[: begin + 1]

    # Isolate the lines we will modify
    lines = lines[begin + 1 :]
    lines = [line for line in lines if line.strip().strip("\n") != ""]
    for line in lines:
        title = parse_title_from_link(line).lower()
        if title in index:
            new_content.append(rewrite(line, index[title], path))
        else:
            # The paper is not present, pass through
            new_content.append(line)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


def links(path: str, sources: List[str]):
    """
    Write links:
    :param path The path to the target
    :param sources The collection of sources
    """
    index = build_index(sources)

    # Locate content files and remove README.md
    markdown_files = [p.as_posix() for p in Path(path).rglob("*.md")]
    markdown_files = [p for p in markdown_files if os.path.basename(p) != "README.md"]

    # Rewrite all files with links
    for file in markdown_files:
        write_links_for(file, index)


def main() -> int:
    path, sources, verbose = parse_arguments()
    logging.basicConfig(level=logging.INFO if verbose else logging.ERROR)

    links(path, sources)

    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
