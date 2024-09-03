# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fp = sp = head

        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next
            if fp == sp: break
        if not fp or not fp.next:
            return None
        while head != sp:
            head,sp = head.next,sp.next
        return head

        
        