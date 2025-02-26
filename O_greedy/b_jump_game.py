# Leetcode link - https://leetcode.com/problems/jump-game/description/
from typing import *

class Solution:
    def canJump_greedy(self, nums: List[int]) -> bool:
        # Shifting goalposts from the right
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0