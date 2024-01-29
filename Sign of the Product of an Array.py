def arraySign( nums):
    result = 1
    for ele in nums:
        if ele <0:
            result *= -1
        elif ele == 0:
            return 0
    return result