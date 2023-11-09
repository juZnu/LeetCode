def removeElement( nums, val):
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                count += 1
                i += 1
                continue
            nums[i-count] = nums[i]
            i += 1
        return len(nums) - count