from windows.all_windows_settings import window
from windows.main_window.input_elements import solution_text_input as usi
from .input_elements.generate_optimized_solution_button import create_and_add_button

main_window = window

solution_text_box = usi.window_gets_txt_bx(main_window)

solution_text_box.pack()  # Create text box

create_and_add_button(main_window)

if __name__ == '__main__':
    from tkinter import Toplevel

    test_window = Toplevel(main_window)

    test_window.mainloop()
