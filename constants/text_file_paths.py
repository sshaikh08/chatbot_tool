from pathlib import Path

TEXT_FILES_PATH = Path('text_files')#.absolute() # Code Review: Would this be a good idea to use?
USER_SOLUTION_PATH = Path.joinpath(TEXT_FILES_PATH, '../text_files/user_texts/user_solution.txt')
OPTIMIZE_SOL_PROMPT_PATH = Path.joinpath(TEXT_FILES_PATH, '../text_files/chat_bot/prompts/optimize_solution_prompt.txt')
OPTIMIZED_SOLUTION_PATH = Path.joinpath(TEXT_FILES_PATH,
                                        '../text_files/chat_bot/gemini/responses/optimized_solution.txt')


if __name__ == '__main__':
    # pass
    # Code Review: Again, how should the below be rewritten to meet best practices?
    print(f"config.py current working directory: {Path.cwd()}")
    #print(Path.resolve())
    print(OPTIMIZE_SOL_PROMPT_PATH)
    print(type(OPTIMIZE_SOL_PROMPT_PATH))
    print(str(OPTIMIZE_SOL_PROMPT_PATH))
