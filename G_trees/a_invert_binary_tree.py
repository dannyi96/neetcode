# Leetcode link - https://leetcode.com/problems/invert-binary-tree/
from typing import *
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # BFS based. T: O(n), S: O(n)
    def invertTree_bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

    # DFS based. T: O(n), S: O(n)
    def invertTree_dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        root.left, root.right = root.right, root.left
        
        self.invertTree_dfs(root.left)
        self.invertTree_dfs(root.right)
        
        return root