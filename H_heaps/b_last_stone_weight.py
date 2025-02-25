# Leetcode link - https://leetcode.com/problems/last-stone-weight/

from typing import *
import heapq

class Solution:
    # Heap based. T: O(n logn), S: O(n)
    def lastStoneWeight_heap(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # for max heap
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])