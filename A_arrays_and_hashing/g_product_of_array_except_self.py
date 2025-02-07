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
    
    # Division based with zero number handling. T: O(n), S:O(1)
    def productExceptSelf_division(self, nums: List[int]) -> List[int]:
        # Get total product(excluding 0s) & total 0 count
        product = 1
        zeroCount = 0
        for num in nums:
            if num:
                product *= num
            else:
                zeroCount += 1
        
        # if 2+ zeros, then final ans will be all 0s
        if zeroCount >= 2:
            return [0] * len(nums)

        res = [0] * len(nums)
        for index, num in enumerate(nums):
            if zeroCount:
                res[index] = 0 if num else product
            else:
                res[index] = product // num
        return res
        
    # Prefix, Suffix based. T: O(n), S:O(n)
    def productExceptSelf_division(self, nums: List[int]) -> List[int]:
        pass