from typing import List

def visibleMountains( peaks: List[List[int]]) -> int:
    
    def areaOfTraingle(point1, point2,point3):
        x1,y1 = point1
        x2,y2 = point2
        x3,y3 = point3
        return abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2
    
    def pointInTriangle(point1,point2,point3,point):
        return (areaOfTraingle(point1,point2,point) + 
                areaOfTraingle(point2,point3,point) +
                areaOfTraingle(point3,point1,point) ) ==  areaOfTraingle(point1,point2,point3)

    
    peaks = [(x,y) for x,y in peaks]
    peaks.sort(key=lambda x: (x[0],-x[1]))
    peaks.sort()
    frontset = set()
    backset = set()
    i = 0
    j = len(peaks)-1
    while i< len(peaks):
        carryI = i
        point  = peaks[i]
        base1 = (point[0]-point[1],0)
        base2 = (point[0]+point[1],0)
        cond = True
        while i < len(peaks)-1 and pointInTriangle(point,base1,base2,peaks[i+1]):
            if peaks[i+1]== point: cond = False
            i += 1
        i += 1
        if cond:frontset.add(peaks[carryI])
    
    while j>= 0:
        carryJ = j
        point  = peaks[j]
        base1 = (point[0]-point[1],0)
        base2 = (point[0]+point[1],0)
        cond = True
        while j >0 and pointInTriangle(point,base1,base2,peaks[j-1]):
            if peaks[j-1]== point: cond = False
            j -= 1
        j -= 1
        if cond :backset.add(peaks[carryJ])
        
    
    return len(frontset.intersection(backset))
    

print(visibleMountains(peaks = [[2,2],[6,3],[5,4]]))
print(visibleMountains(peaks = [[2,2],[2,2],[3,1]]))