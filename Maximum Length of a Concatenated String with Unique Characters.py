class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = [0]
        def backTracking(i,hashSet):
            if i == len(arr):
                res[0] = max(res[0],len(hashSet))
                return
            backTracking(i+1,hashSet)
            copySet = hashSet.copy()
            cont = True
            for char in arr[i]:
                if char in copySet:
                    cont  = False
                    copySet = hashSet.copy()
                    break
                copySet.add(char)
            if cont:backTracking(i+1,copySet)

        backTracking(0,set())
        return res[0]


        
        



        