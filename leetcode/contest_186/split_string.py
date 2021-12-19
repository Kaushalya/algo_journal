

class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        score = 0
        l = [0 for _ in range(n)]
        r = [0 for _ in range(n)]

        prev_l = 0
        prev_r = 0
        for i in range(n-1):
            l[i] = prev_l
            r[n-i-1] = prev_r
            if s[i] == '0':
                l[i] += 1
            if s[n-i-1] == '1':
                r[n-i-1] += 1                
            prev_l = l[i]
            prev_r = r[n-i-1]

        for i in range(n):
            score = max(score, l[i]+r[i])
        return score

if __name__ == "__main__":
    s = "011101"
    s2 = "00111"
    s3 = "111"
    print(Solution().maxScore(s))
