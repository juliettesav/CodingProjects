#Check index 0
#Identify parentheses complement 
#If true, continue with index 2 (For loop and index +2) 

string = "()()"
i = 0 

#Pairs 
round = ")"
square = "]"
curly = "}"


#run a function that checks the bracket type and finds the pair 
#if index == pair

def pair(round, square, curly):
    if string[i] == "(":
        #round = ")"
        return round
    if string[i] == "[":
        #square = "]"
        return square
    if string[i] == "{":
        #curly = "}"
        return curly
    

while i <= (len(string)-1): 
    if string[i] == pair: 
        True

while i <= (len(string)-1): 
    if string[i] == "(":
        if string[i+1] == ")":
            status = "True"
        else: 
            status = "False"
        i = i + 2
print(status)


'''
while i <= (len(string)-1): 
    if string[i] == "(":
        if string[i+1] == ")":
            status = "True"
        else: 
            status = "False"
        i = i + 2
print(status)
'''