# Leetcode link - https://leetcode.com/problems/container-with-most-water/
from typing import *

# Main point:
#  - You may choose any two bars to form a container. 
#  - Return the maximum amount of water a container can store.
#  - it can be seen that area = min(Hl, Hr) * (r-l)

class Solution:
    # Brute Force. T: O(n^2), S: O(1)
    def maxArea_bruteforce(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                res = max(res, min(heights[i], heights[j]) * (j - i))
        return res
    
    # Two Pointer. T: O(n), S: O(1)
    def maxArea_twopointer(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n-1
        res = 0
        
        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            res = max(res, area)
            # if pillar l was the bottleneck
            # note the nuance - will work even when both pillars are same length.
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res