def majorityElement( nums):
    nums.sort()
    i = len(nums)//2
    return nums[i]
