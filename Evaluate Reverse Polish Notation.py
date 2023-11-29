def evalRPN( tokens):
        stack = []
        for i in tokens:
            if i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif i == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(i))
        return stack.pop()