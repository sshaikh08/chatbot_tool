from tkinter import Toplevel, Label
from itertools import cycle

waiting_msg = 'Response is being generated and retrieved'
waiting_animation_values = cycle(['.  ', '.. ', '...', '   '])

WINDOW_WIDTH = '500'
WINDOW_HEIGHT = '200'
WINDOW_SIZE = f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}'

initialized_waiting_window = Toplevel()  #Code Review: popup_window.mainloop() needs to be place somewhere in this module.
waiting_label = Label(initialized_waiting_window, text=waiting_msg)

screen_width = initialized_waiting_window.winfo_screenwidth()
screen_height = initialized_waiting_window.winfo_screenheight()

x = int((screen_width / 2) - (int(WINDOW_WIDTH) / 2))
y = int((screen_height / 2) - (int(WINDOW_HEIGHT) / 2))

initialized_waiting_window.geometry(f"{WINDOW_SIZE}+{x}+{y}")

initialized_waiting_window.resizable(False, False)

waiting_label.pack(pady=75)



