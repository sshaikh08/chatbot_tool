from subprocess import Popen
from pathlib import Path


def open_notepad(target_file_path: Path) -> None:
    Popen(['notepad', target_file_path])


if __name__ == '__main__':
    from pathlib import Path
    from os import getcwd, chdir

    print(getcwd())

    target_directory = Path('../API_request/google_gemini')

    # chdir(target_directory)

    print(getcwd())

    optimized_solution_path_original = Path('..\\..\\text_files\\chat_bot\\prompts\\optimize_solution_prompt.txt')

    relative_path = optimized_solution_path_original.relative_to(optimized_solution_path_original.root)

    print(relative_path)
    print(optimized_solution_path_original.relative_to(optimized_solution_path_original.root))

    # open_notepad(optimized_solution_path_original)
