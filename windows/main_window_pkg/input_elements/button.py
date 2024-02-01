from tkinter import Button


def create_get_solution_button(tk_window, border_width,
                               display_name, gettext_function):
    get_button = Button(tk_window,
                        borderwidth=border_width,
                        text=display_name,
                        command=gettext_function)

    return get_button


if __name__ == '__main__':
    import text_input as ti

    from windows.all_windows_settings import window

    FILE_NAME = 'user_solution.txt'

    GET_SOLUTION_TEXT = "Generate Solution"
    BORDER_WIDTH = '5'

    test_window = window

    test_text = ti.create_solution_txt(test_window)
    test_text.pack()


    def gettext(text_box, file_name):
        print(f'{text_box.get(1.0, "end-1c")}')

        #with open('user_solution.txt', 'w+') as user_solution:
        with open(file_name, 'w+') as user_solution:
            user_solution.write(text_box.get(1.0, "end-1c"))


    #
    #
    # get_button_1 = Button(test_window,
    #                       text=GET_SOLUTION_TEXT,
    #                       command=lambda: gettext(test_text))
    # get_button_1.pack()

    # get_button_2 = create_get_solution_button(test_window,
    #                                           BORDER_WIDTH,
    #                                           GET_SOLUTION_TEXT,
    #                                           lambda: gettext(test_text, FILE_NAME))
    # get_button_2.pack()

    get_button_2 = create_get_solution_button(test_window,
                                              BORDER_WIDTH,
                                              GET_SOLUTION_TEXT,
                                              lambda: ti.get_solution(test_text, FILE_NAME))
    get_button_2.pack()

    test_window.mainloop()
