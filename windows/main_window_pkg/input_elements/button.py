from tkinter import Tk, Button, Text
from tempfile import NamedTemporaryFile
from io import TextIOWrapper
from shutil import move
from typing import Callable
from pathlib import Path

from write_operations import text_box_write_operation


def create_get_solution_button(tk_window: Tk,
                               border_width: str,
                               display_name: str,
                               gettext_function: Callable) -> Button:

    get_button = Button(tk_window,
                        borderwidth=border_width,
                        text=display_name,
                        command=gettext_function)

    return get_button


def get_solution(text_box: Text, target_file: Path) -> None:

    with NamedTemporaryFile(mode='w', delete=False, encoding="utf-8") as temp_file:
        text_box_write_operation(temp_file, text_box) # Address this warning in code review, referred to bard and it had me running circles

    move(temp_file.name, target_file)

#
# def get_solution(text_box: Text, target_file: str) -> None:
#
#     with NamedTemporaryFile(mode='w', delete=False) as temp_file:
#         temp_file.write(text_box.get(1.0, "end-1c"))  # Write to temp file
#
#     move(temp_file.name, target_file)

