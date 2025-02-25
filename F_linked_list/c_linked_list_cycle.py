# Leetcode link - https://leetcode.com/problems/linked-list-cycle/
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Hashset based. T: O(n), S: O(n)
    def hasCycle_hashset(self, head: Optional[ListNode]) -> bool:
        seen = set()
        cur = head
        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False

    # Fast & Slow pointers. T: O(n), S: O(1)
    def hasCycle_fast_slow_pointers(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False