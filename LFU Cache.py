class Node:
    def __init__(self,key=None,val=None,prev=None,next=None):
        self.key = key
        self.val = val
        self.count = 0
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.tail.prev,self.head.next = self.head,self.tail
    
    def addNode(self,node):
        prev_,next_ = self.tail.prev,self.tail
        node.next,node.prev = next_,prev_
        prev_.next,next_.prev = node,node
    
    def delNode(self,node):
        prev_,next_ = node.prev,node.next
        prev_.next,next_.prev = next_,prev_
        node.prev,node.next = None,None
        
    
    def delHead(self):
        node = self.head.next
        self.delNode(node)
        return node

    def isEmpty(self):
        return self.head.next == self.tail

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFreq = 0
        self.hashmap = {}
        self.countMap = {}
       
    def incCount(self,node):
        prevCount = node.count
        node.count += 1
        curCount = node.count

        if curCount not in self.countMap:
            self.countMap[curCount] = DoubleLinkedList()
        curCountDLL = self.countMap[curCount]

        if prevCount == 0:
            self.minFreq = 1
        else:
            prevCountDLL = self.countMap[prevCount]
            prevCountDLL.delNode(node)
            if prevCountDLL.isEmpty():
                del self.countMap[prevCount]
                if prevCount== self.minFreq:
                    self.minFreq = curCount

        curCountDLL.addNode(node)


    def removeLeastUsed(self):
        leastUsedDLL = self.countMap[self.minFreq]
        node =leastUsedDLL.delHead()
        del self.hashmap[node.key]
        if leastUsedDLL.isEmpty():
            del self.countMap[self.minFreq]
            self.minFreq = 0

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.incCount(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return  
        node = None

        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
        elif len(self.hashmap) == self.capacity:
            self.removeLeastUsed()

        if key not in  self.hashmap:
            node = Node(key,value)
            self.hashmap[key] = node

        self.incCount(node)
