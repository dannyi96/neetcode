# Leetcode link - https://leetcode.com/problems/koko-eating-bananas/description/
from typing import *
import math

class Solution:
    # Binary search. T: O(n log m), S:(1) [n is the length of the input array piles and m is the maximum number of bananas in a pile.]
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # Range of possible solutions
        res = r

        while l <= r:
            k = (l + r) // 2 # Try k as a candidate

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res