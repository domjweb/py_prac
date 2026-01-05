import sys

def multiply(a, b):
    return a * b

# Method 1: Direct function call 
result = multiply(2, 4)
print(f"Method 1: The result of the direct multiplication function call: {result}")

# Method 2: Function call using variables
a = 4
b = 4
result2 = multiply(a, b)
print(f"Method 2: The result of the multiplication call using variables is: {result2}")

# Method 3: Function call using keyword arguments
result3 = multiply(b=5, a=4)
print(f"Method 3: The result of the call using keyword arguments is: {result3}")

# Method 4: Multiple test cases
print("Method 4: Multiple Test Cases")
test_cases = [
    (1, 1),
    (5, 5),
    (6, 2),
    (7, 5),
]

for num1, num2 in test_cases:
    result = multiply(num1, num2)
    print(f"The result of each test case on the list is: {result}")


# Method 5: Command line arguments
print("Method 5: Command Line Arguments (sys.argv):")

if len(sys.argv) == 3:
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        result = multiply(num1, num2)
        print(f"From command line: {result}")
    except ValueError:
        print("Error: Please provide valid numbers")
        print("Usage: python Multiply.py <number1> <number2>")
else:
    print("No command-line arguments provided")
    print("Run with: python Multiply.py 6 7")



