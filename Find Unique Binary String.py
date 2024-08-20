class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = [""]
        length = len(nums[0])
        nums = set(nums)

        def helper(i,carry):
            if res[0]: return

            if i == length:
                if carry not in nums:res[0] = carry
                return 
            
            helper(i+1,carry+'0')
            helper(i+1,carry+'1')

        helper(0,"")
        return res[0]
            
        