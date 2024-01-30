# get this removed
from tkinter import Button
import tempfile
from shutil import move

import os

GET_SOLUTION_TEXT = "Generate Solution"
BORDER_WIDTH = '5'


def store_solution(input_text_box,file_path):

    # with tempfile.NamedTemporaryFile(mode='w+', delete=False) as user_solution:
    with open(file_path, 'w+') as user_solution:
        user_solution.write(input_text_box.get(1.0, "end-1c"))
        #cwd = os.getcwd()
        for line in user_solution:
            print(line)

        #temp_file_path = os.path.join(cwd,user_solution.name)
        # move(temp_file_path, file_path)

        # print(f'File stored successfully: {file_path}')

    #     for line in user_solution:
    #         print(line)
    #
    # print(f'temp_file_path: {temp_file_path}')

    #
    # print(f'file_path: {file_path}')


def retrieve_solution(window, input_from_text_box, file_path):
    get_solution_button = Button(window,
                                 text=GET_SOLUTION_TEXT,
                                 borderwidth=BORDER_WIDTH,
                                 command=store_solution(input_from_text_box, file_path))
    get_solution_button.pack()

    with open(file_path, 'r') as checking_file:
        for line in checking_file:
            print(line)





# def show_input(input_txt_box):# label):
#     inp = input_txt_box.get(1.0, "end-1c")
#     label.config(text="Provided Input: " + inp)


# def create_and_add_button(window, input_txt_box):#, label):
#
#     get_optimized_solution = Button(window,
#                                     text=GET_SOLUTION_TEXT,
#                                     borderwidth=BORDER_WIDTH)#,
#                                     #command=lambda: show_input(input_txt_box))      #, label))
#     get_optimized_solution.pack()

#if __name__ == '__main__':

