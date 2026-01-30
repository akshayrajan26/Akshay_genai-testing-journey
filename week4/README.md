# 📦 Week 4: Modules, Packages & Virtual Environments

## 🎯 Week 4 Goal
By end of this week, you will:
- Stop writing "single file" scripts and start building **Software Projects**.
- Master **Modules** (Splitting code into files).
- Master **Packages** (Organizing files into folders).
- Understand **Virtual Environments** (Managing dependencies).

---

## 📅 Daily Breakdown

| Day | Focus | Practice File | Status |
|-----|-------|---------------|--------|
| **Monday** | Modules Basics | `01_modules_basics.py` | |
| **Tuesday** | Packages & `__init__` | `02_packages_intro.py` | |
| **Wednesday** | Virtual Environments | `03_venv_setup.py` | |
| **Thursday** | Paths & Imports | `04_paths_and_imports.py` | |
| **Friday** | Structure Refactor Challenge | `05_structure_challenge.py` | |
| **Sat-Sun** | Mini-Project: `llm_test_utils` Package | | |

**Total: 9 hours**

---

## Practice Files Guide

Week 4 is different. **You cannot just run the file.** You often need to create *other* files to import.

### 1. `practice/01_modules_basics.py` (Monday)
- Creating a separate `.py` file and importing it.
- `import module` vs `from module import function`.
- Aliasing with `as`.

### 2. `practice/02_packages_intro.py` (Tuesday)
- Creating distinct folders for your code.
- The role of `__init__.py`.
- Converting a folder into a Python Package.

### 3. `practice/03_venv_setup.py` (Wednesday)
- Why we need virtual environments (separation).
- Creating and activating a `venv`.
- Installing packages (e.g., `requests`, `pytest`) locally appropriately.

### 4. `practice/04_paths_and_imports.py` (Thursday)
- How Python finds modules (`sys.path`).
- Debugging "Module Not Found" errors.
- Relative vs Absolute imports.

### 5. `practice/05_structure_challenge.py` (Friday)
- **The Boss Level:** Taking a messy 100-line script and refactoring it into a clean package structure.

---

## 📚 LEARNING TRACK

### Monday: Modules Basics (1 hour)

Run `week4/practice/01_modules_basics.py`. It will ask you to create a helper file `my_math.py`.
- **Goal:** Understand that code can live in other files.

### Tuesday: Packages (1 hour)

Run `week4/practice/02_packages_intro.py`. It will ask you to create a folder `text_tools` with an `__init__.py`.
- **Goal:** Understand directories as namespaces.

### Wednesday: Virtual Envs (1 hour)

Run `week4/practice/03_venv_setup.py`. It will check if you are running inside a virtual environment.
- **Goal:** Never pollute your global Python install again.

### Thursday: Imports & Paths (1 hour)

Run `week4/practice/04_paths_and_imports.py`. It will simulate common import errors.
- **Goal:** Be able to fix `ModuleNotFoundError`.

### Friday: Refactor Challenge (1 hour)

Run `week4/practice/05_structure_challenge.py`. It contains a "monolith" of code.
- **Goal:** Break it apart into `helpers.py`, `config.py`, and `main.py`.

---

## Week 4 Deliverables

### Practice Files
- [ ] `week4/practice/01_modules_basics.py`
- [ ] `week4/practice/02_packages_intro.py`
- [ ] `week4/practice/03_venv_setup.py`
- [ ] `week4/practice/04_paths_and_imports.py`
- [ ] `week4/practice/05_structure_challenge.py`

### Mini-Project
- [ ] `week4/mini_project/llm_test_utils/` (Package structure)
