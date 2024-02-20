# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        result = ListNode()
        carryResult = result
        while list1 and list2:
            val1 = list1.val if list1 else float('inf')
            val2 = list2.val if list2 else float('inf')
            if val1 <= val2:
                carryResult.next =  ListNode(val1)
                list1 = list1.next
            else:
                carryResult.next =  ListNode(val2)
                list2 = list2.next
            carryResult = carryResult.next
        carryResult.next = list1 or list2
        return result.next if result.next else ListNode('')



        