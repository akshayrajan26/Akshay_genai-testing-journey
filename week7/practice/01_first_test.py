"""
Week 7: pytest Fundamentals
Topic: First Test

How to write and run your first test in pytest.
"""

# Exercise 1: Your first test function
# TODO: Create a function named 'test_addition' that asserts 1 + 1 == 2.
# TODO: Remember that test functions MUST start with 'test_'.

# Your code here:
def test_addition():
    assert 1 + 1 == 2

# Exercise 2: Naming conventions
# TODO: Create a test function with an invalid name (e.g., 'check_subtraction').
# TODO: Run pytest and observe if it finds the test.

# Your code here:
def check_subtraction():
    assert 5 - 2 == 3

# Exercise 3: Adding a failing test
# TODO: Create a test function that purposefully fails.
# TODO: Observe the output when running pytest.

# Your code here:
def test_failing():
    assert 2 + 2 == 5
