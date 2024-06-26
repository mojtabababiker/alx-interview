#!/usr/bin/python3
"""
The N queens module, is to place N non-attacking
queens on an N×N chessboard
"""
import sys


solutions = []


def is_safe_pos(board: list, row: int, col: int) -> bool:
    """
    Check if the current position is a safe for putting a queen on

    Parameters:
    -----------
    board: list[list], indicate the current board state
    row: int, the current row on the board to place the queen on
    col: int, the current col on the board to place the queen on

    Returns:
    bool: indicate is safe or not
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve(board: list, col: int, sol: list = []):
    """
    solve N-queens problem using  backtracking algorithim


    Parameters:
    -----------
    board: list[list], the board to place the queens on
    col: int, the current col on the board to place the queen

    Returns:
    -----------
    None
    """

    if col >= len(board):
        solutions.append(sol[:])
        return
    for i in range(len(board)):
        if is_safe_pos(board, i, col):
            board[i][col] = 1
            sol.append([i, col])

            solve(board, col + 1, sol)  # recurs

            board[i][col] = 0  # backtracking
            sol.remove([i, col])  # backtracking

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)

    board = [[0] * N for _ in range(N)]
    solve(board, 0)
    for sol in solutions:
        print(sorted(sol, key=lambda e: e[0]))
