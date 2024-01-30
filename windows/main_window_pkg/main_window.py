from windows.all_windows_settings import window
from windows.main_window_pkg.input_elements.solution_text_input import create_solution_txt
from windows.main_window_pkg.input_elements.generate_optimized_solution_button import \
    retrieve_solution  # create_and_add_button
import os

# os.chdir('..')
cwd = os.getcwd()

FILE_NAME = 'user_solution.txt'

FILE_PATH = os.path.join(cwd, FILE_NAME)

main_window = window

main_win_sol_txt = create_solution_txt(main_window)

main_win_sol_txt.pack()  # Create text box

text_input = create_solution_txt(main_window)

retrieve_solution(main_window, text_input, FILE_PATH)

# from tkinter import Label
# label = Label(main_window,
#               text="", justify="left")
# label.pack()

# create_and_add_button(main_window, main_win_sol_txt)  #, label)


if __name__ == '__main__':
    # label = Label(main_window,
    #               text="")
    # label.pack()
    #
    # create_and_add_button(main_window, main_win_sol_txt, label)

    # ----------------------------
    # from tkinter import Toplevel
    #
    # test_window = Toplevel(main_window_pkg)
    #
    # test_window.mainloop()

    # ----------------------------

    # from tkinter import Label, Text
    #
    # test_window = main_window
    #
    # test_txt_box = create_solution_txt(test_window)
    #
    # test_label = Label(window,
    #                    text="")
    #
    # create_and_add_button(main_window, test_txt_box, test_label)
    #
    # test_window.mainloop()
    # -----------------
    #
    test_window = main_window
    test_window.mainloop()
    # -----------------

    # print(cwd)
    # print(os.path.join(cwd, 'user_solution.txt'))
