def moveZeroes(nums) -> None:
    l = 0
    r = 0
    while r < len(nums):
        if nums[r]:
            nums[r],nums[l] = nums[l],nums[r]
            l += 1
        r += 1
        
            
            
            
print(moveZeroes(nums = [1,0,1]))
print(moveZeroes(nums = [0,1,0,3,12]))