"""
231. Power of Two <Easy>
https://leetcode.com/problems/power-of-two/
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (-n) == n

solution = Solution()
print(solution.isPowerOfTwo(1)) # True
print(solution.isPowerOfTwo(16)) # True
print(solution.isPowerOfTwo(218)) # False