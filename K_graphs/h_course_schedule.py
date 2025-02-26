# Leetcode link - https://leetcode.com/problems/course-schedule/
from typing import *
from collections import deque

class Solution:
    # Cycle detection based. T: O(V+E), S: O(V+E)
    '''
    Time Complexity: O(V + E)
        Building the adjacency list (preMap):
            preMap = {i: [] for i in range(numCourses)}
        runs in O(V) because it initializes an empty list for each course.

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        processes E prerequisite pairs, taking O(E).

        DFS Traversal (dfs function):

        Each node (course) is visited once in the worst case.
        Each edge (prerequisite dependency) is also traversed once in total.
        The worst-case scenario occurs when all courses are connected in a way that the algorithm needs to traverse every course and every prerequisite, leading to O(V + E).
        
    Space Complexity: O(V + E)
        Adjacency List Storage (preMap):
            We store each course and its list of prerequisites. The total size of this adjacency list is O(V + E).
        Visiting Set (visiting):
            In the worst case, this set can store all courses, so it takes O(V) space.
        Recursive Call Stack (DFS):
            In the worst case (a single long prerequisite chain), the recursion depth can reach O(V).
    '''
    def canFinish_cycle_detection(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

    # T: O(V+E), S: O(V+E)
    def canFinish_topological_sort(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                
        return finish == numCourses