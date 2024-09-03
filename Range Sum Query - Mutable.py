class NumArray:
    def getLSB(self, n):
        return n & -n

    def __init__(self, nums: List[int]):
        self.nums = [0] + nums
        for index in range(1, len(nums)):
            j = index + self.getLSB(index)
            if j < len(self.nums):
                self.nums[j] += self.nums[index]

    def update(self, index: int, val: int) -> None:
        index += 1
        val -= self.getPrefixSum(index) - self.getPrefixSum(index-1)
        while index < len(self.nums):
            self.nums[index] += val
            index += self.getLSB(index)
        
    def getPrefixSum(self,index):
        i = self.getLSB(index)
        returnSum = 0

        while i :
            returnSum += self.nums[index]
            index -= i 
            i = self.getLSB(index)

        return returnSum

    def sumRange(self, left: int, right: int) -> int:
        return self.getPrefixSum(right+1) - self.getPrefixSum(left)