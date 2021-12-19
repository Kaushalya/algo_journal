# Level: Easy

def romanToInt(s: str) -> int:
    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    number = 0
    n = len(s)

    for i, c in enumerate(s):
        c_int = roman_dict[c]
        if i<n-1:
            if c_int==1 and s[i+1] in ('V', 'X'):
                c_int = -1
            elif c_int==10 and s[i+1] in ('L', 'C'):
                c_int = -10
            elif c_int==100 and s[i+1] in ('D', 'M'):
                c_int = -100
        number += c_int
    return number


if __name__ == "__main__":
    a = 'MCMXCIV'
    print(romanToInt(a))