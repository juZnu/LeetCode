def numberOfMatches( n: int) -> int:
        carry = 0
        result  = 0
        while n != 1:
            carry = 1 if n%2 else 0
            n //= 2
            result += n
            n += carry
        return result