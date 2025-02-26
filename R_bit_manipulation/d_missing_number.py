# Leetcode link - https://leetcode.com/problems/missing-number/
from typing import *

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n
        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr