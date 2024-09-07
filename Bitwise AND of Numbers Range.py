
def rangeBitwiseAnd( left: int, right: int) -> int:
    res = right
    while res > left:
        res = res &(res-1)
        
    return res

print(rangeBitwiseAnd(4,9))
        