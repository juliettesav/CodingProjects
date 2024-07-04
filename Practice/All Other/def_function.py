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

1. Function Exercise: Write a function is_even that takes a number and returns True if it's even, and False otherwise.
'''
def main():
    return 

'''
2. Class Exercise: Create a class Rectangle with attributes length and width. Add methods to calculate the area and perimeter of the rectangle.
'''

'''
Keep practicing and you'll get it in no time!
'''