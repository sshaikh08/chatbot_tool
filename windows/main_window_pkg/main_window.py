from windows.all_windows_settings import window
from windows.main_window_pkg.input_elements.text_input import create_solution_txt, get_solution
from windows.main_window_pkg.input_elements.button import create_get_solution_button

from os import getcwd, chdir, path

chdir('../..')
cwd = getcwd()

FILE_NAME = 'user_solution.txt'

main_window = window

main_win_sol_txt = create_solution_txt(main_window)
main_win_sol_txt.pack()  # Create text box

GET_SOLUTION_TEXT = "Generate Solution"
BORDER_WIDTH = '5'
main_win_button = create_get_solution_button(main_window, BORDER_WIDTH,
                                             GET_SOLUTION_TEXT, lambda: get_solution(main_win_sol_txt, FILE_NAME))
main_win_button.pack()

if __name__ == '__main__':
    chdir('../..')
    cwd = getcwd()

    main_window.mainloop()
