from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#@link - https://neetcode.io/problems/reverse-a-linked-list
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = None
        nxt = head

        while nxt != None:
            curr = nxt
            nxt = nxt.next
            curr.next = prev
            prev = curr

        return prev