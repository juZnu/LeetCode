class Solution(object):
    
    def threeSum(self, nums):
        def twoSum(nums,target):
            l = 0
            r = len(nums)-1

            while l < r:
                carrySum = nums[l] + nums[r]
                if carrySum > target:
                    r -= 1
                elif carrySum < target:
                    l += 1
                else:

                    res.append([-target,nums[l],nums[r]])

                    while l < r and nums[l] == nums[l+1]:
                        l += 1

                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    
                    l += 1
                    r -= 1
                    
            return 

        nums.sort()
        res = []

        for i,value in enumerate(nums[:-1]):
            if value == nums[i-1] and i != 0:
                continue
            twoSum(nums[i+1:],(-1)*value)
            
        return res