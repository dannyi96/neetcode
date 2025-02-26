# Leetcode link - https://leetcode.com/problems/house-robber-ii/
from typing import *

class Solution:
    def rob_1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        return dp[-1]
    
    # T: O(n), S: O(n) --> can be space optimised to O(1)
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        return max(
            self.rob_1(nums[:n-1]),
            self.rob_1(nums[1:])
        )