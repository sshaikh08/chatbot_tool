# get this removed
from tkinter import Button
from shutil import move

GET_SOLUTION_TEXT = "Generate Solution"
BORDER_WIDTH = '5'



def store_solution(input_text_box, file_path):
    temp_file_path = file_path + '.tmp'

    with open(temp_file_path, 'w') as user_solution:
        inp = input_text_box.get(1.0, "end-1c")
        user_solution.write(inp)


    move(temp_file_path, file_path)

    print(f'File stored successfully: {file_path}')

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
                                 command=lambda: store_solution(input_from_text_box, file_path))
    get_solution_button.pack()

    with open(file_path, 'r') as checking_file:
        for line in checking_file:
            print(line)