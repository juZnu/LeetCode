class Solution(object):
    def reverseList(self, head):
        next = None
        val = head
        nextVal = head
        while nextVal:
            nextVal = val.next
            val.next = next
            next = val
            val = nextVal
        return next