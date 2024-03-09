from my_python_tools.read_write_operations import write_to_temp_first, read_txt_to_str

import google.generativeai as genai

from pathlib import Path
from os import getenv, getcwd


TEXT_FILES_PATH = Path('../../text_files')
USER_SOLUTION_PATH = Path.joinpath(TEXT_FILES_PATH, 'user_texts/user_solution.txt')
CHATBOT_PROMPT_PATH = Path.joinpath(TEXT_FILES_PATH, 'chat_bot/prompts/optimize_solution_prompt.txt')
OPTIMIZED_SOLUTION_PATH = Path.joinpath(TEXT_FILES_PATH, 'chat_bot/gemini/responses/optimized_solution.txt')


def receive_write_response():
    def gemini_send_prompt(*text_strings: str) -> str:
        GOOGLE_API_KEY = getenv('GOOGLE_API_KEY')
        genai.configure(api_key=GOOGLE_API_KEY)

        model = 'gemini-pro'
        client = genai.GenerativeModel(model)
        response = client.generate_content("\n".join(text_strings))  # Code review: specifically
        # the ("\n".join(text_strings)

        return response.text

    prompt_string, user_solution_string = read_txt_to_str(CHATBOT_PROMPT_PATH), read_txt_to_str(
        USER_SOLUTION_PATH)  # Code Review: Can this be consolidated?
    # Would creating a class object be worth
    # considering for this scenario

    response_string = gemini_send_prompt(prompt_string, user_solution_string)
    # cwd = getcwd()

    write_to_temp_first(response_string, OPTIMIZED_SOLUTION_PATH)

    return OPTIMIZED_SOLUTION_PATH


if __name__ == '__main__':
    # pass

    receive_write_response()

    # from pathlib import Path
    #
    # text_files_dir = Path('../../text_files')
    # prompt_txt = Path.joinpath(text_files_dir, Path('chat_bot/prompts/optimize_solution_prompt.txt'))
    # user_solution_txt = Path.joinpath(text_files_dir, Path('user_texts/user_solution.txt'))
    #
    # prompt, user_solution = read_txt_to_str(prompt_txt), read_txt_to_str(user_solution_txt)
    #
    # print(user_solution_txt)
    # print(prompt_txt)
    #
    # optimized_solution = gemini_send_prompt(prompt, user_solution)
    # print(optimized_solution)
