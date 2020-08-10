"""
8. String to Integer (atoi) <Medium>
https://leetcode.com/problems/string-to-integer-atoi/
"""
import string

class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        n = len(str)
        i = 0
        while i < n and str[i] == ' ':
            i += 1
        if i >= n: return 0

        sign = 1
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            sign = -1
            i += 1
        if i >= n: return 0

        start = i
        while i < n and str[i] != ' ':
            if str[i] not in string.digits:
                break
            i += 1

        k = 0
        res = 0
        for j in range(i - 1, start - 1, -1):
            res += (ord(str[j]) - ord('0')) * (10**k)
            k += 1

        res = res * sign
        if INT_MIN <= res <= INT_MAX:
            return res
        return INT_MAX if res > 0 else INT_MIN

solution = Solution()
print(solution.myAtoi("42"))
print(solution.myAtoi("    -42"))
print(solution.myAtoi("4193 with words"))
print(solution.myAtoi("words and 987"))
print(solution.myAtoi("-91283472332"))
print(solution.myAtoi(""))
print(solution.myAtoi("  "))
print(solution.myAtoi("+"))
print(solution.myAtoi("   -0012a99"))
print(solution.myAtoi("   3.1415926"))