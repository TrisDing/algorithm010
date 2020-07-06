"""
200. Number of Islands <Medium>
https://leetcode.com/problems/number-of-islands/

695. Max Area of Island <Medium>
https://leetcode.com/problems/max-area-of-island/

463. Island Perimeter <Easy>
https://leetcode.com/problems/island-perimeter/

827. Making A Large Island <Hard>
https://leetcode.com/problems/making-a-large-island/
"""
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        def countIsland(r, c):
            if 0 <= r < m and 0 <= c < n and grid[r][c] == '1':
                grid[r][c] = '0'
                countIsland(r+1, c)
                countIsland(r-1, c)
                countIsland(r, c+1)
                countIsland(r, c-1)

        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    count += 1
                    countIsland(r, c)

        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def area(grid, r, c):
            if not inArea(grid, r, c):
                return 0
            if grid[r][c] != 1: # ocean or visited
                return 0
            grid[r][c] = -1 # mark as visited
            return 1 \
                + area(grid, r, c-1) \
                + area(grid, r+1, c) \
                + area(grid, r, c+1) \
                + area(grid, r-1, c)

        def inArea(grid, r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        maxArea = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    islandArea = area(grid, r, c)
                    maxArea = max(maxArea, islandArea)

        return maxArea

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def perimeter(r, c):
            if not (0 <= r < m and 0 <= c < n): # boundary
                return 1
            if grid[r][c] == 0: # ocean
                return 1
            if grid[r][c] != 1: # not land or visited
                return 0
            grid[r][c] = -1
            return perimeter(r+1, c) \
                 + perimeter(r-1, c) \
                 + perimeter(r, c+1) \
                 + perimeter(r, c-1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return perimeter(r, c)

        return 0

    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def area(r, c, index):
            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                grid[r][c] = index
                return 1 \
                    + area(r+1, c, index) \
                    + area(r-1, c, index) \
                    + area(r, c+1, index) \
                    + area(r, c-1, index)
            return 0

        areas = {}
        index = 2
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    areas[index] = area(r, c, index)
                    index += 1

        def connect(r, c):
            if 0 <= r < m and 0 <= c < n and grid[r][c] > 1:
                return grid[r][c]
            return -1

        res = max(areas.values() or [0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    surroundings = set([
                        connect(r+1, c),
                        connect(r-1, c),
                        connect(r, c+1),
                        connect(r, c-1)
                    ])
                    res = max(res, sum(areas[index] for index in surroundings if index > 0) + 1)

        return res

solution = Solution()

grid = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]
print('numIslands:', solution.numIslands(grid)) # 1

grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
print('numIslands:', solution.numIslands(grid)) # 3

grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
print('maxAreaOfIsland:', solution.maxAreaOfIsland(grid)) # 6

grid = [[0,0,0,0,0,0,0,0]]
print('maxAreaOfIsland:', solution.maxAreaOfIsland(grid)) # 0

grid = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
]
print('islandPerimeter:', solution.islandPerimeter(grid)) # 16

grid = [[1, 0], [0, 1]]
print('largestIsland', solution.largestIsland(grid)) # 3

grid = [[1, 1], [1, 0]]
print('largestIsland', solution.largestIsland(grid)) # 4

grid = [[1, 1], [1, 1]]
print('largestIsland', solution.largestIsland(grid)) # 4
