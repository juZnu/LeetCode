def SwapNumbers(num1,num2):
    num1, num2  = num1^num1^num2, num2^num1^num2
    return num1,num2

print(SwapNumbers(1,2))