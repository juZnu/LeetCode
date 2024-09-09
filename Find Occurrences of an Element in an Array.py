class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] == x:hashmap[len(hashmap)+1] = i

        res = []
        for query in queries:
            res.append(hashmap.get(query,-1))
        
        return res
