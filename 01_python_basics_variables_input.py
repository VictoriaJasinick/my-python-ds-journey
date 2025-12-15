"""
01_python_basics_variables_input.py
Basic examples of Python variables, arithmetic, strings, and user input.
Author: Victoria Jasinick
Date: 2025-12-08
"""

# Example of a variable with a name
my_name = "Victoria"
print(f"Hello, I am {my_name}!")

# Example of working with numbers
number1 = 5.99  # First number (could be any float)
number2 = 3     # Second number (could be any integer)

# Arithmetic operations using two numbers
print(f"Addition: {number1 + number2}")
print(f"Subtraction: {number1 - number2}")
print(f"Multiplication: {number1 * number2}")
print(f"Division: {number1 / number2}")        # Result includes decimals
print(f"Floor division: {number1 // number2}") # Integer result, no decimals
print(f"Modulus: {number1 % number2}")         # Remainder after division

# String operations
text = "Hello, world!"
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Length: {len(text)}")
print(f"Last character: {text[-1]}")

# User input and working with data types
name = input("What's your name? ")
age = int(input("How old are you? "))  # Convert the input age to an integer
print(f"Hello, {name}! Next year you'll be {age + 1}")

# Still learning, but at least I stopped adding 5 + "banana"
# No snakes were harmed in the making of this script. 🐍
