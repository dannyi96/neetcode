# Leetcode link - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import *

class Solution:
    # Normal binary search. T: O(log n), S: O(1)
    def findMin_normal_binary_search(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # l to r is sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            # typical binary search
            m = (l + r) // 2
            res = min(res, nums[m])
            # check if we are in first half
            # [ 3, 4, 5, 1, 2]
            # [ 1, 2, 3, 4, 5]
            # using the inclusive condition is better as lesser handling ( in case m==l )
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

    # Bound based binary search. T: O(log n), S: O(1)
    def findMin_bound_binary_search(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]