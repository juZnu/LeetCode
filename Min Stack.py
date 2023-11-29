class MinStack(object):

    def __init__(self):
        self.stack = []
        self.Min = float('infinity')
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        self.Min = val if val <self.Min else self.Min
        return None
        
    def pop(self):
        value  = self.stack[-1]
        self.stack.pop()
        if self.Min == value:
            self.Min = min(self.stack) if self.stack else float('infinity')
        return None
        
    def top(self):
        return self.stack[-1]
        
    def getMin(self):
        return self.Min
