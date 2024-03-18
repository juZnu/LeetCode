from collections import deque
class Solution(object):
    def timeTaken(self, arrival, state):
        exitPool,enterPool = deque(),deque()
        Doorstate =  1
        curTime = arrival[0]
        result = [0 for _ in range(len(arrival))]
        time  = arrival[0]
        i = 0
        usedPrev = False
        while curTime <= len(arrival) or exitPool or enterPool:
            while i < len(state) and curTime == arrival[i]:
                
                if state[i] == 0:
                    enterPool.append(i)
                else:
                    exitPool.append(i)
                i +=1
            curTime += 1
            while (exitPool or enterPool) and time != curTime :
                if Doorstate == 1 and exitPool:
                    usedPrev = True
                    ele = exitPool.popleft()
                    result[ele] = time
                    time += 1
                elif (not exitPool )and enterPool :
                    Doorstate =0
                    
                if Doorstate == 0 and enterPool:
                    usedPrev = True
                    ele = enterPool.popleft()
                    result[ele] = time
                    time += 1
                elif (not enterPool) and exitPool:
                    Doorstate = 1
            if not usedPrev:
                Doorstate = 1
            usedPrev = False
            time = curTime
        return result