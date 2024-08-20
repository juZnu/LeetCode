class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        seq = collections.deque(range(1,n+1))

        def helper(players,i):
            if len(players) == 1:return players[0]

            while i != 1:
                players.append(players.popleft())
                i -= 1

            seq.popleft()
            return helper(players,k)
            
        return helper(seq,k)