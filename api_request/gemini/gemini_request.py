import google.generativeai as genai

from pathlib import Path
from sys import exit  # The scenarios this should be used
from io import StringIO
from os import getenv

user_solution_txt = Path('user_solution.txt')

with open(user_solution_txt, 'r') as user_solution_handle:
    full_user_solution = user_solution_handle.read()            # What scope is full_user_solution in?


def gemini_send_prompt():  # This looks weird to me
    GOOGLE_API_KEY = getenv('GOOGLE_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)

    model = 'gemini-pro'
    client = genai.GenerativeModel(model)

    prompt = ("Optimize the following code for the stated homework problem which is commented out. If the problem is "
              "not stated before the solution in comments, prompt the user to resubmit the solution with the homework "
              "problem clearly stated as comments. Return the solution with comments on new or altered lines.In "
              "comments, provide a summary of the changes:\n\n")

    response = client.generate_content(prompt + full_user_solution)

    return response.text
