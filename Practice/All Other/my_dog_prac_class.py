class Dog: 
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def bark(self): 
        return f"{self.name} says woof!"
    
    def myage(self):
        return f"I'm {self.age} years old!"


dog_name = input("What is your dog's name? ")
dog_age = int(input("What is your dog's age? "))

my_dog = Dog(dog_name, dog_age)

print(my_dog.bark())
print(my_dog.myage())