def dailyTemperatures(temperatures):
    stack = []
    result = [0] * len(temperatures)
    for index, value in enumerate(temperatures):
        while stack and value > stack[-1][0]:
            pop_value,pop_index = stack.pop()
            result[pop_index] = index - pop_index
        stack.append((value,index))
    return result
            
        
        
        