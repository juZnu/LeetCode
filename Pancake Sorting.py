class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr)-1,-1,-1):
            if arr[i]!= i+1:
                j = i
                while arr[j] != i+1:
                    j -= 1
                
                res.append(j+1)
                arr = arr[:j+1][::-1] + arr[j+1:]
                
                res.append(i+1)
                arr = arr[:i+1][::-1] +arr[i+1:]

        
        return res
        