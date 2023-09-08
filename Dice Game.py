import tkinter as tk
import random

def roll_dice():
    num_dice = int(num_dice_entry.get())
    num_sides = int(num_sides_entry.get())

    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    result_label.config(text=f"Rolls: {rolls}")

# Create GUI
root = tk.Tk()
root.title("Dice Roller")

num_dice_label = tk.Label(root, text="Number of Dice:")
num_dice_label.pack()

num_dice_entry = tk.Entry(root, width=10)
num_dice_entry.pack()

num_sides_label = tk.Label(root, text="Number of Sides:")
num_sides_label.pack()

num_sides_entry = tk.Entry(root, width=10)
num_sides_entry.pack()

roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack()

result_label = tk.Label(root, text="Rolls: ")
result_label.pack()

root.mainloop()
