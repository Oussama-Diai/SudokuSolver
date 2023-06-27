################################################################################
# Filename: gui.py                                                   #
# author: Oussama Diai                                                         #
# Description: main file of the program, meant to make the graphical interface #
# Licence: None                                                                #
################################################################################

import tkinter as tk
from sudoku_solver import solve_sudoku

def solve():
    # Solve the Sudoku grid
    grid = read_grid_from_gui()
    if solve_sudoku(grid):
        update_gui_from_grid(grid)
    else:
        print("La grille n'a pas de solution.")

def read_grid_from_gui():
    # Read the Sudoku grid from the graphical interface
    grid = []
    for i in range(9):
        row = []
        for j in range(9):
            cell_value = cells[i][j].get()
            if cell_value.isdigit():
                row.append((int(cell_value), "blue"))
            else:
                row.append((0, "black"))
        grid.append(row)
    return grid

def update_gui_from_grid(grid):
    # update the graphical interface
    for i in range(9):
        for j in range(9):
            cell_value, cell_color = grid[i][j]
            cells[i][j].delete(0, tk.END)
            cells[i][j].insert(0, str(cell_value))
            cells[i][j].config(fg=cell_color)

def clear():
    # clear the values from the grid
    for i in range(9):
        for j in range(9):
            cells[i][j].delete(0, tk.END)
            cells[i][j].config(fg="black")

def create_grid_cells(root):
    # Create grid cells in the interface
    cells = []
    for i in range(9):
        row = []
        for j in range(9):
            cell = tk.Entry(root, width=2, font=("Arial", 20), justify="center")
            cell.grid(row=i, column=j)
            row.append(cell)
        cells.append(row)
    return cells

# Create the main window for the graphical interface
root = tk.Tk()
root.title("Sudoku Solver")

# Create grid cells
cells = create_grid_cells(root)

# Create Button for solving the puzzle and clearing the grid
solve_button = tk.Button(root, text="Solve", command=solve)
solve_button.grid(row=9, column=0, columnspan=4, padx=10, pady=5)
clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=9, column=5, columnspan=4, padx=10, pady=5)

# Launch the main loop for the graphical interface
root.mainloop()
