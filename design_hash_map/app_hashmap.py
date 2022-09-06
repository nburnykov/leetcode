###########################################################################################
# leetcode problem  https://leetcode.com/problems/design-hashmap/
###########################################################################################
from typing import Optional


class Node:
    def __init__(self,
                 key: Optional[int],
                 val: Optional[int],
                 prev: Optional['Node'] = None,
                 next: Optional['Node'] = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.last = self.head

    def find(self, key: int) -> Optional[Node]:
        node = self.head.next
        while node is not None:
            if node.key == key:
                return node
            node = node.next

    def append(self, key: int, val: int):
        node = Node(key, val)
        node.prev = self.last
        node.prev.next = node
        self.last = node

    def remove(self, key: int) -> Optional[int]:
        node = self.find(key)

        if node is None:
            return

        next_node = node.next
        prev_node = node.prev
        if next_node is not None:
            next_node.prev = prev_node
            prev_node.next = next_node
        else:
            prev_node.next = None
            self.last = prev_node

        return node.val

    def insert(self, key: int, val: int):
        candidate = self.find(key)
        if candidate is not None:
            candidate.val = val
        else:
            self.append(key, val)


class MyHashMap:

    def __init__(self):
        self.size = 10037  # the prime number closest to the number of defined search operations (10 ** 4)
        self.data = [None for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        chunk = key % self.size
        if self.data[chunk] is None:
            self.data[chunk] = LinkedList()
        self.data[chunk].insert(key, value)

    def get(self, key: int) -> int:
        chunk = key % self.size
        if self.data[chunk] is None:
            return -1
        node = self.data[chunk].find(key)
        if node is not None:
            return node.val
        else:
            return -1

    def remove(self, key: int) -> None:
        chunk = key % self.size
        if self.data[chunk] is None:
            return
        self.data[chunk].remove(key)
