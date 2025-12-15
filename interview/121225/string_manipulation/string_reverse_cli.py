'''
This version of the string reversal function 
will take a system argument using sys.argv
'''
import sys

def string_reverse(str):
    return str[::-1]

# Check if command-line argument is provided
if len(sys.argv) > 1:
    input_string = sys.argv[1]
else:
    input_string = "There was no argument..."

result = string_reverse(input_string)
print(result)