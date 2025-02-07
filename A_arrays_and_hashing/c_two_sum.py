# Leetcode link - https://leetcode.com/problems/two-sum/
from typing import *

class Solution:
    # Brute force -> T: O(n^2), S: O(1)
    def twoSum_bruteforce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    # Sorting & 2 pointers -> T: O(nlogn), S: O(n)
    def twoSum_sorting(self, nums: List[int], target: int) -> List[int]:
        # This problems wants the indices as the output. Hence we need to maintain indices
        A = []
        for index, num in enumerate(nums):
            A.append((num, index))
        A.sort()
        
        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [
                    min(A[i][1], A[j][1]), # Note - this min & max for indices is done for -ve number cases
                    max(A[i][1], A[j][1])  # eg - nums=[-1,-2,-3,-4,-5], target=-8
                ]
            elif cur < target:
                i += 1
            else: # cur > target
                j -= 1
        
        return []                
    
    # HashMap One Pass -> T: O(n), S: O(n)
    def twoSum_hashmap(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index
        for index, num in enumerate(nums):
            complement = target - num
            if complement in prevMap:
                return [prevMap[complement], index]
            prevMap[num] = index

        return []