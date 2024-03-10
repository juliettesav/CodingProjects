import random
# Game Title 
print('')
print("What are the odds?!")
print('')
print('')

# Game Description 
print('The game "What are the odds?!" asks the player how likely they are to complete a dare.')

# Think of a dare. What are the odds that you complete this dare? Between 2 and what number? 
print("First, think of a dare. Lock it in. No going back now!")
print('')

# input highest number 
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

# if the same number, print player has to do the dare. 
if computer_choice == player_choice: 
    print('Uh-oh!! Looks like you gotta do the dare! 😱')
    print('Too bad for you... 😈')

# if a differnet number, print player doesn't have to do the dare. 
else: 
    print("Ahh... Well, it looks like you're off the hook.")
    print('This time... 😈')

print('')