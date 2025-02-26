# Leetcode link - https://leetcode.com/problems/course-schedule-ii/
from typing import *
from collections import deque

class Solution:
    # T: O(V+E), S: O(V+E)
    def findOrder_topological_sort(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        finish, output = 0, []
        while q:
            node = q.popleft()
            output.append(node)
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if finish != numCourses:
            return []
        return output[::-1]