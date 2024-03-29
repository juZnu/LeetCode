# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def pairSum(self, head):
        sp = head
        fp = head.next
        maxSum = 0
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        sp.next = ListNode(0,sp.next)
        sp = sp.next
        prev = None
        cur = sp
        while cur:
            tmp = cur.next
            cur.next = prev 
            prev = cur
            cur = tmp
        while head and prev:
            maxSum = max(maxSum, head.val+prev.val)
            head = head.next
            prev = prev.next
        return maxSum