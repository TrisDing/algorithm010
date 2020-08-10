"""
14. Longest Common Prefix <Easy>
https://leetcode.com/problems/longest-common-prefix/
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        m, n = len(strs[0]), len(strs)
        for i in range(m):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, n)):
                return strs[0][:i]
        return strs[0]

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"])) # "fl"
print(solution.longestCommonPrefix(["dog","racecar","car"])) # ""
print(solution.longestCommonPrefix(["a"])) # "a"
print(solution.longestCommonPrefix(["aa", "a"])) # "a"