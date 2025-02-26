# Leetcode link - https://leetcode.com/problems/number-of-1-bits/
from typing import *

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res