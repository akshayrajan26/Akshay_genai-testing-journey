"""Tests for test data loaders."""

def test_load_test_data():
    """Simulate loading test data."""
    dummy_data = [
        {"input": "Hi", "expected": "Hello"},
        {"input": "Bye", "expected": "Goodbye"}
    ]
    
    assert len(dummy_data) == 2
    assert dummy_data[0]["input"] == "Hi"
    
def test_loader_missing_file():
    """Simulate handling of missing file."""
    import pytest
    with pytest.raises(FileNotFoundError):
        open("non_existent_data.json", "r")
