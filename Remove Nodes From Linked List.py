# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            while node:
                next_ = node.next
                node.next = prev
                prev = node
                node = next_
            return prev
        head = reverse(head)
        node = head
        while node.next:
            if node.next.val < node.val:
                node.next = node.next.next
            else:
                node = node.next
        return reverse(head)
