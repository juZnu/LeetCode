class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,-1),(-1,0),(0,1),(1,0)]
        length = len(word)
        m , n = len(board) , len(board[0])

        def dfs(i,j,index):
            if board[i][j] != word[index]: 
                return False
            if index +1 == length:
                return True

            temp = board[i][j]
            board[i][j] = "#"
            res = False
            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < m and 0 <= new_j < n and board[new_i][new_j] != "#":
                    res |= dfs(new_i, new_j, index + 1)

            board[i][j] = temp
            return res

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):return True

        return False


            
            
