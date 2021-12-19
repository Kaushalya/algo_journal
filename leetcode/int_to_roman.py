# Level: Medium

def intToRoman(num: int) -> str:
    mapping = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    out = ''
    keys = list(mapping.keys())[::-1]

    for i, key in enumerate(keys):
        a = num//key

        if num==9:
            out += 'IX'
            break
        elif num<100 and num>=90:
            out += 'XC'
            num -= 90
        elif num<1000 and num>=900:
            out += 'CM'
            num -= 900
        elif a==4:
            out += mapping[key]+mapping[keys[i-1]]
        elif a>0:
            out += a*mapping[key]
        num = num%key

    return out


if __name__ == "__main__":
    print(intToRoman(493))
