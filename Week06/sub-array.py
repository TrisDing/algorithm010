"""
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/

718. Maximum Length of Repeated Subarray
https://leetcode.com/problems/maximum-length-of-repeated-subarray/
"""
from typing import List

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        """
        f(0, *) = 0
        f(*, 0) = 0
        f(i,j) = f(i-1, j-1) + 1, if A[i] == B[j]
        """
        m, n = len(A), len(B)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        res = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res, dp[i][j])

        return res

solution = Solution()
print(solution.findLength([1,2,3,2,1], [3,2,1,4,7])) # 3