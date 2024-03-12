import tkinter as tk
import random

def the_odds(player_odds):
    highest_num = int(input("What are the odds you do this dare? Between 1 and ___ "))
    print('')

    # computer chooses random number between 2 and highest number 
    computer_choice = random.randint(1,highest_num)

    # player inputs number between 2 and highest number 
    player_choice = int(input(f'Pick a number bewteen 1 and {highest_num}. '))

    print('')
    print(f'You chose the number {player_choice}.')
    print(f'The computer chose the number {computer_choice}.')
    print('')
    result = ""

    # if the same number, print player has to do the dare. 
    if computer_choice == player_choice: 
        print('Uh-oh!! Looks like you gotta do the dare! 😱')
        print('Too bad for you... 😈')

    # if a differnet number, print player doesn't have to do the dare. 
    else: 
        print("Ahh... Well, it looks like you're off the hook.")
        print('This time... 😈')

    print('')

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

#create main window 

root = tk.Tk()
root.geometry("312x130")

root.title("What are the Odds?")

#Create and place buttons 

rock_button = tk.Button(root, text="Rock 🪨", command=lambda: the_odds("Rock"))
rock_button.pack()