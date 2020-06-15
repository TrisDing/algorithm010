"""
283. Move Zeroes <Easy>
https://leetcode.com/problems/move-zeroes/
"""
from typing import List

class Solution:
    def moveZeroes1(self, nums: List[int]) -> None:
        """
        Solution #1: use append & remove API
        Time: O(n^2): append O(1) + remove O(n) worst case
        Space: O(1)
        """
        for elem in nums:
            if elem == 0:
                nums.append(0)
                nums.remove(0)

    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Solution #2: remember the next zero position and swap
        Time: O(n)
        Space: O(1)
        """
        next_zero_spot = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[next_zero_spot] = nums[next_zero_spot], nums[i]
                next_zero_spot += 1

    def moveZeroes3(self, nums: List[int]) -> None:
        """
        Solution #3: snowball solution by https://leetcode.com/olsh
        Time: O(n)
        Space: O(1)
        """
        snowBallSize = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                snowBallSize += 1 # the snowball gets bigger
            elif snowBallSize > 0:
                # swap the most left 0 with the element
                nums[i], nums[i - snowBallSize] = nums[i - snowBallSize], nums[i]

solution = Solution()

nums = [0,1,0,3,12]
solution.moveZeroes1(nums)
print(nums) # [1,3,12,0,0]

nums = [0,0,0,0,1]
solution.moveZeroes2(nums)
print(nums) # [1, 0, 0, 0, 0]

nums = [1,0,2,0,3,0]
solution.moveZeroes3(nums)
print(nums) # [1, 2, 3, 0, 0, 0]