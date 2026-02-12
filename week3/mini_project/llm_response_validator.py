import json

"""
Week 3 Mini-Project: LLM Response Validator
Mastering: Control Flow, Functions, List Comprehensions, *args/**kwargs
Aligned with ROADMAP.md
"""

# Day 3: Basic Functions
def validate_json_format(text):
    """Checks if text is a valid JSON."""
    try:
        json.loads(text)
        return True
    except:
        return False

def validate_not_empty(text):
    """Checks if text is not just whitespace."""
    return len(text.strip()) > 0

def validate_max_length(text, limit):
    """Checks if text is within characters limit."""
    return len(text) <= limit

# Day 2: List Comprehensions 
def validate_contains_keywords(text, keywords):
    """
    Checks if all required keywords are present.
    Uses list comprehension for case-insensitive matching.
    """
    text_lower = text.lower()
    # List comprehension to find missing words
    missing = [kw for kw in keywords if kw.lower() not in text_lower]
    
    if missing:
        print(f"[Error]: Missing required keywords: {missing}")
        return False
    return True

def validate_no_pii(text):
    """
    Basic PII check (Personal Identifiable Information).
    Checks for common forbidden words using List Comprehension.
    """
    pii_indicators = ["email:", "phone:", "ssn:"]
    # List comprehension to find PII indicators
    found_pii = [indicator for indicator in pii_indicators if indicator in text.lower()]
    
    if found_pii:
        print(f"[Error]: Potential PII detected: {found_pii}")
        return False
    return True

# Day 4: Advanced Functions (kwargs)
def validate_response(text, **config):
    """
    Main orchestrator function using Control Flow.
    Uses **kwargs for flexible configuration.
    """
    print(f"\n--- Validating Response (Length: {len(text)}) ---")
    
    # Day 1: Control Flow (if/elif/else)
    if not validate_not_empty(text):
        print("[Error]: Response is empty!")
        return False
        
    if not validate_json_format(text):
        print("[Error]: Invalid JSON format!")
        return False
        
    limit = config.get("limit", 1000)
    if not validate_max_length(text, limit):
        print(f"[Error]: Exceeds max length of {limit}!")
        return False
        
    # Optional Keyword check
    if "keywords" in config:
        if not validate_contains_keywords(text, config["keywords"]):
            return False
            
    # Always check safety
    if not validate_no_pii(text):
        return False

    print("[Success]: All checks passed!")
    return True

# Day 4: Advanced Functions (args)
def batch_validate(*responses, **config):
    """
    Validates multiple responses at once using *args.
    """
    print(f"\nStarting Batch Validation for {len(responses)} items...")
    for i, res in enumerate(responses, 1):
        print(f"\nChecking Case #{i}:")
        validate_response(res, **config)

# Day 1: Loops and Interactive Menu
def main():
    print("=== Week 3: LLM Response Validator ===")
    
    # Default Config
    config = {
        "limit": 100,
        "keywords": ["success", "status"]
    }
    
    while True:
        print("\nEnter response to validate (or 'demo', 'quit'):")
        user_input = input("> ")
        
        if user_input.lower() == 'quit':
            break
            
        if user_input.lower() == 'demo':
            batch_validate(
                '{"status": "success", "data": "all good"}',
                '{"status": "error", "reason": "hallucination"}',
                'informal message with email: test@test.com',
                **config
            )
        else:
            validate_response(user_input, **config)

if __name__ == "__main__":
    main()
