class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if divisor == 0:
            raise 2**31
        if dividend == 0:
            return 0
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  
            
        negative = (dividend < 0) ^ (divisor < 0)


        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1

            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1

            dividend -= temp_divisor
            result += multiple

        if negative:
            result = -result

        return result
        