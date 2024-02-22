from functools import cmp_to_key

def largestNumber( nums):
    nums = [ str(ele) for ele in nums]
    def sortingTechnique(n1,n2):
        if n1+n2 > n2+n1:
            return -1
        else: 
            return 1
    nums.sort(key = cmp_to_key(sortingTechnique))
    return str(int(''.join(nums)))
print(largestNumber(nums = [10,2]))