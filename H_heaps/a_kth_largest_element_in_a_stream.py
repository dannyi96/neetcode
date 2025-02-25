# Leetcode link - https://leetcode.com/problems/kth-largest-element-in-a-stream/

from typing import *
import heapq

'''
Main Idea:
    - The min heap always stores exactly k largest elements encountered so far.
    - The smallest element in the heap (heap[0]) is the kth largest element.
'''

# T: O(log k) for each add, S: O(k)
class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]