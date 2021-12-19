# Level: Hard
# The overall run time complexity should be O(log (m+n)).

from typing import List

def median(nums: List[int]):
    size = len(nums)
    if size%2==1:
        return float(nums[size//2])
    else:
        return (nums[size//2] + nums[size//2 - 1])/2.

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1)==0:
        return median(nums2)
    elif  len(nums2)==0:
        return median(nums1)
    return 0.

if __name__ == "__main__":
    l1 = [1, 2, 3, 4]
    l2:List[int] = []
    print(findMedianSortedArrays(l1, l2))