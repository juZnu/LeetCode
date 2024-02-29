# Define the LRUCache class and Node class
class Node:
    def __init__(self, key=0, value=0, prev=None, next_=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next_

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashMap = {}
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head 
        
    def insert(self,key,value):
        node= Node(key,value)
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        self.hashMap[key] = node
        
    def remove(self,key):
        node = self.hashMap[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.hashMap[key]
        
    def get(self, key):
        if key in self.hashMap:
            value = self.hashMap[key].value
            self.remove(key)
            self.insert(key,value)
            return value
        return -1

    def put(self, key, value):
        if key in self.hashMap:
            self.remove(key)
        elif len(self.hashMap) == self.capacity:
            self.remove(self.head.next.key)
        self.insert(key,value)
        
        
        
        

# Perform operations based on the test case
operations = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
arguments = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

# Initialize the LRUCache object
obj = None
result = []
for op, args in zip(operations, arguments):
    if op == "LRUCache":
        obj = LRUCache(*args)
        result.append(None)
    elif op == "put":
        obj.put(*args)
        result.append(None)
    elif op == "get":
        result.append(obj.get(*args))

print(result)  # Print the result of each operation
