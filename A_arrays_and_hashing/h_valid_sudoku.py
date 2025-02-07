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
    
    # Bitmask based. T: O(n^2), S: O(n)
    def isValidSudoku_bitmask(self, board: List[List[str]]) -> bool:
        # Instead of storing multiple numbers 0-9 in the set for each index,
        # we can store only one number whose bit position determines the actual number
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                val = int(board[r][c]) - 1
                # Check if already exists - row, col, square
                if (1 << val) & rows[r]:
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & squares[(r // 3) * 3 + (c // 3)]:
                    return False
                
                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                squares[(r // 3) * 3 + (c // 3)] |= (1 << val)
        
        return True
