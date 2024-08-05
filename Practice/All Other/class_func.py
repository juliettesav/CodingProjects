# CLASS - used for creating objects; objects have attributes (variables) and methods (functions)

class Dog: 
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"
    
my_dog = Dog("Buddy", 3)
    

'''
The __init__ Method:
- A special method in Python, also know as a constructor. 
- Automatically called when a new instance (new object) of the class is created  
- self is a reference to the current instance of the class. 
        - So "self" means the current object 
        - This is how attributes and methods of the class are accessed 

Parameters & Attributes: 
- In this class, 'name' and 'age' are parameters that need to be passed when creating the new 'Dog' object. 
        - these values/variables/attributes belong to and are stored in the current object (self) within the __init__ method 
        - For example, these Attributes: 
            - self.name = name ### Stores the name of the dog 
            - self.age = age   ### Stores the age of the dog 

Methods: 
- Functions within a class (these can manipulate the object's data)
- The first parameter of a method is always 'self' which refers to the instance (object) calling the method 

- In this case, the return of the bark method is a string. 

Instance: 
- An instance is a specific object created from a class 
- In this case, 'my_dog' is an instance of the Dog class 

'''

# CONTINUE BELOW (from this chat https://chatgpt.com/share/56d0f8d2-a7b8-42d8-b674-89003141e5f3)

'''
Creating an Object (Instance) of a Class
To create an object of a class, you call the class as if it were a function:
'''
my_dog = Dog("Buddy", 3)
'''
Here, my_dog is an instance of the Dog class with the name "Buddy" and age 3. You can access its attributes and methods like this:

'''
print(my_dog.name)  # Output: Buddy
print(my_dog.bark())  # Output: Buddy says woof!
'''
Key Points
self: This keyword represents the instance of the class. It's used to access attributes and methods of the class in Python.
__init__: This is the constructor method that initializes the object's attributes.
Attributes: These are variables that belong to the object. They are defined in the __init__ method or elsewhere in the class.
Methods: These are functions defined inside the class. They define the behavior of the objects created from the class.
Example with More Methods
Let's extend the Dog class with more methods:

'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    def get_age(self):
        return f"{self.name} is {self.age} years old."

    def set_age(self, age):
        self.age = age
        return f"{self.name} is now {self.age} years old."
'''
In this extended class:

get_age is a method that returns the dog's age.
set_age is a method that sets a new age for the dog.
'''
print(my_dog.get_age())  # Output: Buddy is 3 years old.
print(my_dog.set_age(4))  # Output: Buddy is now 4 years old.
'''
Summary
Classes: Blueprints for creating objects.
Objects: Instances of classes with attributes and methods.
__init__ method: Initializes the object's attributes.
self: Represents the instance of the class.
Classes help organize code and model real-world entities, making your code more modular and reusable. Let me know if you'd like more details or another example!
'''