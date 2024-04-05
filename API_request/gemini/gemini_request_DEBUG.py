# This first debug version of this module is just to get it to work since this module contains the problem
# code
from my_python_tools.read_write_operations import write_to_temp_first, read_txt_to_str
import google.generativeai as genai

from pathlib import Path
from os import getenv, getcwd

OPTIMIZE_SOL_PROMPT_PATH = Path('../../text_files/chat_bot/prompts/optimize_solution_prompt.txt')
USER_SOLUTION_PATH = Path('../../text_files/user_texts/user_solution.txt')
OPTIMIZED_SOL_PATH = Path('../../text_files/chat_bot/gemini/responses/optimized_solution.txt')


def receive_write_response() -> Path:
    def gemini_send_prompt(*text_strings: str) -> str:
        print(f"gemini_request, receive_write_response(), CHATBOT_PROMPT_PATH:{OPTIMIZE_SOL_PROMPT_PATH}")  # TESTING

        GOOGLE_API_KEY = getenv('GOOGLE_API_KEY')
        genai.configure(api_key=GOOGLE_API_KEY)

        model = 'gemini-pro'
        client = genai.GenerativeModel(model)
        response = client.generate_content("\n\n".join(text_strings))  # Code review: specifically
        # the ("\n".join(text_strings)

        return response.text

    prompt_string, user_solution_string = read_txt_to_str(OPTIMIZE_SOL_PROMPT_PATH), read_txt_to_str(
        USER_SOLUTION_PATH)  # Code Review: Can this be consolidated?
    # Would creating a class object be worth
    # considering for this scenario

    response_string = gemini_send_prompt(prompt_string, user_solution_string)
    # cwd = getcwd()

    write_to_temp_first(response_string, OPTIMIZED_SOL_PATH)

    return OPTIMIZED_SOL_PATH


if __name__ == '__main__':
    # pass

    #print(CHATBOT_PROMPT_PATH)

    # response_path = receive_write_response()
    # print(response_path)

    test_object = receive_write_response()

    print(test_object)

    # print(type(test_object))

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
