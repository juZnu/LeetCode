class TimeMap(object):

    def __init__(self):
        self.hashMap = dict()

    def set(self, key, value, timestamp):
        if self.hashMap.get(key,0) == 0:
            self.hashMap[key] = []
        self.hashMap[key].append([value,timestamp])

    def get(self, key, timestamp):
        i = 0
        if not self.hashMap.get(key,0):
            return ''
        j = len(self.hashMap[key])-1
        while i<j+1:
            middle = (i+j)//2
            if self.hashMap[key][j][-1] > timestamp and self.hashMap[key][middle][-1] > timestamp:
                j = middle - 1
            elif self.hashMap[key][i][-1] < timestamp:
                i = middle + 1
            else:
                return self.hashMap[key][middle][0]
        return self.hashMap[key][j][0] if self.hashMap[key][j][-1]<= timestamp else self.hashMap[key][i][0] if self.hashMap[key][i][-1]<= timestamp else ''

        


        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)