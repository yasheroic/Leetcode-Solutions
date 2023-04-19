class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]  # set to keep track of digits in each row
        cols = [set() for _ in range(9)]  # set to keep track of digits in each column
        boxes = [set() for _ in range(9)]  # set to keep track of digits in each 3x3 sub-box

        for i in range(9):
            for j in range(9):
                # Skip empty cells
                if board[i][j] == '.':
                    continue

                digit = board[i][j]

                # Check row
                if digit in rows[i]:
                    return False
                rows[i].add(digit)

                # Check column
                if digit in cols[j]:
                    return False
                cols[j].add(digit)

                # Check 3x3 sub-box
                box_idx = (i // 3) * 3 + j // 3
                if digit in boxes[box_idx]:
                    return False
                boxes[box_idx].add(digit)

        return True
