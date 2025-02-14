# Leetcode link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import *

class Solution:
    # Bruteforce. T:O(n^2), S: O(1)
    def maxProfit_bruteforce(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell  = prices[j]
                res = max(res, sell - buy)
        return res
    
    # Bruteforce. T:O(n^2), S: O(1)
    def maxProfit_two_pointers(self, prices: List[int]) -> int:
        pass