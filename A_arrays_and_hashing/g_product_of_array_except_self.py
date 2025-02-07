# Leetcode link - https://leetcode.com/problems/product-of-array-except-self/
from typing import *

class Solution:
    # BruteForce. T: O(n^2), S:O(1)
    def productExceptSelf_bruteforce(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        
        for i in range(n):
            running_prod = 1
            for j in range(n):
                if i == j:
                    continue
                running_prod *= nums[j]
            res[i] = running_prod
        
        return res
    
    
        
