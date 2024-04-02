'''
I asked ChatGPT, "Give me a simple python coding challenge that I can try to solve." This is what it gave me, followed by my solution: 

Challenge: FizzBuzz

Write a program that prints the numbers from 1 to 100. 
But for multiples of three, print "Fizz" instead of the number, 
and for the multiples of five, print "Buzz". 
For numbers which are multiples of both three and five, print "FizzBuzz".
'''
num = 1

def multiple3(number):
    return number % 3 == 0

def multiple5(number):
    return number % 5 == 0

while num <= 100: 
    number = num
    if multiple3(number) and multiple5(number): 
        print("FizzBuzz")
    elif multiple3(number): 
        print("Fizz") 
    elif multiple5(number): 
        print("Buzz")
    else: 
        print(num)
    num = num + 1 