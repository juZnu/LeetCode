from typing import List


def calPoints( operations: List[str]) -> int:
    stack = []
    for ele in operations:
        try:
            value = int(ele)
            stack.append(value)
        except:
            if ele =="D":
                stack.append(stack[-1] * 2)
            elif ele == 'C':
                stack.pop()
            elif ele == '+':
                stack.append(stack[-1]+ stack[-2])
    return sum(stack)
                