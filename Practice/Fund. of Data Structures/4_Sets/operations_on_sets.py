set_A = {10, 20, 30, 40, 50}
set_B = {30, 40, 50, 60, 70}

union_set = set_A.union(set_B) # Returns a combined set of both sets (without duplicates)
print(union_set)

intersection_set = set_A.intersection(set_B) # Returns what values are in both sets
print(intersection_set)

difference_set = set_A.difference(set_B) # Removes a set from another set 
print(difference_set)

difference_set_BA = set_B.difference(set_A)
print(difference_set_BA)

symetric_difference_set = set_A.symmetric_difference(set_B) # Unique to both sets
print(symetric_difference_set)