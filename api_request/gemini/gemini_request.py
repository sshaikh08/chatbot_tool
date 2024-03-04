import google.generativeai as genai

from write_operations import read_txt_to_str

from os import getenv


def gemini_send_receive_prompt(*text_strings: str) -> str:
    GOOGLE_API_KEY = getenv('GOOGLE_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)

    model = 'gemini-pro'
    client = genai.GenerativeModel(model)
    response = client.generate_content("\n".join(text_strings))  # Code review: specifically
                                                                 # the ("\n".join(text_strings)

    return response.text


if __name__ == '__main__':
    from pathlib import Path

    text_files_dir = Path('../../text_files')
    prompt_txt = Path.joinpath(text_files_dir, Path('chat_bot/prompts/optimize_solution_prompt.txt'))
    user_solution_txt = Path.joinpath(text_files_dir, Path('user_texts/user_solution.txt'))

    prompt, user_solution = read_txt_to_str(prompt_txt), read_txt_to_str(user_solution_txt)

    print(user_solution_txt)
    print(prompt_txt)

    optimized_solution = gemini_send_receive_prompt(prompt, user_solution)
    print(optimized_solution)
