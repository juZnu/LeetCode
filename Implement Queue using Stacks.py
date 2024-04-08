class MyQueue:

    def __init__(self):
        self.stack = []
        self.i = -1

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.i == -1: self.i += 1
        
    def pop(self) -> int:
        if self.i == -1: return -1
        ele = self.stack[self.i]
        self.i += 1
        if self.i == len(self.stack) : 
            self.stack = []
            self.i = -1
        return ele
        

    def peek(self) -> int:
        return self.stack[self.i]
        

    def empty(self) -> bool:
        return True if self.i == -1 else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()