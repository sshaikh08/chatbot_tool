from os import chdir
from pathlib import Path
from tkinter import Button, Text

from GUI.all_windows_settings import window
from GUI.main_window.input_element_funtctions.main_text_actions import create_solution_txt_box
from GUI.main_window.input_element_funtctions.main_button_actions import get_solution

FILE_NAME = Path('text_files/user_texts/user_solution.txt')

main_window = window

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
                         command=lambda: get_solution(main_win_sol_txt, FILE_NAME))

main_win_button.pack()

if __name__ == '__main__':
    chdir('../..')
    main_window.mainloop()
