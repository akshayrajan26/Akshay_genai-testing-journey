"""
Practice 5: Refactoring Challenge

Goal: Take this single file and break it into a proper package structure.

SCENARIO:
You have a script that does 3 things:
1. Loads configuration
2. Processes text
3. Save results

It's all mixed together. Your job is to separate it.
"""

# ---------------------------------------------------------
# THE MONOLITH (Bad Code)
# ---------------------------------------------------------

import json
import os

# -- Config Section --
DEFAULT_MODEL = "gpt-3.5"
MAX_TOKENS = 1000
API_KEY = "sk-..."

# -- Helper Functions --
def count_tokens(text):
    return len(text.split())

def truncate(text, limit):
    words = text.split()
    return " ".join(words[:limit])

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

# -- Main Logic --
def process_user_input(text):
    print(f"Using model: {DEFAULT_MODEL}")
    tokens = count_tokens(text)
    if tokens > MAX_TOKENS:
        print("Trimming...")
        text = truncate(text, MAX_TOKENS)
    
    result = {
        "original_length": tokens,
        "processed_text": text.upper() # Mock processing
    }
    
    save_to_json(result, "output.json")
    print("Done!")

# ---------------------------------------------------------
# YOUR MISSION:
# ---------------------------------------------------------
# 1. Create a package named 'text_processor'
# 2. Move 'DEFAULT_MODEL', 'MAX_TOKENS' to 'text_processor/config.py'
# 3. Move 'count_tokens', 'truncate' to 'text_processor/utils.py'
# 4. Move 'save_to_json' to 'text_processor/storage.py'
# 5. Create a 'main.py' that imports all these and runs 'process_user_input'

# TODO: Once done, writing the import statements below to prove it works:

# from text_processor.config import DEFAULT_MODEL
# from text_processor.utils import count_tokens
# ...
