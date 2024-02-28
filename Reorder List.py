# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        sp = head
        fp = head.next
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        prev = None
        curr = sp.next
        sp.next = prev
        sp = prev
        while curr:
            temp = curr.next
            curr.next = sp
            prev = sp
            sp = curr
            curr = temp
        fp = head
        while sp:
            val1 = fp.next
            val2 = sp.next
            fp.next = sp
            sp.next = val1
            fp= val1
            sp = val2
            

        
            
        
