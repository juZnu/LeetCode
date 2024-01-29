def leastBricks( wall):
    result = len(wall)
    sum_ = sum(wall[0])
    carryDict = dict()
    for ele in wall:
        carrySum = 0
        for innerEle in ele:
            carrySum += innerEle
            carryDict[carrySum] = carryDict.get(carrySum,len(wall)) - 1
            result = min(result,carryDict[carrySum] if  carrySum != sum_ else float('Inf'))
    return result
