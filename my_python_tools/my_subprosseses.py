from subprocess import Popen
from pathlib import Path


def open_notepad(target_file_path: Path) -> None:
    Popen(['notepad', target_file_path])
