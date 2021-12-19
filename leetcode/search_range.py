# Level: Medium

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums or target<nums[0] or target>nums[-1]:
            return [-1, -1]
        n = len(nums)
        l = 0
        r = n-1
        
        if n==1 and nums[0]==target:
            return [0, 0]

        while l<r:
            mid = (l+r)//2

            if nums[l]==target and nums[r]==target:
                while l>=0 and nums[l]==target:
                    l -= 1
                while r<n and nums[r]==target:
                    r += 1
                return [l+1, r-1]
            elif nums[l]==target and r-l==1:
                r = l
                while l>=0 and nums[l]==target:
                    l -= 1
                return [l+1, r]
            elif nums[r]==target and r-l==1:
                l = r
                while r<n and nums[r]==target:
                    r += 1
                return [l, r-1]

            if r-l==1:
                break
            
            if nums[mid]<target:
                l = mid
            else:
                r = mid
                
        return [-1, -1]

if __name__ == "__main__":
    a = [5,7,7,8,8,10]
    print(Solution().searchRange(a, 8))
            