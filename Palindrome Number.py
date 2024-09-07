def isPalindrome( x: int) -> bool:
    if x < 0:
        return False
    carry = x
    pal = 0
    while carry: 
        pal *= 10
        pal += carry%10
        carry /= 10
    return pal == x

print(isPalindrome(121))