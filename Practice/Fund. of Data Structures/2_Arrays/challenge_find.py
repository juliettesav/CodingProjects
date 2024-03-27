def find_second_smallest(my_list):
    if len(my_list) < 2:
        return None 
    sorted_list = sorted(my_list)
    second_smallest = sorted_list[1]
    return second_smallest

my_list = [9, 3, 10, 2, 6]
print(find_second_smallest(my_list))