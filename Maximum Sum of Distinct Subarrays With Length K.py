from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sum_, maxSum = 0,0
        hashmap = {}
        for i in range(k):
            hashmap[nums[i]] = hashmap.get(nums[i],0) + 1
            sum_ += nums[i]
        if len(hashmap) == k:  maxSum = sum_
        for i in range(k,len(nums)):
            a,b = nums[i],nums[i-k]
            sum_ += a - b
            hashmap[b] -= 1
            if not hashmap[b]: hashmap.pop(b)
            hashmap[a] = hashmap.get(a,0) + 1
            if len(hashmap) == k: maxSum = max(maxSum,sum_)
        return maxSum

        