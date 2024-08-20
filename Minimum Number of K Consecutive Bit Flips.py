class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        res = 0
        queue = collections.deque()

        for i in range(len(nums)):
            # Remove elements from the queue that are out of the current window of size k
            if queue and queue[0] == i - k:
                queue.popleft()
            
            # If the current element needs to be flipped
            if len(queue) % 2 == nums[i]:
                if i + k > len(nums):  # If we can't flip the next k elements, return -1
                    return -1
                res += 1
                queue.append(i)

        return res

        