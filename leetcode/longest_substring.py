#Level: Medium
from typing import Set, Dict

def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0
        
    max_len = [1]*len(s)
    for i in range(1, len(s)):
        for j in range(i-1,-1, -1):
            if s[j] == s[i]:
                max_len[i] = min(max_len[i-1]+1, i-j)
                break
            elif j==0:
                max_len[i] = min(max_len[i-1]+1, i+1)
        # max_len = max(max_len, i+1)
    
    return max(max_len)


def lengthOfLongestSubstringFaster(s: str) -> int:
    ans = 0
    i = 0
    j = 0
    n = len(s)
    c_set: Set[str] = set()

    while i<n and j<n:
        if s[j] not in c_set:
            c_set.add(s[j])
            j += 1
            ans = max(ans, j-i)
        else:
            # keep removing chars from the beginning until
            # no duplicates are present
            c_set.remove(s[i])
            i += 1

    return ans


def lengthOfLongestSubstringFastest(s: str) -> int:
    ans = 0
    i = 0
    n = len(s)
    c_dict: Dict[str, int] = dict()

    for j in range(n):
        if s[j] in c_dict:
            i = max(c_dict[s[j]], i)
        
        c_dict[s[j]] = j+1
        ans = max(ans, j-i+1)

    return ans


if __name__ == "__main__":
    str1 = "abcabcbb"
    str2 = "b"
    str3 = "pwwkew"
    str4 = ""
    str5 = "tmmzuxt"
    s = str5
    print(lengthOfLongestSubstring(s))
    print(lengthOfLongestSubstringFaster(s))
    print(lengthOfLongestSubstringFastest(s))