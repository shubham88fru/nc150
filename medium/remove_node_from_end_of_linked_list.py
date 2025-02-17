# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional

# @link - https://neetcode.io/problems/remove-node-from-end-of-linked-list
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = head

        while n > 0:
            p2 = p2.next
            n -= 1

        if p2 is None:
            return head.next

        while p2.next is not None:
            p2 = p2.next
            p1 = p1.next

        nxt = p1.next.next
        p1.next.next = None
        p1.next = nxt

        return head