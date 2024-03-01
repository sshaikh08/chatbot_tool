from windows.all_windows_settings import window
from windows.main_window_pkg.input_elements.text_input import create_solution_txt_box
from windows.main_window_pkg.input_elements.button import create_get_solution_button, get_solution

from os import chdir
from pathlib import Path

FILE_NAME = Path('text_files/user_solution.txt')

main_window = window

main_win_sol_txt = create_solution_txt_box(main_window)
main_win_sol_txt.pack()  # Create text box

GET_SOLUTION_TEXT = "Generate Solution"
BORDER_WIDTH = '5'
main_win_button = create_get_solution_button(main_window,
                                             BORDER_WIDTH,
                                             GET_SOLUTION_TEXT,
                                             lambda: get_solution(main_win_sol_txt, FILE_NAME))
main_win_button.pack()

if __name__ == '__main__':
    chdir('../..')
    main_window.mainloop()
