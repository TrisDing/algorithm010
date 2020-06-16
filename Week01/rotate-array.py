"""
189. Rotate Array <Easy>
https://leetcode.com/problems/rotate-array/
"""
from typing import List

class Solution:
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Solution #1: Brute Force, rotate k times
        Time: O(n*k)
        Space: O(1)
        """
        for i in range(k):
            prev = nums[len(nums) - 1]
            for j in range(len(nums)):
                nums[j], prev = prev, nums[j]

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Solution #2: Extra Array
        Time: O(n)
        Space: O(n)
        """
        n = len(nums)
        res = [0] * n
        for i in range(n):
            res[(i+k) % n] = nums[i]
        for i in range(n):
            nums[i] = res[i]

    def rotate3(self, nums: List[int], k: int) -> None:
        """
        Solution #3: Cyclic Replacement
        Time: O(n)
        Space: O(1)
        """
        n = len(nums)
        k %= n
        start = count = 0
        while count < n:
            curr, prev = start, nums[start]
            while True:
                next_idx = (curr + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                curr = next_idx
                count += 1
                if start == curr:
                    break
            start += 1

    def rotate4(self, nums: List[int], k: int) -> None:
        """
        Solution #3: Reverse
        Time: O(n): n elements are reversed a total of three times.
        Space: O(1)
        """
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

solution = Solution()

nums = [1,2,3,4,5,6,7]
solution.rotate1(nums, 1)
print(nums) # [7, 1, 2, 3, 4, 5, 6]

nums = [1,2,3,4,5,6,7]
solution.rotate2(nums, 2)
print(nums) # [6, 7, 1, 2, 3, 4, 5]

nums = [1,2,3,4,5,6,7]
solution.rotate3(nums, 3)
print(nums) # [5, 6, 7, 1, 2, 3, 4]

nums = [1,2,3,4,5,6,7]
solution.rotate4(nums, 4)
print(nums) # [4, 5, 6, 7, 1, 2, 3]
