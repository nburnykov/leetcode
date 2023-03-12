import heapq
from typing import List


def medianSlidingWindow(nums: List[int], k: int) -> List[float]:
    def clean_heap(heap: list, gone_index: int):
        while len(heap) > 0 and heap[0][1] <= gone_index:
            heapq.heappop(heap)

    def swap_element(heap_from: list, heap_to: list):
        if len(heap_from) == 0:
            return
        value, index = heapq.heappop(heap_from)
        heapq.heappush(heap_to, (-value, index))

    def get_median(heap_min, heap_max, k):
        if k % 2:
            return heap_max[0][0]
        else:
            return round((-heap_min[0][0] + heap_max[0][0]) / 2, 5)

    # init heaps
    heap_min, heap_max = [], []
    for i in range(k):
        heapq.heappush(heap_max, (nums[i], i))
    heapq.heapify(heap_max)
    for _ in range(k // 2):
        swap_element(heap_max, heap_min)

    result = [get_median(heap_min, heap_max, k)]

    for i in range(k, len(nums)):
        index_in, index_out = i, i - k

        if nums[index_in] < heap_max[0][0]:
            heapq.heappush(heap_min, (-nums[index_in], index_in))
            if nums[index_out] >= heap_max[0][0]:
                swap_element(heap_min, heap_max)
        else:
            heapq.heappush(heap_max, (nums[index_in], index_in))
            if nums[index_out] <= heap_max[0][0]:
                swap_element(heap_max, heap_min)

        clean_heap(heap_min, index_out)
        clean_heap(heap_max, index_out)

        result.append(get_median(heap_min, heap_max, k))

    return result



