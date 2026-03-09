import pytest
import time

@pytest.mark.slow
def test_heavy_computation_simulation():
    """A placeholder test representing a heavy LLM evaluation."""
    time.sleep(0.1) # Simulate delay
    assert True

def test_fast_check():
    """A quick test that should always run."""
    assert 1 + 1 == 2
