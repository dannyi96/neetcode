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
    
    # Two Pointer based. T:O(n), S: O(1)
    def maxProfit_two_pointers(self, prices: List[int]) -> int:
        n = len(prices)
        l, r = 0, 1
        res = 0
        
        while r < n:
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                # Reset
                l = r
            r += 1
        
        return res
    
    # DP based. T:O(n), S: O(1)
    def maxProfit_dp(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]
        
        for sell in prices:
            profit = sell - minBuy
            maxProfit = max(maxProfit, profit)
            minBuy = min(minBuy, sell)
        
        return maxProfit