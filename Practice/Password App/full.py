print('')
print("Welcome! If you are new, please press Enter to create an account. To sign in, type '1'.")
import logon


while True:
   while True:
       print(' ')
       print("Please select an option:")
       print("Type '1' for area calculator.")
       print("Type '2' for Magic 8 Ball.")
       print("Type '3' for MadLibs.")
       print("Type '4' for The Office Trivia Game.")
       print("Type '5' for Rock, Paper, Scissors.")
       print("Type 'more' for More Options.")
       print(' ')
       print("Or type 'sign off' to sign off.")
       print(' ')
       op=input("")
       if op == "1":
           import type_1


       if op == "2":
           import type_2


       if op == "3":
           import type_3


       if op == "4":
           import type_4

       if op == "5":
           import type_5


       if op == "magic cat":
           import magic_cat


       if op == "love":
           import love


       if op == "doggo":
           import doggo


       if op == "more":
           print(' ')
           print("MORE OPTIONS")
           print("Type any of the following for a surprise:")
           print(' ')
           print('- magic cat')
           print('- doggo')
           print('- love')
           print(' ')
           cont=input("Press Enter to select a new option.")
           print(' ')


       if op == "sign off":
           import signout
           break
   break