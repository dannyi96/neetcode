# Leetcode link - https://leetcode.com/problems/find-the-duplicate-number/
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.

from typing import *

class Solution:
    # Sorting based. T: O(nlogn), S: O(1)
    def findDuplicate_sorting(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return -1

    # Hashset based. T: O(n), S: O(n)
    def findDuplicate_hashset(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1

    # -ve marking based. T: O(n), S: O(1) [updating data in nums array itself]
    def findDuplicate_negative_marking(self, nums: List[int]) -> int:
        for num in nums:
            idx = abs(num) - 1   # Get the index corresponding to num
            if nums[idx] < 0:     # If the number at that index is already negative, it means we've seen it before
                return abs(num)   # Return the duplicate number
            nums[idx] *= -1       # Mark the number as visited by making it negative
        return -1                 # This line is never reached since we are guaranteed a duplicate

    # Fast & Slow pointers. T: O(n), S: O(1)
    def findDuplicate_fast_slow_pointers(self, nums: List[int]) -> int:
        # Find the intersection point of the slow and fast pointers
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Get the beginning of the cycle
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow