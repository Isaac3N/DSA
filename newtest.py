# from collections import defaultdict


# def topKFrequent(nums, k):
#     if len(nums) < 2:
#         return nums[0]

#     frequency_map = defaultdict(list)

#     for i in nums:
#         sorted_i = sorted(i)
#         frequency_map[sorted_i].append(i)

#     return frequency_map


# nums = [4, 2, 2, 3, 3, 3, 4, 4, 5, 5]
# k = 2
# result = topKFrequent(nums, k)
# print(result)

import heapq

minHeap = []

heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

while len(minHeap):
    print(heapq.heappop(minHeap))
