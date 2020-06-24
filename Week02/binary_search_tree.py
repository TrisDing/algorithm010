"""
700. Search in a Binary Search Tree <Easy>
https://leetcode.com/problems/search-in-a-binary-search-tree/

701. Insert into a Binary Search Tree <Medium>
https://leetcode.com/problems/insert-into-a-binary-search-tree/

450. Delete Node in a BST <Medium>
https://leetcode.com/problems/delete-node-in-a-bst/
"""
from binary_tree import BinaryTreeNode, create_binary_tree, print_binary_tree

class Solution:
    def searchBST1(self, root: BinaryTreeNode, val: int) -> BinaryTreeNode:
        """
        Solution #1: Recursively
        """
        if root is None:
            return root
        if val < root.val:
            return self.searchBST1(root.left, val)
        if val > root.val:
            return self.searchBST1(root.right, val)
        # val == root.val
        return root

    def searchBST2(self, root: BinaryTreeNode, val: int) -> BinaryTreeNode:
        """
        Solution #2: Iteratively
        """
        curr = root
        while curr:
            if val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right
            else: # val == root.val
                break
        return curr

    def insertIntoBST1(self, root: BinaryTreeNode, val: int) -> BinaryTreeNode:
        if root is None:
            return BinaryTreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST1(root.left, val)
        else: # val > root.val
            root.right = self.insertIntoBST1(root.right, val)
        return root

    def insertIntoBST2(self, root: BinaryTreeNode, val: int) -> BinaryTreeNode:
        if root is None:
            return BinaryTreeNode(val)
        parent, curr = None, root
        while curr:
            parent = curr
            if val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right
            else: # val == root.val
                break
        if val < parent.val:
            parent.left = BinaryTreeNode(val)
        elif val > parent.val:
            parent.right = BinaryTreeNode(val)
        return root

    def deleteNode(self, root: BinaryTreeNode, key: int) -> BinaryTreeNode:
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                # has only right child
                child = root.right
                root = None
                return child
            elif root.right is None:
                # has only left child
                child = root.left
                root = None
                return child
            # has two children
            child = self.minChild(root.right)
            root.val = child.val
            root.right = self.deleteNode(root.right , child.val)
        return root

    def minChild(self, node: BinaryTreeNode) -> BinaryTreeNode:
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

t = create_binary_tree([5,3,7,2,4,6])
print_binary_tree(t)

solution = Solution()
print('Search BST Recursively: ')
ans = solution.searchBST1(t, 3)
print_binary_tree(ans)
print('Search BST Iteratively: ')
ans = solution.searchBST2(t, 7)
print_binary_tree(ans)
print('Insert into BST Recursively: ')
ans = solution.insertIntoBST1(t, 1)
print_binary_tree(ans)
print('Insert into BST Iteratively: ')
ans = solution.insertIntoBST2(t, 8)
print_binary_tree(ans)
print('Delete Node (leaf): ')
ans = solution.deleteNode(t, 1)
print_binary_tree(ans)
print('Delete Node (leaf): ')
ans = solution.deleteNode(t, 4)
print_binary_tree(ans)
print('Delete Node (one child): ')
ans = solution.deleteNode(t, 3)
print_binary_tree(ans)
print('Delete Node (two children): ')
ans = solution.deleteNode(t, 5)
print_binary_tree(ans)
