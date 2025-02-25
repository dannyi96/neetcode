# Leetcode link - https://leetcode.com/problems/subsets/
from typing import *

class Solution:
    # T: O(n*2^n), S: O(n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # consider index i and proceed
            subset.append(nums[i])
            dfs(i + 1)
            # dont consider index i and proceed
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res