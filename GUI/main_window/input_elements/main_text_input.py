from tkinter import Tk, Text


def create_solution_txt_box(window_name: Tk) -> Text:
    solution_text_box = Text(window_name, height=10, width=75)

    return solution_text_box


