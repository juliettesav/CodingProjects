def second_largest(list):
    new_list = sorted(list) 
    return new_list[-2]

print(second_largest([10, 20, 4, 45, 99])) # Output: 45
print(second_largest([10, 10, 10])) # Output: None