# Definition for singly-linked list.
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional

# @link - https://neetcode.io/problems/merge-k-sorted-linked-lists
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.solve(lists)

    def solve(self, lists):
        return self.approach1(lists)

    def approach1(self, lists):
        n = len(lists)
        min_heap = []

        counter = 0  # No idea why this is needed, but doesn't work without this.
        for node in lists:
            if node:
                heapq.heappush(min_heap, (node.val, counter, node))
                counter += 1

        dummy = ListNode(-1)
        ans = dummy
        while len(min_heap) > 0:
            val, counter, node = heapq.heappop(min_heap)
            ans.next = node
            ans = ans.next

            if node != None and node.next != None:
                heapq.heappush(min_heap, (node.next.val, counter, node.next))
                counter += 1

        return dummy.next

    # Kind of brute forceish.
    def approach2(self, lists):
        n = len(lists)
        if n == 0:
            return None

        merged = lists[0]
        for i in range(1, n):
            merged = self.merge_two_sorted_lists(merged, lists[i])

        return merged

    def merge_two_sorted_lists(self, list1, list2):
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        dummy = ListNode(-1)
        prev = dummy
        curr1 = list1
        curr2 = list2

        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                nxt = curr1.next
                curr1.next = curr2
                prev.next = curr1
                prev = curr1
                curr1 = nxt
            else:
                nxt = curr2.next
                curr2.next = curr1
                prev.next = curr2
                prev = curr2
                curr2 = nxt

        return dummy.next