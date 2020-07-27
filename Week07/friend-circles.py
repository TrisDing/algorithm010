"""
547. Friend Circles [Medium]
https://leetcode.com/problems/friend-circles/
"""
from typing import List

class DisjointSet:
    def __init__(self, size):
        self.count = size
        self.parents = [i for i in range(size)]
        self.weights = [1 for _ in range(size)]

    def find(self, x):
        parents = self.parents
        while x != parents[x]:
            # Compression: reduce the path to the root
            parents[x] = parents[parents[x]]
            x = parents[x]
        return x

    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x != parent_y:
            weights = self.weights
            parents = self.parents
            # balancing: connect "lighter" tree onto the "heavier" tree
            if weights[parent_x] > weights[parent_y]:
                parents[parent_y] = parent_x
                weights[parent_x] += weights[parent_y]
            else:
                parents[parent_x] = parent_y
                weights[parent_y] += weights[parent_x]
            self.count -= 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        ds = DisjointSet(N)
        for i in range(N):
            for j in range(N):
                if M[i][j] == 1 and i != j:
                    ds.union(i, j)

        return ds.count

solution = Solution()
ans = solution.findCircleNum([[1,1,0], [1,1,0], [0,0,1]])
print(ans) # 2
ans = solution.findCircleNum([[1,1,0], [1,1,1], [0,1,1]])
print(ans) # 1