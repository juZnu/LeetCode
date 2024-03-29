# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        k1 = k-1
        front = head
        while k1:
            k1 -= 1
            front = front.next
        back = head
        end = front
        while end.next:
            back = back.next
            end = end.next
        front.val,back.val = back.val,front.val
        return head
        
        