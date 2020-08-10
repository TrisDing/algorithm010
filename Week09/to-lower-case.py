"""
709. To Lower Case <Easy>
https://leetcode-cn.com/problems/to-lower-case/
"""
import string

class Solution:
    def toLowerCase(self, str: str) -> str:
        if not str: return str
        res = [''] * len(str)
        for i, c in enumerate(str):
            if c in string.ascii_uppercase:
                res[i] = chr(ord(c) + 32)
            else:
                res[i] = c
        return ''.join(res)

solution = Solution()
print(solution.toLowerCase("Hello"))
print(solution.toLowerCase("here"))
print(solution.toLowerCase("LOVELY"))