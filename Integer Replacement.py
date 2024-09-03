class Solution:
    def integerReplacement(self, n: int) -> int:
        memo={1:0,0:0}

        def move(i):
            if i in memo:return memo[i]

            if not i%2:
                memo[i] = 1+move(i//2)
            else:
                memo[i] = 2+ min(move((i-1)//2),move((i+1 )//2))
            
            return memo[i]
        
        return move(n)