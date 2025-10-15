# Removed window parameter from popup() and deleted the popup_window variable
from tkinter import Tk, Button, Label, Toplevel
from sys import exit
from platform import python_version
from itertools import cycle
from time import sleep
from random import randint
from threading import Thread


def generate_random_num():
    sleep(7)
    random_int = randint(0, 1000)
    random_int_str = str(random_int)
    print(random_int_str)


def popup():
    # global popup_window

    window = None

    waiting_msg = 'Response is being generated and retrieved'
    waiting_animation_values = cycle(['.  ', '.. ', '...', '   '])

    def lock():
        window.grab_set()
        print("Grab set!")

    def unlock():
        window.grab_release()
        print("Grab released!")

    def on_close():
        if window is not None:
            unlock()
            window.destroy()
            # popup_window = None # When I was using a global popup_window

    def retrieve_and_generate_simulation(running_thread):
        if running_thread.is_alive():
            waiting_label['text'] = waiting_msg + next(waiting_animation_values)

            window.after(1000, lambda: retrieve_and_generate_simulation(running_thread))
        else:
            on_close()

    if window is None:
        WINDOW_WIDTH = '500'
        WINDOW_HEIGHT = '200'
        WINDOW_SIZE = f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}'

        window = Toplevel()  #Code Review: popup_window.mainloop() needs to be place somewhere in this module.
        waiting_label = Label(window, text=waiting_msg)

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = int((screen_width / 2) - (int(WINDOW_WIDTH) / 2))
        y = int((screen_height / 2) - (int(WINDOW_HEIGHT) / 2))

        window.geometry(f"{WINDOW_SIZE}+{x}+{y}")

        window.resizable(False, False)

        waiting_label.pack(pady=75)

        lock()
        window.update()
        generate_num_thread = Thread(target=generate_random_num)
        generate_num_thread.start()

        retrieve_and_generate_simulation(generate_num_thread)

        window.mainloop()
        #Code Review Not sure how, but it's somehow running the popup window anyway. Ask Why that is.


if __name__ == '__main__':
    test_window = Tk()
    python_version_label = Label(test_window, text=f"Python v{python_version()}")
    popup_button = Button(test_window, text="Popup!", width=20, command=lambda: popup())
    exit_program_button = Button(test_window, text="Exit", width=20, command=exit)

    python_version_label.pack(padx=12, pady=12)
    popup_button.pack(padx=12, pady=12)
    exit_program_button.pack(padx=12, pady=12)

    test_window.mainloop()
