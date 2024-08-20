import collections
from typing import List


def longestSubarray(nums: List[int], limit: int) -> int:
    minQueue = collections.deque()
    maxQueue = collections.deque()

    l = 0
    res = 0

    for r in range(len(nums)):
        while minQueue and minQueue[-1] > nums[r]:
            minQueue.pop()
        minQueue.append(nums[r])

        while maxQueue and maxQueue[-1] < nums[r]:
            maxQueue.pop()
        maxQueue.append(nums[r])

        while l < r and  maxQueue[0]-minQueue[0] > limit:
            if nums[l] == minQueue[0]: minQueue.popleft()
            if nums[l] == maxQueue[0]: maxQueue.popleft()
            l += 1

        res = max(res,r-l+1)
    
    return res
    
print(longestSubarray(nums = [8,2,4,7], limit = 4))