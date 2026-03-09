"""
Week 8: pytest Advanced
Topic: conftest.py and Markers

Sharing fixtures across multiple files and categorizing tests.
"""

import pytest

# Exercise 1: conftest.py
# TODO: Understand that fixtures in conftest.py are available to all files in the directory.

# Your code here:
# (Fixtures in conftest.py are automatically discovered by pytest for the entire directory)
def test_conftest_concept():
    assert True
# Exercise 2: Built-in Markers
# TODO: Use @pytest.mark.skip to skip a test.
# TODO: Use @pytest.mark.xfail for a test that is expected to fail.

# Your code here:
@pytest.mark.skip(reason="Not implemented yet")
def test_skip_me():
    assert False

@pytest.mark.xfail(reason="Known bug")
def test_expected_to_fail():
    assert 1 == 2
# Exercise 3: Custom Markers
# TODO: Create a custom marker named 'slow' and run only those tests.
#          Hint: Use 'pytest -m slow'.

# Your code here:
@pytest.mark.slow
def test_heavy_computation():
    import time
    time.sleep(0.1)
    assert True
