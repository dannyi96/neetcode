# Leetcode link - https://leetcode.com/problems/climbing-stairs/
from typing import *

class Solution:
    # T: O(n), S: O(n) --> can be space optimised to O(1)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]