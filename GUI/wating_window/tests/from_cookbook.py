from tkinter import Tk, Button, Label, Toplevel
from sys import exit
from platform import python_version
from itertools import cycle
from time import sleep
from random import randint
from threading import Thread

popup_window = None


def popup():
    global popup_window

    waiting_msg = 'Response is being generated and retrieved'
    waiting_animation_values = cycle(['.  ', '.. ', '...', '   '])

    if popup_window is None:
        WINDOW_WIDTH = '500'
        WINDOW_HEIGHT = '200'
        WINDOW_SIZE = f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}'

        popup_window = Toplevel()  #Code Review: popup_window.mainloop() needs to be place somewhere in this module.
        waiting_label = Label(popup_window, text=waiting_msg)

        screen_width = popup_window.winfo_screenwidth()
        screen_height = popup_window.winfo_screenheight()

        x = int((screen_width / 2) - (int(WINDOW_WIDTH) / 2))
        y = int((screen_height / 2) - (int(WINDOW_HEIGHT) / 2))

        popup_window.geometry(f"{WINDOW_SIZE}+{x}+{y}")

        popup_window.resizable(False, False)

        def lock():
            popup_window.grab_set()
            print("Grab set!")

        def unlock():
            popup_window.grab_release()
            print("Grab released!")

        def generate_random_num():
            sleep(7)
            random_int = randint(0, 1000)
            random_int_str = str(random_int)

        def on_close():
            global popup_window
            if popup_window is not None:
                unlock()
                popup_window.destroy()  #Code Review: Pycharm is telling me off, is the way I'm doing this an issue?
                # If so, What's a better way to do this?
                popup_window = None

        def retrieve_and_generate_simulation(running_thread):
            if running_thread.is_alive():
                waiting_label['text'] = waiting_msg + next(waiting_animation_values)

                popup_window.after(1000, lambda: retrieve_and_generate_simulation(running_thread))
            else:
                on_close()

        waiting_label.pack(pady=75)

        lock()
        popup_window.update()
        generate_num_thread = Thread(target=generate_random_num)
        generate_num_thread.start()

        retrieve_and_generate_simulation(generate_num_thread)

        popup_window.mainloop()
        #Code Review Not sure how, but it's somehow running the popup window anyway. Ask Why that is.


sample_window_for_this_module = Tk()
python_version_label = Label(sample_window_for_this_module, text=f"Python v{python_version()}")
popup_button = Button(sample_window_for_this_module, text="Popup!", width=20, command=lambda: popup())
exit_program_button = Button(sample_window_for_this_module, text="Exit", width=20, command=exit)

python_version_label.pack(padx=12, pady=12)
popup_button.pack(padx=12, pady=12)
exit_program_button.pack(padx=12, pady=12)

if __name__ == '__main__':
    sample_window_for_this_module.mainloop()
