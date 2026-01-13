# 📘 Week 2: Data Structures — Lists, Dictionaries, Sets

## 🎯 Week 2 Goal
By end of this week, you will:
- Master Python's core data structures (Lists, Dictionaries, Sets, Tuples)
- Learn **basic functions** (just enough for the project)
- Build `test_data_organizer.py` — a tool to manage test case data
- Push your second deliverable to GitHub

---

## 📊 What Changed from Original Roadmap?

**Original Plan:** Required functions (Week 3) and JSON (Week 5) - same issue as Week 1!

**Fixed Plan:** 
- ✅ Added "Quick Functions Intro" on Day 3
- ✅ Simplified project to match current skill level
- ✅ No JSON or file I/O yet (that's Week 5)
- ✅ Single Python file, not a package

---

## 📅 Daily Breakdown

| Day | Focus | Time | Status |
|-----|-------|------|--------|
| **Monday** | Learn: Lists (Creation, Methods, Iteration) | 1 hr | |
| **Tuesday** | Learn: Dictionaries & Nested Structures | 1 hr | |
| **Wednesday** | Learn: Sets, Tuples + **Quick Functions Intro** | 1 hr | |
| **Thursday** | Practice: Data Structure Exercises | 1 hr | |
| **Friday** | Project: Start `test_data_organizer.py` | 1 hr | |
| **Saturday** | Project: Complete main functions | 2 hrs | |
| **Sunday** | Review, document, push to GitHub | 1 hr | |

**Total: 9 hours**

---

## Practice Files Guide

Week 2 has **FOUR practice files** building up to the mini-project:

### File 1: `practice/list_practice.py`
**Covers:** Lists (Monday)
- Creating, indexing, slicing lists
- List methods: `.append()`, `.extend()`, `.sort()`
- Iteration and comprehensions
- **Time:** 20 mins

### File 2: `practice/dict_practice.py`
**Covers:** Dictionaries (Tuesday)
- Dictionary CRUD operations
- Nested dictionaries
- Lists of dictionaries (test case pattern!)
- **Time:** 20 mins

### File 3: `practice/functions_basics.py`
**Covers:** Basic functions (Wednesday)
- Function definition and calling
- Parameters and return values
- Default parameters
- **Time:** 30 mins

### File 4: `practice/data_structures_challenge.py`
**Covers:** Integration practice (Thursday)
- Combining lists, dicts, and functions
- Real-world data manipulation
- **Time:** 1 hour

> **Note:** Unlike Week 1, Week 2's prerequisites (functions) are taught DURING the week on Day 3, not as a separate "missing" topic!

**Recommended order:**
1. Monday: List practice
2. Tuesday: Dict practice
3. Wednesday: Functions practice (after learning)
4. Thursday: Challenge (combines everything)
5. Friday-Sunday: Mini-project

---

# 📚 LEARNING TRACK

## Monday: Lists Deep Dive (1 hour)

### Why Lists Matter for AI Testing
- Test cases are stored in lists
- Batch prompts are lists of strings
- Results from multiple tests → list of dictionaries

### Watch & Learn (40 mins)
**Resource:** [Corey Schafer - Lists, Tuples, and Sets](https://www.youtube.com/watch?v=W8KRzm-HUcc)
- Focus on: **Lists section (0:00 - 15:00)**

### Key Concepts to Master
```python
# 1. Creating lists
test_prompts = ["Summarize this", "Translate this", "Analyze this"]
results = []

# 2. Adding items
results.append({"prompt": "...", "response": "..."})
results.extend([item1, item2])  # Add multiple

# 3. Accessing items
first_prompt = test_prompts[0]
last_prompt = test_prompts[-1]

# 4. Slicing
first_three = test_prompts[0:3]  # or test_prompts[:3]

# 5. Iteration
for prompt in test_prompts:
    print(f"Testing: {prompt}")

# 6. List methods
test_prompts.sort()  # Sort in place
test_prompts.reverse()  # Reverse in place
count = test_prompts.count("Summarize this")

# 7. List comprehension (preview - we'll use this later)
lengths = [len(p) for p in test_prompts]
```

### Practice Exercise (20 mins)
Create `week2/practice/list_practice.py`:

```python
# Exercise 1: Build a list of test case IDs
test_ids = ["TC001", "TC002", "TC003"]
# Add TC004 and TC005
# Print all IDs

# Exercise 2: Slice operations
prompts = ["prompt1", "prompt2", "prompt3", "prompt4", "prompt5"]
# Get first 3 prompts
# Get last 2 prompts
# Get every other prompt

# Exercise 3: Iteration
scores = [85, 92, 78, 95, 88]
# Calculate average score
# Find maximum score
# Count scores above 90

# Exercise 4: List manipulation
failed_tests = []
all_tests = ["test_A", "test_B", "test_C", "test_D"]
# If a test name contains "B" or "D", add to failed_tests
```

### Monday Checkpoint ✅
- [ ] Can create and populate lists
- [ ] Understand indexing (positive and negative)
- [ ] Can slice lists
- [ ] Can iterate over lists
- [ ] Completed all 4 exercises

---

## Tuesday: Dictionaries & Nested Structures (1 hour)

### Why Dictionaries Matter for AI Testing
- **Test cases are dictionaries:** `{"id": "TC001", "prompt": "...", "expected": "..."}`
- **API responses are dictionaries:** JSON → Python dict
- **Configuration is stored as dictionaries**

### Watch & Learn (40 mins)
**Resource:** [Corey Schafer - Dictionaries](https://www.youtube.com/watch?v=daefaLgNkw0)

### Key Concepts to Master
```python
# 1. Creating dictionaries
test_case = {
    "id": "TC001",
    "prompt": "Summarize this text",
    "expected_keywords": ["summary", "concise"],
    "priority": "high"
}

# 2. Accessing values
test_id = test_case["id"]
# Safer access (won't error if key missing):
priority = test_case.get("priority", "medium")  # default value

# 3. Adding/updating
test_case["status"] = "passed"
test_case["priority"] = "critical"  # Update existing

# 4. Checking for keys
if "status" in test_case:
    print(f"Status: {test_case['status']}")

# 5. Iterating
for key in test_case:
    print(f"{key}: {test_case[key]}")

# Better way:
for key, value in test_case.items():
    print(f"{key}: {value}")

# 6. Nested dictionaries (IMPORTANT!)
test_suite = {
    "TC001": {
        "prompt": "...",
        "result": "passed"
    },
    "TC002": {
        "prompt": "...",
        "result": "failed"
    }
}

# Access nested:
tc001_result = test_suite["TC001"]["result"]

# 7. List of dictionaries (VERY COMMON!)
all_tests = [
    {"id": "TC001", "status": "passed"},
    {"id": "TC002", "status": "failed"},
    {"id": "TC003", "status": "passed"}
]

# Filter passed tests:
passed = [test for test in all_tests if test["status"] == "passed"]
```

### Practice Exercise (20 mins)
Create `week2/practice/dict_practice.py`:

```python
# Exercise 1: Create a test case dictionary
# Create a dict with: id, prompt, expected_response, priority, tags (list)

# Exercise 2: Update and access
# Add a "result" field
# Change priority to "low"
# Safely get a field that doesn't exist

# Exercise 3: Nested dictionary
test_results = {
    "safety_tests": {
        "passed": 10,
        "failed": 2,
        "total": 12
    },
    "accuracy_tests": {
        "passed": 8,
        "failed": 4,
        "total": 12
    }
}
# Calculate overall pass rate
# Print each category's summary

# Exercise 4: List of dictionaries
test_cases = [
    {"id": "TC001", "category": "safety", "score": 95},
    {"id": "TC002", "category": "accuracy", "score": 78},
    {"id": "TC003", "category": "safety", "score": 88}
]
# Find all safety tests
# Calculate average score for safety tests
# Find the test with highest score
```

### Tuesday Checkpoint ✅
- [ ] Can create and work with dictionaries
- [ ] Understand dict methods (.get(), .items(), etc.)
- [ ] Can work with nested dictionaries
- [ ] Can work with lists of dictionaries
- [ ] Completed all 4 exercises

---

## Wednesday: Sets, Tuples + Functions Intro (1 hour)

### Part 1: Sets & Tuples (30 mins)

**Sets** - For unique values (no duplicates)
```python
# Use case: Find unique error types
errors = ["timeout", "invalid", "timeout", "crash", "invalid"]
unique_errors = set(errors)  # {'timeout', 'invalid', 'crash'}

# Set operations
failed_in_v1 = {"TC001", "TC002", "TC003"}
failed_in_v2 = {"TC002", "TC004"}

# What failed in both versions?
common_failures = failed_in_v1 & failed_in_v2  # Intersection

# What was fixed in v2?
fixed = failed_in_v1 - failed_in_v2

# What's new in v2?
new_failures = failed_in_v2 - failed_in_v1
```

**Tuples** - Immutable lists (can't change after creation)
```python
# Use case: Coordinates, fixed configurations
test_config = ("gpt-4", 0.7, 100)  # (model, temperature, max_tokens)
model, temp, max_tokens = test_config  # Unpacking
```

### Part 2: Quick Functions Intro (30 mins)

**Why now?** You need functions for the mini-project, but we'll go deeper in Week 3.

```python
# Basic function structure
def function_name(parameters):
    # Do something
    return result

# Example 1: Simple function
def get_test_count(test_list):
    return len(test_list)

# Example 2: Function with default parameter
def filter_by_status(tests, status="passed"):
    return [t for t in tests if t["status"] == status]

# Example 3: Function with multiple parameters
def create_test_case(test_id, prompt, expected):
    return {
        "id": test_id,
        "prompt": prompt,
        "expected": expected,
        "status": "pending"
    }

# Using functions:
tests = [...]
count = get_test_count(tests)
passed_tests = filter_by_status(tests, "passed")
new_test = create_test_case("TC004", "Test this", "Expected that")
```

### Practice Exercise (time permitting)
Create `week2/practice/functions_basics.py`:

```python
# Exercise 1: Write a function that counts test cases by category
def count_by_category(test_cases, category):
    # Your code here
    pass

# Exercise 2: Write a function that finds failed tests
def get_failed_tests(test_cases):
    # Your code here
    pass

# Exercise 3: Write a function to calculate pass rate
def calculate_pass_rate(test_cases):
    # Return percentage of passed tests
    pass
```

### Wednesday Checkpoint ✅
- [ ] Understand when to use sets vs lists
- [ ] Know basic set operations
- [ ] Can write simple functions
- [ ] Understand function parameters and return values

---

## Thursday: Practice Day (1 hour)

### Consolidation Exercises

Today is pure practice with what you've learned. Create `week2/practice/data_structures_challenge.py`:

```python
"""
Challenge: Build a mini test case database using only data structures
No functions yet (we'll add those in the project!)
"""

# 1. Create your data structure
test_database = []  # List of test case dictionaries

# 2. Add 5 test cases manually
# Each test case should have:
# - id (string)
# - prompt (string)
# - category (string): "safety", "accuracy", or "performance"
# - status (string): "passed", "failed", or "pending"
# - score (int): 0-100

# 3. Extract information (using comprehensions/loops)
# - Count how many tests in each category
# - Find all failed tests
# - Calculate average score
# - Find all safety tests that passed

# 4. Update data
# - Change status of test TC003 to "passed"
# - Add a new field "retries" to all tests, default 0
# - Increase score of all failed tests by 10

# 5. Analysis
# - What percentage passed?
# - Which category has the lowest pass rate?
# - List all unique statuses in the database
```

### Thursday Checkpoint ✅
- [ ] Can comfortably work with lists of dictionaries
- [ ] Can filter and transform data
- [ ] Can perform calculations on data
- [ ] Completed the challenge

---

# 🔨 MINI-PROJECT: `test_data_organizer.py`

## Friday-Sunday: Build Your Test Case Manager

### Project Overview
**What you're building:** A single Python script to manage test case data for LLM testing.

**Scope (Simplified from original):**
- ✅ Store test cases in a list of dictionaries (no files yet!)
- ✅ Add, search, filter test cases using functions
- ✅ Display statistics
- ❌ NO JSON export/import (Week 5)
- ❌ NO CLI framework (just simple menu)
- ❌ NO package structure (just one .py file)

### Project Structure
```
week2/mini_project/
└── test_data_organizer.py  # Everything in one file!
```

### Starter Template
```python
"""
Test Data Organizer
A simple tool to manage LLM test cases using Python data structures.

Week 2 Mini-Project: GenAI Testing Journey
"""

# Global data storage (we'll learn better ways later!)
test_cases = []

# ============================================================================
# CORE FUNCTIONS
# ============================================================================

def add_test_case(test_id, prompt, category, priority="medium"):
    """Add a new test case to the database."""
    test_case = {
        "id": test_id,
        "prompt": prompt,
        "category": category,
        "priority": priority,
        "status": "pending",
        "score": None
    }
    test_cases.append(test_case)
    print(f"✅ Added test case: {test_id}")

def get_all_test_cases():
    """Return all test cases."""
    return test_cases

def get_test_by_id(test_id):
    """Find and return a specific test case by ID."""
    # Your code here
    pass

def update_test_status(test_id, status, score=None):
    """Update the status and optionally score of a test case."""
    # Your code here
    pass

def filter_by_category(category):
    """Return all test cases in a specific category."""
    # Your code here
    pass

def filter_by_status(status):
    """Return all test cases with a specific status."""
    # Your code here
    pass

def get_statistics():
    """Calculate and return statistics about the test cases."""
    if not test_cases:
        return "No test cases yet!"
    
    total = len(test_cases)
    # Calculate:
    # - Number passed, failed, pending
    # - Pass rate
    # - Average score (for completed tests)
    # - Breakdown by category
    
    # Your code here
    pass

# ============================================================================
# DISPLAY FUNCTIONS
# ============================================================================

def display_test_case(test_case):
    """Pretty print a single test case."""
    print(f"\n{'='*60}")
    print(f"ID: {test_case['id']}")
    print(f"Prompt: {test_case['prompt']}")
    print(f"Category: {test_case['category']}")
    print(f"Priority: {test_case['priority']}")
    print(f"Status: {test_case['status']}")
    if test_case['score'] is not None:
        print(f"Score: {test_case['score']}/100")
    print(f"{'='*60}\n")

def display_all_tests():
    """Display all test cases."""
    if not test_cases:
        print("No test cases found.")
        return
    
    print(f"\n📊 Total Test Cases: {len(test_cases)}\n")
    for test_case in test_cases:
        display_test_case(test_case)

# ============================================================================
# MENU SYSTEM
# ============================================================================

def show_menu():
    """Display the main menu."""
    print("\n" + "="*60)
    print("🧪 TEST DATA ORGANIZER")
    print("="*60)
    print("1. Add new test case")
    print("2. View all test cases")
    print("3. Search by ID")
    print("4. Filter by category")
    print("5. Filter by status")
    print("6. Update test status")
    print("7. View statistics")
    print("8. Exit")
    print("="*60)

def main():
    """Main program loop."""
    print("Welcome to Test Data Organizer!")
    
    # Add some sample data for testing
    add_test_case("TC001", "Test safety features", "safety", "high")
    add_test_case("TC002", "Test accuracy of responses", "accuracy", "medium")
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == "1":
            # Get input and add test case
            test_id = input("Test ID: ")
            prompt = input("Prompt: ")
            category = input("Category: ")
            priority = input("Priority (low/medium/high): ") or "medium"
            add_test_case(test_id, prompt, category, priority)
        
        elif choice == "2":
            display_all_tests()
        
        elif choice == "3":
            test_id = input("Enter test ID: ")
            test_case = get_test_by_id(test_id)
            if test_case:
                display_test_case(test_case)
            else:
                print(f"❌ Test case {test_id} not found.")
        
        elif choice == "4":
            category = input("Enter category: ")
            results = filter_by_category(category)
            print(f"\n📋 Found {len(results)} test(s) in category '{category}':")
            for test in results:
                display_test_case(test)
        
        elif choice == "5":
            status = input("Enter status (passed/failed/pending): ")
            results = filter_by_status(status)
            print(f"\n📋 Found {len(results)} test(s) with status '{status}':")
            for test in results:
                display_test_case(test)
        
        elif choice == "6":
            test_id = input("Test ID to update: ")
            status = input("New status (passed/failed/pending): ")
            score_input = input("Score (0-100, or press Enter to skip): ")
            score = int(score_input) if score_input else None
            update_test_status(test_id, status, score)
        
        elif choice == "7":
            stats = get_statistics()
            print(f"\n📊 TEST STATISTICS:\n{stats}")
        
        elif choice == "8":
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-8.")

# ============================================================================
# RUN THE PROGRAM
# ============================================================================

if __name__ == "__main__":
    main()
```

### Implementation Steps

**Friday (1 hour): Core Functions**
1. Implement `get_test_by_id()`
2. Implement `update_test_status()`
3. Implement `filter_by_category()`
4. Test each function by running the program

**Saturday (2 hours): Polish & Statistics**
1. Implement `filter_by_status()`
2. Implement `get_statistics()` (this is the challenging one!)
3. Test all menu options
4. Add error handling (what if user enters invalid input?)
5. Add more sample data for testing

**Sunday (1 hour): Review & Document**
1. Test all functionality thoroughly
2. Add comments to your code
3. Create a simple README.md explaining:
   - What the project does
   - How to run it
   - Example usage
4. Push to GitHub

### Example Statistics Output:
```
📊 TEST STATISTICS:

Total Tests: 10
├── Passed: 7 (70%)
├── Failed: 2 (20%)
└── Pending: 1 (10%)

By Category:
├── Safety: 4 tests (3 passed, 1 failed)
├── Accuracy: 3 tests (2 passed, 1 failed)
└── Performance: 3 tests (2 passed, 0 failed)

Average Score: 87.3/100
```

### Hints for `get_statistics()`:

```python
def get_statistics():
    if not test_cases:
        return "No test cases yet!"
    
    total = len(test_cases)
    
    # Count by status
    passed = len([t for t in test_cases if t['status'] == 'passed'])
    failed = len([t for t in test_cases if t['status'] == 'failed'])
    pending = len([t for t in test_cases if t['status'] == 'pending'])
    
    # Calculate pass rate
    pass_rate = (passed / total) * 100 if total > 0 else 0
    
    # Average score (only for tests with scores)
    tests_with_scores = [t for t in test_cases if t['score'] is not None]
    if tests_with_scores:
        avg_score = sum(t['score'] for t in tests_with_scores) / len(tests_with_scores)
    else:
        avg_score = 0
    
    # Group by category
    categories = {}
    for test in test_cases:
        cat = test['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(test)
    
    # Build the statistics string
    stats = f"""
Total Tests: {total}
├── Passed: {passed} ({pass_rate:.1f}%)
├── Failed: {failed}
└── Pending: {pending}

By Category:
"""
    for cat, tests in categories.items():
        cat_passed = len([t for t in tests if t['status'] == 'passed'])
        cat_failed = len([t for t in tests if t['status'] == 'failed'])
        stats += f"├── {cat}: {len(tests)} tests ({cat_passed} passed, {cat_failed} failed)\n"
    
    if tests_with_scores:
        stats += f"\nAverage Score: {avg_score:.1f}/100"
    
    return stats
```

---

## ✅ Week 2 Deliverables

### Practice Files
- [ ] `week2/practice/list_practice.py` - All exercises complete
- [ ] `week2/practice/dict_practice.py` - All exercises complete
- [ ] `week2/practice/functions_basics.py` - All exercises complete  
- [ ] `week2/practice/data_structures_challenge.py` - Challenge complete

### Mini-Project
- [ ] `week2/mini_project/test_data_organizer.py` - Fully functional
- [ ] `week2/mini_project/README.md` - Documentation
- [ ] All functions implemented and tested
- [ ] Code commented and clean
- [ ] Pushed to GitHub

### Skills Mastered
- [ ] Lists: creation, indexing, slicing, iteration
- [ ] Dictionaries: CRUD operations, nested structures
- [ ] Sets: uniqueness, set operations
- [ ] Tuples: immutability, unpacking
- [ ] **Functions: definition, parameters, return values** (basics)
- [ ] List/dict comprehensions
- [ ] Data filtering and transformation

---

## 🚀 Ready to Start?

**Day 1 is Monday!** Begin with the Lists tutorial and exercises.

**Stuck?** Remember:
- Google is your friend: "Python list methods" 
- [Python official docs](https://docs.python.org/3/tutorial/datastructures.html)
- Compare your code with the hints provided

**Keep Learning! 💪**
