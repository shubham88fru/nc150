# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# @link - https://neetcode.io/problems/copy-linked-list-with-random-pointer
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return self.solve(head)

    # Note that there is a more clever soln
    # than this. Although, TC wise, I don't think
    # its better, than this soln, but SC wise, it's
    # better. That soln was shown by strvr and is
    # available in `dsalgo`. It's indeed a very
    # clever soln.
    def solve(self, head):
        if head is None:
            return None

        mp = {}
        curr = head

        while curr is not None:
            newNode = None
            if curr in mp:
                newNode = mp[curr]
            else:
                newNode = Node(curr.val)
                mp[curr] = newNode

            if curr.next is None:
                newNode.next = None;
            elif curr.next in mp:
                newNode.next = mp[curr.next]
            else:
                newNode.next = Node(curr.next.val)
                mp[curr.next] = newNode.next

            if curr.random is None:
                newNode.random = None
            elif curr.random in mp:
                newNode.random = mp[curr.random]
            else:
                newNode.random = Node(curr.random.val)
                mp[curr.random] = newNode.random

            curr = curr.next

        return mp[head]