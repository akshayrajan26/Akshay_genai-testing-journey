"""
Week 7: pytest Fundamentals
Topic: Test Discovery

Organizing your tests so pytest can find them automatically.
"""

# Exercise 1: File Naming
# TODO: Create a few empty test files with names like 'test_math.py' and 'math_test.py'.
# TODO: Run 'pytest --collect-only' to see which ones are discovered.

# Your code here:
# (Run in terminal: touch test_math.py math_test.py then pytest --collect-only)

# Exercise 2: Directory Structure
# TODO: Understand the project structure where tests are kept in a 'tests/' folder.

# Your code here:
# (We will create a tests/ folder for the mini project)

# Exercise 3: Class-based tests
# TODO: Create a class 'TestMathOperations' and add a test method inside it.
#          Note: The class name must start with 'Test'.

# Your code here:
class TestMathOperations:
    def test_multiplication(self):
        assert 3 * 3 == 9
