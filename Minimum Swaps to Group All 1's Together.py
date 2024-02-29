def minSwaps( data):
    count1 = sum(data)
    countWindow = sum(data[:count1])
    result = count1-countWindow
    i = 0
    for j in data[count1:]:
       countWindow -= data[i]
       i +=1
       countWindow += j
       result = min(result,count1-countWindow)
    return result
       

print(minSwaps(data =
[1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1]))