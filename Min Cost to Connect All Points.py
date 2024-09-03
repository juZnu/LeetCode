class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = []
        pointMap = {(k[0],k[1]): v for v,k in enumerate(points)}
        unionArray = [-1 for _ in points]
        carry = 1
        res = 0
        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1,len(points)):
                x2,y2 = points[j]
                if x1 == x2 and y1 == y2: continue
                dist = abs(x1-x2) + abs(y1-y2)
                heapq.heappush(distances,(dist,(x1,y1),(x2,y2)))
    
        def parent(index):
            if unionArray[index] < 0 :
                return index
            unionArray[index] = parent(unionArray[index])
            return unionArray[index]
        
        def union(index1,index2):
            parent1 = parent(index1)
            parent2 = parent(index2)

            if parent1 == parent2:
                return False

            if unionArray[parent1] > unionArray[parent2]:
                unionArray[parent1] += unionArray[parent2]
                unionArray[parent2] = parent1
            else:
                unionArray[parent2] += unionArray[parent1]
                unionArray[parent1] = parent2
            
            return True
        
        while carry < len(points):
            distance,point1,point2 = heapq.heappop(distances)

            if union(pointMap[point1],pointMap[point2]):
                res += distance
                carry += 1

        return res

        