def convert(s,numRows):
    result = [[] for _ in range(numRows)]
    i = -1
    ele = 1
    for val in s:
        if i == 0:
            ele  = 1
        elif i == numRows-1:
            ele = -1
        i += ele
        result[i].append(val)
    print(result)
    return ""

print(convert(s = "AB", numRows = 1))