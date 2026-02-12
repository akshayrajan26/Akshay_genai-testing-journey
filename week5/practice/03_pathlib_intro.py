"""
Week 5: Path Handling with Pathlib
topic: Modern File Paths in Python

Old Python code uses `os.path.join()`. Modern Python (3.4+) uses `pathlib`.
It makes handling file paths much easier and cross-platform (works on Mac/Windows/Linux).
"""

from pathlib import Path

# -----------------------------------------------------------------------------
# Exercise 1: Creating Paths
# -----------------------------------------------------------------------------
# TODO: 1. Create a Path object for the current directory using `Path.cwd()` (current working directory)
# TODO: 2. Print the path.
# TODO: 3. Create a Path object for the file "data.txt" inside a folder "data" relative to the current directory.
#          Hint: Use the / operator: Path("folder") / "file.txt"

# Your code here:
cwd = Path.cwd()
print(cwd)
data_file = Path("data") / "data.txt"
print(data_file)



# -----------------------------------------------------------------------------
# Exercise 2: Checking Existence
# -----------------------------------------------------------------------------
# TODO: 1. Create a Path object for "week5" (assuming you are running this from the repo root).
#          OR if running from inside week5, adjust accordingly.
# TODO: 2. Use `.exists()` to check if it exists and print the result.
# TODO: 3. Use `.is_dir()` and `.is_file()` to check what it is.

# Your code here:
week5_path = Path("week5")
print(f"Exists: {week5_path.exists()}")
print(f"Is Dir: {week5_path.is_dir()}")
print(f"Is File: {week5_path.is_file()}")



# -----------------------------------------------------------------------------
# Exercise 3: Creating Directories
# -----------------------------------------------------------------------------
# TODO: 1. Define a path for a new directory "temp_practice_output".
# TODO: 2. Use `.mkdir(exist_ok=True)` to create it. 
#          `exist_ok=True` prevents errors if it already exists.

# Your code here:
temp_dir = Path("temp_practice_output")
temp_dir.mkdir(exist_ok=True)
print(f"Created: {temp_dir}")



# -----------------------------------------------------------------------------
# Exercise 4: Reading/Writing with Pathlib
# -----------------------------------------------------------------------------
# Path objects have built-in `.read_text()` and `.write_text()` methods!
# TODO: 1. Define a path object for "temp_practice_output/hello.txt".
# TODO: 2. Use `.write_text("Hello from Pathlib!")` to write to it.
# TODO: 3. Use `.read_text()` to read it back and print the content.

# Your code here:
hello_file = temp_dir / "hello.txt"
hello_file.write_text("Hello from Pathlib!")
print(hello_file.read_text())



# -----------------------------------------------------------------------------
# Exercise 5: Listing Files (Globbing)
# -----------------------------------------------------------------------------
# TODO: 1. Use `Path.cwd().glob("*.py")` to find all Python files in the current directory.
# TODO: 2. Loop through them and print their filenames (`.name`).

# Your code here:
for py_file in Path.cwd().glob("week5/practice/*.py"):
    print(py_file.name)

