import sys
# Method 1: Standard multiplication function

def multiply(a, b):
    return a * b
result = multiply(1, 1)
print(f"Method 1: Result of direct multiply call: {result}")

# Method 2: Using variables

def multiply2(a, b):
    return a * b

a = 2
b = 2
result2 = multiply2(a, b)
print(f"Method 2: Result of multiply call with variables: {result2}")

# Method 3: Using keyword arguments
def multiply3(a ,b):
    return a * b

result = multiply(b=3, a=3)
print(f"Method 3: Result of multiply call using keyword arguments")

# Method 4: Multiple test cases
test_cases = [
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7)
]

count = 1
for num1, num2 in test_cases:
    result = multiply(num1, num2)
    print(f"Method 4: This is test case #{count} and the result of the multiply call: {result}")
    count += 1

# Method 5: Using sys.argv (Command line arguments)
print("Method 5: This methods uses command line arguments")

if len(sys.argv) == 3:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        result = multiply(num1, num2)
        print(f"From command line: {result}")
    except ValueError:
        print("Error: Please provide valid numbers")
        print("Usage: python Multiply.py <number1> <number2>")
else:
    print("No command-line arguments provided")
    print("Run with: python3 multiply.py 8 8")


