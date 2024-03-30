from pathlib import Path

TEXT_FILES_PATH = Path('text_files').absolute()
USER_SOLUTION_PATH = Path.joinpath(TEXT_FILES_PATH, 'user_texts/user_solution.txt')
CHATBOT_PROMPT_PATH = Path.joinpath(TEXT_FILES_PATH, 'chat_bot/prompts/optimize_solution_prompt.txt')
OPTIMIZED_SOLUTION_PATH = Path.joinpath(TEXT_FILES_PATH, 'chat_bot/gemini/responses/optimized_solution.txt')


if __name__ == '__main__':
    # pass

    print(CHATBOT_PROMPT_PATH)
    print(type(CHATBOT_PROMPT_PATH))
    print(str(CHATBOT_PROMPT_PATH))