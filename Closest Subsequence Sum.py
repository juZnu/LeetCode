class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def helper(i,carry_sum,arr,carry_set):
            if i == len(arr):
                carry_set.add(carry_sum)
                return 
            helper(i+1,carry_sum+arr[i],arr,carry_set)
            helper(i+1,carry_sum,arr,carry_set)

        set1,set2 = set(),set()

        helper(0,0,nums[:len(nums)//2],set1)
        helper(0,0,nums[len(nums)//2:],set2)

        set2 = sorted(set2)

        res = 10**10

        for ele in set1:
            diff = goal-ele
            index = bisect_left(set2,diff)
            if index < len(set2):
                res = min(res,abs(diff-set2[index]))
            res = min(res,abs(diff-set2[index-1]))
        return res

        