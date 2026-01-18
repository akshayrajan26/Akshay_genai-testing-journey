# Week 1 Completed: Key Learnings & Challenges

## What I Built
**Project:** `prompt-formatter` - A Python package for LLM prompt template handling

**Core Features:**
- Template creation with variable substitution
- Input validation (empty checks, length limits, keyword validation)
- Response cleaning utilities
- Helper functions for token estimation and list formatting

## Critical Challenge: The ModuleNotFoundError

### The Problem
Spent ~1 hour debugging this error:
```
ModuleNotFoundError: No module named 'prompt_formatter'
```

### Why This Happened
**Root Cause:** Python's module search path (PYTHONPATH) didn't include my package directory.

When you run a Python script, Python looks for modules in:
1. The directory containing the script
2. Directories listed in `PYTHONPATH`
3. Standard library locations

My package structure was:
```
week1/mini_project/
├── prompt_formatter/  # My package
├── tests/             # Test files trying to import
└── examples/          # Example files trying to import
```

When running `python3 tests/test_templates.py` from the `genai-testing-journey/` root, Python couldn't find `prompt_formatter` because it wasn't in the search path.

### The Solution
**Option 1: Set PYTHONPATH (Recommended for development)**
```bash
cd week1/mini_project
PYTHONPATH=. python3 tests/test_templates.py
```

**Option 2: Use pytest (Best practice)**
```bash
cd week1/mini_project
pytest tests/
```
pytest automatically adds the current directory to the path!

**Option 3: Install package in editable mode (For larger projects)**
```bash
cd week1/mini_project
pip install -e .
```

### Key Takeaway
**Always run Python commands from the directory containing your package**, not from parent directories. This is standard Python project practice.

---

## Learning Gap Identified

### What the Roadmap Said to Learn (Week 1):
- ✅ Variables and data types
- ✅ String creation, methods, slicing  
- ✅ f-strings for prompt templates
- ✅ Type conversion

### What the Mini-Project Actually Required:
- ❌ **Functions** (not until Week 3!)
- ❌ **Classes** (not explicitly in roadmap)
- ❌ **Modules & `__init__.py`** (not until Week 4!)
- ❌ **List comprehensions** (Week 3)
- ❌ **`**kwargs`** (Week 3)
- ❌ **Type hints** (`:str`, `->bool`) (not in roadmap)

### The Gap
Week 1's mini-project required concepts from Weeks 3 and 4! This made the learning curve steeper than intended.

### Recommendations for Future Learners
**Option A: Adjust Week 1 mini-project** (Simpler)
- Build just simple functions, not a full package
- Save the package structure for Week 4

**Option B: Add prerequisite topics to Week 1** (What I did)
- Learn basic functions before the mini-project
- Understand classes at a basic level
- Quick intro to imports

---

## What I Actually Learned Beyond the Syllabus

### 1. Functions
```python
def validate_not_empty(text: str) -> bool:
    return bool(text and text.strip())
```
- Definition with `def`
- Parameters and return types
- Return values

### 2. Classes
```python
class PromptTemplate:
    def __init__(self, template: str):
        self.template = template
    
    def fill(self, **kwargs):
        return self.template.format(**kwargs)
```
- `__init__` constructor
- `self` reference
- Instance variables
- Methods

### 3. Modules & Packages
- `__init__.py` makes a folder a package
- Relative imports: `from .validators import ...`
- Package structure and organization

### 4. Advanced String Techniques
- Regular expressions (`re.sub()`)
- List comprehensions with strings
- `**kwargs` for flexible function arguments

---


## ✅ Week 1 Deliverables

### Code
- ✅ `validators.py` - 3 validation functions
- ✅ `templates.py` - PromptTemplate class
- ✅ `cleaners.py` - Response cleaning utilities
- ✅ `utils.py` - Token estimation & list formatting
- ✅ `test_templates.py` - Template tests
- ✅ `test_validators.py` - Validator tests
- ✅ `basic_usage.py` - Working example

### Practice
- ✅ All 5 string exercises completed
- ✅ Understanding of f-strings, `.format()`, string methods
