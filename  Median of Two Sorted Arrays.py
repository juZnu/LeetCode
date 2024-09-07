
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        
        n, m = len(nums1), len(nums2)
        total = n+m
        left = total // 2
        low,high = 0, n

        while low <= high:
            mid1 = low + (high-low)//2
            mid2 = left - mid1

            left1 = nums1[mid1-1] if mid1 > 0 else float('-inf')
            right1 = nums1[mid1] if mid1 < n else float('inf')
            left2 = nums2[mid2-1] if mid2 > 0 else float('-inf')
            right2 = nums2[mid2] if mid2 < m else float('inf')

            if left1 <= right2 and left2 <= right1:
                if total %2:

                    return min(max(right1,left2),max(right2,left1))
                else:
                    return (max(left1,left2) + min(right1,right2) )/2

            elif left1 > right2:
                high = mid1 - 1
                
            else:
                low = mid1 + 1
            
        return 0
