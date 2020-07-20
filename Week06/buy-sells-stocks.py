"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

123. Best Time to Buy and Sell Stock III
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

188. Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

309. Best Time to Buy and Sell Stock with Cooldown
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

714. Best Time to Buy and Sell Stock with Transaction Fee
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
"""
from typing import List
import math

class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        """
        dp[i][0] = max (
            dp[i-1][0]
            dp[i-1][1] + prices[i]
        )
        dp[i][1] = max (
            dp[i-1][1]
            0 - prices[i]
        )
        """
        n = len(prices)
        if n == 0:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])

        return dp[n-1][0]

    def maxProfit2(self, prices: List[int]) -> int:
        """
        dp[i][0] = max(
            dp[i-1][0]
            dp[i-1][1] + prices[i]
        )
        dp[i][1] = max(
            dp[i-1][1]
            dp[i-1][0] - prices[i]
        )
        """
        n = len(prices)
        if n == 0:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        return dp[n-1][0]

    def maxProfit3(self, prices: List[int]) -> int:
        """
        dp[i][k][0] = max(
            dp[i-1][k][0]
            dp[i-1][k][1] + prices[i]
        )
        dp[i][k][1] = max(
            dp[i-1][k][1]
            dp[i-1][k-1][0] - prices[i]
        )
        """
        n = len(prices)
        if n == 0:
            return 0

        k = 2
        dp = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(n)]
        dp[0][1][0] = 0
        dp[0][1][1] = -prices[0]
        dp[0][2][0] = 0
        dp[0][2][1] = -prices[0]

        for i in range(1, n):
            for j in range(1, k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

        return dp[n-1][k][0]

    def maxProfit4(self, k: int, prices: List[int]) -> int:
        """
        dp[i][k][0] = max(
            dp[i-1][k][0]
            dp[i-1][k][1] + prices[i]
        )
        dp[i][k][1] = max(
            dp[i-1][k][1]
            dp[i-1][k-1][0] - prices[i]
        )
        """
        n = len(prices)
        if n == 0:
            return 0

        if k > n/2:
            res = 0
            for i, j in zip(prices[1:], prices[:-1]):
                res += max(0, i-j)
            return res

        dp = [[[-math.inf]*2 for _ in range(k+1)] for _ in range(n)]
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]

        for i in range(1, n):
            for j in range(k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                if k > 0:
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

        res = max(dp[n-1][j][0] for j in range(k+1))
        return res

    def maxProfit5(self, prices: List[int]) -> int:
        """
        dp[i][0] = max(
            dp[i-1][0]
            dp[i-1][1] + price[i]
        )
        dp[i][1] = max(
            dp[i-1][1]
            dp[i-2][0] - price[i]
        )
        """
        n = len(prices)
        if n == 0:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])

        return dp[n-1][0]

    def maxProfit6(self, prices: List[int], fee: int) -> int:
        """
        dp[i][0] = max(
            dp[i-1][0]
            dp[i-1][1] + prices[i]
        )
        dp[i][1] = max(
            dp[i-1][1]
            dp[i-1][0] - prices[i] - fee
        )
        """
        n = len(prices)
        if n == 0:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0] - fee

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)

        return dp[n-1][0]

solution = Solution()
print(solution.maxProfit1([7,1,5,3,6,4])) # 5
print(solution.maxProfit2([7,1,5,3,6,4])) # 7
print(solution.maxProfit3([3,3,5,0,0,3,1,4])) #6
# todo: maxProfit4 test case
print(solution.maxProfit5([1,2,3,0,2])) # 3
print(solution.maxProfit6([1,3,2,8,4,9], 2)) # 8
