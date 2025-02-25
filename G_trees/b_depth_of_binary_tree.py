# Leetcode link - https://leetcode.com/problems/maximum-depth-of-binary-tree/
from typing import *
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive DFS. T: O(n), S: O(h)
    def maxDepth_dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth_dfs(root.left), self.maxDepth_dfs(root.right))
    
    # BFS. T: O(n), S: O(n)
    def maxDepth_bfs(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level