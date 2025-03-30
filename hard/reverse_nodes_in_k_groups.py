from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return self.suboptimal(head, k)

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