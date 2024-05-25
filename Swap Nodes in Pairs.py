# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        def swap(start):
            prev = None
            cur = start
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur 
                cur = tmp
            return prev,start
        dummy = ListNode(0,head)
        carry = dummy
        while carry.next:
            prev = carry
            i = 0
            while prev and i !=2:
                i += 1
                prev = prev.next
            if not prev: break
            end = prev.next
            prev.next = None
            startfront, endfront = swap(carry.next)
            carry.next = startfront
            endfront.next = end
            carry = endfront
        return dummy.next