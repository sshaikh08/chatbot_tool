from itertools import cycle
from platform import python_version
from random import randint
from threading import Thread
from time import sleep
from tkinter import Button, Label, Tk, Toplevel


def while_waiting_window(func):
    """
    Decorator that opens a popup window with an animated loading message
    while waiting for the decorated function to finish execution.
    """
    window = None
    waiting_msg = 'Response is being generated and retrieved'
    waiting_animation_values = cycle(['.  ', '.. ', '...', '   '])

    def lock_window():
        window.grab_set()
        print("Grab set!")

    def unlock_window():
        window.grab_release()
        print("Grab released!")

    def on_close():
        if window is not None:
            unlock_window()
            window.destroy()

    def check_thread_status(running_thread, waiting_label):
        if running_thread.is_alive():
            waiting_label['text'] = waiting_msg + next(waiting_animation_values)
            window.after(1000, check_thread_status, running_thread, waiting_label)
        else:
            on_close()

    def wrapper():
        nonlocal window

        if window is None:
            window = Toplevel()
            waiting_label = Label(window, text=waiting_msg)

            window_width = 500
            window_height = 200
            window_size = f'{window_width}x{window_height}'

            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()

            x = int((screen_width / 2) - (window_width / 2))
            y = int((screen_height / 2) - (window_height / 2))

            window.geometry(f"{window_size}+{x}+{y}")
            window.resizable(False, False)
            waiting_label.pack(pady=75)

            lock_window()
            window.update()

            func_thread = Thread(target=func)
            func_thread.start()

            check_thread_status(func_thread, waiting_label)

            window.mainloop()

    return wrapper


@while_waiting_window
def generate_random_num():
    """
    Simulates generating a random number by sleeping for a while, then printing the result.
    """
    sleep(7)
    random_int = randint(0, 1000)
    print(random_int)


if __name__ == '__main__':
    main_window = Tk()
    python_version_label = Label(main_window, text=f"Python v{python_version()}")
    popup_button = Button(main_window, text="Popup!", width=20, command=generate_random_num)
    exit_program_button = Button(main_window, text="Exit", width=20, command=main_window.quit)

    python_version_label.pack(padx=12, pady=12)
    popup_button.pack(padx=12, pady=12)
    exit_program_button.pack(padx=12, pady=12)

    main_window.mainloop()
