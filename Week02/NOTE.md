Learning Notes Week 02
======================

Hash Table
----------

> A hash table is a data structure used to store vals, optionally, with corresponding values.

- A mapping object maps hashable values to arbitrary objects. Mappings are **mutable** objects. The only standard mapping type in python is `Dictionary`.
- A `dict` vals are almost arbitrary values. Values that are not hashable (like lists, dictionaries or other mutable types) may not be used as vals.
- A `set` is an unordered collection with no duplicate elements. Curly braces or the set() function can be used to create sets. (empty set must use set())

| Operation  | Time Complexity |
| ---------- | :-------------: |
| Access     | N/A             |
| Search     | O(1)            |
| Insertion  | O(1)            |
| Deletion   | O(1)            |

Dictionary Operations
```py
d[val]                 # Return the item of d with val val. Raises a valError if val is not in the map.
d[val] = value         # Set d[val] to value.
del d[val]             # Remove d[val] from d. Raises a valError if val is not in the map.
val in d               # Return True if d has a val val, else False.
val not in d           # Equivalent to not val in d.
d.clear()              # Remove all items from the dictionary.
d.get(val[, default])  # Return the value for val if val is in the dictionary, else default.
d.keys()               # Return a new view of the dictionary’s keys.
d.values()             # Return a new view of the dictionary’s values.
d.items()              # Return a new view of the dictionary’s items ((val, value) pairs).
```

Useful functions
```py
from collections import Counter

cnt = Counter() # A Counter is a dict subclass for counting hashable objects.
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(cnt) # Counter({'blue': 3, 'red': 2, 'green': 1})
```

Leetcode Problems
- [1. Two Sum](https://leetcode.com/problems/two-sum/)
- [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)
- [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

Binary Trees
------------

> A binary tree is either empty, or a root node together with a left binary tree and a right binary tree.

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

- A complete binary tree has `2^k` nodes at every depth `k < n` and between `2^n` and `2^n+1 - 1` nodes altogether.
- It can be efficiently implemented as an array, where a node at index `i` has children at indexes `2i` and `2i+1` and a parent at index `i/2`, with 1-based indexing (`2i+1` and `2i+2` for 0-based indexing)

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

BinaryTree Node
```py
class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

Binary Tree Traversal

DFS Pre-order Traversal: `root -> left -> right`
```py
def preorder(self, root):
    if root:
        visit(root)
        preorder(left)
        preorder(right)
```

DFS In-order Traversal: `left -> root -> right`
```py
def inorder(self, root):
    if root:
        inorder(left)
        visit(root)
        inorder(right)
```

DFS Post-order Traversal:  `left -> right -> root`
```py
def postorder(self, root):
    if root:
        postorder(left)
        postorder(right)
        visit(root)
```

BFS Level Order Traversal: `top -> bottom, left -> right`
```py
def levelorder(root):
    queue = collections.deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        self.visit(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

LeetCode Problems
- [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
- [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [589. N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)
- [590. N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/)
- [429. N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/)

Binary Search Tree (BST)

> A BST is a rooted binary tree whose internal nodes each store a val greater than all the vals in the node's left subtree and less than those in its right subtree.

| Operation  | Time Complexity |
| ---------- | :-------------: |
| Access     | O(log n)       |
| Search     | O(log n)       |
| Insertion  | O(log n)       |
| Deletion   | O(log n)       |

BST Template
```py
def BST(root, target):
    if root.val == target:
        # found it, do something
    if val < root.val:
        BST(root.left, val) # find in left tree
    if val > root.val:
        BST(root.right, val)  # find in right tree
```

Search
```py
def search(root, val):
    if root is None:
        return None
    if val < root.val:
        return search(root.left, val)
    elif val > root.val:
        return search(root.right, val)
    return root
```

Insert
```
     100                        100
    /   \      Insert(40)      /   \
  20    500    --------->     20   500
 /  \                        /  \
10   30                     10   30
                                  \
                                   40
```

```py
def insert(root, val):
    if root is None:
        return BinaryTreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(node.right, val)
    return root
```

Delete
```
1) Node to be deleted is leaf: Simply remove from the tree.

     50                             50
   /    \         Delete(20)      /    \
  30     70       --------->    30     70
 /  \   /  \                      \   /  \
20  40 60  80                     40 60  80

2) Node to be deleted has only one child: Copy the child to the node and delete the child.

     50                             50
   /    \         Delete(30)      /    \
  30     70       --------->    40     70
    \   /  \                          /  \
    40 60  80                        60  80

3) Node to be deleted has two children: Find inorder successor of the node.
   Copy contents of the inorder successor to the node and delete the inorder successor.

     50                             60
   /    \         Delete(50)      /    \
  40     70       --------->    40     70
        /  \                             \
       60  80                            80
```

```py
def deleteNode(self, root: TreeNode, val: int) -> TreeNode:
    if root is None: return root

    if val < root.val:
        root.left = self.deleteNode(root.left, val)
    elif val > root.val:
        root.right = self.deleteNode(root.right, val)
    else:
        # has one child
        if root.left is None: # only right child
            return root.right
        if root.right is None: # only left child
            return root.left

        # has two children
        minNode = self.getMin(root.right)
        root.val = minNode.val
        root.right = self.deleteNode(root.right, minNode.val)

    return root

def getMin(self, node: TreeNode) -> TreeNode:
    # left most child is the smallest
    while node.left is not None:
        node = node.left
    return node
```

LeetCode Problems
- [100. Same Tree](https://leetcode.com/problems/same-tree/)
- [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)
- [701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)
- [450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)
- [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

Heap
----

> A heap is a complete binary tree, and is represent by array. The children of the node at index i are at indices 2i+1 and 2i+2.

Given element in a heap at position `i`:
- parent position: `(i-1) >> 1` or `i // 2`
- left child position: `2*i + 1`
- right child position: `2*i + 2`

| Operation  | Time Complexity |
| ---------- | :-------------: |
| find-min   | O(1)            |
| delete-min | O(logn)         |
| Insert     | O(logn)         |
| K largest  | O(nlogK)        |
| K smallest | O(nlogK)        |

max-heap: the val at each node is at least as great as the vals at it's children.
```
           _____561_____
          /             \
     ___314_           _401_
    /       \         /     \
  _28       156     359     271
 /   \
11    3
```

min-heap: the val at each node is at least as small as the vals at it's children.
```
              _____3____
             /          \
       _____11_         _28_
      /        \       /    \
   _156_       314   561    401
  /     \
359     271
```

**heapq** Operations
```py
heap = []               # creates an empty heap
heap[0]                 # smallest element on the heap without popping it
heapq.heapify(L)        # transforms list into a heap, in-place, in linear time
heapq.heappush(h, e)    # pushes a new element on the heap
heapq.heappop(h)        # pops the smallest item from the heap
heapq.heappushpop(h, a) # pushes a on the heap and then pops and returns the smallest element
heapq.heapreplace(h, e) # pops and returns smallest item, and adds new item; the heap size is unchanged
heapq.nlargest(n, L)    # Find the n largest elements in a dataset.
heapq.nsmallest(n, L)   # Find the n smallest elements in a dataset.
```

Graph
-----

> A graph is a finite set of vertices and connected by a set of edges.

```
(1:M)---(0:E)
  |  \    |
  |   \   |
  |    \  |
(2:B)---(3:L)
   \
    \
   (4:P)
```

Types of graphs:
- Undirected Graph: nodes are connected by edges that are all bidirectional.
- Directed Graph: nodes are connected by directed edges – they only go in one direction.

Graph Adjacency List Representation
- The size of the array is equal to the number of nodes.
- A single index, array[i] represents the list of nodes adjacent to the ith node.
```
0 -> 1 -> 3#
1 -> 0 -> 2 -> 3#
2 -> 1 -> 3 -> 4#
3 -> 0 -> 1 -> 2#
4 -> 2#
```

Graph Adjacency Matrix Representation
- An Adjacency Matrix is a 2D array of size V x V where V is the number of nodes in a graph.
- A slot matrix[i][j] = 1 indicates that there is an edge from node i to node j.

|       | 0 | 1 | 2 | 3 | 4 |
|-------|---|---|---|---|---|
| **0** | 0 | 1 | 0 | 1 | 0 |
| **1** | 1 | 0 | 1 | 1 | 0 |
| **2** | 0 | 1 | 0 | 1 | 1 |
| **3** | 1 | 1 | 1 | 0 | 0 |
| **4** | 0 | 0 | 1 | 0 | 0 |
