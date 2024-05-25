def buyChoco( prices, money):
    
    index, minValue1 = min(enumerate(prices),key = lambda x: x[1])
    minValue2 = float('inf')
    
    for i in range(len(prices)):
        minValue2 = min(minValue2, prices[i]) if i != index else minValue2
        
    result = minValue2 + minValue1
    
    return  money - result if result <= money else money