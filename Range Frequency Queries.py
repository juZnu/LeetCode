class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.hashmap = collections.defaultdict(list)
        for index in range(len(arr)):
            self.hashmap[arr[index]].append(index)
            
    def query(self, left: int, right: int, value: int) -> int:
        indexArray = self.hashmap.get(value,[])
        if not indexArray: return 0
        return bisect.bisect(indexArray,right) - bisect.bisect(indexArray,left-1) 
        
# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)