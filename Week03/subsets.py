"""
78. Subsets <Medium>
https://leetcode.com/problems/subsets/
"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(start = 0, track = []):
            res.append(track[:])

            for i in range(start, n):
                track.append(nums[i])
                backtrack(i + 1, track)
                track.pop()

        backtrack()
        return res

solution = Solution()
print(solution.subsets([1,2,3]))