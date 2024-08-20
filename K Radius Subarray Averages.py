class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        j = (2*k)
        if len(nums) < j: return [-1]*len(nums)
        
        carrySum = sum(nums[:j])
        res = []

        for i in range(k):
            res.append(-1)
        
        for i in range(j,len(nums)):
            carrySum += nums[i]
            res.append(carrySum//(j+1))
            carrySum -= nums[i-j]

        for i in range(k):
            res.append(-1)
        
        return res
