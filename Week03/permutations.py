"""
46. Permutations <Medium>
https://leetcode.com/problems/permutations/

47. Permutations II <Medium>
https://leetcode.com/problems/permutations-ii/
"""
from typing import List
from collections import Counter

class Solution:
    def permute1(self, nums: List[int]) -> List[List[int]]:
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

    def permute2(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        # [0, first - 1] = filled numbers
        # [first, n - 1] = numbers to be filled
        # swap nums[first] and nums[i] before backtrack to maintain the dynamic array
        def backtrack(first = 0):
            if first == n:
                res.append(nums[:])
                return

            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack()
        return res

    def permuteUnique1(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [False] * n
        nums.sort()

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

    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(path = [], unused = Counter(nums)):
            if len(path) == n:
                res.append(path[:])
                return

            for x in unused:
                if unused[x] > 0:
                    path.append(x)
                    unused[x] -= 1
                    backtrack(path)
                    path.pop()
                    unused[x] += 1

        backtrack()
        return res

solution = Solution()
print(solution.permute1([1,2,3]))
print(solution.permute2([1,2,3]))
print(solution.permuteUnique1([1,1,2]))
print(solution.permuteUnique2([3,3,0,3]))