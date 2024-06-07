# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
            begin = None
            end = None
            k = 0
            carry = list1
            while k <= b:
                if k == a-1:
                    begin = carry
                carry = carry.next
                k += 1

            end = carry
            begin.next =list2

            while list2.next:
                list2 = list2.next
            
            list2.next = end
            
            return list1


