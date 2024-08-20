class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l+1 < r:
            while l<r and nums[l] == nums[l+1]:l += 1
            
            while l<r and ((nums[r] == nums[r-1]) or (nums[l] == nums[r])):r -= 1
            
            mid = l + (r-l)//2

            if nums[l] < nums[r]:return nums[l]

            if nums[mid] < nums[r]:r = mid
            elif nums[mid] > nums[l]:l = mid
                
        return min(nums[l],nums[r])