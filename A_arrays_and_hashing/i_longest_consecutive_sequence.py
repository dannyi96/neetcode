# Leetcode link - https://leetcode.com/problems/longest-consecutive-sequence/
from collections import defaultdict
from typing import *

class Solution:
    # Bruteforce. T: O(n^2), S:O(n)
    def longestConsecutive_bruteforce(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res
    
    # Sorting. T: O(nlogn), S:O(1)
    def longestConsecutive_sorting(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        res, streak = 0, 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]: # to prevent resetting of the streak when duplicate elems are encountered
                continue
            elif nums[i] == nums[i - 1] + 1:
                streak += 1
            else:
                res = max(res, streak)
                streak = 1
        
        return max(res, streak)
    
    # Hashset based. T: O(n), S:O(n)
    def longestConsecutive_hashset(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # indicates num is starting point of the consecutive sequence
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    
    # Hashmap based. T: O(n), S:O(n)
    def longestConsecutive_hashmap(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        res = 0

        for num in nums:
            if not hashMap[num]:
                hashMap[num] = hashMap[num - 1] + 1 + hashMap[num + 1]  # Sequence Length
                hashMap[num - hashMap[num - 1]] = hashMap[num] # Update the left boundary
                hashMap[num + hashMap[num + 1]] = hashMap[num] # Update the right boundary
                res = max(res, hashMap[num])
        return res