###########################################################################################
# leetcode problem  https://leetcode.com/problems/bus-routes/
###########################################################################################
from collections import deque
from typing import List


def numBusesToDestination(routes: List[List[int]], source: int, target: int) -> int:
    result = float("inf")
    if source == target:
        return 0

    buses_dict = {_id: set(route) for _id, route in enumerate(routes)}
    stops_dict = dict()
    for _id, route in buses_dict.items():
        for stop in route:
            stops_dict.setdefault(stop, set()).add(_id)

    # BFS
    q = deque([(route_id, 1) for route_id in stops_dict.get(source, [])])
    buses_passed = set()
    stops_checked = set()
    while len(q) > 0:
        bus_id, num = q.pop()
        buses_passed.add(bus_id)

        stops = buses_dict.get(bus_id, set())
        stops -= stops_checked

        if target in stops:
            result = min(result, num)
            continue

        next_buses = set()
        for stop in stops:
            next_buses.update(stops_dict.get(stop, set()))
        next_buses -= buses_passed

        stops_checked.update(stops)

        for nr in next_buses:
            q.append((nr, num + 1))

    return -1 if result==float("inf") else result


