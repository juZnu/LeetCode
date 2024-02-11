class TimeMap(object):
    def __init__(self):
        self.hashMap = dict()

    def set(self, key, value, timestamp):
        if self.hashMap.get(key,0) == 0:
            self.hashMap[key] = []
        self.hashMap[key].append([value,timestamp])

    def get(self, key, timestamp):
        if not self.hashMap.get(key,0):
            return ''
        array = self.hashMap[key]
        i = 0
        j = len(array)-1
        result = ''
        while i<=j:
            middle = (i+j)//2
            if array[middle][-1] > timestamp:
                j = middle-1
            else:
                result = array[middle][0]
                i = middle +1
        return result
        
        


        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)