# Leetcode link - https://leetcode.com/problems/top-k-frequent-elements/
from typing import *
import heapq

class Solution:
    # Sorting based. T: O(nlogn), S: O(n)
    def topKFrequent_frequency_sorting(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Transfer from map to array ( to enable sorting )
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        # sort
        arr.sort()
        
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
    
    # Heap based. T: O(nlogk), S: O(n+k)
    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Maintain a k node max heap
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
    
    # Bucket sort based. T: O(n), S: O(n)
    def topKFrequent_bucketsort(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq = [[] for i in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res