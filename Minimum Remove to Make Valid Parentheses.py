class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        countOpen = 0
        for ele in s:
            if ele ==")":
                if countOpen > 0:
                    countOpen -= 1
                else:
                    ele = ''
            elif ele == "(":
                countOpen += 1
            stack.append(ele)
        reverseStack = []
        while countOpen:
            ele = stack.pop()
            if ele =="(":
                countOpen -= 1
                ele = ''
            reverseStack.append(ele)
        return ''.join(stack+reverseStack[::-1])