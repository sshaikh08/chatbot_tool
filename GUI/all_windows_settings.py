from tkinter import Tk

WINDOW_WIDTH = '3000'
WINDOW_HEIGHT = '2000'
WINDOW_SIZE = f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}'

# WINDOW_COLOR = 'grey'

window = Tk()
window.title('Chat bot tool')
# window.configure(bg=WINDOW_COLOR)


screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (int(WINDOW_WIDTH) / 2))
y = int((screen_height / 2) - (int(WINDOW_HEIGHT) / 2))

window.geometry(f"{WINDOW_SIZE}+{x}+{y}")

window.update()

window.resizable(False, False)


if __name__ == '__main__':
    window.mainloop()
