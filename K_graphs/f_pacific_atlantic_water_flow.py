# Leetcode link - https://leetcode.com/problems/pacific-atlantic-water-flow/
from typing import *

class Solution:
    # DFS based. T: O(mn), S: O(mn)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        M, N = len(heights), len(heights[0])
        
        atlantic, pacific = set(), set()
        
        def dfs(row, col, visited, prevHeight = -1):
            if ( row < 0 or col < 0 or 
                 row >= M or col >= N or
                 (row, col) in visited or
                 heights[row][col] < prevHeight):
                return
            
            visited.add((row, col))
            
            dfs(row+1, col, visited, heights[row][col])
            dfs(row-1, col, visited, heights[row][col])
            dfs(row, col+1, visited, heights[row][col])
            dfs(row, col-1, visited, heights[row][col])
            
        
        # Get all reachable wih fixed column
        for r in range(M):
            dfs(r, 0, pacific)
            dfs(r, N-1, atlantic)
            
        # Get all reachable wih fixed row
        for c in range(N):
            dfs(0, c, pacific)
            dfs(M-1, c, atlantic)
            
        return pacific & atlantic