################################################################################
# Filename: sudoku_solver.py                                                   #
# author: Oussama Diai                                                         #
# Description: file for the sudoku solving algorithm                           #
# Licence: None                                                                #
################################################################################

def solve_sudoku(grid):
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = (num, "black")
            if solve_sudoku(grid):
                return True
            grid[row][col] = (0, "blue")

    return False

def is_valid_move(grid, row, col, num):
    # Verify whether the digit is the same in the row or column
    for i in range(9):
        if grid[row][i][0] == num or grid[i][col][0] == num:
            return False

    # Verify whether the digit already exists within the 3x3 sub-grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j][0] == num:
                return False

    return True

def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j][0] == 0:
                return (i, j)
    return None

