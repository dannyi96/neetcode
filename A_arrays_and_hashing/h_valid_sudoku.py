# Leetcode link - https://leetcode.com/problems/valid-sudoku/
from typing import *
from collections import defaultdict

class Solution:
    
    # Use hashset & validate cols, rows + squares for duplicates. T: O(n^2), S: O(n^2)
    def isValidSudoku_hashset(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set) # unique elems in each col index
        rows = defaultdict(set) # unique elems in each row index
        squares = defaultdict(set) # unique elems in each square (x, y) coordinate
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[ ( r//3, c//3) ]
                ):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        return True
                
        
