from tempfile import NamedTemporaryFile
from shutil import move
import tkinter as tk

window = tk.Tk()

# Creating the text
text = tk.Text(window, width=80, height=15)

text.pack()


def gettext(target_file):
    with NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write(text.get(1.0, "end-1c"))  # Write to temp file

    move(temp_file.name, target_file)


user_solution_txt = 'user_solution.txt'

get_button = tk.Button(window, text="Get Text", command=lambda: gettext(user_solution_txt))
get_button.pack()

window.mainloop()
