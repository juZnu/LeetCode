from collections import deque
import heapq


def reorganizeString( s):
    hashMap = {}
    for ele in s:
        hashMap[ele] = hashMap.get(ele,0) + 1
    pqueue = [[-v,k] for k,v in hashMap.items()]
    heapq.heapify(pqueue)
    result  = []
    stack = deque()
    while pqueue:
        ele = heapq.heappop(pqueue)
        ele[0] += 1
        result.append(ele[1])
        if ele[0]:
            stack.append((len(result)+1,ele))
        if stack and stack[0][0] == len(result):
            stackele = stack.popleft()
            heapq.heappush(pqueue,stackele[1])
    return ''.join(result) if not stack else ''
    
print(reorganizeString(s = "aab"))
    