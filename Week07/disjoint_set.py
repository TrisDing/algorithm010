"""
Disjoint-set Data Structure
"""
class DisjointSet:
    def __init__(self, size):
        self.parents = [i for i in range(size)]

    def find(self, x):
        """
        Worse Case: O(N)
        """
        parents = self.parents
        while x != parents[x]:
            x = parents[x]
        return x

    def union(self, x, y):
        """
        Worse Case: O(N)
        """
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x != parent_y:
            self.parents[parent_x] = parent_y

    def connected(self, x, y):
        return self.find(x) == self.find(y)

ds = DisjointSet(5)
print(ds.find(1)) # 1
print(ds.connected(1, 2)) # False
ds.union(1, 2)
print(ds.find(1)) # 2
print(ds.find(2)) # 2
print(ds.connected(1, 2)) # True

"""
Disjoint-set Data Structure Optimized
"""
class DisjointSetOptimized:
    def __init__(self, size):
        self.count = size
        self.parents = [i for i in range(size)]
        self.weights = [1 for _ in range(size)]

    def find(self, x):
        """
        Close to O(1)
        """
        parents = self.parents
        while x != parents[x]:
            # Compression: reduce the path to the root
            parents[x] = parents[parents[x]]
            x = parents[x]
        return x

    def union(self, x, y):
        """
        Average Case: O(logN)
        """
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

ds = DisjointSetOptimized(5)
print(ds.find(1)) # 1
print(ds.connected(1, 2)) # False
ds.union(1, 2)
print(ds.find(1)) # 2
print(ds.find(2)) # 2
print(ds.connected(1, 2)) # True