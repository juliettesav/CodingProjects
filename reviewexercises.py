# Review of Basic Python Operations and Control Flow

# Variables and Data Types
# Here we define variables that to store different types of data.
age = 23
price = 19.95
first_name = "Juliette"
is_online = True 

print(age)
print(price)

# User Input
first_name = input("What is your name? ")
print(f"Your name is {first_name}?")
print("Hello, " + first_name + "!")

# Calculate Age
birth_year = int(input("Enter your birth year: "))
age = int(2024) - birth_year
print(f'Got it! You are {age} years old!')

# String Operations
course = "Python for beginners"
course = course.upper() # Changes the original string to all uppercase. 
print(course)

print(course.find ('y'))  # Find the index of the letter 'y' in the string. Will present a "-1" if not found in the string.
print(course.replace('for','4'))  # Replace 'for' with '4'.
print(course.replace("x","4"))  # Since 'x' is not found, the string remains unchanged.

# Check if a Substring Exists in a String
print('Python' in course)  # Returns a Boolean result; True if 'Python' is in the course string, otherwise False.

# Math Operators
# Demonstrates various mathematical operations and their corresponding assignments.
x = 10
x += 3  # Equivalent to x = x + 3
print(x)

x = 3 > 2  # x will be assigned the boolean result of the expression.
print(x)

#  For division that just returns a whole number, use // 
# To find the remainder after division, use %
# For exponents, use **   

# Comparison Operators
# Demonstrates equality and inequality operators.
print(3 == 3)  # Returns True because 3 equals 3.
print(3 != 3)  # Returns False because 3 is equal to 3.

# Logical Operators and Control Flow
price = 25
print(price > 10 and price < 30)  # Logical AND operation.
print(price > 10 or price < 30)  # Logical OR operation.
print(not price < 10)  # Logical NOT operation.

# The equality operator is == (not to be confused with =)
# The inequality operator is != 


# Conditional Statements
temp = int(input("What is the current temperature today? "))

if temp > 32:
    print("It is hotter than freezing.")
    print("Make sure to drink water today.")
elif temp <= 32:
    print("It is below freezing.")
    print("Make sure to wear your jacket.")
else:
    print("That is not a valid temperature.")

print("All done!")
