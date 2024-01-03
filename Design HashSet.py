class MyHashSet(object):

    def __init__(self):
        self.hashSet = dict()
        

    def add(self, key):
        if self.hashSet.get(key,0) == 0:
            self.hashSet[key] = 1

    def remove(self, key):
        if self.hashSet.get(key,0):
            del self.hashSet[key]
        
    def contains(self, key):
        return True if self.hashSet.get(key,0) else False
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)