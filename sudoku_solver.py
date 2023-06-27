def find_empty_location(grid):
    # Trouver la prochaine case vide dans la grille
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None

def is_valid(grid, row, col, num):
    # Vérifier si un nombre est valide dans la position spécifiée
    return (
        not used_in_row(grid, row, num)
        and not used_in_col(grid, col, num)
        and not used_in_box(grid, row - row % 3, col - col % 3, num)
    )

def used_in_row(grid, row, num):
    # Vérifier si le nombre est déjà utilisé dans la même ligne
    return num in grid[row]

def used_in_col(grid, col, num):
    # Vérifier si le nombre est déjà utilisé dans la même colonne
    for row in range(9):
        if grid[row][col] == num:
            return True
    return False

def used_in_box(grid, box_start_row, box_start_col, num):
    # Vérifier si le nombre est déjà utilisé dans la même boîte 3x3
    for row in range(3):
        for col in range(3):
            if grid[row + box_start_row][col + box_start_col] == num:
                return True
    return False

def solve_sudoku(grid):
    # Résoudre la grille de Sudoku en utilisant la méthode de backtracking
    empty_location = find_empty_location(grid)
    if not empty_location:
        return True  # La grille est résolue, toutes les cases sont remplies

    row, col = empty_location
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0  # Annuler l'assignation si la solution n'est pas trouvée

    return False

def print_grid(grid):
    # Afficher la grille
    for row in range(9):
        for col in range(9):
            print(grid[row][col], end=" ")
        print()

