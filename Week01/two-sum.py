"""
1. Two Sum <Easy>
https://leetcode.com/problems/two-sum/
"""
from typing import List

class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        """
        Solution #1: brute-force
        Time: O(n^2)
        Space: O(1)
        """
        l = len(nums)
        for i in range(0, l - 1):
            for j in range(i + 1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """
        Solution #2: cache, 2 iteration
        Time: O(n)
        Space: O(n)
        """
        dic = {}
        for i in range(len(nums)):
            dic[target - nums[i]] = i

        for i, num in enumerate(nums):
            if num in dic and dic[num] != i:
                return [i, dic[num]]

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        """
        Solution #3: cache, 1 iteration
        Time: O(n)
        Space: O(n)
        """
        dic = {}
        for i, n in enumerate(nums):
            if n in dic:
                return [dic.get(n), i]
            else:
                dic[target - n] = i

solution = Solution()
lst = [2, 7, 11, 15]
target = 9
ans1 = solution.twoSum1(lst, target)
ans2 = solution.twoSum1(lst, target)
ans3 = solution.twoSum1(lst, target)

print(ans1) # [0, 1]
print(ans2) # [0, 1]
print(ans3) # [0, 1]