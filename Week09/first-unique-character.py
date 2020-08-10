"""
387. First Unique Character in a String <Easy>
https://leetcode.com/problems/first-unique-character-in-a-string/
"""
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: return -1
        cnt = Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1

solution = Solution()
print(solution.firstUniqChar("leetcode"))
print(solution.firstUniqChar("loveleetcode"))