class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = [0]
        
        def helper(i,XOR):
            if i == len(nums):
                res[0] += XOR
                return
            helper(i+1,XOR)
            XOR ^= nums[i]
            helper(i+1,XOR)
        helper(0,0)
        return res[0]
        