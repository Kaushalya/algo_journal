# Level: Medium


def is_palindrome(s):
    if len(s) == 1:
        return True
    elif len(s) == 2 and s[0] == s[1]:
        return True
    elif len(s) == 2 and s[0] != s[1]:
        return False
    elif len(s) > 2 and s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False


def longestPalindrome_fast(s: str) -> str:
    n = len(s)

    if n == 0:
        return ''
    if n == 1:
        return s

    pal_len = [1]*n
    n_pals = [1]*n
    best_pal = ''

    for substr_len in range(2, n+1):
        for i in range(0, n-substr_len+1):
            if ((substr_len == 2 or pal_len[i+1] == substr_len-2 or n_pals[i] == substr_len-1)
                    and s[i] == s[i+substr_len-1]):
                pal_len[i] = substr_len
                n_pals[i] += 1

    max_len = 0
    for i, pl in enumerate(pal_len):
        if pl>max_len:
            max_len = pl
            best_pal = s[i:i+pl]

    return best_pal


def longestPalindrome(s: str) -> str:
    n = len(s)
    best_pal = ''

    if n == 0:
        return ''
    if n == 1:
        return s
    for i, c_i in enumerate(s):
        for j in range(i+1, n+1):
            if is_palindrome(s[i:j]) and len(best_pal)<(j-i):
                best_pal = s[i:j]
    return best_pal


if __name__ == "__main__":
    str1 = "ababaddggdfdsdsadjkdghgd"
    str2 = "abaa"
    str3 = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
    print(longestPalindrome_fast(str2))
    # print(is_palindrome('abad'))
