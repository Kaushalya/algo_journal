"""[summary]
You are given a 2D integer grid of size m x n and an integer x. In one operation, 
you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. 
If it is not possible, return -1.
"""

from itertools import chain
from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        """[summary]
        Sort the grid to find the median. Sorting is O(nlogn)
        Args:
            grid (List[List[int]]): [description]
            x (int): [description]

        Returns:
            int: [description]
        """
        grid = chain(*grid)
        grid = sorted(grid)
        mid = len(grid)//2
        mid_v = grid[mid]
        n_ops = 0
        
        for v in grid:
            dif = abs(mid_v-v)
            if dif%x:
                return -1
            n_ops += dif//x
        return n_ops

    def minOperations_quickselect(self, grid: List[List[int]], x: int) -> int:
        """[summary]
        Use quickselect algorithm to make finding the median efficient.
        Args:
            grid (List[List[int]]): [description]
            x (int): [description]

        Returns:
            int: [description]
        """
        raise NotImplementedError

if __name__ == '__main__':
    grid = []
    