"""
Practice 1: Modules Basics

Goal: Understand how to import code from other files.

Files to creating during this exercise:
1. my_math.py (You will create this)

"""

# ---------------------------------------------------------
# Step 1: Create a Helper Module
# ---------------------------------------------------------
# TODO: Create a new file in this directory called 'my_math.py'
# TODO: Inside 'my_math.py', add a function:
# def add(a, b):
#     return a + b

# ---------------------------------------------------------
# Step 2: Import and Use
# ---------------------------------------------------------
# TODO: Uncomment the lines below after creating the file

from helper.my_math import add

result = add(10, 5)
print(f"10 + 5 is: {result}")

# HINT: If you get ModuleNotFoundError, make sure my_math.py is in the SAME folder.

# ---------------------------------------------------------
# Step 3: Specific Import
# ---------------------------------------------------------
# TODO: Add a 'subtract' function to my_math.py
# TODO: Import ONLY the subtract function below

from helper.my_math import subtract
print(f"10 - 5 is: {subtract(10, 5)}")

# ---------------------------------------------------------
# Step 4: Aliasing
# ---------------------------------------------------------
# TODO: Import my_math as 'mm' and use mm.add()

from helper.my_math import add as mm
print(f"Aliased Add: {mm(20, 20)}")
