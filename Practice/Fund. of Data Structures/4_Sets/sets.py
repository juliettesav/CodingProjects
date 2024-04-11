# With Sets, the order doesn't matter and it's more to indicate grouping and check for compatibility (like containing a number, a character, or a string).
# Sets do not contain duplicates so adding the same value to a set does not return an error or a change to the set.

primary_colors = set(["red", "blue", "yellow"])

color = "green"

if color in primary_colors:
    print(f'{color} is a primary color.')
else: 
    print(f'{color} is not a primary color')

letters = set(['a', 'b'])

letters.add('c')
print(letters)