Learning Notes Week 06
======================

Dynamic Programming
-------------------
> **Optimal Substructure**: the solution to a given optimization problem can be obtained by the combination of optimal solutions to its sub-problems. Such optimal substructures are usually described by means of "_recursion_".

> **Overlapping Subproblems**: the space of sub-problems must be small, that is, any recursive algorithm solving the problem should solve the same sub-problems over and over, rather than generating new sub-problems. If a problem can be solved by combining optimal solutions to non-overlapping sub-problems, the strategy is called _"divide and conquer"_ instead.

This can be achieved in either of two ways:
1. **Top-down**: Recursion + Memo
2. **Bottom-up**: Iteration + DP Table (states)

Fibonacci sequence
------------------

Top-down
```
                            _________________f(5)________________
                           /                                     \
                  _______f(4)______                       _______f(3)_
                 /                 \                     /            \
        _______f(3)_             __f(2)_             __f(2)_          f(1)
       /            \           /       \           /       \
   __f(2)_          f(1)      f(1)      f(1)      f(1)      f(1)
  /       \
f(1)      f(1)
```

Recursion
```py
def fib(N):
    if N < 2: return N
    return fib(N-1) + fib(N-2)
```

Space Optimization (Memo)
```py
memo = {}
def fib(N):
    if N < 2: return N
    if N not in memo:
        memo[N] = fib(N-1) + fib(N-2)
    return memo[N]
```

Bottom-up
```
f(0) f(1) f(2) f(3) f(4) f(5)
  1    2    3    5    8   13
--------------------------->
```

Dynamic Programming
```py
def fib(N):
    """
    dp(N) = {
        N, N < 2
        dp(N-1) + dp(N-2), N >= 2
    }
    """
    if N < 2: return N
    dp = [0] * (N+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]
```

Space Optimization (Reduce States)
```py
def fib(self):
    if N < 2: return N
    f, f1, f2 = 0, 0, 1
    for i in range(N):
        f = f1 + f2
        f2 = f1
        f1 = f
    return f
```

DP Framework
------------
```py
# initialize base case
dp[0][0][...] = base

# status transfer
for status_1 in all_values_in_status_1：
    for status_2 in all_values_in_status_2:
        for ...
            dp[status_1][status_2][...] = choose(choice_1，choice_2...)
```

Leetcode Problems
-----------------

Basics
- [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)
- [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- [120. Triangle](https://leetcode.com/problems/triangle/)
- [322. Coin Change](https://leetcode.com/problems/coin-change/)
- [518. Coin Change 2](https://leetcode.com/problems/coin-change-2/)

House Robber
- [198. House Robber](https://leetcode.com/problems/house-robber/)
- [213. House Robber II](https://leetcode.com/problems/house-robber-ii/)
- [337. House Robber III](https://leetcode.com/problems/house-robber-iii/)

Unique Paths
- [62. Unique Paths](https://leetcode.com/problems/unique-paths/)
- [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)
- [980. Unique Paths III](https://leetcode.com/problems/unique-paths-iii/)

Sub Array / Sub Subsequence
- [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
- [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/description/)
- [718. Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)
- [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
- [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
- [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)
- [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
- [1035. Uncrossed Lines](https://leetcode.com/problems/uncrossed-lines/)

Buy and Sell Stocks
- [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
- [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)
- [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)
- [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
- [714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)
