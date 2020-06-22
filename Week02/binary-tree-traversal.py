"""
144. Binary Tree Preorder Traversal <Medium>
https://leetcode.com/problems/binary-tree-preorder-traversal/

94. Binary Tree Inorder Traversal <Medium>
https://leetcode.com/problems/binary-tree-inorder-traversal/

145. Binary Tree Postorder Traversal <Hard>
https://leetcode.com/problems/binary-tree-postorder-traversal/
"""
from typing import List
from tree import BinaryTreeNode, create_binary_tree, print_binary_tree

class Solution:
    def preorderTraversal1(self, root: BinaryTreeNode) -> List[int]:
        """
        Solution #1: Recursively
        """
        def traverse(root):
            if not root: return
            res.append(root.val)
            traverse(root.left)
            traverse(root.right)

        res = []
        traverse(root)
        return res

    def preorderTraversal2(self, root: BinaryTreeNode) -> List[int]:
        """
        Solution #2: Iteratively
        """
        WHITE, GREY = 0, 1
        res = []
        stack = [(WHITE, root),]
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
                stack.append((GREY, node))
            else:
                res.append(node.val)
        return res

    def inorderTraversal1(self, root: BinaryTreeNode) -> List[int]:
        """
        Solution #1: Recursively
        """
        def traverse(root):
            if not root: return
            traverse(root.left)
            res.append(root.val)
            traverse(root.right)

        res = []
        traverse(root)
        return res

    def inorderTraversal2(self, root: BinaryTreeNode) -> List[int]:
        """
        Solution #2: Iteratively
        """
        WHITE, GREY = 0, 1
        res = []
        stack = [(WHITE, root),]
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GREY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

    def postorderTraversal1(self, root: BinaryTreeNode) -> List[int]:
        """
        Solution #1: Recursively
        """
        def traverse(root):
            if not root: return
            traverse(root.left)
            traverse(root.right)
            res.append(root.val)

        res = []
        traverse(root)
        return res

    def postorderTraversal2(self, root: BinaryTreeNode) -> List[int]:
        """
        Solution #1: Iteratively
        """
        WHITE, GREY = 0, 1
        res = []
        stack = [(WHITE, root),]
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color == WHITE:
                stack.append((GREY, node))
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

t = create_binary_tree([0,1,2,3,4,5,6,7,8,9])
print_binary_tree(t)

solution = Solution()
ans = solution.preorderTraversal1(t)
print('Binary Tree Preorder  Traversal Recursively: ', ans)
ans = solution.preorderTraversal2(t)
print('Binary Tree Preorder  Traversal Iteratively: ', ans)
ans = solution.inorderTraversal1(t)
print('Binary Tree Inorder   Traversal Recursively: ', ans)
ans = solution.inorderTraversal2(t)
print('Binary Tree Inorder   Traversal Iteratively: ', ans)
ans = solution.postorderTraversal1(t)
print('Binary Tree Postorder Traversal Recursively: ', ans)
ans = solution.postorderTraversal2(t)
print('Binary Tree Postorder Traversal Iteratively: ', ans)