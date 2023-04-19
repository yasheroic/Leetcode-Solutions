class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the given 2D matrix by 90 degrees clockwise in-place.

        Args:
            matrix (List[List[int]]): The input 2D matrix.
        """
        n = len(matrix)
        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for i in range(n):
            matrix[i] = matrix[i][::-1]
