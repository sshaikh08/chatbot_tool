from tkinter import Tk, Label, Button
from API_request.google_gemini.gemini_request import receive_write_response

if __name__ == '__main__':
    sample_window = Tk()
    Generate_solution = Label(sample_window, text=f"Fill this in with something better")
    popup_button = Button(sample_window, text="Generate Solution", width=20, command=receive_write_response)
    exit_program_button = Button(sample_window, text="Exit", width=20, command=sample_window.quit)

    Generate_solution.pack(padx=12, pady=12)
    popup_button.pack(padx=12, pady=12)
    exit_program_button.pack(padx=12, pady=12)

    sample_window.mainloop()

