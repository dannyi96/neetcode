# Leetcode link - https://leetcode.com/problems/binary-tree-right-side-view/

from typing import *
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # BFS. T: O(n), S: O(n)
    def rightSideView_bfs(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for _ in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
    
    # DFS. T: O(n), S: O(n)
    def rightSideView_dfs(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # All w.r.t root.
        # Inorder -> left, root, right
        # Preorder -> root, left, right
        # Postorder -> left, right, root
        def dfs(node, depth):
            if not node:
                return None
            if depth == len(res):
                res.append(node.val)
            
            # Right child first, then left
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return res