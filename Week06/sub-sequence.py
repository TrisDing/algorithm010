"""
300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/)

516. Longest Palindromic Subsequence
https://leetcode.com/problems/longest-palindromic-subsequence/

1143. Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/

1035. Uncrossed Lines
https://leetcode.com/problems/uncrossed-lines/
"""
class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        """
        f(0, *) = 0
        f(*, 0) = 0
        f(i, j) = {
            f(i-1, j-1) + 1           , when s[i-1] == t[j-1]
            max(f(i-1, j), f(i, j-1)) , when s[i-1] != t[j-1]
        }
        """
        if not s or not t:
            return 0

        m, n = len(s), len(t)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]

solution = Solution()
print(solution.longestCommonSubsequence('abcde', 'ace')) # 3
print(solution.longestCommonSubsequence('abc', 'abc')) # 3
print(solution.longestCommonSubsequence('abc', 'def')) # 0
