def is_multiple_of_3(number):
    return number % 3 == 0

# Example usage:
number = int(input("Input a number: "))
if is_multiple_of_3(number):
    print(number, "is a multiple of 3")
else:
    print(number, "is not a multiple of 3")