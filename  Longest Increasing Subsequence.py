import bisect
from typing import List


def lengthOfLIS( nums: List[int]) -> int:
    lis = []
        
    for num in nums:
        # Find the position to replace or extend in the lis array
        pos = bisect.bisect_left(lis, num)
        
        # If pos is equal to the length of lis, append num (extend the sequence)
        if pos == len(lis):
            lis.append(num)
        else:
            # Otherwise, replace the element at index pos with num
            lis[pos] = num
            
    # The length of lis is the length of the longest increasing subsequence
    return len(lis)

print(lengthOfLIS([10,9,2,5,6,3,7,101,18]))