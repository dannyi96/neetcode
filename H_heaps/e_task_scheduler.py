# Leetcode link - https://leetcode.com/problems/task-scheduler/description/
# Input: tasks = ["X","X","Y","Y"], n = 2
# Return the minimum number of CPU cycles required to complete all tasks.
# Output: 5
# Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

from typing import *
import heapq
from collections import deque, Counter

class Solution:
    # Heap based. T: O(m) where m is number of tasks, S: O(1) [at most 26 characters]
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time