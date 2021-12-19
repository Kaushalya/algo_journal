from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(0, n//2):
            temp = [matrix[i][j] for j in range(n)]
            matrix[i][i:n-i] = [row[i] for row in matrix[::-1]][i:n-i]
            for j in range(i,n-i):
                matrix[j][i] = matrix[n-i-1][j]
            matrix[n-i-1][i:n-i] = [row[n-i-1] for row in matrix[::-1]][i:n-i]
            print(temp)
            for j in range(i,n-i):
                matrix[j][n-i-1] = temp[j]

if __name__ == "__main__":
    matrix = [[5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]
    Solution().rotate(matrix)
    print(matrix)