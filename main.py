# TESTING OPEN: Checking Path
import os
from my_python_tools.testing_tools import print_path

print(f"main.py, cwd: {os.getcwd()}")
print_path()
# TESTING CLOSE: COMMENT OUT OR DELETE WHEN DONE

from GUI.main_window import main_window as m_w


# from sys import exit  # Code Review: The scenarios this should be used

def main() -> None:
    m_w.main_window.mainloop()


if __name__ == '__main__':
    main()
