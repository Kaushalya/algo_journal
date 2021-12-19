# Level: Medium

from typing import List, Tuple
import heapq


class Solution:
    def longestSubarray_iter(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        max_len = 0
        l = 0

        for i in range(n):
            while max(nums[l:i+1])-min(nums[l:i+1])>limit:
                l += 1

            max_len = max(max_len, i-l+1)
            print(l, i, max(nums[l:i+1])-min(nums[l:i+1]))
        return max_len
    

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        max_len = 0
        l = 0
        min_heap = []
        max_heap = []
    
        for i in range(n):
            heapq.heappush(min_heap, (nums[i], i))
            heapq.heappush(max_heap, (-nums[i], i))

            while -max_heap[0][0]-min_heap[0][0] > limit:
                while max_heap[0][1]<=l:
                    heapq.heappop(max_heap)
                while min_heap[0][1]<=l:
                    heapq.heappop(min_heap)
                l += 1

            max_len = max(max_len, i-l+1)
        return max_len




if __name__ == "__main__":
    nums = [10, 1, 2, 4, 7, 2]
    nums2 = [4, 2, 2, 2, 4, 4, 2, 2]
    nums3 = [4, 8, 5, 1, 7, 9]
    nums4 = [24,12,71,33,5,87,10,11,3,58,2,97,97,36,32,35,15,80,24,45,38,9,22,21,33,68,22,85,35,83,92,38,59,90,42,64,61,15,4,40,50,44,54,25,34,14,33,94,66,27,78,56,3,29,3,51,19,5,93,21,58,91,65,87,55,70,29,81,89,67,58,29,68,84,4,51,87,74,42,85,81,55,8,95,39]
    print(Solution().longestSubarray(nums4, 87))
