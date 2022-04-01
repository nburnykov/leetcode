from typing import Optional


class LLItem:
    def __init__(self, value: Optional[object] = None, prev: Optional[object] = None, next: Optional[object] = None):
        self.prev = prev
        self.next = next
        self.value = value


class LinkedList:
    def __init__(self):
        self.head: Optional[LLItem] = None
        self.tail: Optional[LLItem] = None
        self.length = 0

    def insert_last(self, value: object):
        v = LLItem(value)
        if not self.head:
            self.head = v
            self.tail = v
        else:
            t = self.tail
            t.next = v
            v.prev = t
            self.tail = v
        self.length += 1

    def insert_first(self, value: object):
        v = LLItem(value)
        if not self.head:
            self.head = v
            self.tail = v
        else:
            h = self.head
            self.head = v
            v.next = h
        self.length += 1

    def pop_first(self) -> Optional[object]:
        if not self.head:
            return

        h = self.head
        self.head = h.next
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return h.value

    def pop_last(self) -> Optional[object]:
        if not self.tail:
            return

        t = self.tail
        self.tail = t.prev
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return t.value

    def __len__(self):
        return self.length