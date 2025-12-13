# This script includes three beginner-level Python functions:
# 1. Filtering even numbers
# 2. Finding the longest word in a list
# 3. Creating a list of positive numbers (ignoring negatives and zero)


# 1. Function that returns a list of even numbers from the input list
def filter_even(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    return even

# Example:
print("Even numbers:", filter_even([1, 2, 3, 4, 5]))


# 2. Function that returns the longest word from a list of words
def longest_word(words):
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# Example:
print("Longest word:", longest_word(["apple", "banana", "cherry", "kiwi"]))


# 3. Function that returns a new list with only positive numbers
def remove_negatives(numbers):
    positives = []
    for num in numbers:
        if num > 0:
            positives.append(num)
    return positives

# Example:
print("Positive numbers only:", remove_negatives([3, -2, 0, 4, -1]))
