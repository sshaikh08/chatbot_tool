# Method 1
import tempfile
import shutil

with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
    temp_file.write("This is temporary content.")  # Write to temp file

target_file = "target.txt"
shutil.move(temp_file.name, target_file)  # Move to target file


################################################################

# Method 2

import tempfile
import os

with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
    temp_file.write("This is temporary content.")

target_file = "target.txt"
os.rename(temp_file.name, target_file)


################################################################
# Method 3
import tempfile

with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
    temp_file.write("This is temporary content.")

target_file = "target.txt"
with open(temp_file.name, 'r') as temp_in, open(target_file, 'w') as target_out:
    target_out.write(temp_in.read())  # Manually copy content
