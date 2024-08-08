import re

class Solution:
    def __init__(self, s):
        self.s = s 
    
    def isPalindrome(self): 
        self.s = re.sub(r'\W+', '', self.s).lower()
        return self.s == self.s[::-1]

# Create an instance of the Solution class with user input
my_string = Solution(input("What is your string? "))

# Check and print whether the string is a palindrome
print(my_string.isPalindrome())