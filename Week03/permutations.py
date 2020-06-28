"""
46. Permutations <Medium>
https://leetcode.com/problems/permutations/

47. Permutations II <Medium>
https://leetcode.com/problems/permutations-ii/
"""
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(path = []):
            if len(path) == n:
                res.append(path[:])
                return

            for i in range(n):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(path)
                path.pop()

        backtrack()
        return res

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [False] * n

        def backtrack(path = []):
            if len(path) == n:
                res.append(path[:])
                return

            for i in range(n):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    path.append(nums[i])
                    used[i] = True
                    backtrack(path)
                    path.pop()
                    used[i] = False

        backtrack()
        return res

solution = Solution()
print(solution.permute([1,2,3]))
print(solution.permuteUnique([1,1,2]))