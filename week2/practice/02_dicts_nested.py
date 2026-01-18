# Exercise 1: Create a simple dictionary (User Profile)
# Create a dict with: name, age, city, and a list of skills
user = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "Testing"]
}
print("User Profile:", user)

# Exercise 2: Update and access
# Add a "favorite_color" field
user["favorite_color"] = "Blue"

# Update the age
user["age"] = 31

# Safely get a field called "occupation" with a default value
occ = user.get("occupation", "Unemployed")
print(f"Occupation: {occ}")

# Exercise 3: Nested dictionary (Company structure)
company = {
    "engineering": {"headCount": 50, "budget": 100000},
    "marketing": {"headCount": 20, "budget": 50000}
}
# Calculate total budget
total_budget = company["engineering"]["budget"] + company["marketing"]["budget"]
print(f"Total Budget: {total_budget}")

# Print the headCount for engineering
print(f"Engineering Headcount: {company['engineering']['headCount']}")

# Exercise 4: List of dictionaries (Light Test Context)
# Create a list of 3 dictionaries, each representing a test case
# Each should have: "id", "status" (passed/failed), and "score"
test_results = [
    {"id": "TC001", "status": "passed", "score": 90},
    {"id": "TC002", "status": "failed", "score": 45},
    {"id": "TC003", "status": "passed", "score": 85}
]

# Calculate the average score
avg_score = sum([t["score"] for t in test_results]) / len(test_results)
print(f"Average Test Score: {avg_score}")
