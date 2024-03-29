# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        carry = dummy
        nextVal = carry.next
        while nextVal:
            if nextVal.val == val:
                carry.next =nextVal.next
            else:
                carry = carry.next
            nextVal = carry.next
        return dummy.next
        