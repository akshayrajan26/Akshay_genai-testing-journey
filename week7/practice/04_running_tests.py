"""
Week 7: pytest Fundamentals
Topic: Running and Filtering Tests

Learn how to run specific tests using markers and keyword expressions.
"""

# Exercise 1: Running by Keyword
# TODO: Use 'pytest -k "addition"' to run only tests with "addition" in their name.

# Your code here:
def test_addition_example():
    assert 10 + 5 == 15

# Exercise 2: Verbose Output
# TODO: Run tests with 'pytest -v' to see more detail.

# Your code here:
# (Run in terminal: pytest -v 04_running_tests.py)

# Exercise 3: Stopping on first failure
# TODO: Run tests with 'pytest -x' and observe the behavior when a test fails.

# Your code here:
def test_will_fail():
    assert False
