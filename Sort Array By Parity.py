class Solution(object):
    def sortArrayByParity(self, nums):
        oddHeap = []
        evenHeap = []
        for num in nums:
            heapq.heappush(oddHeap if num%2 else evenHeap,num)
        return evenHeap+oddHeap