from tkinter import Text
from pathlib import Path
from tempfile import NamedTemporaryFile
from shutil import move

from my_python_tools.read_write_operations import text_box_write_operation


def get_solution(text_box: Text, target_file: Path) -> None:
    with NamedTemporaryFile(mode='w', delete=False, encoding="utf-8") as temp_file:
        text_box_write_operation(temp_file, text_box)  # Code Review: referred to bard and it had me running circles,
        # can't seem to make pycharm happy with this

    move(temp_file.name, target_file)


def open_in_notepad():
    pass
