from typing import List


def maximumWhiteTiles( tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        i,j = 0,0
        begin,end = 1,carpetLen
        
        start_i,end_i = tiles[i]
        start_j,end_j = tiles[j]
        res,carry = 0,0
        while j < len(tiles):
            while not (start_j <= end <= end_j):
                carry += end_j - start_j +1
                j += 1
                if j >= len(tiles):break
                start_j,end_j = tiles[j]
            
            carry += end - start_j + 1  
            res = max(res,carry)
            
            if j >= len(tiles):break
            
            begin += 1
            end += 1
            carry -= end - start_j +1

            if  begin  > end_i:
                i += 1
                j = i
                start_i,end_i = tiles[i]
                start_j,end_j = tiles[j]
                begin = start_i
                end = start_i + carpetLen-1
                carry = 0

        return res
print(maximumWhiteTiles(tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10))