"""
589. N-ary Tree Preorder Traversal <Easy>
https://leetcode.com/problems/n-ary-tree-preorder-traversal/

590. N-ary Tree Postorder Traversal <Easy>
https://leetcode.com/problems/n-ary-tree-postorder-traversal/

429. N-ary Tree Level Order Traversal <Medium>
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
"""
from typing import List
from tree import TreeNode, simple_tree

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
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            if root.children is not None:
                # from right to left append child
                for child in root.children[::-1]:
                    stack.append(child)
            if root is not None:
                res.append(root.val)
        return res

    def postorder1(self, root: TreeNode) -> List[int]:
        """
        Solution #1: Recursively
        """
        def traverse(root):
            if not root: return
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

t = simple_tree()

solution = Solution()
ans = solution.preorder1(t)
print('N-ary Tree Preorder  Traversal Recursively: ', ans)
ans = solution.preorder2(t)
print('N-ary Tree Preorder  Traversal Iteratively: ', ans)
ans = solution.postorder1(t)
print('N-ary Tree Postorder Traversal Recursively: ', ans)
ans = solution.postorder2(t)
print('N-ary Tree Postorder Traversal Iteratively: ', ans)