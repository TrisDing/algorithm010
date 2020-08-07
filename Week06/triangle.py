"""
120. Triangle <Medium>
https://leetcode.com/problems/triangle/
"""
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        1. state definition:
            dp[i][j] is the min total from (i,j) to bottom

        2. state transform:
            dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        """
        m = len(triangle)
        dp = [[0 for _ in range(m+1)] for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(i+1):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        return dp[0][0]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        """
        m = len(triangle)
        dp = [0 for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]

solution = Solution()
ans = solution.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])
print(ans) # 2 + 3 + 5 = 11