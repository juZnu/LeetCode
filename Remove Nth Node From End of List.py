# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0,head)
        fp = head
        sp = dummy
        while n>0:
            fp = fp.next
            n -= 1
        while fp:
            fp = fp.next
            sp = sp.next
        sp.next = sp.next.next
        return dummy.next
        
        
        