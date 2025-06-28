""""""""""""""""""""""""""""
------------------------------------
OPTIMAL: Simple linkedlist operation
------------------------------------
TC: O(n)
SC: O(1)

------------------------------------
BETTER:
------------------------------------
TC:
SC:

----------------------------------------------
BRUTE:
----------------------------------------------
TC:
SC:

"""""""""""""""""""""""""""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional

# @link - https://neetcode.io/problems/add-two-numbers
class Solution:
    """
      Strvr and Nc showed a soln which has
      the exact same appraoch and TC but is a
      bit cleaner coz it uses lesser number of loops.
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.sumLL(l1, l2)

    def sumLL(self, l1, l2):
        curr1 = l1
        curr2 = l2

        dummy = ListNode(-1)
        ans = dummy

        carry = 0
        while curr1 is not None and curr2 is not None:
            sm = curr1.val + curr2.val + carry
            if sm >= 10:
                carry = 1
                sm %= 10
            else:
                carry = 0

            ans.next = ListNode(sm)
            ans = ans.next
            curr1 = curr1.next
            curr2 = curr2.next

        while curr1 is not None:
            sm = curr1.val + carry
            if sm >= 10:
                carry = 1
                sm %= 10
            else:
                carry = 0

            ans.next = ListNode(sm)
            ans = ans.next
            curr1 = curr1.next

        while curr2 is not None:
            sm = curr2.val + carry
            if sm >= 10:
                carry = 1
                sm %= 10
            else:
                carry = 0

            ans.next = ListNode(sm)
            ans = ans.next
            curr2 = curr2.next

        if carry != 0:
            ans.next = ListNode(carry)

        return dummy.next
