from typing import Optional

from utils import LinkedList
from app import TreeNode


def compose_binary_tree(tree_arr: list) -> Optional[TreeNode]:
    if len(tree_arr) == 0:
        return
    head = TreeNode()
    head.val = tree_arr[0]
    queue = LinkedList()
    queue.insert_last((0, head))

    while len(queue) > 0:  # breadth first search
        index, parent_node = queue.pop_first()
        left_index = index * 2 + 1
        right_index = index * 2 + 2
        if left_index < len(tree_arr) and tree_arr[left_index] is not None:  # array has indexed element
            node = TreeNode()
            node.val = tree_arr[left_index]
            parent_node.left = node
            queue.insert_last((left_index, node))

        if right_index < len(tree_arr) and tree_arr[right_index] is not None:  # array has indexed element
            node = TreeNode()
            node.val = tree_arr[right_index]
            parent_node.right = node
            queue.insert_last((right_index, node))

    return head


def decompose_binary_tree(tree: Optional[TreeNode]) -> list:
    if not tree:
        return []

    queue = LinkedList()
    queue.insert_last(tree)
    result = []
    while len(queue):  # breadth first search
        node = queue.pop_first()  # type: TreeNode
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