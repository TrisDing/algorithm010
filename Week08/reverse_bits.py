"""
190. Reverse Bits <Easy>
https://leetcode.com/problems/reverse-bits/
"""
class Solution:
    def reverseBits1(self, x: int) -> int:
        result = 0
        power = 31
        while x:
            result += (x & 1) << power
            x >>= 1
            power -= 1
        return result

    def reverseBits2(self, n: int) -> int:
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n

solution = Solution()
print(bin(solution.reverseBits1(0b00000010100101000001111010011111)))
print(bin(solution.reverseBits1(0b11111111111111111111111111111101)))
print(bin(solution.reverseBits2(0b00000010100101000001111010011111)))
print(bin(solution.reverseBits2(0b11111111111111111111111111111101)))