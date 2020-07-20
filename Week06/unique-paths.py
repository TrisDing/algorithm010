"""
62. Unique Paths <Medium>
https://leetcode.com/problems/unique-paths/

63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/

980. Unique Paths III
https://leetcode.com/problems/unique-paths-iii/
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        f(0, *) = 1
        f(*, 0) = 1
        f(i, j) = f(i, j-1) + f(i-1, j)
        """
        dp = [[1]*n] + [[1] + [0]*(n-1) for _ in range(m-1)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

solution = Solution()
print(solution.uniquePaths(7, 2)) # 28