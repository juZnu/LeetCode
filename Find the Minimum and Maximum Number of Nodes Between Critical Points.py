# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        i = 1
        minDist = float('inf')
        first = 0
        prev = 0
        pres = 0

        while head.next and head.next.next:
            if (head.next.val > head.val and head.next.val > head.next.next.val) or (head.next.val < head.val and head.next.val < head.next.next.val):
                if not first:first = i
                prev = pres
                pres = i
                minDist = min(minDist ,pres - prev if prev else minDist)
            i += 1
            head = head.next

        maxDist = -1 if pres == first else pres - first
        minDist = -1 if minDist == float('inf') else minDist

        return [minDist,maxDist]
        

        