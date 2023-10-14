def topKFrequent( nums, k):
    hash_dict = dict()
    for ele in nums:
        if hash_dict.get(ele,0):
            hash_dict[ele] += 1
        else:
            hash_dict[ele] = 1
    return_list = [[] for _ in range(len(nums))]
    for key,v in hash_dict.items():
        return_list[v-1].append(key)
    result = []
    i = -1

    while  k >0:
        if return_list[i]:
            for ele in return_list[i]:
                result.append(ele)
                k -= 1
        i -= 1
    return result