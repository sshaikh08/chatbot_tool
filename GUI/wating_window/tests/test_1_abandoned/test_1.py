from GUI.wating_window.waiting_window_settings import *
from GUI.wating_window.waiting_window_functions import *

from tkinter import Tk, Label, Button
from platform import python_version
from time import sleep
from random import randint
from threading import Thread

waiting_window = None


def waiting_popup():
    global waiting_window

    def generate_random_num():
        sleep(7)
        random_int = randint(0, 1000)
        random_int_str = str(random_int)

    def retrieve_and_generate_simulation(window_obj: Toplevel,
                                         top_level_label,
                                         window_msg,
                                         window_animation_values,
                                         running_thread):
        if running_thread.is_alive():
            top_level_label['text'] = window_msg + next(window_animation_values)

            window_obj.after(1000, lambda: retrieve_and_generate_simulation(window_obj,
                                                                            top_level_label,
                                                                            window_msg,
                                                                            window_animation_values,
                                                                            running_thread))
        else:
            on_close(window_obj)

    if waiting_window is None:
        waiting_window = initialized_waiting_window

        lock(waiting_window)
        waiting_window.update()
        generate_num_thread = Thread(target=generate_random_num)
        generate_num_thread.start()

        retrieve_and_generate_simulation(waiting_window,
                                         waiting_label,
                                         waiting_msg,
                                         waiting_animation_values,
                                         generate_num_thread)

        waiting_window.mainloop()


if __name__ == '__main__':
    main_window = Tk()
    python_version_label = Label(main_window, text=f"Python v{python_version()}")
    popup_button = Button(main_window, text="Popup!", width=20, command=lambda: waiting_popup())
    exit_program_button = Button(main_window, text="Exit", width=20, command=exit)

    python_version_label.pack(padx=12, pady=12)
    popup_button.pack(padx=12, pady=12)
    exit_program_button.pack(padx=12, pady=12)

    main_window.mainloop()
