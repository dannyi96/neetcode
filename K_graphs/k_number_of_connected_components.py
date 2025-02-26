# Leetcode link - https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
from typing import *

class Solution:
    # DFS based. T: O(V+E), S: O(V+E)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            visit[node] = True
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        res = 0
        for node in range(n):
            if not visit[node]:
                dfs(node)
                res += 1
        return res
