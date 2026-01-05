import sys

def multiply(a, b):
    return a * b

# Method 1: Direct function call 
result = multiply(2, 4)
print(f"The result of the direct multiplication function call: {result}")

# Method 2: Function call using variables
a = 4
b = 4
result2 = multiply(a, b)
print(f"The result of the multiplication call using variables is: {result2}")

# Method 3: Function call using keyword arguments
result3 = multiply(b=5, a=4)
print(f"The result of the call using keyword arguments is: {result3}")

# Method 4: Multiple test cases
test_cases = [
    (1, 1),
    (5, 5),
    (6, 2),
    (7, 5),
]

for num1, num2 in test_cases:
    result = multiply(num1, num2)
    print(f"The result of each test case on the list is: {result}")


# Method 5: 
