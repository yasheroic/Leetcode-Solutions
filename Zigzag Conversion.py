class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [''] * numRows
        direction = -1
        current_row = 0
        
        for c in s:
            rows[current_row] += c
            
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1
            
            current_row += direction
        
        return ''.join(rows)
