"""
Week 5: JSON Handling
topic: JSON Serialization and Deserialization

JSON (JavaScript Object Notation) is the standard format for API responses, 
LLM outputs, and datasets. Python makes it easy to work with.
"""

import json

# Sample data to work with
llm_response = {
    "model": "gpt-4o",
    "created_at": "2024-02-03T10:00:00Z",
    "usage": {
        "prompt_tokens": 50,
        "completion_tokens": 120,
        "total_tokens": 170
    },
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain JSON in one sentence."}
    ]
}

# -----------------------------------------------------------------------------
# Exercise 1: dumps() vs dump()
# -----------------------------------------------------------------------------
# `json.dumps()` (dump string) takes a dictionary and returns a JSON string.
# `json.dump()` (dump file) takes a dictionary and writes it to a file.

# TODO: 1. Use `json.dumps()` to convert `llm_response` to a string. 
#          Use `indent=2` for pretty printing. Store it in variables `json_str`.
# TODO: 2. Print `json_str` and its type.

# Your code here:
json_str = json.dumps(llm_response, indent=2)
print(json_str)
print(type(json_str))



# -----------------------------------------------------------------------------
# Exercise 2: Writing JSON to a file
# -----------------------------------------------------------------------------
# TODO: 1. Use `with open(...)` to create a file named "response_data.json" in write mode.
# TODO: 2. Use `json.dump()` to write `llm_response` to the file.
#          Tip: Add `indent=4` to make it readable in the file.

# Your code here:
with open("response_data.json", "w") as file:
    json.dump(llm_response, file, indent=4)



# -----------------------------------------------------------------------------
# Exercise 3: Reading JSON from a file
# -----------------------------------------------------------------------------
# TODO: 1. Use `with open(...)` to read "response_data.json".
# TODO: 2. Use `json.load()` (not loads!) to parse the file content back into a Python dictionary.
# TODO: 3. Print the value of the "model" key from the loaded data.

# Your code here:
with open("response_data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data["model"])



# -----------------------------------------------------------------------------
# Exercise 4: Handling JSON Strings (loads)
# -----------------------------------------------------------------------------
# Sometimes you get a JSON string directly from an API, not a file.
raw_api_string = '{"id": "call_123", "object": "chat.completion", "choices": []}'

# TODO: 1. Use `json.loads()` to parse `raw_api_string` into a dictionary.
# TODO: 2. Add a new key "status" with value "processed".
# TODO: 3. Print the modified dictionary.

# Your code here:
api_data = json.loads(raw_api_string)
api_data["status"] = "processed"
print(api_data)

