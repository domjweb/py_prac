''' 
Write a function that takes a string and returns a reversed string
This version is hardcoded so an argument doesn't have to be passed
through the terminal.
'''

def string_reverse(str):
    return str[::-1]
result = string_reverse("This is a hardcoded string.")
print(result)
