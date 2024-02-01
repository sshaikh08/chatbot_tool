from tkinter import Text


def create_solution_txt(window_name):
    text_in_box = Text(window_name, height=10, width=75)

    return text_in_box


def get_solution(text_box, file_name):
    with open(file_name, 'w+') as user_solution:
        user_solution.write(text_box.get(1.0, "end-1c"))

        for line in user_solution:
            print(line)
