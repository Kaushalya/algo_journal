# Level: Medium
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return ['']
        
        out = ['(']
        for i in range(2*n-1):
            combs = []
            for s in out:
                l = sum([c=='(' for c in s])
                r = len(s) - l
                if i<2*n-2 and l<n:
                    combs.append(s+'(')
                    
                if l>r:
                    combs.append(s+')')
            out = combs
        return out
