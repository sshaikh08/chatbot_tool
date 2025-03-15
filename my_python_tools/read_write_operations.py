import os
from typing import TextIO
from tkinter import Text
from io import TextIOWrapper
from pathlib import Path

from tempfile import NamedTemporaryFile
from shutil import move

from io import StringIO


def text_box_write_operation(handle: TextIO | TextIOWrapper, text_box: Text) -> None:
    handle.write(text_box.get(1.0, "end-1c"))


# I was going to put read operations here too in here but I found read() instead

def read_txt_to_str(txt_path: Path) -> str:
    absolute_path = txt_path #.resolve()
    with open(absolute_path, 'r') as txt_handle:
        full_txt_str = txt_handle.read()

    return full_txt_str


def write_to_temp_first(string_to_write: str, target_file: Path) -> None:  # , current_working_directory: str
    # os.chdir(current_working_directory)

    with NamedTemporaryFile(mode='w', delete=False, encoding="utf-8") as temp_file:
        temp_file.write(string_to_write)

    move(temp_file.name, target_file)


if __name__ == '__main__':
    from os import getcwd, chdir

    print(getcwd())

    # chdir()
