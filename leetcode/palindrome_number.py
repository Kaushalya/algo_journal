# Level: Easy

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    y = x
    back_num = 0
    while y > 0:
        back_num = back_num * 10 + y%10
        y = y//10
    
    if x == back_num:
        return True

    return False

if __name__ == "__main__":
    x = 12321
    print(isPalindrome(x))