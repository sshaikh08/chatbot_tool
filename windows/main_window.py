from windows.all_windows_settings import window
from .user_input_elements import user_solution_input as usi

main_window = window

solution_text_box = usi.window_gets_txt_bx(main_window)

solution_text_box.pack()  # Create text box

if __name__ == '__main__':
    main_window.mainloop()
