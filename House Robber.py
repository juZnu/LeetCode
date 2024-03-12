def rob(nums):
    amount = [-1 for i in nums]
    def rob2(nums,i):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        elif amount[i] != -1:
            return amount[i]
        amount[i] = nums[0]+rob2(nums[2:],i+2)    
        amount[i+1] = rob2(nums[1:],i+1)
        return max(amount[i],amount[i+1])
    return rob2(nums,0)
print(rob(nums = [2,7,9,3,1]))