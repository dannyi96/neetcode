# Leetcode link - https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # In order traversal based. T: O(n), S: O(n)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        # In order traversal
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return arr[k - 1]