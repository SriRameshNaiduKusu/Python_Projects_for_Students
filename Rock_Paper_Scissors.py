import tkinter as tk
import random

def play():
    choices = ['Rock', 'Paper', 'Scissors']
    player_choice = user_choice.get()
    computer_choice = random.choice(choices)

    result_label.config(text=f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        outcome_label.config(text="It's a tie!")
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        outcome_label.config(text="You win!")
    else:
        outcome_label.config(text="You lose!")

# Create GUI
root = tk.Tk()
root.title("Rock, Paper, Scissors")

user_choice_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
user_choice_label.pack()

user_choice = tk.StringVar(root)
user_choice.set("Rock")
user_choice_menu = tk.OptionMenu(root, user_choice, "Rock", "Paper", "Scissors")
user_choice_menu.pack()

play_button = tk.Button(root, text="Play", command=play)
play_button.pack()

result_label = tk.Label(root, text="Computer chose: ")
result_label.pack()

outcome_label = tk.Label(root, text="")
outcome_label.pack()

root.mainloop()
