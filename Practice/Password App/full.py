print('')
print("Welcome! If you are new, please press Enter to create an account. To sign in, type '1'.")
import login

def display_menu():
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

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            import type_1
            type_1.play()
            input("\nPress Enter to return to the menu.")
        elif choice == '2':
            import type_2
            type_2.play()
            input("\nPress Enter to return to the menu.")
        elif choice == '3':
            import type_3
            type_3.play()
            input("\nPress Enter to return to the menu.")
        elif choice == '4':
            import type_4
            type_4.play()
            input("\nPress Enter to return to the menu.")
        elif choice == '5':
            import type_5
            type_5.play()
            input("\nPress Enter to return to the menu.")
        elif choice == 'sign off':
            print("Exiting the game menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


'''#

print('')
print("Welcome! If you are new, please press Enter to create an account. To sign in, type '1'.")
import login

from type_1 import type_1_function


while True:
    import menu

    op=input("")

    if op == "1":
        type_1_function()

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

'''