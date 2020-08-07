"""
62. Unique Paths <Medium>
https://leetcode.com/problems/unique-paths/
"""
from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        status = {
            dp[i][j] = 1, i = 0
            dp[i][j] = 1, j = 0
            dp[i][j] = dp[i-1][j] + dp[i][j-1], i >= 1, j >= 1
        }
        """
        dp = [[1]*n] + [[1] + [0]*(n-1) for _ in range(m-1)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        status = {
            dp[i][j] = 0, i = 0, obstacleGrid[i][j] == 0
            dp[i][j] = 1, j = 0, obstacleGrid[i][j] == 1
            dp[i][j] = 0, i = 0, obstacleGrid[i][j] == 0
            dp[i][j] = 1, j = 0, obstacleGrid[i][j] == 1
            dp[i][j] = dp[i-1][j] + dp[i][j-1], i >= 1, j >= 1
        }
        """
        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        for i in range(1, m):
            if obstacleGrid[i][0] == 1: break
            else: dp[i][0] = dp[i-1][0]

        for j in range(1, n):
            if obstacleGrid[0][j] == 1: break
            else: dp[0][j] = dp[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

solution = Solution()
print(solution.uniquePaths(3,2)) # 3
print(solution.uniquePaths(7,3)) # 28
print(solution.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
])) # 2