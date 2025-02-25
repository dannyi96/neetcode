# Leetcode link - https://leetcode.com/problems/remove-nth-node-from-end-of-list/
from typing import *

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Optimal. T: O(n), S: O(1)
    def removeNthFromEnd_optimal(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Move right pointer n steps forward
        while n > 0:
            right = right.next
            n -= 1

        # Then move both till right reaches end
        while right:
            left = left.next
            right = right.next

        # update for the removal
        left.next = left.next.next
        return dummy.next