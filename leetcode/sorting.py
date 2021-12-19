from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_arrays(left, right):
            i = j = 0
            merged = []
            while i<len(left) and j<len(right):
                if i<len(left) and left[i]<right[j]:
                    merged.append(left[i])
                    i += 1
                elif j<len(right):
                    merged.append(right[j])
                    j += 1

        def merge_sort(left, right):
            if right-left==1:
                if left<right:
                    return nums[left]
                else:
                    return nums[right]
            mid = (left+right)//2
            return merge_arrays(merge_sort(left, mid), merge_sort(mid, right))

        n = len(nums)
        return merge_sort(0, n-1)
