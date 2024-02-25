# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        result = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            carry,sum = divmod(val1+val2+carry,10)
            result.next = ListNode(sum)
            result = result.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        return dummy.next



            

        