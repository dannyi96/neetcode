# Leetcode link - https://leetcode.com/problems/contains-duplicate/
from typing import *

class Solution:
    # Brute force -> T: O(n^2), S: O(1)
    def hasDuplicates_bruteforce(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
        return False

    # Sorting -> T: O(nlogn), S: O(1)/O(n) based on sorting
    def hasDuplicates_sorting(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    
    # Hashset -> T: O(n), S: O(n)
    def hasDuplicates_hashset(self, nums: List[int]) -> bool:
        seen = set()
        for elem in nums:
            if elem in seen:
                return True
            seen.add(elem)
        return False

    # Hashset vs numsay length -> T: O(n), S: O(n)
    def hasDuplicates_hashset_nums_length(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)