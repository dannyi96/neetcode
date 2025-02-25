# Leetcode link - https://leetcode.com/problems/reorder-list/
# Input: head = [2,4,6,8,10]
# Output: [2,10,4,8,6]

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Optimal. T: O(n), S: O(1)
    def reorderList_optimal(self, head: Optional[ListNode]) -> None:
        # Get the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Using first half + reversed second half -> merge to final list
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2