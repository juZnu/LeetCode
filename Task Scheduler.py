import heapq
from typing import List


def leastInterval(tasks: List[str], n: int) -> int:
    hashMap = {}
    for ele in tasks:
        hashMap[ele] = hashMap.get(ele,0) + 1
    minheap = [-v for k,v in hashMap.items()]
    heapq.heapify(minheap)
    time = 0
    stack = []
    while minheap or stack:
        time+=1
        if minheap:
            ele = heapq.heappop(minheap)
            if ele+1:
                stack.append([ele+1,time+n])
        while stack and stack[0][1] == time:
            heapq.heappush(minheap,stack.pop(0)[0])
    return time

print(leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))    