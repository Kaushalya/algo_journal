# Medium: 89
from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        codes = []
        n_codes = 2**n
        gray = set([2**i for i in range(n)])
        codes = list(range(0, n_codes))
        
        for i in range(0, n_codes-1):
            r = i+1
            while codes[r]^codes[i] not in gray:
                # print(i, r, codes[r]^codes[i])
                r += 1
                # r %= n_codes
            if r>i+1:
                print(i, r)
                codes[i+1], codes[r] = codes[r], codes[i+1]
                   
        return codes

if __name__ == "__main__":
    print(Solution().grayCode(5))