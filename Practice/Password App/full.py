def login():
    import login

login()

def main():
    while True:
        import menu
        menu.display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            import type_1
            type_1.play()
        elif choice == '2':
            import type_2
            type_2.play()
        elif choice == '3':
            import type_3
            type_3.play()
        elif choice == '4':
            import type_4
            type_4.play()
        elif choice == '5':
            import type_5
            type_5.play()
        elif choice == 'more':
            import menu
            menu.display_more()
            if choice == "magic cat":
                import magic_cat
                magic_cat.display()
        elif choice == 'sign off':
            print('')
            print("Exiting the game menu.")
            print("Thank you for playing, ","{username}","!",sep='')
            #print("See you next time!")
            print('')
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

