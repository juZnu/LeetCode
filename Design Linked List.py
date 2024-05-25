class Node:
    def __init__(self,val= 0,next= None):
        self.val = val
        self.next = next
    def __str__(self):
        return "{"+str(self.val)+ ":" + str(self.next)+"}"

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        
        self.hashmap ={}

    def get(self, index):
        cur = self.head
        i = 0
        print(self.head)
        while i != index and cur:
            cur = cur.next
            i += 1
        return cur.val if cur else -1
        
    def addAtHead(self, val):
        self.head = Node(val,self.head)
        return
        
    def addAtTail(self, val):
        if not self.head : 
            self.addAtHead(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(val)

    def addAtIndex(self, index, val):
        if index  == 0:
            self.addAtHead(val)
        else:
            cur = self.head
            i = 0
            while i < index-1 and cur:
                cur = cur.next
                i += 1
            if cur :
                cur.next = Node(val,cur.next)
        

    def deleteAtIndex(self, index):
        if index == 0: 
            self.head = self.head.next
        else:
            cur = self.head
            i = 0
            while i < index-1 and cur:
                cur = cur.next
                i += 1
            if cur and cur.next:
                cur.next = cur.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)