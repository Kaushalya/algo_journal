from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        rows = len(nums)
        cols = max([len(a) for a in nums])
        n = sum([len(a) for a in nums])
        diags = [0 for _ in range(n)]

        print(n)

        for row in range(rows):
            continue

        return [0]


if __name__ == "__main__":
    ll = [[1,2,3],[4,5,6],[7,8,9]]
    print(Solution().findDiagonalOrder(ll))