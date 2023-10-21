def isValid(s):
    dict_ = {
        '{' : '}',
        "[" : ']',
        '(' : ')'
    }
    stack = []
    for i in s:
        if dict_.get(i,0):
            stack.append(i)
        elif stack and dict_.get(stack[-1],0) == i:
            stack.pop()
        else:
            return False
    return not stack
        
print(isValid('({[({[{]})]})'))     