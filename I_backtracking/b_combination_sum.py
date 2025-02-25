# Leetcode link - https://leetcode.com/problems/combination-sum/description/
from typing import *

class Solution:
    # T: O(2^(t/m)), S: O(2^(t/m)) [ where t is target, m is minimum value in nums ]
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res