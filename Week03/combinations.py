"""
77. Combinations <Medium>
https://leetcode.com/problems/combinations/
"""
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        if k <= 0 or n <= 0:
            return res

        def backtrack(start = 1, path = []):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack()
        return res

solution = Solution()
print(solution.combine(4, 2))