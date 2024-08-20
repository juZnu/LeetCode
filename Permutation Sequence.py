def getPermutation( n: int, k: int) -> str:
    memo = {0:1}
    for i in range(1,n+1):
        memo[i]= memo[i-1]*i
    def helper(numArray,count):
        if not numArray:
            return ''
        res = ''
        n_fact = memo[len(numArray)-1]
        carry = 0
        for i in range(len(numArray)):
            if carry+n_fact >= count:
                res = numArray[i] + helper(numArray[:i]+numArray[i+1:],count- carry)
                break
            carry += n_fact
        return res
    return helper([str(i) for i in range(1,n+1)],k)

print(getPermutation(4,9))
