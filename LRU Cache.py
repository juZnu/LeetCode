class Node:
    def __init__(self,key= None,value= None,prev=None,next=None):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = Node()
        self.tail = Node()
        self.head.next,self.tail.prev = self.tail,self.head


    def get(self, key: int) -> int:
        if key in self.hashmap:
            return self.hashmap[key].val
        return -1

    def remove(self,node):
        if not node.val : return
        prev_,next_ = node.prev,node.next
        prev_.next,next_.prev = next_,prev_
        node.next,node.prev = None,None

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
        elif len(self.hashmap) == self.capacity:
            node = self.head.next
            self.remove(node)
            del self.hashmap[node.key]

        if key not in self.hashmap:
            self.hashmap[key] = Node(key,value)

        node = self.hashmap[key]
        node.val = value
        prev_,next_ = self.tail.prev,self.tail
        node.prev,node.next = prev_,next_
        prev_.next,next_.prev = node,node

        
        
        
        

# Perform operations based on the test case
operations = ["LRUCache","put","put","get","put","get","put","get","get","get"]
arguments = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

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
