from pathlib import Path

CURRENT_FILE = Path(__file__).absolute()
CURRENT_FILE_DIRECTORY = CURRENT_FILE.parent
TEXT_FILES_PATH = Path('text_files').absolute() # Code Review: Would this be a good idea to use?
USER_SOLUTION_PATH = Path.joinpath(CURRENT_FILE_DIRECTORY, 'user_texts/user_solution.txt')
USER_SOLUTION_PATH_2 = Path.joinpath(TEXT_FILES_PATH, 'user_texts/user_solution.txt')
OPTIMIZE_SOL_PROMPT_PATH = Path.joinpath(TEXT_FILES_PATH, 'chat_bot/prompts/optimize_solution_prompt.txt')
OPTIMIZED_SOLUTION_PATH = Path.joinpath(TEXT_FILES_PATH, 'chat_bot/gemini/responses/optimized_solution.txt')


if __name__ == '__main__':
    # pass
    # Code Review: Again, how should the below be rewritten to meet best practices?
    print(f"CURRENT FILE: {CURRENT_FILE}\n"
          f"CURRENT FILE DIRECTORY: {CURRENT_FILE_DIRECTORY}\n"
          f"TEXT_FILES_PATH: {TEXT_FILES_PATH}\n"
          f"current working directory: {Path.cwd()}\n"
          f"Prompt Path: {OPTIMIZE_SOL_PROMPT_PATH}\n"
          f"Prompt type: {type(OPTIMIZE_SOL_PROMPT_PATH)}\n"
          f"Prompt String: {str(OPTIMIZE_SOL_PROMPT_PATH)}\n")

