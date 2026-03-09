import pytest

@pytest.fixture(scope="session")
def model_config():
    """Simulates loading a global model configuration that takes time."""
    print("\n[conftest] Loading heavy model config (Session Scope)...")
    return {
        "model": "gpt-4",
        "temperature": 0.7,
        "max_tokens": 100
    }

@pytest.fixture
def mock_api_client():
    """Simulates an API client injected into tests."""
    class MockClient:
        def predict(self, prompt):
            if "hello" in prompt.lower():
                return "Hi there!"
            return "Generated response"
    return MockClient()
