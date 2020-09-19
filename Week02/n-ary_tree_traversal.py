"""
589. N-ary Tree Preorder Traversal <Easy>
https://leetcode.com/problems/n-ary-tree-preorder-traversal/

590. N-ary Tree Postorder Traversal <Easy>
https://leetcode.com/problems/n-ary-tree-postorder-traversal/

429. N-ary Tree Level Order Traversal <Medium>
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
"""
from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder1(self, root: TreeNode) -> List[int]:
        """
        Solution #1: Recursively
        """
        def traverse(root):
            if not root: return
            res.append(root.val)
            if root.children is not None:
                for child in root.children:
                    traverse(child)

        res = []
        traverse(root)
        return res

    def preorder2(self, root: TreeNode) -> List[int]:
        """
        Solution #2: Iteratively
        """
        if not root: return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node: continue
            res.append(node.val)
            if node.children:
                for child in node.children[::-1]:
                    stack.append(child)
        return res

    def postorder1(self, root: TreeNode) -> List[int]:
        """
        Solution #1: Recursively
        """
        def traverse(root):
            if not root:
                return
            if root.children is not None:
                for child in root.children:
                    traverse(child)
            res.append(root.val)

        res = []
        traverse(root)
        return res

    def postorder2(self, root: TreeNode) -> List[int]:
        """
        Solution #2: Iteratively
        """
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            if root is not None:
                res.append(root.val)
            if root.children is not None:
                # from left to right append child
                for child in root.children:
                    stack.append(child)
        return res[::-1] # the result is reversed

    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        """
        Solution #1: Recursively
        """
        def traverse(root, level):
            if not root:
                return
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            if root.children is not None:
                for child in root.children:
                    traverse(child, level + 1)

        res = []
        traverse(root, 0)
        return res

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            n = len(queue)
            level = []
            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)
                if node.children is not None:
                    for child in node.children:
                        queue.append(child)
            res.append(level)
        return res

t = TreeNode(1, [TreeNode(3, [TreeNode(5), TreeNode(6)]), TreeNode(2), TreeNode(4)])
"""
      ___1___
     /   |   \
  __3__  2    4
 /     \
5       6
"""

solution = Solution()
ans = solution.preorder1(t)
print('N-ary Tree Preorder Traversal Recursively: ', ans)
ans = solution.preorder2(t)
print('N-ary Tree Preorder Traversal Iteratively: ', ans)
ans = solution.postorder1(t)
print('N-ary Tree Postorder Traversal Recursively: ', ans)
ans = solution.postorder2(t)
print('N-ary Tree Postorder Traversal Iteratively: ', ans)
ans = solution.levelOrder1(t)
print('N-ary Tree Level Order Traversal Recursively: ', ans)
ans = solution.levelOrder2(t)
print('N-ary Tree Level Order Traversal Iteratively: ', ans)