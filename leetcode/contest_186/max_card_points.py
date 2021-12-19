# Level: Medium

from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if n==1:
            return cardPoints[0]

        score = 0
        l = [0 for _ in range(n)]
        r = [0 for _ in range(n)]
        prev_l = 0
        prev_r = 0

        for i in range(k):
            l[i] = prev_l+cardPoints[i]
            r[n-i-1] = prev_r+cardPoints[n-i-1]             
            prev_l = l[i]
            prev_r = r[n-i-1]

        score = max(max(l), max(r))

        for i in range(k-1):
            score = max(score, l[i]+r[n-k+i+1])

        return score

if __name__ == "__main__":
    cards = [1,2,3,4,5,6,1]
    cards2 = [1,1,1,9,7,7,9]
    cards3 = [1,79,80,1,1,1,200,1]
    cards4 = [1,100,1,1]
    print(Solution().maxScore(cards3, 3))