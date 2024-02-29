def findDuplicate(nums):
    slow,fast = 0,0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if fast == slow:
            break
    fast = 0
    while fast!= slow:
        slow = nums[slow]
        fast = nums[fast]
    return slow