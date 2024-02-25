class Solution(object):
    def singleNumber(self, nums):
        res = 0
        for ele in nums:
            res = res ^ ele
        return res
        