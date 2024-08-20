# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

## 1. Open brackets must be closed by the same type of brackets.
## 2. Open brackets must be closed in the correct order.
## 3. Every close bracket has a corresponding open bracket of the same type.


def isValid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack

string = input("Input a string with any combination of these parentheses (){}[] ")
print(isValid(string))