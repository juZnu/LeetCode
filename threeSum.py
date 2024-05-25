class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        prevSet = set()
        def twoSum(array,target):
            carry = []
            forward = 0
            backward = len(array) - 1
            while forward < backward:
                if array[forward] + array[backward] < target:
                    forward += 1
                elif array[forward] + array[backward] > target:
                    backward -= 1
                elif array[forward] + array[backward] == target:
                    carry.append([array[forward],array[backward]])
                    while forward < backward and array[forward+1] == array[forward] :
                        forward += 1
                    while forward < backward and array[backward-1] == array[backward]:
                        backward -= 1
                    forward += 1
                    backward -= 1
            return carry
        for i in range(len(nums)):
            if nums[i] not in prevSet:
                for ele in twoSum(nums[i+1:],-1 * nums[i]):
                    result.append(ele+[nums[i]])
                prevSet.add(nums[i])
        return result


