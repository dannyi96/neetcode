# Leetcode link - https://neetcode.io/problems/count-number-of-islands
from typing import *

class Solution:
    # DFS based. T: O(m*n), S: O(m*n)
    def numIslands_dfs(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or 
                c >= COLS or grid[r][c] == "0"
            ):
                return
                
            grid[r][c] = "0" # instead of using a visited array
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands