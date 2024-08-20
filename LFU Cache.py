class ListNode:
    def __init__(self, key, val=None, prev=None, next=None):
        self.key = key
        self.val = val if val is not None else key  # Handle 0 or None values properly
        self.count = 0
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, node):
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def addHead(self, node):
        if not self.head:
            self.addNode(node)
            return  # Stop further execution as the node is already added
        node.next = self.head
        self.head.prev = node
        self.head = node

    def addAfterNode(self, node, prevNode=None):
        if not prevNode:
            self.addHead(node)
        else:
            nextNode = prevNode.next
            node.prev = prevNode
            node.next = nextNode
            prevNode.next = node
            if nextNode:
                nextNode.prev = node

    def remove_head(self):
        if not self.head:
            return
        tmp = self.head
        self.head = tmp.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None  # List becomes empty
        tmp.next = None

    def remove_tail(self):
        if not self.tail:
            return
        tmp = self.tail
        self.tail = tmp.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None  # List becomes empty
        tmp.prev = None

    def removeNode(self, node):
        if node == self.head:
            self.remove_head()
        elif node == self.tail:
            self.remove_tail()
        else:
            nextNode, prevNode = node.next, node.prev
            if prevNode:
                prevNode.next = nextNode
            if nextNode:
                nextNode.prev = prevNode
            node.next, node.prev = None, None

class LFUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}  # Map from key to node
        self.count = {}  # Map from count to (count node, DoubleLinkedList)
        self.countList = DoubleLinkedList()  # Ordered list of counts
        self.capacity = capacity

    def addCountNode(self, count, countPrev):
        if count and count not in self.count:
            self.count[count] = (ListNode(count), DoubleLinkedList())
            if countPrev:
                self.countList.addAfterNode(self.count[count][0], self.count[countPrev][0])
            else:
                self.countList.addAfterNode(self.count[count][0])

    def removeCountNode(self, count):
        if count in self.count:
            countNode, dll = self.count[count]
            if not dll.head:  # Only remove the count node if the list is empty
                self.countList.removeNode(countNode)
                del self.count[count]
    
    def delete(self):
        leastCount = self.countList.head
        if not leastCount:  # Edge case if the list is empty
            return
        key = self.count[leastCount.key][1].head.key
        self.count[leastCount.key][1].remove_head()
        del self.hashmap[key]
        self.removeCountNode(leastCount.key)
            
    def addCount(self, node):
        prev_count = node.count
        node.count += 1
        pres_count = node.count

        if pres_count not in self.count:
            self.addCountNode(pres_count, prev_count)
        
        if prev_count: 
            self.count[prev_count][1].removeNode(node)
            self.removeCountNode(prev_count)

        self.count[pres_count][1].addNode(node)

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.addCount(self.hashmap[key])
            return self.hashmap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key not in self.hashmap:
            if len(self.hashmap) == self.capacity:
                self.delete()
            self.hashmap[key] = ListNode(key, value)
        else:
            node = self.hashmap[key]
            node.val = value
        
        node = self.hashmap[key]
        self.addCount(node)
