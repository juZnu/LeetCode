def gridGame(grid):
    topbackSum,topFrontSum = 0,sum(grid[0])
    bottomFrontSum, bottombackSum = sum(grid[1]),0
    maxValue  = 0
    result = float('inf')
    for index in range(len(grid[0])):
        topbackSum += grid[0][index]
        topFrontSum -= grid[0][index]
        if result > max(topFrontSum, bottombackSum):
            maxValue = topbackSum + bottomFrontSum
            result = max(topFrontSum, bottombackSum)
        bottombackSum += grid[1][index]
        bottomFrontSum -= grid[1][index]
    return result
