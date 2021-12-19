# Level: Easy

def reverse(x: int) -> int:
    neg = 1
    if x == 0:
        return 0
    if x < 0:
        x *= -1
        neg = -1

    n_digits = 1
    x_copy = x

    while x_copy//10 > 0:
        n_digits += 1
        x_copy = x_copy//10

    y = 0
    for i in range(n_digits):
        y = 10*y + x % 10
        x = x//10

    if y >= 2**31:
        y = 0

    return y*neg

if __name__ == "__main__":
    d1 = 1563847412
    print(reverse(d1))
