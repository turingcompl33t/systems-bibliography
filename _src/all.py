"""
Wrap all content generation functionality.
"""

import argparse
import glob
import logging
import os
import subprocess
import sys
from typing import List

# Script exit codes
EXIT_SUCCESS = 0
EXIT_FAILURE = 1

# The names of the directories that contain content
DIR_NAMES = [
    "ai",
    "cloud-computing",
    "database-systems",
    "mlsys",
    "programming-languages",
    "software-engineering",
    "storage-systems",
]

# The name of the source directory
SRC_DIRNAME = "_src"

# The name of the table of contents script
TOC_SCRIPT_NAME = "toc.py"

# The name of the links script
LINKS_SCRIPT_NAME = "links.py"

# -----------------------------------------------------------------------------
# Argument Parsing
# -----------------------------------------------------------------------------


def parse_arguments() -> bool:
    """
    Parse commandline arguments.
    :return verbose
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "repository_root", type=str, help="The path to the root of the repository."
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output.")
    args = parser.parse_args()
    return args.repository_root, args.verbose


# -----------------------------------------------------------------------------
# Introspection
# -----------------------------------------------------------------------------


def interpreter() -> str:
    """Return the path to the current Python interpreter."""
    return sys.executable


def resolve_script_path(repo_root: str, name: str) -> str:
    """
    Resolve the path to a script.
    :param repo_root The path to the repository root
    :param name The name of the script
    :return The path to the script
    """
    assert os.path.isdir(repo_root), "Broken precondition."
    path = os.path.join(repo_root, SRC_DIRNAME, name)
    if not os.path.isfile(path):
        raise RuntimeError(f"Failed to resolve script: {name}.")
    return path


# -----------------------------------------------------------------------------
# Table of Contents
# -----------------------------------------------------------------------------


def write_one(path: str, interpreter_path: str, script_path: str, args: List[str]):
    """
    Invoke a script on a single directory.
    :param path The path to the directory of interest
    :param interpreter_path The path to the interpreter
    :param script_path The path to the script
    :param args Additional arguments
    """
    assert os.path.isdir(path), "Broken precondition."
    logging.info(f"Invoking script {script_path} on directory {path}...")

    command = [interpreter_path, script_path, path, *args]
    logging.info(command)

    subprocess.check_call(command)


def write_all(
    repo_root: str, interpreter_path: str, script_path: str, args: List[str] = []
):
    """
    Invoke script on all directories.
    :param repo_root The root repository path
    :param interpreter_path The path to the interpreter
    :param script_path The path to the script
    :param args Additional arguments
    """
    assert os.path.isfile(interpreter_path), "Broken precondition."
    assert os.path.isfile(script_path), "Broken precondition."

    for dirname in DIR_NAMES:
        path = os.path.join(repo_root, dirname)
        write_one(path, interpreter_path, script_path, args)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


def all(repo_root: str):
    """
    Do everything.
    :param repo_root The path to the repository root
    """
    repo_root = os.path.abspath(repo_root)
    if not os.path.isdir(repo_root):
        logging.error(f"Invalid repository root: {repo_root}.")
        return EXIT_FAILURE

    # Write table of contents
    write_all(repo_root, interpreter(), resolve_script_path(repo_root, TOC_SCRIPT_NAME))

    # Write links
    write_all(
        repo_root,
        interpreter(),
        resolve_script_path(repo_root, LINKS_SCRIPT_NAME),
        [os.path.abspath(item) for item in os.listdir(repo_root) if item in DIR_NAMES],
    )


def main() -> int:
    repo_root, verbose = parse_arguments()
    logging.basicConfig(level=logging.INFO if verbose else logging.ERROR)

    all(repo_root)

    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
