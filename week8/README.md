# Week 8: pytest Advanced

## Week 8 Goal
By end of this week, you will:
- Implement fixtures for efficient test setup and teardown
- Understand fixture scopes to optimize test performance
- Use parametrization to run tests with diverse datasets
- Organize shared fixtures using conftest.py
- Use markers to categorize and control test execution
- Build parametrized-test-suite (Mini-project)
- Push your eighth deliverable to GitHub

## Daily Breakdown

### Time Budget: 9 hours total
| Day | Focus | Time |
|-----|-------|------|
| Monday | Learn: Introduction to fixtures | 1 hr |
| Tuesday | Learn: Fixture scopes | 1 hr |
| Wednesday | Learn: Parametrization | 1 hr |
| Thursday | Learn: conftest.py and markers | 1 hr |
| Friday | Practice: Complex test scenarios | 1 hr |
| Saturday | Project: Start parametrized-test-suite | 2 hrs |
| Sunday | Complete mini-project + Push to GitHub | 1 hr |

## Resources

### YouTube
- [Corey Schafer: Pytest Fixtures - Setup and Teardown](https://www.youtube.com/watch?v=H7mJ9uA_QHs)

### Documentation
- [pytest Fixtures: explicit, modular, scalable](https://docs.pytest.org/en/latest/explanation/fixtures.html)
- [Parametrizing fixtures and test functions](https://docs.pytest.org/en/latest/how-to/parametrize.html)

## Practice Files Guide

Week 8 has 4 practice files to cover everything for the mini-project:

### File 1: `practice/01_fixtures_intro.py`
**Covers:**
- Creating and using basic fixtures
- Yield vs Return in fixtures
- Fixture dependency injection
- **Time:** 1 hour

### File 2: `practice/02_fixture_scopes.py`
**Covers:**
- Function, Class, Module, and Session scopes
- When to use each scope for LLM testing
- Performance implications of scopes
- **Time:** 1 hour

### File 3: `practice/03_parametrization.py`
**Covers:**
- Running one test with many inputs
- Testing boundary conditions efficiently
- Fixture-level parametrization
- **Time:** 1 hour

### File 4: `practice/04_conftest_markers.py`
**Covers:**
- Global fixtures in conftest.py
- Using markers to skip or group tests
- Registering custom markers in pytest.ini
- **Time:** 1 hour

# LEARNING TRACK

## Monday: Introduction to Fixtures (1 hour)

### Watch These Videos
1. **Corey Schafer: Pytest Fixtures**
   - URL: https://www.youtube.com/watch?v=H7mJ9uA_QHs
   - Why: Learn how to manage test state properly.

### Practice Exercises
Run `week8/practice/01_fixtures_intro.py`.

## Tuesday: Fixture Scopes (1 hour)

### Practice Exercises
Run `week8/practice/02_fixture_scopes.py`.

## Wednesday: Parametrization (1 hour)

### Practice Exercises
Run `week8/practice/03_parametrization.py`.

## Thursday: Markers & conftest (1 hour)

### Practice Exercises
Run `week8/practice/04_conftest_markers.py`.

## Friday: Integration (1 hour)

Review how to build a scalable test architecture using everything learned in Phase 0.

## Week 8 Deliverables

## Saturday-Sunday: Build `parametrized-test-suite`

**Mini-Project: `parametrized-test-suite`**

### Why this matters in AI testing?
LLMs handle infinitely variable inputs. You cannot write a separate test for every possible prompt. You must use parametrization to test hundreds of inputs reliably and fixtures to manage the setup of different model configurations.

### Learning Focus
- Advanced fixture patterns for model setup
- Massively parametrized tests for prompt evaluation
- Organized test structure using conftest.py
- Using markers to separate fast unit tests from slow model calls

### Mini-Project Overview
**An advanced, scalable test suite for evaluating LLM responses across multiple scenarios.**
```
parametrized-test-suite/
├── tests/
│   ├── conftest.py
│   ├── test_evaluation.py
│   └── test_performance.py
└── pytest.ini
```
