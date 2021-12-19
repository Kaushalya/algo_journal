# Level: Medium
from typing import List


class Solution:
    def setZeroes_const(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        for i, row in enumerate(matrix):
            row_zero = False
            for j, col in enumerate(row):
                if not col:
                    row_zero = True
                while False:
                    # TODO fix this
                    pass
            if row_zero:
                matrix[i] = [0]*n

        for row in rows:
            matrix[row] = [0]*n

        for col in cols:
            for i in range(m):
                matrix[i][col] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Space = O(n+m)
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        m = len(matrix)
        n = len(matrix[0])

        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if not col:
                    rows.append(i)
                    cols.append(j)

        for row in rows:
            matrix[row] = [0]*n

        for col in cols:
            for i in range(m):
                matrix[i][col] = 0


if __name__ == "__main__":
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    Solution().setZeroes(matrix)
    print(matrix)
