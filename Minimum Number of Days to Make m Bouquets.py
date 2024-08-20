class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m*k > len(bloomDay): return -1

        maxDays = []
        monQueue = collections.deque()

        for i in range(k):
            while monQueue and monQueue[-1] < bloomDay[i]:
                monQueue.pop()
            monQueue.append(bloomDay[i])
        maxDays.append(monQueue[0])

        for i in range(k,len(bloomDay)):
            while monQueue and monQueue[-1] < bloomDay[i]:
                monQueue.pop()
            monQueue.append(bloomDay[i])
            if monQueue[0] == bloomDay[i-k]: 
                monQueue.popleft()
            maxDays.append(monQueue[0])
        
        def canMakeBoquets(num,m):
            i = 0
            while i < len(maxDays) and m:
                if maxDays[i]<=num:
                    i +=k
                    m -= 1
                else:
                    i += 1
            return not m

        l =1
        r = max(bloomDay)

        while l < r:
            mid = l+((r-l)//2)
            if canMakeBoquets(mid,m):
                r = mid
            else:
                l = mid+1

        return l




        