# Leetcode Link - https://leetcode.com/problems/daily-temperatures/
# Input: temperatures = [30,38,30,36,35,40,28]
# Output: [1,4,1,2,1,0,0]

from typing import *

class Solution:
    # Bruteforce. T:O(n^2), S: O(1)
    def dailyTemperatures_bruteforce(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []

        for i in range(n):
            # Find next greatest temperature for index i
            days = 0
            for j in range(i+1, n+1):
                days += 1
                if j >= n: break
                if temperatures[j] > temperatures[i]: break

            days = 0 if j == n else days
            res.append(days)
        return res