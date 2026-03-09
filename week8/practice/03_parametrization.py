"""
Week 8: pytest Advanced
Topic: Parametrization

Run the same test logic with different inputs and expected outputs.
"""

import pytest

# Exercise 1: Basic Parametrization
# TODO: Use @pytest.mark.parametrize to test an 'add(a, b)' function with 3 different data sets.

# Your code here:
def add(a, b):
    return a + b

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (5, 5, 10),
    (-1, 1, 0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected
# Exercise 2: Parametrizing multiple arguments
# TODO: Test a 'validate_prompt(prompt, max_len)' function with various inputs and expected boolean results.

# Your code here:
def validate_prompt(prompt, max_len):
    return len(prompt) <= max_len

@pytest.mark.parametrize("prompt,max_len,expected", [
    ("hi", 5, True),
    ("hello world", 5, False),
    ("", 10, True)
])
def test_validate_prompt(prompt, max_len, expected):
    assert validate_prompt(prompt, max_len) == expected
# Exercise 3: Fixture Parametrization
# TODO: Learn how to parametrize a fixture so that every test using it runs multiple times.

# Your code here:
@pytest.fixture(params=["gpt-3.5", "gpt-4"])
def llm_model(request):
    return request.param

def test_model_loaded(llm_model):
    assert "gpt" in llm_model
