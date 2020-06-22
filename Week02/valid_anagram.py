"""
242. Valid Anagram <Easy>
https://leetcode.com/problems/valid-anagram/
"""
from typing import List

class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        """
        Solution #1: Sort
        Time: O(N*logN): sort
        Space: O(1)
        """
        return sorted(s) == sorted(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        """
        Solution #2: Dictionary
        Time: O(1)
        Space: O(K): K is the common character in s and t
        """
        if len(s) != len(t): return False
        d = {}
        for c in s:
            d[ord(c)] = d.get(ord(c), 0) + 1
        for c in t:
            d[ord(c)] = d.get(ord(c), 0) - 1
        return not [x for x in d if d[x] != 0]

solution = Solution()
print(solution.isAnagram1("anagram", "nagaram")) # True
print(solution.isAnagram1("anagram", "nagara"))  # False
print(solution.isAnagram2("anagram", "nagaram")) # True
print(solution.isAnagram2("anagram", "nagara"))  # False
