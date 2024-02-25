class Solution(object):
    def plusOne(self, digits):
        carry = 1
        for index in range(-1, -1 * (len(digits)+1),-1):
            div,mod = divmod(carry+digits[index],10)
            print(div,mod)
            digits[index] =mod
            carry = div
        return digits if not carry else [carry]+digits
        