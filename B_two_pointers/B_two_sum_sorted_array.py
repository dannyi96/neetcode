# Leetcode link - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from collections import defaultdict
from typing import *

class Solution:
    # Brute force -> T: O(n^2), S: O(1)
    def twoSum_bruteforce(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1] # output is expected in 1 index format
        return []
    
    # HashMap One Pass -> T: O(n), S: O(n)
    def twoSum_hashmap(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for index, num in enumerate(numbers):
            complement = target - num
            if mp[complement]:
                return [mp[complement], index + 1] # output is expected in 1 index format
            mp[num] = index + 1
        return []
    
    # Note - above 2 solutions would work for even non sorted scenario.
    # We need to come up with better solutions for sorted usecases
    
    # Binary Search based -> T: O(nlogn), S: O(1)
    def twoSum_binary_search(self, numbers: List[int], target: int) -> List[int]:
        # Basic idea - for each elem in numbers, do a binary search for its complement
        def binary_search(l: int, r: int, goal: int) -> int:
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == goal:
                    return mid
                elif numbers[mid] < goal:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        n = len(numbers)
        for index, elem in enumerate(numbers):
            complement = target - elem
            search_index = binary_search(index+1, n-1, complement)
            if search_index != -1:
                return [index + 1, search_index + 1] # output is expected in 1 index format
        return []
    
    # Two pointer based -> T: O(n), S: O(1)
    def twoSum_two_pointer(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum == target:
                return [l+1, r+1] # output is expected in 1 index format
            elif curSum < target:
                l += 1
            else:
                r -= 1
        return []