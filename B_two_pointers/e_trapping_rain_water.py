# Leetcode link - https://leetcode.com/problems/trapping-rain-water/
from typing import *

# Main idea - column 'i' water -> min(max left column, max right column) - column 'i' height

class Solution:
    # Bruteforce. T: O(n^2), S: O(1)
    def trap_bruteforce(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        
        for i in range(n):
            leftMax = rightMax = height[i]
            # find left max
            for j in range(i):
                leftMax = max(leftMax, height[j])
            # find right max
            for j in range(i + 1, n):
                rightMax = max(rightMax, height[j])
            
            res += min(leftMax, rightMax) - height[i]
        
        return res