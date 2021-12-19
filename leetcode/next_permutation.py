from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        for i in range(0, n):
            j = n-i-1
            temp = nums[j]

            while j<n-1 and nums[j+1]<=temp:
                j += 1
            if j<n-1:
                nums[n-i-1] = nums[j+1]
                nums[j+1] = temp
                break
            else:
                j = n-i-1
                while j<n-1 and nums[j]<=temp:
                    nums[j] = nums[j+1]
                    j += 1
                nums[j] = temp


if __name__ == "__main__":
    nums = [1, 1, 3]
    Solution().nextPermutation(nums)
    print(nums)