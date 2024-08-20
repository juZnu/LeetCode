# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        res = 0
        nums = set(nums)

        while head:
            if head.val in nums:
                nums.remove(head.val)
                
                while head.next and head.next.val in nums:
                    head = head.next
                    nums.remove(head.val)

                res += 1

            head = head.next

        return res
        