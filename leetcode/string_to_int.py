# Level: Medium

def myAtoi(s: str) -> int:
    n = len(s)
    if n==0:
        return 0

    out = 0
    neg = 1
    begin = True

    c_map = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

    for c_i in s:
        if c_i == ' ':
            if begin:
                continue
            else:
                break
        else:
            if begin and c_i=='-':
                neg = -1
                begin = False
            elif begin and c_i=='+':
                begin = False
            elif c_i in c_map.keys():
                out = out*10 + c_map[c_i]
                begin = False
            else:
                break

    out *= neg
    int_max = 2**31-1
    int_min = -2**31

    if out>int_max:
        out = int_max
    elif out<int_min:
        out = int_min
    return out


if __name__ == "__main__":
    print(myAtoi('+255'))