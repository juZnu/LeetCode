from typing import List


def getSumAbsoluteDifferences( nums: List[int]) -> List[int]:
        carrysum = sum(nums)
        backsum = 0
        result = []
        n = len(nums)
        for i in range(n):
            backsum += nums[i]
            carrysum -= nums[i]
            result.append((((i+1)*nums[i]) - backsum) + (carrysum - ((n-i-1)* nums[i])))
        return result