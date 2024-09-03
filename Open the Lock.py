class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:return -1
        if '0000' == target :return 0
        deadends,beginSet,endSet = set(deadends),{'0000'},{target}
        dist = 0
        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet

            newSet = set()
            dist += 1
            for lock in beginSet:
                
                for index in range(4):
                    
                    val = int(lock[index])
                    prevLock = lock[:index] + str((val+1) if val < 9 else 0) +lock[index+1:]
                    newLock = lock[:index] + str((val-1) if val else 9) +lock[index+1:]
                    
                    if prevLock in endSet or newLock in endSet:
                        return dist
                    
                    if prevLock not in deadends:
                        deadends.add(prevLock)
                        newSet.add(prevLock)

                    if newLock not in deadends:
                        deadends.add(newLock)
                        newSet.add(newLock)
                    
                    
            beginSet = newSet
                
        return -1

        