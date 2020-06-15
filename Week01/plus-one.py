"""
66. Plus One <Easy>
https://leetcode.com/problems/plus-one/
"""
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Time: O(n)
        Space: O(1)
        """
        n = len(digits) - 1
        while n >= 0:
            if digits[n] == 9:
                digits[n] = 0
                n -= 1
            else:
                digits[n] += 1
                break

        return [1] + digits[:] if digits[0] == 0 else digits

solution = Solution()
ans = solution.plusOne([9,9,9])

print(ans) # [1,0,0,0]