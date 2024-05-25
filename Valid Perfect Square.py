def isPerfectSquare( num: int) -> bool:
    
    l = 1
    r = num-1
    while l < r:
        mid =  (l+r) // 2
        if num == mid * mid:
            return True
        elif num > mid * mid:
            l = mid + 1
        elif num < mid * mid:
            r = mid - 1
    return False

print(isPerfectSquare(9))