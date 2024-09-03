class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = nums[0] <= nums[-1]

        prev= nums[0]
        for ele in nums[1:]:
            if (prev > ele) and inc:
                return False
            elif (prev < ele) and  not inc:
                return False
            prev = ele
        
        return True
        