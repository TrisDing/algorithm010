"""
121. Best Time to Buy and Sell Stock <Easy>
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

122. Best Time to Buy and Sell Stock II <Easy>
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

309. Best Time to Buy and Sell Stock with Cooldown <Medium>
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

714. Best Time to Buy and Sell Stock with Transaction Fee <Medium>
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

123. Best Time to Buy and Sell Stock III <Hard>
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

188. Best Time to Buy and Sell Stock IV <Hard>
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
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
        if n <= 1: return 0

        dp = [[None, None] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])

        return dp[-1][0]

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
        if n <= 1: return 0

        dp = [[None, None] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        return dp[-1][0]

    def maxProfit3(self, prices: List[int]) -> int:
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
        if n <= 1: return 0

        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])

        return dp[n-1][0]

    def maxProfit4(self, prices: List[int], fee: int) -> int:
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
        if n <= 1: return 0

        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0] - fee

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)

        return dp[n-1][0]

    def maxProfit5(self, prices: List[int]) -> int:
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
        if n <= 1: return 0

        dp = [[[None, None] for _ in range(3)] for _ in range(n)] # (n, k+1, 2)
        for i in range(n):
            dp[i][0][0] = 0
            dp[i][0][1] = -math.inf
        for j in range(1, 3):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]

        for i in range(1, n):
            for j in range(1, 3):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

        return dp[-1][-1][0]

    def maxProfit6(self, k: int, prices: List[int]) -> int:
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
        if n <= 1: return 0

        if k > n // 2: # back to unlimited situation (maxProfit3)
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        dp = [[[None, None] for _ in range(k+1)] for _ in range(n)] # (n, k+1, 2)
        for i in range(n):
            dp[i][0][0] = 0
            dp[i][0][1] = -math.inf
        for j in range(1, k+1):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]

        for i in range(1, n):
            for j in range(1, k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

        return dp[-1][-1][0]


solution = Solution()
print("Maximum 1 Transaction:", solution.maxProfit1([7,1,5,3,6,4])) # 5
print("Unlimited Transactions:", solution.maxProfit2([7,1,5,3,6,4])) # 7
print("Unlimited Transactions with Cooldown:", solution.maxProfit3([1,2,3,0,2])) # 3
print("Unlimited Transactions with Fee:", solution.maxProfit4([1,3,2,8,4,9], 2)) # 8
print("Maximum 2 Transactions:", solution.maxProfit5([3,3,5,0,0,3,1,4])) # 6
print("Maximum k Transactions:", solution.maxProfit6(2, [3,2,6,5,0,3])) # 7