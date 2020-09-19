"""
144. Binary Tree Preorder Traversal <Medium>
https://leetcode.com/problems/binary-tree-preorder-traversal/

94. Binary Tree Inorder Traversal <Medium>
https://leetcode.com/problems/binary-tree-inorder-traversal/

145. Binary Tree Postorder Traversal <Hard>
https://leetcode.com/problems/binary-tree-postorder-traversal/

102. Binary Tree Level Order Traversal <Medium>
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""
from typing import List
from binary_tree import BinaryTreeNode, create_binary_tree, print_binary_tree
from collections import deque

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
        if not root: return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is not None:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res

    def preorderTraversal3(self, root: BinaryTreeNode) -> List[int]:
        """
        Solution #3: White/Grey Tagging
        """
        WHITE, GREY = 0, 1
        res = []
        stack = [(WHITE, root)]
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

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        Solution #2: Iteratively
        """
        if not root: return []
        res = []
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res

    def inorderTraversal3(self, root: BinaryTreeNode) -> List[int]:
        """
        Solution #3: White/Grey Tagging
        """
        WHITE, GREY = 0, 1
        res = []
        stack = [(WHITE, root)]
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

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        Solution #2: Iteratively
        """
        if not root: return root
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is not None:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]

    def postorderTraversal3(self, root: BinaryTreeNode) -> List[int]:
        """
        Solution #3: White/Grey Tagging
        """
        WHITE, GREY = 0, 1
        res = []
        stack = [(WHITE, root)]
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

    def levelOrder1(self, root: BinaryTreeNode) -> List[List[int]]:
        """
        Solution #1: Recursively
        """
        def traverse(root, level):
            if not root:
                return
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            if root.left:
                traverse(root.left, level+1)
            if root.right:
                traverse(root.right, level+1)

        res = []
        traverse(root, 0)
        return res

    def levelOrder2(self, root: BinaryTreeNode) -> List[List[int]]:
        """
        Solution #2: Iteratively
        """
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            n = len(queue)
            level = []
            for _ in range(n):
                root = queue.popleft()
                level.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(level)
        return res

t = create_binary_tree([0,1,2,3,4,5,6,7,8,9])
print_binary_tree(t)

solution = Solution()
ans = solution.preorderTraversal1(t)
print('Binary Tree Preorder Traversal Recursively: ', ans)
ans = solution.preorderTraversal2(t)
print('Binary Tree Preorder Traversal Iteratively: ', ans)
ans = solution.inorderTraversal1(t)
print('Binary Tree Inorder Traversal Recursively: ', ans)
ans = solution.inorderTraversal2(t)
print('Binary Tree Inorder Traversal Iteratively: ', ans)
ans = solution.postorderTraversal1(t)
print('Binary Tree Postorder Traversal Recursively: ', ans)
ans = solution.postorderTraversal2(t)
print('Binary Tree Postorder Traversal Iteratively: ', ans)
ans = solution.levelOrder1(t)
print('Binary Tree Level Order Traversal Recursively: ', ans)
ans = solution.levelOrder2(t)
print('Binary Tree Level Order Traversal Iteratively: ', ans)