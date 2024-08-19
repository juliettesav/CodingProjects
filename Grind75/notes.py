def second_largest(list):
    new_list = sorted(list) 
    return new_list[-2]

def largest(list):
    new_list = sorted(list) 
    return new_list[-1]

print(second_largest([10, 20, 4, 45, 99])) # Output: 45
print(second_largest([10, 10, 10])) # Output: None
print(second_largest([1, 8, 2, 15, 99, 28]))
print(largest([1, 8, 2, 15, 99, 28]))