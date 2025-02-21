class DLL:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None


# @link - https://neetcode.io/problems/lru-cache
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # DLL with setup of head
        # and tail makes life
        # much easier. TRUST ME.
        self.head = DLL(-1, -1)
        self.tail = DLL(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.moveToFront(self.cache.get(key))
        return self.cache.get(key).v

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.get(key).v = value
            self.moveToFront(self.cache.get(key))
            return
        elif len(self.cache) == self.capacity:
            lru = self.removeLRU()
            del self.cache[lru]

        newNode = DLL(key, value)
        self.cache[key] = newNode
        self.moveToFront(newNode)

    def removeLRU(self):
        last_node = self.tail.prev
        prev = last_node.prev
        prev.next = self.tail
        self.tail.prev = prev

        last_node.prev = None
        last_node.next = None
        return last_node.k

    def moveToFront(self, node):
        prev = node.prev
        nxt = node.next

        if prev is not None:
            prev.next = node.next

        if nxt is not None:
            nxt.prev = prev

        old_head = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = old_head
        old_head.prev = node