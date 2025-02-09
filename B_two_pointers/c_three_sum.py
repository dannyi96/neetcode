# Leetcode link - https://leetcode.com/problems/3sum/
from typing import *
from collections import Counter

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
    
    # Counter Hashmap based -> T: O(n^2), S: O(n)
    def threeSum_hashmap(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort() # To help in duplicate handling
        counterMap = Counter(nums) # Compute counter map
        
        res = []
        for i in range(n):
            counterMap[nums[i]] -= 1
            # For skipping duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, n):
                counterMap[nums[j]] -= 1
                # For skipping duplicates
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                # default val for Counter for key is not present is 0
                if counterMap[target] > 0:
                    res.append([nums[i], nums[j], target])

            # Readd data from [j...n-1] back to counter map
            for j in range(i + 1, len(nums)):
                counterMap[nums[j]] += 1

        return res
                    
    # Two Pointer based -> T: O(n^2), S: O(1) / O(n) based on sorting algorithm
    def threeSum_two_pointer(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        res = []
        for i, a in enumerate(nums):
            # If number is +ve(post sorting), no chance to get three sum as 0. Hence early quit
            if a > 0:
                break

            # Handling duplicates - 1st number
            if i > 0 and a == nums[i - 1]:
                continue

            # Rest of the problem -> treated as a sorted array 2 sum problem
            l, r = i + 1, n - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Handling duplicates - 2nd number
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res