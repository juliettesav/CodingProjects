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
- To create an object (instance) of a class, you write it as a function 
'''
my_dog = Dog("Buddy", 3)
'''
- Now if you want to access this instance, you have to print out the function by calling one of the attributes or methods. 
- For example, 

'''
print(my_dog.name) # This runs the my_dog function and asks to print the attribute of the dog's name. 
print(my_dog.age) # Similarly, this would just print the attribute of the dog's age. 

print(my_dog.bark()) # In this case, we are running the my_dog function and asking to print the method bark() which returns this output: Buddy says woof!

'''
Example with More Methods (the Dog class with more methods):

'''
'''
'''
class Dog: 
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def bark(self): 
        return f"{self.name} says woof!"
    
    def get_age(self):
        return f"I'm {self.age} years old!"
    
dog_name = input("What is your dog's name? ")
dog_age = int(input("What is your dog's age? "))

my_dog = Dog(dog_name, dog_age)

print(my_dog.bark())
print(my_dog.get_age())

'''
In this extended class:
get_age is a method that returns the dog's age.

SUMMARY
Classes: These are blueprints for creating objects. Essentionally the framework to hold instances. They help organize code and model real-world entities, making the code more modular and reusable.
Objects/Instances: Objects are instances of the class that contains attributes and methods. 
Attributes: These are values or variables that belong to an object. They are defined in the __init__ method or elsewhere in the class. 
Methods: These are functions defined inside the class. They define the behavior of the objects created from the class. 
__init__: This is the constructor method that initializes the object's attributes. 
self: This keyword represents the instance of a class. It is used to access attributes and methods of the class in Python. 
'''