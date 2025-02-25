# Leetcode link - https://leetcode.com/problems/subtree-of-another-tree/
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Time: O(m*n), Space: O(m+n) [skewed trees]
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                return (sameTree(root.left, subRoot.left) and 
                    sameTree(root.right, subRoot.right))
            return False
        
        if not subRoot:
            return True
        if not root:
            return False

        if sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or 
               self.isSubtree(root.right, subRoot))

