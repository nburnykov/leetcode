from typing import List, Optional

from LINKED_STRUCTURES.next_right_pointer.app import Node


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(nums: List[int]) -> ListNode:
    result = None

    for n in nums[::-1]:
        r = ListNode()
        r.val = n
        r.next = result
        result = r

    return result


def read_linked_list(l: ListNode) -> list:
    if not l:
        return []
    result = [l.val]
    l_p = l.next
    while l_p is not None:
        result.append(l_p.val)
        l_p = l_p.next
    return result


def compose_binary_tree(tree_arr: list) -> Optional[Node]:
    if len(tree_arr) == 0:
        return
    head = Node()
    head.val = tree_arr[0]
    queue = LinkedList()
    queue.insert_last((0, head))

    while len(queue) > 0:  # breadth first search
        index, parent_node = queue.pop_first()
        left_index = index * 2 + 1
        right_index = index * 2 + 2
        if left_index < len(tree_arr) and tree_arr[left_index] is not None:  # array has indexed element
            node = Node()
            node.val = tree_arr[left_index]
            parent_node.left = node
            queue.insert_last((left_index, node))

        if right_index < len(tree_arr) and tree_arr[right_index] is not None:  # array has indexed element
            node = Node()
            node.val = tree_arr[right_index]
            parent_node.right = node
            queue.insert_last((right_index, node))

    return head


def decompose_binary_tree(tree: Optional[Node]) -> list:
    if not tree:
        return []

    queue = LinkedList()
    queue.insert_last(tree)
    result = []
    while len(queue):  # breadth first search
        node = queue.pop_first()  # type: Node
        if node:
            result.append(node.val)
            queue.insert_last(node.left)
            queue.insert_last(node.right)
        else:
            result.append(None)

    while len(result) > 0:  # [1, 2, None, 3, None, None, None] -> [1, 2, None, 3]
        if result[-1] is None:
            result.pop(-1)
        else:
            break

    return result


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