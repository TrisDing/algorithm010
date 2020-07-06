"""
74. Search a 2D Matrix <Medium>
https://leetcode.com/problems/making-a-large-island/
"""
from typing import List

class Solution:
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        """
        1. 2D Binary Search
        Treat the (m x n) 2D Matrix as sorted 1D array (length = m x n)
        For any element in the array we have: x = matrix[m // n][m % n]
        """
        m = len(matrix)
        if m == 0:
            return False

        n = len(matrix[0])
        if n == 0:
            return False

        l, r = 0, m * n - 1
        while l <= r:
            m = (l + r) // 2
            x = matrix[m // n][m % n]
            if x < target:
                l = m + 1
            elif x > target:
                r = m - 1
            elif x == target:
                return True

        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        """
        2. Diagonal Binary Search
        """
        m = len(matrix)
        if m == 0:
            return False

        n = len(matrix[0])
        if n == 0:
            return False

        # Start from the bottom-left corner to up-right corner
        x, y = m-1, 0
        while x >= 0 and y < n:
            if matrix[x][y] > target:
                x -= 1 # move up
            elif matrix[x][y] < target:
                y += 1 # move right
            else:
                return True

        return False

    def searchMatrix3(self, matrix: List[List[int]], target: int) -> bool:
        """
        3. Twice Binary Search
        """
        m = len(matrix)
        if m == 0:
            return False

        n = len(matrix[0])
        if n == 0:
            return False

        l, r = 0, m - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][-1] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                break

        row = matrix[mid]

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if row[mid] < target:
                l = mid + 1
            elif row[mid] > target:
                r = mid - 1
            elif row[mid] == target:
                return True

        return False

solution = Solution()

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

target = 3 # found
print('searchMatrix1:', solution.searchMatrix1(matrix, target))
print('searchMatrix2:', solution.searchMatrix1(matrix, target))
print('searchMatrix3:', solution.searchMatrix1(matrix, target))

target = 13 # not found
print('searchMatrix1:', solution.searchMatrix1(matrix, target))
print('searchMatrix2:', solution.searchMatrix1(matrix, target))
print('searchMatrix3:', solution.searchMatrix1(matrix, target))
