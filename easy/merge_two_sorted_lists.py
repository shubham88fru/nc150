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
    def optimal(self, list1, list2):
        if list1 == None:
            return list2

        if list2 == None:
            return list1

        if list2.val < list1.val:
            temp = list1
            list1 = list2
            list2 = temp

        curr1 = list1
        curr2 = list2
        prev = ListNode(-1)
        while curr1 != None and curr2 != None:
            if curr1.val <= curr2.val:
                prev.next = curr1
                prev = curr1
                nxt = curr1.next
                curr1.next = curr2
                curr1 = nxt
            else:
                prev.next = curr2
                prev = curr2
                nxt = curr2.next
                curr2.next = curr1
                curr2 = nxt

        return list1

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

        # while curr1 != None:
        #     curr3.next = ListNode(curr1.val)
        #     curr1 = curr1.next
        #     curr3 = curr3.next
        if curr1 != None:
            curr3.next = curr1

        # while curr2 != None:
        #     curr3.next = ListNode(curr2.val)
        #     curr2 = curr2.next
        #     curr3 = curr3.next
        if curr2 != None:
            curr3.next = curr2

        return dummy.next
