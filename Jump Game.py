class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <2: return nums

        index = len(nums)-2
        result = True
        for i in range(len(nums)-2,-1,-1):
            if nums[i] == 0 and result:
                index = i
                result = False
            if not result and (index-i) < nums[i]:
                result = True
        return result

                



        