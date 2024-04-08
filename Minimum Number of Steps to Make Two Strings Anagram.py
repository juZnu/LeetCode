class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hashmap = {}
        for ele in s:
            hashmap[ele] = hashmap.get(ele,0) + 1
        for ele in t:
            if hashmap.get(ele,0) :
                hashmap[ele] -= 1
        result = 0
        for k,v in hashmap.items():
            result += v
        return result       