"""
Week 5: File Handling - Text Files
topic: Reading and Writing Text Files

This practice file will help you understand how to work with basic text files in Python.
This is fundamental for logging, saving simple data, and managing configuration files.
"""

# -----------------------------------------------------------------------------
# Exercise 1: Writing to a file
# -----------------------------------------------------------------------------
# TODO: 1. Create a variable named `content` with the string "Hello, AI World!\nThis is my first file."
# TODO: 2. Open a file named "example.txt" in write mode ('w')
# TODO: 3. Write the `content` to the file
# TODO: 4. Close the file

# Your code here:

content = "Hello, AI World!\nThis is my first file."

with open("example.txt", "w") as file:
    file.write(content)




# -----------------------------------------------------------------------------
# Exercise 2: Reading from a file
# -----------------------------------------------------------------------------
# TODO: 1. Open "example.txt" in read mode ('r')
# TODO: 2. Read the entire content of the file into a variable named `read_content`
# TODO: 3. Print `read_content`
# TODO: 4. Close the file

# Your code here:

with open("example.txt", "r") as file:
    read_content = file.read()
    print(read_content)




# -----------------------------------------------------------------------------
# Exercise 3: Appending to a file
# -----------------------------------------------------------------------------
# TODO: 1. Open "example.txt" in append mode ('a')
# TODO: 2. Write "\nAppending a new line!" to the file
# TODO: 3. Close the file

# Your code here:
with open("example.txt", "a") as file:
    file.write("\nAppending a new line!")



# -----------------------------------------------------------------------------
# Exercise 4: The 'with' statement (Context Manager) - BEST PRACTICE
# -----------------------------------------------------------------------------
# It is easy to forget to close a file. The `with` statement closes it automatically.
# TODO: 1. Use the `with` statement to open "example.txt" in read mode
# TODO: 2. Loop through each line in the file and print it with line numbers (e.g., "Line 1: ...")

# Your code here:

with open("example.txt", "r") as file:
    for line_no, line in enumerate(file, start=1):
        print(f"Line {line_no}: {line}", end="")




# -----------------------------------------------------------------------------
# Exercise 5: Error Handling
# -----------------------------------------------------------------------------
# TODO: 1. Try to open a file that doesn't exist (e.g., "ghost_file.txt") in read mode
# TODO: 2. Use a try/except block to catch the `FileNotFoundError`
# TODO: 3. Print a friendly error message

# Your code here:

try:
    with open("ghost_file.txt", "r") as file:
        file.read()
except FileNotFoundError:
    print("File not found!")


