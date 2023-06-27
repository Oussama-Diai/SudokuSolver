import tkinter as tk
from sudoku_solver import solve_sudoku, print_grid

def solve():
    # Résoudre la grille de Sudoku
    grid = read_grid_from_gui()
    solve_sudoku(grid)
    update_gui_from_grid(grid)

def read_grid_from_gui():
    # Lire la grille de Sudoku à partir de l'interface graphique
    grid = []
    for i in range(9):
        row = []
        for j in range(9):
            cell_value = cells[i][j].get()
            if cell_value.isdigit():
                row.append(int(cell_value))
            else:
                row.append(0)
        grid.append(row)
    return grid

def update_gui_from_grid(grid):
    # Mettre à jour l'interface graphique avec la grille résolue
    for i in range(9):
        for j in range(9):
            cells[i][j].delete(0, tk.END)
            cells[i][j].insert(0, str(grid[i][j]))

def clear():
    # Effacer les valeurs de la grille
    for i in range(9):
        for j in range(9):
            cells[i][j].delete(0, tk.END)

def create_grid_cells(root):
    # Créer les cellules de la grille dans l'interface graphique
    cells = []
    for i in range(9):
        row = []
        for j in range(9):
            cell = tk.Entry(root, width=2, font=("Arial", 20))
            cell.grid(row=i, column=j)
            row.append(cell)
        cells.append(row)
    return cells

# Créer la fenêtre principale de l'interface graphique
root = tk.Tk()
root.title("Sudoku Solver")

# Créer les cellules de la grille
cells = create_grid_cells(root)

# Créer les boutons de résolution et d'effacement
solve_button = tk.Button(root, text="Solve", command=solve)
solve_button.grid(row=9, column=0, columnspan=4, padx=10, pady=5)
clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=9, column=5, columnspan=4, padx=10, pady=5)

# Lancer la boucle principale de l'interface graphique
root.mainloop()

