from typing import List
import numpy as np


# problem set 1
# Sudoku
class Problem:
  def solveSudoku(self, board: List[List[str]]) -> None:
    if not board:
      return
    self.solve(board)

  def solve(self, board: List[List[str]]) -> None:
    nums_str = "123456789"
    for i in range(9):
      for j in range(9):
        if board[i][j] == '.':
          for c in nums_str:
            if self.is_valid(board, i, j, c):
              board[i][j] = c

              if self.solve(board):
                return True
              else:
                board[i][j] = '.'
          return False

    return True

  def is_valid(self, board, row, col, c):
    for i in range(9):
      # Check columns
      if board[i][col] != '.' and board[i][col] == c:
        return False
      # Check rows
      if board[row][i] != '.' and board[row][i] == c:
        return False

      # Check 3x3 square
      if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] != '.' and board[3 * (row // 3) + i // 3][
        3 * (col // 3) + i % 3] == c:
        return False
    return True


if __name__ == "__main__":
  # Run actual funcs
  test = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
  solver = Problem()

  solver.solveSudoku(test)

  print(test)
