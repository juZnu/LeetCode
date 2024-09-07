# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,node1,node2):
            dummy = ListNode()
            carry = dummy
            while node1 and node2:
                if node1.val < node2.val:
                    carry.next = node1
                    node1 = node1.next
                else:
                    carry.next = node2
                    node2 = node2.next
                carry = carry.next
            carry.next = node1 or node2
            return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next :
            return head

        dummy = ListNode(0,head)
        fp,sp = dummy,dummy

        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next

        head1,head2 = head,sp.next 
        sp.next = None
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        return self.merge(head1,head2)
        
        