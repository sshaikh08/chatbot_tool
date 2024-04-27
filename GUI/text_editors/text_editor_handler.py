import os.path
# Code Review this
from psutil import process_iter, Process
from os import path

notepad_pids = list()
file_paths_open_in_notepad = list()
files_open_in_notepad = list()

notepad_process = dict()

for item in process_iter():
    p = Process(item.pid)
    if item.name() == 'notepad.exe':
        # print(item)
        # print(type(p))
        notepad_pids.append(item.pid)

        open_in_notepad_file_path = p.cmdline()[1]
        open_in_notepad_file_name = path.basename(open_in_notepad_file_path)
        file_paths_open_in_notepad.append(open_in_notepad_file_path)

        notepad_process[open_in_notepad_file_name] = {'pid': item.pid}

if __name__ == '__main__':
    print(f"{file_paths_open_in_notepad}")
