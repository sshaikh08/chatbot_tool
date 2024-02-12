import tempfile
import shutil
import os


# Method 1: Using shutil.copyfileobj
def transfer_method_1(temp_file, target_file):
    with open(temp_file, 'rb') as fsrc, open(target_file, 'wb') as fdst:
        shutil.copyfileobj(fsrc, fdst)


# Method 2: Using shutil.move
def transfer_method_2(temp_file, target_file):
    shutil.move(temp_file, target_file)


# Method 3: Using os.rename
def transfer_method_3(temp_file, target_file):
    os.rename(temp_file, target_file)


# Main function
def main():
    # Writing to a temporary file
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file.write("This is some sample text to be written to the temp file.")

    # Defining target file path
    target_file = "target_file.txt"

    # Transferring contents from temp file to target file using each method
    temp_file_path = temp_file.name
    transfer_method_1(temp_file_path, target_file)
    print(f"Contents transferred using Method 1")

    # Re-writing to temp file to demonstrate other methods
    with open(temp_file_path, 'w') as temp_file:
        temp_file.write("Updated text in the temp file.")

    transfer_method_2(temp_file_path, target_file)
    print(f"Contents transferred using Method 2")

    transfer_method_3(temp_file_path, target_file)
    print(f"Contents transferred using Method 3")

    # Cleaning up the temporary file
    os.remove(target_file)


if __name__ == "__main__":
    main()
