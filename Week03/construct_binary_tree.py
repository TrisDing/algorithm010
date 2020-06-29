"""
105. Construct Binary Tree from Preorder and Inorder Traversal <Medium>
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""
from typing import List
from binary_tree import BinaryTreeNode, print_binary_tree

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> BinaryTreeNode:
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None

        def build(preorder_left, preorder_right, inorder_left, inorder_right):
            # base
            if preorder_left > preorder_right:
                return None

            # process
            preorder_root = preorder_left
            inorder_root = index[preorder[preorder_root]]
            root = BinaryTreeNode(preorder[preorder_root])

            # drill down
            size_left_subtree = inorder_root - inorder_left
            root.left = build(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root + 1)
            root.right = build(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)

            # return
            return root

        # preorder = [root, [left subtree], [right subtree]]
        # inorder =  [[left subtree], root, [right subtree]]
        n = len(preorder)
        index = { elem: i for i, elem in enumerate(inorder) }
        return build(0, n-1, 0, n-1)

solution = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
ans = solution.buildTree(preorder, inorder)
print_binary_tree(ans)
