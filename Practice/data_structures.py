# List: stores a collection of items in a specific order 

list = [1, 2, 3]

# Tuple: stores related data and is immutable

tuple = (1, 2)

# Dictionary: stores key-value pairs; the key retrieves the value

dictionary = {'Monica':'Chef', 'Rachel': 'Assistant Buyer', 'Phoebe':'Masseuse','Ross':'Paleontologist','Joey':'Actor','Chandler':'in the field of Statistical Analysis and Data Reconfiguration'}

# Set: stores a collection of unique items in an unordered manner 

set = {'dog', 'cat','bird'}

# Deque: (pronounced like 'deck') allows for inserting or removing date from both ends; similar to a list 
from collections import deque

### Create a deque from a list
dq = deque([1, 2, 3])
# deque([1, 2, 3])

### Create a deque from a tuple
dq = deque((4, 5, 6))
# deque([4, 5, 6])

### Create a deque from a string
dq = deque("hello")
# deque(['h', 'e', 'l', 'l', 'o'])

# Array Structure: consists of a collection of elements where each item is idetified by an index or key; includes tuples and lists 
## Zero-based indexing: a way of numbering in which the initial element of a sequence is assigned to 0; used by arrays

# Number of pets of each student
array = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]

num_of_students = len(array)
#print(num_of_students)

stu4 = array[3]

#print(stu4)

stu_3_from_end = array[-3]

print("Hello world!")