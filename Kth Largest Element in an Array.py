class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        carry = []
        for ele in nums:
            if len(carry) == k:
                if carry[0] < ele:
                    heapq.heappop(carry)
                    heapq.heappush(carry,ele)
            else:
                heapq.heappush(carry,ele)
        return heapq.heappop(carry)
        
