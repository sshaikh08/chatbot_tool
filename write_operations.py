from typing import TextIO
from tkinter import Text
from io import TextIOWrapper
from io import StringIO


def text_box_write_operation(handle: TextIO | TextIOWrapper, text_box: Text):
    handle.write(text_box.get(1.0, "end-1c"))


# I was going to put read operations here too in here but I found read() instead




