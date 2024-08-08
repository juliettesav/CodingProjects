import re

class Solution:
    def __init__(self, s):
        self.s = s 
    
    def isPalindrome(self): 
        self.s = re.sub(r'\W+', '', self.s).lower()
        return self.s == self.s[::-1]

my_string = Solution((input("What is your string? ")))
print(my_string.isPalindrome())