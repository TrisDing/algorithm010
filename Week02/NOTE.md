Learning Notes Week 02
======================

Binary Trees
------------

> A binary tree is either empty, or a root node r together with a left binary tree and a right binary tree.

```
                         Height  Depth  Level
        __A__      ---->   4       0      1
       /     \
    __B       C    ---->   3       1      2
   /   \     / \
  D     E   F   G  ---->   2       2      3
 / \
H   I              ---->   1       3      4
```
- Node `A` is Root
- Node `A` has 2 children: Node `B` and Node `C`
- Node `B` is Node `A`'s left child
- Node `C` is Node `A`'s right child
- Node `A` is Node `B` and Node `C`'s parent
- Node `H` and Node `I` are a Leaf Nodes
- Node `A` is Node `H`'s ancestor
- Node `I` is Node `A`'s decedent

Binary tree
> A tree has a root node and every node has at most 2 children

Full Binary Tree
> A tree in which every node has either 0 or 2 children

Perfect Binary Tree
> A full binary tree in which all leaves are at the same depth, and in which every parent has 2 children

Complete Binary Tree
> A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.

```
      __A__
     /     \
    B       C
   / \     / \
  D   E   F   G
 /
H

[_,A,B,C,D,E,F,G,H]
```

A complete binary tree has `2^k` nodes at every depth `k < n` and between `2^n` and `2^n+1 - 1` nodes altogether. It can be efficiently implemented as an array, where a node at index `i` has children at indexes `2i` and `2i+1` and a parent at index `i/2`, with 1-based indexing.

Below are **NOT** Complete Binary Trees
```
      __A__              __A__                   ______A______
     /     \            /     \                 /             \
    B       C          B       C             __B__           __C__
   / \                / \     / \           /     \         /     \
  D   E              D   E   F   G         D       E       F       G
 / \   \              \       \           / \     / \     / \     / \
F   G   H              H       I         H   I   J   K   L   M   N   O
```

Binary Tree Traversal
---------------------

BinaryTree Node
```py
class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```


DFS Pre-order Traversal: `root -> left -> right`
```py
def preorder(self, root):
    if root:
        self.visit(root.val)
        self.preorder(left)
        self.preorder(right)
```

DFS In-order Traversal: `left -> root -> right`
```py
def inorder(self, root):
    if root:
        self.inorder(left)
        self.visit(root.val)
        self.inorder(right)
```

DFS Post-order Traversal:  `left -> right -> root`
```py
def postorder(self, root):
    if root:
        self.postorder(left)
        self.postorder(right)
        self.visit(root.val)
```

BFS Level Order Traversal: `top -> bottom, left -> right`
```py
def levelorder(root):
    queue = collections.deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        visit(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```
