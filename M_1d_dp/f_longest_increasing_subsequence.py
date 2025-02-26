# Leetcode link - https://leetcode.com/problems/longest-increasing-subsequence/description/
from typing import *

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [ [None] * (n) ] * n 
        
        def f(index, prevIndex=-1):
            
            if index == n:
                return 0

            if dp[index][prevIndex+1] is not None:
                return dp[index][prevIndex+1]

            notChoose = f(index+1, prevIndex)
            choose = 0
            if prevIndex == -1 or nums[prevIndex] < nums[index]:
                choose = 1 + f(index+1, index)
            dp[index][prevIndex+1] = max(choose, notChoose)
            return dp[index][prevIndex+1]
        
        return f(0)