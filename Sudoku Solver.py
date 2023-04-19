class Solution:
    def solveSudoku(self, board):
        """
        Solve the Sudoku puzzle by filling the empty cells using backtracking.

        Args:
            board (List[List[str]]): The Sudoku puzzle represented as a 9x9 matrix of strings.

        Returns:
            None
        """
        def is_valid(row, col, num):
            """
            Check if a number can be placed at a certain position on the Sudoku board.

            Args:
                row (int): The row index of the position to check.
                col (int): The column index of the position to check.
                num (str): The number to place at the position.

            Returns:
                bool: True if the number can be placed at the position, False otherwise.
            """
            # Check row
            for i in range(9):
                if board[row][i] == num:
                    return False

            # Check column
            for i in range(9):
                if board[i][col] == num:
                    return False

            # Check 3x3 sub-box
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False

            return True

        def solve():
            """
            Recursively solve the Sudoku puzzle.

            Returns:
                bool: True if the puzzle is solved, False otherwise.
            """
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            if is_valid(i, j, num):
                                board[i][j] = num
                                if solve():
                                    return True
                                else:
                                    board[i][j] = '.'  # Undo the placement if it doesn't lead to a solution
                        return False  # No number can be placed at the current position
            return True  # All cells are filled, puzzle is solved

        solve()
