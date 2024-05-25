import  collections
def subArrayRanges(nums):
    result = 0
    maxQueue = collections.deque()
    minQueue = collections.deque()  
    
    for i in range(len(nums)):
        while maxQueue and maxQueue[-1][0] <= nums[i]:
            ele = maxQueue.pop()
            left = maxQueue[-1][-1] if maxQueue else -1
            mid = ele[1]
            result += ele[0] * (mid-left) * (i - mid)
            
        while minQueue and minQueue[-1][0] >= nums[i]:
            ele = minQueue.pop()
            left = minQueue[-1][-1] if minQueue else -1
            mid = ele[1]
            result -= ele[0] * (mid-left) * (i - mid)
        
        maxQueue.append([nums[i],i])
        minQueue.append([nums[i],i])
            
    right = len(nums)
    
    while maxQueue:
        ele = maxQueue.pop()
        left = maxQueue[-1][-1] if maxQueue else -1
        mid = ele[1]
        result += ele[0] * (mid-left) * (right - mid)
        
    while minQueue:
        ele = minQueue.pop()
        left = minQueue[-1][-1] if minQueue else -1
        mid = ele[1]
        result -= ele[0] * (mid-left) * (right - mid)
        
    return result

print(subArrayRanges(nums = [4,-2,-3,4,1]))

print(subArrayRanges(nums = [1,2,3]))