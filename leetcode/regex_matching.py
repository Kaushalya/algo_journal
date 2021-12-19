# Level: Hard

def isMatch(s: str, p: str) -> bool:
    if not p:
        return not s
    n_s = len(s)
    n_p = len(p)

    j = 0
    i = -1
    while i < n_s-1:
        i = i+ 1
        if j >= n_p:
            return False

        if p[j] == '*':
            while s[i]==s[i-1]:
                i += 1
            j += 1

        if p[j] == '.' or s[i] == p[j]:
            j += 1
            # continue
        elif s[i] != p[j] and j<n_p-1:
            j += 2
        else:
            return False

    return True

if __name__ == "__main__":
    ss = 'abbbbbc'
    p = 'a*'
    print(isMatch(ss, p))