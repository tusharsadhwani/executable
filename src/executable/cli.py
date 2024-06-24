"""CLI interface for executable."""
from __future__ import annotations

import argparse
import os.path
import sys

from executable import create_cmd, create_exe


class CLIArgs:
    python_file: str
    python_executable: str
    create_cmd: bool


def cli(argv: list[str] | None = None) -> None:
    """CLI interface."""
    parser = argparse.ArgumentParser()
    parser.add_argument("python_file")
    parser.add_argument(
        "--python-executable",
        type=os.path.abspath,
        default=sys.executable,
    )
    parser.add_argument(
        "--create-cmd",
        help="Crete a .cmd instead of .exe",
        action="store_true",
    )
    args = parser.parse_args(argv, namespace=CLIArgs)

    if args.create_cmd:
        cmd_path, script_path = create_cmd(args.python_file, args.python_executable)
        print(f"Created {cmd_path} and {script_path}")
    else:
        exe_path, script_path = create_exe(args.python_file, args.python_executable)
        print(f"Created {exe_path} and {script_path}")
