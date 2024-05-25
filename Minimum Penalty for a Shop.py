def bestClosingTime( customers: str) -> int:
    countY = 0
    for i in customers:
        if i =='Y':
            countY += 1

    countN = 0
    loss = (countN * 1) + (countY * 1)
    index = 0

    for i in range(len(customers)):
    
        if customers[i] == 'Y':
            countY -= 1
        else:
            countN += 1
        
        carryLoss = (countN * 1) + (countY * 1)

        if carryLoss < loss:
            loss = carryLoss
            index = i+1

    return index

print(bestClosingTime(customers = "YYNY"))