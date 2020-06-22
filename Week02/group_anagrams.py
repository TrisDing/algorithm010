"""
49. Group Anagrams <Medium>
https://leetcode.com/problems/valid-anagram/
"""
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        """
        Solution #1: Sort
        Time: O(N*K*logK): N = len(strs), K = len(longest string in strs)
        Space: O(N*K): the dictionary
        """
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        """
        Solution #2: Count
        Time: O(N*K): N = len(strs), K = len(longest string in strs)
        Space: O(N*K): the dictionary
        """
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

solution = Solution()
print(solution.groupAnagrams1(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
