def containsDuplicate(self, nums):
    num_count = dict()
    for ele in nums:
        if num_count.get(ele,0):
            return True
        num_count[ele] = 1
    return False