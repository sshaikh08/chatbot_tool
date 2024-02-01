from windows.all_windows_settings import window
from windows.main_window_pkg.input_elements.text_input import create_solution_txt, get_solution
from windows.main_window_pkg.input_elements.button import create_get_solution_button

from os import getcwd, chdir, path

chdir('..')
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
    # ---------------------------------------------------

    # from tkinter import Button
    # from tkinter import Text
    #
    # cwd = os.getcwd()
    # print(f'Current working directory BEFORE: {cwd}')
    # os.chdir('../..')
    # target_wd = os.getcwd()
    # print(f'Current working directory AFTER: {target_wd}')
    #
    # text = Text(window, width=80, height=15)
    # text.pack()
    #
    #
    # def gettext():
    #     print(f'{main_win_sol_txt.get(1.0, "end-1c")}')
    #
    #     with open('user_solution.txt', 'w+') as user_solution:
    #         user_solution.write(main_win_sol_txt.get(1.0, "end-1c"))
    #         for line in user_solution:
    #             print(line)
    #
    #
    # get_button = Button(window, text="Get Text", command=gettext)
    # get_button.pack()
    #
    # test_window = main_window
    # test_window.mainloop()
    # ---------------------------------------------------
    # from tkinter import Button
    # from tkinter import Text
    #
    # cwd = getcwd()
    # print(f'Current working directory BEFORE: {cwd}')
    # chdir('../..')
    # target_wd = getcwd()
    # print(f'Current working directory AFTER: {target_wd}')
    #
    # # text = Text(window, width=80, height=15)
    # # text.pack()
    #
    #
    # def gettext(text_box):
    #     print(f'{text_box.get(1.0, "end-1c")}')
    #
    #     with open('user_solution.txt', 'w+') as user_solution:
    #         user_solution.write(text_box.get(1.0, "end-1c"))
    #         for line in user_solution:
    #             print(line)
    #
    #
    # get_button = Button(main_window,
    #                     text="Get Text",
    #                     command=lambda: gettext(main_win_sol_txt))
    # get_button.pack()
    #
    # test_window = main_window
    # test_window.mainloop()
    # ---------------------------------------------------

    # get_solution_button = create_get_solution_button(window,
    #                                                  get_solution,
    #                                                  main_win_sol_txt,
    #                                                  'user_solution.txt')
    # get_solution_button.pack()
    #
    # test_window = window
    # test_window.mainloop()
