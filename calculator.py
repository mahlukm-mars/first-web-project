# Question 1: Addition and Subtraction Calculator
print("=== Question 1: Addition and Subtraction Calculator ===")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2

print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")

print("\n" + "="*50 + "\n")

# Question 2: Multiplication and Division Calculator
print("=== Question 2: Multiplication and Division Calculator ===")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

multiplication = num1 * num2
if num2 != 0:
    division = num1 / num2
    print(f"Multiplication: {num1} * {num2} = {multiplication}")
    print(f"Division: {num1} / {num2} = {division}")
else:
    print(f"Multiplication: {num1} * {num2} = {multiplication}")
    print("Division: Cannot divide by zero!")

print("\n" + "="*50 + "\n")

# Question 3: Simple Arithmetic Expressions
print("=== Question 3: Simple Arithmetic Expressions ===")
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
third = float(input("Enter the third number: "))

result = (first + second) * third
print(f"Result of ({first} + {second}) * {third} = {result}")

print("\n" + "="*50 + "\n")

# Question 4: Number Comparison (True/False)
print("=== Question 4: Number Comparison (True/False) ===")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

is_greater = num1 > num2
are_equal = num1 == num2

print(f"Is {num1} greater than {num2}? {is_greater}")
print(f"Are {num1} and {num2} equal? {are_equal}")