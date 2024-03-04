import google.generativeai as genai

from gemini_request import gemini_send_receive_prompt

from pathlib import Path
from sys import exit  # Go over all The scenarios this should be used, both related and unrelated to this project
from io import StringIO
from os import getenv




def gemini_store_response():
    pass


if __name__ == '__main__':
    pass
    gemini_response = gemini_send_receive_prompt()

    gemini_response_txt = Path('../../text_files/chat_bot/gemini/responses/optimized_solution.txt')


    # print(gemini_send_prompt())

    # optimized_solution = gemini_send_prompt()
    #
    # print(optimized_solution)
