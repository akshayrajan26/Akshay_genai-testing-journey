"""
Week 8: pytest Advanced
Topic: Fixture Scopes

Understanding how often a fixture is executed (function, class, module, session).
"""

import pytest

# Exercise 1: Function Scope (Default)
# TODO: Create a fixture with scope="function" and a counter.
# TODO: Write two tests and observe if the counter resets.

# Your code here:
counter = 0

@pytest.fixture(scope="function")
def function_counter():
    global counter
    counter += 1
    return counter

def test_counter_one(function_counter):
    assert function_counter > 0

def test_counter_two(function_counter):
    # It resets (increments) every function call
    assert function_counter > 1
# Exercise 2: Module Scope
# TODO: Create a fixture with scope="module" and a database connection simulation.
# TODO: Observe that it only runs once for all tests in the file.

# Your code here:
@pytest.fixture(scope="module")
def module_db():
    print("\nConnecting to DB (Module Scope)...")
    yield "DB_CONN"
    print("\nClosing DB (Module Scope)...")

def test_db_one(module_db):
    assert module_db == "DB_CONN"

def test_db_two(module_db):
    assert module_db == "DB_CONN"
# Exercise 3: Session Scope
# TODO: Create a fixture with scope="session". This is used for expensive setups.

# Your code here:
@pytest.fixture(scope="session")
def session_config():
    print("\nLoading heavy config (Session Scope)...")
    return {"loaded": True}

def test_config(session_config):
    assert session_config["loaded"] is True
