"""
Challenge: Build a mini test case database using only data structures.
Uses a helper function as a bridge to Week 3/Mini-Project concepts.
"""

# 1. Create a function to help organize data (Bridge concept)
def create_test_case(id, category, status):
    return {
        "id": id,
        "category": category,
        "status": status
    }

# 2. Create a list called 'test_db'
test_db = []

# 3. Use your function to add 3 test cases
test_db.append(create_test_case("TC001", "safety", "passed"))
test_db.append(create_test_case("TC002", "accuracy", "failed"))
test_db.append(create_test_case("TC003", "safety", "passed"))

# 4. Filter the list to find only 'passed' tests (Standard list/dict practice)
passed_tests = [t for t in test_db if t["status"] == "passed"]

# 5. Print the IDs of the passed tests
print("Passed Test IDs:", [t["id"] for t in passed_tests])

# 6. Basic Analysis (Bridge to Mini-Project stats)
total = len(test_db)
passed_count = len(passed_tests)
print(f"Pass Rate: {(passed_count/total)*100:.1f}%")
