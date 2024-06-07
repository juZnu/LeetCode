from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        
        def encrypt(n):
            n = str(n)
            maxele = max(n)
            return int(maxele*len(n))

        res = 0
        for n in nums:
            res += encrypt(n)

        return res