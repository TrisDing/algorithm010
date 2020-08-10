"""
771. Jewels and Stones <Easy>
https://leetcode.com/problems/jewels-and-stones/
"""
from collections import Counter

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if not J or not S: return 0
        return sum([1 for s in S if s in Counter(J)])

solution = Solution()
print(solution.numJewelsInStones("aA", "aAAbbbb"))
print(solution.numJewelsInStones("z", "ZZ"))