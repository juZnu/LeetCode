import heapq


def findMaximizedCapital( k, w, profits, capital):
    capitalProfit = sorted([(c,-p) for c,p in zip(capital,profits)],reverse=True)
    pq = []
    
    while k and capitalProfit:
        while capitalProfit and abs(capitalProfit[-1][0])<= w :
            ele = capitalProfit.pop()
            heapq.heappush(pq,ele[-1])
        w += abs(heapq.heappop(pq)) 
        k -= 1
        
    while pq and k:
        w += abs(heapq.heappop(pq))
        k -= 1
        
    return w

print(findMaximizedCapital(1,0,[1,2,3],[1,1,2]))

            
            
        