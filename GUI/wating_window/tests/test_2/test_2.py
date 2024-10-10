from tkinter import Tk, Button, Label, Toplevel
from sys import exit
from platform import python_version
from itertools import cycle
from time import sleep
from random import randint
from threading import Thread

from GUI.wating_window.tests.cookbook_rewrite import popup
popup_window = None

main_window = Tk()
python_version_label = Label(main_window, text=f"Python v{python_version()}")
popup_button = Button(main_window, text="Popup!", width=20, command=lambda: popup(popup_window))
exit_program_button = Button(main_window, text="Exit", width=20, command=exit)

python_version_label.pack(padx=12, pady=12)
popup_button.pack(padx=12, pady=12)
exit_program_button.pack(padx=12, pady=12)

if __name__ == '__main__':
    main_window.mainloop()
