Learning Notes Week 02
======================

Hash Table
----------

> A hash table is a data structure used to store keys, optionally, with corresponding values.

- A mapping object maps hashable values to arbitrary objects. Mappings are mutable objects. The only standard mapping type in python is Dictionary.
- A dictionary’s keys are almost arbitrary values. Values that are not hashable (like lists, dictionaries or other mutable types) may not be used as keys.
- Dictionaries can be created by placing a comma-separated list of key: value pairs within braces or by the dict() constructor.
- A set is an unordered collection with no duplicate elements. Curly braces or the set() function can be used to create sets. (empty set must use set())

| Operation  | Time Complexity |
| ---------- | :-------------: |
| Access     | N/A             |
| Search     | O(1)            |
| Insertion  | O(1)            |
| Deletion   | O(1)            |

Dictionary Operations
```py
d[key]                 # Return the item of d with key key. Raises a KeyError if key is not in the map.
d[key] = value         # Set d[key] to value.
del d[key]             # Remove d[key] from d. Raises a KeyError if key is not in the map.
key in d               # Return True if d has a key key, else False.
key not in d           # Equivalent to not key in d.
d.clear()              # Remove all items from the dictionary.
d.get(key[, default])  # Return the value for key if key is in the dictionary, else default.
d.items()              # Return a new view of the dictionary’s items ((key, value) pairs).
d.keys()               # Return a new view of the dictionary’s keys.
d.values()             # Return a new view of the dictionary’s values.
```

Binary Trees
------------

> A binary tree is either empty, or a root node together with a left binary tree and a right binary tree.

| Operation  | Time Complexity |
| ---------- | :-------------: |
| Access     | O(log(n))       |
| Search     | O(log(n))       |
| Insertion  | O(log(n))       |
| Deletion   | O(log(n))       |

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

[A,B,C,D,E,F,G,H]
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
        self.postorder(left)
        self.postorder(right)
        self.visit(root)
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

Heap
----

> A heap is a complete binary tree, and is represent by array. The children of the node at index i are at indices 2i + 1 and 2i + 2.

Given element in a heap at position `i`:
- parent position: `(i-1) >> 1`
- left child position: `2*i + 1`
- right child position: `2*i + 2`

| Operation  | Time Complexity |
| ---------- | :-------------: |
| find-min   | O(1)            |
| delete-min | O(logn)         |
| Insert     | O(logn)         |
| K largest  | O(nlogK)        |
| K smallest | O(nlogK)        |

max-heap: the key at each node is at least as great as the keys at it's children.
```
           _____561_____
          /             \
     ___314_           _401_
    /       \         /     \
  _28       156     359     271
 /   \
11    3
```

min-heap: the key at each node is at least as small as the keys at it's children.
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