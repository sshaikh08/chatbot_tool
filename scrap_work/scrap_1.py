import tkinter as tk
import os

window = tk.Tk()

# Creating the text
text = tk.Text(window, width=80, height=15)

text.pack()

print(os.getcwd())


def gettext():
    print(text.get(1.0, "end-1c"))

    with open('user_solution.txt', 'w+') as user_solution:
        user_solution.write(text.get(1.0, "end-1c"))
        for line in user_solution:
            print(line)


get_button = tk.Button(window, text="Get Text", command=gettext)
get_button.pack()

window.mainloop()
