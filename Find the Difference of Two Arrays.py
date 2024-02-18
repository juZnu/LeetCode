def findDifference(self, nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    nums1 = [ele for ele in set1 if ele not in set2]
    nums2 = [ele for ele in set2 if ele not in set1]
    return [nums1,nums2]
    