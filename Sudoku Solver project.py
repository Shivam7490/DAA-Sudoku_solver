#Sudoku solver using Backtracking method.
class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def solve(self):
        empty_cell = self.find_empty()
        if not empty_cell:
            return True  
        row, col = empty_cell

        for num in range(1, 10):
            if self.is_valid(num, row, col):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = 0  

        return False

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col  # Return the first empty cell (row, col)
        return None

    def is_valid(self, num, row, col):
        # Check row
        for c in range(9):
            if self.board[row][c] == num:
                return False

        # Check column
        for r in range(9):
            if self.board[r][col] == num:
                return False

        # Check 3x3 sub-grid
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if self.board[r][c] == num:
                    return False

        return True

    def print_board(self):
        for row in range(9):
            if row % 3 == 0 and row != 0:
                print("-" * 21)  # Print a horizontal divider after every 3 rows
            for col in range(9):
                if col % 3 == 0 and col != 0:
                    print(" | ", end="")  # Print a vertical divider after every 3 columns
                print(self.board[row][col], end=" ")
            print()


# Example usage
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

solver = SudokuSolver(board)
if solver.solve():
    print("Sudoku solved:")
    solver.print_board()
else:
    print("No solution exists.")
