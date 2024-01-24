from tkinter import Button

GENERATE_SOLUTION_TEXT = "Generate Solution"
BORDER_WIDTH = '5'


def create_and_add_button(window):
    get_optimized_solution = Button(window,
                                    text=GENERATE_SOLUTION_TEXT,
                                    borderwidth=BORDER_WIDTH)
    get_optimized_solution.pack()
