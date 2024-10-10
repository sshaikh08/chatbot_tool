from pathlib import Path
from tkinter import Button, Text

from GUI.main_window.main_windows_settings import main_window
from GUI.main_window.input_element_funtctions.main_button_actions import generate_solution_action

FILE_NAME = Path('text_files/user_texts/user_solution.txt')

# main_win_sol_txt = create_solution_txt_box(main_window)
main_win_sol_txt = Text(main_window, height=10, width=75)
main_win_sol_txt.pack()  # Create text box

#
# def create_solution_txt_box(window_name: Tk) -> Text:
#     solution_text_box = Text(window_name, height=10, width=75)

GET_SOLUTION_TEXT = "Generate Solution"
BORDER_WIDTH = '5'
main_win_button = Button(main_window,
                         borderwidth='5',
                         text=GET_SOLUTION_TEXT,
                         command=lambda: generate_solution_action(FILE_NAME, main_win_sol_txt))

main_win_button.pack()
main_window.update()

# TESTING: Checking Path

if __name__ == '__main__':
    from os import chdir

    chdir('../..')
    main_window.mainloop()
