# Leetcode link - https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import *
from __future__ import annotations

class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    # HashMap based. T: O(n), S: O(n)
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]