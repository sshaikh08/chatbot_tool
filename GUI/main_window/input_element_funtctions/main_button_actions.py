from tkinter import Text
from pathlib import Path
from tempfile import NamedTemporaryFile
from shutil import move

from my_python_tools.read_write_operations import text_box_write_operation
from my_python_tools import my_subprosseses as my_sub


def generate_solution_action(target_file: Path, text_box: Text) -> None:
    def get_user_solution():
        with NamedTemporaryFile(mode='w', delete=False, encoding="utf-8") as temp_file:
            text_box_write_operation(temp_file,
                                     text_box)  # Code Review: referred to bard and it had me running circles,
            # can't seem to make pycharm happy with this

        move(temp_file.name, target_file)

    def send_user_solution():
        pass

    get_user_solution()




