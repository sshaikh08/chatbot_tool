import tkinter as tk
import os

import tempfile
import shutil

window = tk.Tk()

# Creating the text
text = tk.Text(window, width=80, height=15)
text.pack()

print(os.getcwd())


#
# with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
#     temp_file.write("This is temporary content.")  # Write to temp file
#
# target_file = "target.txt"
# shutil.move(temp_file.name, target_file)
target_file = 'user_solution.txt'

def gettext_2(target_file):
    print(text.get(1.0, "end-1c"))

    with open('user_solution.txt', 'w+') as user_solution:
        user_solution.write(text.get(1.0, "end-1c"))
        for line in user_solution:
            print(line)

def gettext():
    print(text.get(1.0, "end-1c"))

    with open('user_solution.txt', 'w+') as user_solution:
        user_solution.write(text.get(1.0, "end-1c"))
        for line in user_solution:
            print(line)


get_button = tk.Button(window, text="Get Text", command=gettext_2)
get_button.pack()

window.mainloop()
