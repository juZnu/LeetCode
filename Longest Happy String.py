class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a:heapq.heappush(pq,(-a,'a'))
        if b:heapq.heappush(pq,(-b,'b'))
        if c:heapq.heappush(pq,(-c,'c'))

        res = []

        while pq:
            count, ele = heapq.heappop(pq)

            if count == -2 or count == -1:
                res.append(ele* (-count))
                continue

            res.append(ele*2)
            count += 2
            
            if pq  and count <=pq[0][0]:
                count2, ele2 = heapq.heappop(pq)
                count2 += 1
                res.append(ele2)
                if count2: heapq.heappush(pq,(count2,ele2))
                if count:heapq.heappush(pq,(count,ele))
            elif pq:
                heapq.heappush(pq,(count,ele))

        return ''.join(res)