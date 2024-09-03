import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_row, max_col = len(heights) - 1, len(heights[0]) - 1
        
        # Priority queue initialized with the starting point (0,0) and effort 0
        queue = [(0, 0, 0)]
        
        # 2D difference array initialized with infinity
        difference = [[float('inf')] * len(heights[0]) for _ in range(len(heights))]
        difference[0][0] = 0
        
        while queue:
            diff, i, j = heapq.heappop(queue)
            
            # If we reached the bottom-right corner, return the difference
            if i == max_row and j == max_col:
                return diff
            
            # Explore the neighbors
            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy
                
                if 0 <= new_i <= max_row and 0 <= new_j <= max_col:
                    # Calculate the effort to move to the neighboring cell
                    abs_diff = abs(heights[i][j] - heights[new_i][new_j])
                    new_diff = max(diff, abs_diff)
                    
                    # If this path is better, update and push to the queue
                    if new_diff < difference[new_i][new_j]:
                        difference[new_i][new_j] = new_diff
                        heapq.heappush(queue, (new_diff, new_i, new_j))
        
        return difference[max_row][max_col]
