Learning Notes Week 04
======================

DFS Template
------------

```py
visited = set()

def dfs(node):
    # terminator
    if not node:
        return

    # already visited
    if node in visited:
        return

    # process current node
    process(node.val)

    # add to visited
    visited.add(node)

    # process children (drill down)
    if node.children:
        for child in node.children:
            if child not in visited:
                dfs(child, visited)
```

DFS Application
---------------

Island Problem
```py
def island(self, grid: List[List[int]]):
    # length of row and column
    m, n = len(grid), len(grid[0])

    def dfs(r, c):
        # base case: grid[r][c] is out of bound
        if not inArea(r, c):
            return

        # current node is not an island, or it's already visited
        if grid[r][c] != 1:
            return

        # mark as visited
        grid[r][c] = 2

        # visit neighbor nodes
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)

    def inArea(r, c):
        return 0 <= r < m and 0 <= c < n
```

Backtrack (see Week03 NOTE)

Leetcode Problems
- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
- [463. Island Perimeter](https://leetcode.com/problems/island-perimeter/)
- [827. Making A Large Island](https://leetcode.com/problems/making-a-large-island/)

BFS Template
------------

```py
def bfs(root):
    visited = set()
    queue = collections.deque([root])

    # Loop until queue is empty
    while queue:
        # get current node from queue
        node = queue.popleft()
        # process current node
        process(node.val)
        # add to visited
        visited.add(node)
        # process children
        if node.children:
            for child in node.children:
                if child not in visited:
                    queue.append(child)
```

BFS Application
---------------

Level Order
```py
def bfs(root):
    res = []
    visited = set()
    queue = collections.deque([root])

    # Loop until queue is empty
    while queue:
        # process all nodes from the current level
        level_nodes = []
        for _ in range(len(queue)):
            # get current node from queue
            node = queue.popleft()
            # process current node
            level_nodes.append(node.val)
            # add to visited
            visited.add(node)
            # process children
            if node.children:
                for child in node.children:
                    if child not in visited:
                        queue.append(child)
        res.append(level_nodes)

    return res
```

Shorted Path
```py
def bfs(start, target): # any two nodes, doesn't have to start from the root
    step = 0
    visited = set()
    queue = collections.deque([start])

    # Loop until queue is empty
    while queue:
        # spread the search from the current level
        for _ in range(len(queue)):
            # get current node from queue
            node = queue.popleft()
            # see if we reach the target
            if node is target:
                return step
            # add to visited
            visited.add(node)
            # process children
            if node.children:
                for child in node.children:
                    if child not in visited:
                        queue.append(child)
        step += 1

    return 0
```

Leetcode Problems
- [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
- [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
- [752. Open the Lock](https://leetcode.com/problems/open-the-lock/)
- [127. Word Ladder](https://leetcode.com/problems/word-ladder/)
- [126. Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)
- [433. Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/)
- [515. Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/)
- [529. Minesweeper](https://leetcode.com/problems/minesweeper/)

Greedy Algorithm
----------------
[TODO]

Binary Search
-------------

- Monotonically increasing/decreasing
- Bounded (have upper and lower bound)
- Index accessible

[left, right]
```py
def binary_search(nums, target)
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            return mid
    return -1
```

[left, right)
```py
def left_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # don't return, lock down the left boundary
            right = mid - 1

    # check if left is out of boundary
    if left >= nums.length or nums[left] != target
        return -1
    return left
}
```

(left, right]
```py
def right_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # don't return, lock down the right boundary
            left = mid + 1

    # check if right is out of boundary
    if right < 0 or nums[right] != target
        return -1
    return right
}
```

Target Function g(m)
```py
def binary_search(l, r):
    """
    Returns the smallest number m in range [l, r] such that g(m) is true.
    Returns r+1 if not found.

    Time Complexity: O(log(r - l) * (f(m) + g(m)))
    Space Complexity: O(1)
    """
    while l <= r:
        m = l + (r - l) // 2
        if f(m): # optional: if somehow we can determine m is the answer, return it
            return m
        if g(m):
            r = m - 1  # new range [l, m-1]
        else:
            l = m + 1  # new range [m+1, r]
    return l # or not found
```

Leetcode Problems
- [704. Binary Search](https://leetcode.com/problems/binary-search/)
- [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)
- [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
- [367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)