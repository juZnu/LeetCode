from typing import List


def numberOfSubarrays( nums: List[int], k: int) -> int:
    arr = [-1]
    res = 0
    for i in range(len(nums)):
        if nums[i]%2:
            arr.append(i)

    arr.append(len(nums))
    l = 1
    print(arr)
    for r in range(k,len(arr)-1):
        res += (arr[l]-arr[l-1]) * (arr[r+1]-arr[r])
        l +=1
    return res

print(numberOfSubarrays([2044,96397,50143],1))