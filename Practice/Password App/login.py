username=input("Please enter your username: ")


#USER JULIETTESAV
if username == "juliettesav":
    enter_pw=int(input("Please enter your password: "))


    if enter_pw == 162387:
        print("Access granted.")
        print(' ')
        
#USER GUEST
if username == "guest":
    enter_pw=input("Please enter your password: ")


    if enter_pw == '':
        print("Access granted.")
        print(' ')


#USER TEMPLATE
if username == "username":
    enter_pw=input("Please enter your password: ")


    if enter_pw == 'password':
        print("Access granted.")
        print(' ')