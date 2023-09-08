import tkinter as tk
import random

# Function to start a new game
def new_game():
    global board
    board = [[0 for _ in range(4)] for _ in range(4)]
    add_new_tile()
    add_new_tile()
    update_board()

# Function to add a new tile
def add_new_tile():
    row, col = random.choice([(i, j) for i in range(4) for j in range(4) if board[i][j] == 0])
    board[row][col] = random.choice([2, 4])

# Function to update the GUI
def update_board():
    for i in range(4):
        for j in range(4):
            cell = board[i][j]
            if cell == 0:
                labels[i][j].config(text='', bg='lightgray')
            else:
                labels[i][j].config(text=str(cell), bg=colors[cell], fg='white')

# Function to move the tiles
def move(direction):
    global board
    if direction == 'up':
        board = [list(row) for row in zip(*board)]
        move_left()
        board = [list(row) for row in zip(*board)]
    elif direction == 'down':
        board = [list(row[::-1]) for row in board]
        move_left()
        board = [list(row[::-1]) for row in board]
    elif direction == 'left':
        move_left()
    elif direction == 'right':
        board = [row[::-1] for row in board]
        move_left()
        board = [row[::-1] for row in board]
    add_new_tile()
    update_board()

# Function to handle left movement
def move_left():
    global board
    for i in range(4):
        row = board[i]
        row = [cell for cell in row if cell != 0]
        row += [0] * (4 - len(row))
        for j in range(3):
            if row[j] == row[j+1] and row[j] != 0:
                row[j] *= 2
                row[j+1] = 0
        row = [cell for cell in row if cell != 0]
        row += [0] * (4 - len(row))
        board[i] = row

# Define colors for different tile values
colors = {
    2: '#eee4da', 4: '#ede0c8', 8: '#f2b179',
    16: '#f59563', 32: '#f67c5f', 64: '#f65e3b',
    128: '#edcf72', 256: '#edcc61', 512: '#edc850',
    1024: '#edc53f', 2048: '#edc22e'
}

# Create the main window
root = tk.Tk()
root.title("2048 Game")

# Initialize the board and labels
board = [[0 for _ in range(4)] for _ in range(4)]
labels = [[tk.Label(root, font=('Arial', 32), width=4, height=2, relief='ridge') for _ in range(4)] for _ in range(4)]

# Place the labels on the grid
for i in range(4):
    for j in range(4):
        labels[i][j].grid(row=i, column=j, padx=5, pady=5)

# Create buttons for controls
new_game_button = tk.Button(root, text="New Game", command=new_game, font=('Arial', 12))
new_game_button.grid(row=4, column=0, columnspan=2, pady=10)
up_button = tk.Button(root, text="Up", command=lambda: move('up'), font=('Arial', 12))
up_button.grid(row=4, column=2, pady=10)
down_button = tk.Button(root, text="Down", command=lambda: move('down'), font=('Arial', 12))
down_button.grid(row=4, column=3, pady=10)
left_button = tk.Button(root, text="Left", command=lambda: move('left'), font=('Arial', 12))
left_button.grid(row=5, column=0, pady=10)
right_button = tk.Button(root, text="Right", command=lambda: move('right'), font=('Arial', 12))
right_button.grid(row=5, column=1, pady=10)

# Start a new game
new_game()

# Start the main loop
root.mainloop()
