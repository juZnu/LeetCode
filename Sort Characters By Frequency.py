from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        max_heap = []
        ans = ""

        counter = Counter(s)
        for key in counter: 
            heapq.heappush(max_heap, (-counter[key], key))
        
        while max_heap: 
            freq, c = heapq.heappop(max_heap)
            ans += -freq*c
        
        return ans

        