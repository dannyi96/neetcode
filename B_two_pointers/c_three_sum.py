# Leetcode link - https://leetcode.com/problems/3sum/
from typing import *

# Key points
# - we need to return the list of numbers and not the indices
# - we should not return duplicates ( eg - [1,2,3] & [2,3,1] )

class Solution:
    # Brute force -> T: O(n^3), S: O(m) [ where m is the number of triplets ]
    def threeSum_bruteforce(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort() # Sorting helps to overcome to duplicate issue ( eg - [-1,-2,3,-2,3,-1] )
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp))
        return [list(i) for i in res]
    
    
