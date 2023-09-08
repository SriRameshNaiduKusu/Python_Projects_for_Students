import tkinter as tk

def print_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))

def is_valid_move(grid, row, col, num):
    # Check row
    if num in grid[row]:
        return False

    # Check column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check subgrid
    subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(subgrid_row, subgrid_row + 3):
        for j in range(subgrid_col, subgrid_col + 3):
            if grid[i][j] == num:
                return False

    return True

def find_empty_location(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def solve_sudoku(grid):
    empty_location = find_empty_location(grid)

    if not empty_location:
        return True

    row, col = empty_location

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False

def validate_input(input_str):
    if len(input_str) != 81 or not input_str.isdigit():
        return False
    return True

def create_grid_from_input(input_str):
    grid = [[int(input_str[i*9 + j]) for j in range(9)] for i in range(9)]
    return grid

def solve_and_update():
    input_str = input_entry.get()
    if not validate_input(input_str):
        result_label.config(text="Invalid input. Please enter 81 digits.")
        return

    sudoku_grid = create_grid_from_input(input_str)

    if solve_sudoku(sudoku_grid):
        result_label.config(text="Solution found:")
        print_grid(sudoku_grid)
    else:
        result_label.config(text="No solution exists")

# Create GUI
root = tk.Tk()
root.title("Sudoku Solver")

input_label = tk.Label(root, text="Enter Sudoku puzzle (81 digits):")
input_label.pack()

input_entry = tk.Entry(root, width=20)
input_entry.pack()

solve_button = tk.Button(root, text="Solve Sudoku", command=solve_and_update)
solve_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
