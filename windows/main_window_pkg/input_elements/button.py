from tkinter import Button
from tempfile import NamedTemporaryFile
from shutil import move
from os import remove


def create_get_solution_button(tk_window, border_width,
                               display_name, gettext_function):
    get_button = Button(tk_window,
                        borderwidth=border_width,
                        text=display_name,
                        command=gettext_function)

    return get_button


def get_solution(text_box, target_file):
    # print(f'{text_box.get(1.0, "end-1c")}')
    with NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write(text_box.get(1.0, "end-1c"))  # Write to temp file

    move(temp_file.name, target_file)
    remove(temp_file.name)

