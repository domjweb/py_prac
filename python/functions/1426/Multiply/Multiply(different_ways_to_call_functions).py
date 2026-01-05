# Simple multiplication function in its purest form
import sys

def multiply(a, b):
    return a * b


# Testing the function with different arguments
if __name__ == "__main__":
    # Method 1: Direct function call with positional arguments
    result1 = multiply(5, 3)
    print(f"Method 1 - Direct call: 5 * 3 = {result1}")
    
    # Method 2: Using variables
    x = 10
    y = 7
    result2 = multiply(x, y)
    print(f"Method 2 - Using variables: {x} * {y} = {result2}")
    
    # Method 3: Using keyword arguments
    result3 = multiply(a=4, b=9)
    print(f"Method 3 - Keyword arguments: 4 * 9 = {result3}")
    
    # Method 4: Multiple test cases
    test_cases = [
        (2, 3),
        (10, 5),
        (7, 8),
        (-3, 4),
        (0, 100)
    ]
    
    print("\nMethod 4 - Multiple test cases:")
    for num1, num2 in test_cases:
        result = multiply(num1, num2)
        print(f"  {num1} * {num2} = {result}")
    
    # Method 5: Using command-line arguments (sys.argv)
    # sys.argv is a list: [script_name, arg1, arg2, ...]
    # Example: "python Multiply.py 6 7" gives sys.argv = ["Multiply.py", "6", "7"]
    # So len(sys.argv) == 3 means: 1 script name + 2 user arguments
    print("\nMethod 5 - Command-line arguments (sys.argv):")
    if len(sys.argv) == 3:  # Script name + 2 numbers = 3 total items
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            result = multiply(num1, num2)
            print(f"  From command line: {num1} * {num2} = {result}")
        except ValueError:
            print("  Error: Please provide valid numbers")
            print("  Usage: python Multiply.py <number1> <number2>")
    else:
        print("  No command-line arguments provided")
        print("  Run with: python Multiply.py 6 7")

