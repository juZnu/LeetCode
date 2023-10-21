from collections import deque
def maxSlidingWindow(nums, k):
    deque_ = deque()
    result = []
    for i in range(len(nums)):
        while deque_ and deque_[-1] <nums[i]:
            deque_.pop()
        deque_.append(nums[i])
        if i >= k-1:
            result.append(deque_[0])
            if nums[i-k+1] == deque_[0]:
                deque_.popleft()
    return result
                
