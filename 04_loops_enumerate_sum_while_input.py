# 1. Print all even numbers from 2 to 20 using for + range
print("Even numbers from 2 to 20:")
for number in range(2, 21):
    if number % 2 == 0:
        print(number, end=" ")
print("\n")  # newline for spacing

# 2. Ask for password using a while loop until the correct one is entered
correct_password = "letmein"
user_input = ""
while user_input != correct_password:
    user_input = input("Enter the password: ")
print("Access granted.\n")

# 3. Enumerate all letters in the user-provided word
word = input("Insert a word: ")
print("Enumerated letters:")
for index, letter in enumerate(word):
    print(f"{index}: {letter}")
print()

# 4. Keep asking for numbers until 0 is entered, then show the total sum
total = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    total += number
print("Total sum of all entered numbers:", total, "\n")

# 5. Print all numbers from 1 to 20 except those divisible by 3
print("Numbers from 1 to 20, skipping those divisible by 3:")
for num in range(1, 21):
    if num % 3 == 0:
        continue
    print(num, end=" ")
print("\n")

# 6. Draw a triangle of * with the height defined by the user
height = int(input("Enter the height of the triangle: "))
print("Triangle:")
for row in range(1, height + 1):
    for star in range(row):
        print("*", end="")
    print()
