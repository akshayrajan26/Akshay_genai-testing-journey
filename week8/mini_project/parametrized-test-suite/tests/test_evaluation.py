import pytest

# Simulating data-driven tests for LLM prompts
@pytest.mark.parametrize("prompt,expected_in_response", [
    ("Hello AI", "Hi"),
    ("hello world", "Hi"),
    ("What is testing?", "Generated"),
])
def test_prompt_responses(mock_api_client, prompt, expected_in_response):
    """Test the mock API client with various prompts using parametrization."""
    response = mock_api_client.predict(prompt)
    assert expected_in_response in response

def test_model_config_loaded(model_config):
    """Test that the session-scoped fixture loads successfully."""
    assert model_config["model"] == "gpt-4"
    assert model_config["temperature"] == 0.7
