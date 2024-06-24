#Check index 0
#Identify parentheses complement 
#If true, continue with index 2 (For loop and index +2) 

string = "()()"
i = 0 

#run a function that checks the bracket type and finds the pair 

round = ")"
square = "]"
curly = "}"

while i <= (len(string)-1): 
    if string[i] == "(":
        if string[i+1] == ")":
            #print(f"i equals {i}")
            status = "True"
            #print("True")
        else: 
            
            #print(f"i equals {i}")
            status = "False"
            #print("False")
        i = i + 2
        #print(f"i equals {i}")
print(status)