# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if  (not head) or (not head.next) : return head
        
        length = 0
        fp = head

        while fp:
            fp = fp.next
            length += 1

        rotate = length - (k % length)

        if rotate == length : return head

        dummy = ListNode(0)
        dummy.next = head
        copy_ = dummy

        while rotate :
            copy_ = copy_.next
            rotate -= 1

        end = copy_
        start = copy_.next

        while copy_.next:
            copy_ = copy_.next
        
        dummy.next = start
        copy_.next = head
        end.next = None
        
        return dummy.next
        