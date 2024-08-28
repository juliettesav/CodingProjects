fnln= input("What is your name? ")
#ln=input("What is your last name? ")
username=input("Please enter a username: ")


correct_pw=int(input("Create a password: "))
print(' ')
print("Hello ",fnln,"!",sep='')
#print("Welcome ",fn," ",ln,"!",sep='')
print("This program is a work in progress but we currently have a few games and activities")
print("for you to do! If you wish to continue, please sign in.")
print()
cont=input("Press Enter to sign in.")
print(' ')


enter_username=input("Please enter your username: ")
if enter_username == username:
    
    enter_pw=int(input("Please enter your password: "))


else:
    print("Incorrect username. Try again.")
    print(' ')
    enter_username=input("Please enter your username: ")
    if enter_username == username:
        enter_pw=int(input("Please enter your password: "))


if enter_pw == correct_pw:
    print("Access granted.")
    print(' ')


else:
    print("Access denied.")
    print("Please try again later.")