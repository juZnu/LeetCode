class Solution(object):
    def maxDistance(self, position, m):
        position.sort()
    
        # Define the binary search range
        l = 1
        r = position[-1] - position[0]

        def checkPossible(distance, m):
            # Place the first ball at the first position
            count = 1
            last_position = position[0]
            
            for pos in position[1:]:
                if pos - last_position >= distance:
                    count += 1
                    last_position = pos
                    if count >= m:
                        return True
            return False

        while l < r:
            mid = (l + r + 1) // 2  # Try the middle distance
            if checkPossible(mid, m):
                l = mid  # If it is possible to place all balls with at least `mid` distance
            else:
                r = mid - 1  # If not possible, reduce the distance

        return l