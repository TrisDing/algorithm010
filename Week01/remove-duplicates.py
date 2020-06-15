"""
26. Remove Duplicates from Sorted Array <Easy>
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Solution #1: Two Pointers
        """
        if len(nums) == 0:
            return 0

        p = 0
        for q in range(1, len(nums)):
            if nums[q] > nums[p]:
                p += 1
                nums[p] = nums[q]

        return p + 1

solution = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
ans = solution.removeDuplicates(nums)
print(nums[:ans]) # [0, 1, 2, 3, 4]