import google.generativeai as genai

FILE_NOT_FOUND_ERR_MSG = f"Error: File containing keys not found at{keys_file_path} . Please enter a valid file path."

def get_api_key(api_name):  # test it but rewrite right after successful contact and response has been made with
                            # the api to use an environment variable instead
    keys = '../keys.txt'
    with open(keys, 'r') as keys_handle:
        for line in keys_handle:
            if line.startswith(api_name):
                api_key = line.split()[1]
                break
            else:
                continue
    return api_key


def gemini_send_prompt():
    keys = '../keys.txt'
    gemini_api_key = None
    with open(keys, 'r') as keys_handle:
        for line in keys_handle:
            if line.startswith('gemini_api'):
                gemini_api_key = line.split()[1]
                break
            else:
                continue
    return gemini_api_key


def gemini_response():
    pass


print(gemini_send_prompt())
