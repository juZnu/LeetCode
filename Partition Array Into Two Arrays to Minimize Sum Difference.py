class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        def helper(i, added, carry_sum, arr, carry_set):
            if i == len(arr):
                carry_set[added].add(carry_sum)
                return
            helper(i + 1, added + 1, carry_sum + arr[i], arr, carry_set)
            helper(i + 1, added, carry_sum, arr, carry_set)
        
        # Split the array into two halves
        set1, set2 = collections.defaultdict(set), collections.defaultdict(set)
        total_sum = sum(nums)
        # Generate all possible subset sums for each half
        helper(0, 0, 0, nums[:len(nums)//2], set1)
        helper(0, 0, 0, nums[len(nums)//2:], set2)
        
        half = len(nums) // 2
        
        # Sort the subset sums for efficient binary search
        for key in set2:
            set2[key] = sorted(set2[key])
        
        res = float('inf')
        
        # Find the minimum difference
        for index, arr in set1.items():
            for ele in arr:
                carry = (total_sum - ele -ele)//2
                pos = bisect_left(set2[half - index], carry)
                if pos < len(set2[half - index]):
                    sum_= ele +set2[half - index][pos]
                    res = min(res, abs(sum_ - (total_sum - sum_)))
                if pos > 0:
                    sum_= ele +set2[half - index][pos-1]
                    res = min(res, abs(sum_ - (total_sum - sum_)))
        
        return res