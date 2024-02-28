'''
age = 23
price = 19.95
print(age)
first_name = "Juliette"
is_online = True 
print(price)

#Check in at hospital. Name, age, returning patient or new patient 

first_name = input("What is your name? ")
print(f"Your name is {first_name}?")
print("Hello, " + first_name + "!")



birth_year = int(input("Enter your birth year: "))
age = int(2024) - birth_year
print(f'Got it! You are {age} years old!')



course = "Python for beginners"
#course = course.upper()

print(course)
print(course.find ('y'))
#prints the index of the letter y in the string. Will present a "-1" if not found in the string. 

print(course.replace('for','4'))
print(course.replace("x","4")) #does nothing since it does not contain the string "x" 



print('Python' in course) #provides a boolean answer 

'''

#other math operators 
#  // division that just provides a whole number ... % the remainder after division ... ** exponent ... 

#By using an equal sign after an operator, like x += 3, it will perform that operation on the x value and update the value as well.
'''
x = 10
x += 3
print(x)


x = 3 > 2 #Provides a boolean result.

'''

# == equality openator != inequality operator (not to be confused with =)


#Logical Operators
'''
price = 25 
print(price > 10 and price < 30)
print(not price < 10)


temp = int(input("What is the current temperature today? ")) 

if temp > 32: 
    print("It is hotter that freezing.")
    print("Make sure to drink water today.")

elif temp <= 32: 
    print("It is below freezing.")
    print("Make sure to wear your jacket.")

else: 
    print("That is not a valid temperature.")

print("All done!")

'''