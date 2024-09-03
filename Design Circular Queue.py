class MyCircularQueue(object):

    def __init__(self, k):
        self.array = []
        self.length = k
        

    def enQueue(self, value):
        if self.length > len(self.array):
            self.array.append(value)
            return True
        return False
        

    def deQueue(self):
        if self.array:
            self.array.pop()
            return True
        return False
        

    def Front(self):
        return self.array[0] if self.array else -1
        

    def Rear(self):
        return self.array[-1] if self.array else -1
        

    def isEmpty(self):
        return not self.array
        

    def isFull(self):
        return len(self.array) == self.length
        
