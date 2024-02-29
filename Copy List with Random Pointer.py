# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        copy = {None:None}
        curr = head
        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy[curr].next = copy[curr.next]
            copy[curr].random = copy[curr.random]
            curr = curr.next
        return copy[head]
        
        