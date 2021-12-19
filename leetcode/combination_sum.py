# Level: Medium

from collections import defaultdict
from typing import List

class Solution:
    def combinationSum_recursion(self, candidates: List[int], target: int) -> List[List[int]]:
        out:List[int] = []
        candidates.sort()

        def partial_sum(partial, rem, idx):
            for i, cand in enumerate(candidates[idx:]):
                if rem==cand:
                    out.append(partial+[cand])
                    break
                    # return partial+[cand]
                if rem<cand:
                    break
                partial_sum(partial+[cand], rem-cand, idx+i)
        partial_sum([], target, 0)

        return out
    
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        partial_sum = set()
        partial_sum.add(0)
        combs = defaultdict(list)
        candidates.sort()
        
        # partial_sum.add(0)
        combs[0] = []

        for cand in candidates:
            partial_sum = list(combs.keys())
            # partial_sum.append(0)
            for ps in partial_sum:
                if ps+cand<=target:
                    # if ps+cand not in combs:
                    partial_sum.append(ps+cand)
                    if ps>0 and ps in combs:
                        combs[ps+cand].extend([l+[cand] for l in combs[ps]])
                    else:
                        combs[ps+cand].append([cand])

        return combs[target]


if __name__ == "__main__":
    ar = [7, 3, 2]
    # print(Solution().combinationSum(ar, 18))
    print(Solution().combinationSum_recursion(ar, 18))