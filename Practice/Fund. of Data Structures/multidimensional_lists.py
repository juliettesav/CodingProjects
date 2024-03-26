seating_chart = [ 
    ["Sarah", "Claire", "Ben", "Taylor", "Eva",],
    ["Frankie", "George", "Lauren", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary","Nathan", "Olive"], 
    ["Chad", "April", "Matt", "Thomas","Penny"]
]

# print(seating_chart[2][1])

# First, we display each row number with the list of students in that row. 
# The enumerate function allows us to loop through the list while giving us access to a counter and the value of each item in the iterable.
'''
for i, row in enumerate(seating_chart):
    print(f"row {i+1}, students {row}")
'''

for i, row in enumerate(seating_chart):
    for j, student_name in enumerate(row):
        print(f"{student_name} is in row {i+1}, seat {j+1}")

