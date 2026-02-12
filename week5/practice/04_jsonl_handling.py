"""
Week 5: JSONL Handling
topic: Working with JSON Lines (JSONL)

JSONL = JSON Lines. Each line in the file is a valid, independent JSON object.
It is the standard format for:
- Fine-tuning datasets (OpenAI, Anthropic)
- Large datasets that don't fit in memory
- Streaming logs
"""

import json

# Sample dataset (list of dictionaries)
test_cases = [
    {"input": "Hello", "expected": "Hi there!"},
    {"input": "What is 2+2?", "expected": "4"},
    {"input": "Bye", "expected": "Goodbye!"}
]

# -----------------------------------------------------------------------------
# Exercise 1: Writing JSONL
# -----------------------------------------------------------------------------
# Unlike `json.dump`, there is no built-in `jsonl` module. We write it line by line.

# TODO: 1. Define a function `save_jsonl(data, filename)`.
# TODO: 2. Inside the function, open the file in write mode.
# TODO: 3. Loop through `data`. For each item:
#          - Convert it to a JSON string using `json.dumps()`
#          - Write it to the file followed by a newline `\n`.
# TODO: 4. Call `save_jsonl(test_cases, "test_data.jsonl")`

# Your code here:
def save_jsonl(data, filename):
    with open(filename, "w") as f:
        for item in data:
            f.write(json.dumps(item) + "\n")

save_jsonl(test_cases, "test_data.jsonl")



# -----------------------------------------------------------------------------
# Exercise 2: Reading JSONL
# -----------------------------------------------------------------------------
# TODO: 1. Define a function `load_jsonl(filename)`.
# TODO: 2. Inside, create an empty list `results`.
# TODO: 3. Open the file in read mode.
# TODO: 4. Loop through each line in the file:
#          - Skip empty lines if any (using `.strip()`).
#          - Parse the line using `json.loads()`.
#          - Append to `results`.
# TODO: 5. Return `results`.
# TODO: 6. Call the function and print the loaded data.

# Your code here:
def load_jsonl(filename):
    results = []
    with open(filename, "r") as f:
        for line in f:
            if line.strip():
                results.append(json.loads(line))
    return results

loaded_data = load_jsonl("test_data.jsonl")
print(loaded_data)



# -----------------------------------------------------------------------------
# Exercise 3: Appending to JSONL
# -----------------------------------------------------------------------------
# JSONL is great because you can append without reading the whole file!
new_entry = {"input": "Explain AI", "expected": "AI is artificial intelligence."}

# TODO: 1. Open "test_data.jsonl" in append mode ('a').
# TODO: 2. Create a JSON string from `new_entry`.
# TODO: 3. Write it with a newline.
# TODO: 4. Read the file again using your `load_jsonl` function to verify there are now 4 items.

# Your code here:
with open("test_data.jsonl", "a") as f:
    f.write(json.dumps(new_entry) + "\n")

updated_data = load_jsonl("test_data.jsonl")
print(f"Total items: {len(updated_data)}")
for item in updated_data:
    print(item)

