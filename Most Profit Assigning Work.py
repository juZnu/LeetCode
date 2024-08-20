def maxProfitAssignment( difficulty, profit, worker):
    difficultyProfit = sorted(zip(profit,difficulty),reverse=True)
    worker.sort()
    i = len(worker)-1
    previ = len(worker)-1
    profit = 0
    for prof,diff in difficultyProfit:
        while i>=0 and worker[i] >= diff:
            i -= 1
        profit += (previ-i) * prof
        previ = i
        if i <0:break
    return profit

print(maxProfitAssignment(difficulty = [5,50,92,21,24,70,17,63,30,53], profit = [68,100,3,99,56,43,26,93,55,25], worker = [96,3,55,30,11,58,68,36,26,1]))