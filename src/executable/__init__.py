"""executable - Create windows .exe files that just wrap a Python script."""
from __future__ import annotations

import os.path
import shutil


def create_exe(python_file: str, python_executable: str) -> tuple[str, str]:
    output_folder = os.path.join(".", "out")
    os.makedirs(output_folder, exist_ok=True)
    
    python_filename, _ = os.path.splitext(os.path.basename(python_file))
    exe_name = python_filename + ".exe"
    exe_path = os.path.join(output_folder, exe_name)
    script_name = python_filename + "-script.py"
    script_path = os.path.join(output_folder, script_name)
    
    cli_exe = os.path.join(os.path.dirname(__file__), "cli.exe")
    shutil.copyfile(cli_exe, exe_path)
    # prepend shebang to script
    with open(python_file) as infile, open(script_path, "w") as script:
        script.write(f"#!{python_executable}\n")
        script.write(infile.read())

    return exe_path, script_path


def create_cmd(python_file: str, python_executable: str) -> tuple[str, str]:
    output_folder = os.path.join(".", "out")
    os.makedirs(output_folder, exist_ok=True)
    
    python_filename, _ = os.path.splitext(os.path.basename(python_file))
    cmd_name = python_filename + ".cmd"
    cmd_path = os.path.join(output_folder, cmd_name)
    script_name = python_filename + "-script.py"
    script_path = os.path.join(output_folder, script_name)
    
    shutil.copyfile(python_file, script_path)

    with open(cmd_path, "w") as cmd:
        cmd.write(f"@echo off\n{python_executable} {script_path}")

    return cmd_path, script_path