from typing import List
def merge( nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    while m and n:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    while n > 0:
        nums1[n-1],nums2[n-1] = nums2[n-1],nums1[n-1]
        n -= 1
print(merge(nums1 = [[1,2,3,0,0,0]], m = 3, nums2 = [2,5,6], n = 3))
