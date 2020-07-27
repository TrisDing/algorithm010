Learning Notes Week 07
======================

Trie
----
> A trie is a tree-like data structure whose nodes store the letters of an alphabet. By structuring the nodes in a particular way, words and strings can be retrieved from the structure by traversing down a branch path of the tree.

```py
def buildTrie(words):
    trie = {}
    for word in words:
        node = trie
        for char in word:
            node = node.setdefault(char, {})
        node['#'] = True
    return trie
```

```
trie = buildTrie(["app", "apple", "bar", "ball"])

   ()
  /  \
 a    b
 |    |
 p    a
 |   / \
 p   r l
/ \  | |
# l  # l
  |    |
  e    #
  |
  #
```

Leetcode Problems
- [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
- [212. Word Search II](https://leetcode.com/problems/word-search-ii/)

Disjoint-set (Union-find set)
------------
> A disjoint-set data structure is a data structure that tracks a set of elements partitioned into a number of disjoint (non-overlapping) subsets. It provides near-constant-time operations to add new sets, to merge existing sets, and to determine whether elements are in the same set.

```py
ds = DisjointSet(5)

(0) (1) (2) (3) (4)

ds.union(1, 2)
ds.union(3, 4)

(0) (1) (3)
     |   |
    (2) (4)
```

Leetcode Problems
- [547. Friend Circles](https://leetcode.com/problems/friend-circles/)
- [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)
- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)

Advanced Search
---------------

Backtrack DFS with Pruning
```py
# Generate Parenthesis
def dfs(left = 0, right = 0, path = ''):
    if left == n and right == n:
        res.append(path)
        return

    if right > left: # Pruning
        return

    if left < n:
        dfs(left + 1, right, path + '(')

    if right < n:
        dfs(left, right + 1, path + ')')
```

Bidirectional BFS
```py
sourceQueue = collections.deque([source])
targetQueue = collections.deque([target])
visited = set([source])
step = 0

while sourceQueue and targetQueue:
    step += 1

    # choose the smaller queue to spread
    if len(sourceQueue) > len(targetQueue):
        sourceQueue, targetQueue = targetQueue, sourceQueue

    for _ in range(len(sourceQueue)):
        node = sourceQueue.popleft()

        for child in node.children:
            # source and target meet
            if child in targetQueue:
                return step + 1

            if not child in visited:
                sourceQueue.append(child)
                visited.add(child)

return 0 # not found
```

A-Star (A*) Search
```py
def AstarSearch(graph, start, end):
	pq = collections.priority_queue() # priority —> heuristic function
	pq.append([start])
	visited.add(start)
	while pq:
		node = pq.pop() # can we add more intelligence here?
		visited.add(node)
		process(node)
		nodes = generate_related_nodes(node)
        unvisited = [node for node in nodes if node not in visited]
		pq.push(unvisited)
```

Leetcode Problems
- [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
- [51. N-Queens](https://leetcode.com/problems/n-queens/)
- [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)
- [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)
- [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)
- [773. Sliding Puzzle](https://leetcode.com/problems/sliding-puzzle/)

Self-balancing Binary Search Tree
--------------

> A self-balancing (or height-balanced) BST is any node-based BST that automatically keeps its height (maximal number of levels below the root) small in the face of arbitrary item insertions and deletions.

AVL Tree

> In an AVL tree, the heights of the two child subtrees of any node differ by at most one; if at any time they differ by more than one, re-balancing is done to restore this property. Lookup, insertion, and deletion all take O(log n) time in both the average and worst cases.

```py
BalanceFactor(node) = Height(RightSubtree(node)) - Height(LeftSubtree(node))
BalanceFactor(node) = {-1, 0, 1}
```

4 Types of Rotations
```
Left-Left Case, right rotation:

    A (-2)      B (0)
   /          /   \
  B (-1)     C (0) A (0)
 /
C (0)

Right Right Case, left rotation:

A (2)           B (0)
 \            /   \
  B (1)      A (0) C (0)
   \
    C (0)

Left-Right Case, right rotation -> left rotation:

  A (-2)       A (-2)      C (0)
 /            /          /   \
B (1)        C (-1)     B (0) A (0)
 \          /
  C (0)    B (0)

Right-Left Case, left rotation -> right rotation:

A (-2)      A (-2)         C (0)
 \           \           /   \
  B (-1)      C (-1)    A (0) B (0)
 /             \
C (0)           B (0)
```

With Subtree
```
                              right rotation
                            ------------------>
                               Y            X
                              / \          / \
                             X  T3        T1  Y
                            / \              / \
                           T1 T2            T2 T3
                            <------------------
                                left rotation

                     Case 1                      Case 4
                 Z           Y       |       Y           Z
                / \        /   \     |     /   \        / \
               Y  T4      X     Z    |    Z     X      T1  Y
              / \        / \   / \   |   / \   / \        / \
             X  T3      T1 T2 T3 T4  |  T1 T2 T3 T4      T2  X
            / \                      |                      / \
           T1 T2                     |                     T3 T4

                 Case 2                              Case 3
      Z           Z          X       |       Y         Z          Z
     / \         / \       /   \     |     /   \      / \        / \
    Y  T4       X  T4     Y     Z    |    Z     X    T1  Y      T1  Y
   / \         / \       / \   / \   |   / \   / \      / \        / \
  T1   X      Y  T3     T1 T2 T3 T4  |  T1 T2 T3 T4    T2  X      X  T4
      / \    / \                     |                    / \    / \
     T1 T2  T1 T2                    |                   T3 T4  T2 T3
```

Red-Black Tree

> In a red–black tree, each node stores an extra bit representing color, used to ensure that the tree remains approximately balanced during insertions and deletions.

Properties
- Each node is either red or black.
- The root is black. This rule is sometimes omitted. Since the root can always be changed from red to black, but not necessarily vice versa, this rule has little effect on analysis.
- All leaves (NIL) are black.
- If a node is red, then both its children are black.
- Every path from a given node to any of its descendant NIL nodes goes through the same number of black nodes.