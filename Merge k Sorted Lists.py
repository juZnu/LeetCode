# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortTwoLists(self,list1,list2):
        dummy = ListNode()
        result = dummy
        while list1 and list2:
            val1 = list1.val
            val2 = list2.val
            if val1 <= val2:
                dummy.next = ListNode(val1)
                list1 = list1.next
            else:
                dummy.next = ListNode(val2)
                list2 = list2.next
            dummy = dummy.next
        dummy.next = list1 or list2
        return result.next 
    def mergeKLists(self, lists):
        if len(lists) == 1:
            return lists[0]
        elif len(lists) == 0:
            return None

        mid = len(lists) // 2
        front = self.mergeKLists(lists[:mid])
        back = self.mergeKLists(lists[mid:])
        
        return self.sortTwoLists(front, back)

        

            

        
            
        