from tkinter import Tk
from platform import system

macOS = 'Darwin'

WINDOW_WIDTH = '1000'
WINDOW_HEIGHT = '750'
WINDOW_SIZE = f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}'

# WINDOW_COLOR = 'grey'

main_window = Tk()
main_window.title('Chat bot tool')
# window.configure(bg=WINDOW_COLOR)


screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

x = int((screen_width / 2) - (int(WINDOW_WIDTH) / 2))
y = int((screen_height / 2) - (int(WINDOW_HEIGHT) / 2))

main_window.geometry(f"{WINDOW_SIZE}+{x}+{y}")

if system() == macOS:  # Code Review: This is a workaround to make the window generate closer to expected
    main_window.update()  # Is there a better way to deal with this? Usually this would update in the module
    # directly implementing these settings. See main_window_implementation.py for more clarity.

main_window.resizable(False, False)

if __name__ == '__main__':
    main_window.mainloop()
