from typing import Optional

""""""""""""""""""""""""""""
-----------------------------
OPTIMAL: 3 pointers Iterative
-----------------------------
TC: O(n)
SC: O(1)

--------------------------
BETTER: Recursive solution
--------------------------
TC: O(n)
SC: O(n)

--------------------------------------------
BRUTE: Use stack. Push to stack and then pop
--------------------------------------------
TC: O(2N)
SC: O(N)

"""""""""""""""""""""""""""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#@link - https://neetcode.io/problems/reverse-a-linked-list
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.iterative(head)
        # return self.recursive(head)

    # Based on strvr's explanation
    def recursive(self, head):
        if head is None or head.next is None:
            return head

        new_head = self.recursive(head.next)
        front = head.next
        front.next = head
        head.next = None
        return new_head

    def iterative(self, head):
        prev = None
        curr = head
        nxt = head

        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev