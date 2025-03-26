import sys
from pathlib import Path


def print_path(path_name: Path = Path.cwd(), path_string: str = None) -> None:
    if path_string is not None:
        path_name = Path(path_string)

    this_python_file = sys.argv[0]
    print(f"{this_python_file}: {path_name}")

    print()


if __name__ == '__main__':
    print_path()
