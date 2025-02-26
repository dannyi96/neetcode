# Leetcode link - https://leetcode.com/problems/surrounded-regions/
from typing import *

# Reverse thinking ( S = A + B)
# - Capture surrounded regions ( give A )
# - Capture everything except unsurrounded regions (Reverse thinking) ( give S - B )

class Solution:
    # DFS based. T: O(mn), S: O(mn)
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or 
                c == COLS or board[r][c] != "O"
            ):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # for all cells at first & last column
        for r in range(ROWS):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][COLS - 1] == "O":
                capture(r, COLS - 1)
        
        # for all cells at first & last row
        for c in range(COLS):
            if board[0][c] == "O":
                capture(0, c)
            if board[ROWS - 1][c] == "O":
                capture(ROWS - 1, c)

        # Update the board accordingly
        for r in range(ROWS):
            for c in range(COLS):
                # if still O -> surrounded region
                if board[r][c] == "O":
                    board[r][c] = "X"
                # replace our temp T back to O for unsurrounded region
                elif board[r][c] == "T":
                    board[r][c] = "O"
