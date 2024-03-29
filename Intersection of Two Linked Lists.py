# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        link1 = headA
        link2 = headB
        while link1 != link2:
            link1 = link1.next if link1 else headB
            link2 = link2.next if link2 else headA
        return link1
       
        