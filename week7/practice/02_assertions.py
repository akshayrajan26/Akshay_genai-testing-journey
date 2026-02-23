"""
Week 7: pytest Fundamentals
Topic: Assertions and Matchers

Pytest uses standard Python 'assert' statements, but provides detailed error reports.
"""
import pytest

# Exercise 1: Basic Assertions
# TODO: Write tests for equality, inequality, and list membership.

# Your code here:
def test_basic_assertions():
    assert 10 == 10
    assert 5 != 3
    assert 2 in [1, 2, 3]

# Exercise 2: Testing for Exceptions
# TODO: Use 'with pytest.raises(ZeroDivisionError):' to verify an error occurs.
#          Note: You'll need to 'import pytest'.

# Your code here:
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

# Exercise 3: String Matching
# TODO: Assert that a string contains a specific substring.
# TODO: Assert that a list has a specific length.

# Your code here:
def test_string_and_length():
    assert "pytest" in "learning pytest is fun"
    assert len([1, 2, 3]) == 3
