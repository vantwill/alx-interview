#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens
on an NxN chessboard. Write a program that solves the N queens problem.
    Usage: nqueens N
        If the user called the program with the wrong number of arguments,
        print Usage: nqueens N, followed by a new line,
        and exit with the status 1
    where N must be an integer greater or equal to 4
        If N is not an integer, print N must be a number,
        followed by a new line, and exit with the status 1.
        If N is smaller than 4, print N must be at least 4,
        followed by a new line, and exit with the status 1.
    The program should print every possible solution to the problem
        One solution per line
        Format: see example
        You don't have to print the solutions in a specific order
    You are only allowed to import the sys module
"""
import sys


if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    num = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if num < 4:
    print("N must be at least 4")
    sys.exit(1)


def solveNQueens(n):
    """
    Places N non-attacking queens on an NxN chessboard.
    """
    col, pos, neg = set(), set(), set()
    current_board = [[] for n in range(n)]
    solved_board = []

    def backtrack(row):
        """
        Tool for solving constraint satisfaction problems.
        """
        if row == n:
            copy = current_board.copy()
            solved_board.append(copy)
            return

        for c in range(n):
            if c in col or (row + c) in pos or (row - c) in neg:
                continue

            col.add(c)
            pos.add(row + c)
            neg.add(row - c)

            current_board[row] = [row, c]

            backtrack(row + 1)

            col.remove(c)
            pos.remove(row + c)
            neg.remove(row - c)
            current_board[row] = []

    backtrack(0)

    return solved_board


if __name__ == "__main__":
    boards = solveNQueens(num)
    for board in boards:
        print(board)