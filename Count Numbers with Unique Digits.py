class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        i = 1
        res = 1
        while i <= n:
            carry = 9
            num = 9
            for _ in range(i-1):
                carry *= num
                num -= 1
            res += carry
            i += 1
        return res