# Level: Medium

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(p, q):
            # print(p, q)
            if nums[p]==target:
                return p
            elif nums[q]==target:
                return q
            if p==q or q-p == 1:
                return -1
            
            mid = (p+q)//2
            if nums[mid] >= nums[q]:
                if target>nums[p] and target<nums[mid]:
                    return binary_search(p, mid)
                else:
                    return binary_search(mid, q)
            else:
                if target>nums[mid] and target<nums[q]:
                    return binary_search(mid, q)
                else:
                    return binary_search(p, mid)
        
        if not nums:
            return -1
        
        return binary_search(0, len(nums)-1)
        