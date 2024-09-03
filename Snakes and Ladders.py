import collections
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()  # Reverse the board to simplify calculations
        n = len(board)
        end = n * n - 1  # Target cell (0-based)
        visited = set()

        queue = collections.deque()
        queue.append([0, 0, 0])  # Start at cell 0 with 0 moves

        def numToCell(num):
            r = num // n
            c = num % n if r % 2 == 0 else n - 1 - (num % n)
            return r, c

        def cellToNum(r, c):
            num = r * n
            num += c if r % 2 == 0 else n - 1 - c
            return num

        while queue:
            r, c, dist = queue.popleft()
            num = cellToNum(r, c)

            if num == end:  # If we reach the end cell, return the distance
                return dist

            for dice in range(1, 7):  # Try all possible dice rolls
                next_num = num + dice
                if next_num >= n * n:
                    continue

                new_r, new_c = numToCell(next_num)

                # If there's a snake or ladder, move to the destination cell
                if board[new_r][new_c] != -1:
                    next_num = board[new_r][new_c] - 1  # Convert to 0-based index
                    new_r, new_c = numToCell(next_num)

                if next_num not in visited:  # Only process unvisited cells
                    visited.add(next_num)
                    queue.append([new_r, new_c, dist + 1])

        return -1  # If there's no way to reach the end, return -1