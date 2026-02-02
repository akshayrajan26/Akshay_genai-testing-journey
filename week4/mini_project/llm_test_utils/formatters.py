
"""
Formatters Module
-----------------
This module handles dynamic prompt creation.
It takes a template string and a dictionary of variables, then
replaces the placeholders (e.g., {{name}}) with actual values.
"""

def format_prompt(template, **kwargs):
    """
    Replaces variables in a template string with provided values.
    
    Args:
        template (str): The prompt template (e.g., "Hello {{name}}")
        **kwargs: Key-value pairs for replacement (e.g., name="Alice")
        
    Returns:
        str: The formatted prompt.
        
    Raises:
        ValueError: If a required variable is missing.
    """
    
    # 1. Check for missing variables
    # We find all words inside {{...}} and check if they exist in kwargs
    # Note: A regex would be better, but we are keeping it simple (Week 1 style)
    
    # Simple check: try to format and catch KeyErrors
    # In Python, str.format() uses {name}, but standard LLM templates often use {{name}}.
    # Let's stick to standard Python f-string style formatting for simplicity: "Hello {name}"
    
    try:
        formatted_text = template.format(**kwargs)
        return formatted_text
    except KeyError as e:
        missing_key = e.args[0]
        raise ValueError(f"Missing variable for placeholder: {missing_key}")
    except Exception as e:
        raise ValueError(f"Error formatting prompt: {str(e)}")

# Example usage (if run directly):
if __name__ == "__main__":
    t = "Translate '{text}' to {language}."
    print(format_prompt(t, text="Hello", language="Spanish"))
