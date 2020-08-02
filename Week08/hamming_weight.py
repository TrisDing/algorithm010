"""
191. Number of 1 Bits <Easy>
https://leetcode.com/problems/number-of-1-bits/
"""
class Solution:
    def hammingWeight1(self, n: int) -> int:
        bits = 0
        while n != 0:
            bits += 1
            n &= (n - 1) # drop lowest set bit
        return bits

    def hammingWeight2(self, n: int) -> int:
        bits = 0
        mask = 1
        for i in range(32):
            if (n & mask) != 0:
                bits += 1
            mask <<= 1
        return bits

solution = Solution()
print(solution.hammingWeight1(0b00000000000000000000000000001011)) # 3
print(solution.hammingWeight1(0b00000000000000000000000010000000)) # 1
print(solution.hammingWeight1(0b11111111111111111111111111111101)) # 31
print(solution.hammingWeight2(0b00000000000000000000000000001011)) # 3
print(solution.hammingWeight2(0b00000000000000000000000010000000)) # 1
print(solution.hammingWeight2(0b11111111111111111111111111111101)) # 31