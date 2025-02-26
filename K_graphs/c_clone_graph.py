# Leetcode link - https://leetcode.com/problems/clone-graph/
from typing import *

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    # DFS based. T: O(V+E), S: O(V)
    '''
        The function uses Depth First Search (DFS) to traverse the graph.
        Each node is visited once, so the number of recursive calls is V (number of vertices).
        For each node, we iterate through all of its neighbors, leading to E (number of edges) total iterations.
        Since we only process each node and edge once, the overall time complexity is O(V + E).
    '''
    def cloneGraph_dfs(self, node: Optional[Node]) -> Optional[Node]:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None