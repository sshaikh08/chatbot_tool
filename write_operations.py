from typing import TextIO
from tkinter import Text
from io import TextIOWrapper
from pathlib import Path

from io import StringIO


def text_box_write_operation(handle: TextIO | TextIOWrapper, text_box: Text):
    handle.write(text_box.get(1.0, "end-1c"))


# I was going to put read operations here too in here but I found read() instead

def read_txt_to_str(txt_path: Path) -> str:
    with open(txt_path, 'r') as txt_handle:
        full_txt_str = txt_handle.read()

    return full_txt_str


