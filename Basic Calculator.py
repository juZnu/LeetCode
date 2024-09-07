def calculate( s: str) -> int:
    stack = []

    for ele in s:
        if ele == ' ':
            continue
        if stack:
            if stack[-1] == '-':
                stack.pop()
                stack.append(int(stack.pop()) - int(ele))
            elif stack[-1] == '+':
                stack.pop()
                stack.append(int(stack.pop()) + int(ele))
            elif ele == ')':
                bracketValue = stack.pop()
                stack[-1] = bracketValue
            else:
                stack.append(ele)
        else:
            stack.append(ele)
    
    return stack[0]

        

print(calculate(s = "(1+(4+5+2)-3)+(6+8)"))