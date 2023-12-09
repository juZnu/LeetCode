class NumArray(object):

    def __init__(self, nums):
        self.sum = [nums[0]]
        for ele in nums[1:]:
            self.sum.append(self.sum[-1]+ele)

        

    def sumRange(self, i, j):
        if i > 0 and j > 0:
            return self.sum[j] - self.sum[i - 1]
        else:
            return self.sum[i or j]
    


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)