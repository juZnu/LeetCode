class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        aliceUF = [-1 for _ in range(n+1)]
        bobUF = [-1 for _ in range(n+1)]
        res = 0

        def parent(arr,index):
            if arr[index] < 0:
                return index
            arr[index] = parent(arr,arr[index])
            return arr[index]

        def Union(arr,index1,index2):
            parent1 = parent(arr,index1)
            parent2 = parent(arr,index2)
            if parent1 == parent2: return False

            if arr[parent1] > arr[parent2]:
                arr[parent1] = arr[parent1]+arr[parent2]
                arr[parent2] = parent1
            else:
                arr[parent2] = arr[parent1]+arr[parent2]
                arr[parent1] = parent2
            
            return True

        for route,index1,index2 in sorted(edges,key= lambda x: x[0], reverse=True):
            if route == 1:
                if not Union(aliceUF,index1,index2):
                    res += 1
            elif route == 2:
                if not Union(bobUF,index1,index2):
                    res += 1
            else:
                tmp1 = Union(aliceUF,index1,index2)
                tmp2 = Union(bobUF,index1,index2)
                res += 1 if not tmp1 and not tmp2 else 0
                
        alice_components = sum(1 for i in range(1, n + 1) if parent(aliceUF, i) == i)
        bob_components = sum(1 for i in range(1, n + 1) if parent(bobUF, i) == i)

        if alice_components > 1 or bob_components > 1:
            return -1

        return res

            

        
        