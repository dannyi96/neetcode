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
    