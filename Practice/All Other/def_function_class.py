'''
Let's break down def functions and classes in Python.

FUNCTIONS
Functions are blocks of reusable code that perform a specific task. 
You define a function using the def keyword, followed by the function name, parentheses (which may include parameters), and a colon. 
The function body is indented below the definition line.

Example of a Simple Function
'''
def greet(name):
    print(f"Hello, {name}!")
'''
def: This keyword is used to declare a function.
greet: This is the name of the function.
name: This is a parameter, a placeholder for the value you pass to the function when you call it.
Function body: The indented lines of code that define what the function does. In this case, it prints a greeting.

Calling the Function
'''
greet("Alice")
# Output: Hello, Alice!
'''
Function with Return Value
'''
def add(a, b):
    return a + b
'''
return: This keyword is used to return a value from the function.
'''
result = add(3, 4)
print(result)
# Output: 7
'''
CLASSEES
Classes are blueprints for creating objects (instances). They encapsulate data (attributes) and functions (methods) that operate on that data. You define a class using the class keyword.

Example of a Simple Class
'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says woof!")

'''
class: This keyword is used to declare a class.
Dog: This is the name of the class.
__init__: This is a special method called a constructor. It initializes the object's attributes.
self: This refers to the instance of the class. It's used to access attributes and methods of the class in Python.

Creating an Instance
'''
my_dog = Dog("Buddy", 5)
'''
my_dog: This is an instance of the Dog class.

Accessing Attributes and Methods
'''
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 5
my_dog.bark()       # Output: Buddy says woof!
'''
Putting It All Together
Here's a more comprehensive example combining functions and classes:
'''
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, a, b):
        self.result = a + b
        return self.result
    
    def subtract(self, a, b):
        self.result = a - b
        return self.result

def main():
    calc = Calculator()
    print(calc.add(5, 3))        # Output: 8
    print(calc.subtract(10, 4))  # Output: 6

if __name__ == "__main__":
    main()
    
'''
Calculator: This class has an attribute result and two methods add and subtract.
main: This function creates an instance of the Calculator class and calls its methods.


PRACTICE

To get comfortable with functions and classes, try the following exercises:

Function Exercise 1: Write a function is_even that takes a number and returns True if it's even, and False otherwise.
'''
def is_even(num):
    if num % 2 == 0:
        return True 
    else: 
        return False

print(is_even(6))

# Function Exercise 2: Write a function is_odd that takes a number and returns True if it's odd, and False otherwise.

def is_odd(num):
    if num % 2 != 0: 
        return True
    else: 
        return False 
    
print(is_odd(6))

# Function Exercise 3: Check if a Number is a Multiple of Another Number 

def multiple(num, divisor):
    if num % divisor == 0:
        return True 
    else: 
        return False 

num = int(input("What number do you want to check? "))
divisor = int(input("What do you want to see if this number is a multiple of? "))

print(f"The answer is {multiple(num, divisor)}.")

'''
2. Class Exercise: Create a class Rectangle with attributes length and width. Add methods to calculate the area and perimeter of the rectangle.
'''
len = int(input("Input length: "))
wid = int(input("Input Width: "))

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Area(self, length, width): 
        area = length * width
        print(area)
    
    def Perimeter(self, length, width):
        perimeter = (2 * length) + (2 * width)
        print(perimeter)


my_rectangle = Rectangle(len,wid)
my_rectangle.Area(len,wid)
my_rectangle.Perimeter(len,wid)

'''
Keep practicing and you'll get it in no time!

Here are some more practice challenges: 

FUNCTION CHALLENGES
1: Check Prime
Write a function is_prime(n) that takes an integer n and returns True if n is a prime number and False otherwise.

'''
def is_prime(n):
    if n <= 1:
        return False 
    if n<= 3: 
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False 
    i += 6
    return True 

n = int(input("Check for prime: "))
print(f"The answer is {is_prime(n)}.")
'''

2: Find Maximum
Write a function find_max(numbers) that takes a list of numbers and returns the largest number in the list.

'''
def find_max(nums): 
    nums.sort()
    return nums[-1]

nums = [3, 5, 1, 8, 2]
print(f"The largest number in the string is {find_max(nums)}.")

add = 'y'
while add == 'y': 
    num = int(input("Add a number to the list: ")) 
    nums.append(num)
    add = input("Want to add another number? Type y or n: ")

print(f"The largest number in the string is {find_max(nums)}.") 

'''

3: Fibonacci Sequence
Write a function fibonacci(n) that returns a list containing the first n numbers in the Fibonacci sequence.
'''

def fibo(nacci, i, n):
    while i < n: 
        x = nacci[i] + nacci[i + 1]
        nacci.append(x) 
        i = i + 1
    return x


i = 0
nacci = [0,1]

n = (int(input("How many numbers of the fibonacci sequence do you want to see? "))-2)
fibo(nacci, i, n)
print(f"The Fibonacci sequence is {nacci}.")
'''

CLASS CHALLENGES
1: Simple Bank Account
Create a class BankAccount with attributes owner and balance. Add methods deposit(amount) to add to the balance, and withdraw(amount) to subtract from the balance if sufficient funds are available.

'''

'''
2: Circle
Create a class Circle with attribute radius. Add methods to calculate the area and circumference of the circle.

'''

'''
3: Student Grades
Create a class Student with attributes name and grades (a list of grades). Add methods to calculate the average grade, add a new grade, and return the highest and lowest grades.

class Student: 
    def __init__(self, name, grade):
        self.name = name 
        print(name)
        self.grade = grade
        print(grade)
        return grade
    def grades():
        grades = []
'''

def grades(grades_list):
    add_new = "y"
    while add_new == 'y': 
        new_grade = int(input("New Grade: "))
        grades_list.append(new_grade)
        add_new = input("Add another new grade? Select y or n: ")
    return grades_list 

def avg_grade(grades_list):
    if len(grades_list) > 0:
        avg = sum(grades_list) / len(grades_list)
        return avg 
    else: 
        return 0

grades_list = grades([])
print(f"Your grades: {grades_list}")
print(f"Your average grade: {avg_grade(grades_list)}")
### End