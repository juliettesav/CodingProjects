print('')
print("Welcome! If you are new, please press Enter to create an account. To sign in, type '1'.")
enter=input('')


while True:
   if enter == "1":
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


#END OF SAVED ACCOUNTS
       break
   while False:
       print("Incorrect username. Press Enter to try again.")
       print(' ')
       retry=input("")
       break
#END OF SAVED ACCOUNTS FILE




#CREATE AN ACCOUNT
      
   if enter == '':
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


       break


#END OF CREATE AN ACCOUNT


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
           from rpsgame import *
           print(' ')
           cont=input("Press Enter to select a new option.")
           print(' ')


       if op == "magic cat":
           print(' ')
           print("This is the magic cat! He will bring you good luck!")
           print(".∧＿∧")
           print("( ･ω･｡)つ━☆・*。")
           print("⊂　 ノ 　　　・゜+.")
           print("しーＪ　　　°。+ *´¨)")
           print("　　　　　　　　　.· ´¸.·*´¨) ¸.·*¨)")
           print("　　　　　　　　　　(¸.·´ (¸.·’* ☆")
           print(' ')
           cont=input("Press Enter to select a new option.")
           print(' ')


       if op == "love":
           print(' ')
           print("░░▄███▄███▄")
           print("░░█████████")
           print("░░▒▀█████▀░")
           print("░░▒░░▀█▀")
           print("░░▒░░█░")
           print("░░▒░█")
           print("░░░█")
           print("░░█░░░░███████")
           print("░██░░░██▓▓███▓██▒")
           print("██░░░█▓▓▓▓▓▓▓█▓████")
           print("██░░██▓▓▓(◐)▓█▓█▓█")
           print("███▓▓▓█▓▓▓▓▓█▓█▓▓▓▓█")
           print("▀██▓▓█░██▓▓▓▓██▓▓▓▓▓█")
           print("░▀██▀░░█▓▓▓▓▓▓▓▓▓▓▓▓▓█")
           print("░░░░▒░░░█▓▓▓▓▓█▓▓▓▓▓▓█")
           print("░░░░▒░░░█▓▓▓▓█▓█▓▓▓▓▓█")
           print("░▒░░▒░░░█▓▓▓█▓▓▓█▓▓▓▓█")
           print("░▒░░▒░░░█▓▓▓█░░░█▓▓▓█")
           print("░▒░░▒░░██▓██░░░██▓▓██")
           print("████████████████████████")
           print("█▄─▄███─▄▄─█▄─█─▄█▄─▄▄─█")
           print("██─██▀█─██─██─█─███─▄█▀█")
           print("▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀")
           print(' ')
           cont=input("Press Enter to select a new option.")
           print(' ')


       if op == "doggo":
           print(' ')
           print("          ██████████                                      ")
           print("    ▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒████████                ██████        ")
           print("  ▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒██              ██▓▓▒▒██      ")
           print("  ▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒████              ██▓▓▒▒██    ")
           print("▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓██            ██▓▓▒▒██    ")
           print("▓▓▒▒  ▒▒▒▒▒▒▒▒▒▒  ██▓▓▓▓▒▒▒▒▒▒▒▒▓▓██            ██▓▓▒▒██  ")
           print("▓▓▒▒██▒▒▒▒▒▒▒▒▒▒████▓▓▓▓▒▒▒▒▒▒▒▒▓▓██            ██▓▓▒▒██  ")
           print("▓▓▒▒██▒▒▒▒▒▒▒▒▒▒████▓▓▓▓▒▒▒▒▒▒▒▒▓▓██            ██▓▓▒▒██  ")
           print("  ▓▓░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒██            ██▓▓▓▓▒▒██  ")
           print("  ▓▓▒▒▒▒▒▒▒▒░░░░▓▓▓▓▓▓▓▓▒▒▒▒▒▒██        ██████████▒▒██    ")
           print("▓▓  ▒▒██▒▒░░░░░░░░░░░░▓▓▓▓▒▒██      ████▒▒▒▒▒▒▒▒▓▓██      ")
           print("▓▓██████░░░░░░░░░░░░░░▒▒▓▓▓▓████████▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██    ")
           print("▓▓░░░░░░░░░░░░░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██    ")
           print("  ▓▓▓▓▓▓░░░░▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██  ")
           print("      ▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██  ")
           print("            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▓▓██  ")
           print("            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▓▓██  ")
           print("              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████████▓▓██▒▒▒▒▒▒████")
           print("              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██    ▓▓▓▓▓▓▓▓██▒▒▒▒▒▒██")
           print("              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    ▓▓▓▓▓▓████  ▒▒  ▒▒██")
           print("            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    ▓▓▓▓▓▓██    ▒▒  ░░██")
           print("            ▒▒  ▒▒██    ▒▒▒▒▒▒▒▒██  ░░░░░░██      ▒▒  ░░██")
           print("          ▒▒  ▒▒▒▒██    ▒▒  ▒▒██    ▒▒▒▒▒▒▒▒    ▒▒  ░░▒▒  ")
           print("          ▒▒▒▒▒▒▒▒    ▒▒  ▒▒▒▒██                ▒▒▒▒▒▒▒▒  ")
           print("                      ▒▒▒▒▒▒▒▒                            ")
           print(' ')
           cont=input("Press Enter to select a new option.")
           print(' ')


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
           print(' ')
           print("Thank you for playing, ",username,"!",sep='')
           print("See you next time!")
           break
   break