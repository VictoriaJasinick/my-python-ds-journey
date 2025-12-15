# This script includes several Python functions to practice:
# - Positional and default parameters
# - Return values
# - Calling one function inside another
# - Basic math operations

# 1. Function that describes a person using name and age
def describe_person(name, age):
    print(f"{name} is {age} years old.")


# 2. Function that greets a person, calling them "Guest" if no name is provided
def greet_user(name="Guest"):
    print(f"Hello, {name}")


# 3. Function that calculates the area of a rectangle using width and height
def area_of_rectangle(width, height=1):
    return width * height


# 4. Function that calculates the final price after a discount
def discounted_price(price, discount_percent):
    return price * (1 - discount_percent / 100)


# 5. Function that returns the sum of a list of numbers
def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


# 6. Function that returns the average of a list of numbers,
#    using the sum_list() function from above
def average_list(numbers):
    total = sum_list(numbers)  # Call to another function
    return total / len(numbers)
