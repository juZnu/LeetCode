# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(0,head)
        sp = dummy
        fp = dummy
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        if fp:
            next_n = sp.next
            sp.next = ListNode(0)
            sp = sp.next
            sp.next = next_n
        prev = None
        cur = sp
        nextVal = cur.next
        while cur:
            cur.next = prev
            prev = cur
            cur = nextVal
            nextVal = cur.next if cur else None
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True

            


        