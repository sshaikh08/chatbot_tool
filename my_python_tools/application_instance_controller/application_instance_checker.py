import os.path
# Code Review this
from psutil import process_iter, Process
from pathlib import Path
from logging import error

from constants import app_cmdline_indexes as aci


# Code Review this: Potentially could use/be a decorator
def list_files_open(application_name: str) -> dict:
    global open_in_app_file_path
    application_pids = list()
    file_paths_open_in_app = list()
    files_open_in_app = list()

    app_processes = dict()

    cmdline_index = aci[application_name]

    for process_item in process_iter():
        target_process_pid = process_item.pid
        target_process = Process(target_process_pid)

        if process_item.name() == application_name:
            application_pids.append(target_process_pid)

            try:
                open_in_app_file_path = target_process.cmdline()[1]
            except IndexError:
                

            file_paths_open_in_app.append(open_in_app_file_path)

            app_processes[open_in_app_file_path] = {'pid': target_process_pid}

    return app_processes  # Code Review: How should I handle empty dictionary?


# Code Review this: I feel like a decorator could be used in this instance
def is_file_open_in_app(dict_of_open_files: dict, file_path: Path) -> bool:
    for key in dict_of_open_files.keys():
        if Path(key) == file_path:
            return True
    return False


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

    print(aci['notepad.exe'])
