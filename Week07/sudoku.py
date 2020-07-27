"""
36. Valid Sudoku <Medium>
https://leetcode.com/problems/valid-sudoku/

37. Sudoku Solver <Hard>
https://leetcode.com/problems/sudoku-solver/
"""
from typing import List
from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [Counter() for _ in range(9)]
        col = [Counter() for _ in range(9)]
        box = [Counter() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    k = (i // 3) * 3 + (j // 3) # box index

                    row[i][num] += 1
                    col[j][num] += 1
                    box[k][num] += 1

                    if row[i][num] > 1 or col[j][num] > 1 or box[k][num] > 1:
                        return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nums = ['1','2','3','4','5','6','7','8','9']

        def backtrack(row = 0, col = 0):
            if col == 9:
                return backtrack(row + 1, 0) # next row

            if row == 9:
                return True # end of board

            if board[row][col] != '.':
                return backtrack(row, col + 1) # next number

            for num in nums:
                if not isValid(row, col, num):
                    continue

                board[row][col] = num
                if backtrack(row, col + 1):
                    return True # found an solution
                board[row][col] = '.'

            return False

        def isValid(r, c, n) -> bool:
            for i in range(9):
                if board[r][i] == n:
                    return False
                if board[i][c] == n:
                    return False
                if board[(r//3)*3 + i//3][(c//3)*3 + i%3] == n:
                    return False
            return True

        backtrack()


solution = Solution()

board1 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

board2 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(solution.isValidSudoku(board1)) # True
print(solution.isValidSudoku(board2)) # True

solution.solveSudoku(board1)
print(board1)
# ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
# ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
# ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
# ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
# ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
# ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
# ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
# ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
# ['3', '4', '5', '2', '8', '6', '1', '7', '9'],