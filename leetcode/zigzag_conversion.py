# Level: Medium
from typing import List

def convert(s, numRows: int) -> str:
    n = len(s)
    if n==0 or n<=numRows:
        return s
    z_size = 2*numRows-2
    out_s = ''
    for i in range(numRows):
        row: List[int] = []
        seq = list(range(i, n, z_size))
        gap2 = z_size-i*2
        # seq2 = list()
        # print(gap2)
        for c_i in seq:
            out_s += s[c_i]
            if gap2>0 and gap2<z_size and (c_i+gap2)<n:
                out_s += s[c_i+gap2]
    # print(len(out_s))
    return out_s

if __name__ == "__main__":
    ss = "PAYPALISHIRING"
    print(convert(ss, 3))