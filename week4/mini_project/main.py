
"""
Week 4 Mini-Project: LLM Test Utils Runner
------------------------------------------
This script demonstrates how to use our new 'llm_test_utils' package.
It simulates a workflow:
1. Define test cases (using test_cases module)
2. Format prompts (using formatters module)
3. "Call" an LLM (simulated)
4. Validate the response (using validators module)
"""

import random
from llm_test_utils import (
    TestCaseManager, 
    format_prompt, 
    validate_not_empty, 
    validate_max_length, 
    validate_contains_keywords,
    validate_json_format
)

# -------------------------------------------------------------
# 1. Setup Test Cases (Reusing Week 2 Concept: Data Structures)
# -------------------------------------------------------------
print("--- 1. Setting up Test Cases ---")
# Week 2 taught us to organize data in lists and dictionaries.
# Here we use our TestCaseManager to keep things clean.
manager = TestCaseManager()

# Add a case for translation
manager.add_test_case(
    name="Spanish Translation",
    prompt_template="Translate '{text}' to {language}.",
    variables={"text": "Hello World", "language": "Spanish"},
    expected_keywords=["Hola"]
)

# Add a case for summarization
manager.add_test_case(
    name="Short Summary",
    prompt_template="Summarize this in under 10 words: {text}",
    variables={"text": "Python is a high-level, general-purpose programming language."},
    expected_keywords=[]
)

# Add a case for JSON output
manager.add_test_case(
    name="JSON Extractor",
    prompt_template="Extract name and age from '{text}' as JSON.",
    variables={"text": "My name is Alice and I am 30."},
    expected_keywords=["Alice", "30"]
)

# -------------------------------------------------------------
# 2. Run Tests
# -------------------------------------------------------------
print("\n--- 2. Running Tests ---")

def mock_llm_call(prompt):
    """Simulates an LLM response based on the prompt."""
    if "Spanish" in prompt:
        return "Hola Mundo"
    elif "Summarize" in prompt:
        return "Python is a general-purpose language."
    elif "JSON" in prompt:
        return '{"name": "Alice", "age": 30}'
    return "I don't understand."

# Iterate through all cases
for case in manager.get_all_cases():
    print(f"\nTesting Case: {case['name']}")
    
    # A. Format Prompt (Reusing Week 1 Concept: String Manipulation)
    try:
        # Week 1 taught us f-strings and formatting. 
        # formatters.py handles this logic now.
        prompt = format_prompt(case["template"], **case["variables"])
        print(f"  Prompt: {prompt}")
    except ValueError as e:
        print(f"  Error formatting prompt: {e}")
        continue
        
    # B. Get Response (Simulated)
    response = mock_llm_call(prompt)
    print(f"  Response: {response}")
    
    # C. Validate (Reusing Week 3 Concept: Control Flow & Logic)
    is_valid = True
    
    # Week 3 taught us to write functions that check conditions (if/else).
    # validators.py contains all these checks.
    
    # Check 1: Not Empty
    if not validate_not_empty(response):
        print("  [FAIL] Response is empty.")
        is_valid = False
        
    # Check 2: Max Length (Arbitrary limit for demo)
    if not validate_max_length(response, 100):
        print("  [FAIL] Response too long.")
        is_valid = False
        
    # Check 3: Keywords
    if case["expected_keywords"]:
        if not validate_contains_keywords(response, case["expected_keywords"]):
            print(f"  [FAIL] Missing keywords: {case['expected_keywords']}")
            is_valid = False
            
    # Check 4: JSON (only if name implies it)
    if "JSON" in case["name"]:
        if not validate_json_format(response):
            print("  [FAIL] Invalid JSON format.")
            is_valid = False
            
    if is_valid:
        print("  [PASS] All validations passed.")
    else:
        print("  [FAIL] Some validations failed.")

print("\n--- Done! ---")
