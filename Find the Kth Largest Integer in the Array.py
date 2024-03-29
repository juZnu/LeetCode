import heapq
from typing import List


def kthLargestNumber(nums: List[str], k: int) -> str:
    nums = [int(ele) for ele in nums]
    heapq.heapify(nums)
    for _ in range(len(nums)-k):
        heapq.heappop(nums)
    return str(heapq.heappop(nums))

print(kthLargestNumber(nums = ["3","6","7","10"], k = 4))