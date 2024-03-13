from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        carrySum = sum(arr[:k])
        result = 1 if carrySum / k >= threshold else 0
        for index in range(k,len(arr)):
            carrySum += arr[index] - arr[index-k]
            result += 1 if carrySum / k >= threshold else 0
        return result

        