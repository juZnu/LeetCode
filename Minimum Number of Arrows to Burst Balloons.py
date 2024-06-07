from typing import List


def findMinArrowShots( points: List[List[int]]) -> int:
    points.sort()
    result = 1
    start = points[0][0]
    end = points[0][1]
    for i,j in points[1:]:
        if i > end:
            result += 1
            start = i
            end = j
        else:
            end = min(end,j)
    return result

print(findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]]))