import sys

from psutil import process_iter, Process  # Code Review this
from pathlib import Path, PureWindowsPath
from logging import basicConfig, getLogger  # Ask ChatGPT/Gemini the most common ways/best practices to logging
# messages and using the logging module.

from constants import app_cmdline_indexes as aci

logger = getLogger(
    Path(__file__).name)  # Code Review: This was defined in list_files_open, is it appropriate to define it here
# instead


# Code Review: Potentially could use/be a decorator somewhere (don't really think this is the case anymore but ask
# anyway).
def list_files_open(
        application_name: str = 'notepad.exe') -> dict:  # Rewrite this at some point to support macos and linux
    value_missing_from_dict_err_msg = (
        f"Key \"{application_name}\" does not exist in app_cmdline_indexes dictionary. Update app_cmdline_indexes\n"
        f"dictionary in constants.py with an appropriate application .exe name and the corresponding psutil cmdline\n"
        f"list index containing the target file path.")

    application_pids = list()
    file_paths_open_in_app = list()
    # Afiles_open_in_app = list()

    app_processes = dict()

    try:
        cmdline_index = aci[application_name]
    except KeyError as e:
        basicConfig(level='DEBUG')  # RESEARCH FURTHER
        logger.error(value_missing_from_dict_err_msg)
        sys.exit()

    for process_item in process_iter():
        target_process_pid = process_item.pid
        target_process = Process(target_process_pid)

        if process_item.name() == application_name:
            application_pids.append(target_process_pid)

            open_in_app_file_path = target_process.cmdline()[cmdline_index]

            file_paths_open_in_app.append(open_in_app_file_path)

            app_processes[open_in_app_file_path] = {'pid': target_process_pid}

    return app_processes  # Code Review: How should I handle empty dictionary?


# Code Review: I feel like a decorator could be used in this instance
def is_file_open_in_app(dict_of_open_files: dict, file_path: Path) -> bool:  # Code Review: In my testing below, to get
    # the result that I want, I end up having to convert the path as a str object into a Path object for this to work.
    # This seems redundant to me. What are different ways I can approach this to get the result that I want that is less
    # redundant.
    for key in dict_of_open_files.keys():
        if Path(key) is file_path:
            return True
    return False


# Code Review: What should be down here? Should it be unit
# tests or is how I'm using it currently fine? (This is meant for all non main.py 'if __name__ == '__main__':'s).
# How would ever write unit tests for functions like these?
if __name__ == '__main__':
    # notepad = 'notepad.exe'
    #
    # files_open_in_notepad = list_files_open(notepad)
    # optimized_solution_path = Path(
    #     'C:\\Users\sshai\PycharmProjects\chatbot_tool\\text_files\chat_bot\gemini\\responses\optimized_solution.txt')
    #
    # print(files_open_in_notepad)
    #
    # is_optimized_sol_open = is_file_open_in_app(files_open_in_notepad, optimized_solution_path)
    #
    # print(is_optimized_sol_open)

    # print(aci['notepad.exe'])

    #-----------------------------------------------------------------------

    # import os
    # from sys import path
    # from pathlib import Path

    # print (__file__)
    # print (os.path.abspath(__file__))
    # print (os.path.realpath(__file__))
    # print (__loader__.name)
    # print (path[0])
    # print(Path(__file__).stem)
    # print(Path(__file__).resolve().stem)
    # print(Path(__file__).name)

    #-----------------------------------------------------------------------

    # application_name = 'this_is_a_test'

    # print((f"key value \"{application_name}\""
    #        f"Update app_cmdline_indexes dictionary in constants.py with an\n" 
    #        f"appropriate application executable name and the corresponding\n"
    #        f"psutil cmdline list index containing the target file path"))

    # -----------------------------------------------------------------------

    # print(list_files_open('notepad.exe'))
    # print(list_files_open('Code.exe'))  # Code Review: How do I write a unit test for this. Also, provide a
    # methodology/resources for approaching unit tests regardless of the type of module I'm writing

    # -----------------------------------------------------------------------
    import pathlib, os

    files_open_in_notepad = list_files_open()
    # optimized_solution_path = Path('../../text_files/chat_bot/gemini/responses/optimized_solution.txt')
    # optimized_solution_path_1 = Path('../../text_files/chat_bot/gemini/responses/optimized_solution.txt').absolute()
    # optimized_solution_path_2 = PureWindowsPath('../../text_files/chat_bot/gemini/responses/optimized_solution.txt')
    # optimized_solution_path_3 = optimized_solution_path_2.parent
    optimized_solution_path_4 = Path(
        os.path.abspath('../../text_files/chat_bot/gemini/responses/optimized_solution.txt'))

    # print(files_open_in_notepad)
    # print(optimized_solution_path)
    # print(optimized_solution_path_1)
    # print(optimized_solution_path_2)
    # print(optimized_solution_path_3)
    # print(optimized_solution_path_4)
    # print(is_file_open_in_app(files_open_in_notepad, optimized_solution_path))
    # print(is_file_open_in_app(files_open_in_notepad, optimized_solution_path_4))

    print(is_file_open_in_app(files_open_in_notepad, optimized_solution_path_4))  # Code Review: This test case is
    # the result that I was looking for. I can't get the full path without this conversion by just using
    # pathlib.Path().absolute

    # print(type(optimized_solution_path_4))
    # print(files_open_in_notepad)
