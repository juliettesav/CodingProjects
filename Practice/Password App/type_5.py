def play():
    import tkinter as tk
    import random

    def play_game(player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        result = ""
        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
            (player_choice == "Paper" and computer_choice == "Rock") or \
            (player_choice == "Scissors" and computer_choice == "Paper"):
            result = "You win!"
        else:
            result = "Computer wins!"

        result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

    # Create the main window
    root = tk.Tk()
    root.geometry("312x130")
    root.title("Rock Paper Scissors")

    # Create and place the buttons
    rock_button = tk.Button(root, text="Rock 🪨", command=lambda: play_game("Rock"))
    rock_button.pack()

    paper_button = tk.Button(root, text="Paper 📜", command=lambda: play_game("Paper"))
    paper_button.pack()

    scissors_button = tk.Button(root, text="Scissors ✂️", command=lambda: play_game("Scissors"))
    scissors_button.pack()

    # Create a label to display the result
    result_label = tk.Label(root, text="")
    result_label.pack()

    # Start the GUI
    root.mainloop()

    print(' ')