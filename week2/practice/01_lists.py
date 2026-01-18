# Exercise 1: Basic list operations (Grocery List)
# Create a list with: "apples", "bananas", "milk"
groceries = ["apples", "bananas", "milk"]

# Add "bread" and "eggs"
groceries.append("bread")
groceries.append("eggs")

# Print the final list
print("Grocery List:", groceries)

# Exercise 2: Slice operations (Numbers)
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Get first 3 numbers
print("First 3:", nums[:3])

# Get last 2 numbers
print("Last 2:", nums[-2:])

# Get every other number
print("Every other:", nums[::2])

# Exercise 3: Iteration & Math (Grades)
grades = [85, 92, 78, 95, 88]
# Calculate average grade
avg = sum(grades) / len(grades)
print(f"Average grade: {avg}")

# Find maximum grade
print(f"Max grade: {max(grades)}")

# Count grades above 90
count_90 = len([g for g in grades if g > 90])
print(f"Grades above 90: {count_90}")

# Exercise 4: Filtering (Light Test Case context)
# You have a list of test names: ["test_login", "test_signup", "test_api", "test_ui"]
test_names = ["test_login", "test_signup", "test_api", "test_ui"]

# Create a new list called 'ui_tests' that only contains names with "ui" or "api"
ui_tests = [t for t in test_names if "ui" in t or "api" in t]
print("UI/API Tests:", ui_tests)
