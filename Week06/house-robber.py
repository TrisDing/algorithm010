"""
198. House Robber <Easy>
https://leetcode.com/problems/house-robber/

213. House Robber II
https://leetcode.com/problems/house-robber-ii/

337. House Robber III
https://leetcode.com/problems/house-robber-iii/
"""
from typing import List

class Solution:
    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        k = 0   # dp[k]
        k_1 = 0 # dp[k-1]
        k_2 = 0 # dp[k-2]

        for i in range(n):
            k = max(k_1, k_2 + nums[i])
            k_2 = k_1
            k_1 = k

        return k

    def rob2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        return max(self.rob1(nums[1:]), self.rob1(nums[:-1]))

    def rob3(self, root: TreeNode, memo = {}) -> int:
        def dp(root):
            if not root:
                return 0, 0

            rob_left, not_rob_left = dp(root.left)
            rob_right, not_rob_right = dp(root.right)

            rob = root.val + not_rob_left + not_rob_right
            not_rob = max(rob_left, not_rob_left) + max(rob_right, not_rob_right)

            return rob, not_rob

        rob, not_rob = dp(root)
        return max(rob, not_rob)


solution = Solution()
print(solution.rob1([1,2,3,1])) # 4
print(solution.rob2([2,3,2])) # 3
# todo: rob3 test case