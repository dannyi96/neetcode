# Leetcode link - https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import *
import heapq

class Solution:
    # Heap based. T: O(n log k), S: O(k)
    def findKthLargest_inbuilt(self, nums, k):
        # This is inbuilt method. Can be done from scratch like earlier problems
        return heapq.nlargest(k, nums)[-1]
    
    def findKthLargest_scratch(self, nums: List[int], k: int) -> int:
        heap = []
        for elem in nums:
            if len(heap) >= k:
                if elem > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, elem)
            else:
                heapq.heappush(heap, elem)

        return heap[0]