# https://leetcode.com/problems/course-schedule-ii
from typing import List


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    Topological order - DFS postorder - add value to an order list only when all child nodes are already added
    """
    prerequisite_map = dict()
    for course_num, prerequisite_num in prerequisites:
        prerequisite_map.setdefault(prerequisite_num, set()).add(course_num)

    for i in range(numCourses):
        if i not in prerequisite_map:
            prerequisite_map[i] = set()

    seen = set()
    result = []
    while len(nodes_left := prerequisite_map.keys() - seen) > 0:
        stack = [nodes_left.pop()]
        visited = set()  # keep visited nodes in current dfs to detect cycles
        while len(stack) > 0:
            course_id = stack[-1]
            visited.add(course_id)
            candidates = prerequisite_map[course_id] - seen

            if prerequisite_map[course_id] & visited:
                return []  # it means that we found visited node in the next variants
            seen.add(course_id)

            if len(candidates) > 0:
                stack.append(candidates.pop())
                continue

            result.append(course_id)
            stack.pop(-1)
            visited.discard(course_id)

    return result[::-1]


