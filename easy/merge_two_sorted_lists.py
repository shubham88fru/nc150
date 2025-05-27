""""""""""""""""""""""""""""
-----------------------
OPTIMAL: In place merge
-----------------------
TC: O(m+n)
SC: O(1)

------------------------------------------------
BETTER: Merge two sorted list using a third list
------------------------------------------------
TC: O(m+n)
SC: O(m+n)

-----------------------------------------------------------------
BRUTE: Put the lists in a common list and sort the list then link
-----------------------------------------------------------------
TC: O(n + m + (m+n)log(m+n) + (m+n))
SC: O(m+n)

"""""""""""""""""""""""""""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @link - https://neetcode.io/problems/merge-two-sorted-linked-lists
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # return self.suboptimal(list1, list2)
        return self.optimal(list1, list2)

    # constant space.
    def optimal(self, l1, l2):
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        dummy = ListNode(-1)
        prev = dummy

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                nxt = l1.next
                l1.next = l2
                prev.next = l1
                prev = l1
                l1 = nxt
            else:
                nxt = l2.next
                l2.next = l1
                prev.next = l2
                prev = l2
                l2 = nxt

        return dummy.next

    # extra space for a brand new merged list.
    def suboptimal(self, list1, list2):
        dummy = ListNode(-1)

        curr1 = list1
        curr2 = list2
        curr3 = dummy
        while curr1 != None and curr2 != None:
            if curr1.val <= curr2.val:
                curr3.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                curr3.next = ListNode(curr2.val)
                curr2 = curr2.next

            curr3 = curr3.next

        if curr1 != None:
            curr3.next = curr1

        if curr2 != None:
            curr3.next = curr2

        return dummy.next
