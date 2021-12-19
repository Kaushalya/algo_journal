# Level: Medium
from typing import List

def maxArea_slow(height: List[int]) -> int:
    if len(height)<2:
        return 0

    n = len(height)
    area = 0

    for i in range(n-1):
        for j in range(i+1, n):
            area = max(area, min(height[i], height[j]) * (j-i))
    return area


def maxArea(height: List[int]) -> int:
    if len(height)<2:
        return 0

    n = len(height)
    area = 0
    i = 0
    j = n-1

    while i<j:
        area = max(area, min(height[i], height[j])*(j-i))

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    print([i, j])
    return area

if __name__ == "__main__":
    a = [1,8,6,2,5,4,8,3,7]
    b = [5, 3]
    c = [2,3,4,5,18,17,6]
    print(maxArea(a))
    print(maxArea_slow(a))