import tkinter as tk

# Function to update the display
def click_button(value):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to perform calculations
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the display
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry field
entry = tk.Entry(root, width=16, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and position buttons
row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: click_button(x)
    tk.Button(root, text=button, width=4, height=2, command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create additional buttons (Clear and Equals)
tk.Button(root, text='Clear', width=10, height=2, command=clear).grid(row=row_val, column=0, columnspan=2)
tk.Button(root, text='=', width=10, height=2, command=evaluate).grid(row=row_val, column=2, columnspan=2)

# Start the main loop
root.mainloop()
