""""""""""""""""""""""""""""
----------------------
OPTIMAL: Two pointers.
----------------------
TC: O(n)
SC: O(1)

------------------------------------
BETTER:
------------------------------------
TC:
SC:

----------------
BRUTE: Two pass.
----------------
TC: O(2n)
SC: O(1)

"""""""""""""""""""""""""""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional

# @link - https://neetcode.io/problems/remove-node-from-end-of-linked-list
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return self.optimal(head, n)

    # optimal - one pass
    def optimal(self, head, n):
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

    # Brute - 2 pass
    def brute(self, head, n):
        m = 0
        curr = head
        while curr is not None:
            m += 1
            curr = curr.next

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy

        target = head
        i = m - n - 1
        while i >= 0:
            prev = target
            target = target.next
            i -= 1

        prev.next = target.next
        target.next = None

        return dummy.next