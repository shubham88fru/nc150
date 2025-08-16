from typing import Optional

""""""""""""""""""""""""""""
-----------------------
OPTIMAL: Using pointers
-----------------------
TC: O(n)
SC: O(1)

------------------------------------
BETTER:
------------------------------------
TC:
SC:

-------------------------------
BRUTE: store in lst and reverse
-------------------------------
TC: O(n)
SC: O(n)

"""""""""""""""""""""""""""

# @link - https://leetcode.com/problems/reverse-nodes-in-k-group/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # return self.suboptimal(head, k)
        return self.optimal(head, k)

    # Based on nc's explanation.
    def optimal(self, head, k):
        dummy = ListNode(-1, head)
        group_prev = dummy

        while True:
            kth = self.get_kth(group_prev, k)

            if not kth:
                break

            group_next = kth.next
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next

    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr

    # 2) This ain't the optimal
    # approach coz it uses extra
    # space.
    def suboptimal(self, head, k):
        lst = []
        curr = head
        while curr:
            lst.append(curr)
            curr = curr.next

        start = 0
        end = k - 1
        batches = len(lst) // k
        i = 0
        while i < batches:
            if i == 0:
                head = lst[end]
            tail = lst[start]
            while start <= end:
                if start != 0:
                    lst[start].next = lst[start - 1]
                else:
                    lst[start].next = None
                start += 1

            i += 1

            if i >= batches:
                break

            end = start + k - 1
            tail.next = lst[end]

        if start < len(lst):
            tail.next = lst[start]
        else:
            tail.next = None

        return head