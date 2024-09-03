class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hashmap = collections.defaultdict(int)

        for ele in arr:
            hashmap[ele] += 1
        
        res  = []

        for key,v in hashmap.items():
            heapq.heappush(res,v)
        
        while k and res:
            count  = heapq.heappop(res)
            if count > k:
                heapq.heappush(res,count-k)
                k = count
            k -= count

        return len(res)
            

        