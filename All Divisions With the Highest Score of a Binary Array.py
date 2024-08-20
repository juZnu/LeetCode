class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        hashmap = collections.defaultdict(list)
        total_one = sum(nums)
        total_zero = 0
        
        for index in range(len(nums)):
            score = total_one+total_zero
            hashmap[score].append(index)
            total_one -= nums[index]
            total_zero += 1 if not nums[index] else 0

        score = total_one+total_zero
        hashmap[score].append(len(nums))

        return hashmap[max(hashmap.keys())]
        