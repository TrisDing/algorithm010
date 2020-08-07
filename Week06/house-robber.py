"""
198. House Robber <Easy>
https://leetcode.com/problems/house-robber/

213. House Robber II <Medium>
https://leetcode.com/problems/house-robber-ii/

337. House Robber III <Medium>
https://leetcode.com/problems/house-robber-iii/
"""
from typing import List

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

def createTree(iterable = ()):
    def insert(node, i):
        if i < len(iterable) and iterable[i] is not None:
            node = TreeNode(iterable[i])
            node.left = insert(node.left, 2 * i + 1)
            node.right = insert(node.right, 2 * i + 2)
        return node
    return insert(None, 0)

class Solution:
    def rob1(self, nums: List[int]) -> int:
        """
        choices = {
            0: not rob
            1: rob
        }

        status = {
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]
        }

        base case = {
            dp[0][0] = 0
            dp[0][1] = nums[0]
        }

        answer = max(dp[-1][0], dp[-1][1])
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = nums[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]

        return max(dp[-1][0], dp[-1][1])

    def rob1(self, nums: List[int]) -> int:
        """
        dp[i] = {
            dp[0] = nums[0], n = 0
            dp[1] = max(nums[0], nums[1]), n = 1
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]), n >= 2
        }
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]

    def rob1(self, nums: List[int]) -> int:
        """
        Space Optimization
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        f = 0  # dp[i]
        f1 = 0 # dp[i-1]
        f2 = 0 # dp[i-2]

        for i in range(n):
            f = max(f1, f2 + nums[i])
            f2 = f1
            f1 = f

        return f

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

tree = createTree([3,2,3,None,3,None,1])
print(solution.rob3(tree)) # 7

tree = createTree([3,4,5,1,3,None,1])
print(solution.rob3(tree)) # 9