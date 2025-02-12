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
    
    # Prefix, Suffix array based. T: O(n), S: O(n)
    def trap_prefix_suffix_array(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        
        res = 0
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res

    # Monotonic Stack based. T: O(n), S: O(n)
    def trap_monotonic_stack(self, height: List[int]) -> int:
        stack = [] # We maintain a non increasing monotonic stack
        res = 0
        
        for index, cur_height in enumerate(height):
            # as long as current height exceeds top of stack
            while stack and cur_height >= height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    right = cur_height
                    left = height[stack[-1]]
                    h = min(left, right) - mid
                    w = index - stack[-1] - 1
                    res += h * w
            # Store the index of height in stack
            stack.append(index)

        return res
    
    