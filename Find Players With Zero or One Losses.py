from typing import List


def findWinners( matches: List[List[int]]) -> List[List[int]]:
        hashmap = {}
        for k,v in matches:
            if not hashmap.get(k,0): hashmap[k] = 0
            hashmap[v] = hashmap.get(v,0) + 1
        result = [[],[]]
        sorted_keys = sorted(hashmap.keys())
        for k in sorted_keys:
            if not hashmap[k]:
                result[0].append(k)
            elif hashmap[k] == 1:
                result[1].append(k)
        return result