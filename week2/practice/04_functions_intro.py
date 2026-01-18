# Exercise 1: Simple greeting
# Write a function that takes a name and returns "Hello, [name]!"
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Exercise 2: Math operation
# Write a function that take two numbers and returns their sum
def add_nums(a, b):
    return a + b

print(f"Sum: {add_nums(5, 10)}")

# Exercise 3: Light Test Context
# Write a function called 'format_test_info' that takes an ID and a status
# and returns a formatted string: "Test [ID] status is: [STATUS]"
def format_test_info(test_id, status):
    return f"Test {test_id} status is: {status}"

print(format_test_info("TC001", "passed"))
