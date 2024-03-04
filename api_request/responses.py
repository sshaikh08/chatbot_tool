from gemini.gemini_request import gemini_send_receive_prompt

from pathlib import Path





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
