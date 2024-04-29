#PCMS helpers

import numpy as np

def actions(board):
    return [col for col in range(board.shape[1]) if 0 in board[:, col]]

def result(board, player, action):
    new_board = board.copy()
    for r in range(board.shape[0] - 1, -1, -1):
        if np.any(new_board[r, action] == 0):
            new_board[r, action] = player
            break
    return new_board

def check_horizontal(board, player, row, col, n):
    for i in range(n):
        if not (0 <= col + i < board.shape[1] and board[row, col + i] == player):
            return False
    return True

def check_vertical(board, player, row, col, n):
    for i in range(n):
        if not (0 <= row + i < board.shape[0] and board[row + i, col] == player):
            return False
    return True

def check_diagonal(board, player, row, col, n):
  # Check downward-right diagonal
  for i in range(n):
    if not (0 <= row + i < board.shape[0] and 0 <= col + i < board.shape[1] and board[row + i, col + i] == player):
      return False

  # Check upward-right diagonal
  for i in range(n):
    if not (0 <= row - i < board.shape[0] and 0 <= col + i < board.shape[1] and board[row - i, col + i] == player):
      return False

  return True

def terminal(board, n):
    for player in [-1, 1]:
        for r in range(board.shape[0]):
            for c in range(board.shape[1]):
                if (
                    check_horizontal(board, player, r, c, n)
                    or check_vertical(board, player, r, c, n)
                    or check_diagonal(board, player, r, c, n)
                ):
                    return True
    return False

def utility(board, player, n):
    if not terminal(board, n):
        return None

    for r in range(board.shape[0]):
        for c in range(board.shape[1]):
            if (
                check_horizontal(board, player, r, c, n)
                or check_vertical(board, player, r, c, n)
                or check_diagonal(board, player, r, c, n)
            ):
                utility_value = 1 if player == 1 else -1  
                return utility_value
    return 0