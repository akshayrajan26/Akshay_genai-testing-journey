"""Tests for Prompt formatters."""

class TestFormatters:
    
    def test_basic_formatting(self):
        """Test simple prompt formatting."""
        template = "Hello {name}"
        formatted = template.format(name="AI")
        assert formatted == "Hello AI"
        
    def test_missing_key_formatting_error(self):
        """Test formatting with missing keys."""
        template = "Hello {name}, your role is {role}"
        try:
            template.format(name="AI")
        except KeyError as e:
            assert 'role' in str(e)
