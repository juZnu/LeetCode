from functools import lru_cache


def checkRecord( n: int) -> int:
    
    def helper(length,AbsentCount,LateCount):
        if length == n:
            return 1
        count = 0
        
        if LateCount < 3:
            count += helper(length+1,AbsentCount,LateCount+1)
            if  AbsentCount+1 < 2: count += helper(length+1,AbsentCount+1,LateCount)
            count += helper(length+1,AbsentCount,LateCount)
            
        else:
            if  AbsentCount+1 < 2: count += helper(length+1,AbsentCount+1,0)
            count += helper(length+1,AbsentCount,0)
            
        return count
        
    return helper(1,0,0) + helper(1,1,0) + helper(1,0,1)

print(checkRecord(1101))

            
            
        