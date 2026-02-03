# Week 5: File Handling & JSON

**Why This Matters for AI Testing:**
Test datasets are JSON/JSONL files. Results are saved as JSON. This is fundamental.

**Learning Focus:**
- Reading/writing text files
- JSON parsing and serialization
- JSONL (JSON Lines) format
- Error handling for file operations
- Path handling with pathlib

## Practice Files
The `practice/` directory contains structured exercises with TODOs to reinforce these concepts.

1.  **`practice/01_text_files.py`**
    *   Basic file I/O operations (read, write, append).
    *   Context managers (`with` statement) for safe file handling.
    *   Error handling for file operations.

2.  **`practice/02_json_basics.py`**
    *   `json.dumps` vs `json.dump` usage.
    *   Loading and interacting with JSON data.
    *   Parsing JSON strings from simulated API responses.

3.  **`practice/03_pathlib_intro.py`**
    *   Modern file path manipulation using `pathlib` (replacing `os.path`).
    *   Creating cross-platform compatible paths.
    *   Reading/writing directly from Path objects.

4.  **`practice/04_jsonl_handling.py`**
    *   Processing JSONL files (line-delimited JSON).
    *   Reading and appending to large datasets efficiently.

## Plan
1.  Complete the TODOs in each practice file sequentially.
2.  Verify understanding by running the scripts:
    ```bash
    python week5/practice/01_text_files.py
    ```
3.  Proceed to the Week 5 Mini-Project: **`dataset-loader`**.

**Mini-Project: `dataset-loader`**
```
Build a dataset manager:
├── Load test cases from JSONL
├── Validate schema (required fields)
├── Handle malformed entries gracefully
├── Report statistics
├── Save results back to JSONL
└── Support for multiple dataset formats
```
