def combine( n: int, k: int):
    result = []
    def combinations(carry,i):
        if len(carry) == k:
            result.append(carry.copy())
            return
        for ele in range(i+1,n+1):
            carry.append(ele)
            combinations(carry ,ele)
            carry.pop()
    combinations([],0)
    return result

print(combine(n = 4, k = 2))