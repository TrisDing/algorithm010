"""
22. Generate Parentheses <Medium>
https://leetcode.com/problems/generate-parentheses/
"""
from typing import List

class Solution:
    def generateParenthesis1(self, n: int) -> List[str]:
        res = []

        def generate(left = 0, right = 0, s = ''):
            if left == n and right == n:
                res.append(s)
                return

            # process and drill down
            if left < n:
                generate(left + 1, right, s + '(')
            if left > right:
                generate(left, right + 1, s + ')')

        generate()
        return res

    def generateParenthesis2(self, n: int) -> List[str]:
        res = []

        def backtrack(left = n, right = n, path = ''):
            if left < 0 or right < 0: return
            if right < left: return
            if left == 0 and right == 0:
                res.append(path)
                return

            path = path + '('
            backtrack(left - 1, right, path)
            path = path[:-1]

            path = path + ')'
            backtrack(left, right - 1, path)
            path = path[:-1]

        backtrack()
        return res

solution = Solution()
print(solution.generateParenthesis1(3))
print(solution.generateParenthesis2(3))