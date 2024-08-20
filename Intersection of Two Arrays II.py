class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = dict()
        for ele in nums1:
            hashmap[ele] = hashmap.get(ele,0) + 1
        
        result  = []
        for ele in nums2:
            if hashmap.get(ele,0):
                hashmap[ele] -= 1
                result.append(ele)

        return result