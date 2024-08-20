class Solution(object):
    def sortColors(self, nums):
        start = 0
        end = len(nums)-1
        i = 0
        while i <= end:
            while i >= start and nums[i]==0:
                nums[i],nums[start] = nums[start],nums[i]
                start += 1
            while nums[i] == 2 and i <= end:
                nums[i],nums[end] = nums[end],nums[i]
                end -= 1
            while i >= start and nums[i]==0:
                nums[i],nums[start] = nums[start],nums[i]
                start += 1
            i += 1
        return nums


        