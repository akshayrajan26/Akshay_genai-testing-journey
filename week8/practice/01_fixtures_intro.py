"""
Week 8: pytest Advanced
Topic: Introduction to Fixtures

Fixtures are a way to provide data or setup/teardown logic to your tests.
"""

import pytest

# Exercise 1: Basic Fixture
# TODO: Create a fixture named 'sample_data' that returns a dictionary.
# TODO: Write a test that accepts 'sample_data' as an argument and asserts a value.

# Your code here:
@pytest.fixture
def sample_data():
    return {"name": "Llama", "role": "Assistant"}

def test_sample_data(sample_data):
    assert sample_data["name"] == "Llama"
# Exercise 2: Setup and Teardown
# TODO: Create a fixture that prints "Setup" before yielding a value and "Teardown" after.
#          Hint: Use 'yield' instead of 'return'.

# Your code here:
@pytest.fixture
def setup_teardown_demo():
    print("\nSetup")
    yield "Active"
    print("\nTeardown")

def test_setup_teardown(setup_teardown_demo):
    assert setup_teardown_demo == "Active"
# Exercise 3: Injecting fixtures into other fixtures
# TODO: Create a 'base_config' fixture and a 'user_config' fixture that uses 'base_config'.

# Your code here:
@pytest.fixture
def base_config():
    return {"timeout": 30}

@pytest.fixture
def user_config(base_config):
    config = base_config.copy()
    config["retry"] = 3
    return config

def test_nested_fixtures(user_config):
    assert user_config["timeout"] == 30
    assert user_config["retry"] == 3
