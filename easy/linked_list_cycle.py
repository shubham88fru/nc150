""""""""""""""""""""""""""""
-----------------------------------------------------------
OPTIMAL: Floyds' Tortoise and Hare - fast and slow pointers
-----------------------------------------------------------
TC: O(n)
SC: O(1)

------------------------------------
BETTER:
------------------------------------
TC:
SC:

-----------
BRUTE: Sets
-----------
TC: O(n)
SC: O(n)

"""""""""""""""""""""""""""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional

# @link - https://neetcode.io/problems/linked-list-cycle-detection
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # return self.better(head)
        return self.optimal(head)

    # check nc or strvr for proof
    # on why the algo will always
    # work.
    def optimal(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    def better(self, head):
        st = set()
        curr = head
        while curr is not None:
            if curr in st:
                return True
            st.add(curr)
            curr = curr.next
        return False
