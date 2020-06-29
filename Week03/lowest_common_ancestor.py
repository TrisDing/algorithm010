"""
236. Lowest Common Ancestor of a Binary Tree <Medium>
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""
from binary_tree import BinaryTreeNode, create_binary_tree, print_binary_tree, cherry_pick

class Solution:
    def lowestCommonAncestor1(self, root: BinaryTreeNode, p: BinaryTreeNode, q: BinaryTreeNode) -> BinaryTreeNode:
        if root is None:
            return None

        def helper(root: BinaryTreeNode, p: BinaryTreeNode, q: BinaryTreeNode) -> BinaryTreeNode:
            if root is None:
                return None

            p_in_left = nodesIndex[p.val] <= nodesIndex[root.val]
            p_in_right = nodesIndex[p.val] >= nodesIndex[root.val]

            q_in_left = nodesIndex[q.val] <= nodesIndex[root.val]
            q_in_right = nodesIndex[q.val] >= nodesIndex[root.val]

            if (p_in_left and q_in_right) or (p_in_right and q_in_left):
                # found LCA
                return root

            if p_in_left and q_in_left:
                # LCA must in the left subtree, keep finding
                return helper(root.left, p, q)

            if p_in_right and q_in_right:
                # LCA must in the right subtree, keep finding
                return helper(root.right, p, q)

            return None

        def inorder(root: BinaryTreeNode):
            if root is None:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        nodesInorder = inorder(root)
        nodesIndex = {} # based on assumption that all nodes values are unique
        for i, elem in enumerate(nodesInorder):
            nodesIndex[elem] = i
        return helper(root, p, q)


    def lowestCommonAncestor2(self, root: BinaryTreeNode, p: BinaryTreeNode, q: BinaryTreeNode) -> BinaryTreeNode:
        # terminator
        if root is None:
            return None
        if root == p or root == q:
            return root

        # drill down
        lca_left = self.lowestCommonAncestor2(root.left, p, q)
        lca_right = self.lowestCommonAncestor2(root.right, p, q)

        # process
        if lca_left is None:
            return lca_right
        if lca_right is None:
            return lca_left
        if lca_left and lca_right:
            return root

        # return
        return None

solution = Solution()
tree = create_binary_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print_binary_tree(tree)

p = cherry_pick(tree, 5)
q = cherry_pick(tree, 1)
ans = solution.lowestCommonAncestor1(tree, p, q)
print('lowestCommonAncestor1 of', '(', p.val, ') and (', q.val, ') is (', ans.val, ')')
ans = solution.lowestCommonAncestor2(tree, p, q)
print('lowestCommonAncestor2 of', '(', p.val, ') and (', q.val, ') is (', ans.val, ')')

p = cherry_pick(tree, 5)
q = cherry_pick(tree, 4)
ans = solution.lowestCommonAncestor1(tree, p, q)
print('lowestCommonAncestor1 of', '(', p.val, ') and (', q.val, ') is (', ans.val, ')')
ans = solution.lowestCommonAncestor2(tree, p, q)
print('lowestCommonAncestor2 of', '(', p.val, ') and (', q.val, ') is (', ans.val, ')')
