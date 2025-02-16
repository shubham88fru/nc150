# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


# @link - https://neetcode.io/problems/reorder-linked-list
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        right = self.reverse(self.half(head))
        left = head

        curr1 = left
        curr2 = right

        while curr1 is not None and curr2 is not None:
            nxt1 = curr1.next
            curr1.next = curr2
            curr1 = nxt1

            nxt2 = curr2.next
            curr2.next = nxt1
            curr2 = nxt2

    def reverse(self, head):
        if head is None:
            return None

        prev = None
        curr = head
        nxt = None

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def half(self, head):
        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None
        return right


