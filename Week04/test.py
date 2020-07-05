import collections

class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def DFS1(root: TreeNode):
    """
    Recursively
    """
    def _dfs(node, visited = set()):
        # terminator
        if not node:
            return
        # already visited
        if node in visited:
            return
        # process current node
        res.append(node.val)
        # add to visited
        visited.add(node)
        # process children (drill down)
        if node.children:
            for child in node.children:
                if child not in visited:
                    _dfs(child, visited)
    res = []
    _dfs(root)
    return res

def DFS2(root: TreeNode):
    """
    Iteratively
    """
    if not root:
        return []
    res = []
    visited = set()
    stack = [root]
    # Loop until stack is empty
    while stack:
        # get current node from stack
        node = stack.pop()
        # already visited
        if node in visited:
            continue
        # process current node
        res.append(node.val)
        # add to visited
        visited.add(node)
        # process children
        if node.children:
            for child in node.children[::-1]:
                if child not in visited:
                    stack.append(child)
    return res

def BFS1(root: TreeNode):
    """
    Recursively
    """
    def _bfs(node, level = 0, visited = set()):
        # terminator
        if not node:
            return
        # already visited
        if node in visited:
            return
        # process all nodes from the current level
        if len(res) == level:
            res.append([])
        res[level].append(node.val)
        # add to visited
        visited.add(node)
        # process children (drill down)
        if node.children:
            for child in node.children:
                if child not in visited:
                    _bfs(child, level + 1, visited)
    res = []
    _bfs(root)
    return [node for level in res for node in level] # flatten

def BFS2(root: TreeNode):
    """
    Iteratively
    """
    if not root:
        return []
    res = []
    visited = set()
    queue = collections.deque([root])
    # Loop until queue is empty
    while queue:
        n = len(queue)
        level_nodes = []
        # process all nodes from the current level
        for _ in range(n):
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
    return [node for level in res for node in level] # flatten

tree = TreeNode(1, [TreeNode(3, [TreeNode(5), TreeNode(6)]), TreeNode(2), TreeNode(4)])
"""
      ___1___
     /   |   \
  __3__  2    4
 /     \
5       6
"""
print(DFS1(tree))
print(DFS2(tree))
print(BFS1(tree))
print(BFS2(tree))

def ShortestPathDFS(root, target):
    if not root:
        return -1
    step = 0
    visited = set()
    stack = [root]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        if node is target:
            return step
        if node.children:
            for child in node.children:
                if child not in visited:
                    stack.append(child)
                    visited.add(child)
        step += 1
    return step

target = TreeNode(6)
tree = TreeNode(1, [TreeNode(3, [TreeNode(5), target]), TreeNode(2), TreeNode(4)])
print(ShortestPathDFS(tree, target))
print(ShortestPathBFS(tree, target))