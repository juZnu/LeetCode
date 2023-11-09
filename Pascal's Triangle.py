def generate( numRows):
    result =[]
    for i in range(numRows):
        array = [1] if i else []
        for j in range(i-1):
            array.append(result[-1][j] + result[-1][j+1])
        array.append(1)
        result.append(array)
    return result