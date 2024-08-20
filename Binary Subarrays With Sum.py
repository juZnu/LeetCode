class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        carry = {0:1}
        carrySum = 0
        res = 0
        
        for ele in nums:
            carrySum += ele
            res += carry.get(carrySum - goal,0)
            carry[carrySum] = carry.get(carrySum,0) + 1
        
        return res
        


        

            