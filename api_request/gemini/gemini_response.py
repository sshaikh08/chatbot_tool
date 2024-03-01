from gemini_request import gemini_send_prompt

import google.generativeai as genai

from pathlib import Path
from sys import exit  # Go over all The scenarios this should be used, both related and unrelated to this project
from io import StringIO
from os import getenv

gemini_response = gemini_send_prompt()

gemini_response_txt = Path('../../text_files/gemini_response.txt')


def gemini_response():
    pass


# print(gemini_send_prompt())

if __name__ == '__main__':
    # pass

    optimized_solution = gemini_send_prompt()

    print(optimized_solution)
